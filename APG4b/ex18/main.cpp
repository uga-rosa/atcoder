#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N, M;
  cin >> N >> M;
  vector<vector<char>> ans(N, vector<char>(N, '-'));
  rep(i, M) {
    int w, l;
    cin >> w >> l;
    w--;
    l--;
    ans.at(w).at(l) = 'o';
    ans.at(l).at(w) = 'x';
  }

  rep(i, N) {
    rep(j, N) {
      cout << ans.at(i).at(j);
      if (j == N - 1) {
        cout << endl;
      } else {
        cout << " ";
      }
    }
  }
}
