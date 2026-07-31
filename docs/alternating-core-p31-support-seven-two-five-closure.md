# Exact `(2,5)` support-seven closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5pb--AC5pc for the explicit `p=31`, `n=30` three-triple endpoint. It closes the mixed seven-extra family with exactly two additional red row addresses and five additional blue row addresses.

## AC5pb -- complete `(2,5)` seven-extra census -- PROVED

The support universe has

\[
\binom{26}{2}\binom{25}{5}=\boxed{17{,}267{,}250}
\]

members. For every support, fix all outside cells, permute exactly the retained current values on the enlarged supports, reject red-blue collisions, and prune every branch whose exact partial potential exceeds two.

The complete exact census examines

\[
\boxed{3{,}283{,}839{,}275}
\]

admissible partial states and finds no complete collision-free endpoint of potential at most two.

### Proof

The support universe is partitioned into 52 contiguous lexicographic intervals. Their exact support and node counts are retained in `data/ac-p31-support-seven-two-five-closure.json`. The intervals cover `[0,17267250)` without overlap or omission. Every branch terminates at a collision, at exact partial potential above two, or as a complete assignment. The complete-assignment count is zero. QED.

## AC5pc -- five of eight support-seven distributions closed -- PROVED

No endpoint in the `(2,5)` family lowers the current three-triple state:

\[
\boxed{\Phi\ge3.}
\]

The closed seven-extra distributions are now

\[
(0,7),\ (1,6),\ (2,5),\ (6,1),\ (7,0).
\]

Only `(3,4)`, `(4,3)`, and `(5,2)` remain.

## Deterministic audit

Compile the inherited generic range verifier:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_seven_range.cpp -o verify_support_seven_range
```

For each ledger triple `(lo,hi,nodes)`, run

```text
./verify_support_seven_range 2 lo hi nodes
```

The interval totals are:

- support choices: `17267250`;
- partial states: `3283839275`;
- complete potential-at-most-two endpoints: `0`.

## Remaining frontier

1. Close or solve `(3,4)`, `(4,3)`, and `(5,2)`.
2. Finish the independent barrier-nine switch component.
3. Convert any wider-support endpoint into a legal low-barrier switch ordering.
4. Explain the support closures structurally.

AC6 and the general no-three-in-line conjecture remain open.
