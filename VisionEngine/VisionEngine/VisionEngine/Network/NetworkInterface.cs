using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace VisionEngine.Network
{
    /// <summary>
    /// Handles all network Connections
    /// </summary>
    public class NetworkInterface
    {
        private TcpClient  clientSocket = new TcpClient();  //tcp object
        private NetworkStream serverStream;                 //socket connection to server
        private Semaphore networkInterfaceSemaphore;        

        /// <summary>
        /// Default constructor
        /// </summary>
        public NetworkInterface()
        {
            this.networkInterfaceSemaphore = new Semaphore(1, 1);
        }

        /// <summary>
        /// Connects client to server with the address and port provided
        /// </summary>
        /// <param name="Address"></param>
        /// <param name="Port"></param>
        /// <param name="cform"></param>
        public void Connect(string Address, int Port, ConnectionForm cform)
        {
            try
            {
                this.clientSocket.Connect(Address, Port);
                this.serverStream = clientSocket.GetStream();
                cform.Invoke(cform.formDelegate, new Object[] {"Connected"});
            }
            catch (ArgumentNullException)
            {
                cform.Invoke(cform.formDelegate, new Object[] {"Hostname not valid"});
            }
            catch (ArgumentOutOfRangeException)
            {
                cform.Invoke(cform.formDelegate, new Object[] {"The port parameter is not between MinPort and MaxPort."});
            }
            catch (SocketException e)
            {
                cform.Invoke(cform.formDelegate, new Object[] {"Socket returned: " + e.ErrorCode});
            }
            catch (ObjectDisposedException)
            {
                cform.Invoke(cform.formDelegate, new Object[] {"Server closed the connection"});
            }
        }

        /// <summary>
        /// sends data to the server
        /// </summary>
        /// <param name="Data"></param>
        public void Send(string Data)
        {
            try
            {
                networkInterfaceSemaphore.WaitOne();
                byte[] outStream = System.Text.Encoding.ASCII.GetBytes(Data);
                this.serverStream.Write(outStream, 0, outStream.Length);
                this.serverStream.Flush();
                networkInterfaceSemaphore.Release();
            }
            catch
            {

            }
        }

        /// <summary>
        /// receives data from the server and returns it as a string.
        /// keeps receiving data until <EOF> has been recieved
        /// </summary>
        /// <returns></returns>
        public string Recv()
        {
                networkInterfaceSemaphore.WaitOne();
                byte[] inStream = new byte[1024];
                string Data = string.Empty;

                while (!Data.Contains("<EOF>"))
                {
                    serverStream.Read(inStream, 0, 1024);
                    Data += Encoding.ASCII.GetString(inStream);
                    inStream = new byte[1024];
                }

                Data = Data.Replace("\0", "");

                int EOFIndex = Data.IndexOf("<EOF>");
                networkInterfaceSemaphore.Release();
                return Data.Substring(0, EOFIndex);

        }

        /// <summary>
        /// Disconnects the client from the server
        /// </summary>
        public void Disconnect()
        {
            networkInterfaceSemaphore.WaitOne();
            clientSocket.Close();
            serverStream.Close();
            clientSocket = null;
            serverStream = null;
            networkInterfaceSemaphore.Release();
        }

    }
}
