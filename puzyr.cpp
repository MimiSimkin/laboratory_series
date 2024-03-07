#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>

int main() {
    std::srand(std::time(0));
    std::vector<int> arr(100);
    for (int i = 0; i < 100; i++) {
        arr[i] = std::rand() % (2 * 100000 + 1) - 100000;
    }
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 99 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
    for (int i = 0; i < 100; i++) {
        std::cout << arr[i] << " ";
    }
    return 0;
}
