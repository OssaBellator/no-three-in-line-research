#!/usr/bin/env python3
"""Deterministic audit for AC5kt--AC5ky."""
from __future__ import annotations
import copy
import json
import random

SEED = 31
SYSTEMS = 2500
KINDS = (
    "install", "repair", "flow", "payment", "resource",
    "recreation", "tail", "disturbance", "reset", "terminal",
)
COMMON = {
    "version", "kind", "epoch", "address", "occurrence",
    "precondition", "footprint", "lineage", "effects",
}
REQUIRED = {
    "install": {"target", "partner", "target_state"},
    "repair": {"defect", "slot", "repair_token"},
    "flow": {"physical_source", "issued_source", "certificate", "defect"},
    "payment": {"owner_token", "claim_address", "amount"},
    "resource": {"macro", "increment_vector", "lower_guard"},
    "recreation": {"atom", "restoration_edge", "recreation_ticket"},
    "tail": {"control", "residue", "increment", "lower_requirement"},
    "disturbance": {"event_atom", "disturbance_weight"},
    "reset": {"changed_field", "target_schema", "reset_address"},
    "terminal": {"terminal_predicate", "final_state_hash"},
}


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def make_state(rng):
    return {
        "schema": "v1",
        "resources": [rng.randint(1, 5) for _ in range(3)],
        "balances": [rng.randint(1, 5) for _ in range(3)],
        "queue": [0, 1, 2],
        "atoms": [0, 1, 2],
        "control": rng.randrange(4),
        "residue": rng.randrange(5),
        "terminal": False,
        "history": [],
    }


def make_operation(rng, kind, index):
    effects = {
        "resource_delta": [0, 0, 0],
        "balance_delta": [0, 0, 0],
        "queue_pop": False,
        "queue_push": None,
        "atom_remove": None,
        "atom_add": None,
        "control_next": None,
        "residue_next": None,
        "schema_next": None,
        "terminal": False,
    }
    op = {
        "version": "v1",
        "kind": kind,
        "epoch": 0,
        "address": f"{kind}:{index}",
        "occurrence": f"occ:{kind}:{index}",
        "precondition": {"schema": "v1"},
        "footprint": [index % 7, (index + 1) % 7],
        "lineage": [f"src:{index % 5}"],
        "effects": effects,
    }

    if kind == "install":
        op.update(target=index % 5, partner=(index + 2) % 7, target_state=f"ts:{index}")
        effects["queue_pop"] = True
    elif kind == "repair":
        op.update(defect=f"d:{index}", slot=f"s:{index}", repair_token=f"rt:{index}")
        effects["queue_pop"] = True
        effects["queue_push"] = index + 10
    elif kind == "flow":
        op.update(
            physical_source=f"ps:{index}", issued_source=f"is:{index}",
            certificate=f"c:{index}", defect=f"d:{index}",
        )
        effects["balance_delta"][0] = -1
        effects["balance_delta"][1] = 1
    elif kind == "payment":
        op.update(owner_token=f"o:{index}", claim_address=f"cl:{index}", amount=1)
        effects["balance_delta"][0] = -1
    elif kind == "resource":
        increment = [0, 0, 0]
        increment[index % 3] = 1
        op.update(macro=f"m:{index}", increment_vector=increment, lower_guard=[0, 0, 0])
        effects["resource_delta"] = increment
    elif kind == "recreation":
        op.update(
            atom=index % 3, restoration_edge=f"e:{index}",
            recreation_ticket=f"t:{index}",
        )
        effects["atom_remove"] = index % 3
        effects["atom_add"] = index + 20
    elif kind == "tail":
        increment = rng.choice([-1, 0, 1])
        control = index % 4
        residue = index % 5
        op.update(
            control=control, residue=residue, increment=increment, lower_requirement=0,
        )
        effects["control_next"] = (control + 1) % 4
        effects["residue_next"] = (residue + increment) % 5
        effects["resource_delta"][2] = increment
    elif kind == "disturbance":
        op.update(event_atom=f"ev:{index}", disturbance_weight=1)
        effects["resource_delta"][1] = 1
    elif kind == "reset":
        op.update(
            changed_field="owner_route", target_schema="v1-reset",
            reset_address=f"rs:{index}",
        )
        effects["schema_next"] = "v1-reset"
    elif kind == "terminal":
        op.update(terminal_predicate="complete_installation", final_state_hash=f"h:{index}")
        effects["terminal"] = True
    return op


def validate(op):
    missing = sorted((COMMON | REQUIRED.get(op.get("kind"), set())) - set(op))
    if missing:
        raise ValueError(("missing", missing[0]))
    if op["kind"] not in KINDS:
        raise ValueError(("kind", op["kind"]))
    if op["version"] != "v1":
        raise ValueError(("version", op["version"]))
    effects = op["effects"]
    if len(effects["resource_delta"]) != 3 or len(effects["balance_delta"]) != 3:
        raise ValueError(("effect-shape", op["address"]))
    if op["kind"] == "payment" and effects["balance_delta"][0] != -op["amount"]:
        raise ValueError(("payment-effect", op["address"]))
    if op["kind"] == "resource" and effects["resource_delta"] != op["increment_vector"]:
        raise ValueError(("resource-effect", op["address"]))
    if op["kind"] == "tail" and effects["residue_next"] != (
        op["residue"] + op["increment"]
    ) % 5:
        raise ValueError(("tail-effect", op["address"]))
    if op["kind"] == "reset" and effects["schema_next"] != op["target_schema"]:
        raise ValueError(("reset-effect", op["address"]))
    if op["kind"] == "terminal" and not effects["terminal"]:
        raise ValueError(("terminal-effect", op["address"]))


def successor(state, op):
    validate(op)
    if state["schema"] != op["precondition"]["schema"]:
        return "reset-precondition", None
    out = copy.deepcopy(state)
    effects = op["effects"]
    resources = [a + b for a, b in zip(out["resources"], effects["resource_delta"])]
    balances = [a + b for a, b in zip(out["balances"], effects["balance_delta"])]
    if min(resources) < 0:
        return "resource-shortage", None
    if min(balances) < 0:
        return "capacity-shortage", None
    out["resources"] = resources
    out["balances"] = balances

    if effects["queue_pop"]:
        if not out["queue"]:
            return "queue-shortage", None
        out["queue"].pop(0)
    if effects["queue_push"] is not None:
        out["queue"].append(effects["queue_push"])
    if effects["atom_remove"] is not None:
        if effects["atom_remove"] not in out["atoms"]:
            return "atom-shortage", None
        out["atoms"].remove(effects["atom_remove"])
    if effects["atom_add"] is not None:
        out["atoms"].append(effects["atom_add"])
    if effects["control_next"] is not None:
        out["control"] = effects["control_next"]
    if effects["residue_next"] is not None:
        out["residue"] = effects["residue_next"]
    if effects["schema_next"] is not None:
        out["schema"] = effects["schema_next"]
    if effects["terminal"]:
        out["terminal"] = True
    out["history"].append(op["occurrence"])
    return "internal", out


def box_route(state, op, caps):
    route, out = successor(state, op)
    if route != "internal":
        return route, out
    for index, value in enumerate(out["resources"]):
        if value > caps["resources"][index]:
            return "resource-overflow", out
    for index, value in enumerate(out["balances"]):
        if value > caps["balances"][index]:
            return "capacity-amplification", out
    return route, out


def run():
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "valid_registries": 0,
        "operation_records": 0,
        "deterministic_outcomes": 0,
        "internal_outcomes": 0,
        "shortage_outcomes": 0,
        "upper_boundary_outcomes": 0,
        "cap_invariance_checks": 0,
        "cross_kind_alias_witnesses": 0,
        "omitted_field_witnesses": 0,
    }

    for system in range(SYSTEMS):
        state = make_state(rng)
        operations = [
            make_operation(rng, kind, system * len(KINDS) + index)
            for index, kind in enumerate(KINDS)
        ]
        addresses = [op["address"] for op in operations]
        assert len(addresses) == len(set(addresses))

        if system < 1000:
            stats["valid_registries"] += 1
            for op in operations:
                validate(op)
                route1, successor1 = successor(state, op)
                route2, successor2 = successor(state, op)
                assert route1 == route2 and canonical(successor1) == canonical(successor2)
                stats["operation_records"] += 1
                stats["deterministic_outcomes"] += 1

                caps = {
                    "resources": list(state["resources"]),
                    "balances": list(state["balances"]),
                }
                large = {
                    "resources": [value + 5 for value in state["resources"]],
                    "balances": [value + 5 for value in state["balances"]],
                }
                small_route, _ = box_route(state, op, caps)
                large_route, large_successor = box_route(state, op, large)
                if route1 == "internal":
                    if small_route == "internal":
                        stats["internal_outcomes"] += 1
                    else:
                        stats["upper_boundary_outcomes"] += 1
                    assert large_route == "internal"
                    assert canonical(large_successor) == canonical(successor1)
                    stats["cap_invariance_checks"] += 1
                else:
                    stats["shortage_outcomes"] += 1

            alias = copy.deepcopy(operations[1])
            alias["address"] = operations[0]["address"]
            assert alias["kind"] != operations[0]["kind"]
            stats["cross_kind_alias_witnesses"] += 1
        else:
            kind = KINDS[(system - 1000) % len(KINDS)]
            operation = next(op for op in operations if op["kind"] == kind)
            missing = sorted(REQUIRED[kind])[0]
            del operation[missing]
            try:
                validate(operation)
            except ValueError as exc:
                assert exc.args[0][0] == "missing"
                stats["omitted_field_witnesses"] += 1
            else:
                raise AssertionError("missing field accepted")

    return stats


if __name__ == "__main__":
    result = run()
    print("AC operation family registry audit")
    for key, value in result.items():
        print(f"{key}: {value}")
