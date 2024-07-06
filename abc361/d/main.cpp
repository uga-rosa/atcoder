#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;
using ull = unsigned long long;

int bfs(string s, const string &t) {
  unordered_map<string, int> dp;
  queue<pair<string, int>> q;
  q.push({s, 0});
  dp[s] = 0;

  while (!q.empty()) {
    auto [current, cost] = q.front();
    q.pop();

    if (current == t) {
      return cost;
    }

    int n = current.size();
    int dot = current.find('.');
    rep(i, 0, n - 1) {
      if (current[i] == '.' || current[i + 1] == '.') {
        continue;
      } else {
        string next = current;
        next[dot] = next[i];
        next[dot + 1] = next[i + 1];
        next[i] = '.';
        next[i + 1] = '.';

        if (dp.count(next) == 0) {
          dp[next] = cost + 1;
          q.push({next, cost + 1});
        }
      }
    }
  }
  return -1; // 目的の状態に到達できない場合
}

int main() {
  int n;
  cin >> n;
  string s, t;
  cin >> s >> t;
  s += "..";
  t += "..";

  // ある盤面から次の盤面までの移行パターンは n-1 か n-2 通りしかない。
  // 盤面のパターンは (n+2, 2) * 2**n 通り
  // 2 <= n <= 14 なので移行パターンを全部挙げることはできる

  cout << bfs(s, t) << endl;
}
