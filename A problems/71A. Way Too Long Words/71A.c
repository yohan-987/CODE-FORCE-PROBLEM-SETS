#include <stdio.h>
int main()
{
 int n;
 scanf("%d",&n); // n is number of word being entered , it scans multiple word in one go 
 char word[101]; // Array to store one word (max 100 letters + 1 for null terminator '\0')

 int i;
 for(i=0; i<n;i++) // it will scan each word one at a time and fit 100 characters in word array
 { scanf("%100s",word); // %100s ensures at most 100 characters are read, leaving space for the null terminator

 
 int len=0; // len will store the length of the current word

 for(len=0;word[len]!='\0';len++); // <== important semicolon , so it can store value inside len before jumping into if condition
 
 // \0 is called the null character.
 //It has ASCII value 0.
 //In C, all strings are arrays of characters that end with \0.
 //It tells the program “this is the end of the string”.
 //Without \0, the program would not know where the string ends, leading to garbage output or memory errors.
 //so its basically that , run the while loop and starting with index 0 and end when index value is equal \0 , count each loop and the number would be number of characters
 if (len>10)
 {printf("%c%d%c\n",word[0],len-2,word[len-1]);
 }
 else
 {
    printf("%s\n",word);
 }

}
 return 0;


}