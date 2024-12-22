#include <iostream>
#include <string>

using namespace std;

namespace Learn_DefaultArgument {

template <typename T = std::string>

T defaultArgument(T arg = "default") {
  cout << "default argument is: " << arg << "\n";
  return arg;
}

void test() {
  defaultArgument();
  defaultArgument("was Changed");
}

} // namespace Learn_DefaultArgument
