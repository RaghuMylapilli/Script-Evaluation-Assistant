#include <stdio.h>

int main() {
    int a, b;
    print("Enter two numbers: ");
    scanf("%d%d", &a, &b);

    if (a % b == 0) {
        printf("divisible");
    } else {
        printf("not divisible");
    }
}