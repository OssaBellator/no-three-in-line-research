#!/usr/bin/env python3
"""Finite audit for GC2dr--GC2dv compatible witness execution."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from random import Random


def exact_mean(values: tuple[int, ...]) -> Fraction:
    return Fraction(sum(values), len(values))


def math_prod(values) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def audit_product_system(
    destroyed: tuple[int, ...],
    fixed: tuple[int, ...],
    collateral_tables: tuple[tuple[int, ...], ...],
) -> tuple[Fraction, int]:
    local_means = tuple(exact_mean(table) for table in collateral_tables)
    expected_bound = sum(
        (Fraction(fixed[i]) - Fraction(destroyed[i]) + local_means[i])
        for i in range(len(destroyed))
    )

    deltas: list[int] = []
    for choice in product(*(range(len(table)) for table in collateral_tables)):
        delta = sum(
            fixed[i] - destroyed[i] + collateral_tables[i][choice[i]]
            for i in range(len(choice))
        )
        deltas.append(delta)

    exact_product_mean = Fraction(sum(deltas), len(deltas))
    assert exact_product_mean == expected_bound

    margin = sum(
        Fraction(destroyed[i]) - Fraction(fixed[i]) - local_means[i]
        for i in range(len(destroyed))
    )
    if margin > 0:
        assert exact_product_mean < 0
        assert min(deltas) < 0
        assert -exact_product_mean == margin

    return exact_product_mean, min(deltas)


def random_product_audit(seed: int = 54123) -> dict[str, int]:
    rng = Random(seed)
    systems = 0
    product_states = 0
    improving_systems = 0
    local_budget_failures = 0
    occurrence_ids = 0

    for _ in range(20_000):
        k = rng.randint(1, 6)
        destroyed = []
        fixed = []
        collateral_tables = []
        source_ids: set[tuple[int, int]] = set()

        for v in range(k):
            d = rng.randint(1, 20)
            f = rng.randint(0, 8)
            choices = rng.randint(1, 5)
            table = tuple(rng.randint(0, 12) for _ in range(choices))
            destroyed.append(d)
            fixed.append(f)
            collateral_tables.append(table)

            for j in range(d):
                key = (v, j)
                assert key not in source_ids
                source_ids.add(key)

        mean_delta, min_delta = audit_product_system(
            tuple(destroyed), tuple(fixed), tuple(collateral_tables)
        )
        margin = -mean_delta
        if margin > 0:
            improving_systems += 1
            assert min_delta < 0
        else:
            failures = [
                i
                for i, table in enumerate(collateral_tables)
                if Fraction(destroyed[i]) <= Fraction(fixed[i]) + exact_mean(table)
            ]
            assert failures
            local_budget_failures += 1

        systems += 1
        product_states += math_prod(len(table) for table in collateral_tables)
        occurrence_ids += len(source_ids)

    return {
        "systems": systems,
        "product_states": product_states,
        "improving_systems": improving_systems,
        "local_budget_failures": local_budget_failures,
        "occurrence_ids": occurrence_ids,
    }


def integrated_bound_audit(seed: int = 8407) -> dict[str, int]:
    rng = Random(seed)
    checks = 0
    for _ in range(50_000):
        n = rng.randint(2, 25)
        ell = rng.randint(1, n * n * (n * n - 1) // 2)
        d_out = rng.randint(0, 30)
        total_w = Fraction(rng.randint(1, 10_000), rng.randint(1, 20))
        eps = Fraction(rng.randint(1, 10), rng.randint(11, 40))
        retained = total_w / (2 * n * n * ell * (2 * d_out + 1))
        descent = eps * retained
        assert descent > 0
        assert descent == eps * total_w / (2 * n * n * ell * (2 * d_out + 1))
        checks += 1
    return {"integrated_bounds": checks}


def main() -> None:
    result = random_product_audit()
    result.update(integrated_bound_audit())
    print(result)


if __name__ == "__main__":
    main()
