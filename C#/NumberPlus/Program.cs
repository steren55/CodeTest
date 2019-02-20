using System;

namespace NumberPlus
{
	class Program
	{
		static void Main(string[] args)
		{
			for (int i=1;i<=10;i++) {
//				Console.Write("{0}\t", i);
				int sum=0;
				for (int j=1;j<=i;j++) {
					sum+=j;
					Console.Write("{0} ", j);
					if (j!=i)
						Console.Write("+ ");
				}
				Console.Write("= {0}", sum);
				Console.WriteLine("");
			}
		}
	}
}
