namespace WindowsFormsApp1
{
    partial class Form2
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
            this.RandomisedNumberDisplay = new System.Windows.Forms.Label();
            this.UserGuessTextBox = new System.Windows.Forms.TextBox();
            this.EnterGuessLabel = new System.Windows.Forms.Label();
            this.EnterButton = new System.Windows.Forms.Button();
            this.AppropriateMessageLabel = new System.Windows.Forms.Label();
            this.MoreThanLabel = new System.Windows.Forms.Label();
            this.LessThanLabel = new System.Windows.Forms.Label();
            this.HomeButton = new System.Windows.Forms.Button();
            this.ExitButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // RandomisedNumberDisplay
            // 
            this.RandomisedNumberDisplay.AutoSize = true;
            this.RandomisedNumberDisplay.BackColor = System.Drawing.SystemColors.ControlText;
            this.RandomisedNumberDisplay.ForeColor = System.Drawing.SystemColors.Control;
            this.RandomisedNumberDisplay.Location = new System.Drawing.Point(267, 94);
            this.RandomisedNumberDisplay.Name = "RandomisedNumberDisplay";
            this.RandomisedNumberDisplay.Size = new System.Drawing.Size(249, 25);
            this.RandomisedNumberDisplay.TabIndex = 0;
            this.RandomisedNumberDisplay.Text = "Randomised Number = ?";
            // 
            // UserGuessTextBox
            // 
            this.UserGuessTextBox.Location = new System.Drawing.Point(275, 315);
            this.UserGuessTextBox.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.UserGuessTextBox.Name = "UserGuessTextBox";
            this.UserGuessTextBox.Size = new System.Drawing.Size(229, 31);
            this.UserGuessTextBox.TabIndex = 3;
            // 
            // EnterGuessLabel
            // 
            this.EnterGuessLabel.AutoSize = true;
            this.EnterGuessLabel.BackColor = System.Drawing.SystemColors.ControlText;
            this.EnterGuessLabel.ForeColor = System.Drawing.SystemColors.Control;
            this.EnterGuessLabel.Location = new System.Drawing.Point(75, 318);
            this.EnterGuessLabel.Name = "EnterGuessLabel";
            this.EnterGuessLabel.Size = new System.Drawing.Size(182, 25);
            this.EnterGuessLabel.TabIndex = 4;
            this.EnterGuessLabel.Text = "Enter guess here:";
            // 
            // EnterButton
            // 
            this.EnterButton.Location = new System.Drawing.Point(529, 301);
            this.EnterButton.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.EnterButton.Name = "EnterButton";
            this.EnterButton.Size = new System.Drawing.Size(141, 51);
            this.EnterButton.TabIndex = 5;
            this.EnterButton.Text = "Enter";
            this.EnterButton.UseVisualStyleBackColor = true;
            this.EnterButton.Click += new System.EventHandler(this.EnterButton_Click);
            // 
            // AppropriateMessageLabel
            // 
            this.AppropriateMessageLabel.AutoSize = true;
            this.AppropriateMessageLabel.BackColor = System.Drawing.SystemColors.ControlText;
            this.AppropriateMessageLabel.ForeColor = System.Drawing.SystemColors.Control;
            this.AppropriateMessageLabel.Location = new System.Drawing.Point(179, 388);
            this.AppropriateMessageLabel.Name = "AppropriateMessageLabel";
            this.AppropriateMessageLabel.Size = new System.Drawing.Size(0, 25);
            this.AppropriateMessageLabel.TabIndex = 6;
            // 
            // MoreThanLabel
            // 
            this.MoreThanLabel.AutoSize = true;
            this.MoreThanLabel.BackColor = System.Drawing.SystemColors.ControlText;
            this.MoreThanLabel.ForeColor = System.Drawing.SystemColors.Control;
            this.MoreThanLabel.Location = new System.Drawing.Point(132, 178);
            this.MoreThanLabel.Name = "MoreThanLabel";
            this.MoreThanLabel.Size = new System.Drawing.Size(140, 25);
            this.MoreThanLabel.TabIndex = 7;
            this.MoreThanLabel.Text = "More Than: 0";
            // 
            // LessThanLabel
            // 
            this.LessThanLabel.AutoSize = true;
            this.LessThanLabel.BackColor = System.Drawing.SystemColors.ControlText;
            this.LessThanLabel.ForeColor = System.Drawing.SystemColors.Control;
            this.LessThanLabel.Location = new System.Drawing.Point(493, 178);
            this.LessThanLabel.Name = "LessThanLabel";
            this.LessThanLabel.Size = new System.Drawing.Size(161, 25);
            this.LessThanLabel.TabIndex = 8;
            this.LessThanLabel.Text = "Less Than: 100";
            // 
            // HomeButton
            // 
            this.HomeButton.Location = new System.Drawing.Point(525, 12);
            this.HomeButton.Name = "HomeButton";
            this.HomeButton.Size = new System.Drawing.Size(118, 46);
            this.HomeButton.TabIndex = 9;
            this.HomeButton.Text = "Home";
            this.HomeButton.UseVisualStyleBackColor = true;
            this.HomeButton.Click += new System.EventHandler(this.HomeButton_Click);
            // 
            // ExitButton
            // 
            this.ExitButton.Location = new System.Drawing.Point(682, 12);
            this.ExitButton.Name = "ExitButton";
            this.ExitButton.Size = new System.Drawing.Size(99, 43);
            this.ExitButton.TabIndex = 10;
            this.ExitButton.Text = "Exit";
            this.ExitButton.UseVisualStyleBackColor = true;
            this.ExitButton.Click += new System.EventHandler(this.ExitButton_Click);
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlText;
            this.ClientSize = new System.Drawing.Size(807, 470);
            this.Controls.Add(this.ExitButton);
            this.Controls.Add(this.HomeButton);
            this.Controls.Add(this.LessThanLabel);
            this.Controls.Add(this.MoreThanLabel);
            this.Controls.Add(this.AppropriateMessageLabel);
            this.Controls.Add(this.EnterButton);
            this.Controls.Add(this.EnterGuessLabel);
            this.Controls.Add(this.UserGuessTextBox);
            this.Controls.Add(this.RandomisedNumberDisplay);
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Name = "Form2";
            this.Text = "LuckyGuess";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label RandomisedNumberDisplay;
        private System.Windows.Forms.TextBox UserGuessTextBox;
        private System.Windows.Forms.Label EnterGuessLabel;
        private System.Windows.Forms.Button EnterButton;
        private System.Windows.Forms.Label AppropriateMessageLabel;
        private System.Windows.Forms.Label MoreThanLabel;
        private System.Windows.Forms.Label LessThanLabel;
        private System.Windows.Forms.Button HomeButton;
        private System.Windows.Forms.Button ExitButton;
    }
}