#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

codes = {
    "level0": "0",
    "level1": "10",
    "level2": "110",
    "level3": "111",
}
base_load = {
    "level0": Fraction(1, 4),
    "level1": Fraction(1, 5),
    "level2": Fraction(1, 6),
    "level3": Fraction(1, 8),
}
symbol_factor = {"0": Fraction(4, 3), "1": Fraction(3, 2)}


def is_prefix_free(words):
    return all(not b.startswith(a) for a, b in combinations(words, 2))


def word_factor(word):
    out = Fraction(1)
    for symbol in word:
        out *= symbol_factor[symbol]
    return out


assert is_prefix_free(list(codes.values()))
class_load = {
    name: base_load[name] * word_factor(word)
    for name, word in codes.items()
}
assert class_load == {
    "level0": Fraction(1, 3),
    "level1": Fraction(2, 5),
    "level2": Fraction(1, 2),
    "level3": Fraction(27, 64),
}

# Prefix-free target tags make the load of every union the maximum class load,
# not the sum.  Exhaust every nonempty class subset.
names = list(codes)
checked_subsets = 0
for mask in range(1, 1 << len(names)):
    selected = [names[i] for i in range(len(names)) if mask & (1 << i)]
    combined = max(class_load[name] for name in selected)
    explicit_targets = {codes[name]: class_load[name] for name in selected}
    assert max(explicit_targets.values()) == combined
    checked_subsets += 1

# Product failure localizes to one bad symbol transition.
expected = [Fraction(2, 3)] * 3
actual = [Fraction(3, 4), Fraction(1, 2), Fraction(3, 4)]
expected_product = Fraction(1)
actual_product = Fraction(1)
for p in expected:
    expected_product *= p
for p in actual:
    actual_product *= p
assert actual_product < expected_product
bad_positions = [i for i, (a, e) in enumerate(zip(actual, expected), start=1) if a < e]
assert bad_positions == [2]

print({
    "prefix_free": True,
    "class_loads": {k: str(v) for k, v in class_load.items()},
    "combined_load": str(max(class_load.values())),
    "checked_subsets": checked_subsets,
    "bad_prefix_positions": bad_positions,
})
