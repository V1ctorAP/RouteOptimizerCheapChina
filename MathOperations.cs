using System;

public class MathOperations
{
    public bool IsSumOddOrEven(int a, int b)
    {
        int sum = a + b;
        return sum % 2 == 0;
    }
}
