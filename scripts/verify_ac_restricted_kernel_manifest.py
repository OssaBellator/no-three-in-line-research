#!/usr/bin/env python3
"""Deterministic audit for AC5id--AC5ih."""
from collections import Counter
from itertools import permutations
from random import Random

SYSTEMS = 2500
SEED = 202607292347
CLASS_NAMES = ("support", "secant", "line", "residual", "new")


def maximum_matching(adjacency, right_size):
    match_right = [-1] * right_size

    def augment(left, seen):
        for right in sorted(adjacency[left]):
            if right in seen:
                continue
            seen.add(right)
            if match_right[right] == -1 or augment(match_right[right], seen):
                match_right[right] = left
                return True
        return False

    return sum(augment(left, set()) for left in range(len(adjacency)))


def minimum_cost_matching(adjacency, costs):
    left_size = len(adjacency)
    best = None
    count = 0
    for chosen in permutations(range(len(costs)), left_size):
        if all(chosen[left] in adjacency[left] for left in range(left_size)):
            count += 1
            value = sum(costs[right] for right in chosen)
            if best is None or value < best:
                best = value
    return best, count


def falling_factorial(n, length):
    result = 1
    for offset in range(length):
        result *= n - offset
    return result


def audit():
    rng = Random(SEED)
    out = Counter()

    for _ in range(SYSTEMS):
        initial_pool_size = rng.randint(4, 8)
        depletion = rng.randint(0, min(2, initial_pool_size - 2))
        initial_pool = list(range(initial_pool_size))
        removed = set(rng.sample(initial_pool, depletion))
        retained_pool = [partner for partner in initial_pool if partner not in removed]
        retained_size = len(retained_pool)
        target_count = rng.randint(1, min(4, retained_size))

        exclusions = []
        capacity_rows = []
        for _target in range(target_count):
            support_count = rng.randint(0, 2)
            line_count = rng.randint(0, 2)
            residual_cap = rng.randint(0, 2)
            new_cap = rng.randint(0, 2)
            cap_row = [
                support_count,
                2 * support_count,
                2 * line_count,
                residual_cap,
                new_cap,
            ]
            target_sets = []
            for cap in cap_row:
                size = rng.randint(0, min(cap, retained_size))
                target_sets.append(set(rng.sample(retained_pool, size)))
            exclusions.append(target_sets)
            capacity_rows.append(cap_row)

        adjacency = []
        declared_deltas = []
        exact_degrees = []
        for target in range(target_count):
            blocked = set().union(*exclusions[target])
            neighbours = {
                retained_pool.index(partner)
                for partner in retained_pool
                if partner not in blocked
            }
            adjacency.append(neighbours)
            declared_delta = sum(capacity_rows[target])
            declared_deltas.append(declared_delta)
            exact_degrees.append(len(neighbours))
            assert len(neighbours) >= retained_size - declared_delta

        delta = max(declared_deltas)
        sigma = retained_size - delta - target_count
        if sigma > 0:
            assert all(degree >= retained_size - delta for degree in exact_degrees)
            out["positive_slack"] += 1
        else:
            assert delta + target_count >= retained_size
            out["nonpositive_slack"] += 1

        for target in range(target_count):
            for partner_index, partner in enumerate(retained_pool):
                compatible = all(partner not in block for block in exclusions[target])
                assert compatible == (partner_index in adjacency[target])
                out["compat_pairs"] += 1

        costs = [rng.randint(0, 4) for _ in retained_pool]
        matching_size = maximum_matching(adjacency, retained_size)
        if matching_size == target_count:
            minimum_cost, matching_count = minimum_cost_matching(adjacency, costs)
            assert minimum_cost is not None
            layer_cake = 0
            for threshold in range(max(costs) + 1):
                threshold_graph = [
                    {right for right in neighbours if costs[right] <= threshold}
                    for neighbours in adjacency
                ]
                nu = maximum_matching(threshold_graph, retained_size)
                layer_cake += target_count - nu
            assert layer_cake == minimum_cost
            out["full_matchings"] += 1
            out["min_cost"] += minimum_cost
            out["matching_count"] += matching_count
        else:
            out["hall_failures"] += 1

        theta_num = rng.randint(1, 3)
        theta_den = rng.randint(theta_num, 4)
        local_layers = []
        labels = []
        for _layer in range(rng.randint(1, 6)):
            reverse_load = rng.randint(0, 8)
            forward_degree = rng.randint(0, 8)
            shortfall = max(0, theta_num * reverse_load - theta_den * forward_degree)
            local_layers.append((reverse_load, forward_degree, shortfall))
            labels.append(rng.choice(CLASS_NAMES))

        aggregate_shortfall = max(
            0,
            theta_num * sum(layer[0] for layer in local_layers)
            - theta_den * sum(layer[1] for layer in local_layers),
        )
        assert aggregate_shortfall <= sum(layer[2] for layer in local_layers)
        class_shortfall = Counter()
        for label, layer in zip(labels, local_layers):
            class_shortfall[label] += layer[2]
        assert sum(class_shortfall.values()) == sum(layer[2] for layer in local_layers)

        class_capacity = {}
        for label in CLASS_NAMES:
            if rng.random() < 0.8:
                class_capacity[label] = class_shortfall[label] + rng.randint(0, 5)
            else:
                class_capacity[label] = max(
                    0, class_shortfall[label] - rng.randint(1, 3)
                )
        overloaded = [
            label
            for label in CLASS_NAMES
            if class_shortfall[label] > class_capacity[label]
        ]
        if overloaded:
            out["shortfall_overloads"] += 1
        else:
            out["shortfall_paid"] += 1

        paid_failure_bound = 0
        for _label in CLASS_NAMES:
            threshold = rng.randint(1, 4)
            initial_capacity = rng.randint(0, 12)
            deposits = rng.randint(0, 8)
            paid_failure_bound += (initial_capacity + deposits) // threshold

        resource_count = rng.randint(1, 4)
        betas = [rng.randint(1, 5) for _ in range(resource_count)]
        low_ticket_stock = 0
        for beta in betas:
            for _height in range(beta):
                low_ticket_stock += rng.randint(0, 4)
        low_slots = sum(betas)

        atom_count = rng.randint(1, 6)
        recreation_edge_count = rng.randint(1, 7)
        recreation_ticket_stock = atom_count * recreation_edge_count

        control_count = rng.randint(1, 4)
        modulus = rng.randint(2, 6)
        strip_threshold = rng.randint(1, 6)
        phase_count = control_count * modulus
        transition = []
        increment = []
        for state in range(phase_count):
            next_control = rng.randrange(control_count)
            next_residue = rng.randrange(modulus)
            next_state = next_control * modulus + next_residue
            multiple = rng.randint(-1, 1)
            residue = state % modulus
            delta_value = next_residue - residue + multiple * modulus
            transition.append(next_state)
            increment.append(delta_value)
            assert (residue + delta_value) % modulus == next_residue

        start = rng.randrange(phase_count)
        seen = {}
        orbit = []
        state = start
        while state not in seen:
            seen[state] = len(orbit)
            orbit.append(state)
            state = transition[state]
        cycle_start = seen[state]
        cycle = orbit[cycle_start:]
        drift = sum(increment[phase] for phase in cycle)
        assert drift % modulus == 0
        assert cycle_start + len(cycle) <= phase_count
        if drift > 0:
            out["tail_positive"] += 1
        elif drift == 0:
            out["tail_zero"] += 1
        else:
            out["tail_negative"] += 1

        injection_states = sum(
            falling_factorial(retained_size, length)
            for length in range(target_count + 1)
        )
        enumerated_states = sum(
            sum(1 for _ in permutations(retained_pool, length))
            for length in range(target_count + 1)
        )
        assert injection_states == enumerated_states

        rank_star = rng.randint(1, 100)
        restart_star = rng.randint(0, 50)
        deficit_star = rng.randint(0, 20)
        deficit_weight = (restart_star + 1) * (rank_star + 1)
        manifest_potential_star = (
            deficit_star * deficit_weight
            + restart_star * (rank_star + 1)
            + rank_star
        )
        # The restricted compiler includes the ambient prefix-state stock in the
        # exact kernel maximum before applying AC5ih.
        kernel_potential_star = manifest_potential_star + injection_states
        strip_states = control_count * strip_threshold
        episode_bound = (
            kernel_potential_star
            + paid_failure_bound
            + low_ticket_stock
            + recreation_ticket_stock
            + strip_states
            + phase_count
        )
        assert episode_bound >= injection_states

        out.update(
            restricted_states=injection_states,
            low_slots=low_slots,
            low_tickets=low_ticket_stock,
            recreation_tickets=recreation_ticket_stock,
            strip_states=strip_states,
            phase_states=phase_count,
            paid_failure_bound=paid_failure_bound,
            compiled_bound=episode_bound,
        )

    return out


def main():
    got = audit()
    expected = {
        "positive_slack": 129,
        "nonpositive_slack": 2371,
        "compat_pairs": 30698,
        "full_matchings": 1735,
        "hall_failures": 765,
        "min_cost": 5209,
        "matching_count": 39177,
        "shortfall_paid": 1990,
        "shortfall_overloads": 510,
        "tail_positive": 881,
        "tail_zero": 735,
        "tail_negative": 884,
        "restricted_states": 381054,
        "low_slots": 18682,
        "low_tickets": 37532,
        "recreation_tickets": 35310,
        "strip_states": 22167,
        "phase_states": 25407,
        "paid_failure_bound": 62684,
        "compiled_bound": 36546268,
    }
    assert dict(got) == expected
    print(
        f"systems={SYSTEMS} compat_pairs={got['compat_pairs']} "
        f"positive_slack={got['positive_slack']} "
        f"nonpositive_slack={got['nonpositive_slack']}"
    )
    print(
        f"full_matchings={got['full_matchings']} hall_failures={got['hall_failures']} "
        f"min_cost={got['min_cost']} shortfall_paid={got['shortfall_paid']} "
        f"shortfall_overloads={got['shortfall_overloads']}"
    )
    print(
        f"restricted_states={got['restricted_states']} low_tickets={got['low_tickets']} "
        f"recreation_tickets={got['recreation_tickets']} strip_states={got['strip_states']} "
        f"phase_states={got['phase_states']} compiled_bound={got['compiled_bound']}"
    )


if __name__ == "__main__":
    main()
