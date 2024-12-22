#include <iostream>

using namespace std;

namespace Learn_CustomMax {

template <typename T> T max(T a, T b) { return b < a ? a : b; }

void test() { cout << "Custom Max: " << ::max(7, 9) << "\n"; }
} // namespace Learn_CustomMax
