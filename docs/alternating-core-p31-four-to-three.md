# Exact p=31 four-to-three extension

## Status

This note keeps AC as the sole active research track and proves AC5ob--AC5od. It continues AC5oa from the explicit four-triple state to an explicit three-triple state.

## AC5ob -- exact barrier ten from four triples to three -- PROVED

The four-triple state of AC5oa has complete lower sublevel components of sizes

\[
2,\ 10,\ 29,\ 286,\ 2033
\]

at barriers 5 through 9, and none contains a state of potential below four.

There is a legal 42-switch path with exact potential word

\[
\begin{aligned}
&4,8,9,7,9,9,9,10,8,10,9,9,10,9,10,10,9,10,9,10,9,\
&10,9,9,10,9,10,7,9,9,4,9,10,7,6,6,6,9,8,8,8,6,3.
\end{aligned}
\]

Therefore

\[
\boxed{\mathcal B(v_4)=10}.
\]

### Proof

The exhaustive barrier-nine component proves the lower bound. Direct replay verifies every switch, keeps both layers disjoint permutations, never exceeds potential ten and ends at potential three. QED.

## AC5oc -- explicit 254-switch path from 75 triples to three -- PROVED

Concatenating AC5nt, AC5nx, AC5ny and AC5ob gives

\[
75\longrightarrow6\longrightarrow5\longrightarrow4\longrightarrow3
\]

using

\[
\boxed{154+26+32+42=254}
\]

legal two-row switches after the alternating-star installation.

The complete tail from six to three remains inside potential ten.

## AC5od -- exact three-triple lower frontier -- PROVED

The three-triple endpoint has red permutation

\[
(12,15,24,9,27,20,4,17,28,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,25,16)
\]

and blue permutation

\[
(17,10,21,22,7,15,8,28,25,13,9,4,20,26,30,12,27,24,29,23,14,1,2,11,18,6,3,16,5,19).
\]

Its remaining triples are

\[
\begin{aligned}
&\{(14,13),(20,11),(23,10)\},\\
&\{(16,18),(9,25),(29,5)\},\\
&\{(14,26),(18,24),(20,23)\}.
\end{aligned}
\]

The first is red, the third is blue, and the middle triple is mixed.

Its complete sublevel-component sizes are

\[
\begin{array}{c|rrrrrr}
\text{barrier}&3&4&5&6&7&8\\
\hline
\text{states}&1&3&5&17&302&2196.
\end{array}
\]

None contains a state below potential three. Hence

\[
\boxed{\mathcal B(v_3)\ge9}.
\]

The barrier-nine component is being enumerated separately. No equality or stronger lower bound is claimed until that search returns a lower state or exhausts.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_four_to_three.cpp -o verify_p31_43
```

Replay:

```text
./verify_p31_43
```

Recompute each lower component:

```text
./verify_p31_43 3
./verify_p31_43 4
./verify_p31_43 5
./verify_p31_43 6
./verify_p31_43 7
./verify_p31_43 8
```

Expected component sizes are `1,3,5,17,302,2196`.

## Remaining frontier

1. Complete the barrier-nine search from the three-triple endpoint.
2. Continue to two, one and zero triples.
3. Classify the three remaining lines by carry, denominator, channel and owner data.
4. Extract a reusable low-potential minimax template from the repeated barriers.
5. Extend beyond this explicit `p=31` trajectory.

AC6 and the general no-three-in-line conjecture remain open.
