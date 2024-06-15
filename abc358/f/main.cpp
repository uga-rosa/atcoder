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

string repeat(string s, int n, string sep = "") {
  string ans = "";
  rep(i, 0, n) {
    ans += s;
    if (i != n - 1)
      ans += sep;
  }
  return ans;
}

int main() {
  int n, m, k;
  cin >> n >> m >> k;
  if (k < n || (k - n) % 2 == 1) {
    cout << "No" << endl;
    return 0;
  }
  cout << "Yes" << endl;
  cout << repeat("+", 2 * m - 1) + "S" + "+" << endl;

  if (k == n) {
    rep(i, 0, n) {
      if (m == 1) {
        cout << "+o+" << endl;
      } else {
        cout << "+" + repeat("o.", max(m - 2, 0)) + "o|o+" << endl;
      }
      if (i < n - 1) {
        cout << "+" + repeat("-+", max(m - 1, 0)) + ".+" << endl;
      }
    }
    cout << repeat("+", 2 * m - 1) + "G" + "+" << endl;
    return 0;
  }

  int branch_count = (k - n) / ((m - 1) * 2);
  int remain = (k - n) / 2 - (branch_count - 1) * (m - 1);

  rep(i, 0, n / 2) {
    int branch_length = i < branch_count ? m - 1 : min(remain, m - 1);
    if (branch_length == m - 1) {
      cout << "+" + repeat("o", m, ".") + "+" << endl;
    } else {
      cout << "+" + repeat("o", m - 1 - branch_length, ".") + "|" +
                  repeat("o", branch_length + 1, ".") + "+"
           << endl;
    }

    cout << repeat("+", m - branch_length, "-") + "." +
                repeat("+", branch_length + 1, "-")
         << endl;

    if (branch_length == m - 1) {
      cout << "+" + repeat("o", m, ".") + "+" << endl;
    } else {
      cout << "+" + repeat("o", m - 1 - branch_length, ".") + "|" +
                  repeat("o", branch_length + 1, ".") + "+"
           << endl;
    }

    if (n % 2 == 0 && i == (n / 2) - 1) {
      break;
    }

    cout << repeat("+", branch_length + 1, "-") + "." +
                repeat("+", m - branch_length, "-")
         << endl;
  }

  if (n % 2 == 1) {
    if (remain > (m - 1)) {
      // TODO
    } else {
      cout << "+" + repeat("o", m - 1, ".") + "|" + "o+" << endl;
    }
  }

  cout << repeat("+", 2 * m - 1) + "G" + "+" << endl;
}
