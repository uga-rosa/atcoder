#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = int64_t;

int binary_search(int n, function<bool(int)> isok) {
  int ng, ok, mid;
  ng = -1;
  ok = n;
  while (ok - ng > 1) {
    mid = (ok + ng) / 2;
    (isok(mid) ? ok : ng) = mid;
  }
  return ok;
}

int main() {
  int MOD = 1e8;
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];

  // 全ての組み合わせに対して (x+y) の mod の総和
  // a の要素の登場回数はそれぞれ n-1
  // (n-1) * n[i] を n 周するので sum < 9*10**18 < 2**63-1 であり、ループ途中に
  // mod を取らなくても over flow しない。 制約から、(x+y) の mod は、1回 MOD
  // を引くか引かないか つまり、何回引かれるか (足したら MOD
  // を越える組み合わせはいくつあるか) を知りたい。 これは a
  // をソートしておけば、各要素につき O(log n) で求まる (2分探索) ソート自体も
  // O(n log n) なので、全体の計算量は O(n log n) で十分高速
  sort(a.begin(), a.end());
  ll sum = 0;
  int j;
  rep(i, n) {
    sum += (n - 1) * a[i];
    j = binary_search(n, [a, MOD, i](int x) { return a[x] >= MOD - a[i]; });
    j = max(j, i + 1);
    sum -= (n - j) * MOD;
  }
  cout << sum << endl;
}
