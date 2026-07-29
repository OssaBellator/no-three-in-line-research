#!/usr/bin/env python3
"""Deterministic audit for AC consolidated main-focus imports."""
from collections import Counter
from random import Random

SEED = 29001
SYSTEMS = 2500

SCHEMAS = {
    "AC": ("physical_source", "certificate", "defect", "epoch", "repair_class"),
    "RI": ("repair_type", "field_element_data", "host_context", "secant_line_address", "coherence", "collateral_class", "epoch"),
    "BDA": ("physical_source", "numerator_weight", "rational_gain", "damping_factor", "restoration_class", "epoch"),
    "GC": ("physical_source", "donor", "remedy", "height", "cause", "local_geometry", "epoch"),
    "OP": ("repair_type", "physical_source", "unit_class", "valuation_vector", "holonomy", "action_kernel", "epoch"),
    "SRR": ("candidate", "witness_atom", "conditioned_threshold", "physical_source", "tensor_cylinder", "epoch"),
    "SAS": ("repair_type", "sign", "boundary_profile", "neutral_move", "legality_class", "physical_source", "epoch"),
}
VERSIONS = {track: 1 for track in SCHEMAS}

IMPORTS = {
    "RI": {
        "payment": "payment", "descent": "descent", "occurrence_ticket": "ticket",
        "field_ticket": "ticket", "reset": "reset", "failure": "obstruction",
    },
    "BDA": {
        "impossible": "obstruction", "payment": "payment", "descent": "descent",
        "restoration_ticket": "ticket", "reset": "reset",
    },
    "GC": {
        "full_assignment": "supply", "donor_ticket": "ticket",
        "restoration": "payment", "hall_core": "shortage", "reset": "reset",
    },
    "OP": {
        "path_displacement": "descent", "phase_ticket": "ticket",
        "zero_holonomy_payment": "payment", "reset": "reset", "failure": "obstruction",
    },
    "SRR": {
        "robust_hall": "supply", "local_loss": "payment",
        "threshold_shortage": "shortage", "incidence_failure": "obstruction",
    },
    "SAS": {
        "legal_square": "supply", "single_swap_blocker": "obstruction",
        "guard_atom": "obstruction", "reset": "reset",
    },
}

TERMINAL_KINDS = {"shortage", "obstruction"}


def encode(track, record):
    fields = SCHEMAS[track]
    if tuple(record) != fields:
        raise ValueError("record fields do not match schema order")
    return (track, VERSIONS[track], tuple(record.items()))


def decode(code):
    track, version, items = code
    if version != VERSIONS[track]:
        raise ValueError("stale version")
    record = dict(items)
    if tuple(record) != SCHEMAS[track]:
        raise ValueError("field order mismatch")
    return track, record


def random_record(rng, track):
    return {field: rng.randrange(5) for field in SCHEMAS[track]}


def audit():
    rng = Random(SEED)
    out = Counter()
    tracks = tuple(SCHEMAS)
    for _ in range(SYSTEMS):
        out["systems"] += 1
        records = {}
        for track in tracks:
            record = random_record(rng, track)
            code = encode(track, record)
            got_track, got_record = decode(code)
            assert got_track == track and got_record == record
            records[track] = code
            out["roundtrips"] += 1

            field = rng.choice(SCHEMAS[track])
            r2 = dict(record)
            r2[field] = (r2[field] + 1) % 5
            projection1 = tuple((k, v) for k, v in record.items() if k != field)
            projection2 = tuple((k, v) for k, v in r2.items() if k != field)
            assert projection1 == projection2 and record != r2
            out["omission_witnesses"] += 1

        for i, s in enumerate(tracks):
            for t in tracks[i + 1:]:
                assert records[s] != records[t]
                out["cross_track_separations"] += 1

        for mapping in IMPORTS.values():
            for ac_kind in mapping.values():
                assert ac_kind in {
                    "supply", "payment", "descent", "ticket", "reset",
                    "shortage", "obstruction",
                }
                out["import_routes"] += 1
                out["route_" + ac_kind] += 1

        deficit_budget = rng.randint(1, 12)
        disturbance_budget = rng.randint(0, 8)
        resource = {
            "payment": rng.randint(0, 12),
            "descent": rng.randint(0, 12),
            "ticket": rng.randint(0, 12),
            "reset": rng.randint(0, 12),
        }
        bound = deficit_budget + disturbance_budget + sum(resource.values())
        steps = 0
        remaining_deficit_drops = deficit_budget + disturbance_budget
        while remaining_deficit_drops or any(resource.values()):
            available = []
            if remaining_deficit_drops:
                available.append("supply")
            available.extend(k for k, v in resource.items() if v)
            kind = rng.choice(available)
            if kind == "supply":
                remaining_deficit_drops -= 1
                out["supply_steps"] += 1
            else:
                resource[kind] -= 1
                out[kind + "_steps"] += 1
            steps += 1
        assert steps == bound
        out["bounded_episodes"] += steps
        out["episode_bounds"] += bound

        terminal = rng.choice(tuple(TERMINAL_KINDS))
        out["terminal_" + terminal] += 1

    return out


def main():
    got = audit()
    expected = {
        "systems": 2500,
        "roundtrips": 17500,
        "omission_witnesses": 17500,
        "cross_track_separations": 52500,
        "import_routes": 72500,
        "route_payment": 12500,
        "route_descent": 7500,
        "route_ticket": 12500,
        "route_reset": 12500,
        "route_obstruction": 15000,
        "route_supply": 7500,
        "route_shortage": 5000,
        "supply_steps": 26441,
        "payment_steps": 14760,
        "descent_steps": 14959,
        "ticket_steps": 15046,
        "reset_steps": 15184,
        "bounded_episodes": 86390,
        "episode_bounds": 86390,
        "terminal_shortage": 1256,
        "terminal_obstruction": 1244,
    }
    assert dict(got) == expected, (dict(got), expected)
    print(
        f"systems={got['systems']} roundtrips={got['roundtrips']} "
        f"omissions={got['omission_witnesses']} cross_track={got['cross_track_separations']}"
    )
    print(
        f"routes={got['import_routes']} bounded_episodes={got['bounded_episodes']} "
        f"supply={got['supply_steps']} payment={got['payment_steps']} "
        f"descent={got['descent_steps']} ticket={got['ticket_steps']} reset={got['reset_steps']}"
    )


if __name__ == "__main__":
    main()
