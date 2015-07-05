namespace VisionEngine
{
    partial class VisionEngineForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.disconnectToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitServerToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.shutdownServerToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.rebootServerToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitVisionEngineToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.streamToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.startStreamToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.stopStreamToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveInputPictureToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveOutputPictureToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.controllerToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.enableControllerToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.disableControllerToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.advancedToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.enableCustomCommandsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.infoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.InputTextbox = new System.Windows.Forms.TextBox();
            this.executeButton = new System.Windows.Forms.Button();
            this.OutputTextbox = new System.Windows.Forms.TextBox();
            this.pictureBoxInput = new System.Windows.Forms.PictureBox();
            this.RaiseLegsButton = new System.Windows.Forms.Button();
            this.LowerLegsButton = new System.Windows.Forms.Button();
            this.BatteryTextbox = new System.Windows.Forms.TextBox();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxInput)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(11, 26);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(31, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Input";
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.streamToolStripMenuItem,
            this.controllerToolStripMenuItem,
            this.advancedToolStripMenuItem,
            this.aboutToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1059, 24);
            this.menuStrip1.TabIndex = 9;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.disconnectToolStripMenuItem,
            this.exitServerToolStripMenuItem,
            this.shutdownServerToolStripMenuItem,
            this.rebootServerToolStripMenuItem,
            this.exitVisionEngineToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "File";
            // 
            // disconnectToolStripMenuItem
            // 
            this.disconnectToolStripMenuItem.Name = "disconnectToolStripMenuItem";
            this.disconnectToolStripMenuItem.Size = new System.Drawing.Size(166, 22);
            this.disconnectToolStripMenuItem.Text = "Disconnect";
            this.disconnectToolStripMenuItem.Click += new System.EventHandler(this.disconnectToolStripMenuItem_Click);
            // 
            // exitServerToolStripMenuItem
            // 
            this.exitServerToolStripMenuItem.Name = "exitServerToolStripMenuItem";
            this.exitServerToolStripMenuItem.Size = new System.Drawing.Size(166, 22);
            this.exitServerToolStripMenuItem.Text = "Exit server";
            this.exitServerToolStripMenuItem.Click += new System.EventHandler(this.exitServerToolStripMenuItem_Click);
            // 
            // shutdownServerToolStripMenuItem
            // 
            this.shutdownServerToolStripMenuItem.Name = "shutdownServerToolStripMenuItem";
            this.shutdownServerToolStripMenuItem.Size = new System.Drawing.Size(166, 22);
            this.shutdownServerToolStripMenuItem.Text = "Shutdown server";
            this.shutdownServerToolStripMenuItem.Click += new System.EventHandler(this.shutdownServerToolStripMenuItem_Click);
            // 
            // rebootServerToolStripMenuItem
            // 
            this.rebootServerToolStripMenuItem.Name = "rebootServerToolStripMenuItem";
            this.rebootServerToolStripMenuItem.Size = new System.Drawing.Size(166, 22);
            this.rebootServerToolStripMenuItem.Text = "Reboot server";
            this.rebootServerToolStripMenuItem.Click += new System.EventHandler(this.rebootServerToolStripMenuItem_Click);
            // 
            // exitVisionEngineToolStripMenuItem
            // 
            this.exitVisionEngineToolStripMenuItem.Name = "exitVisionEngineToolStripMenuItem";
            this.exitVisionEngineToolStripMenuItem.Size = new System.Drawing.Size(166, 22);
            this.exitVisionEngineToolStripMenuItem.Text = "Exit Vision Engine";
            this.exitVisionEngineToolStripMenuItem.Click += new System.EventHandler(this.exitVisionEngineToolStripMenuItem_Click);
            // 
            // streamToolStripMenuItem
            // 
            this.streamToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.startStreamToolStripMenuItem,
            this.stopStreamToolStripMenuItem,
            this.saveInputPictureToolStripMenuItem,
            this.saveOutputPictureToolStripMenuItem});
            this.streamToolStripMenuItem.Name = "streamToolStripMenuItem";
            this.streamToolStripMenuItem.Size = new System.Drawing.Size(56, 20);
            this.streamToolStripMenuItem.Text = "Stream";
            // 
            // startStreamToolStripMenuItem
            // 
            this.startStreamToolStripMenuItem.Name = "startStreamToolStripMenuItem";
            this.startStreamToolStripMenuItem.Size = new System.Drawing.Size(179, 22);
            this.startStreamToolStripMenuItem.Text = "Start stream";
            this.startStreamToolStripMenuItem.Click += new System.EventHandler(this.startStreamToolStripMenuItem_Click);
            // 
            // stopStreamToolStripMenuItem
            // 
            this.stopStreamToolStripMenuItem.Enabled = false;
            this.stopStreamToolStripMenuItem.Name = "stopStreamToolStripMenuItem";
            this.stopStreamToolStripMenuItem.Size = new System.Drawing.Size(179, 22);
            this.stopStreamToolStripMenuItem.Text = "Stop stream";
            this.stopStreamToolStripMenuItem.Click += new System.EventHandler(this.stopStreamToolStripMenuItem_Click);
            // 
            // saveInputPictureToolStripMenuItem
            // 
            this.saveInputPictureToolStripMenuItem.Name = "saveInputPictureToolStripMenuItem";
            this.saveInputPictureToolStripMenuItem.Size = new System.Drawing.Size(179, 22);
            this.saveInputPictureToolStripMenuItem.Text = "Save Input picture";
            this.saveInputPictureToolStripMenuItem.Click += new System.EventHandler(this.saveInputPictureToolStripMenuItem_Click);
            // 
            // saveOutputPictureToolStripMenuItem
            // 
            this.saveOutputPictureToolStripMenuItem.Name = "saveOutputPictureToolStripMenuItem";
            this.saveOutputPictureToolStripMenuItem.Size = new System.Drawing.Size(179, 22);
            this.saveOutputPictureToolStripMenuItem.Text = "Save Output picture";
            // 
            // controllerToolStripMenuItem
            // 
            this.controllerToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.enableControllerToolStripMenuItem,
            this.disableControllerToolStripMenuItem});
            this.controllerToolStripMenuItem.Name = "controllerToolStripMenuItem";
            this.controllerToolStripMenuItem.Size = new System.Drawing.Size(72, 20);
            this.controllerToolStripMenuItem.Text = "Controller";
            // 
            // enableControllerToolStripMenuItem
            // 
            this.enableControllerToolStripMenuItem.Name = "enableControllerToolStripMenuItem";
            this.enableControllerToolStripMenuItem.Size = new System.Drawing.Size(166, 22);
            this.enableControllerToolStripMenuItem.Text = "Enable controller";
            this.enableControllerToolStripMenuItem.Click += new System.EventHandler(this.enableControllerToolStripMenuItem_Click);
            // 
            // disableControllerToolStripMenuItem
            // 
            this.disableControllerToolStripMenuItem.Enabled = false;
            this.disableControllerToolStripMenuItem.Name = "disableControllerToolStripMenuItem";
            this.disableControllerToolStripMenuItem.Size = new System.Drawing.Size(166, 22);
            this.disableControllerToolStripMenuItem.Text = "Disable controller";
            this.disableControllerToolStripMenuItem.Click += new System.EventHandler(this.disableControllerToolStripMenuItem_Click);
            // 
            // advancedToolStripMenuItem
            // 
            this.advancedToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.enableCustomCommandsToolStripMenuItem});
            this.advancedToolStripMenuItem.Name = "advancedToolStripMenuItem";
            this.advancedToolStripMenuItem.Size = new System.Drawing.Size(72, 20);
            this.advancedToolStripMenuItem.Text = "Advanced";
            // 
            // enableCustomCommandsToolStripMenuItem
            // 
            this.enableCustomCommandsToolStripMenuItem.Name = "enableCustomCommandsToolStripMenuItem";
            this.enableCustomCommandsToolStripMenuItem.Size = new System.Drawing.Size(215, 22);
            this.enableCustomCommandsToolStripMenuItem.Text = "Enable custom commands";
            this.enableCustomCommandsToolStripMenuItem.Click += new System.EventHandler(this.enableCustomCommandsToolStripMenuItem_Click);
            // 
            // aboutToolStripMenuItem
            // 
            this.aboutToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.infoToolStripMenuItem});
            this.aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            this.aboutToolStripMenuItem.Size = new System.Drawing.Size(52, 20);
            this.aboutToolStripMenuItem.Text = "About";
            // 
            // infoToolStripMenuItem
            // 
            this.infoToolStripMenuItem.Name = "infoToolStripMenuItem";
            this.infoToolStripMenuItem.Size = new System.Drawing.Size(95, 22);
            this.infoToolStripMenuItem.Text = "Info";
            this.infoToolStripMenuItem.Click += new System.EventHandler(this.infoToolStripMenuItem_Click);
            // 
            // InputTextbox
            // 
            this.InputTextbox.Location = new System.Drawing.Point(12, 534);
            this.InputTextbox.Name = "InputTextbox";
            this.InputTextbox.Size = new System.Drawing.Size(882, 20);
            this.InputTextbox.TabIndex = 10;
            // 
            // executeButton
            // 
            this.executeButton.Location = new System.Drawing.Point(896, 531);
            this.executeButton.Name = "executeButton";
            this.executeButton.Size = new System.Drawing.Size(75, 23);
            this.executeButton.TabIndex = 11;
            this.executeButton.Text = "execute";
            this.executeButton.UseVisualStyleBackColor = true;
            this.executeButton.Click += new System.EventHandler(this.executeButton_Click);
            // 
            // OutputTextbox
            // 
            this.OutputTextbox.Location = new System.Drawing.Point(12, 560);
            this.OutputTextbox.Multiline = true;
            this.OutputTextbox.Name = "OutputTextbox";
            this.OutputTextbox.ReadOnly = true;
            this.OutputTextbox.Size = new System.Drawing.Size(959, 35);
            this.OutputTextbox.TabIndex = 12;
            // 
            // pictureBoxInput
            // 
            this.pictureBoxInput.Location = new System.Drawing.Point(12, 42);
            this.pictureBoxInput.Name = "pictureBoxInput";
            this.pictureBoxInput.Size = new System.Drawing.Size(959, 483);
            this.pictureBoxInput.TabIndex = 1;
            this.pictureBoxInput.TabStop = false;
            // 
            // RaiseLegsButton
            // 
            this.RaiseLegsButton.Location = new System.Drawing.Point(977, 68);
            this.RaiseLegsButton.Name = "RaiseLegsButton";
            this.RaiseLegsButton.Size = new System.Drawing.Size(75, 23);
            this.RaiseLegsButton.TabIndex = 13;
            this.RaiseLegsButton.Text = "Raise Legs";
            this.RaiseLegsButton.UseVisualStyleBackColor = true;
            this.RaiseLegsButton.Click += new System.EventHandler(this.RaiseLegsButton_Click);
            // 
            // LowerLegsButton
            // 
            this.LowerLegsButton.Location = new System.Drawing.Point(978, 97);
            this.LowerLegsButton.Name = "LowerLegsButton";
            this.LowerLegsButton.Size = new System.Drawing.Size(75, 23);
            this.LowerLegsButton.TabIndex = 14;
            this.LowerLegsButton.Text = "Lower legs";
            this.LowerLegsButton.UseVisualStyleBackColor = true;
            this.LowerLegsButton.Click += new System.EventHandler(this.LowerLegsButton_Click);
            // 
            // BatteryTextbox
            // 
            this.BatteryTextbox.Location = new System.Drawing.Point(978, 42);
            this.BatteryTextbox.Name = "BatteryTextbox";
            this.BatteryTextbox.ReadOnly = true;
            this.BatteryTextbox.Size = new System.Drawing.Size(75, 20);
            this.BatteryTextbox.TabIndex = 15;
            // 
            // VisionEngineForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1059, 603);
            this.ControlBox = false;
            this.Controls.Add(this.BatteryTextbox);
            this.Controls.Add(this.LowerLegsButton);
            this.Controls.Add(this.RaiseLegsButton);
            this.Controls.Add(this.OutputTextbox);
            this.Controls.Add(this.executeButton);
            this.Controls.Add(this.InputTextbox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.pictureBoxInput);
            this.Controls.Add(this.menuStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MainMenuStrip = this.menuStrip1;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "VisionEngineForm";
            this.Text = "Vision Engine®";
            this.Load += new System.EventHandler(this.VisionEngineForm_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxInput)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBoxInput;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem disconnectToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitServerToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem rebootServerToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem shutdownServerToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem streamToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem startStreamToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem stopStreamToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem advancedToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem infoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitVisionEngineToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem enableCustomCommandsToolStripMenuItem;
        private System.Windows.Forms.TextBox InputTextbox;
        private System.Windows.Forms.Button executeButton;
        private System.Windows.Forms.TextBox OutputTextbox;
        private System.Windows.Forms.ToolStripMenuItem saveInputPictureToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveOutputPictureToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem controllerToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem enableControllerToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem disableControllerToolStripMenuItem;
        private System.Windows.Forms.Button RaiseLegsButton;
        private System.Windows.Forms.Button LowerLegsButton;
        private System.Windows.Forms.TextBox BatteryTextbox;
    }
}

