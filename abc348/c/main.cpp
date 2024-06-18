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
  vector<int> a(n), c(n);
  rep(i, 0, n) cin >> a[i] >> c[i];

  unordered_map<int, int> ctoa;
  rep(i, 0, n) {
    if (ctoa[c[i]] == 0) {
      ctoa[c[i]] = a[i];
    } else {
      ctoa[c[i]] = min(ctoa[c[i]], a[i]);
    }
  }
  int ans = 0;
  for (auto [_, a] : ctoa)
    ans = max(ans, a);
  cout << ans << endl;
}
