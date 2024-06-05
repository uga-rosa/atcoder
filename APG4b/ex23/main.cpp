#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  map<int, int> cnt;
  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
    cnt[A.at(i)]++;
  }

  int max_a = 0, max_cnt = 0;
  for (int i = 0; i < N; i++) {
    int a = A.at(i);
    if (cnt[a] > max_cnt) {
      max_a = a;
      max_cnt = cnt[a];
    }
  }
  cout << max_a << " " << max_cnt << endl;
}
