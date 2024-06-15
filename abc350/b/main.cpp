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
  int n, q, t;
  cin >> n >> q;
  vector<int> tooth(n, 1);
  rep(i, 0, q) {
    cin >> t;
    tooth[t-1] = !tooth[t-1];
  }
  cout << reduce(all(tooth)) << endl;
}
