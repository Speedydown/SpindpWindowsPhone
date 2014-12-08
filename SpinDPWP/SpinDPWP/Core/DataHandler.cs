using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Windows.Networking.Proximity;
using Windows.Networking.Sockets;
using Windows.Storage.Streams;

namespace SpinDPWP
{
    public class DataHandler
    {
        const string Port = "6";

        private static DataHandler _DH = null;
        public static DataHandler DH
        {
            get
            {
                if (_DH == null)
                {
                    _DH = new DataHandler();
                }

                return _DH;
            }
        }

        private Semaphore DataSemaphore = new Semaphore(1, 1);
        private StreamSocket Socket = null;

        public DataHandler()
        {

        }

        public bool isConnected()
        {
            return this.Socket != null;
        }

        private async Task Connect()
        {
            bool retry = false;

            this.DataSemaphore.WaitOne();

            if (this.isConnected())
            {
                return;
            }

            try
            {
                PeerFinder.AlternateIdentities["Bluetooth:Paired"] = "";
                var pairedDevices = await PeerFinder.FindAllPeersAsync();

                if (pairedDevices.Count == 0)
                {
                    return;
                }
                else
                {
                    PeerInformation selectedDevice = null;

                    foreach (PeerInformation pi in pairedDevices)
                    {
                        if (pi.DisplayName.Contains("pi"))
                        {
                            selectedDevice = pi;
                        }
                    }

                    if (selectedDevice == null)
                    {
                        return;
                    }

                    this.Socket = new StreamSocket();
                    await this.Socket.ConnectAsync(selectedDevice.HostName, "6");
                }
            }
            catch (Exception e)
            {
                if (e.Message.StartsWith("A socket operation was attempted to an unreachable network") || e.Message.StartsWith("A connection attempt failed because the connected party did not properly respond after a period of time"))
                {
                    this.Socket = null;
                    retry = true;
                    Thread.Sleep(500);
                }
            }

            try
            {
                this.DataSemaphore.Release();
            }
            catch
            {

            }

            if (retry)
            {
                await this.Connect();
            }
        }

        public async Task<string> ProcessCommand(string Command, bool SecondAttempt = false)
        {
            bool retry = false;
            string Output = string.Empty;
            //Connect
            if (!this.isConnected())
            {
                if (SecondAttempt)
                {
                    return "Not connected";
                }

                await this.Connect();
                return await this.ProcessCommand(Command, true);
            }

            //Handle Command
            bool TimedOut = !this.DataSemaphore.WaitOne(5000);

            if (TimedOut)
            {
                try
                {
                    this.DataSemaphore.Release();
                }
                catch
                {

                }
                Disconnect();
                return await this.ProcessCommand(Command);
            }

            try
            {
                if (!Command.Contains("<EOF>"))
                {
                    Command += "<EOF>";
                }

                DataWriter writer = new DataWriter(this.Socket.OutputStream);
                writer.WriteString(Command);

                await writer.StoreAsync();


                //Read response
                DataReader dr = new DataReader(this.Socket.InputStream);
                dr.InputStreamOptions = InputStreamOptions.Partial;

                while (!Output.Contains("<EOF>"))
                {
                    uint s = await dr.LoadAsync(512);


                    Output += dr.ReadString(s);

                    if (Output.Contains("/0"))
                    {
                        Output.Replace("/0", "");
                    }
                }

            }
            catch (ObjectDisposedException)
            {
                try
                {
                    this.DataSemaphore.Release();
                }
                catch
                {

                }

                this.Disconnect();
                retry = true;
                this.DataSemaphore.WaitOne();
            }
            catch (InvalidOperationException)
            {
                try
                {
                    this.DataSemaphore.Release();
                }
                catch
                {

                }

                this.Disconnect();
                retry = true;
                this.DataSemaphore.WaitOne();
            }
            catch (Exception)
            {

            }

            try
            {
                this.DataSemaphore.Release();
            }
            catch
            {

            }

            if (Output.Contains("<EOF>"))
            {
                Output = Output.Substring(0, Output.Length - 5);
            }

            if (retry)
            {
                return await this.ProcessCommand(Command);
            }

            return Output;

        }

        private void Disconnect()
        {
            this.DataSemaphore.WaitOne();

            try
            {
                this.Socket.Dispose();
                this.Socket = null;
            }
            catch (Exception)
            {

            }

            try
            {
                this.DataSemaphore.Release();
            }
            catch
            {

            }
        }
    }
}
