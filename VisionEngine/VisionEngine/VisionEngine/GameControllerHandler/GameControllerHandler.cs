using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SharpDX.DirectInput;
using System.Threading;

namespace VisionEngine
{
    public class GameControllerHandler
    {
        private CommandHandler chandler;
        private Thread controllerThread;
        private Semaphore controllerSemaphore;

        // joystick joystick
        private Joystick joystick;
        // joystick left
        int move;
        // joystick right
        int spec;
        // dpad
        private int hwchange;
        // buttons
        private int buttons;

        // send string
        private string leftstick;
        private string rightstick;
        private string btncmd;
        private string dpdcmd;

        // help for input updates
        private float sec = DateTime.Now.Second;
        private string oldleftstick = "";
        private string oldrightstick = "";
        private string oldbtncmd = "";
        private string olddpdcmd = "";

        // dpad input
        private bool dpdbool = false;
        private int spdint = 1;
        private int degint = 10;

        private string smulstring;
        private string sdegstring;


        public GameControllerHandler(CommandHandler chandler)
        {
            this.chandler = chandler;
            this.controllerSemaphore = new Semaphore(1,1);

        }

        public void enable()
        {
            // Initialize DirectInput
            var directInput = new DirectInput();

            // Find a Gamepad Guid
            var gamepadGuid = Guid.Empty;

            DeviceType[] dtList = { DeviceType.Gamepad, DeviceType.Joystick, DeviceType.FirstPerson };
            IList<DeviceInstance> deviceInstanceList = null;

            foreach (DeviceType dt in dtList)
            {
                deviceInstanceList = directInput.GetDevices(dt, DeviceEnumerationFlags.AllDevices);

                if (deviceInstanceList.Count > 0)
                {
                    break;
                }
            }

            foreach (var deviceInstance in deviceInstanceList)
                gamepadGuid = deviceInstance.InstanceGuid;

            // Instantiate the gamepad
            joystick = null;

            try
            {
                joystick = new Joystick(directInput, gamepadGuid);
            }
            catch (Exception)
            {
                this.disable();
                return;
            }
            
            // Set BufferSize in order to use buffered data.
            joystick.Properties.BufferSize = 128;

            // Acquire the joystick
            joystick.Acquire();

            controllerThread = new Thread(() => run());
            controllerThread.Start();
        }

        public void disable()
        {
            controllerSemaphore.WaitOne();
            if (controllerThread != null)
            {
                controllerThread.Abort();
            }
            controllerSemaphore.Release();
        }

        public void run()
        {
            while (true)
            {
                controllerSemaphore.WaitOne();

                int state = getCurrentState().X;
                int state2 = getCurrentState().Y;

                #region Left Joystick
                //STOP
                if (getCurrentState().X > 25000 && getCurrentState().X < 40000 && getCurrentState().Y > 25000 && getCurrentState().Y < 40000)
                {
                    move = 10;
                }

                //LEFTFORWARD
                if (getCurrentState().X < 20000 && getCurrentState().Y < 20000)
                {
                    move = 18;
                }

                //FORWARD
                if (getCurrentState().Y < 15000 && getCurrentState().X > 25000 && getCurrentState().X < 35000)
                {
                    move = 11;
                }

                //RIGHTFORWARD
                if (getCurrentState().X > 45000 && getCurrentState().Y < 20000)
                {
                    move = 12;
                }

                //RIGHT
                if (getCurrentState().X > 45000 && getCurrentState().Y > 25000 && getCurrentState().Y < 40000)
                {
                    move = 13;
                }

                //RIGHTDOWN
                if (getCurrentState().X > 40000 && getCurrentState().Y > 40000)
                {
                    move = 14;
                }

                //DOWN
                if (getCurrentState().Y > 45000 && getCurrentState().X > 25000 && getCurrentState().X < 35000)
                {
                    move = 15;
                }

                //LEFTDOWN
                if (getCurrentState().X < 20000 && getCurrentState().Y > 40000)
                {
                    move = 16;
                }

                //LEFT
                if (getCurrentState().X < 20000 && getCurrentState().Y > 25000 && getCurrentState().Y < 40000)
                {
                    move = 17;
                }

                #endregion

                #region Right Joystick

                //STOP
                if (getCurrentState().Z > 25000 && getCurrentState().Z < 40000 && getCurrentState().RotationZ > 25000 && getCurrentState().RotationZ < 40000)
                {
                    spec = 10;
                }
                //LEFT
                if (getCurrentState().Z < 20000 && getCurrentState().RotationZ > 25000 && getCurrentState().RotationZ < 50000)
                {
                    spec = 24;
                }
                //FORWARD
                if (getCurrentState().RotationZ < 20000 && getCurrentState().Z > 25000 && getCurrentState().Z < 35000)
                {
                    spec = 25;
                }
                //RIGHT
                if (getCurrentState().Z > 45000 && getCurrentState().RotationZ > 25000 && getCurrentState().RotationZ < 50000)
                {
                    spec = 26;
                }

                #endregion

                #region DPAD

                if (getCurrentState().PointOfViewControllers[0] == 0 && dpdbool != true)
                {
                    getMul();
                    dpdbool = true;
                    hwchange = 1;
                    if (spdint <= 2)
                    {
                        spdint += 1;
                    }
                }

                if (getCurrentState().PointOfViewControllers[0] == 9000 && dpdbool != true)
                {
                    getDeg();
                    dpdbool = true;
                    hwchange = 2;
                    if (degint <= 25)
                    {
                        degint += 5;
                    }
                }

                if (getCurrentState().PointOfViewControllers[0] == 18000 && dpdbool != true)
                {
                    getMul();
                    dpdbool = true;
                    hwchange = 3;
                    if (spdint >= 2)
                    {
                        spdint -= 1;
                    }
                }

                if (getCurrentState().PointOfViewControllers[0] == 27000 && dpdbool != true)
                {
                    getDeg();
                    dpdbool = true;
                    hwchange = 4;
                    if (degint >= 15)
                    {
                        degint -= 5;
                    }
                }

                if (getCurrentState().PointOfViewControllers[0] == -1)
                {
                    dpdbool = false;
                    hwchange = 0;
                }

                #endregion

                #region Buttons

                if (getCurrentState().Buttons[0] == true)
                {
                    buttons = 1;
                }

                if (getCurrentState().Buttons[1] == true)
                {
                    buttons = 2;
                }

                if (getCurrentState().Buttons[2] == true)
                {
                    buttons = 3;
                }

                if (getCurrentState().Buttons[3] == true)
                {
                    buttons = 4;
                }

                // HORN
                if (getCurrentState().Buttons[10] == true)
                {
                    if (sec != DateTime.Now.Second)
                    {
                        sendCommand("horn");
                        sec = DateTime.Now.Second;
                    }
                }

                #endregion

                #region Get and Send Input
                getInputLeftJoyStick(move);
                getInputRightJoystick(spec);
                getInputDpad(hwchange);
                getInputButton(buttons);

                if (sec != (DateTime.Now.Second / 2) && rightstick != oldrightstick)
                {
                    sendCommand(rightstick);

                    sec = DateTime.Now.Second;

                    oldrightstick = rightstick;
                }

                if (sec != (DateTime.Now.Second / 2) && leftstick != oldleftstick)
                {
                    sendCommand(leftstick);

                    sec = DateTime.Now.Second;

                    oldleftstick = leftstick;
                }

                if (sec != (DateTime.Now.Second / 2) && dpdcmd != olddpdcmd)
                {
                    sendCommand(dpdcmd);

                    sec = DateTime.Now.Second;

                    olddpdcmd = dpdcmd;
                }

                if (sec != (DateTime.Now.Second / 2) && btncmd != oldbtncmd)
                {
                    sendCommand(btncmd);

                    sec = DateTime.Now.Second;

                    oldbtncmd = btncmd;
                }

                #endregion

                controllerSemaphore.Release();
                Thread.Sleep(1);
            }
        }

        public void getInputRightJoystick(int specInt)
        {
            switch (specInt)
            {
                case 10:
                    getRightJoystick("move " + specInt.ToString());
                    break;
                case 24:
                    getRightJoystick("move " + specInt.ToString());
                    break;
                case 25:
                    getRightJoystick("move " + specInt.ToString());
                    break;
                case 26:
                    getRightJoystick("move " + specInt.ToString());
                    break;
                default:
                    break;
            }
        }

        public void getInputLeftJoyStick(int moveInt)
        {
            switch (moveInt)
            {
                // stop
                case 10:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                // fw
                case 11:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                // rfw
                case 12:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                // r
                case 13:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                // rbw
                case 14:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                // bw
                case 15:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                // lbw
                case 16:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                // l
                case 17:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                //lfw
                case 18:
                    getLeftJoystick("move " + moveInt.ToString());
                    break;
                default:
                    break;
            }
        }

        public void getInputDpad(int mod)
        {
            switch (mod)
            {
                case 1:
                    getDpad("smul " + spdint.ToString());
                    break;
                case 2:
                    getDpad("sdeg " + degint.ToString());
                    break;
                case 3:
                    getDpad("smul " + spdint.ToString());
                    break;
                case 4:
                    getDpad("sdeg " + degint.ToString());
                    break;
                default:
                    break;
            }
        }

        public void getInputButton(int keys)
        {
            switch (keys)
            {
                case 1:
                    getButtons("btns");
                    break;
                case 2:
                    getButtons("btnx");
                    break;
                case 3:
                    getButtons("btno");
                    break;
                case 4:
                    getButtons("btnt");
                    break;
                default:
                    break;
            }
        }

        public void getRightJoystick(string command)
        {
            rightstick = command;
        }

        public void getLeftJoystick(string command)
        {
            leftstick = command;
        }

        public void getButtons(string command)
        {
            btncmd = command;
        }

        public void getDpad(string command)
        {
            dpdcmd = command;
        }

        public void sendCommand(string send)
        {
            chandler.execute(send);
        }

        public JoystickState getCurrentState()
        {
            try
            {
                return joystick.GetCurrentState();
            }
            catch (Exception e)
            {
                this.disable();
                return null;
            }
        }

        public void getMul()
        {
            smulstring = chandler.execute("gmul");
            spdint = Convert.ToInt16(smulstring);
        }

        public void getDeg()
        {
            sdegstring = chandler.execute("gdeg");
            spdint = Convert.ToInt16(sdegstring);
        }
    }
}
