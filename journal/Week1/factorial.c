#include <stdio.h>

int factorial(int number)
{
    int answer = 1;
    // check if above one
    if (number == 1)
    {
        return answer;
    }    
    answer = (number - 1) * number;
    factorial(answer);
        

    
}

int main(void)
{
    factorial(5);
}



// find the number

//check if above 1
// subtract number by 1 and multiply by previous
//check if above 1
// subtract number by 1 and multiply by previous
