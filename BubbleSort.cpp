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
        bool flag = false;
        for (j = i + 1; j < size - i - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                flag = true;
                temp = array[j + 1];
                array[j + 1] = array[j];
                array[j] = temp;
            }
        }
        if (flag == false)
        {
            break;
        }
    }

    cout << "\nSorted Array\n";
    displayArray(array, size);
    return 0;
}