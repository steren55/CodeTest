using System;

namespace ImageRotate
{
    class Program
    {
        static void Main(string[] args)
        {
            #region Step 1: Initial
            Console.WriteLine("Step 1: Initial\n");

            int oriWid = 2;                 // Width  : Original Image
            int oriHei = 2;                 // Height : Original Image
            double theta = 180;              // Rotate Angle (degree)
            theta = theta*Math.PI/180.0;    // Change (degree) to (radians)
            // Calculate New Image Width & Height
            int newWid = (int)((double)oriWid*Math.Abs(Math.Cos(theta))+(double)oriHei*Math.Abs(Math.Sin(theta)));
            int newHei = (int)((double)oriHei*Math.Abs(Math.Cos(theta))+(double)oriWid*Math.Abs(Math.Sin(theta)));
            // Initial Image Matrix
            byte[,] oriImg = new byte[oriHei,oriWid];
            byte[,] newImg = new byte[newHei,newWid];
            // Show Result
            Console.WriteLine("Original Image: {0} x {1}", oriWid, oriHei);
            Console.WriteLine(" Rotated Image: {0} x {1}", newWid, newHei);
            Console.WriteLine();

            #endregion

            #region Step 2: Rotate
            Console.WriteLine("Step 2: Rotate\n");

            // Show Original Image
            Console.WriteLine("Original Image:");
            for (int i=0; i<oriHei; i++) {
                for (int j=0; j<oriWid; j++) {
                    Console.Write("({0},{1}) ", i, j);
                }
                Console.WriteLine();
            }
            Console.WriteLine();
            // Show Rotated Image
            Console.WriteLine("Rotated Image:");
            double v=0,w=0,x=0,y=0,ii=0,jj=0;
            for (int i=0; i<newHei; i++) {
                for (int j=0; j<newWid; j++) {
                    // Translation
                    v=(double)i-(double)(newHei-1)/2.0;
                    w=(double)j-(double)(newWid-1)/2.0;
                    // Rotate
                    Rotate(v, w, ref x, ref y, theta*(-1.0));
                    // Translation
                    x+=((double)(oriWid-1)/2.0);
                    y+=((double)(oriHei-1)/2.0);
                    // Nearest-neighbor
                    ii=(int)Math.Round(x,0);
                    jj=(int)Math.Round(y,0);
                    // Show Result
                    if (0<=ii && ii<oriHei && 0<=jj && jj<oriWid)
                        Console.Write("({0},{1}) ", ii, jj);
                    else {
                        Console.Write("(x,x) ");
                    }
                }
                Console.WriteLine();
            }

            #endregion
        }

        static private void Rotate(double v, double w, ref double x, ref double y, double theta) {
            x = v*Math.Cos(theta)-w*Math.Sin(theta);
            y = v*Math.Sin(theta)+w*Math.Cos(theta);
        }
    }
}
