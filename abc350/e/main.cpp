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
ll n, a, x, y;
map<ll, double> memo;

double f(ll N) {
  if (N == 0) {
    return 0;
  }
  if (memo[N]) {
    return memo[N];
  }
  double ans =
      min(x + f(N / a),
          (6 * y + f(N / 2) + f(N / 3) + f(N / 4) + f(N / 5) + f(N / 6)) / 5);
  memo[N] = ans;
  return ans;
}

int main() {
  cin >> n >> a >> x >> y;
  cout << fixed << setprecision(10) << f(n) << endl;
}
