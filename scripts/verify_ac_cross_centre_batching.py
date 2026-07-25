#!/usr/bin/env python3
"""Exhaust AC3al on small residual-support systems."""

from itertools import combinations, product


def maximum_disjoint_weight(scopes, weights):
    best = 0
    for mask in range(1 << len(scopes)):
        chosen = [index for index in range(len(scopes)) if mask & (1 << index)]
        if all(
            scopes[left].isdisjoint(scopes[right])
            for left, right in combinations(chosen, 2)
        ):
            best = max(best, sum(weights[index] for index in chosen))
    return best


def verify(maximum_blocks=3, maximum_arms=5, maximum_weight=2):
    scope_options = [frozenset()]
    for rank in (1, 2):
        scope_options.extend(
            frozenset(choice)
            for choice in combinations(range(maximum_blocks), rank)
        )

    for arm_count in range(1, maximum_arms + 1):
        for scopes in product(scope_options, repeat=arm_count):
            for weights in product(range(1, maximum_weight + 1), repeat=arm_count):
                total_weight = sum(weights)
                optimum = maximum_disjoint_weight(scopes, weights)
                for reuse_cap in range(1, arm_count + 1):
                    loads = [
                        sum(block in scope for scope in scopes)
                        for block in range(maximum_blocks)
                    ]
                    if any(load > reuse_cap for load in loads):
                        continue
                    assert optimum * (2 * reuse_cap - 1) >= total_weight


def main():
    verify()
    print("AC cross-centre bounded-reuse batching: verified")


if __name__ == "__main__":
    main()
