#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using namespace std;

class Solver {
  int p_, height_;
  vector<int> forbidden_, allowed_, map_;
  uint64_t used_images_ = 0;
  vector<uint64_t> used_colours_;
  uint64_t nodes_ = 0;

  int mod(long long value) const {
    value %= p_;
    if (value < 0) value += p_;
    return static_cast<int>(value);
  }

  int inverse(int value) const {
    long long result = 1;
    long long base = value;
    int exponent = p_ - 2;
    while (exponent) {
      if (exponent & 1) result = result * base % p_;
      base = base * base % p_;
      exponent >>= 1;
    }
    return static_cast<int>(result);
  }

  bool valid(int row, int image) const {
    if ((used_images_ >> image) & 1ULL) return false;
    for (size_t index = 0; index < forbidden_.size(); ++index) {
      int colour = mod(image - 1LL * forbidden_[index] * row);
      if ((used_colours_[index] >> colour) & 1ULL) return false;
    }
    return true;
  }

  void insert(int row, int image) {
    map_[row] = image;
    used_images_ |= 1ULL << image;
    for (size_t index = 0; index < forbidden_.size(); ++index) {
      int colour = mod(image - 1LL * forbidden_[index] * row);
      used_colours_[index] |= 1ULL << colour;
    }
  }

  void erase(int row, int image) {
    map_[row] = -1;
    used_images_ &= ~(1ULL << image);
    for (size_t index = 0; index < forbidden_.size(); ++index) {
      int colour = mod(image - 1LL * forbidden_[index] * row);
      used_colours_[index] &= ~(1ULL << colour);
    }
  }

  bool affine() const {
    int slope = map_[1];
    for (int row = 0; row < p_; ++row) {
      if (map_[row] != mod(1LL * slope * row)) return false;
    }
    return true;
  }

  bool search(int assigned) {
    ++nodes_;
    if (assigned == p_) return !affine();

    int best_row = -1;
    vector<int> best_candidates;
    for (int row = 0; row < p_; ++row) {
      if (map_[row] >= 0) continue;
      vector<int> candidates;
      for (int image = 0; image < p_; ++image) {
        if (valid(row, image)) candidates.push_back(image);
      }
      if (candidates.empty()) return false;
      if (best_row < 0 || candidates.size() < best_candidates.size()) {
        best_row = row;
        best_candidates = move(candidates);
        if (best_candidates.size() == 1) break;
      }
    }

    for (int image : best_candidates) {
      insert(best_row, image);
      if (search(assigned + 1)) return true;
      erase(best_row, image);
    }
    return false;
  }

 public:
  Solver(int prime, int height)
      : p_(prime), height_(height), map_(prime, -1) {
    set<int> slopes;
    for (int a = 1; a <= height_; ++a) {
      for (int b = 1; b <= height_; ++b) {
        if (gcd(a, b) != 1) continue;
        int slope = 1LL * b * inverse(a) % p_;
        slopes.insert(slope);
        slopes.insert(mod(-slope));
      }
    }
    forbidden_.assign(slopes.begin(), slopes.end());
    for (int slope = 1; slope < p_; ++slope) {
      if (!slopes.count(slope)) allowed_.push_back(slope);
    }
    used_colours_.assign(forbidden_.size(), 0);
  }

  bool has_nonlinear_solution() {
    for (int slope : allowed_) {
      fill(map_.begin(), map_.end(), -1);
      used_images_ = 0;
      fill(used_colours_.begin(), used_colours_.end(), 0);
      insert(0, 0);
      insert(1, slope);
      if (search(2)) return true;
    }
    return false;
  }

  size_t forbidden_count() const { return forbidden_.size(); }
  size_t allowed_count() const { return allowed_.size(); }
  uint64_t nodes() const { return nodes_; }
};

int main() {
  const vector<pair<int, int>> cases = {
      {37, 3}, {41, 3}, {43, 3}, {47, 3}, {53, 4}};

  for (auto [prime, height] : cases) {
    Solver solver(prime, height);
    if (solver.has_nonlinear_solution()) {
      cerr << "unexpected nonlinear solution at p=" << prime
           << ", H=" << height << '\n';
      return 1;
    }
    cout << "p=" << prime << ", H=" << height
         << ": protected=" << solver.forbidden_count()
         << ", allowed=" << solver.allowed_count()
         << ", nodes=" << solver.nodes()
         << ", all solutions affine\n";
  }
  cout << "PX177 height-family rigidity census verified\n";
}
