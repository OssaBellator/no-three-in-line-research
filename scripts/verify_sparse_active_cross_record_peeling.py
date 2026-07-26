#!/usr/bin/env python3
"""Finite audit for SAS5db--SAS5dg active cross-record peeling."""

from __future__ import annotations

from itertools import combinations
from random import Random


def active_stock(records: list[dict], donors: set[int]) -> tuple[int, int]:
    omega = 0
    cminus = 0
    for rec in records:
        incidences = rec["inc"] & donors
        if incidences:
            omega += rec["weight"]
            cminus += len(incidences) * rec["weight"]
    return omega, cminus


def donor_negative(records: list[dict], donor: int) -> int:
    return sum(rec["weight"] for rec in records if donor in rec["inc"])


def exhaustive_incidence_audit() -> dict[str, int]:
    systems = 0
    identities = 0
    peel_tests = 0
    for n in range(1, 6):
        donors = set(range(n))
        possible = [(i,) for i in range(n)] + list(combinations(range(n), 2))
        # Small deterministic families: one record for each selected incidence pattern.
        for take in range(1, min(5, len(possible)) + 1):
            records = [
                {"inc": set(possible[j]), "weight": (j % 4) + 1}
                for j in range(take)
            ]
            omega, cminus = active_stock(records, donors)
            direct = sum(donor_negative(records, d) for d in donors)
            assert cminus == direct
            assert omega <= cminus <= 2 * omega
            identities += 1

            heavy = max(records, key=lambda r: r["weight"])
            assert 1 <= len(heavy["inc"]) <= 2
            for d in heavy["inc"]:
                assert donor_negative(records, d) >= heavy["weight"]

            residual_donors = donors - heavy["inc"]
            residual_records = [r for r in records if r is not heavy]
            omega_res_bound = omega - heavy["weight"]
            _, cminus_res = active_stock(records, residual_donors)
            assert cminus_res <= 2 * omega_res_bound
            # Removing the record itself gives the same or a smaller exact active stock.
            exact_omega_res, exact_cminus_res = active_stock(residual_records, residual_donors)
            assert exact_cminus_res == cminus_res
            assert exact_omega_res <= omega_res_bound
            peel_tests += 1
            systems += 1
    return {
        "exhaustive_systems": systems,
        "exact_incidence_identities": identities,
        "exhaustive_peels": peel_tests,
    }


def random_energy_audit(rng: Random, trials: int = 60000) -> dict[str, int]:
    five_way = 0
    deep_improvements = 0
    residual_scale = 0
    residual_collateral = 0
    peel_steps = 0
    for _ in range(trials):
        n = rng.randint(1, 12)
        donors = set(range(n))
        records: list[dict] = []
        for _ in range(rng.randint(1, 30)):
            size = 1 if n == 1 or rng.random() < 0.55 else 2
            inc = set(rng.sample(range(n), size))
            records.append({"inc": inc, "weight": rng.randint(1, 30)})

        omega_act, cminus_bank = active_stock(records, donors)
        assert omega_act <= cminus_bank <= 2 * omega_act

        delta_omega = rng.randint(0, 25)
        delta_tau = {d: rng.randint(0, 25) for d in donors}
        selected = {d: rng.randint(1, 30) for d in donors}
        cplus = {d: rng.randint(0, 25) for d in donors}
        cminus = {d: donor_negative(records, d) for d in donors}
        delta_comb = {
            d: delta_omega + delta_tau[d] + selected[d] + cplus[d] - cminus[d]
            for d in donors
        }
        lhs = sum(delta_comb.values())
        l_bank = sum(selected.values())
        assert lhs >= l_bank - 2 * omega_act

        heavy = max(records, key=lambda r: r["weight"])
        omega_star = heavy["weight"]
        incident = sorted(heavy["inc"])
        canonical = incident[0]
        assert cminus[canonical] >= omega_star
        if delta_comb[canonical] <= -omega_star / 2:
            deep_improvements += 1
        else:
            terms = [delta_omega, delta_tau[canonical], selected[canonical], cplus[canonical]]
            assert max(terms) > omega_star / 8
        five_way += 1

        residual = donors - heavy["inc"]
        l_res = sum(selected[d] for d in residual)
        omega_res_bound = omega_act - omega_star
        cminus_res = sum(cminus[d] - (omega_star if d in heavy["inc"] else 0) for d in residual)
        # For residual donors the heavy record has no incidence, so the direct sum suffices.
        cminus_res_direct = sum(donor_negative(records, d) for d in residual)
        assert cminus_res == cminus_res_direct
        assert cminus_res <= 2 * omega_res_bound
        if residual:
            residual_sum = sum(delta_comb[d] for d in residual)
            assert residual_sum >= l_res - 2 * omega_res_bound
            if l_res > 2 * omega_res_bound:
                assert max(delta_comb[d] for d in residual) >= (l_res - 2 * omega_res_bound) / len(residual)
                residual_scale += 1
            elif all(delta_comb[d] <= 0 for d in residual):
                assert omega_res_bound >= l_res / 2
                residual_collateral += 1

        # Repeatedly remove a heaviest active record and all its incident donors.
        current_donors = set(donors)
        previous_active = len(records) + 1
        while current_donors:
            active = [r for r in records if r["inc"] & current_donors]
            if not active:
                break
            assert len(active) < previous_active or previous_active == len(records) + 1
            previous_active = len(active)
            q = max(active, key=lambda r: r["weight"])
            current_donors -= q["inc"]
            peel_steps += 1
            remaining_active = [r for r in active if r is not q and r["inc"] & current_donors]
            assert len(remaining_active) <= len(active) - 1
    return {
        "random_systems": trials,
        "five_way_routers": five_way,
        "deep_improvements": deep_improvements,
        "residual_scale_dominant": residual_scale,
        "residual_collateral_dominant": residual_collateral,
        "iterative_peel_steps": peel_steps,
    }


def main() -> None:
    rng = Random(0x5A5DB)
    counts = exhaustive_incidence_audit()
    counts.update(random_energy_audit(rng))
    print("SAS active cross-record peeling audit passed")
    for key, value in counts.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
