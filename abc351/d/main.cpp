#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;

using ll = int64_t;
#define WRAP_REP(_1, _2, _3, NAME, ...) NAME
#define REP2(i, n) for (ll i = 0; i < (ll)(n); i++)
#define REP3(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define rep(...) WRAP_REP(__VA_ARGS__, REP3, REP2)(__VA_ARGS__)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
#define $(idx) (std::get<(idx)>(std::forward_as_tuple(_args...)))
#define lambda(...) ([&](auto &&..._args) { return (__VA_ARGS__); })

vector<int> used(1e6, -1);

template <typename T> inline bool chmax(T &a, T b) {
  return ((a < b) ? (a = b, true) : (false));
}

int dfs(int crr, int id, vector<vector<int>> &graph) {
  if (used[crr] == id) {
    return 0;
  }
  used[crr] = id;
  int ans = 1;
  for (auto nxt : graph[crr]) {
    ans += dfs(nxt, id, graph);
  }
  return ans;
}

int main() {
  int h, w, idx;
  cin >> h >> w;
  vector<string> s(h);
  rep(i, h) cin >> s[i];

  vector<vector<int>> graph(h * w);
  rep(i, h) rep(j, w) {
    idx = i * w + j;
    if (s[i][j] == '.' &&
        ((i == 0 || s[i - 1][j] == '.') && (i == h - 1 || s[i + 1][j] == '.') &&
         (j == 0 || s[i][j - 1] == '.') &&
         (j == w - 1 || s[i][j + 1] == '.'))) {
      if (i > 0)
        graph[idx].push_back(idx - w);
      if (i < h - 1)
        graph[idx].push_back(idx + w);
      if (j > 0)
        graph[idx].push_back(idx - 1);
      if (j < w - 1)
        graph[idx].push_back(idx + 1);
    }
  }

  int ans = 1;
  rep(i, h) rep(j, w) {
    idx = i * w + j;
    if (s[i][j] == '.' && used[idx] < 0) {
      chmax(ans, dfs(idx, idx, graph));
    }
  }
  cout << ans << endl;
}
