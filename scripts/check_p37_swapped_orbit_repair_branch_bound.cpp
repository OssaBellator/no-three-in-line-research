// Exact branch-and-bound for canonical swapped-orbit repairs of the p=37 near-state.
//
// Compile:
//   g++ -O3 -std=c++17 scripts/check_p37_swapped_orbit_repair_branch_bound.cpp \
//     -o /tmp/check_p37_orbit_branch
//
// Run one exact support and one subset-index shard:
//   /tmp/check_p37_orbit_branch INPUT_JSON SUPPORT SHARD SHARDS

#include <algorithm>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using Point = std::pair<int, int>;

struct Option {
    int source = -1;
    int target = -1;
    int orientation = -1;
    int orbit_id = -1;
    std::vector<std::pair<int, std::uint8_t>> line_counts;
};

std::vector<int> parse_integer_array(const std::string& text, const std::string& key) {
    const std::string quoted = "\"" + key + "\"";
    const std::size_t key_pos = text.find(quoted);
    if (key_pos == std::string::npos) {
        throw std::runtime_error("missing JSON key " + key);
    }
    const std::size_t left = text.find('[', key_pos + quoted.size());
    const std::size_t right = text.find(']', left == std::string::npos ? left : left + 1);
    if (left == std::string::npos || right == std::string::npos) {
        throw std::runtime_error("malformed JSON array for " + key);
    }

    std::vector<int> values;
    std::size_t pos = left + 1;
    while (pos < right) {
        while (pos < right && (text[pos] == ' ' || text[pos] == '\n' ||
                               text[pos] == '\r' || text[pos] == '\t' ||
                               text[pos] == ',')) {
            ++pos;
        }
        if (pos >= right) {
            break;
        }
        bool negative = false;
        if (text[pos] == '-') {
            negative = true;
            ++pos;
        }
        if (pos >= right || text[pos] < '0' || text[pos] > '9') {
            throw std::runtime_error("noninteger JSON array entry for " + key);
        }
        int value = 0;
        while (pos < right && text[pos] >= '0' && text[pos] <= '9') {
            value = 10 * value + (text[pos] - '0');
            ++pos;
        }
        values.push_back(negative ? -value : value);
    }
    return values;
}

int main(int argc, char** argv) {
    try {
        if (argc != 5) {
            throw std::runtime_error(
                "usage: INPUT_JSON SUPPORT SHARD SHARDS"
            );
        }
        const std::string input_path = argv[1];
        const int support_size = std::stoi(argv[2]);
        const int shard = std::stoi(argv[3]);
        const int shard_count = std::stoi(argv[4]);
        if (support_size < 1 || support_size > 18) {
            throw std::runtime_error("SUPPORT must lie in 1..18");
        }
        if (shard_count < 1 || shard < 0 || shard >= shard_count) {
            throw std::runtime_error("expected 0 <= SHARD < SHARDS");
        }

        std::ifstream input(input_path);
        if (!input) {
            throw std::runtime_error("cannot open input JSON");
        }
        const std::string text(
            (std::istreambuf_iterator<char>(input)),
            std::istreambuf_iterator<char>()
        );

        constexpr int n = 36;
        constexpr int m = 18;
        std::vector<int> rho = parse_integer_array(text, "pair_permutation");
        std::vector<int> orientation = parse_integer_array(text, "pair_orientations");
        std::vector<int> bad_owners = parse_integer_array(text, "bad_orbit_owners");
        if (rho.size() != m || orientation.size() != m) {
            throw std::runtime_error("expected 18 pair assignments and orientations");
        }
        std::vector<int> sorted_rho = rho;
        std::sort(sorted_rho.begin(), sorted_rho.end());
        for (int i = 0; i < m; ++i) {
            if (sorted_rho[i] != i + 1) {
                throw std::runtime_error("pair_permutation must be one-based permutation 1..18");
            }
            --rho[i];
            if (orientation[i] != 0 && orientation[i] != 1) {
                throw std::runtime_error("pair orientations must be bits");
            }
        }
        if (bad_owners.empty()) {
            throw std::runtime_error("expected at least one bad orbit owner");
        }
        std::uint32_t bad_owner_mask = 0;
        for (int owner : bad_owners) {
            if (owner < 1 || owner > m) {
                throw std::runtime_error("bad orbit owner outside 1..18");
            }
            bad_owner_mask |= std::uint32_t(1) << (owner - 1);
        }

        auto reversal = [](int coordinate) { return n - 1 - coordinate; };
        auto orbit_cells = [&](int source, int target, int sign) {
            std::vector<Point> cells;
            if (sign == 0) {
                cells = {
                    {source, target},
                    {reversal(source), reversal(target)},
                    {target, reversal(source)},
                    {reversal(target), source},
                };
            } else {
                cells = {
                    {source, reversal(target)},
                    {reversal(source), target},
                    {target, source},
                    {reversal(target), reversal(source)},
                };
            }
            std::sort(cells.begin(), cells.end());
            cells.erase(std::unique(cells.begin(), cells.end()), cells.end());
            return cells;
        };

        // Generate every maximal nonaxis grid line with at least three board cells.
        std::vector<std::vector<int>> cell_lines(n * n);
        int line_count = 0;
        for (int dx = 1; dx < n; ++dx) {
            for (int dy = -(n - 1); dy < n; ++dy) {
                if (dy == 0 || std::gcd(dx, std::abs(dy)) != 1) {
                    continue;
                }
                for (int x = 0; x < n; ++x) {
                    for (int y = 0; y < n; ++y) {
                        const int previous_x = x - dx;
                        const int previous_y = y - dy;
                        if (0 <= previous_x && previous_x < n &&
                            0 <= previous_y && previous_y < n) {
                            continue;
                        }
                        std::vector<Point> line;
                        for (int current_x = x, current_y = y;
                             0 <= current_x && current_x < n &&
                             0 <= current_y && current_y < n;
                             current_x += dx, current_y += dy) {
                            line.push_back({current_x, current_y});
                        }
                        if (line.size() < 3) {
                            continue;
                        }
                        for (const auto& [line_x, line_y] : line) {
                            cell_lines[line_x * n + line_y].push_back(line_count);
                        }
                        ++line_count;
                    }
                }
            }
        }
        if (line_count != 70726) {
            throw std::runtime_error("unexpected maximal nonaxis line count");
        }

        auto canonical_orbit_id = [](int source, int target, int sign) {
            if (source == target) {
                return source * m + source;
            }
            if (source < target) {
                return m * m + 2 * (source * m + target) + sign;
            }
            return m * m + 2 * (target * m + source) + (1 - sign);
        };

        std::vector<Option> options;
        std::vector<std::vector<std::vector<int>>> by_source_target(
            m, std::vector<std::vector<int>>(m)
        );
        for (int source = 0; source < m; ++source) {
            for (int target = 0; target < m; ++target) {
                const int orientation_count = source == target ? 1 : 2;
                for (int sign = 0; sign < orientation_count; ++sign) {
                    std::unordered_map<int, int> counts;
                    for (const auto& [x, y] : orbit_cells(source, target, sign)) {
                        for (int line : cell_lines[x * n + y]) {
                            ++counts[line];
                        }
                    }
                    Option option;
                    option.source = source;
                    option.target = target;
                    option.orientation = sign;
                    option.orbit_id = canonical_orbit_id(source, target, sign);
                    option.line_counts.reserve(counts.size());
                    for (const auto& [line, count] : counts) {
                        option.line_counts.push_back(
                            {line, static_cast<std::uint8_t>(count)}
                        );
                    }
                    const int option_id = static_cast<int>(options.size());
                    options.push_back(std::move(option));
                    by_source_target[source][target].push_back(option_id);
                }
            }
        }

        std::vector<int> base_option(m, -1);
        std::vector<int> base_occupancy(line_count, 0);
        for (int source = 0; source < m; ++source) {
            const int target = rho[source];
            const int sign = source == target ? 0 : orientation[source];
            for (int option_id : by_source_target[source][target]) {
                if (options[option_id].orientation == sign) {
                    base_option[source] = option_id;
                }
            }
            if (base_option[source] < 0) {
                throw std::runtime_error("could not reconstruct base orbit option");
            }
            for (const auto& [line, count] : options[base_option[source]].line_counts) {
                base_occupancy[line] += count;
            }
        }

        std::vector<int> base_bad_lines;
        for (int line = 0; line < line_count; ++line) {
            if (base_occupancy[line] > 2) {
                base_bad_lines.push_back(line);
            }
        }
        if (base_bad_lines.size() != 4) {
            throw std::runtime_error("expected exactly four overloaded base lines");
        }

        std::uint64_t subset_ordinal = 0;
        std::uint64_t processed_subsets = 0;
        std::uint64_t search_nodes = 0;
        std::uint64_t hall_failures = 0;
        std::uint64_t initial_domain_failures = 0;
        bool found = false;
        std::vector<int> found_support;
        std::vector<int> found_options;

        std::vector<int> support(support_size);
        std::iota(support.begin(), support.end(), 0);
        auto next_combination = [&]() {
            int position = support_size - 1;
            while (position >= 0 &&
                   support[position] == m - support_size + position) {
                --position;
            }
            if (position < 0) {
                return false;
            }
            ++support[position];
            for (int next = position + 1; next < support_size; ++next) {
                support[next] = support[next - 1] + 1;
            }
            return true;
        };

        do {
            std::uint32_t support_mask = 0;
            for (int source : support) {
                support_mask |= std::uint32_t(1) << source;
            }
            if ((support_mask & bad_owner_mask) == 0) {
                ++subset_ordinal;
                continue;
            }
            const std::uint64_t ordinal = subset_ordinal++;
            if (ordinal % shard_count != static_cast<std::uint64_t>(shard)) {
                continue;
            }
            ++processed_subsets;

            std::vector<char> in_support(m, false);
            std::uint32_t target_mask = 0;
            for (int source : support) {
                in_support[source] = true;
                target_mask |= std::uint32_t(1) << rho[source];
            }

            std::vector<int> occupancy = base_occupancy;
            std::unordered_set<int> used_orbits;
            for (int source = 0; source < m; ++source) {
                if (!in_support[source]) {
                    used_orbits.insert(options[base_option[source]].orbit_id);
                }
            }
            for (int source : support) {
                for (const auto& [line, count] : options[base_option[source]].line_counts) {
                    occupancy[line] -= count;
                }
            }

            std::vector<std::vector<int>> candidates(m);
            bool impossible = false;
            for (int source : support) {
                for (int target = 0; target < m; ++target) {
                    if (((target_mask >> target) & 1U) == 0) {
                        continue;
                    }
                    for (int option_id : by_source_target[source][target]) {
                        const Option& option = options[option_id];
                        if (option_id == base_option[source] ||
                            used_orbits.count(option.orbit_id)) {
                            continue;
                        }
                        bool legal = true;
                        for (const auto& [line, count] : option.line_counts) {
                            if (occupancy[line] + count > 2) {
                                legal = false;
                                break;
                            }
                        }
                        if (legal) {
                            candidates[source].push_back(option_id);
                        }
                    }
                }
                if (candidates[source].empty()) {
                    impossible = true;
                    ++initial_domain_failures;
                    break;
                }
            }
            if (impossible) {
                continue;
            }

            std::vector<char> assigned(m, false);
            std::vector<int> chosen;
            std::uint32_t used_targets = 0;

            std::function<bool()> search = [&]() -> bool {
                ++search_nodes;
                if (chosen.size() == support.size()) {
                    for (int line : base_bad_lines) {
                        if (occupancy[line] > 2) {
                            return false;
                        }
                    }
                    found_support = support;
                    found_options = chosen;
                    return true;
                }

                int best_source = -1;
                std::vector<int> best_available;
                std::vector<std::pair<int, std::uint32_t>> remaining_target_domains;

                for (int source : support) {
                    if (assigned[source]) {
                        continue;
                    }
                    std::vector<int> available;
                    std::uint32_t target_domain = 0;
                    for (int option_id : candidates[source]) {
                        const Option& option = options[option_id];
                        if (((used_targets >> option.target) & 1U) != 0 ||
                            used_orbits.count(option.orbit_id)) {
                            continue;
                        }
                        bool legal = true;
                        for (const auto& [line, count] : option.line_counts) {
                            if (occupancy[line] + count > 2) {
                                legal = false;
                                break;
                            }
                        }
                        if (legal) {
                            available.push_back(option_id);
                            target_domain |= std::uint32_t(1) << option.target;
                        }
                    }
                    if (available.empty()) {
                        return false;
                    }
                    remaining_target_domains.push_back({source, target_domain});
                    if (best_source < 0 || available.size() < best_available.size()) {
                        best_source = source;
                        best_available = std::move(available);
                    }
                }

                // Exact Hall test on the remaining source-to-target domains.
                std::vector<int> target_match(m, -1);
                std::function<bool(int, std::vector<char>&)> augment =
                    [&](int source_index, std::vector<char>& seen) {
                        const std::uint32_t domain =
                            remaining_target_domains[source_index].second;
                        for (int target = 0; target < m; ++target) {
                            if (((domain >> target) & 1U) == 0 || seen[target]) {
                                continue;
                            }
                            seen[target] = true;
                            if (target_match[target] < 0 ||
                                augment(target_match[target], seen)) {
                                target_match[target] = source_index;
                                return true;
                            }
                        }
                        return false;
                    };
                for (int source_index = 0;
                     source_index < static_cast<int>(remaining_target_domains.size());
                     ++source_index) {
                    std::vector<char> seen(m, false);
                    if (!augment(source_index, seen)) {
                        ++hall_failures;
                        return false;
                    }
                }

                std::sort(
                    best_available.begin(),
                    best_available.end(),
                    [&](int left_id, int right_id) {
                        int left_score = 0;
                        int right_score = 0;
                        for (const auto& [line, count] : options[left_id].line_counts) {
                            left_score += occupancy[line] * count;
                        }
                        for (const auto& [line, count] : options[right_id].line_counts) {
                            right_score += occupancy[line] * count;
                        }
                        return left_score < right_score;
                    }
                );

                assigned[best_source] = true;
                for (int option_id : best_available) {
                    const Option& option = options[option_id];
                    used_targets |= std::uint32_t(1) << option.target;
                    used_orbits.insert(option.orbit_id);
                    for (const auto& [line, count] : option.line_counts) {
                        occupancy[line] += count;
                    }
                    chosen.push_back(option_id);

                    if (search()) {
                        return true;
                    }

                    chosen.pop_back();
                    for (const auto& [line, count] : option.line_counts) {
                        occupancy[line] -= count;
                    }
                    used_orbits.erase(option.orbit_id);
                    used_targets &= ~(std::uint32_t(1) << option.target);
                }
                assigned[best_source] = false;
                return false;
            };

            if (search()) {
                found = true;
                break;
            }
        } while (next_combination());

        std::cout
            << "support=" << support_size
            << " shard=" << shard
            << " shards=" << shard_count
            << " subsets=" << processed_subsets
            << " nodes=" << search_nodes
            << " hall_failures=" << hall_failures
            << " initial_domain_failures=" << initial_domain_failures
            << " found=" << (found ? 1 : 0);
        if (found) {
            std::cout << " support_set=";
            for (int source : found_support) {
                std::cout << (source + 1) << ',';
            }
            std::cout << " choices=";
            for (int option_id : found_options) {
                const Option& option = options[option_id];
                std::cout
                    << (option.source + 1) << ':'
                    << (option.target + 1) << ':'
                    << option.orientation << ',';
            }
        }
        std::cout << '\n';
        return 0;
    } catch (const std::exception& exc) {
        std::cerr << "verification failed: " << exc.what() << '\n';
        return 2;
    }
}
