#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
using namespace std;

struct Point {
  int x;
  int y;
};

long long cross(Point a, Point b, Point c) {
  return 1LL * (b.x - a.x) * (c.y - a.y) -
         1LL * (b.y - a.y) * (c.x - a.x);
}

array<Point, 4> orbit_block(int m, int source, int target, int orientation) {
  const int n = 2 * m;
  auto reversal = [n](int x) { return n - 1 - x; };
  Point q0{source, orientation ? reversal(target) : target};
  Point q1{reversal(source), orientation ? target : reversal(target)};
  return {q0, q1, Point{reversal(q0.y), q0.x},
          Point{reversal(q1.y), q1.x}};
}

bool two_owner_bad(int m, int sa, int ta, int ea,
                   int sb, int tb, int eb) {
  auto a = orbit_block(m, sa, ta, ea);
  auto b = orbit_block(m, sb, tb, eb);
  array<Point, 8> points{};
  for (int i = 0; i < 4; ++i) {
    points[i] = a[i];
    points[i + 4] = b[i];
  }
  for (int i = 0; i < 8; ++i)
    for (int j = i + 1; j < 8; ++j)
      for (int k = j + 1; k < 8; ++k)
        if (cross(points[i], points[j], points[k]) == 0) return true;
  return false;
}

bool classified_impossible(int m, int sa, int ta, int sb, int tb) {
  const long long u = 2LL * m - 1 - 2 * sa;
  const long long v = 2LL * m - 1 - 2 * ta;
  const long long x = 2LL * m - 1 - 2 * sb;
  const long long y = 2LL * m - 1 - 2 * tb;

  const bool direct_ray = u * y == v * x;
  const bool swapped_ray = u * x == v * y;
  if (!direct_ray && !swapped_ray) return false;

  const long long scale = std::gcd(u, v);
  const long long a = u / scale;
  const long long b = v / scale;
  const long long k = scale;
  long long l = 0;

  if (direct_ray) {
    if (x % a || y % b || x / a != y / b) return false;
    l = x / a;
  } else {
    if (x % b || y % a || x / b != y / a) return false;
    l = x / b;
  }

  const long long r = a * a + b * b;
  const long long d_plus = llabs(a * a + 2 * a * b - b * b);
  const long long d_minus = llabs(a * a - 2 * a * b - b * b);
  return r * k == d_plus * l || r * l == d_plus * k ||
         r * k == d_minus * l || r * l == d_minus * k;
}

int main() {
  const map<int, int> expected = {
      {4,0},{5,0},{6,0},{7,0},{8,4},{9,4},{10,4},{11,8},{12,8},
      {13,8},{14,8},{15,8},{16,8},{17,8},{18,8},{19,8},{20,8},
      {21,8},{22,8},{23,12},{24,12},{25,12},{26,12},{27,12},
      {28,12},{29,12},{30,12},{31,12},{32,16},{33,20},{34,20},
      {35,20},{36,20},{37,20},{38,24},{39,24},{40,24},{41,24},
      {42,24},{43,32},{44,32},{45,32},{46,32},{47,32},{48,32},
      {49,32},{50,32},{51,32},{52,32},{53,40},{54,40},{55,40},
      {56,40},{57,40},{58,44},{59,44},{60,44},{61,44},{62,44},
      {63,44},{64,44},{65,44},{66,44},{67,44},{68,48},{69,48},
      {70,48},{71,48},{72,48},{73,48},{74,52},{75,52},{76,52},
      {77,52},{78,52},{79,52},{80,52}};

  cout << "{\n  \"cases\": [\n";
  bool first = true;
  for (int m = 4; m <= 80; ++m) {
    int count = 0;
    for (int sa = 0; sa < m; ++sa)
      for (int ta = 0; ta < m; ++ta) {
        if (ta == sa) continue;
        for (int sb = sa + 1; sb < m; ++sb)
          for (int tb = 0; tb < m; ++tb) {
            if (tb == sb || tb == ta) continue;
            const bool actual =
                two_owner_bad(m, sa, ta, 0, sb, tb, 0) &&
                two_owner_bad(m, sa, ta, 0, sb, tb, 1);
            const bool predicted = classified_impossible(m, sa, ta, sb, tb);
            if (actual != predicted) {
              cerr << "classification mismatch at m=" << m << " tuple="
                   << sa << ',' << ta << ',' << sb << ',' << tb << '\n';
              return 1;
            }
            if (actual) ++count;
          }
      }
    if (count != expected.at(m)) {
      cerr << "count mismatch at m=" << m << '\n';
      return 2;
    }
    if (!first) cout << ",\n";
    first = false;
    cout << "    {\"m\": " << m
         << ", \"impossible_compatible_owner_pairs\": " << count << '}';
  }
  cout << "\n  ],\n"
       << "  \"centered_ray_multiplier_classification_verified\": true,\n"
       << "  \"maximum_pair_size\": 80,\n"
       << "  \"asymptotic_seed_theorem_proved\": false\n}\n";
}
