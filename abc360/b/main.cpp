#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;
using ull = unsigned long long;

int main() {
  string s, t;
  cin >> s >> t;
  int ss = s.size();
  int ts = t.size();
  rep(w, (ss / ts), (ss / (ts - 1)) + 1) {
    cout << "w " << w << endl;
  }
}
