using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media.Imaging;
using System.Windows.Threading;
using Windows.UI.Core;

namespace SpinDPWP
{
    public static class ImageConverter
    {
        public static void base64image(string base64string, Image image)
        {
            try
            {
                byte[] fileBytes = Convert.FromBase64String(base64string);
                Semaphore ImageSemaphore = new Semaphore(1, 1);
                BitmapImage bitmapImage = null;

                ImageSemaphore.WaitOne();

                Deployment.Current.Dispatcher.BeginInvoke(() =>
                {

                    using (MemoryStream ms = new MemoryStream(fileBytes, 0, fileBytes.Length))
                    {
                        ms.Write(fileBytes, 0, fileBytes.Length);
                        bitmapImage = new BitmapImage();
                        bitmapImage.SetSource(ms);
                        image.Source = bitmapImage;
                        ImageSemaphore.Release();
                    }
                });


                ImageSemaphore.WaitOne();
                ImageSemaphore.Release();


            }
            catch (Exception)
            {
            }
        }
    }
}
