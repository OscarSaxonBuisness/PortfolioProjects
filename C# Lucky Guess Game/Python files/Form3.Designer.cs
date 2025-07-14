namespace WindowsFormsApp1
{
    partial class Form3
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
            this.CongractulationsLabel = new System.Windows.Forms.Label();
            this.TryAgainButton = new System.Windows.Forms.Button();
            this.ConcractulationsLabel = new System.Windows.Forms.Label();
            this.GuessShowLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // CongractulationsLabel
            // 
            this.CongractulationsLabel.AutoSize = true;
            this.CongractulationsLabel.Location = new System.Drawing.Point(208, 142);
            this.CongractulationsLabel.Name = "CongractulationsLabel";
            this.CongractulationsLabel.Size = new System.Drawing.Size(0, 25);
            this.CongractulationsLabel.TabIndex = 0;
            // 
            // TryAgainButton
            // 
            this.TryAgainButton.Location = new System.Drawing.Point(286, 148);
            this.TryAgainButton.Name = "TryAgainButton";
            this.TryAgainButton.Size = new System.Drawing.Size(216, 92);
            this.TryAgainButton.TabIndex = 1;
            this.TryAgainButton.Text = "Try Again";
            this.TryAgainButton.UseVisualStyleBackColor = true;
            this.TryAgainButton.Click += new System.EventHandler(this.TryAgainButton_Click);
            // 
            // ConcractulationsLabel
            // 
            this.ConcractulationsLabel.AutoSize = true;
            this.ConcractulationsLabel.ForeColor = System.Drawing.SystemColors.Control;
            this.ConcractulationsLabel.Location = new System.Drawing.Point(142, 278);
            this.ConcractulationsLabel.Name = "ConcractulationsLabel";
            this.ConcractulationsLabel.Size = new System.Drawing.Size(511, 25);
            this.ConcractulationsLabel.TabIndex = 2;
            this.ConcractulationsLabel.Text = "Congractulations!!! You guessed the correct number";
            // 
            // GuessShowLabel
            // 
            this.GuessShowLabel.AutoSize = true;
            this.GuessShowLabel.ForeColor = System.Drawing.SystemColors.Control;
            this.GuessShowLabel.Location = new System.Drawing.Point(281, 335);
            this.GuessShowLabel.Name = "GuessShowLabel";
            this.GuessShowLabel.Size = new System.Drawing.Size(236, 25);
            this.GuessShowLabel.TabIndex = 3;
            this.GuessShowLabel.Text = "You got it in ? Guesses";
            // 
            // Form3
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlText;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.GuessShowLabel);
            this.Controls.Add(this.ConcractulationsLabel);
            this.Controls.Add(this.TryAgainButton);
            this.Controls.Add(this.CongractulationsLabel);
            this.Name = "Form3";
            this.Text = "LuckyGuess";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label CongractulationsLabel;
        private System.Windows.Forms.Button TryAgainButton;
        private System.Windows.Forms.Label ConcractulationsLabel;
        private System.Windows.Forms.Label GuessShowLabel;
    }
}