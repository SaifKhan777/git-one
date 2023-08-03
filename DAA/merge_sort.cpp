#include <iostream>
#include <algorithm>
#include <random>

using namespace std;

void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }

    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
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

    cout << "Given array is: ";
    printArray(arr, size);

    mergeSort(arr, 0, size - 1);

    cout << "\nSorted array is: ";
    printArray(arr, size);
    return 0;
}
