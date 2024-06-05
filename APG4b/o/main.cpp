#include <bits/stdc++.h>
using namespace std;
#define max(vec) *max_element(vec.begin(), vec.end())
#define min(vec) *min_element(vec.begin(), vec.end())

int main() {
  int A, B, C;
  cin >> A >> B >> C;
  vector<int> vec = {A, B, C};

  cout << max(vec) - min(vec) << endl;
}
