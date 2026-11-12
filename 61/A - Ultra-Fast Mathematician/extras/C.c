#include <stdio.h>
#include <string.h>

int main() {
    // Correct Declaration: Use arrays large enough for the input (e.g., 101 chars)
    char n[101], t[101], a[101];

    // Read the input strings
    // The array name itself acts as the pointer for scanf %s
    scanf("%s", n);
    scanf("%s", t);

    // Get the length of one of the strings (they are guaranteed to be the same length)
    int len = strlen(n);

    // Iterate through and store the result in array 'a'
    for (int i = 0; i < len; i++) {
        if (n[i] == t[i]) {
            a[i] = '0'; // Assign the character '0'
        } else {
            a[i] = '1'; // Assign the character '1'
        }
    }

    // Manually add the null-terminator at the end to make 'a' a valid C string
    a[len] = '\0';

    // Print the new result string 'a'
    printf("%s\n", a);

    return 0;
}
