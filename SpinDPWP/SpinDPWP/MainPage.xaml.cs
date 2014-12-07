using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using SpinDPWP.Resources;
using System.Threading.Tasks;

namespace SpinDPWP
{
    public partial class MainPage : PhoneApplicationPage
    {
        public MainPage()
        {
            InitializeComponent();
            Task t = this.Connect();
        }

        public async Task Connect()
        {
            Task<string> t = Task.Run(() => DataHandler.DH.ProcessCommand("cllg"));
            string output = await t;

            NavigationService.Navigate(new Uri("/ControlRoom.xaml", UriKind.Relative));
        }
    }
}