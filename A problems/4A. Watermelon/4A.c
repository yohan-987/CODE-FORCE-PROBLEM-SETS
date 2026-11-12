#include<stdio.h>
int main()
{int w;
    //printf("Enter the weight= ");
    // problem never specified for user input
    scanf("%d",&w);
    if(2<w && w<=100 && w%2==0)
    {printf("Yes\n");}
    else
    {printf("No\n");}
    
    return 0;
}