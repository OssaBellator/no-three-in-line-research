# Frontier pass: explicit p=19 zero certificate

## Active branch

`agent/ac-p19-certificate-audit`

Parent: `agent/ac-explicit-p19-zero-certificate` at `3a48afc3ab4521dffa96809066768a1562b9b46a`.

Only AC remains active. Historical side branches are immutable source libraries.

## Completed theorem block

- **AC5nb:** the five-triple checkpoint has exact lower barrier seven.
- **AC5nc:** the four-triple checkpoint has exact lower barrier six.
- **AC5nd:** the two-triple checkpoint has exact lower barrier six.
- **AC5ne:** the one-triple checkpoint has exact barrier five to zero.
- **AC5nf:** the displayed red and blue permutations form a 36-point no-three-in-line set on the 18 by 18 board.
- **AC5ng:** the explicit modular-hyperbola initial state has a complete finite terminal trajectory.

## Standalone deterministic replay

Run:

```text
python scripts/verify_ac_explicit_p19_zero_certificate.py
```

The verifier reconstructs the `H_7` and `H_1` seed, applies the canonical alternating-star matching, and then replays all stored two-row switches. It recomputes every path potential from the exact real-line census and checks every move against both permutation and opposite-layer collision constraints.

The audit verifies:

- real board lines containing at least three cells: `4,398`;
- alternating-star installed potential: `41`;
- post-installation switches: `389`;
- total physical operations including the AN installation: `390`;
- barrier-six component above the five-triple checkpoint: `5` states;
- barrier-five component above the four-triple checkpoint: `16` states;
- barrier-five component above the two-triple checkpoint: `181` states;
- one-triple components at barriers two, three and four: `2`, `5` and `56` states;
- exact checkpoint barriers: `7`, `6`, `6`, `5`;
- final selected cells: `36`;
- final collinear-triple potential: `0`.

Every stored path edge is also checked by a full recomputation of the line potential. The low-barrier component searches use the independently derived incremental line-count update and reproduce all committed component sizes.

## Explicit terminal configuration

The red permutation is

```text
4, 15, 11, 14, 7, 3, 18, 9, 16, 2, 12, 1, 5, 8, 17, 10, 6, 13
```

and the blue permutation is

```text
12, 7, 3, 10, 5, 15, 14, 11, 18, 9, 4, 16, 17, 2, 1, 6, 13, 8.
```

Their union is two points in each row and column and has no real collinear triple.

## Remaining AC frontier

1. Compress the 389-switch certificate by symmetry, cycle deletion and local-template reuse.
2. Identify the structural reason for the exact low-potential barriers.
3. Generate and test analogous physical AN seeds for neighbouring prime-minus-one boards.
4. Replace board-specific switch paths by a parameterized repair template or a finite exceptional-size table.
5. Complete the unresolved uniform AC1 arithmetic and repair/source compatibility predicates.

This proves only the `n=18` special case and one explicit initial-state termination manifest. AC6 and the general no-three-in-line conjecture remain open.
