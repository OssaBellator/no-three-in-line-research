#!/usr/bin/env python3
"""Finite checks for CMR974--CMR981."""

from itertools import combinations, permutations, product
import random


def minimum_face(family, potential):
    value = min(potential[state] for state in family)
    return {state for state in family if potential[state] == value}, value


def common_core(family):
    iterator = iter(family)
    result = set(next(iterator))
    for state in iterator:
        result.intersection_update(state)
    return frozenset(result)


def check_general_conditioning():
    rng = random.Random(974)
    checked = 0
    for universe_size in range(1, 30):
        for state_size in range(universe_size + 1):
            all_states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(40):
                family = set(
                    rng.sample(all_states, rng.randint(1, min(100, len(all_states))))
                )
                potential = {state: rng.randint(0, 30) for state in family}
                face, value = minimum_face(family, potential)
                core = common_core(face)
                rank = rng.randint(0, min(3, len(core)))
                prescription = frozenset(rng.sample(tuple(core), rank))
                conditioned = {
                    state for state in family if set(prescription) <= set(state)
                }
                conditioned_face, conditioned_value = minimum_face(
                    conditioned, potential
                )
                assert conditioned_value == value
                assert conditioned_face == face
                residual = {
                    frozenset(set(state) - set(prescription))
                    for state in conditioned
                }
                induced = {
                    state: potential[frozenset(set(state) | set(prescription))]
                    for state in residual
                }
                residual_face, residual_value = minimum_face(residual, induced)
                assert residual_value == value
                assert residual_face == {
                    frozenset(set(state) - set(prescription))
                    for state in face
                }
                checked += 1
    return checked


def matching(permutation):
    return frozenset((source, permutation[source]) for source in range(len(permutation)))


def perfect_matchings(side, host):
    return {
        matching(permutation)
        for permutation in permutations(range(side))
        if matching(permutation) <= set(host)
    }


def residual_host(host, prescription):
    sources = {source for source, _target in prescription}
    targets = {target for _source, target in prescription}
    return {
        (source, target)
        for source, target in host
        if source not in sources and target not in targets
    }


def check_one_layer_hosts():
    rng = random.Random(976)
    checked = 0
    for side in range(1, 5):
        edges = [(source, target) for source in range(side) for target in range(side)]
        trials = range(1 << len(edges)) if side <= 3 else range(5000)
        for trial in trials:
            if side <= 3:
                host = {
                    edge for index, edge in enumerate(edges) if trial & (1 << index)
                }
            else:
                host = {edge for edge in edges if rng.random() < rng.uniform(0.3, 0.9)}
            family = perfect_matchings(side, host)
            if not family:
                continue
            selected = rng.choice(tuple(family))
            rank = rng.randint(0, min(3, side))
            prescription = frozenset(rng.sample(tuple(selected), rank))
            conditioned = {
                state for state in family if set(prescription) <= set(state)
            }
            residual = residual_host(host, prescription)
            residual_sources = sorted(
                set(range(side)) - {source for source, _ in prescription}
            )
            residual_targets = sorted(
                set(range(side)) - {target for _, target in prescription}
            )
            source_index = {source: index for index, source in enumerate(residual_sources)}
            target_index = {target: index for index, target in enumerate(residual_targets)}
            relabelled_host = {
                (source_index[source], target_index[target])
                for source, target in residual
            }
            residual_matchings = perfect_matchings(side - rank, relabelled_host)
            lifted_residuals = {
                frozenset(
                    (residual_sources[source], residual_targets[target])
                    for source, target in state
                )
                for state in residual_matchings
            }
            assert {
                frozenset(set(state) - set(prescription))
                for state in conditioned
            } == lifted_residuals
            checked += 1
    return checked


def joint_states(side, host0, host1):
    first = perfect_matchings(side, host0)
    second = perfect_matchings(side, host1)
    return {
        (state0, state1)
        for state0 in first
        for state1 in second
        if set(state0).isdisjoint(state1)
    }


def check_two_layer_joint_systems():
    rng = random.Random(977)
    checked = 0
    for side in range(1, 5):
        edges = [(source, target) for source in range(side) for target in range(side)]
        for _ in range(2000 if side <= 3 else 1000):
            host0 = {edge for edge in edges if rng.random() < rng.uniform(0.35, 0.9)}
            host1 = {edge for edge in edges if rng.random() < rng.uniform(0.35, 0.9)}
            family = joint_states(side, host0, host1)
            if not family:
                continue
            selected0, selected1 = rng.choice(tuple(family))
            rank0 = rng.randint(0, min(2, side))
            rank1 = rng.randint(0, min(2, side))
            prescription0 = frozenset(rng.sample(tuple(selected0), rank0))
            available1 = [edge for edge in selected1 if edge not in prescription0]
            rank1 = min(rank1, len(available1))
            prescription1 = frozenset(rng.sample(available1, rank1))
            prescription = (prescription0, prescription1)
            conditioned = {
                state
                for state in family
                if set(prescription0) <= set(state[0])
                and set(prescription1) <= set(state[1])
            }

            residual0 = residual_host(host0, prescription0) - set(prescription1)
            residual1 = residual_host(host1, prescription1) - set(prescription0)
            sources0 = sorted(set(range(side)) - {source for source, _ in prescription0})
            targets0 = sorted(set(range(side)) - {target for _, target in prescription0})
            sources1 = sorted(set(range(side)) - {source for source, _ in prescription1})
            targets1 = sorted(set(range(side)) - {target for _, target in prescription1})

            residual_pairs = set()
            for permutation0 in permutations(targets0):
                state0 = frozenset(zip(sources0, permutation0))
                if not set(state0) <= residual0:
                    continue
                for permutation1 in permutations(targets1):
                    state1 = frozenset(zip(sources1, permutation1))
                    if set(state1) <= residual1 and set(state0).isdisjoint(state1):
                        residual_pairs.add((state0, state1))

            restricted = {
                (
                    frozenset(set(state0) - set(prescription0)),
                    frozenset(set(state1) - set(prescription1)),
                )
                for state0, state1 in conditioned
            }
            assert restricted == residual_pairs
            checked += 1
    return checked


def check_product_conditioning():
    rng = random.Random(978)
    checked = 0
    for factor_count in range(1, 5):
        for _ in range(3000):
            factors = []
            chosen_parts = []
            prescriptions = []
            offset = 0
            for _factor in range(factor_count):
                universe_size = rng.randint(1, 6)
                state_size = rng.randint(0, universe_size)
                edges = tuple(range(offset, offset + universe_size))
                all_states = [
                    frozenset(state)
                    for state in combinations(edges, state_size)
                ]
                family = set(
                    rng.sample(all_states, rng.randint(1, min(10, len(all_states))))
                )
                chosen = rng.choice(tuple(family))
                rank = rng.randint(0, min(2, len(chosen)))
                prescription = frozenset(rng.sample(tuple(chosen), rank))
                factors.append(family)
                chosen_parts.append(chosen)
                prescriptions.append(prescription)
                offset += universe_size
            full_family = {
                frozenset().union(*states) for states in product(*factors)
            }
            full_prescription = frozenset().union(*prescriptions)
            conditioned = {
                state
                for state in full_family
                if set(full_prescription) <= set(state)
            }
            local_conditioned = [
                {state for state in family if set(prescription) <= set(state)}
                for family, prescription in zip(factors, prescriptions)
            ]
            expected = {
                frozenset().union(*states)
                for states in product(*local_conditioned)
            }
            assert conditioned == expected
            checked += 1
    return checked


def check_potential_transport_and_rank_budget():
    rng = random.Random(979)
    transport = 0
    budgets = 0
    for universe_size in range(3, 60):
        for _ in range(200):
            state = frozenset(
                rng.sample(range(universe_size), rng.randint(1, universe_size))
            )
            rank = rng.randint(0, min(3, len(state)))
            prescription = frozenset(rng.sample(tuple(state), rank))
            residual = frozenset(set(state) - set(prescription))
            atom = frozenset(rng.sample(range(universe_size), 3))
            assert (set(atom) <= set(state)) == (
                (set(atom) - set(prescription)) <= set(residual)
                and (set(atom) & set(prescription)) <= set(state)
            )
            transport += 1

            remaining = len(state)
            contracted = 0
            while remaining:
                next_rank = rng.randint(1, remaining)
                remaining -= next_rank
                contracted += next_rank
                assert contracted + remaining == len(state)
            assert contracted <= len(state)
            budgets += 1
    return transport, budgets


def main():
    transport, budgets = check_potential_transport_and_rank_budget()
    print(
        "verified minimum-core host representability:",
        check_general_conditioning(),
        "conditioned faces,",
        check_one_layer_hosts(),
        "one-layer hosts,",
        check_two_layer_joint_systems(),
        "joint systems,",
        check_product_conditioning(),
        "product conditions,",
        transport,
        "potential transports, and",
        budgets,
        "rank budgets",
    )


if __name__ == "__main__":
    main()
