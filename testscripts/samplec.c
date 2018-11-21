#include <stdio.h>
int main() {
    int x, y;
    printf("Enter x:\n");
    fflush(stdout);
    scanf("%d", &x);

    printf("Enter y:\n");
    fflush(stdout);
    scanf("%d", &y);
    printf("%d %d\n", x, y);
    fflush(stdout);
    return 0;
}