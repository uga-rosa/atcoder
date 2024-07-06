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
  ll n;
  cin >> n;
  vector<ll> a(n), w(n);
  rep(i, 0, n) cin >> a[i];
  rep(i, 0, n) cin >> w[i];

  vector<priority_queue<ll, vector<ll>, greater<ll>>> q(n);
  rep(i, 0, n) { q[a[i] - 1].push(w[i]); }

  ll ans = 0;
  rep(i, 0, n) {
    while (q[i].size() > 1) {
      ans += q[i].top();
      q[i].pop();
    }
  }
  cout << ans << endl;
}
