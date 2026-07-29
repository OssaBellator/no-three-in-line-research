# Explicit physical alternating-star seed on the 18 by 18 board

## Status

This note keeps AC as the sole active research focus and proves AC5mp--AC5mu. It instantiates the prime-minus-one schema and AN-bank compiler with one fully explicit board state at `p=19`, `n=18`. All layer points, switch cells, secant pairs, forbidden positions, legal replacement matchings, real-line certificate counts and potential values are enumerated exactly.

This is a concrete initial-state certificate, not a proof for every AC initial state. It proves that one physical member of the manifested AN class has an explicit improving alternating installation. The general AC6 and no-three-in-line conjectures remain open.

## Two modular-hyperbola layers

For `c in F_19^*`, put

\[
H_c=\{(x,y)\in[1,18]^2:xy\equiv c\pmod{19}\}.
\]

Take the two current permutation layers

\[
R=H_7,
\qquad
B=H_1.
\]

They are disjoint because one point cannot have product congruent to both `7` and `1` modulo `19`.

In `B`, the rows `6` and `16` contain

\[
(6,16),
\qquad
(16,6).
\]

Switch these two images, removing those cells and inserting

\[
z=(6,6),
\qquad
w=(16,16).
\]

The switched blue layer remains a permutation. Moreover

\[
6\cdot6\equiv17\not\equiv7,
\qquad
16\cdot16\equiv9\not\equiv7
\pmod{19},
\]

so the switched layer remains disjoint from `H_7`.

## AC5mp -- explicit legal rectangle switch -- PROVED

The state

\[
S=H_7\cup H_1
\]

is a two-layer permutation configuration on `[1,18]^2`. Replacing `(6,16),(16,6)` in `H_1` by `(6,6),(16,16)` gives another permutation layer disjoint from `H_7`.

The inserted point `z=(6,6)` is therefore a physically legal AN candidate.

### Proof

The inverse of `6` modulo `19` is `16`, and conversely, giving the two removed `H_1` cells. A two-row image swap preserves bijectivity. The displayed modular products exclude both inserted cells from `H_7`. QED.

## Seven explicit secant pairs

The following fourteen points lie on `H_7` and split into seven endpoint-disjoint pairs whose real supporting lines contain `z`:

\[
\begin{array}{c|c}
Q_j&P_j\\\hline
(1,7)&(16,4)\\
(3,15)&(5,9)\\
(4,16)&(7,1)\\
(8,8)&(11,11)\\
(9,5)&(15,3)\\
(10,14)&(12,18)\\
(14,10)&(18,12)
\end{array}
\]

Choose the `Q_j` as the movable endpoints. Their columns and rows are

\[
C=(1,3,4,8,9,10,14),
\]

\[
R=(7,15,16,8,5,14,10).
\]

All selected endpoints belong to the same permutation layer `H_7` and the same hyperbola channel `7`.

## AC5mq -- explicit endpoint-disjoint same-channel star -- PROVED

Every listed endpoint lies on `H_7`; the fourteen endpoints are distinct; the selected `Q_j` have distinct rows and columns; and

\[
z,Q_j,P_j
\]

are collinear for every `j=1,...,7`.

Hence these pairs form a valid `t=7` physical AN star.

### Proof

Direct modular multiplication verifies membership in `H_7`. Direct determinant evaluation verifies each real collinearity relation. Distinct coordinates are visible in the table, and a permutation layer has distinct rows and columns. QED.

## Exact forbidden-position bank

Index the selected columns and rows in the displayed orders. The original-position forbidden cells are `(i,i)`. The switched blue layer contributes two additional selected-block collisions. The complete forbidden set is

\[
\begin{aligned}
F=\{&(0,0),(1,1),(2,2),(2,4),(3,3),\\
    &(4,4),(5,5),(6,1),(6,6)\}.
\end{aligned}
\]

Every source row and target column has forbidden degree at most two.

## AC5mr -- exact legal matching bank -- PROVED

The set

\[
\Omega(F)=\{\pi\in S_7:(i,\pi(i))\notin F\text{ for all }i\}
\]

has exactly

\[
\boxed{|\Omega(F)|=1300}
\]

states.

Every state preserves the selected rows and columns, avoids the switched blue layer, moves every selected `Q_j`, and destroys all seven original star triples.

The count satisfies the general AN1 lower bound

\[
1300>7!/128.
\]

### Proof

Exhaustive enumeration of all `7!=5040` permutations gives exactly 1300 avoiding `F`. The forbidden diagonal moves every selected endpoint and the two additional forbidden positions are precisely the switched-blue collisions. QED.

## Exact physical collateral census

Let

\[
X=S\setminus(A\cup\{(6,16),(16,6)\}),
\]

where `A={Q_1,...,Q_7}`, and put

\[
Z=X\cup\{(6,6),(16,16)\}.
\]

Enumerating all real collinear triples with exactly `r` compatible nonforbidden anchor-block cells gives

\[
\boxed{T_1=149,
\qquad T_2=138,
\qquad T_3=33.}
\]

The exact triple potentials are

\[
\boxed{
\Phi(S)=66,
\qquad
\Phi(X)=15,
\qquad
\Phi(Z)=29.
}
\]

Thus

\[
D_\star=51,
\qquad
F_\star=14.
\]

## AC5ms -- exact certificate and potential audit -- PROVED

The displayed values are the complete occurrence-faithful rank-one through rank-three certificate census and exact real-line triple potentials for this seed.

The average anchor-created collateral over the 1300 legal matching states is

\[
\frac{1}{1300}
\sum_{\pi\in\Omega(F)}
\bigl(\Phi(S_\pi)-\Phi(Z)\bigr)
=
30.9538461538\ldots.
\]

The general AN4 upper bound is valid but loose on this small instance; the improvement below is certified by complete finite enumeration rather than by the strict AN4 sufficient inequality.

### Proof

Enumerate all physical anchor-block cells outside `F`, all triples containing one to three mutually compatible anchor cells and the required number of `Z` cells, and test the real collinearity determinant. Separately enumerate all triples in `S,X,Z`. QED.

## Canonical improving installation

In lexicographic order on `S_7`, the minimum-potential legal matching is

\[
\boxed{
\pi_*=(3,6,1,5,2,4,0).
}
\]

Its replacement cells are

\[
\boxed{
\{(1,8),(3,10),(4,15),(8,14),(9,16),(10,5),(14,7)\}.
}
\]

The resulting physical state has

\[
\boxed{\Phi(S_{\pi_*})=41.}
\]

Therefore

\[
\boxed{
\Phi(S_{\pi_*})-\Phi(S)=-25.
}
\]

Exactly 1025 of the 1300 legal matching states have potential strictly below 66.

## AC5mt -- explicit improving operation -- PROVED

The operation address consisting of the `p=19` seed, switched blue rectangle and matching `pi_*` is a complete physical `install` operation. It destroys the seven designated star triples, preserves both permutation layers and strictly lowers the total real triple potential by 25.

Consequently this explicit initial state terminates at the first manifest decision through a genuine supply/improvement edge; it does not enter the AC1 no-improvement frontier.

### Proof

The bank legality is AC5mr. Exhaustive triple enumeration gives the source and successor potentials 66 and 41. The successor is therefore a valid strict-improvement operation. QED.

## AC5mu -- completed explicit initial-state manifest prefix -- PROVED

For the concrete data file `data/ac-explicit-p19-an-seed.json`:

1. the prime-minus-one `schema` section is complete;
2. the two permutation layers and legal switch are complete physical records;
3. the AN `install` operation dictionary contains all 1300 legal states;
4. the exact pair/state/certificate census is complete;
5. the canonical scheduler selects `pi_*`;
6. the selected edge is stratified as strict supply because the triple deficit decreases by 25;
7. no exceptional source, ticket, repair or reset occurrence is used.

Thus one fully explicit AC initial state has a complete terminating manifest prefix ending in an improved state.

This theorem does not assert that the improved state is no-three-in-line or that every required initial state reduces to this seed.

### Proof

AC5mp--AC5mt verify every listed schema, serializer, frontier and stratification record. The edge uses no exceptional debit. QED.

## Deterministic audit

`scripts/verify_ac_explicit_p19_an_seed.py` reconstructs the two modular-hyperbola layers from first principles, verifies the switch and all seven secants, enumerates the 1300-state bank, computes `T_1,T_2,T_3`, evaluates every successor potential and checks the canonical improving operation and committed JSON record.

## Main AC frontier

Only AC remains active. The explicit seed completes one physical initial-state case. The remaining tasks are:

1. manifest the improved successor and determine its next canonical AC state class;
2. search for additional explicit seed classes, especially nonimproving banks that exercise AC1;
3. prove a coverage rule reducing every AC6 initial state to manifested classes;
4. continue the physical rank, repair and exception ledgers for nonterminal successors.

AC6 and the global no-three-in-line conjecture remain open.
