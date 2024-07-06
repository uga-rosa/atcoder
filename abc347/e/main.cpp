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
  int n, q, xx;
  cin >> n >> q;
  vector<int> x(q);
  rep(i, 0, q) {
    cin >> x[i];
    x[i]--;
  };
  unordered_set<int> st;

  vector<ll> a(n, 0);
  ll size_sum = 0;
  rep(i, 0, q) {
    xx = x[i];
    if (st.contains(xx)) {
      st.erase(xx);
      a[xx] += size_sum;
    } else {
      st.insert(xx);
      a[xx] -= size_sum;
    }
    size_sum += st.size();
  }
  for (int xx : st) {
    a[xx] += size_sum;
  }

  rep(i, 0, n) cout << a[i] << (i == n - 1 ? "\n" : " ");
}
