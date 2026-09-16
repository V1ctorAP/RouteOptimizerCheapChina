using System;

namespace RouteOptimizer.Core.Utilities
{
    public class OddEvenChecker
    {
        private int a;
        private int b;

        public OddEvenChecker(int a, int b)
        {
            this.a = a;
            this.b = b;
        }

        public string ComputeDifference()
        {
            int difference = Math.Abs(a - b);
            return difference % 2 == 0 ? "even" : "odd";
        }
    }
}
