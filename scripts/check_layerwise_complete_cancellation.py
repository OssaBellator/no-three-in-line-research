#!/usr/bin/env python3
import json
import sys


def main(path: str) -> None:
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    sizes = [int(value) for value in data["layer_sizes"]]
    records = data["first_insertion_records"]
    first_credit = int(data["first_removal_credit"])
    second_costs = [int(value) for value in data["second_insertion_costs"]]

    if len(second_costs) != len(sizes):
        raise ValueError("second_insertion_costs must match layer count")

    total_insertion = sum(int(record["weight"]) for record in records)
    removed = [0] * len(sizes)
    for record in records:
        weight = int(record["weight"])
        layers = sorted({int(value) for value in record["layers"]})
        if not layers:
            raise ValueError("every first insertion record must meet an inserted layer")
        removed[layers[0]] += weight

    if sum(removed) != total_insertion:
        raise AssertionError("layerwise assignment did not cover all insertion mass")

    helper_volume = sum(size * size for size in sizes)
    total_size = sum(sizes)
    if helper_volume > total_size * total_size:
        raise AssertionError("sum of layer squares exceeded total square")

    composite = (
        total_insertion
        - first_credit
        + sum(cost - removal for cost, removal in zip(second_costs, removed))
    )
    expected_bound = -first_credit + sum(second_costs)
    if composite > expected_bound:
        raise AssertionError("composite cancellation bound failed")

    print("layer sizes", sizes)
    print("total marked size", total_size)
    print("layer helper square volume", helper_volume)
    print("global square budget", total_size * total_size)
    print("first insertion cost", total_insertion)
    print("layerwise removed insertion", removed)
    print("second insertion costs", second_costs)
    print("first removal credit", first_credit)
    print("composite change", composite)
    print("composite upper bound", expected_bound)
    print("outcome layerwise_complete_insertion_cancellation")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} INPUT.json")
    main(sys.argv[1])
