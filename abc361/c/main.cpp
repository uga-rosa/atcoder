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
  ll n, k;
  cin >> n >> k;
  vector<ll> a(n);
  rep(i, 0, n) cin >> a[i];
  sort(all(a));

  ll min_diff = LLONG_MAX;
  for (ll i = 0; i <= k; i++) {
    min_diff = min(min_diff, a[i + (n - k - 1)] - a[i]);
  }
  cout << min_diff << endl;
}
