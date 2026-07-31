# Exact `(6,1)` support-seven closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5oz--AC5pa for the explicit `p=31`, `n=30` three-triple endpoint. It closes the mixed seven-extra family with exactly six additional red row addresses and one additional blue row address.

## AC5oz -- complete `(6,1)` seven-extra census -- PROVED

The support universe has

\[
\binom{26}{6}25=\boxed{5{,}755{,}750}
\]

members. On every support, retain exactly the current moved values, fix all outside cells, reject red-blue collisions, and prune as soon as the exact partial potential exceeds two.

The complete census examines

\[
\boxed{961{,}623{,}575}
\]

admissible partial states and reaches no complete collision-free endpoint of potential at most two.

### Proof

The support universe is partitioned into 59 contiguous lexicographic intervals. Their exact counts are retained in `data/ac-p31-support-seven-six-one-closure.json`; they cover `[0,5755750)` without overlap or omission. Every branch ends by collision, by partial potential exceeding two, or as a complete assignment. No complete assignment survives. QED.

## AC5pa -- four of eight support-seven distributions closed -- PROVED

No endpoint in distribution `(6,1)` lowers the current three-triple state:

\[
\boxed{\Phi\ge3.}
\]

Together with AC5ov--AC5ow and AC5ox--AC5oy, the closed seven-extra distributions are

\[
(0,7),\ (1,6),\ (6,1),\ (7,0).
\]

Only `(2,5)`, `(3,4)`, `(4,3)`, and `(5,2)` remain.

## Deterministic audit

Compile the generic range verifier:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_seven_range.cpp -o verify_support_seven_range
```

For every ledger triple `(lo,hi,nodes)`, run

```text
./verify_support_seven_range 6 lo hi nodes
```

The interval totals are:

- support choices: `5755750`;
- partial states: `961623575`;
- complete potential-at-most-two endpoints: `0`.

## Remaining frontier

1. Close or solve `(2,5)`, `(3,4)`, `(4,3)`, and `(5,2)`.
2. Finish the independent barrier-nine switch component.
3. Convert any wider-support endpoint into a legal low-barrier switch ordering.
4. Explain the support closures structurally.

AC6 and the general no-three-in-line conjecture remain open.
