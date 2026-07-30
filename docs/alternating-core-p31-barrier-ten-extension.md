# Exact p=31 barrier-ten extension from six triples to three

## Status

This note keeps AC as the sole active research track and proves AC5nx--AC5oa. It extends the explicit `p=31`, `n=30` trajectory of AC5nt from six real collinear-triple occurrences to three by legal two-row switches.

All lower bounds below are complete sublevel-component exhaustions. All upper bounds are replayed physical paths. The note does not yet produce a zero-triple configuration on the `30 by 30` board.

## Setup

A state is an ordered pair `(R,B)` of disjoint permutation graphs on `[1,30]^2`. A legal move swaps the images of two rows in one layer and is retained only when the two inserted cells avoid the opposite layer. The potential is

\[
\Phi(R,B)=\sum_L\binom{|(R\cup B)\cap L|}{3}.
\]

For a state `v`, write

\[
\mathcal B(v)=
\min_{P:v\leadsto\{\Phi<\Phi(v)\}}
\max_{x\in P}\Phi(x).
\]

## AC5nx -- exact barrier ten from six triples to five -- PROVED

At the six-triple endpoint of AC5nt, the complete sublevel components have sizes

\[
\begin{array}{c|cccc}
\text{barrier}&6&7&8&9\\
\hline
\text{states}&1&9&33&860.
\end{array}
\]

None contains a state of potential below six.

The stored 26-switch path has potential word

\[
6,7,7,8,10,10,10,9,9,10,7,9,10,8,10,10,9,10,10,9,9,8,10,9,8,8,5.
\]

Therefore

\[
\boxed{\mathcal B(v_6)=10}.
\]

The exact barrier-ten search that produced the path processed `65,864` accepted states and discovered `75,944` sublevel states.

### Proof

The barrier-nine component exhaustion proves the lower bound. Direct replay proves every stored switch is legal, the maximum potential is ten and the endpoint has potential five. QED.

## AC5ny -- exact barrier ten from five triples to four -- PROVED

At the resulting five-triple state, the complete lower components are

\[
\begin{array}{c|cccc}
\text{barrier}&6&7&8&9\\
\hline
\text{states}&2&18&68&501.
\end{array}
\]

None contains a state of potential below five. A stored 32-switch path remains inside `Phi<=10` and ends at potential four. Hence

\[
\boxed{\mathcal B(v_5)=10}.
\]

The exact barrier-ten search processed `182,765` accepted states and discovered `223,691` sublevel states before returning the stored predecessor path.

### Proof

As in AC5nx, the complete barrier-nine component gives the lower bound and physical replay of the stored path gives the matching upper bound. QED.

## AC5nz -- exact barrier ten from four triples to three -- PROVED

At the four-triple checkpoint, the complete lower components have sizes

\[
\begin{array}{c|ccccc}
\text{barrier}&5&6&7&8&9\\
\hline
\text{states}&2&10&29&286&2033.
\end{array}
\]

None contains a state of potential below four.

The stored 42-switch path has maximum potential ten and terminal value three. Consequently

\[
\boxed{\mathcal B(v_4)=10}.
\]

The terminal red permutation is

\[
(12,15,24,9,27,20,4,17,28,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,25,16),
\]

and the terminal blue permutation is

\[
(17,10,21,22,7,15,8,28,25,13,9,4,20,26,30,12,27,24,29,23,14,1,2,11,18,6,3,16,5,19).
\]

### Proof

Breadth-first enumeration exhausts the displayed barrier-nine component. The 42 stored switches preserve two disjoint permutations, never exceed potential ten and end at the displayed three-triple state. QED.

## AC5oa -- explicit 254-switch trajectory from 75 triples to three -- PROVED

Concatenate:

1. the 154-switch AC5nt path from the strongest AN successor at potential 75 to six;
2. the 26-switch AC5nx path from six to five;
3. the 32-switch AC5ny path from five to four;
4. the 42-switch AC5nz path from four to three.

This gives a legal physical path of

\[
\boxed{154+26+32+42=254}
\]

two-row switches from potential 75 to potential three. The added 100-switch tail never exceeds ten; the complete trajectory never exceeds its initial potential 75.

The data are retained in `data/ac-p31-barrier-ten-extension.json`.

### Proof

Each segment starts at the exact endpoint of its predecessor. The deterministic verifier reconstructs every state and potential. Concatenation proves the claim. QED.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_barrier_ten_extension.cpp -o verify_p31_extension
```

Replay all three new segments:

```text
./verify_p31_extension
```

Recompute the exact lower components separately:

```text
./verify_p31_extension 6
./verify_p31_extension 5
./verify_p31_extension 4
```

Expected replay ledger:

- six-to-five moves: `26`;
- five-to-four moves: `32`;
- four-to-three moves: `42`;
- new tail moves: `100`;
- cumulative switches from the 75-triple installed state: `254`;
- final potential: `3`.

## Remaining frontier

The next exact physical task is the three-triple checkpoint. Its barrier-nine component is being enumerated fail-closed: until that traversal either exhausts or returns a lower state, no barrier-ten claim is made. After reaching two, continue through one and zero, then compare the resulting terminal path and low-potential cores with the completed `p=19` certificate.

AC6 and the general no-three-in-line conjecture remain open.
