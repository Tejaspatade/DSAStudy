#include <iostream>
#include <cstdlib>
#define MAX 100
using namespace std;

void displayArray(int array[], int size)
{
    for (int iter = 0; iter < size; iter++)
    {
        cout << array[iter] << " ";
    }
}
int main()
{
    int array[MAX], size;
    cout << "Enter Array Size:";
    cin >> size;
    for (int iter = 0; iter < size; iter++)
    {
        array[iter] = rand();
    }

    cout << "Unsorted Array\n";
    displayArray(array, size);

    // Sorting -> Bubble Sort
    int i, j, temp;
    for (i = 0; i < size; i++)
    {
        for (j = i + 1; j < size - 1; j++)
        {
            if (array[j] < array[i])
            {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }

    cout << "Sorted Array\n";
    displayArray(array, size);
    return 0;
}