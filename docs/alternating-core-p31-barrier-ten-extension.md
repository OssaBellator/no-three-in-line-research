# Exact p=31 barrier-ten extensions

## Status

This note keeps AC as the sole active research track and proves AC5nx--AC5oa. It continues the explicit `p=31`, `n=30` trajectory of AC5nt--AC5nw from six real collinear triples to four.

Every operation is one legal two-row switch in one of the two disjoint permutation layers. This note does not yet reach a zero-triple configuration or prove AC6.

## AC5nx -- exact barrier ten from six triples to five -- PROVED

Let `v_6` be the six-triple state displayed in AC5nv. Its complete sublevel components at barriers 6 through 9 have sizes

\[
1,\ 9,\ 33,\ 860,
\]

and none contains a state of smaller potential.

The following 26-switch path has exact potential word

\[
\begin{aligned}
&6,7,7,8,10,10,10,9,9,10,7,9,10,8,10,10,9,\
&10,10,9,9,8,10,9,8,8,5.
\end{aligned}
\]

Consequently

\[
\boxed{\mathcal B(v_6)=10}.
\]

The exact barrier-ten search processed 65,864 accepted states and discovered 75,944 sublevel states before returning the stored path.

### Proof

The exhaustive barrier-nine enumeration gives the lower bound. Direct replay verifies every switch, preserves two disjoint permutations, never exceeds potential ten and ends at potential five. QED.

## AC5ny -- exact barrier ten from five triples to four -- PROVED

At the resulting five-triple state `v_5`, the complete sublevel components at barriers 6 through 9 have sizes

\[
2,\ 18,\ 68,\ 501,
\]

and none contains a state of potential below five.

A stored 32-switch path has potential word

\[
\begin{aligned}
&5,7,10,10,9,10,9,10,9,10,10,9,10,10,10,9,10,10,8,\
&10,8,10,10,10,10,9,10,7,10,10,10,8,4.
\end{aligned}
\]

Therefore

\[
\boxed{\mathcal B(v_5)=10}.
\]

The exact barrier-ten search processed 182,765 accepted states and discovered 223,691 sublevel states before returning this path.

### Proof

The barrier-nine component exhaustion proves that every route to a lower state reaches potential at least ten. Replay of the stored path proves the matching upper bound and the four-triple endpoint. QED.

## AC5nz -- explicit 212-switch path from 75 triples to four -- PROVED

Concatenating AC5nt with AC5nx and AC5ny gives a physical path

\[
75\longrightarrow6\longrightarrow5\longrightarrow4
\]

using

\[
\boxed{154+26+32=212}
\]

legal two-row switches after the alternating-star installation.

The extension from six to four never exceeds potential ten. Every state remains a pair of disjoint permutation graphs on the `30 by 30` board.

### Proof

The terminal permutation tables of each segment agree with the initial tables of the next segment. Concatenation preserves every legality and potential assertion. QED.

## AC5oa -- exact four-triple lower frontier -- PROVED

The four-triple endpoint has red permutation

\[
(17,15,24,9,23,18,4,28,25,13,6,2,8,20,1,12,7,19,29,11,5,30,27,26,14,3,21,16,22,10)
\]

and blue permutation

\[
(12,25,23,18,7,15,8,2,28,1,9,4,20,29,30,16,27,24,26,5,14,21,6,11,22,10,3,13,17,19).
\]

Its complete sublevel-component sizes are

\[
\begin{array}{c|ccccc}
\text{barrier}&5&6&7&8&9\\
\hline
\text{states}&2&10&29&286&2033.
\end{array}
\]

None contains a state of potential below four. Hence

\[
\boxed{\mathcal B(v_4)\ge10}.
\]

The barrier-ten component is being enumerated separately. Until that finite search either returns a lower state or exhausts, no claim is made about equality or a larger lower bound.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_barrier_ten_extension.cpp -o verify_p31_ext
```

Replay both paths:

```text
./verify_p31_ext
```

Recompute the exact lower components independently:

```text
./verify_p31_ext 6
./verify_p31_ext 5
./verify_p31_ext 4
```

Expected ledger:

- six-to-five switches: `26`;
- five-to-four switches: `32`;
- final potential: `4`;
- six-triple lower states total: `903`;
- five-triple lower states total: `589`;
- four-triple lower states total: `2360`.

The large barrier-ten search counts are retained as provenance for the returned predecessor paths; exactness of each barrier conclusion uses only the stored path and exhaustive lower-barrier component.

## Remaining frontier

1. Finish the exact barrier-ten component above `v_4` or return a three-triple path.
2. Continue the same exact process through three, two, one and zero triples.
3. Classify the low-potential cores by line, layer, carry, denominator and owner fields.
4. Extract a reusable repair template from the common barrier-ten behaviour at six and five triples.
5. Generalize beyond the selected `p=31` initial state.

AC6 and the general no-three-in-line conjecture remain open.
