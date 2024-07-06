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
  ll n, a, b;
  cin >> n >> a >> b;
  vector<ll> d(n);
  rep(i, 0, n) cin >> d[i];

  rep(i, 0, n) { d[i] %= a + b; }
  sort(all(d));
  d.erase(unique(all(d)), d.end());
  n = d.size();

  bool ans = false;
  rep(i, 1, n) {
    if ((d[i] - d[i - 1]) > b) {
      ans = true;
    }
  }
  if (!ans) {
    ans = (d[0] - d[n - 1]) + (a + b) > b;
  }
  cout << (ans ? "Yes" : "No") << endl;
}
