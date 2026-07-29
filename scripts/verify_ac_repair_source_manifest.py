#!/usr/bin/env python3
from __future__ import annotations
from collections import defaultdict
import random

SEED = 61
SYSTEMS = 2500


def nonempty_subsets(items):
    values = list(items)
    for mask in range(1, 1 << len(values)):
        yield tuple(values[i] for i in range(len(values)) if (mask >> i) & 1)


def maximum_matching(left, right, edges):
    matched_right = {}

    def augment(u, seen):
        for v in sorted(right):
            if (u, v) not in edges or v in seen:
                continue
            seen.add(v)
            if v not in matched_right or augment(matched_right[v], seen):
                matched_right[v] = u
                return True
        return False

    for u in sorted(left):
        augment(u, set())
    return {u: v for v, u in matched_right.items()}


def canonical_hall_core(left, right, edges):
    best = None
    for subset in nonempty_subsets(left):
        neighbourhood = {
            v for u in subset for v in right if (u, v) in edges
        }
        deficit = len(subset) - len(neighbourhood)
        if deficit > 0:
            key = -deficit, len(subset), subset
            if best is None or key < best[0]:
                best = key, subset, neighbourhood, deficit
    return None if best is None else best[1:]


def run():
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "layers": 0,
        "bad_layer_witnesses": 0,
        "global_layer_successes": 0,
        "slot_uses": 0,
        "old_slots": 0,
        "repair_transversal_incidences": 0,
        "repair_extension_failures": 0,
        "source_tokens": 0,
        "issued_incidences": 0,
        "conservation_checks": 0,
        "source_assignments": 0,
        "source_hall_cores": 0,
        "hall_deficit_units": 0,
        "missing_rectangle_pairs": 0,
        "predicate_concentration_checks": 0,
        "source_less_issuance_failures": 0,
    }

    for system in range(SYSTEMS):
        layer_count = rng.randint(2, 6)
        layer_data = []
        for _ in range(layer_count):
            reverse_load = rng.randint(1, 8)
            adjusted_forward = rng.randint(0, reverse_load + 2)
            layer_data.append((adjusted_forward, reverse_load))
        forward_total = sum(value for value, _ in layer_data)
        reverse_total = sum(value for _, value in layer_data)
        stats["layers"] += layer_count
        if forward_total < reverse_total:
            relative = (reverse_total - forward_total) / reverse_total
            assert any(
                max(0, reverse - forward) / reverse >= relative - 1e-12
                for forward, reverse in layer_data
            )
            stats["bad_layer_witnesses"] += 1
        else:
            stats["global_layer_successes"] += 1

        use_count = rng.randint(2, 6)
        uses = tuple(range(use_count))
        old_slots = tuple(range(rng.randint(1, use_count)))
        old_edges = {
            (use, slot)
            for use in uses
            for slot in old_slots
            if rng.random() < 0.55
        }
        core = canonical_hall_core(uses, old_slots, old_edges)
        if core is None:
            old_slots = (0,)
            old_edges = {(use, 0) for use in uses}
            core = canonical_hall_core(uses, old_slots, old_edges)
        core_uses, old_neighbourhood, deficit = core
        assert deficit > 0
        new_slots = tuple(range(len(old_slots), len(old_slots) + deficit))
        extended_slots = old_slots + new_slots
        extended_edges = set(old_edges)
        assignment = {}
        for use, slot in zip(core_uses, new_slots):
            assignment[use] = slot
            extended_edges.add((use, slot))
        for use in uses:
            if use in assignment:
                continue
            choices = [
                slot for slot in extended_slots if slot not in assignment.values()
            ]
            if not choices:
                break
            assignment[use] = choices[0]
            extended_edges.add((use, choices[0]))

        stats["slot_uses"] += len(uses)
        stats["old_slots"] += len(old_slots)
        if len(assignment) != len(uses):
            stats["repair_extension_failures"] += 1
            continue
        outside = [
            (use, assignment[use])
            for use in core_uses
            if assignment[use] not in old_neighbourhood
        ]
        assert len(outside) >= deficit
        transversal = tuple(sorted(outside)[:deficit])
        assert len({use for use, _ in transversal}) == deficit
        assert len({slot for _, slot in transversal}) == deficit
        stats["repair_transversal_incidences"] += deficit

        classes = tuple(range(rng.randint(1, 4)))
        tokens = []
        for repair_class in classes:
            for index in range(rng.randint(1, 4)):
                tokens.append((repair_class, index))
        stats["source_tokens"] += len(tokens)
        live = set(tokens)
        issued = []
        for index, (use, slot) in enumerate(transversal):
            repair_class = classes[index % len(classes)]
            candidates = sorted(token for token in live if token[0] == repair_class)
            if candidates:
                token = candidates[0]
                live.remove(token)
                issued.append((use, slot, repair_class, token))
                stats["issued_incidences"] += 1
            elif system % 7 == 0:
                stats["source_less_issuance_failures"] += 1
        assert len(live) + len(issued) == len(tokens)
        stats["conservation_checks"] += 1

        repair_incidences = tuple(range(len(transversal)))
        source_units = tuple(
            range(max(len(repair_incidences), 1) + rng.randint(0, 3))
        )
        compatibility = {
            (repair, source)
            for repair in repair_incidences
            for source in source_units
            if rng.random() < 0.55
        }
        if system % 3 == 0 and repair_incidences:
            compatibility |= {
                (repair, repair % len(source_units))
                for repair in repair_incidences
            }
        matching = maximum_matching(
            repair_incidences, source_units, compatibility
        )
        if len(matching) == len(repair_incidences):
            stats["source_assignments"] += 1
        else:
            hall_core = canonical_hall_core(
                repair_incidences, source_units, compatibility
            )
            assert hall_core is not None
            core_set, neighbourhood, hall_deficit = hall_core
            outside_sources = set(source_units) - set(neighbourhood)
            rectangle = [
                (repair, source)
                for repair in core_set
                for source in outside_sources
                if (repair, source) not in compatibility
            ]
            assert len(rectangle) >= hall_deficit
            stats["source_hall_cores"] += 1
            stats["hall_deficit_units"] += hall_deficit
            stats["missing_rectangle_pairs"] += len(rectangle)
            predicates = defaultdict(list)
            for pair in rectangle:
                predicates[("predicate", (pair[0] + pair[1]) % 4)].append(pair)
            largest = max(predicates.values(), key=len)
            assert len(largest) * len(predicates) >= len(rectangle)
            stats["predicate_concentration_checks"] += 1

    return stats


if __name__ == "__main__":
    output = run()
    print("AC repair source manifest audit")
    for key, value in output.items():
        print(f"{key}: {value}")
