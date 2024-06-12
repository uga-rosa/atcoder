#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (int)(s); i < (int)(n); i++)

int main() {
  int N, P, Q;
  cin >> N >> P >> Q;
  vector<int> A(N);
  rep(i, N) cin >> A[i];

  int64_t ans = 0;
  rep(i, N) rep2(j, i + 1, N) rep2(k, j + 1, N) rep2(l, k + 1, N)
      rep2(m, l + 1, N) {
    int64_t mod = A[i] % P;
    mod = mod * A[j] % P;
    mod = mod * A[k] % P;
    mod = mod * A[l] % P;
    mod = mod * A[m] % P;
    if (mod == Q) {
      ans++;
    }
  }
  cout << ans << endl;
}
