# Exact p=31 three-triple lower components

## Status

This note keeps AC as the sole active research track and proves AC5og--AC5oh. It starts from the three-triple endpoint of AC5oe and exhausts the first six legal switch sublevels.

It does not yet determine whether a two-triple state exists at barrier nine or above.

## AC5og -- complete components through barrier eight -- PROVED

Let `v_3` be the endpoint of AC5oe. The complete legal switch components containing `v_3` have sizes

\[
\begin{array}{c|rrrrrr}
\text{barrier}&3&4&5&6&7&8\\
\hline
\text{states}&1&2&5&16&80&1159.
\end{array}
\]

None contains a state of potential below three.

### Proof

For each displayed barrier, breadth-first search enumerates every legal two-permutation state reachable from `v_3` without exceeding the barrier. Exact determinant evaluation confirms that all enumerated states have potential at least three. The stored state counts are reproduced by `scripts/verify_ac_p31_three_triple_lower_components.cpp`. QED.

## AC5oh -- certified next barrier lower bound -- PROVED

Every path from `v_3` to a state of potential at most two must visit a state of potential at least nine. Equivalently,

\[
\boxed{\mathcal B(v_3,\{\Phi<3\})\ge9.}
\]

### Proof

The complete barrier-eight component contains no lower state by AC5og. QED.

## Deterministic audit

Compile and run:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_three_triple_lower_components.cpp -o verify_p31_3lower
./verify_p31_3lower
```

Expected ledger:

- component sizes: `1,2,5,16,80,1159`;
- certified barrier lower bound: `9`.

## Remaining frontier

1. Enumerate the complete barrier-nine component with durable checkpoint serialization.
2. If it contains a two-triple state, lift and replay the physical path.
3. If it exhausts without a lower state, commit its exact size and raise the lower bound to ten.
4. Continue through two, one and zero triples.

AC6 and the general no-three-in-line conjecture remain open.
