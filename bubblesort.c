// Bubble sort algorithm in C

#include <stdio.h>

void bubbleSort(int arr[], int n)
{
    for(int i = n; i > 0;i--) {
        for(int j = 1; j < i; j++) {
            if(arr[j] < arr[j-1]) {
                arr[j] += arr[j-1];
                arr[j-1] = arr[j] - arr[j-1];
                arr[j] -= arr[j-1];
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
}

int main()
{
    int arr[6] = {76, 22, 21, 96, 70, 20};
    bubbleSort(arr, 6);
    return 0;
}

// Output
// 20 21 22 70 76 96