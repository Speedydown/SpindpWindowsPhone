﻿#pragma checksum "C:\Users\Teake\Documents\GitHub\SpindpWindowsPhone\SpinDPWP\SpinDPWP\Assets\Controls\Joystick.xaml" "{406ea660-64cf-4c82-b6f0-42d48172a799}" "BD9DD507D619C8EE7A6CAFFD848758C5"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.34014
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Automation.Peers;
using System.Windows.Automation.Provider;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Interop;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Imaging;
using System.Windows.Resources;
using System.Windows.Shapes;
using System.Windows.Threading;


namespace SpinDPWP.Controls {
    
    
    public partial class Joystick : System.Windows.Controls.UserControl {
        
        internal System.Windows.Controls.Grid LayoutRoot;
        
        internal System.Windows.Shapes.Ellipse ellipseMain;
        
        internal System.Windows.Controls.Grid ellipseButton;
        
        internal System.Windows.Shapes.Ellipse ellipseSense;
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Windows.Application.LoadComponent(this, new System.Uri("/SpinDPWP;component/Assets/Controls/Joystick.xaml", System.UriKind.Relative));
            this.LayoutRoot = ((System.Windows.Controls.Grid)(this.FindName("LayoutRoot")));
            this.ellipseMain = ((System.Windows.Shapes.Ellipse)(this.FindName("ellipseMain")));
            this.ellipseButton = ((System.Windows.Controls.Grid)(this.FindName("ellipseButton")));
            this.ellipseSense = ((System.Windows.Shapes.Ellipse)(this.FindName("ellipseSense")));
        }
    }
}

