#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;

int main() {
  ll sx, sy, tx, ty;
  cin >> sx >> sy >> tx >> ty;

  if (abs(sx - tx) <= abs(sy - ty)) {
    cout << abs(sy - ty) << endl;
    return 0;
  }

  ll ans = abs(sy - ty);
  ll l, r;
  if (sx < tx) {
    l = sx + ans;
    r = tx;
  } else {
    l = tx;
    r = sx - ans;
  }

  if ((l % 2) == (ty % 2)) {
    l++;
  }
  if ((r % 2) != (ty % 2)) {
    r--;
  }

  if (r > l) {
    ans += (r - l + 1) / 2;
  }
  cout << ans << endl;
}
