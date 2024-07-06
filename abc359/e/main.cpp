#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;
using mint = modint998244353;

class SegmentTree {
private:
  int n;
  vector<int> data;
  vector<int> indices;

  void build(int node, int start, int end, const vector<int> &arr) {
    if (start == end) {
      data[node] = arr[start];
      indices[node] = start;
    } else {
      int mid = (start + end) / 2;
      build(2 * node, start, mid, arr);
      build(2 * node + 1, mid + 1, end, arr);
      if (data[2 * node] >= data[2 * node + 1]) {
        data[node] = data[2 * node];
        indices[node] = indices[2 * node];
      } else {
        data[node] = data[2 * node + 1];
        indices[node] = indices[2 * node + 1];
      }
    }
  }

  pair<int, int> query(int node, int start, int end, int l, int r, int k) {
    if (r < start || end < l) {
      return {INT_MIN, -1}; // 範囲外
    }
    if (l <= start && end <= r) {
      if (data[node] >= k) {
        return {data[node], indices[node]};
      } else {
        return {INT_MIN, -1};
      }
    }
    int mid = (start + end) / 2;
    auto left_result = query(2 * node, start, mid, l, r, k);
    auto right_result = query(2 * node + 1, mid + 1, end, l, r, k);
    if (left_result.first >= k && right_result.first >= k) {
      if (left_result.second < right_result.second) {
        return left_result;
      } else {
        return right_result;
      }
    } else if (left_result.first >= k) {
      return left_result;
    } else {
      return right_result;
    }
  }

public:
  SegmentTree(const vector<int> &arr) {
    n = arr.size();
    data.resize(4 * n, INT_MIN);
    indices.resize(4 * n, -1);
    build(1, 0, n - 1, arr);
  }

  int findIndex(int l, int r, int k) {
    auto result = query(1, 0, n - 1, l, r - 1, k);
    return result.second;
  }
};

int main() {
  int n;
  cin >> n;
  vector<int> h(n);
  rep(i, 0, n) cin >> h[i];

  SegmentTree st(h);
  rep(i, 0, n) {
    mint ans = 0;
    while (i >= 0) {
      int j = st.findIndex(0, i, h[i]);
      ans += (i - j) * h[i];
      i = j;
    }
    cout << ans.val() << endl;
  }
}
