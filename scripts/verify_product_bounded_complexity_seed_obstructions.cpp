#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

namespace {

int mod_pow(int base, int exponent, int modulus) {
    std::int64_t result = 1;
    std::int64_t value = base % modulus;
    while (exponent > 0) {
        if (exponent & 1) result = result * value % modulus;
        value = value * value % modulus;
        exponent >>= 1;
    }
    return static_cast<int>(result);
}

bool mark_three(
    std::vector<unsigned char>& image,
    std::vector<unsigned char>& minus,
    std::vector<unsigned char>& plus,
    int x,
    int y,
    int p
) {
    const int ym = (y - x + p) % p;
    const int yp = (y + x) % p;
    if (image[y] || minus[ym] || plus[yp]) return false;
    image[y] = minus[ym] = plus[yp] = 1;
    return true;
}

std::int64_t strong_cubic_count(int p) {
    std::int64_t count = 0;
    for (int a = 1; a < p; ++a) {
        for (int b = 0; b < p; ++b) {
            for (int c = 0; c < p; ++c) {
                std::vector<unsigned char> image(p), minus(p), plus(p);
                bool ok = true;
                for (int x = 0; x < p; ++x) {
                    const std::int64_t xx = x;
                    const int y = static_cast<int>(
                        (static_cast<std::int64_t>(a) * xx % p * xx % p * xx
                         + static_cast<std::int64_t>(b) * xx % p * xx
                         + static_cast<std::int64_t>(c) * xx) % p
                    );
                    if (!mark_three(image, minus, plus, x, y, p)) {
                        ok = false;
                        break;
                    }
                }
                if (ok) ++count;
            }
        }
    }
    return count;
}

std::int64_t strong_completed_mobius_count(int p) {
    std::vector<int> inverse(p);
    for (int x = 1; x < p; ++x) inverse[x] = mod_pow(x, p - 2, p);

    std::int64_t count = 0;
    for (int a = 0; a < p; ++a) {
        for (int b = 0; b < p; ++b) {
            for (int d = 0; d < p; ++d) {
                if ((static_cast<std::int64_t>(a) * d - b) % p == 0) continue;
                std::vector<unsigned char> image(p), minus(p), plus(p);
                bool ok = true;
                for (int x = 0; x < p; ++x) {
                    const int denominator = (x + d) % p;
                    const int y = denominator == 0
                        ? a
                        : static_cast<int>(
                            static_cast<std::int64_t>((a * x + b) % p)
                            * inverse[denominator] % p
                        );
                    if (!mark_three(image, minus, plus, x, y, p)) {
                        ok = false;
                        break;
                    }
                }
                if (ok) ++count;
            }
        }
    }
    return count;
}

}  // namespace

int main() {
    const std::array<int, 24> primes = {
        5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61,
        67, 71, 73, 79, 83, 89, 97, 101
    };

    for (const int p : primes) {
        const auto cubic = strong_cubic_count(p);
        const auto mobius = strong_completed_mobius_count(p);
        if (cubic != 0 || mobius != 0) {
            std::cerr << "unexpected seed at p=" << p
                      << ": cubic=" << cubic
                      << ", mobius=" << mobius << '\n';
            return 1;
        }
        std::cout << "p=" << p << ": cubic=0, completed-Mobius=0\n";
    }

    std::cout << "PX137 bounded-complexity seed obstructions verified\n";
    return 0;
}
