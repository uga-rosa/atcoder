#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = int64_t;

struct Node {
  unordered_map<char, Node *> children;
  int pass_c = 1;
};

struct Tree {
  Node *root;
  ll ans = 0;

  Tree() { root = new Node(); }

  void insert(string word) {
    auto cur = root;
    for (char c : word) {
      if (cur->children.contains(c)) {
        cur = cur->children[c];
        ans += cur->pass_c;
        cur->pass_c++;
      } else {
        cur->children[c] = new Node();
        cur = cur->children[c];
      }
    }
  };
};

int main() {
  int n;
  cin >> n;
  vector<string> s(n);
  rep(i, n) cin >> s[i];

  auto tree = new Tree();
  rep(i, n) { tree->insert(s[i]); }
  cout << tree->ans << endl;
}
