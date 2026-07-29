#!/usr/bin/env python3
"""Finite checks for AC5fp--AC5ft."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Set, Tuple


@dataclass(frozen=True, order=True)
class Record:
    kind: str
    ident: int
    cls: int
    feature: int
    version: int


def compat(r: Record, t: Record) -> bool:
    """Deterministic retained-field compatibility predicate."""
    assert r.kind == "r" and t.kind == "t"
    return r.cls == t.cls and (3 * r.feature + 5 * t.feature + r.ident + t.ident) % 7 not in (0, 1)


def edges(R: Iterable[Record], T: Iterable[Record]) -> Set[Tuple[Record, Record]]:
    return {(r, t) for r in R for t in T if compat(r, t)}


def maximum_matching(
    R: Iterable[Record], T: Iterable[Record], E: Set[Tuple[Record, Record]]
) -> Dict[Record, Record]:
    R = sorted(R)
    T = sorted(T)
    nbr = {r: [t for t in T if (r, t) in E] for r in R}
    owner: Dict[Record, Record] = {}

    def augment(r: Record, seen: Set[Record]) -> bool:
        for t in nbr[r]:
            if t in seen:
                continue
            seen.add(t)
            if t not in owner or augment(owner[t], seen):
                owner[t] = r
                return True
        return False

    for r in R:
        augment(r, set())
    return {r: t for t, r in owner.items()}


def mutate_records(old: List[Record], seed: int, kind: str) -> Tuple[Set[Record], Set[Record], Set[Record]]:
    """Return next records, stable old records, and new/changed records."""
    stable: Set[Record] = set()
    changed: Set[Record] = set()
    for rec in old:
        code = (seed + 11 * rec.ident + 7 * rec.cls + 3 * rec.feature) % 6
        if code in (0, 1, 2):
            stable.add(rec)
        elif code in (3, 4):
            changed.add(
                Record(kind, rec.ident, rec.cls, (rec.feature + 1 + seed % 3) % 8, rec.version + 1)
            )
        # code 5 deletes the record.

    new_count = seed % 3
    base = 100 + 10 * seed + (0 if kind == "r" else 5)
    for j in range(new_count):
        changed.add(Record(kind, base + j, (seed + j) % 3, (2 * seed + 3 * j) % 8, 0))

    next_records = stable | changed
    return next_records, stable, changed


def main() -> None:
    systems = 0
    exact_updates = 0
    corrupted_boundaries = 0
    full_reassignments = 0
    deficient_updates = 0
    pair_checks = 0

    for seed in range(12000):
        nr = 1 + seed % 6
        nt = nr + (seed // 3) % 4
        R = [Record("r", i, (seed + 2 * i) % 3, (seed + 5 * i) % 8, 0) for i in range(nr)]
        T = [Record("t", j, (seed + j) % 3, (3 * seed + 2 * j) % 8, 0) for j in range(nt)]
        E = edges(R, T)
        old_match = maximum_matching(R, T, E)
        if len(old_match) != len(R):
            continue

        R2, R0, dR = mutate_records(R, seed + 17, "r")
        T2, T0, dT = mutate_records(T, seed + 29, "t")
        E2 = edges(R2, T2)

        # AC5fp: unchanged block is copied exactly.
        for r in R0:
            for t in T0:
                assert ((r, t) in E2) == ((r, t) in E)

        # AC5fq: exact disjoint boundary and reconstruction.
        boundary = {(r, t) for r in dR for t in T2} | {(r, t) for r in R0 for t in dT}
        assert len(boundary) == len(dR) * len(T2) + len(R0) * len(dT)
        reconstructed = {(r, t) for r in R0 for t in T0 if (r, t) in E}
        reconstructed |= {(r, t) for r, t in boundary if (r, t) in E2}
        assert reconstructed == E2
        pair_checks += len(boundary)
        exact_updates += 1

        # A flipped boundary bit is found inside the audited boundary.
        if boundary:
            first = min(boundary)
            corrupted = set(reconstructed)
            if first in corrupted:
                corrupted.remove(first)
            else:
                corrupted.add(first)
            assert corrupted != E2
            assert any(((r, t) in corrupted) != ((r, t) in E2) for r, t in boundary)
            corrupted_boundaries += 1

        # AC5fr: carry old matching through stable records and tokens.
        carried = {r: t for r, t in old_match.items() if r in R0 and t in T0}
        assert len(set(carried.values())) == len(carried)
        assert all((r, t) in E2 for r, t in carried.items())
        a = len(dR)
        b = sum(1 for r in R0 if old_match[r] not in T0)
        unmatched = len(R2) - len(carried)
        assert unmatched == a + b

        # AC5fs: the carried matching witnesses deficit at most a+b.
        new_match = maximum_matching(R2, T2, E2)
        deficit = len(R2) - len(new_match)
        assert 0 <= deficit <= a + b
        if deficit == 0:
            augmentations = len(R2) - len(carried)
            assert augmentations <= a + b
            full_reassignments += 1
        else:
            deficient_updates += 1

        systems += 1

    assert systems > 1000
    print(
        "verified "
        f"{systems} incremental repair epochs; "
        f"{exact_updates} exact boundary reconstructions; "
        f"{pair_checks} boundary pair checks; "
        f"{corrupted_boundaries} detected boundary corruptions; "
        f"{full_reassignments} fully assignable and {deficient_updates} deficient updates"
    )


if __name__ == "__main__":
    main()
