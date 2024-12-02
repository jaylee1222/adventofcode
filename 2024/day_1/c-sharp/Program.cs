using System;

namespace MyApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                using (StringReader reader = new StringReader("input.txt") {
                    string line = string.Empty();
                    do
                    {
                        line = reader.ReadLine();
                        Console.WriteLine(line);
                    } while (line != null);
                }
            }
            catch (IOException e)
            {
                Console.WriteLine("The file could not be read.");
                Console.WriteLine(e.Message);
            }
            for
        }
    }
}
