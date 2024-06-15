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

int op_min(int a, int b) { return min(a, b); }
int e_min() { return (int)(1e9); }
int op_max(int a, int b) { return max(a, b); }
int e_max() { return -1; }

template <typename T> bool chmin(T &a, const T &b) {
  if (a > b) {
    a = b; // aをbで更新
    return true;
  }
  return false;
}

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> p(n);
  rep(i, n) cin >> p[i];
  vector<int> d(n);
  rep(i, n) d[p[i] - 1] = i;

  segtree<int, op_min, e_min> min_seg(d);
  segtree<int, op_max, e_max> max_seg(d);
  int ans = n + 1;
  rep(i, n - k + 1) {
    chmin(ans, max_seg.prod(i, i + k) - min_seg.prod(i, i + k));
  }
  cout << ans << endl;
}
