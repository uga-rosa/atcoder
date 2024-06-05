#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<pair<int, int>> ba(N);
  for (int i = 0; i < N; i++) {
    int a, b;
    cin >> a >> b;
    ba.at(i) = make_pair(b, a);
  }
  sort(ba.begin(), ba.end());
  for (int i = 0; i < N; i++) {
    cout << ba[i].second << " " << ba[i].first << endl;
  }
}
