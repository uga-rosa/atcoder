#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = (l); i < (int)(r); i++)
int n;
vector<int> a, c;

void merge_sort(int l = 0, int r = n) {
  if (r - l == 1) {
    return;
  }
  int m = (l + r) / 2;
  merge_sort(l, m);
  merge_sort(m, r);

  int i = l, j = m, cnt = 0;
  while (i < m || j < r) {
    if (i == m) {
      c[cnt] = a[j];
      j++;
    } else if (j == r) {
      c[cnt] = a[i];
      i++;
    } else {
      if (a[i] <= a[j]) {
        c[cnt] = a[i];
        i++;
      } else {
        c[cnt] = a[j];
        j++;
      }
    }
    cnt++;
  }

  rep(i, 0, cnt) a[l + i] = c[i];
}

int main() {
  cin >> n;
  a.resize(n);
  c.resize(n);
  rep(i, 0, n) cin >> a[i];
  merge_sort();
  rep(i, 0, n) cout << a[i] << (i == n - 1 ? "\n" : " ");
}
