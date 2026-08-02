# Recovered explicit p=31 six-to-five barrier segment

## Status

This AC-only note proves AC5nx--AC5ny for the explicit `p=31`, `n=30` trajectory of AC5nt--AC5nw. It reconstructs a repository-backed route from the committed six-triple frontier to a five-triple state.

## AC5nx -- exact barrier ten from six triples -- PROVED

Let `v_6` be the committed six-triple state. Its complete legal switch component inside `Phi<=9` has exactly

\[
\boxed{860}
\]

states and contains no state of potential below six.

The 69-switch physical route stored in `data/ac-p31-recovered-tail.json` starts at `v_6`, preserves two disjoint permutation layers, never exceeds potential ten, and ends at potential five. Therefore

\[
\boxed{\mathcal B(v_6,\{\Phi<6\})=10.}
\]

### Proof

The lower bound is complete breadth-first enumeration of the barrier-nine component. The upper bound is direct replay of the stored layer-and-row switch words. Exact determinant counting agrees with every stored potential and gives final value five. QED.

## AC5ny -- durable recovered endpoint -- PROVED

The recovered five-triple endpoint has red permutation

\[
(17,25,23,18,29,15,8,28,21,13,9,4,20,27,1,12,7,19,3,5,26,30,2,11,14,6,24,16,22,10)
\]

and blue permutation

\[
(12,10,20,9,7,25,4,2,15,1,3,26,8,23,30,16,27,24,29,11,14,18,6,5,22,28,21,13,17,19).
\]

Both are permutations of `1,...,30`, their cells are disjoint, and their union has exactly five real collinear triple occurrences.

This endpoint is the next repository-backed search state. No claim about its minimum escape barrier is made in this note.

## Deterministic audit

Compile and run:

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_recovered_tail.cpp -o verify_tail
./verify_tail
```

Expected ledger:

- stored switches: `69`;
- maximum stored potential: `10`;
- exact barrier-nine component: `860` states;
- lower states in that component: `0`;
- final potential: `5`.

## Remaining frontier

1. Find a verified five-to-four route and prove its lower barrier by complete component exhaustion.
2. Continue through four, three, two, one and zero triples.
3. Compare recovered low-potential cores with the explicit `p=19` barriers.
4. Extract a uniform physical repair template rather than relying on unrestricted search.

AC6 and the general no-three-in-line conjecture remain open.
