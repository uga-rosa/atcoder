#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;

int main() {
  int n;
  string s;
  cin >> n >> s;
  string ans = "";
  rep(i, 0, n) {
    ans += s[i];
    ans += s[i];
  }
  cout << ans << endl;
}