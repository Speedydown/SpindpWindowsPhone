using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpinDPWP
{
    public static class BatteryController
    {
        public static async Task<string> GetBatteryLevel()
        {
            string Battery = await DataHandler.DH.ProcessCommand("gspi");
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
