# Exact p=31 barrier-ten extensions

## Status

This note keeps AC as the sole active research track and proves AC5nx--AC5od. It continues the explicit `p=31`, `n=30` trajectory of AC5nt--AC5nw from six real collinear triples to three.

Every operation is one legal two-row switch in one of the two disjoint permutation layers. This note does not yet reach a zero-triple configuration or prove AC6.

## AC5nx -- exact barrier ten from six triples to five -- PROVED

Let `v_6` be the six-triple state displayed in AC5nv. Its complete sublevel components at barriers 6 through 9 have sizes

\[
1,\ 9,\ 33,\ 860,
\]

and none contains a state of smaller potential.

The stored 26-switch path has exact potential word

\[
\begin{aligned}
&6,7,7,8,10,10,10,9,9,10,7,9,10,8,10,10,9,\\
&10,10,9,9,8,10,9,8,8,5.
\end{aligned}
\]

Consequently

\[
\boxed{\mathcal B(v_6)=10}.
\]

The exact barrier-ten search processed 65,864 accepted states and discovered 75,944 sublevel states before returning the stored path.

## AC5ny -- exact barrier ten from five triples to four -- PROVED

At the resulting five-triple state `v_5`, the complete sublevel components at barriers 6 through 9 have sizes

\[
2,\ 18,\ 68,\ 501,
\]

and none contains a state of potential below five.

A stored 32-switch path has potential word

\[
\begin{aligned}
&5,7,10,10,9,10,9,10,9,10,10,9,10,10,10,9,10,10,8,\\
&10,8,10,10,10,10,9,10,7,10,10,10,8,4.
\end{aligned}
\]

Therefore

\[
\boxed{\mathcal B(v_5)=10}.
\]

The exact barrier-ten search processed 182,765 accepted states and discovered 223,691 sublevel states before returning this path.

## AC5nz -- explicit 212-switch path from 75 triples to four -- PROVED

Concatenating AC5nt with AC5nx and AC5ny gives a physical path

\[
75\longrightarrow6\longrightarrow5\longrightarrow4
\]

using

\[
\boxed{154+26+32=212}
\]

legal two-row switches after the alternating-star installation. The extension from six to four never exceeds potential ten.

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

None contains a state of potential below four. Hence every route to three triples has maximum potential at least ten.

## AC5ob -- exact barrier ten from four triples to three -- PROVED

The stored 42-switch path from `v_4` has potential word

\[
\begin{aligned}
&4,8,9,7,9,9,9,10,8,10,9,9,10,9,10,10,9,10,9,10,9,10,\\
&9,9,10,9,10,7,9,9,4,9,10,7,6,6,6,9,8,8,8,6,3.
\end{aligned}
\]

It never exceeds ten and ends at potential three. Combined with AC5oa,

\[
\boxed{\mathcal B(v_4)=10}.
\]

The upper path was returned by a persistent goal-prioritised search restricted to the exact barrier-ten sublevel and is replayed independently by the deterministic verifier.

## AC5oc -- explicit 254-switch path from 75 triples to three -- PROVED

Concatenating the preceding segments gives

\[
75\longrightarrow6\longrightarrow5\longrightarrow4\longrightarrow3
\]

using

\[
\boxed{154+26+32+42=254}
\]

legal switches after the AN installation. Every state remains a pair of disjoint permutation graphs.

## AC5od -- exact three-triple lower frontier through barrier eight -- PROVED

The three-triple endpoint has red permutation

\[
(12,15,24,9,27,20,4,17,28,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,25,16)
\]

and blue permutation

\[
(17,10,21,22,7,15,8,28,25,13,9,4,20,26,30,12,27,24,29,23,14,1,2,11,18,6,3,16,5,19).
\]

Its three exact line occurrences are

\[
\{(14,13),(20,11),(23,10)\},
\]

\[
\{(16,18),(9,25),(29,5)\},
\]

and

\[
\{(14,26),(18,24),(20,23)\},
\]

with layer identities retained in the data file.

The complete sublevel-component sizes are

\[
\begin{array}{c|rrrrrr}
\text{barrier}&3&4&5&6&7&8\\
\hline
\text{states}&1&3&5&17&302&2196.
\end{array}
\]

None contains a state of potential below three. Therefore

\[
\boxed{\mathcal B(v_3)\ge9}.
\]

The barrier-nine component is a separate exact computation. Until it either returns a two-triple state or exhausts, no equality or stronger lower bound is claimed.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_barrier_ten_extension.cpp -o verify_p31_ext
```

Replay all three new segments:

```text
./verify_p31_ext
```

Recompute the exact lower components independently:

```text
./verify_p31_ext 6
./verify_p31_ext 5
./verify_p31_ext 4
./verify_p31_ext 3
```

Expected ledger:

- six-to-five switches: `26`;
- five-to-four switches: `32`;
- four-to-three switches: `42`;
- final potential: `3`;
- six-triple lower states total: `903`;
- five-triple lower states total: `589`;
- four-triple lower states total: `2360`;
- three-triple lower states total: `2524`.

## Remaining frontier

1. Finish the exact barrier-nine component above `v_3` or return a two-triple path.
2. Continue the same exact process through two, one and zero triples.
3. Classify the three-triple core by line, layer, carry, denominator and owner fields.
4. Extract a reusable repair template from the repeated barrier-ten behaviour.
5. Generalize beyond the selected `p=31` initial state.

AC6 and the general no-three-in-line conjecture remain open.
