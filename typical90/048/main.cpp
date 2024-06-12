#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N, K, a, b;
  cin >> N >> K;

  vector<int> S(2*N);
  rep(i, N) {
    cin >> a >> b;
    S[2*i] = b;
    S[2*i+1] = a - b;
  }
  // B[i] > A[i] - B[i] なので、部分点を選ぶ前に満点を選ぶことはない
  sort(S.begin(), S.end(), greater());

  int64_t ans = 0;
  rep(i, K) ans += S[i];
  cout << ans << endl;
}
