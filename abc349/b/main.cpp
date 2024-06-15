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
  string s;
  cin >> s;
  unordered_map<char, int> ctoi;
  for (auto ss : s) {
    ctoi[ss]++;
  }
  unordered_map<char, int> itoc;
  for (auto ci : ctoi) {
    itoc[ci.second]++;
  }
  for (auto [_, freq] : itoc) {
    if (freq != 2 && freq != 0) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}
