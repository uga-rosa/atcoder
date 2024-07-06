#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;
using ull = unsigned long long;

int main() {
  ll a, b, C, X, Y;
  cin >> a >> b >> C;
  X = Y = 0;
  int zeroCount = 0;
  rep(i, 0, 60) {
    if (C & (1LL << i)) {
      (a > b ? X : Y) |= 1LL << i;
      (a > b ? a : b)--;
    } else {
      zeroCount++;
    }
  }
  if (a != b || a > zeroCount || a < 0) {
    cout << -1 << endl;
    return 0;
  }
  rep(i, 0, 60) {
    if (a > 0 && (C & (1LL << i)) == 0) {
      X |= 1LL << i;
      Y |= 1LL << i;
      a--;
    }
  }
  cout << X << " " << Y << endl;
}
