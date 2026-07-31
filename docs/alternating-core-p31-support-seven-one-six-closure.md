# Exact `(1,6)` support-seven closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5ox--AC5oy for the explicit `p=31`, `n=30` three-triple endpoint. It closes the mixed seven-extra family with exactly one additional red row address and six additional blue row addresses.

## AC5ox -- complete `(1,6)` seven-extra census -- PROVED

Choose one red address outside the four-address red core and six blue addresses outside the five-address blue core. There are

\[
26\binom{25}{6}=\boxed{4{,}604{,}600}
\]

supports.

For each support, fix every outside cell, permute exactly the current retained values on the enlarged red and blue supports, reject red-blue cell collisions, and prune a branch as soon as its exact partial potential exceeds two.

The complete search examines

\[
\boxed{1{,}163{,}897{,}840}
\]

admissible partial states and reaches no complete collision-free endpoint of potential at most two.

### Proof

The support universe is partitioned into 87 contiguous lexicographic intervals. Each interval is exhaustively searched and retains its exact partial-state count in `data/ac-p31-support-seven-one-six-closure.json`. The intervals cover `[0,4604600)` without overlap or omission. Every branch terminates at a collision, at exact partial potential greater than two, or at a complete assignment; the complete-assignment count is zero. QED.

## AC5oy -- no `(1,6)` endpoint improvement -- PROVED

No endpoint obtained from the nine core layer-row addresses plus exactly one additional red and six additional blue addresses lowers the current three-triple potential:

\[
\boxed{\Phi\ge3.}
\]

Combined with AC5ov--AC5ow, the closed seven-extra distributions are now `(0,7)`, `(1,6)`, and `(7,0)`. The five remaining mixed distributions stay open.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_seven_one_six.cpp -o verify_support_seven_one_six
```

For each ledger row `(lo,hi,nodes)`, run

```text
./verify_support_seven_one_six lo hi nodes
```

The verifier asserts the interval size, exact partial-state count, and zero potential-at-most-two endpoints. The 87 ledger rows sum to:

- support choices: `4604600`;
- partial states: `1163897840`;
- complete lower endpoints: `0`.

## Remaining frontier

1. Close or solve the mixed seven-extra families `(2,5)`, `(3,4)`, `(4,3)`, `(5,2)`, and `(6,1)`.
2. Finish the independent barrier-nine switch component from the same three-triple state.
3. Convert any wider-support endpoint into a legal low-barrier switch ordering.
4. Explain structurally why the closed support families cannot lower the core.

AC6 and the general no-three-in-line conjecture remain open.
