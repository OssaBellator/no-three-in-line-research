#!/usr/bin/env python3
"""Deterministic audit for AC5in--AC5ir."""
from collections import Counter
from random import Random

SYSTEMS = 2500
SEED = 20260730


def popcount(mask):
    return mask.bit_count()


def indices(mask, size):
    return [i for i in range(size) if (mask >> i) & 1]


def prerequisite_bundle(i, prerequisites, template_count):
    bundle = 1 << i
    changed = True
    while changed:
        changed = False
        for j in range(template_count):
            if (bundle >> j) & 1:
                new = prerequisites[j] & ~bundle
                if new:
                    bundle |= new
                    changed = True
    return bundle


def closure_valid(selected, prerequisites, template_count):
    return all(
        not ((selected >> i) & 1) or prerequisites[i] & ~selected == 0
        for i in range(template_count)
    )


def coverage(selected, covers, template_count):
    answer = 0
    for i in range(template_count):
        if (selected >> i) & 1:
            answer |= covers[i]
    return answer


def object_records_consistent(selected, records, template_count):
    seen = {}
    first = None
    for i in range(template_count):
        if not ((selected >> i) & 1):
            continue
        for obj, value in records[i].items():
            if obj in seen and seen[obj] != value:
                candidate = (obj, seen[obj], value, i)
                if first is None or candidate < first:
                    first = candidate
            else:
                seen[obj] = value
    return first is None, first


def capacity_records_consistent(selected, capacities, template_count):
    seen = {}
    first = None
    raw_amount = 0
    for i in range(template_count):
        if not ((selected >> i) & 1):
            continue
        for address, record in capacities[i].items():
            raw_amount += record[1]
            if address in seen and seen[address] != record:
                candidate = (address, seen[address], record, i)
                if first is None or candidate < first:
                    first = candidate
            else:
                seen[address] = record
    return first is None, first, seen, raw_amount


def greedy_closed_atlas(
    covers,
    prerequisites,
    weights,
    records,
    capacities,
    full,
    template_count,
):
    selected = 0
    insertion_order = []
    while coverage(selected, covers, template_count) != full:
        uncovered = full & ~coverage(selected, covers, template_count)
        best = None
        for i in range(template_count):
            if (selected >> i) & 1:
                continue
            added = prerequisite_bundle(i, prerequisites, template_count) & ~selected
            trial = selected | added
            if not closure_valid(trial, prerequisites, template_count):
                continue
            if not object_records_consistent(trial, records, template_count)[0]:
                continue
            if not capacity_records_consistent(trial, capacities, template_count)[0]:
                continue
            gain = popcount(coverage(added, covers, template_count) & uncovered)
            if gain == 0:
                continue
            added_weight = sum(
                weights[j] for j in range(template_count) if (added >> j) & 1
            )
            key = (gain, -added_weight, -popcount(added), -i)
            if best is None or key > best[0]:
                best = (key, added)
        if best is None:
            return None
        added = best[1]
        selected |= added
        insertion_order.extend(
            j
            for j in range(template_count)
            if (added >> j) & 1 and j not in insertion_order
        )

    for i in reversed(insertion_order):
        if not ((selected >> i) & 1):
            continue
        trial = selected & ~(1 << i)
        if not closure_valid(trial, prerequisites, template_count):
            continue
        if coverage(trial, covers, template_count) != full:
            continue
        if not object_records_consistent(trial, records, template_count)[0]:
            continue
        if not capacity_records_consistent(trial, capacities, template_count)[0]:
            continue
        selected = trial
    return selected


def exact_minimum_atlas(
    covers,
    prerequisites,
    weights,
    records,
    capacities,
    full,
    template_count,
):
    best_objective = None
    best_selected = None
    for selected in range(1 << template_count):
        if coverage(selected, covers, template_count) != full:
            continue
        if not closure_valid(selected, prerequisites, template_count):
            continue
        if not object_records_consistent(selected, records, template_count)[0]:
            continue
        if not capacity_records_consistent(selected, capacities, template_count)[0]:
            continue
        selected_indices = tuple(indices(selected, template_count))
        objective = (
            sum(weights[i] for i in selected_indices),
            len(selected_indices),
            selected_indices,
        )
        if best_objective is None or objective < best_objective:
            best_objective = objective
            best_selected = selected
    return best_selected, best_objective


def irredundancy_witness(i, selected, covers, prerequisites, full, template_count):
    trial = selected & ~(1 << i)
    missing = full & ~coverage(trial, covers, template_count)
    if missing:
        return "private", min(indices(missing, full.bit_length()))
    dependents = [
        j
        for j in range(template_count)
        if (trial >> j) & 1 and (prerequisites[j] >> i) & 1
    ]
    if dependents:
        return "dependency", min(dependents)
    raise AssertionError("selected template is not irredundant")


def bottleneck_packing(covers, template_count, object_count):
    neighbourhoods = []
    for obj in range(object_count):
        neighbourhood = 0
        for i in range(template_count):
            if (covers[i] >> obj) & 1:
                neighbourhood |= 1 << i
        neighbourhoods.append(neighbourhood)
    zero = [obj for obj, neighbourhood in enumerate(neighbourhoods) if neighbourhood == 0]
    if zero:
        return None, min(zero)

    chosen = []
    used_templates = 0
    for obj in sorted(
        range(object_count),
        key=lambda x: (popcount(neighbourhoods[x]), x),
    ):
        if neighbourhoods[obj] & used_templates == 0:
            chosen.append(obj)
            used_templates |= neighbourhoods[obj]
    return chosen, None


def generate_system(rng, mode):
    pair_count = rng.randint(3, 7)
    state_count = rng.randint(3, 7)
    edge_count = rng.randint(3, 7)
    object_count = pair_count + state_count + edge_count
    full = (1 << object_count) - 1
    template_count = rng.randint(6, 11)

    covers = [0] * template_count
    for obj in range(object_count):
        multiplicity = rng.randint(1, min(4, template_count))
        for i in rng.sample(range(template_count), multiplicity):
            covers[i] |= 1 << obj
    for i in range(template_count):
        for obj in range(object_count):
            if rng.random() < 0.12:
                covers[i] |= 1 << obj
        if covers[i] == 0:
            covers[i] = 1 << rng.randrange(object_count)

    prerequisites = [0] * template_count
    for i in range(1, template_count):
        if rng.random() < 0.25:
            prerequisites[i] |= 1 << rng.randrange(i)
        if rng.random() < 0.08 and i > 1:
            prerequisites[i] |= 1 << rng.randrange(i)

    weights = [rng.randint(1, 7) for _ in range(template_count)]
    canonical_records = {
        obj: (obj % 3, rng.randint(0, 5)) for obj in range(object_count)
    }
    records = [
        {obj: canonical_records[obj] for obj in indices(covers[i], object_count)}
        for i in range(template_count)
    ]

    address_pool = [f"a{j}" for j in range(rng.randint(5, 10))]
    canonical_capacities = {
        address: (
            rng.choice(("pay", "ticket", "reset", "dist")),
            rng.randint(1, 4),
            rng.randint(1, 5),
        )
        for address in address_pool
    }
    capacities = []
    for _ in range(template_count):
        capacities.append(
            {
                address: canonical_capacities[address]
                for address in rng.sample(
                    address_pool, rng.randint(1, min(4, len(address_pool)))
                )
            }
        )

    if mode == 1:
        obj = rng.randrange(object_count)
        for i in range(template_count):
            covers[i] &= ~(1 << obj)
            records[i].pop(obj, None)
    elif mode == 2:
        obj = min(
            obj
            for obj in range(object_count)
            if sum((covers[i] >> obj) & 1 for i in range(template_count)) >= 2
        )
        conflicting = [
            i for i in range(template_count) if (covers[i] >> obj) & 1
        ][:2]
        records[conflicting[1]][obj] = (99, 99)
    elif mode == 3:
        prerequisites[rng.randrange(template_count)] |= 1 << template_count
    elif mode == 4:
        address = address_pool[0]
        capacities[0][address] = canonical_capacities[address]
        base = canonical_capacities[address]
        capacities[1][address] = (base[0], base[1] + 1, base[2])

    return (
        object_count,
        template_count,
        full,
        covers,
        prerequisites,
        weights,
        records,
        capacities,
    )


def audit():
    rng = Random(SEED)
    out = Counter()

    for system in range(SYSTEMS):
        mode = system % 5
        (
            object_count,
            template_count,
            full,
            covers,
            prerequisites,
            weights,
            records,
            capacities,
        ) = generate_system(rng, mode)

        malformed = next(
            (
                i
                for i, prerequisite in enumerate(prerequisites)
                if prerequisite >> template_count
            ),
            None,
        )
        if malformed is not None:
            assert mode == 3
            out["bad_prerequisite"] += 1
            continue

        object_ok, _ = object_records_consistent(
            (1 << template_count) - 1, records, template_count
        )
        if not object_ok:
            assert mode == 2
            out["object_conflict"] += 1
            continue

        capacity_ok, _, _, _ = capacity_records_consistent(
            (1 << template_count) - 1, capacities, template_count
        )
        if not capacity_ok:
            assert mode == 4
            out["capacity_conflict"] += 1
            continue

        packing, uncovered = bottleneck_packing(
            covers, template_count, object_count
        )
        if uncovered is not None:
            assert mode == 1
            out["uncovered"] += 1
            out["least_uncovered_sum"] += uncovered
            continue

        assert mode == 0
        greedy = greedy_closed_atlas(
            covers,
            prerequisites,
            weights,
            records,
            capacities,
            full,
            template_count,
        )
        exact, objective = exact_minimum_atlas(
            covers,
            prerequisites,
            weights,
            records,
            capacities,
            full,
            template_count,
        )
        assert greedy is not None and exact is not None
        assert closure_valid(greedy, prerequisites, template_count)
        assert closure_valid(exact, prerequisites, template_count)
        assert coverage(greedy, covers, template_count) == full
        assert coverage(exact, covers, template_count) == full

        private = 0
        dependency = 0
        for i in indices(greedy, template_count):
            kind, _ = irredundancy_witness(
                i, greedy, covers, prerequisites, full, template_count
            )
            if kind == "private":
                private += 1
            else:
                dependency += 1
        assert popcount(greedy) == private + dependency
        assert len(packing) <= popcount(exact)

        capacity_ok, _, unique, raw_amount = capacity_records_consistent(
            exact, capacities, template_count
        )
        assert capacity_ok
        unique_amount = sum(record[1] for record in unique.values())
        assert unique_amount <= raw_amount

        psi_star = rng.randint(10, 80)
        reset = sum(
            record[1] for record in unique.values() if record[0] == "reset"
        )
        payment = sum(
            record[1] for record in unique.values() if record[0] == "pay"
        )
        ticket = sum(
            record[1] for record in unique.values() if record[0] == "ticket"
        )
        disturbance = sum(
            record[1] for record in unique.values() if record[0] == "dist"
        )
        disturbance_weight = max(
            [record[2] for record in unique.values() if record[0] == "dist"]
            or [0]
        )
        episode_bound = (
            (reset + 1) * psi_star
            + disturbance * disturbance_weight
            + payment
            + ticket
        )

        out.update(
            valid=1,
            physical_objects=object_count,
            candidate_templates=template_count,
            greedy_templates=popcount(greedy),
            exact_templates=popcount(exact),
            greedy_weight=sum(
                weights[i] for i in indices(greedy, template_count)
            ),
            exact_weight=objective[0],
            private_witnesses=private,
            dependency_witnesses=dependency,
            bottleneck_packing=len(packing),
            raw_capacity_amount=raw_amount,
            unique_capacity_amount=unique_amount,
            capacity_alias_savings=raw_amount - unique_amount,
            episode_bound=episode_bound,
        )

    return out


def main():
    got = audit()
    expected = {
        "valid": 500,
        "uncovered": 500,
        "object_conflict": 500,
        "bad_prerequisite": 500,
        "capacity_conflict": 500,
        "physical_objects": 7596,
        "candidate_templates": 4214,
        "greedy_templates": 2025,
        "exact_templates": 1951,
        "greedy_weight": 7756,
        "exact_weight": 6862,
        "private_witnesses": 1859,
        "dependency_witnesses": 166,
        "bottleneck_packing": 1567,
        "raw_capacity_amount": 11975,
        "unique_capacity_amount": 7092,
        "capacity_alias_savings": 4883,
        "episode_bound": 110691,
        "least_uncovered_sum": 3545,
    }
    assert dict(got) == expected
    print(
        f"systems={SYSTEMS} valid={got['valid']} uncovered={got['uncovered']} "
        f"object_conflicts={got['object_conflict']} "
        f"bad_prerequisites={got['bad_prerequisite']} "
        f"capacity_conflicts={got['capacity_conflict']}"
    )
    print(
        f"objects={got['physical_objects']} candidates={got['candidate_templates']} "
        f"greedy={got['greedy_templates']} exact={got['exact_templates']} "
        f"private={got['private_witnesses']} dependency={got['dependency_witnesses']}"
    )
    print(
        f"greedy_weight={got['greedy_weight']} exact_weight={got['exact_weight']} "
        f"packing_lower_bound={got['bottleneck_packing']} "
        f"raw_capacity={got['raw_capacity_amount']} "
        f"unique_capacity={got['unique_capacity_amount']} "
        f"alias_savings={got['capacity_alias_savings']} "
        f"episode_bound={got['episode_bound']}"
    )


if __name__ == "__main__":
    main()
