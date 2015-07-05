using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using System.Threading.Tasks;
using System.Threading;
using SpinDPWP.Controls;
using System.ComponentModel;
using Windows.UI.Core;

namespace SpinDPWP
{
    public partial class ControlRoom : PhoneApplicationPage
    {
        private bool RunStream = true;
        private Semaphore StreamSemaphore = new Semaphore(1,1);
        private Semaphore JoystickSemaphore = new Semaphore(1, 1);
        private DateTime LastBatteryRequest;

        public ControlRoom()
        {
            InitializeComponent();
            this.Joystick.StartJoystick();
            this.Init();
        }

        private async Task Init()
        {
           // await Task.Run(() => this.Stream());
            await Task.Run(() => this.Battery());
            await DataHandler.DH.ProcessCommand("move 10");
            //await DataHandler.DH.ProcessCommand("slen 145");

            string output1 = await DataHandler.DH.ProcessCommand("sdeg 30");
            string output2 = await DataHandler.DH.ProcessCommand("shgt 55");
            string output3 = await DataHandler.DH.ProcessCommand("slen 125");
        }

        public async Task Stream()
        {
            while (true)
            {
                this.StreamSemaphore.WaitOne();

                if (this.RunStream)
                {
                    Task<string> t = Task.Run(() => DataHandler.DH.ProcessCommand("gimg"));
                    ImageConverter.base64image(await t, this.CameraImage);
                }
                else
                {
                    break;
                }

                this.StreamSemaphore.Release();
            }
        }

        private void Joystick_NewCoordinates(object sender, EventArgs e)
        {
            Task t = Task.Run(()=> this.Move((MyCoordinates)e));
        }

        private async Task Move(MyCoordinates Coordinates)
        {
            if (!this.JoystickSemaphore.WaitOne(1500))
            {
                return;
            }

            //Set speed
            int Speed = (Convert.ToInt32(Coordinates.Speed) / 51);
            await DataHandler.DH.ProcessCommand("smul " + Speed);

            //Direction
            int Direction = Convert.ToInt32(Coordinates.Direction);
            if (Direction > 337 || Direction < 23)
            {
                Semaphore DisPatchSemaphore = new Semaphore(1, 1);
                DisPatchSemaphore.WaitOne();
                bool Turbo = false;
                Deployment.Current.Dispatcher.BeginInvoke(() =>
                {
                    Turbo = Convert.ToBoolean(this.TurboCheckbox.IsChecked);
                    DisPatchSemaphore.Release();
                });

                DisPatchSemaphore.WaitOne();
                DisPatchSemaphore.Release();

                if (Turbo)
                {
                    await DataHandler.DH.ProcessCommand("move 25");
                    await DataHandler.DH.ProcessCommand("smul " + 5);
                }
                else
                {
                    await DataHandler.DH.ProcessCommand("move 11");
                    await DataHandler.DH.ProcessCommand("smul " + Speed);
                    
                }
            }
            else if (Direction > 22 && Direction < 70)
            {
                await DataHandler.DH.ProcessCommand("move 12");
                await DataHandler.DH.ProcessCommand("smul " + Speed);
            }
            else if (Direction > 69 && Direction < 116)
            {
                await DataHandler.DH.ProcessCommand("move 13");
                await DataHandler.DH.ProcessCommand("smul " + Speed + 1);
            }
            else if (Direction > 115 && Direction < 163)
            {
                await DataHandler.DH.ProcessCommand("move 14");
                await DataHandler.DH.ProcessCommand("smul " + Speed);
            }
            else if (Direction > 162 && Direction < 210)
            {
                await DataHandler.DH.ProcessCommand("move 15");
                await DataHandler.DH.ProcessCommand("smul " + Speed);
            }
            else if (Direction > 209 && Direction < 255)
            {
                await DataHandler.DH.ProcessCommand("move 16");
                await DataHandler.DH.ProcessCommand("smul " + Speed);
            }
            else if (Direction > 254 && Direction < 302)
            {
                await DataHandler.DH.ProcessCommand("move 17");
                await DataHandler.DH.ProcessCommand("smul " + Speed + 1);
            }
            else if (Direction > 301 && Direction < 349)
            {
                await DataHandler.DH.ProcessCommand("move 18");
                await DataHandler.DH.ProcessCommand("smul " + Speed);
            }
            else
            {
                await DataHandler.DH.ProcessCommand("move 10");
            }

            this.JoystickSemaphore.Release();
        }

        private async Task Battery()
        {
            while (true)
            {
                if (DateTime.Now.Subtract(LastBatteryRequest).Minutes > 2)
                {
                    LastBatteryRequest = DateTime.Now;
                    string BatteryLevel = await BatteryController.GetBatteryLevel();

                    try
                    {
                        Deployment.Current.Dispatcher.BeginInvoke(() =>
                        {
                            this.BatteryLevel.Text = BatteryLevel;
                        });

                    }
                    catch (Exception)
                    {

                    }
                }
            }
        }

        private void Joystick_Stop(object sender, EventArgs e)
        {

        }

        protected override void OnBackKeyPress(System.ComponentModel.CancelEventArgs e)
        {
            e.Cancel = true;
        }

        private void Joystick_ManipulationCompleted(object sender, System.Windows.Input.ManipulationCompletedEventArgs e)
        {
            Task t = Task.Run(() => this.Stop());
        }

        private async Task Stop()
        {
            this.JoystickSemaphore.WaitOne();
            await DataHandler.DH.ProcessCommand("move 10");
            this.JoystickSemaphore.Release();
        }

        private void CheckBox_Checked(object sender, RoutedEventArgs e)
        {

        }

        public event PropertyChangedEventHandler PropertyChanged;
        void OnPropertyChanged(string propertyName)
        {
            PropertyChangedEventHandler handler = PropertyChanged;

            if (handler != null)
            {
                if (propertyName == "Image")
                {
                    Semaphore tempSemaphore = new Semaphore(1, 1);

                    Deployment.Current.Dispatcher.BeginInvoke(() =>
                    {
                        tempSemaphore.WaitOne();
                        handler(this, new PropertyChangedEventArgs(propertyName));
                        tempSemaphore.Release();
                    });

                    tempSemaphore.WaitOne();
                    tempSemaphore.Release();
                }
                else
                {
                    handler(this, new PropertyChangedEventArgs(propertyName));
                }

            }
        }

    }
}