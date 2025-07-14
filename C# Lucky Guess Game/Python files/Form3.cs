using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form3 : Form
    {
        public Form3(int Guess)
        {
            InitializeComponent();
            GuessShowLabel.Text = "You got it in "+ Guess + " Guesses";
        }

        private void TryAgainButton_Click(object sender, EventArgs e)
        {
            Form2 frm2 = new Form2();
            frm2.Show();

            this.Hide();
        }

        
    }
}
