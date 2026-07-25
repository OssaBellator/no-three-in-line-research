#!/usr/bin/env python3
"""Verify OP4n charge-back from paid factors to improving corrections."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

try:
    from scripts.verify_phase_syndrome_payment import (
        PaymentSystem,
        proportional_payment,
    )
except ModuleNotFoundError:
    from verify_phase_syndrome_payment import (
        PaymentSystem,
        proportional_payment,
    )


Weight = Fraction


@dataclass(frozen=True)
class ChargeSystem:
    gains: tuple[Weight, ...]
    charges: tuple[tuple[Weight, ...], ...]
    rank: int

    def validate(self) -> None:
        assert self.gains
        assert self.charges
        assert len(self.charges) == len(self.gains)
        factor_count = len(self.charges[0])
        assert factor_count > 0
        assert all(len(row) == factor_count for row in self.charges)
        assert all(gain > 0 for gain in self.gains)
        assert all(charge >= 0 for row in self.charges for charge in row)
        assert 1 <= self.rank <= len(self.gains)
        for gain, row in zip(self.gains, self.charges):
            assert sum(row, Fraction()) <= gain
        for factor in range(factor_count):
            degree = sum(
                row[factor] > 0 for row in self.charges
            )
            assert degree <= self.rank

    @property
    def factor_count(self) -> int:
        return len(self.charges[0])

    def factor_load(self, factor: int) -> Weight:
        return sum(
            (row[factor] for row in self.charges),
            Fraction(),
        )


@dataclass(frozen=True)
class ChargeBack:
    correction: int
    factor: int
    charge: Weight
    gain: Weight
    fibre_payment: Weight
    fibre_size: int


def charge_back(
    system: ChargeSystem,
    factors: frozenset[int],
) -> ChargeBack:
    system.validate()
    assert factors
    assert all(0 <= factor < system.factor_count for factor in factors)
    payment = sum(
        (system.factor_load(factor) for factor in factors),
        Fraction(),
    )
    assert payment > 0
    candidates = tuple(
        (system.charges[correction][factor], correction, factor)
        for correction in range(len(system.gains))
        for factor in factors
        if system.charges[correction][factor] > 0
    )
    assert candidates
    charge, correction, factor = max(candidates)
    assert system.gains[correction] >= charge
    assert (
        charge * system.rank * len(factors)
        >= payment
    )
    return ChargeBack(
        correction=correction,
        factor=factor,
        charge=charge,
        gain=system.gains[correction],
        fibre_payment=payment,
        fibre_size=len(factors),
    )


def verify_occurrence_reaggregation(
    system: ChargeSystem,
    factors: frozenset[int],
) -> None:
    occurrences = tuple(
        factor
        for factor in sorted(factors)
        for _ in range(factor + 2)
    )
    occurrence_weights = tuple(
        system.factor_load(factor) / occurrences.count(factor)
        for factor in occurrences
    )
    for factor in factors:
        assert sum(
            (
                weight
                for source, weight in zip(
                    occurrences,
                    occurrence_weights,
                )
                if source == factor
            ),
            Fraction(),
        ) == system.factor_load(factor)
    assert sum(occurrence_weights, Fraction()) == sum(
        (system.factor_load(factor) for factor in factors),
        Fraction(),
    )


def verify_all_fibres(system: ChargeSystem) -> int:
    system.validate()
    cases = 0
    for mask in range(1, 1 << system.factor_count):
        factors = frozenset(
            factor
            for factor in range(system.factor_count)
            if mask & (1 << factor)
        )
        payment = sum(
            (system.factor_load(factor) for factor in factors),
            Fraction(),
        )
        if payment == 0:
            continue
        result = charge_back(system, factors)
        assert result.gain * system.rank * len(factors) >= payment
        verify_occurrence_reaggregation(system, factors)
        cases += 1
    return cases


def verify_charge_matrices() -> tuple[int, int]:
    systems = 0
    fibres = 0
    correction_count = 3
    factor_count = 3
    for integer_entries in product(
        (0, 1, 2),
        repeat=correction_count * factor_count,
    ):
        rows = tuple(
            tuple(
                Fraction(
                    integer_entries[
                        correction * factor_count + factor
                    ]
                )
                for factor in range(factor_count)
            )
            for correction in range(correction_count)
        )
        if not any(charge > 0 for row in rows for charge in row):
            continue
        rank = max(
            sum(row[factor] > 0 for row in rows)
            for factor in range(factor_count)
        )
        if rank == 0 or rank > 3:
            continue
        row_loads = tuple(sum(row, Fraction()) for row in rows)
        gains = tuple(
            load if load > 0 else Fraction(1)
            for load in row_loads
        )
        system = ChargeSystem(gains=gains, charges=rows, rank=rank)
        fibres += verify_all_fibres(system)
        systems += 1
    return systems, fibres


def verify_proportional_integration() -> int:
    payment_system = PaymentSystem(
        factor_weights=(
            Fraction(2),
            Fraction(3),
            Fraction(1),
        ),
        neighborhoods=(
            frozenset({0, 1}),
            frozenset({0, 2}),
            frozenset({1, 2}),
        ),
        gains=(
            Fraction(4),
            Fraction(2),
            Fraction(3),
        ),
    )
    payment = proportional_payment(payment_system)
    charge_system = ChargeSystem(
        gains=payment_system.gains,
        charges=payment.incidence,
        rank=payment_system.rank,
    )
    cases = verify_all_fibres(charge_system)
    for factor in range(charge_system.factor_count):
        load = charge_system.factor_load(factor)
        result = charge_back(charge_system, frozenset({factor}))
        assert result.gain * charge_system.rank >= load
    return cases


def verify_divisor_fibres() -> None:
    rank = 3
    for capacity in (1, 2, 5, 16):
        charges = tuple(
            tuple(
                Fraction(1)
                if correction // rank == factor
                else Fraction()
                for factor in range(capacity)
            )
            for correction in range(rank * capacity)
        )
        gains = tuple(Fraction(1) for _ in charges)
        system = ChargeSystem(
            gains=gains,
            charges=charges,
            rank=rank,
        )
        all_factors = frozenset(range(capacity))
        result = charge_back(system, all_factors)
        assert result.fibre_payment == rank * capacity
        assert result.gain == 1
        assert (
            result.gain
            == result.fibre_payment / (rank * capacity)
        )


def verify_sharp_families() -> None:
    for rank in range(1, 4):
        for factor_count in range(1, 6):
            correction_count = rank * factor_count
            charges = tuple(
                tuple(
                    Fraction(1)
                    if correction // rank == factor
                    else Fraction()
                    for factor in range(factor_count)
                )
                for correction in range(correction_count)
            )
            system = ChargeSystem(
                gains=tuple(
                    Fraction(1) for _ in range(correction_count)
                ),
                charges=charges,
                rank=rank,
            )
            result = charge_back(
                system,
                frozenset(range(factor_count)),
            )
            assert result.fibre_payment == rank * factor_count
            assert result.gain == 1
            assert result.charge == 1


def main() -> None:
    systems, fibres = verify_charge_matrices()
    proportional_cases = verify_proportional_integration()
    verify_divisor_fibres()
    verify_sharp_families()
    print(
        "phase charge-back verified:",
        f"{systems} charge matrices,",
        f"{fibres} paid fibres,",
        f"{proportional_cases} proportional fibres,",
        "sharp rank/fibre bounds",
    )


if __name__ == "__main__":
    main()
