using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics.Eventing.Reader;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WindowsFormsApp1
{
    

    public partial class Form2 : Form
    {
        int rnumber = 0;
        int RandomNumber = 0;
        public int Guess = 1;
        public Form2()
        {
            InitializeComponent();
            Random random = new Random();
            rnumber = random.Next(1,101);
            RandomNumber = rnumber;
        }

        


        private void EnterButton_Click(object sender, EventArgs e)


        {
            int MoreThan = 1;
            int LessThan = 100;

            
            

            string UserGuessString = UserGuessTextBox.Text;
            int UserGuess = Convert.ToInt32(UserGuessString);

            if (UserGuess != RandomNumber)
            {
                //if (UserGuess > 100)
                //{
                //    AppropriateMessageLabel.Text = "Guess is too high enter a value less than" + LessThan;
                //}
                //else if (UserGuess < 0)
                //{
                //    AppropriateMessageLabel.Text = "Guess is too low enter a value more than " + MoreThan;
                //}



                if (UserGuess < RandomNumber && UserGuess > MoreThan)
                {
                    MoreThan = UserGuess;
                    MoreThanLabel.Text = "More Than: " + MoreThan;
                    AppropriateMessageLabel.Text = "Your guess is too low, Try a higher number";
                    Guess += 1;
                }

                else if (UserGuess > RandomNumber && UserGuess < LessThan)
                {
                    LessThan = UserGuess;
                    LessThanLabel.Text = "Less Than: " + LessThan;
                    AppropriateMessageLabel.Text = "Your guess is too high. Try a lower number";
                    Guess += 1;
                }

                else if (UserGuess <= MoreThan)
                {
                    AppropriateMessageLabel.Text = "Guess is too low enter a value greater than: " + MoreThan;
                    Guess += 1;

                }

                else if (UserGuess >= LessThan)
                {
                    AppropriateMessageLabel.Text = "Guess is too high enter a lower value than: " + LessThan;
                    Guess += 1;

                }




            }
            if (UserGuess == RandomNumber)
            {
               
                Form3 Frm3 = new Form3(Guess);
                Frm3.ShowDialog();
                
                this.Hide();


            }
        }

        private void HomeButton_Click(object sender, EventArgs e)
        {
            Form1 frm1 = new Form1();
            frm1.Show();

            this.Hide();
        }

        private void ExitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

    }
}

            
        
    

