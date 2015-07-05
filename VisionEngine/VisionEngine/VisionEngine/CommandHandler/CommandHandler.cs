using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using VisionEngine.Network;

namespace VisionEngine
{
    public class CommandHandler
    {
        private NetworkInterface networkInterface;
        private Thread streamThread;
        private Thread batteryThread;
        private VisionEngineForm visionEngine;
        private Semaphore commandHandlerSemaphore;
        private ConnectionForm connectionForm;
        private GameControllerHandler gcHandler;
        public CommandHandler(NetworkInterface networkInterface, ConnectionForm connectionForm)
        {
            this.gcHandler = new GameControllerHandler(this);
            this.connectionForm = connectionForm;
            this.networkInterface = networkInterface;
            this.visionEngine = new VisionEngineForm(this, connectionForm, gcHandler);
            this.commandHandlerSemaphore = new Semaphore(1, 1);
            this.visionEngine.Show();

            string output1 = this.execute("sdeg 30");
            string output2 = this.execute("shgt 55");
            string output3 = this.execute("slen 125");

            batteryThread = new Thread(() => CommandHandler.runBAttery(this, visionEngine));
            batteryThread.Start();

        }

        public void startStream()
        {
            streamThread = new Thread(() => CommandHandler.runStream(this, visionEngine));
            streamThread.Start();
        }

        public void stopStream()
        {
            commandHandlerSemaphore.WaitOne();
            if (streamThread != null)
            {
                streamThread.Abort();
            }
            commandHandlerSemaphore.Release(); 
        }

        public void disconnect()
        {
            networkInterface.Disconnect();
            connectionForm.UpdateFormAFterConnect("Disconnected");
        }

        public string execute(string Command)
        {
            commandHandlerSemaphore.WaitOne();
            networkInterface.Send(Command + "<EOF>");
            string output = networkInterface.Recv();
            commandHandlerSemaphore.Release();

            return output;
        }

        public static void runStream(CommandHandler commandHandler, VisionEngineForm visionEngine)
        {
            while (true)
            {

                byte[] bytes = Convert.FromBase64String(commandHandler.execute("gimg"));

                Image InputImage;
                using (MemoryStream ms = new MemoryStream(bytes))
                {
                    try
                    {
                        
                        InputImage = new Bitmap(Image.FromStream(ms));
                        visionEngine.Invoke(visionEngine.UpdateImageDelegate, new Object[] { InputImage });
                    }
                    catch (Exception)
                    {

                    }
                }
            }
        }

        public static void runBAttery(CommandHandler commandHandler, VisionEngineForm visionEngine)
        {
            while (true)
            {
                string BatteryText = commandHandler.GetBatteryLevel();
                visionEngine.Invoke(visionEngine.UpdateBatteryDelagate, new Object[] { BatteryText });
                Thread.Sleep(10000);
            }
        }

        public string GetBatteryLevel()
        {
            string Battery = this.execute("gspi");
            int BatteryLevelAsInt = 0;

            bool result = Int32.TryParse(Battery, out BatteryLevelAsInt);

            if (result == true)
            {
                float batVolt = ((BatteryLevelAsInt * 3.3f) / 1023f) * 4;
                float batPerc = (batVolt / 12.6f) * 100;
                return "Battery: " + Math.Round(batPerc).ToString() + " %";
            }
            else
            {
                return "Battery: " + "Error";
            }
        }

    }
}
