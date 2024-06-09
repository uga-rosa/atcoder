#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int H, W, rs, cs, rt, ct, i, j, d, rank, ni, nj;
  cin >> H >> W >> rs >> cs >> rt >> ct;
  rs--;
  cs--;
  rt--;
  ct--;
  vector<vector<bool>> maze(H, vector(W, false));
  char c;
  rep(i, H) rep(j, W) {
    cin >> c;
    maze.at(i).at(j) = c == '.';
  }

  vector<pair<int, int>> D = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
  vector<vector<vector<int>>> ranks(H, vector(W, vector(4, -1)));
  deque<tuple<int, int, int, int>> que;
  que.push_back({rs, cs, 0, 0});
  que.push_back({rs, cs, 1, 0});
  que.push_back({rs, cs, 2, 0});
  que.push_back({rs, cs, 3, 0});
  while (!que.empty()) {
    tie(i, j, d, rank) = que.front();
    que.pop_front();
    ranks.at(i).at(j).at(d) = rank;
    if (i == rt && j == ct) {
      break;
    }
    ni = i + D.at(d).first;
    nj = j + D.at(d).second;
    if (0 <= ni && ni < H && 0 <= nj && nj < W && maze.at(ni).at(nj)) {
      rep(dd, 4) {
        if (ranks.at(ni).at(nj).at(dd) != -1) {
          continue;
        }
        if (dd == d) {
          que.push_front({ni, nj, d, rank});
        } else {
          que.push_back({ni, nj, dd, rank + 1});
        }
      }
    }
  }

  auto goal = ranks.at(rt).at(ct);
  cout << *max_element(goal.begin(), goal.end()) << endl;
};
