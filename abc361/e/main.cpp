#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;
using ull = unsigned long long;

vector<vector<pair<int, int>>> G;

void treeDFS(ll from, ll current, ll dist, ll &maxDist, ll &maxVertex) {
  if (dist > maxDist) {
    maxDist = dist;
    maxVertex = current;
  }

  for (auto to : G[current]) {
    if (to.first == from)
      continue;
    treeDFS(current, to.first, dist + to.second, maxDist, maxVertex);
  }
}

int main() {
  ll n, a, b, c;
  cin >> n;
  G.resize(n);

  ll ans = 0;
  rep(i, 0, n - 1) {
    cin >> a >> b >> c;
    a--, b--;
    G[a].push_back({b, c});
    G[b].push_back({a, c});
    ans += c * 2;
  }

  ll d = 0, v = 0;
  treeDFS(-1, 0, 0, d, v);
  d = 0;
  treeDFS(-1, v, 0, d, v);
  ans -= d;

  cout << ans << endl;
}
