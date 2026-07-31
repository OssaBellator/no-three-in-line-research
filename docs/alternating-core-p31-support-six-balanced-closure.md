# Balanced support-six closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5oq--AC5or for the explicit `p=31`, `n=30` three-triple state. It treats the first six-extra support family: exactly three additional red row addresses and three additional blue row addresses.

## AC5oq -- complete balanced six-extra census -- PROVED

Choose

\[
A_R\subseteq[30]\setminus R_0,\qquad |A_R|=3,
\]

and

\[
A_B\subseteq[30]\setminus B_0,\qquad |A_B|=3.
\]

There are

\[
\binom{26}{3}\binom{25}{3}=2600\cdot2300=
\boxed{5{,}980{,}000}
\]

such supports.

On each support, permute exactly the current retained red and blue values, fix every outside cell, reject red-blue collisions, and prune as soon as the exact partial potential exceeds two.

The complete search visits

\[
\boxed{577{,}440{,}893}
\]

admissible partial states and reaches no complete state of potential at most two.

### Proof

The support set is partitioned into twelve contiguous lexicographic shards. Every shard is independently exhaustive, and the committed partial-state counts sum to the displayed total. Every branch ends by collision, by exact potential greater than two, or as a complete assignment. The complete-assignment count is zero. QED.

## AC5or -- no balanced six-extra endpoint improvement -- PROVED

No endpoint supported on the nine core addresses plus exactly three extra red and three extra blue addresses has potential below three:

\[
\boxed{\Phi\ge3.}
\]

This does not yet close the five unbalanced six-extra distributions.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_six_balanced.cpp -o verify_support_six_balanced
```

Run one shard at a time:

```text
./verify_support_six_balanced 0
./verify_support_six_balanced 1
# ...
./verify_support_six_balanced 11
```

Every invocation checks its exact support interval, partial-state count, and zero complete endpoints. The twelve shard counts sum to:

- supports: `5980000`;
- partial states: `577440893`;
- potential-at-most-two endpoints: `0`.

## Remaining frontier

1. Close or solve the unbalanced six-extra distributions `(0,6)`, `(1,5)`, `(2,4)`, `(4,2)`, `(5,1)`, and `(6,0)`.
2. Finish the independent barrier-nine switch component from the same three-triple state.
3. Convert any wider-support endpoint into a legal switch ordering.
4. Seek a structural explanation for the balanced closure.

AC6 and the general no-three-in-line conjecture remain open.
