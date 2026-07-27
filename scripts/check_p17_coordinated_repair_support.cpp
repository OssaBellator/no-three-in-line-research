#include <algorithm>
#include <array>
#include <cctype>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using Point = std::pair<int, int>;

static std::string read_all(const std::string &path) {
    std::ifstream input(path);
    if (!input) throw std::runtime_error("cannot open input file");
    std::ostringstream buffer;
    buffer << input.rdbuf();
    return buffer.str();
}

static std::string bracket_value(const std::string &text, const std::string &key) {
    const std::string quoted = "\"" + key + "\"";
    std::size_t pos = text.find(quoted);
    if (pos == std::string::npos) throw std::runtime_error("missing key " + key);
    pos = text.find('[', pos + quoted.size());
    if (pos == std::string::npos) throw std::runtime_error("missing array for " + key);
    int depth = 0;
    for (std::size_t end = pos; end < text.size(); ++end) {
        if (text[end] == '[') ++depth;
        if (text[end] == ']') {
            --depth;
            if (depth == 0) return text.substr(pos, end - pos + 1);
        }
    }
    throw std::runtime_error("unterminated array for " + key);
}

static std::vector<int> parse_integers(const std::string &value) {
    std::vector<int> result;
    for (std::size_t i = 0; i < value.size();) {
        if (value[i] == '-' || std::isdigit(static_cast<unsigned char>(value[i]))) {
            bool negative = value[i] == '-';
            if (negative) ++i;
            int number = 0;
            bool found = false;
            while (i < value.size() && std::isdigit(static_cast<unsigned char>(value[i]))) {
                found = true;
                number = 10 * number + (value[i] - '0');
                ++i;
            }
            if (found) result.push_back(negative ? -number : number);
        } else {
            ++i;
        }
    }
    return result;
}

static int scalar_int(const std::string &text, const std::string &key) {
    const std::string quoted = "\"" + key + "\"";
    std::size_t pos = text.find(quoted);
    if (pos == std::string::npos) throw std::runtime_error("missing key " + key);
    pos = text.find(':', pos + quoted.size());
    if (pos == std::string::npos) throw std::runtime_error("missing scalar for " + key);
    ++pos;
    while (pos < text.size() && std::isspace(static_cast<unsigned char>(text[pos]))) ++pos;
    int sign = 1;
    if (pos < text.size() && text[pos] == '-') { sign = -1; ++pos; }
    if (pos >= text.size() || !std::isdigit(static_cast<unsigned char>(text[pos])))
        throw std::runtime_error("invalid scalar for " + key);
    int value = 0;
    while (pos < text.size() && std::isdigit(static_cast<unsigned char>(text[pos]))) {
        value = 10 * value + (text[pos] - '0');
        ++pos;
    }
    return sign * value;
}

static bool is_prime(int p) {
    if (p < 2) return false;
    if (p % 2 == 0) return p == 2;
    for (int d = 3; d * d <= p; d += 2) if (p % d == 0) return false;
    return true;
}

static long long determinant(Point a, Point b, Point c) {
    return 1LL * (b.first - a.first) * (c.second - a.second)
         - 1LL * (b.second - a.second) * (c.first - a.first);
}

static void require_permutation(const std::vector<int> &p, int n, const std::string &name) {
    if (static_cast<int>(p.size()) != n) throw std::runtime_error(name + " has wrong length");
    std::vector<int> sorted = p;
    std::sort(sorted.begin(), sorted.end());
    for (int i = 0; i < n; ++i) if (sorted[i] != i)
        throw std::runtime_error(name + " is not a permutation");
}

static std::vector<std::array<Point, 3>> bad_triples(
    const std::vector<int> &sigma, const std::vector<int> &tau, bool both_layers
) {
    const int n = static_cast<int>(sigma.size());
    std::vector<Point> points;
    for (int x = 0; x < n; ++x) points.push_back({x, sigma[x]});
    if (both_layers) for (int x = 0; x < n; ++x) points.push_back({x, tau[x]});
    std::vector<std::array<Point, 3>> bad;
    for (int i = 0; i < static_cast<int>(points.size()); ++i)
        for (int j = i + 1; j < static_cast<int>(points.size()); ++j)
            for (int k = j + 1; k < static_cast<int>(points.size()); ++k)
                if (determinant(points[i], points[j], points[k]) == 0)
                    bad.push_back({points[i], points[j], points[k]});
    return bad;
}

static std::vector<std::vector<Point>> maximal_nonaxis_lines(int n) {
    std::map<std::tuple<int, int, int>, std::vector<Point>> unique;
    for (int x1 = 0; x1 < n; ++x1) for (int y1 = 0; y1 < n; ++y1)
        for (int x2 = 0; x2 < n; ++x2) for (int y2 = 0; y2 < n; ++y2) {
            if (Point{x1, y1} >= Point{x2, y2}) continue;
            int dx = x2 - x1;
            int dy = y2 - y1;
            if (dx == 0 || dy == 0) continue;
            int g = std::gcd(std::abs(dx), std::abs(dy));
            dx /= g;
            dy /= g;
            if (dx < 0) { dx = -dx; dy = -dy; }
            int constant = dy * x1 - dx * y1;
            auto key = std::make_tuple(dx, dy, constant);
            if (unique.count(key)) continue;
            std::vector<Point> line;
            for (int x = 0; x < n; ++x) for (int y = 0; y < n; ++y)
                if (dy * x - dx * y == constant) line.push_back({x, y});
            if (line.size() >= 3) unique[key] = line;
        }
    std::vector<std::vector<Point>> lines;
    for (auto &entry : unique) lines.push_back(entry.second);
    return lines;
}

int main(int argc, char **argv) {
    try {
        if (argc != 2) throw std::runtime_error("usage: checker input.json");
        const std::string text = read_all(argv[1]);
        const int p = scalar_int(text, "p");
        if (!is_prime(p) || p != 17) throw std::runtime_error("this audit requires p=17");
        const int n = p - 1;
        auto sigma = parse_integers(bracket_value(text, "sigma"));
        auto tau = parse_integers(bracket_value(text, "tau"));
        auto valid_sigma = parse_integers(bracket_value(text, "known_valid_sigma"));
        auto valid_tau = parse_integers(bracket_value(text, "known_valid_tau"));
        auto bad_flat = parse_integers(bracket_value(text, "unique_bad_triple"));
        auto expected_counts = parse_integers(
            bracket_value(text, "expected_two_sided_candidate_counts")
        );
        const int max_support = scalar_int(text, "max_total_support");
        const int expected_upper = scalar_int(text, "expected_known_upper_support");
        if (max_support != 7) throw std::runtime_error("expected max_total_support=7");
        if (expected_counts.size() != 4) throw std::runtime_error("expected four support counts");
        for (auto *layer : {&sigma, &tau, &valid_sigma, &valid_tau})
            for (int &value : *layer) --value;
        require_permutation(sigma, n, "sigma");
        require_permutation(tau, n, "tau");
        require_permutation(valid_sigma, n, "known_valid_sigma");
        require_permutation(valid_tau, n, "known_valid_tau");
        for (int x = 0; x < n; ++x) {
            if (sigma[x] == tau[x]) throw std::runtime_error("base layers collide");
            if (valid_sigma[x] == valid_tau[x]) throw std::runtime_error("known valid layers collide");
        }
        if (!bad_triples(sigma, tau, false).empty())
            throw std::runtime_error("sigma is not individually clean");
        if (!bad_triples(tau, sigma, false).empty())
            throw std::runtime_error("tau is not individually clean");
        auto base_bad = bad_triples(sigma, tau, true);
        if (base_bad.size() != 1)
            throw std::runtime_error("base union does not have exactly one bad triple");
        if (bad_flat.size() != 6)
            throw std::runtime_error("unique_bad_triple must contain three points");
        std::set<Point> expected_bad;
        for (int i = 0; i < 3; ++i)
            expected_bad.insert({bad_flat[2 * i] - 1, bad_flat[2 * i + 1] - 1});
        std::set<Point> observed_bad(base_bad[0].begin(), base_bad[0].end());
        if (expected_bad != observed_bad) throw std::runtime_error("bad triple mismatch");
        if (!bad_triples(valid_sigma, valid_tau, true).empty())
            throw std::runtime_error("known upper certificate is not no-three");
        int upper_support = 0;
        for (int x = 0; x < n; ++x) {
            upper_support += valid_sigma[x] != sigma[x];
            upper_support += valid_tau[x] != tau[x];
        }
        if (upper_support != expected_upper)
            throw std::runtime_error("known upper support mismatch");

        const auto lines = maximal_nonaxis_lines(n);
        const int line_count = static_cast<int>(lines.size());
        std::vector<std::vector<int>> cell_lines(n * n);
        for (int line = 0; line < line_count; ++line)
            for (Point point : lines[line])
                cell_lines[point.first * n + point.second].push_back(line);
        std::vector<int> occupancy(line_count, 0);
        for (int layer = 0; layer < 2; ++layer) {
            const auto &permutation = layer == 0 ? sigma : tau;
            for (int x = 0; x < n; ++x)
                for (int line : cell_lines[x * n + permutation[x]]) ++occupancy[line];
        }
        int overloaded = 0;
        for (int value : occupancy) overloaded += value > 2;
        if (overloaded != 1)
            throw std::runtime_error("expected one overloaded maximal line");

        std::set<int> marked_sigma;
        std::set<int> marked_tau;
        for (Point point : observed_bad) {
            if (sigma[point.first] == point.second) marked_sigma.insert(point.first);
            else if (tau[point.first] == point.second) marked_tau.insert(point.first);
            else throw std::runtime_error("bad point is not selected");
        }
        if (marked_sigma.size() != 2 || marked_tau.size() != 1)
            throw std::runtime_error("unexpected bad-triple layer pattern");

        std::vector<std::vector<std::vector<int>>> subsets(max_support + 1);
        for (int mask = 0; mask < (1 << n); ++mask) {
            int size = __builtin_popcount(static_cast<unsigned>(mask));
            if (size > max_support) continue;
            std::vector<int> subset;
            for (int x = 0; x < n; ++x) if ((mask >> x) & 1) subset.push_back(x);
            subsets[size].push_back(std::move(subset));
        }
        std::vector<std::vector<std::vector<int>>> derangements(max_support + 1);
        for (int size = 0; size <= max_support; ++size) {
            std::vector<int> permutation(size);
            std::iota(permutation.begin(), permutation.end(), 0);
            do {
                bool fixed = false;
                for (int i = 0; i < size; ++i) fixed |= permutation[i] == i;
                if (!fixed) derangements[size].push_back(permutation);
            } while (std::next_permutation(permutation.begin(), permutation.end()));
        }

        std::vector<int> delta(line_count, 0);
        std::vector<int> generation_seen(line_count, 0);
        std::vector<int> touched;
        int generation = 0;
        std::array<long long, 8> checked{};
        auto candidate_is_valid = [&](const std::vector<int> &support_sigma,
                                      const std::vector<int> &move_sigma,
                                      const std::vector<int> &support_tau,
                                      const std::vector<int> &move_tau) {
            std::array<std::array<int, 16>, 2> values{};
            for (int x = 0; x < n; ++x) {
                values[0][x] = sigma[x];
                values[1][x] = tau[x];
            }
            for (int i = 0; i < static_cast<int>(support_sigma.size()); ++i)
                values[0][support_sigma[i]] = sigma[support_sigma[move_sigma[i]]];
            for (int i = 0; i < static_cast<int>(support_tau.size()); ++i)
                values[1][support_tau[i]] = tau[support_tau[move_tau[i]]];
            for (int x = 0; x < n; ++x)
                if (values[0][x] == values[1][x]) return false;

            ++generation;
            touched.clear();
            auto add_delta = [&](int line, int amount) {
                if (generation_seen[line] != generation) {
                    generation_seen[line] = generation;
                    delta[line] = 0;
                    touched.push_back(line);
                }
                delta[line] += amount;
            };
            for (int i = 0; i < static_cast<int>(support_sigma.size()); ++i) {
                int x = support_sigma[i];
                for (int line : cell_lines[x * n + sigma[x]]) add_delta(line, -1);
                for (int line : cell_lines[x * n + values[0][x]]) add_delta(line, 1);
            }
            for (int i = 0; i < static_cast<int>(support_tau.size()); ++i) {
                int x = support_tau[i];
                for (int line : cell_lines[x * n + tau[x]]) add_delta(line, -1);
                for (int line : cell_lines[x * n + values[1][x]]) add_delta(line, 1);
            }
            for (int line : touched)
                if (occupancy[line] + delta[line] > 2) return false;
            for (int line = 0; line < line_count; ++line)
                if (occupancy[line] > 2 && generation_seen[line] != generation)
                    return false;
            return true;
        };

        for (int total = 4; total <= max_support; ++total) {
            for (int a = 2; a <= total - 2; ++a) {
                int b = total - a;
                for (const auto &support_sigma : subsets[a]) {
                    bool sigma_hits = false;
                    for (int column : support_sigma)
                        sigma_hits |= marked_sigma.count(column) != 0;
                    for (const auto &support_tau : subsets[b]) {
                        bool hits = sigma_hits;
                        for (int column : support_tau)
                            hits |= marked_tau.count(column) != 0;
                        if (!hits) continue;
                        for (const auto &move_sigma : derangements[a])
                            for (const auto &move_tau : derangements[b]) {
                                ++checked[total];
                                if (candidate_is_valid(
                                        support_sigma, move_sigma, support_tau, move_tau
                                    ))
                                    throw std::runtime_error(
                                        "unexpected repair found through support seven"
                                    );
                            }
                    }
                }
            }
            if (checked[total] != expected_counts[total - 4])
                throw std::runtime_error(
                    "candidate count mismatch at support " + std::to_string(total)
                );
        }

        long long total_checked = 0;
        for (int total = 4; total <= max_support; ++total)
            total_checked += checked[total];
        std::cout << "{\n"
                  << "  \"outcome\": \"no_two_sided_repair_through_support_7\",\n"
                  << "  \"p\": 17,\n"
                  << "  \"max_total_support_checked\": 7,\n"
                  << "  \"candidate_counts\": {\n"
                  << "    \"4\": " << checked[4] << ",\n"
                  << "    \"5\": " << checked[5] << ",\n"
                  << "    \"6\": " << checked[6] << ",\n"
                  << "    \"7\": " << checked[7] << "\n"
                  << "  },\n"
                  << "  \"total_candidates_checked\": " << total_checked << ",\n"
                  << "  \"known_valid_upper_support\": " << upper_support << ",\n"
                  << "  \"one_sided_nonextension_dependency\": \"PP3bdw\",\n"
                  << "  \"minimum_repair_support_lower_bound\": 8,\n"
                  << "  \"asymptotic_seed_theorem_proved\": false\n"
                  << "}\n";
    } catch (const std::exception &error) {
        std::cerr << "verification failed: " << error.what() << "\n";
        return 1;
    }
    return 0;
}
