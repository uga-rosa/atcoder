#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;

using ll = long long;
#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
#define $(idx) (std::get<(idx)>(std::forward_as_tuple(_args...)))
#define lambda(...) ([&](auto &&..._args) { return (__VA_ARGS__); })

int main() {
  int n, m, a, b;
  cin >> n >> m;
  dsu uf(n);
  rep(i, 0, m) {
    cin >> a >> b;
    uf.merge(a-1, b-1);
  }
  ll ans = -m;
  for (auto g : uf.groups()) {
    ans += g.size() * (g.size() - 1) / 2;
  }
  cout << ans << endl;
}
