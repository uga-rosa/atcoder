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
using node = pair<int, int>;
using res = pair<int, int>;

int main() {
  int n, aa, j;
  cin >> n;
  vector<int> a(n), rev(n);
  rep(i, 0, n) {
    cin >> aa;
    aa--;
    a[i] = aa;
    rev[aa] = i;
  }

  vector<pair<int, int>> ans(0);
  rep(i, 0, n) {
    if (a[i] == i)
      continue;
    j = rev[i];
    ans.push_back({i + 1, j + 1});
    swap(a[i], a[j]);
    swap(rev[a[i]], rev[a[j]]);
  }

  cout << ans.size() << endl;;
  for (auto anss : ans)
    cout << anss.first << " " << anss.second << endl;
}
