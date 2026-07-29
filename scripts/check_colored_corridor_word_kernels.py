#!/usr/bin/env python3
from fractions import Fraction
import json

banks = {
    0: {
        "a0": ("a00", "a01", "shared01"),
        "a1": ("a10", "a11", "shared02"),
    },
    1: {
        "b0": ("b00", "b01", "shared01"),
        "b1": ("b10", "b11", "shared12"),
    },
    2: {
        "c0": ("c00", "c01", "shared02"),
        "c1": ("c10", "c11", "shared12"),
    },
}

def column_loads(data):
    loads = {}
    bank_loads = {}
    supports = {}
    for i, rows in data.items():
        local = {}
        supports[i] = set()
        for x, words in rows.items():
            p = Fraction(1, len(words))
            for y in words:
                loads[y] = loads.get(y, Fraction(0)) + p
                local[y] = local.get(y, Fraction(0)) + p
                supports[i].add(y)
        bank_loads[i] = max(local.values())
    overlap = max(sum(y in supports[i] for i in supports) for y in loads)
    return loads, bank_loads, overlap

loads, bank_loads, g = column_loads(banks)
assert max(bank_loads.values()) == Fraction(1, 3)
assert g == 2
assert max(loads.values()) == Fraction(2, 3)
assert max(loads.values()) <= Fraction(g, 3)

conditioned = {
    i: {x: (words[0], words[2]) for x, words in rows.items()}
    for i, rows in banks.items()
}
cloads, cbank, cg = column_loads(conditioned)
assert max(cbank.values()) == Fraction(1, 2)
assert cg == 2
assert max(cloads.values()) == 1

print(json.dumps({
    "all_checks_passed": True,
    "banks": len(banks),
    "words_per_source": 3,
    "within_bank_h": 1,
    "bank_support_overlap_g": g,
    "combined_exact_load": str(max(loads.values())),
    "combined_bound": str(Fraction(2, 3)),
    "conditioned_words_per_source": 2,
    "conditioned_exact_load": str(max(cloads.values())),
}, indent=2))
