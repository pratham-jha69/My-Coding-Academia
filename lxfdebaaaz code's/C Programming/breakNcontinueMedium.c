#include <stdio.h>
int main()
{
    int num;
    while(1)
    {
        printf("Enter a number: ");
        scanf("%d",&num);
        if (num<0){
            printf("Negative number encountered...Exiting!");
            break;
        }
    }
    return 0;
}