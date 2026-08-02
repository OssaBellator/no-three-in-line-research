# Explicit p=31 five-to-four barrier segment

## Status

This AC-only note proves AC5ob--AC5oc. It continues the recovered `p=31`, `n=30` trajectory from the five-triple endpoint of AC5ny to a concrete four-triple state.

## AC5ob -- exact minimax barrier ten from five triples -- PROVED

AC5nz exhausts the complete components of the five-triple state through barrier nine; the barrier-nine component has 6797 states and contains no state below potential five.

The physical path stored in `data/ac-p31-five-to-four.json` has 527 legal two-row switches, never exceeds potential ten, and reaches potential four. Hence

\[
\boxed{\mathcal B(v_5,\{\Phi<5\})=10.}
\]

### Proof

The lower bound is AC5nz. For the upper bound, replay every stored layer-and-row switch. Each insertion avoids the opposite layer, so both layers remain disjoint permutations. Exhaustive determinant counting agrees with every stored potential, whose maximum is ten and final value is four. QED.

## AC5oc -- explicit four-triple endpoint -- PROVED

The terminal red permutation is

\[
(14,15,23,18,4,25,7,17,29,13,9,2,20,28,1,12,19,24,26,5,3,30,27,11,22,6,21,16,8,10)
\]

and the terminal blue permutation is

\[
(5,10,24,9,8,15,28,20,25,1,6,4,23,29,30,18,7,19,2,11,26,13,21,3,14,27,12,22,17,16).
\]

They are disjoint permutation layers and their union has exactly four real collinear triple occurrences.

The 527-switch route was returned after 163321 expanded candidate states and 560184 discovered states. Those search counts are diagnostic only; the proof is the replayed path plus the independently exhausted lower component.

## Audit

Run:

```text
python scripts/verify_ac_p31_five_to_four.py
```

and separately verify the lower bound with:

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_five_triple_frontier.cpp -o verify_five
./verify_five 9
```

## Remaining frontier

1. Enumerate the physical four-triple core and its immediate repair atlas.
2. Exhaust the necessary lower sublevels from the four-triple endpoint.
3. Find and replay a path to three triples.
4. Continue through two, one and zero triples.
