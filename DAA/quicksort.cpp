#include <iostream>
#include <algorithm>
#include <random>


// Function to partition the array and return the pivot index
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Choose the rightmost element as the pivot
    int i = low - 1; // Index of the smaller element

    for (int j = low; j <= high - 1; j++) {                                                                                         
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }

    std::swap(arr[i + 1], arr[high]);
    return (i + 1);
}

// Function to implement Quick Sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to print the array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int size;
    std::cout << "Enter the size of the array: ";
    std::cin >> size;

    int* arr = new int[size];

    // Option to manually enter the elements or generate random values
    char choice;
    std::cout << "Do you want to manually enter the elements? (y/n): ";
    std::cin >> choice;

    if (choice == 'y' || choice == 'Y') {
        std::cout << "Enter the elements:" << std::endl;
        for (int i = 0; i < size; i++) {
            std::cin >> arr[i];
        }
    } else {
        // Use random number generator to fill the array
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(1, 100);

        for (int i = 0; i < size; i++) {
            arr[i] = dis(gen);
        }

        std::cout << "Randomly generated array: ";
        printArray(arr, size);
    }

    std::cout << "Original array: ";
    printArray(arr, size);

    quickSort(arr, 0, size - 1);

    std::cout << "Sorted array: ";
    printArray(arr, size);

    delete[] arr;
    return 0;
}
