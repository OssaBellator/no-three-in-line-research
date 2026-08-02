# Exact p=31 five-to-four tail segment

## Status

This note keeps AC as the sole active research track and proves AC5oa--AC5oc. It continues the explicit `p=31`, `n=30` trajectory from the five-triple endpoint of AC5ny to a four-triple state.

It does not yet produce a zero-triple configuration or a uniform prime-minus-one theorem.

## AC5oa -- exact barrier ten from five triples -- PROVED

Let `v_5` be the endpoint of AC5ny. Complete legal switch components at barriers `5,6,7,8,9` have sizes

\[
1,2,18,68,501,
\]

and none contains a state of potential below five.

The 32-switch path stored in `data/ac-p31-tail-five-to-four.json` has maximum potential ten and reaches potential four. Therefore

\[
\boxed{\mathcal B(v_5,\{\Phi<5\})=10.}
\]

### Proof

The exact component enumerations give the lower bound. Replay of the stored legal switch word gives a matching upper path whose maximum potential is ten. QED.

## AC5ob -- explicit 32-switch physical repair -- PROVED

The stored potential sequence is

\[
\begin{aligned}
&5,7,10,10,9,10,9,10,9,10,10,9,10,10,10,9,10,10,8,\\
&10,8,10,10,10,10,9,10,7,10,10,10,8,4.
\end{aligned}
\]

Every switch preserves two disjoint permutation layers. The endpoint has red permutation

\[
(17,15,24,9,23,18,4,28,25,13,6,2,8,20,1,12,7,19,29,11,5,30,27,26,14,3,21,16,22,10)
\]

and blue permutation

\[
(12,25,23,18,7,15,8,2,28,1,9,4,20,29,30,16,27,24,26,5,14,21,6,11,22,10,3,13,17,19).
\]

Its exact potential is four.

### Proof

The verifier checks legality and cross-layer disjointness before every move, then recomputes the determinant potential of all 60 selected cells. The stored sequence and endpoint tables agree exactly. QED.

## AC5oc -- durable manifest extension through four triples -- PROVED

The repository-backed explicit trajectory now contains

\[
75\longrightarrow6\longrightarrow5\longrightarrow4
\]

using

\[
154+26+32=212
\]

legal two-row switches after the alternating-star installation.

The two tail barriers are both exact:

\[
\mathcal B(v_6)=\mathcal B(v_5)=10.
\]

## Deterministic audit

Compile and run:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_tail_five_to_four.cpp -o verify_p31_54
./verify_p31_54
```

The verifier reuses the original exact switch-graph implementation, independently recomputes all five lower components, and replays all 32 switches.

Expected ledger:

- lower-component sizes: `1,2,18,68,501`;
- switches: `32`;
- maximum potential: `10`;
- terminal potential: `4`;
- deterministic recovery processed/discovered counts: `182,766 / 223,692`.

## Remaining frontier

1. Regenerate and commit the exact four-to-three barrier-ten path.
2. Add a combined replay audit for the durable trajectory from 75 through three.
3. Resume the three-triple exact quotient search toward two.
4. Continue through one and zero triples.
5. Extract reusable minimax repair templates from the `p=19` and `p=31` tails.

AC6 and the general no-three-in-line conjecture remain open.
