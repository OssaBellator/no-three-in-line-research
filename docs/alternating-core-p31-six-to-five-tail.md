# Exact p=31 six-to-five tail segment

## Status

This note keeps AC as the sole active research track and proves AC5nx--AC5nz. It continues the explicit `p=31`, `n=30` trajectory of AC5nt from the committed six-triple state to a five-triple state.

It does not yet produce a zero-triple configuration or a uniform prime-minus-one theorem.

## AC5nx -- exact barrier ten from six triples -- PROVED

Let `v_6` be the terminal state of AC5nt. AC5nv exhausts its complete legal switch components at barriers `6,7,8,9`; their sizes are

\[
1,9,33,860,
\]

and none contains a state of potential below six.

The path recorded in `data/ac-p31-tail-six-to-five.json` has potential sequence

\[
6,7,7,8,10,10,10,9,9,10,7,9,10,8,10,10,9,10,10,9,9,8,10,9,8,8,5.
\]

Consequently

\[
\boxed{\mathcal B(v_6,\{\Phi<6\})=10.}
\]

### Proof

The exhausted barrier-nine component gives the lower bound. Direct replay of the stored legal switches gives a path to potential five whose maximum is ten, proving the matching upper bound. QED.

## AC5ny -- explicit 26-switch physical repair -- PROVED

The exact switch word is

\[
\begin{aligned}
&r:(1,6), r:(6,18), b:(8,11), b:(6,8), b:(6,18), r:(2,6),\\
&b:(18,27), b:(7,23), b:(2,26), b:(2,8), r:(2,13), r:(1,4),\\
&b:(13,27), r:(3,7), b:(7,27), b:(23,27), r:(1,4), r:(3,13),\\
&b:(3,27), r:(7,12), b:(12,23), r:(8,12), r:(8,26), r:(21,26),\\
&b:(19,24), b:(20,27).
\end{aligned}
\]

Every move preserves two disjoint permutation layers. The endpoint has red permutation

\[
(17,20,24,18,23,15,4,6,25,13,9,2,8,28,1,12,7,19,29,5,26,30,27,11,14,3,21,16,22,10)
\]

and blue permutation

\[
(12,15,26,9,7,25,8,28,21,1,6,4,20,29,30,16,27,24,5,23,14,18,2,3,22,10).
\]

Its exact potential is five.

### Proof

At each switch the two inserted cells avoid the opposite layer. Both row-image lists remain permutations. Exhaustive determinant counting on all 60 selected cells gives the stored potential sequence and terminal value five. QED.

## AC5nz -- durable manifest extension -- PROVED

The explicit `p=31` manifest now contains a repository-backed trajectory

\[
75\longrightarrow6\longrightarrow5
\]

using `154+26=180` legal two-row switches after the alternating-star installation.

The six-to-five segment is independent of heuristic search results: its lower bound comes from complete sublevel exhaustion and its upper bound from a fully addressed replayable path.

## Deterministic audit

Run:

```text
python scripts/verify_ac_p31_tail_six_to_five.py
```

For the exact lower-component recomputation, compile the existing frontier verifier and run its six-triple checkpoint mode:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_switch_frontier.cpp -o verify_p31
./verify_p31 6
```

Expected replay ledger:

- switches: `26`;
- maximum potential: `10`;
- terminal potential: `5`;
- complete barrier-nine component: `860` states.

## Remaining frontier

1. Regenerate and commit the five-to-four barrier-ten path.
2. Regenerate and commit the four-to-three barrier-ten path.
3. Resume the exact three-triple sublevel search with durable quotient checkpoints.
4. Continue through two, one and zero triples.
5. Extract reusable repair templates from the `p=19` and `p=31` tails.

AC6 and the general no-three-in-line conjecture remain open.
