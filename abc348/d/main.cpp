#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;

int main() {
  int h, w, idx;
  cin >> h >> w;
  vector<string> a(h);
  rep(i, 0, h) cin >> a[i];

  vector<vector<int>> graph(h * w, vector<int>(0));
  int S = -1;
  int T = -1;
  rep(i, 0, h) rep(j, 0, w) {
    idx = i * w + j;
    if (a[i][j] == '#') {
      continue;
    } else if (a[i][j] == 'S') {
      S = idx;
    } else if (a[i][j] == 'T') {
      T = idx;
    }
    if (i > 0 && a[i - 1][j] != '#')
      graph[idx].push_back(idx - w);
    if (i < h - 1 && a[i + 1][j] != '#')
      graph[idx].push_back(idx + w);
    if (j > 0 && a[i][j - 1] != '#')
      graph[idx].push_back(idx - 1);
    if (j < w - 1 && a[i][j + 1] != '#')
      graph[idx].push_back(idx + 1);
  }
  assert(S != -1 && T != -1);

  vector<int> egrid(h * w, -1);
  int n, r, c, e;
  cin >> n;
  rep(i, 0, n) {
    cin >> r >> c >> e;
    egrid[(r - 1) * w + (c - 1)] = e;
  }
  egrid[T] = 0;

  vector<bool> used(h * w, false);
  rep(i, 0, n) {
    e = egrid[i];
    if (e <= 0)
      continue;
    vector<int> dist(h * w, -1);
    dist[i] = e;
    queue<int> que;
    que.push(i);
    while (!que.empty()) {
      int crr = que.front();
      que.pop();
      if (dist[crr] == -1)
        continue;
      used[crr] = true;
      for (auto nxt : graph[crr]) {
        if (dist[nxt] == -1) {
          dist[nxt] = dist[crr] - 1;
          que.push(nxt);
        }
      }
    }
    cout << i / w << " " << i % w << endl;
    rep(i, 0, h) rep(j, 0, w) {
      cout << dist[i * w + j] << (j == w - 1 ? "\n" : " ");
    }
  }

  cout << (used[T] ? "Yes" : "No") << endl;
}
