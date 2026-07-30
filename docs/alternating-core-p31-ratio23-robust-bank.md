# Robust p=31 ratio-23 alternating-star obstruction

## Status

This note keeps AC as the only active research track and proves AC5nv--AC5nz. It removes the selector dependence from the uniformly nonimproving ratio-23 class found by AC5nr.

The result is an explicit physical AC1 obstruction for one modular-hyperbola seed. It is not a counterexample to the no-three-in-line conjecture: other repair families may still improve the state.

## Physical seed

Use `p=31`, `n=30`, anchor layer `H_1` and switch layer `H_23`. Switch

\[
(15,16),(16,15)\longrightarrow(15,15),(16,16).
\]

For candidate `z=(15,15)`, the anchor hyperbola has eight endpoint-disjoint real secant pairs:

\[
\begin{aligned}
&(1,1)-(30,30),\quad (3,21)-(11,17),\quad (5,25)-(25,5),\\
&(7,9)-(19,18),\quad (9,7)-(18,19),\\
&(12,13)-(27,23),\quad (13,12)-(23,27),\\
&(17,11)-(21,3).
\end{aligned}
\]

The current two-layer state has

\[
\Phi(S)=82.
\]

## AC5nv -- complete seven-pair orientation bank -- PROVED

A complete seven-pair orientation address consists of:

1. one omitted pair among the eight secants;
2. one selected endpoint from each retained pair;
3. distinct selected rows and columns;
4. one permutation avoiding the old diagonal and opposite-layer collision positions.

Every state retains all unchanged points of both hyperbola layers, the two inserted switch cells and the seven replacement cells. Thus every state contains exactly 60 points.

The eight omitted-pair classes contain respectively

\[
166944,183448,168582,176536,176536,160560,160560,183448
\]

occurrence-addressed states, for total

\[
\boxed{1{,}376{,}614}.
\]

### Proof

Exhaust the eight omissions and all `2^7` endpoint words. Reject endpoint words which repeat a row or column. For every surviving word enumerate all allowed matching permutations. The complete physical occurrence address distinguishes equal cell sets arising from different omissions or endpoint choices. QED.

## AC5nw -- robust nonimprovement -- PROVED

The exact minimum potentials in the eight omitted-pair classes are

\[
\boxed{90,89,89,87,87,91,91,89.}
\]

Consequently

\[
\boxed{
\min\Phi(S_\pi)=87>82=\Phi(S),
}
\]

and none of the `1,376,614` complete orientation-bank states improves the current configuration.

The unique lexicographically first global minimum omits pair

\[
(7,9)-(19,18),
\]

selects endpoints

\[
(30,30),(11,17),(5,25),(18,19),(12,13),(23,27),(17,11),
\]

and uses replacement cells

\[
(5,11),(11,30),(12,17),(17,25),(18,27),(23,19),(30,13).
\]

### Proof

For each endpoint word, write the exact potential as the fixed-state potential plus unary, pair and triple costs of the seven matching cells. This identity includes every unchanged cell of both hyperbola layers. Exhausting all allowed permutations gives the displayed counts and minima. The minimum record is independently checked by direct enumeration of all real triples in its 60-point state. QED.

## AC5nx -- two-candidate conjugacy -- PROVED

The half-turn

\[
\iota(x,y)=(31-x,31-y)
\]

preserves both `H_1` and `H_23`, preserves the removed and inserted switch-cell sets, and exchanges candidates `(15,15)` and `(16,16)`.

It bijects their complete eight-pair orientation banks and preserves real collinearity. Therefore the conjugate candidate has the same state count, class minima and robust nonimprovement result.

## AC5ny -- exact AC1 record at the best bank state -- PROVED

For the global-minimum endpoint orientation, let `X` remove the seven selected endpoints and the two switch cells, and let `Z` add the two inserted cells. Then

\[
\Phi(X)=51,\qquad \Phi(Z)=73,
\]

so

\[
D_\star=31,\qquad F_\star=22,\qquad G=9.
\]

The occurrence-faithful certificate counts are

\[
\boxed{T_1=208,\qquad T_2=122,\qquad T_3=13.}
\]

Rank one is the unique heaviest normalized rank. Its canonical heavy anchor address `(2,3)` is the physical replacement cell

\[
\boxed{(5,19)},
\]

which lies in 14 rank-one certificate occurrences.

Thus the selector-complete obstruction still returns a concrete AC1 one-anchor concentration.

## AC5nz -- rich-line decomposition and filter persistence -- PROVED

The 14 certificates through `(5,19)` split into four exact fixed-line classes:

\[
6+6+1+1.
\]

The two six-certificate classes arise from four fixed points on directions `(1,-1)` and `(1,1)`; the remaining directions `(1,-10)` and `(1,-5)` each contain two fixed points.

Filter the best orientation bank by forbidding every anchor position lying on a line through at least `h` fixed points. For `h=3,4,5`, the exact results are

\[
\begin{array}{c|c|c|c}
h&\text{forbidden positions}&\text{remaining bank states}&\text{minimum potential}\\\hline
3&13&42&87\\
4&8&167&87\\
5&1&1044&87.
\end{array}
\]

Hence deleting all visible rich-line anchor positions does not restore an improving state. The residual obstruction is not explained solely by the two four-point lines through the heavy anchor.

## Deterministic audit

Run:

```text
python scripts/verify_ac_p31_ratio23_robust_bank.py
```

Expected ledger:

- complete secant pairs: `8`;
- pair-selection/orientation classes: `8 x 128`;
- occurrence-addressed states: `1,376,614`;
- omitted-pair minima: `90,89,89,87,87,91,91,89`;
- current/global minimum: `82/87`;
- improving states: `0`;
- best-record AC1 counts: `208,122,13`;
- heavy anchor: `(5,19)`, degree `14`;
- heavy-line split: `6,6,1,1`;
- high-line-filter minima: `87,87,87`;
- half-turn candidate conjugacy: verified.

## Remaining frontier

1. Classify the 14 heavy-anchor certificate occurrences by quotient, carry, denominator and current-payment labels.
2. Identify a conflict-safe paid substar or prove that its full incompatibility neighbourhood is overloaded.
3. Test larger matching blocks, all eight-pair repairs and non-AN repair families on the same state.
4. Determine whether ratio `23` is exceptional for a structural finite-field reason or only at `p=31`.
5. Search the full legal two-row switch graph for a terminal path from this state.

AC6 and the general no-three-in-line conjecture remain open.
