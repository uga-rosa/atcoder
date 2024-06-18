#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;

int main() {
  int n;
  cin >> n;
  rep(i, 1, n + 1) { cout << (i % 3 == 0 ? "x" : "o"); }
  cout << endl;
}
