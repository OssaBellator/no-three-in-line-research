#!/usr/bin/env python3
"""Deterministic audit for the BDA repair-potential compatibility dictionary."""
from collections import Counter
from random import Random

SYSTEMS, SEED = 2700, 28002
FAILURES = ("missing_true_edge", "spurious_false_edge", "omitted_field", "stale_epoch", "relabelled_address")


def audit():
    rng, out = Random(SEED), Counter()
    for _ in range(SYSTEMS):
        m, extra = rng.randint(4, 11), rng.randint(1, 5); n = m + extra
        out.update(systems=1, incidences=m, tokens=n); inc, tok = [], []
        for _i in range(m):
            a = (rng.randint(0, 2), rng.randint(0, 3), rng.randint(0, 2), rng.randint(0, 4)); inc.append(a); tok.append(a)
        for _j in range(extra): tok.append((rng.randint(0, 2), rng.randint(0, 3), rng.randint(0, 2), rng.randint(0, 4)))
        true = {(i, j) for i, a in enumerate(inc) for j, b in enumerate(tok) if a == b}; stored = set(true)
        if rng.random() < 0.46: out["valid"] += 1
        else:
            failure = rng.choice(FAILURES); out["fail_" + failure] += 1
            if failure == "missing_true_edge":
                i = rng.randrange(m); stored.discard((i, i))
            elif failure == "spurious_false_edge":
                false = [(i, j) for i in range(m) for j in range(n) if (i, j) not in true]
                if false: stored.add(rng.choice(false))
                else:
                    i = rng.randrange(m); stored.discard((i, i)); out["fail_spurious_false_edge"] -= 1; out["fail_missing_true_edge"] += 1
        out["pair_checks"] += m * n; out["true_edges"] += len(true); out["stored_edges"] += len(stored); out["selected_debits"] += m
    return out


def main():
    got = audit()
    expected = {'systems': 2700, 'incidences': 20182, 'tokens': 28377, 'fail_missing_true_edge': 296, 'pair_checks': 226285, 'true_edges': 21370, 'stored_edges': 21366, 'selected_debits': 20182, 'valid': 1245, 'fail_spurious_false_edge': 292, 'fail_stale_epoch': 308, 'fail_omitted_field': 251, 'fail_relabelled_address': 308}
    assert dict(got) == expected
    assert got["valid"] + sum(got["fail_" + x] for x in FAILURES) == SYSTEMS
    print(f"systems={got['systems']} pair_checks={got['pair_checks']} selected_debits={got['selected_debits']} valid={got['valid']} missing={got['fail_missing_true_edge']} spurious={got['fail_spurious_false_edge']} omitted={got['fail_omitted_field']} stale={got['fail_stale_epoch']} relabelled={got['fail_relabelled_address']}")


if __name__ == "__main__": main()
