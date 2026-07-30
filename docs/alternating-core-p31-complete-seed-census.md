# Complete p=31 alternating-star seed orientation census

## Status

This note keeps AC as the sole active track and extends the prime-minus-one seed census by AC5nq--AC5ns. It exhausts every retained seven-or-more-pair seed orientation at `p=31` under the canonical rule that the first seven ordered secant pairs and the first endpoint of each pair form the alternating block.

The statements are finite and physical. They do not assert that the canonical endpoint rule is optimal among all orientations of an eight-pair star.

## AC5nq -- complete p=31 seed split -- PROVED

There are exactly

\[
\boxed{216}
\]

legal seed orientations with at least seven same-channel secant pairs. Exhausting the complete matching bank for every orientation gives

\[
\boxed{140\text{ improving orientations},\qquad 76\text{ nonimproving orientations}.}
\]

Thus the explicit nonimproving seed of AC5nn is a genuine AC1 input, but nonimprovement is not forced by the prime, board size, or seven-pair threshold alone.

### Proof

For every ordered pair of distinct channels, every two-row rectangle switch, and each inserted candidate, enumerate the complete secant-pair set in the anchor hyperbola. Retain a seed only when both inserted cells avoid the anchor layer and at least seven secant pairs occur. For each retained address, form all legal permutations avoiding the diagonal and opposite-layer collision positions. Every successor retains all unchanged points of both layers. Exact line masks compute the real triple potential. The deterministic audit returns 216, 140 and 76. QED.

## AC5nr -- strongest recorded p=31 AN decrease -- PROVED

Use anchor channel `H_1`, switch channel `H_12`, switch

\[
(16,24),(24,16)\longrightarrow(16,16),(24,24),
\]

and candidate `z=(16,16)`. There are eight secant pairs through `z`; use the first seven ordered pairs. The exact forbidden-position bank has 1094 states.

The current potential is

\[
\Phi(H_1\cup H_{12})=108,
\]

and 1083 of the 1094 bank states improve. The canonical least-potential matching has permutation

\[
(2,0,6,4,5,3,1)
\]

and replacement cells

\[
\{(1,26),(4,1),(6,12),(8,28),(10,13),(12,4),(13,8)\}.
\]

Its exact potential is

\[
\boxed{75},
\]

so the decrease is

\[
\boxed{108-75=33}.
\]

No other retained p=31 seed orientation has a larger potential decrease under the canonical seven-pair rule.

### Proof

The complete 216-orientation census records the minimum bank value for each seed. The displayed seed has current, fixed and best potentials `108,59,75`, bank size `1094`, and improving count `1083`. The maximum of `current-best` over all retained orientations is 33. QED.

## AC5ns -- exact heavy-anchor line decomposition -- PROVED

Return to the nonimproving AC5nn seed. Its heaviest rank-one anchor cell is

\[
A=(12,12)
\]

with 20 occurrence-faithful collateral certificates. Those certificates decompose exactly by primitive line direction as follows:

\[
\begin{array}{c|c|c}
\text{direction}&\text{fixed points on the line through }A&\text{certificate count}\\\hline
(1,1)&(4,4),(8,8),(16,16),(23,23),(30,30)&10\\
(1,-1)&(3,21),(5,19),(19,5),(21,3)&6\\
(2,-3)&(6,21),(14,9)&1\\
(3,-2)&(9,14),(21,6)&1\\
(1,2)&(17,22),(20,28)&1\\
(2,1)&(22,17),(28,20)&1.
\end{array}
\]

In particular, the diagonal and anti-diagonal directions carry

\[
\boxed{16/20}
\]

of the heavy-anchor occurrences.

These are created collateral certificates involving the proposed replacement cell `A`; they are not current destroyed payment. The family is mixed-source: the diagonal contains unchanged hyperbola points and both inserted switch cells. Therefore the same-channel cross-carry theorem does not apply without a new mixed-source compatibility statement.

The exact next AC1 target is consequently:

> classify a proposed replacement cell supporting a rich mixed-source diagonal or anti-diagonal into an improving alternative, a current payable owner, a bounded-denominator/carry chamber, or a named rigid obstruction.

### Proof

Enumerate every pair of fixed-state points collinear with `A`, normalize its direction, and group equal lines. A line with `m` fixed points contributes `binom(m,2)` rank-one occurrences. The displayed group sizes are `5,4,2,2,2,2`, giving `10+6+1+1+1+1=20`. Direct state membership classifies the points and confirms that `A` is absent before installation. QED.

## Complete-state regression guardrail

The corrected audit retains every unchanged switch-layer point. In the nonimproving seed the fixed state has potential 88. Any evaluator that omits the unchanged switch layer is not evaluating the AC state and can falsely report much smaller successors. The verifier asserts the full `2(p-1)` state cardinality and the fixed potential before accepting any bank value.

## Deterministic audit

Run:

```text
python scripts/verify_ac_prime_seed_census.py
```

Expected additional ledger:

- p=31 retained orientations: `216`;
- improving orientations: `140`;
- nonimproving orientations: `76`;
- maximum potential decrease: `33`;
- strongest-seed bank size: `1094`;
- strongest-seed improving states: `1083`;
- strongest-seed successor potential: `75`;
- nonimproving fixed potential: `88`;
- heavy-anchor line counts: `10,6,1,1,1,1`.

## Remaining frontier

1. Continue the explicit 75-potential successor by legal two-row switches.
2. Classify the mixed-source diagonal and anti-diagonal heavy-anchor families.
3. Repeat the complete orientation census at larger primes using occurrence-faithful endpoint choices.
4. Replace the finite p=31 split by a uniform arithmetic criterion predicting improving versus AC1 seeds.

AC6 and the general no-three-in-line conjecture remain open.
