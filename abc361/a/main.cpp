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
  ll n, k, x;
  cin >> n >> k >> x;
  vector<ll> a(n);
  rep(i, 0, n) cin >> a[i];

  auto it = a.begin();
  rep(_, 0, k) it++;

  a.insert(it, x);
  rep(i, 0, n + 1) cout << a[i] << (i == n ? "\n" : " ");
}
