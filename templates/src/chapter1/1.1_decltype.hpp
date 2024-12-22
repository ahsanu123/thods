#include <iostream>

using namespace std;

namespace Learn_Decltype {

template <typename T1, typename T2>
auto max(T1 a, T2 b) -> decltype(b < a ? a : b) {
  return b < a ? a : b;
}

void test() {
  auto whatMaxIs = max(2, 4.1);
  cout << "So Max is Double if you use fraction, and int if you use number: "
       << whatMaxIs << "\n";
}

} // namespace Learn_Decltype
