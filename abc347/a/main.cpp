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
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  rep(i, 0, n) cin >> a[i];

  vector<int> ans(0);
  rep(i, 0, n) {
    if (a[i] % k == 0) {
      ans.push_back(a[i] / k);
    }
  }
  sort(all(ans));
  rep(i, 0, ans.size()) {
    cout << ans[i] << (i == ans.size() - 1 ? "\n" : " ");
  }
}
