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
  vector<int> a(2 * n);
  rep(i, 0, 2 * n) cin >> a[i];

  int ans = 0;
  rep(i, 2, 2 * n) {
    if (a[i] == a[i - 2]) {
      ans++;
    }
  }
  cout << ans << endl;
}
