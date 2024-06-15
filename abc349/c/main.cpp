#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;

using ll = long long;
#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
#define $(idx) (std::get<(idx)>(std::forward_as_tuple(_args...)))
#define lambda(...) ([&](auto &&..._args) { return (__VA_ARGS__); })

int main() {
  string s, t;
  cin >> s >> t;

  int imax = s.size();
  int jmax = 3;
  if (t[2] == 'X') {
    t = t.substr(0, 2);
    jmax--;
  }

  int i = 0;
  int j = 0;
  while (i < imax && j < jmax) {
    if (s[i] == tolower(t[j])) {
      j++;
    }
    i++;
  }

  cout << (j == jmax ? "Yes" : "No") << endl;
}
