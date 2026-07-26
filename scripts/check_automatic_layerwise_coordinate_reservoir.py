#!/usr/bin/env python3
import json
import sys


def main(path: str) -> None:
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    m = int(data["m"])
    R = int(data["R"])
    W = int(data["W"])
    constant = int(data["helper_constant"])
    sizes = [int(value) for value in data["layer_sizes"]]
    reserved = [int(value) for value in data["globally_reserved"]]

    if sum(sizes) > W:
        raise AssertionError("total marked size exceeds W")
    if len(sizes) != len(reserved):
        raise ValueError("layer_sizes and globally_reserved must have equal length")

    demands = [constant * max(size * size, 1) for size in sizes]
    available = [m - block - size for block, size in zip(reserved, sizes)]
    for index, (need, have) in enumerate(zip(demands, available)):
        if need > have:
            raise AssertionError(f"layer {index} lacks the predicted reservoir")

    total_square = sum(size * size for size in sizes)
    total_size = sum(sizes)
    if total_square > total_size * total_size:
        raise AssertionError("layer square demand exceeds global square budget")
    if max(demands) >= m:
        raise AssertionError("helper demand is not subambient in the finite model")
    if R >= m:
        raise AssertionError("R must be smaller than m")

    print("m", m)
    print("R", R)
    print("R to m ratio", R / m)
    print("W", W)
    print("layer marked sizes", sizes)
    print("globally reserved", reserved)
    print("layer helper demands", demands)
    print("layer available coordinates", available)
    print("total layer square demand", total_square)
    print("global square budget", total_size * total_size)
    print("outcome automatic_layerwise_coordinate_reservoir")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} INPUT.json")
    main(sys.argv[1])
