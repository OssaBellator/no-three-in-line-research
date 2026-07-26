#!/usr/bin/env python3
import json
import sys


def main(path: str) -> None:
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    R = int(data["R"])
    W = int(data["W"])
    selected_size = int(data["selected_size"])
    xi = float(data["xi"])
    gamma = float(data["gamma"])
    marked_controllers = int(data["selected_marked_controllers"])
    helper_controllers = int(data["selected_helper_controllers"])
    punctures = marked_controllers + helper_controllers

    if selected_size > W:
        raise AssertionError("selected size exceeds W")
    if punctures > 2 * selected_size:
        raise AssertionError("selected puncture count exceeds 2s")

    original = (gamma + xi) * R
    after = original - punctures
    half_margin = (gamma + xi / 2.0) * R

    if after < half_margin:
        raise AssertionError("half-margin certificate did not survive")
    if int(data["selected_positive_supports"]) != 0:
        raise AssertionError("chosen helper block is not support-free")

    print("R", R)
    print("W", W)
    print("selected marked size", selected_size)
    print("ambient controller density", data["ambient_controller_density"])
    print("selected marked controllers", marked_controllers)
    print("selected helper controllers", helper_controllers)
    print("total selected punctures", punctures)
    print("puncture to R ratio", punctures / R)
    print("original domain lower bound", original)
    print("post-puncture lower bound", after)
    print("half-margin threshold", half_margin)
    print("selected positive supports", data["selected_positive_supports"])
    print("outcome selected_helper_puncturing_bypasses_full_controller_density")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} INPUT.json")
    main(sys.argv[1])
