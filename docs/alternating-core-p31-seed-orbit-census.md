# Complete p=31 alternating-star seed and symmetry census

## Status

This note keeps AC as the sole active research track and proves AC5nq--AC5nu. It exhausts all 216 seven-or-more-pair hyperbola-rectangle seed addresses at `p=31` under the canonical first-seven-pair, first-endpoint bank rule introduced in AC5nk--AC5np.

The census is finite and rule-specific. It does not claim that the raw lexicographic rule is geometrically natural; one purpose of the symmetry audit is to identify and correct that limitation.

## AC5nq -- complete canonical seed census -- PROVED

Among all 216 physical seed addresses:

- 140 have at least one improving bank state;
- 76 have no improving bank state;
- 10 have best bank potential equal to the current potential;
- 66 have every bank state strictly worse than the current state.

The difference

\[
\min_{\pi\in\Omega(F)}\Phi(S_\pi)-\Phi(S)
\]

ranges from `-33` to `31`.

The bank-size distribution is

\[
\begin{array}{c|rrrrrrrrrrrr}
|\Omega(F)|&927&928&933&1077&1086&1088&1094&1101&1289&1300&1545&1854\\\hline
\#\text{seeds}&4&4&2&2&4&2&22&6&12&48&70&40.
\end{array}
\]

### Proof

Enumerate every ordered channel pair, legal two-row rectangle switch and inserted candidate. Retain the addresses with at least seven real secant pairs in the anchor hyperbola, choose the first seven pairs and first endpoint of each, and exhaust the resulting forbidden-position matching bank. Every evaluated state retains all unchanged cells of both layers and therefore has exactly 60 points. QED.

## AC5nr -- exact channel-ratio census -- PROVED

Attach to a seed the multiplicative channel ratio

\[
q=b/a\pmod {31},
\]

where `H_a` is the anchor layer and `H_b` is the switched layer.

Exactly one ratio class is uniformly nonimproving under the canonical rule:

\[
\boxed{q=23.}
\]

All eight canonical ratio-23 seed addresses have no improving state.

Nine ratio classes are uniformly improving:

\[
\boxed{7,8,9,11,15,17,24,26,30.}
\]

Every other represented ratio has both improving and nonimproving addresses.

For clarity, ratio `2` has two improving and six nonimproving addresses. This value is derived by the committed audit and corrects an earlier scratch-table transposition.

## Square-symmetry orbits

Let `D_4` act on the `30` by `30` board by the eight square symmetries. The anchor and switch roles are retained. A seed record includes both complete hyperbola layers, the removed and inserted switch cells, the candidate and the full secant-pair set.

## AC5ns -- geometric seed-orbit quotient -- PROVED

The 216 seed addresses split into

\[
\boxed{54}
\]

geometric orbits, each of size four.

Under the raw lexicographic endpoint rule:

- 30 orbits have all four representatives improving;
- 14 orbits have all four representatives nonimproving;
- 10 orbits split into two improving and two nonimproving representatives.

Thus the raw rule is not equivariant under the square symmetries. A different outcome inside one geometric orbit is a selector artefact, not a change in the underlying seed geometry.

### Proof

Canonicalize complete physical seed records under all eight board actions. Every transformed record occurs in the census. Each orbit contains four distinct addresses because the other four actions stabilize one of the role-preserving hyperbola descriptions. Direct bank evaluation gives the three displayed orbit types. QED.

## AC5nt -- equivariant canonical selector -- PROVED

For each geometric orbit, choose the lexicographically least complete transformed seed record, apply the first-seven-pair, first-endpoint rule only in that representative, and transport the selected bank back by the inverse board symmetry.

This is a well-defined `D_4`-equivariant selector. Among the 54 orbits it gives:

\[
\boxed{37\text{ improving orbits},\qquad17\text{ nonimproving orbits}.}
\]

### Proof

A finite orbit has one least complete record. Board symmetries biject the retained cells, legal matching states and real collinear triples, so transporting the representative bank preserves every potential. The counts follow by evaluating the 54 representatives. QED.

## AC5nu -- corrected seed continuation interface -- PROVED

A uniform AC seed theorem may not use a coordinate-dependent first-endpoint rule without recording the chosen coordinate frame. It must instead use one of:

1. the equivariant orbit-representative selector of AC5nt;
2. a complete union over all pair omissions and endpoint orientations;
3. another physically declared selector proved invariant under the permitted board symmetries.

Under the first option, 17 of the 54 p=31 seed orbits still enter AC1. Under the second option, the ratio-23 obstruction is tested in the next theorem block.

No raw mixed orbit is promoted to progress merely because one coordinate representative improves.

## Deterministic audit

Run:

```text
python scripts/verify_ac_p31_seed_orbit_census.py
```

Expected ledger:

- raw seed addresses: `216`;
- improving/nonimproving: `140/76`;
- neutral/strictly worse: `10/66`;
- best-minus-current range: `-33,31`;
- square-symmetry orbits: `54`, all of size `4`;
- all-improving/all-nonimproving/mixed orbits: `30/14/10`;
- equivariant-selector improving/nonimproving orbits: `37/17`;
- uniformly nonimproving ratio: `23`;
- ratio-2 improving/nonimproving addresses: `2/6`.

## Remaining frontier

1. Test the ratio-23 class against every seven-of-eight pair choice and every endpoint orientation.
2. Classify the exact AC1 certificate family of the resulting robust nonimproving bank.
3. Determine which ratio classes remain uniformly improving after replacing the raw rule by a complete-orientation union.
4. Prove a structural channel-ratio criterion rather than a finite p=31 table.

AC6 and the general no-three-in-line conjecture remain open.
