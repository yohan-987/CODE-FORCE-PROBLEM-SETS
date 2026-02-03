#include <stdio.h>
#include <string.h>

int main() {
    int n, i, j;
    int score[1000];
    char name[1000][32];

    // Input number of entries
    scanf("%d", &n);

    // Input names and scores
    for (i = 0; i < n; i++) {
        scanf("%s %d", name[i], &score[i]);
    }

    // Sort based on score (ascending order)
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (score[j] > score[j + 1]) {
                // swap scores
                int temp = score[j];
                score[j] = score[j + 1];
                score[j + 1] = temp;

                // swap names accordingly
                char tempName[32];
                strcpy(tempName, name[j]);
                strcpy(name[j], name[j + 1]);
                strcpy(name[j + 1], tempName);
            }
        }
    }

    // Print name with highest score (last element)
    printf("%s\n", name[n - 1]);

    return 0;
}
