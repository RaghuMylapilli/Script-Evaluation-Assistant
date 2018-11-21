#include <stdio.h>
int main() {
    int x, y;
    printf("Enter x:");
    printf("\n");
    fflush(stdout);
    scanf("%d", &x);

    printf("Enter y:");
    printf("\n");
    fflush(stdout);
    scanf("%d", &y);
    printf("%d %d", x, y);
    printf("\n");
    fflush(stdout);
    return 0;
}