#include<stdio.h>
int main()
{int n,count=0,i=0;
char s[100];
    scanf("%d",&n);
    scanf("%s",s);
for(i=0;i<n-1;i++) 
{ if(s[i]==s[i+1])
    { count+=1;
    }
}   
printf("%d\n",count);
return 0;
    
}