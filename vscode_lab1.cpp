#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main() {
    std::ifstream file("data1.txt");
    std::ofstream g("tutorial.txt", std::ios::app);
    std::vector<int> arr;
    int num;
    while (file >> num) {
        arr.push_back(num);
    }
    int founder;
    std::cin >> founder;
    std::vector<int> binarr = arr;
    std::sort(binarr.begin(), binarr.end());
    int i;
    for (i = 0; i < arr.size(); i++) {
        if (founder == arr[i]) {
            std::cout << i << std::endl;
            break;
        }
    }
    std::cout << i << std::endl;
    int j = binarr.size() / 2;
    while (founder != binarr[j]) {
        if (founder < binarr[j]) {
            j /= 2;
        } else {
            j += j / 2;
        }
    }
    std::cout << j << std::endl;
    g << i << ' ' << j << '\n';
    g.close();
    return 0;
}
