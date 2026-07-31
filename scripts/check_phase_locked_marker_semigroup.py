#!/usr/bin/env python3

MAX_N = 1000


def representations(n):
    return [(a, b) for b in range(n // 7 + 1) if (n - 7 * b) % 4 == 0 for a in [(n - 7 * b) // 4]]


def phase_locked_representations(n, phase):
    return [(a, b) for a, b in representations(n) if b % 3 == phase]

apery = []
for residue in range(4):
    value = next(n for n in range(500) if n % 4 == residue and any(n == 4 * a + 21 * c for a in range(n // 4 + 1) for c in range(n // 21 + 1)))
    apery.append(value)
assert tuple(apery) == (0, 21, 42, 63)
conductor = max(apery) - 4 + 1
assert conductor == 60

thresholds = {}
for phase in range(3):
    threshold = 60 + 7 * phase
    thresholds[phase] = threshold
    assert not phase_locked_representations(threshold - 1, phase)
    for n in range(threshold, MAX_N + 1):
        assert phase_locked_representations(n, phase), (n, phase)

for rule in [
    lambda n: n % 3,
    lambda n: (2 * n + 1) % 3,
    lambda n: 2,
]:
    for n in range(74, MAX_N + 1):
        phase = rule(n)
        witnesses = phase_locked_representations(n, phase)
        assert witnesses
        a, b = witnesses[0]
        assert 4 * a + 7 * b == n
        assert b % 3 == phase

print({
    "apery_mod_4": tuple(apery),
    "conductor_4_21": conductor,
    "phase_thresholds": thresholds,
    "uniform_threshold": 74,
    "lengths_checked": MAX_N,
    "status": "passed",
})
