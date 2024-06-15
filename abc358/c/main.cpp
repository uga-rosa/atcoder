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
  int n, m, ans, done, count;
  cin >> n >> m;
  string S;
  vector<int> s(n);
  rep(i, 0, n) {
    cin >> S;
    int b = 0;
    rep(j, 0, m) {
      b <<= 1;
      if (S[j] == 'o') {
        b |= 1;
      }
    }
    s[i] = b;
  }

  ans = n;
  rep(bit, 0, 1 << n) {
    done = 0;
    count = 0;
    rep(i, 0, n) {
      if ((bit >> i) & 1) {
        done |= s[i];
        count++;
      }
    }
    if (done == (1 << m) - 1 && count < ans) {
      ans = count;
    }
  }
  cout << ans << endl;
}
