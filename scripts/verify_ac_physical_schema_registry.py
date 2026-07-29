#!/usr/bin/env python3
"""Deterministic audit for AC5kn--AC5ks."""
from __future__ import annotations
from math import gcd
import hashlib
import json
import random

SEED = 29
SYSTEMS = 2500


def least_primitive_root(p):
    phi = p - 1
    factors = []
    x = phi
    q = 2
    while q * q <= x:
        if x % q == 0:
            factors.append(q)
            while x % q == 0:
                x //= q
        q += 1
    if x > 1:
        factors.append(x)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    raise AssertionError("no primitive root")


def dlog_table(p, gamma):
    out = {}
    x = 1
    for j in range(p - 1):
        out[x] = j
        x = x * gamma % p
    return out


def active_host(base, exclusions, context):
    blocked = set()
    for cell, scope, forbidden in exclusions:
        if tuple(context[i] for i in scope) == forbidden:
            blocked.add(cell)
    return frozenset(base - blocked)


def minimal_envelope(states):
    out = set()
    for state in states:
        out.update(state)
    return frozenset(out)


def max_matching_lex(demands, owners, edges, spent):
    live = tuple(o for o in owners if o not in spent)
    sentinel = max(owners) + 1 if owners else 0
    best = None
    best_card = -1

    def rec(i, used, assignment):
        nonlocal best, best_card
        if i == len(demands):
            card = sum(a != sentinel for a in assignment)
            value = tuple(assignment)
            if card > best_card or (card == best_card and (best is None or value < best)):
                best_card = card
                best = value
            return
        d = demands[i]
        options = sorted(o for o in live if o not in used and (d, o) in edges)
        options.append(sentinel)
        for owner in options:
            assignment.append(owner)
            if owner != sentinel:
                used.add(owner)
            rec(i + 1, used, assignment)
            if owner != sentinel:
                used.remove(owner)
            assignment.pop()

    rec(0, set(), [])
    assert best is not None
    return best


def digest(obj):
    text = json.dumps(obj, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()


def primitive_vec(rng, bound):
    while True:
        a = rng.randint(1, max(1, bound))
        b = rng.randint(-bound, bound)
        if gcd(a, abs(b)) == 1:
            return a, b


def build_valid(rng):
    p = rng.choice([5, 7, 11, 13, 17, 19, 23])
    n = p - 1
    gamma = least_primitive_root(p)
    logs = dlog_table(p, gamma)

    red = list(range(n))
    blue = list(range(n))
    rng.shuffle(red)
    rng.shuffle(blue)

    context_length = rng.randint(2, 5)
    context = tuple(rng.randrange(2) for _ in range(context_length))
    universe = min(n * n, 32)
    base = set(rng.sample(range(universe), rng.randint(3, min(10, universe))))
    exclusions = []
    for _ in range(rng.randint(1, 5)):
        cell = rng.choice(tuple(base))
        scope_length = rng.randint(1, min(2, context_length))
        scope = tuple(sorted(rng.sample(range(context_length), scope_length)))
        forbidden = tuple(rng.randrange(2) for _ in scope)
        exclusions.append((cell, scope, forbidden))

    cells = list(range(min(n * n, 24)))
    local_states = [
        frozenset(rng.sample(cells, rng.randint(0, min(4, len(cells)))))
        for _ in range(rng.randint(1, 5))
    ]

    bound = n - 1
    d1, e1 = primitive_vec(rng, bound), primitive_vec(rng, bound)
    d2, e2 = primitive_vec(rng, bound), primitive_vec(rng, bound)
    den_raw = d2[0] * e2[1] - d2[1] * e2[0]
    while den_raw == 0:
        d2, e2 = primitive_vec(rng, bound), primitive_vec(rng, bound)
        den_raw = d2[0] * e2[1] - d2[1] * e2[0]
    num_raw = d1[0] * e1[1] - d1[1] * e1[0]
    factor = gcd(abs(num_raw), abs(den_raw))
    denominator = abs(den_raw) // max(factor, 1)
    numerator = num_raw // max(factor, 1)
    residue = 0 if denominator == 1 else rng.randrange(denominator)

    while True:
        a, b, x, z = [rng.randrange(1, p) for _ in range(4)]
        ratio = b * pow(a, -1, p) % p
        root = z * pow(x, -1, p) % p
        if ratio != 1 and root not in (1, ratio):
            image = root * (1 - root) * pow((ratio - root) % p, -1, p) % p
            u = image * x % p
            if u:
                break
    h = rng.choice([value for value in range(1, p) if (p - 1) % value == 0])
    quotient_order = (p - 1) // h
    companion = ratio * (root - 1) * pow((root - ratio) % p, -1, p) % p
    ri_quotient = {
        "R": logs[ratio] % quotient_order,
        "A": logs[root] % quotient_order,
        "B": logs[companion] % quotient_order,
        "C": logs[image] % quotient_order,
        "S": logs[x] % quotient_order,
    }
    assert ri_quotient["B"] == (
        ri_quotient["R"] + ri_quotient["C"] - ri_quotient["A"]
    ) % quotient_order

    demand_count = rng.randint(1, 4)
    owner_count = rng.randint(1, 5)
    demands = tuple(range(demand_count))
    owners = tuple(range(owner_count))
    edges = {(d, o) for d in demands for o in owners if rng.random() < 0.6}
    spent = frozenset(o for o in owners if rng.random() < 0.2)
    assignment = max_matching_lex(demands, owners, edges, spent)

    schema = {
        "version": "ac-prime-minus-one-v1",
        "p": p,
        "n": n,
        "primitive_root": gamma,
        "layer_universe": 2 * n * n,
        "orders": ["cell", "owner", "operation", "row"],
        "dictionaries": {
            "owner_kinds": ["P", "B", "R", "F", "S", "C", "U"],
            "owner_routes": [
                "PAID", "FIXED_CURRENT", "PROSPECTIVE",
                "OCCURRENCE_FAILURE", "COHERENCE_MISMATCH", "OWNER_RESET",
            ],
            "recognizers": ["direct", "layered", "pool", "repair", "flow", "recurrence"],
        },
    }
    live = {
        "red_permutation": red,
        "blue_permutation": blue,
        "neutralization_bank_size": rng.randint(7, 12),
        "current_star": [rng.randint(0, 20), rng.randint(0, 20)],
        "certificate_weights": [rng.randint(0, 30) for _ in range(3)],
        "base_support": sorted(base),
        "context": context,
        "exclusions": exclusions,
        "local_states": [sorted(state) for state in local_states],
        "bda_physical": [d1, e1, d2, e2, num_raw, den_raw, residue],
        "ri_physical": [a, b, x, u, z, h],
        "owner_inputs": {
            "demands": demands,
            "owners": owners,
            "edges": sorted(edges),
            "spent": sorted(spent),
        },
        "live_guardrails": {
            "discretionary_filters": [],
            "shared_owners": [],
            "global_contracts": [],
        },
    }
    derived = {
        "active_host": sorted(active_host(base, exclusions, context)),
        "minimal_envelope": sorted(minimal_envelope(local_states)),
        "bda_reduced": [numerator, denominator, residue],
        "ri_quotient": ri_quotient,
        "owner_assignment": assignment,
        "selected_private_subbank": sorted(
            owner for owner in assignment if owners and owner <= max(owners)
        ),
    }
    return schema, live, derived


def reconstruct(schema, live):
    p, n = schema["p"], schema["n"]
    if n != p - 1:
        raise ValueError("prime-minus-one")
    gamma = least_primitive_root(p)
    if schema["primitive_root"] != gamma:
        raise ValueError("primitive-root")

    base = set(live["base_support"])
    context = tuple(live["context"])
    exclusions = [(z, tuple(scope), tuple(value)) for z, scope, value in live["exclusions"]]
    local_states = [frozenset(state) for state in live["local_states"]]

    d1, e1, d2, e2, num_raw, den_raw, residue = live["bda_physical"]
    if d1[0] * e1[1] - d1[1] * e1[0] != num_raw:
        raise ValueError("bda-numerator")
    if d2[0] * e2[1] - d2[1] * e2[0] != den_raw or den_raw == 0:
        raise ValueError("bda-denominator")
    if abs(den_raw) > 2 * (n - 1) ** 2:
        raise ValueError("bda-bound")
    factor = gcd(abs(num_raw), abs(den_raw))
    numerator = num_raw // max(factor, 1)
    denominator = abs(den_raw) // max(factor, 1)
    if denominator > 1 and not 0 <= residue < denominator:
        raise ValueError("bda-residue")
    if denominator == 1 and residue != 0:
        raise ValueError("bda-residue")

    a, b, x, u, z, h = live["ri_physical"]
    if any(not 1 <= value < p for value in (a, b, x, u, z)) or (p - 1) % h:
        raise ValueError("ri-occurrence")
    ratio = b * pow(a, -1, p) % p
    root = z * pow(x, -1, p) % p
    if ratio == 1 or root in (1, ratio):
        raise ValueError("ri-degenerate")
    image = u * pow(x, -1, p) % p
    expected = root * (1 - root) * pow((ratio - root) % p, -1, p) % p
    if image != expected:
        raise ValueError("ri-identity")
    companion = ratio * (root - 1) * pow((root - ratio) % p, -1, p) % p
    logs = dlog_table(p, gamma)
    quotient_order = (p - 1) // h
    ri_quotient = {
        "R": logs[ratio] % quotient_order,
        "A": logs[root] % quotient_order,
        "B": logs[companion] % quotient_order,
        "C": logs[image] % quotient_order,
        "S": logs[x] % quotient_order,
    }
    if ri_quotient["B"] != (
        ri_quotient["R"] + ri_quotient["C"] - ri_quotient["A"]
    ) % quotient_order:
        raise ValueError("ri-quotient")

    owner = live["owner_inputs"]
    demands = tuple(owner["demands"])
    owners = tuple(owner["owners"])
    assignment = max_matching_lex(
        demands, owners, {tuple(edge) for edge in owner["edges"]}, frozenset(owner["spent"])
    )

    if live["neutralization_bank_size"] < 7:
        raise ValueError("bank-size")
    for name in ("red_permutation", "blue_permutation"):
        if sorted(live[name]) != list(range(n)):
            raise ValueError("permutation")

    return {
        "active_host": sorted(active_host(base, exclusions, context)),
        "minimal_envelope": sorted(minimal_envelope(local_states)),
        "bda_reduced": [numerator, denominator, residue],
        "ri_quotient": ri_quotient,
        "owner_assignment": assignment,
        "selected_private_subbank": sorted(
            value for value in assignment if owners and value <= max(owners)
        ),
    }


def run():
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "valid": 0,
        "derived_round_trips": 0,
        "derived_mutation_witnesses": 0,
        "prime_minus_one_failures": 0,
        "bank_failures": 0,
        "permutation_failures": 0,
        "bda_failures": 0,
        "ri_failures": 0,
        "schema_digest_failures": 0,
        "live_field_changes": 0,
    }
    failure_types = ["prime", "bank", "permutation", "bda", "ri", "digest"]

    for index in range(SYSTEMS):
        schema, live, derived = build_valid(rng)
        reduced_digest = digest({"schema": schema, "live": live})
        assert reconstruct(schema, live) == derived
        stats["derived_round_trips"] += 5

        mutated = dict(derived)
        mutated["active_host"] = list(reversed(mutated["active_host"]))
        if mutated["active_host"] == derived["active_host"]:
            mutated["active_host"] = mutated["active_host"] + [-1]
        assert reconstruct(schema, live) != mutated
        stats["derived_mutation_witnesses"] += 1

        if index < 1000:
            stats["valid"] += 1
            changed = json.loads(json.dumps(live))
            changed["neutralization_bank_size"] += 1
            assert digest({"schema": schema, "live": changed}) != reduced_digest
            stats["live_field_changes"] += 1
            continue

        failure = failure_types[(index - 1000) % len(failure_types)]
        bad_schema = json.loads(json.dumps(schema))
        bad_live = json.loads(json.dumps(live))
        try:
            if failure == "prime":
                bad_schema["n"] += 1
            elif failure == "bank":
                bad_live["neutralization_bank_size"] = 6
            elif failure == "permutation":
                bad_live["red_permutation"][0] = bad_live["red_permutation"][1]
            elif failure == "bda":
                bad_live["bda_physical"][5] = 0
            elif failure == "ri":
                p = bad_schema["p"]
                bad_live["ri_physical"][3] = bad_live["ri_physical"][2]
                a, b, x, u, z, _ = bad_live["ri_physical"]
                ratio = b * pow(a, -1, p) % p
                root = z * pow(x, -1, p) % p
                expected = root * (1 - root) * pow((ratio - root) % p, -1, p) % p
                if u * pow(x, -1, p) % p == expected:
                    bad_live["ri_physical"][3] = u % (p - 1) + 1
            else:
                bad_schema["dictionaries"]["owner_routes"][0] = "PAID_CHANGED"
                assert digest({"schema": bad_schema, "live": bad_live}) != reduced_digest
                stats["schema_digest_failures"] += 1
                continue
            reconstruct(bad_schema, bad_live)
        except (ValueError, ZeroDivisionError):
            key = {
                "prime": "prime_minus_one_failures",
                "bank": "bank_failures",
                "permutation": "permutation_failures",
                "bda": "bda_failures",
                "ri": "ri_failures",
            }[failure]
            stats[key] += 1
        else:
            raise AssertionError("expected failure: " + failure)

    return stats


if __name__ == "__main__":
    result = run()
    print("AC physical schema registry audit")
    for key, value in result.items():
        print(f"{key}: {value}")
