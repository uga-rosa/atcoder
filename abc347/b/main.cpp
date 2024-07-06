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
  string s;
  cin >> s;
  int n = s.size();
  unordered_set<string> st;
  rep(i, 0, n) rep(j, i + 1, n + 1) { st.insert(s.substr(i, j - i)); }
  cout << st.size() << endl;
}
