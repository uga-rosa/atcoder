#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string S;
  cin >> S;

  int res = 1;
  for (int i = 1; i < S.size(); i += 2) {
    char op = S.at(i);
    if (op == '+') {
      res++;
    } else {
      res--;
    }
  }
  cout << res << endl;
}
