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

namespace SpinDPWP
{
    public partial class ControlRoom : PhoneApplicationPage
    {
        private bool RunStream = true;
        private Semaphore StreamSemaphore = new Semaphore(1,1);
        private Semaphore JoystickSemaphore = new Semaphore(1, 1);

        public ControlRoom()
        {
            InitializeComponent();
           // this.Joystick.StartJoystick();
            this.Init();
        }

        private async Task Init()
        {
            await Task.Run(() => this.Stream());
            await DataHandler.DH.ProcessCommand("move 10");
            //await DataHandler.DH.ProcessCommand("slen 145");
            await DataHandler.DH.ProcessCommand("slen 90");
            await DataHandler.DH.ProcessCommand("shgt 55");
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
            if (!this.JoystickSemaphore.WaitOne(500))
            {
                return;
            }

            //Set speed
            int Speed = (Convert.ToInt32(Coordinates.Speed) / 51) + 1;
            await DataHandler.DH.ProcessCommand("smul " + Speed);

            //Direction
            int Direction = Convert.ToInt32(Coordinates.Direction);
            if (Direction > 337 || Direction < 23)
            {
                await DataHandler.DH.ProcessCommand("move 25");
            }
            else if (Direction > 22 && Direction < 70)
            {
                await DataHandler.DH.ProcessCommand("move 12");
            }
            else if (Direction > 69 && Direction < 116)
            {
                await DataHandler.DH.ProcessCommand("move 13");
            }
            else if (Direction > 115 && Direction < 163)
            {
                await DataHandler.DH.ProcessCommand("move 14");
            }
            else if (Direction > 162 && Direction < 210)
            {
                await DataHandler.DH.ProcessCommand("move 15");
            }
            else if (Direction > 209 && Direction < 255)
            {
                await DataHandler.DH.ProcessCommand("move 16");
            }
            else if (Direction > 254 && Direction < 302)
            {
                await DataHandler.DH.ProcessCommand("move 17");
            }
            else if (Direction > 301 && Direction < 349)
            {
                await DataHandler.DH.ProcessCommand("move 18");
            }
            else
            {
                await DataHandler.DH.ProcessCommand("move 10");
            }

            this.JoystickSemaphore.Release();
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

    }
}