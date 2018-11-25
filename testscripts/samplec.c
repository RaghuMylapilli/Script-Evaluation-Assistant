#include <stdio.h>

int main()
{
    int n;

    printf("Enter N value: "); /**/
    printf("\n");
    fflush(stdout); /**/
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("%d\n", i); /**/
        printf("\n");
        fflush(stdout); /**/
    }

    return 0;
}