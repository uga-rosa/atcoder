#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int64_t> lucas(N + 1);
  lucas.at(0) = 2;
  lucas.at(1) = 1;

  for (int i = 2; i < N + 1; i++) {
    lucas.at(i) = lucas.at(i - 1) + lucas.at(i - 2);
  }
  cout << lucas.at(N) << endl;
}
