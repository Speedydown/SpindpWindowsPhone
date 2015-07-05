using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using VisionEngine.Network;

namespace VisionEngine
{
    public partial class VisionEngineForm : Form
    {
        public delegate void UpdateImage(Bitmap Input);
        public UpdateImage UpdateImageDelegate;
        public delegate void BatteryUpdate(string BatteryText);
        public BatteryUpdate UpdateBatteryDelagate;
        public delegate void UpdateImageBalloon(string color, int index);
        public UpdateImageBalloon UpdateImageBalloonDelegate;
        private CommandHandler commandHandler;
        private ConnectionForm connectionForm;
        private GameControllerHandler gcHandler;
        private int ImageCount = 1;

        public VisionEngineForm(CommandHandler commandHandler, ConnectionForm connectionForm, GameControllerHandler gcHandler)
        {
            InitializeComponent();
            this.commandHandler = commandHandler;
            this.connectionForm = connectionForm;
            this.gcHandler = gcHandler;
            pictureBoxInput.SizeMode = PictureBoxSizeMode.StretchImage;
            UpdateImageDelegate = new UpdateImage(updateImages);
            UpdateBatteryDelagate = new BatteryUpdate(UpdateBattery);
        }

        private void updateImages(Bitmap Input)
        {
            this.pictureBoxInput.Image = Input;
        }

        private void UpdateBattery(string Input)
        {
            this.BatteryTextbox.Text = Input;
        }

        private void startStreamToolStripMenuItem_Click(object sender, EventArgs e)
        {
            commandHandler.startStream();
            startStreamToolStripMenuItem.Enabled = false;
            stopStreamToolStripMenuItem.Enabled = true;
        }

        private void stopStreamToolStripMenuItem_Click(object sender, EventArgs e)
        {
            commandHandler.stopStream();
            startStreamToolStripMenuItem.Enabled = true;
            stopStreamToolStripMenuItem.Enabled = false;
        }

        private void disconnectToolStripMenuItem_Click(object sender, EventArgs e)
        {
            commandHandler.disconnect();
            commandHandler.stopStream();
            connectionForm.Show();
            this.Dispose();
            
        }

        private void shutdownServerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            commandHandler.execute("shtd");
            commandHandler.stopStream();
            connectionForm.Dispose();
        }

        private void rebootServerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            commandHandler.execute("rebt");
            commandHandler.stopStream();
            connectionForm.Dispose();
        }

        private void infoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            InfoForm infoform = new InfoForm();
            infoform.Show();
        }

        private void exitServerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            commandHandler.execute("exit");
            commandHandler.stopStream();
            connectionForm.Dispose();
        }

        private void exitVisionEngineToolStripMenuItem_Click(object sender, EventArgs e)
        {
            commandHandler.disconnect();
            commandHandler.stopStream();
            connectionForm.Dispose();
            this.Dispose();
        }

        private void executeButton_Click(object sender, EventArgs e)
        {
            executeButton.Enabled = false;
            OutputTextbox.Text = commandHandler.execute(InputTextbox.Text);
            InputTextbox.Text = "";
            executeButton.Enabled = true;
        }

        private void enableCustomCommandsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (this.Height != 502)
            {
                this.Height = 502;
                enableCustomCommandsToolStripMenuItem.Text = "Disable custom commands";
            }
            else
            {
                this.Height = 420;
                enableCustomCommandsToolStripMenuItem.Text = "Enable custom commands";
            }
        }

        private void saveInputPictureToolStripMenuItem_Click(object sender, EventArgs e)
        {
            lock (pictureBoxInput.Image)
            {
                pictureBoxInput.Image.Save("Input" + ImageCount + ".jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
                ImageCount++;
            }
        }

        private void VisionEngineForm_Load(object sender, EventArgs e)
        {

        }

        private void balloon1_Click(object sender, EventArgs e)
        {

        }

        private void enableControllerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            gcHandler.enable();
            enableControllerToolStripMenuItem.Enabled = false;
            disableControllerToolStripMenuItem.Enabled = true;
        }

        private void disableControllerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            gcHandler.disable();
            enableControllerToolStripMenuItem.Enabled = true;
            disableControllerToolStripMenuItem.Enabled = false;
        }

        private void RaiseLegsButton_Click(object sender, EventArgs e)
        {
            commandHandler.execute("slen 75");
        }

        private void LowerLegsButton_Click(object sender, EventArgs e)
        {
            commandHandler.execute("slen 125");
        }



    }
}
