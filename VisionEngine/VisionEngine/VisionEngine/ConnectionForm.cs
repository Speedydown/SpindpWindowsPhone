using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using VisionEngine.Network;

namespace VisionEngine
{
    public partial class ConnectionForm : Form
    {
        public delegate void UpdateForm(string result);
        public UpdateForm formDelegate;
        private NetworkInterface networkInterface;

        public ConnectionForm()
        {
            InitializeComponent();
            IPAdressTextbox.Text = "192.168.24.150"; //192.168.178.24
            PortTextbox.Text = "1337";
            CheckTextSizes();
            formDelegate = new UpdateForm(UpdateFormAFterConnect);
        }

        private void IPAdressTextbox_TextChanged(object sender, EventArgs e)
        {
            CheckTextSizes();

        }

        private void PortTextbox_TextChanged(object sender, EventArgs e)
        {
            CheckTextSizes();
        }

        private void ConnectButton_Click(object sender, EventArgs e)
        {
            networkInterface = new NetworkInterface();
            IPAdressTextbox.Enabled = false;
            PortTextbox.Enabled = false;
            ConnectButton.Enabled = false;

            Thread t = new Thread(() => networkInterface.Connect(IPAdressTextbox.Text, Convert.ToInt32(PortTextbox.Text), this));
            t.Start();
        }

        public void UpdateFormAFterConnect(string result)
        {
            if (result == "Connected")
            {
                this.Hide();
                new CommandHandler(networkInterface, this);
            }
            else
            {
                ErrorLabel.Text = result;
                IPAdressTextbox.Enabled = true;
                PortTextbox.Enabled = true;
                ConnectButton.Enabled = true;
            }
        }

        private void CheckTextSizes()
        {
            string source = IPAdressTextbox.Text;
            int DotCount = source.Length - source.Replace(".", "").Length;

            //parse portnumber
            int Portnumber = 1337;           

            if (IPAdressTextbox.Text.Length > 7 && DotCount == 3 && IPAdressTextbox.Text[IPAdressTextbox.Text.Length -1] != '.' && int.TryParse(PortTextbox.Text, out Portnumber) && PortTextbox.Text.Length == 4)
            {
                ConnectButton.Enabled = true;
            }
            else
            {
                ConnectButton.Enabled = false;
            }

        }
    }
}
