#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = int64_t;

int main() {
  int N;
  cin >> N;
  vector<int> A(N), B(N), C(N);
  rep(i, N) cin >> A[i];
  rep(i, N) cin >> B[i];
  rep(i, N) cin >> C[i];
  vector<int> am(46), bm(46), cm(46);
  rep(i, N) {
    am[A[i] % 46]++;
    bm[B[i] % 46]++;
    cm[C[i] % 46]++;
  }

  ll ans = 0;
  rep(i, 46) rep(j, 46) rep(k, 46) {
    if ((i + j + k) % 46 == 0) {
      ans += (ll)am[i] * bm[j] * cm[k];
    }
  }
  cout << ans << endl;
}
