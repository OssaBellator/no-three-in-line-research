# Arithmetic classification of the robust p=31 heavy-anchor family

## Status

This note keeps AC as the only active track and proves AC5oa--AC5of. It classifies the 14 rank-one AC1 certificate occurrences through the robust ratio-23 bank’s heavy anchor `(5,19)`.

The classification does not manufacture current payment. The heavy anchor is a prospective replacement cell, so every target-containing triple remains prospective unless a separate current owner is attached.

## AC5oa -- complete occurrence dictionary -- PROVED

Every one of the 14 occurrences retains:

- its two fixed physical endpoints;
- the endpoint hyperbola channels in `{1,23}`;
- the exact product-carry levels
  \[
  \kappa_c(x,y)=\frac{xy-c}{31};
  \]
- its primitive real-line direction;
- the common heavy anchor `(5,19)`;
- the `PROSPECTIVE` owner route.

The complete dictionary is stored in `data/ac-p31-ratio23-heavy-anchor.json`. No two physical pairs are merged merely because their coarse carry signature agrees.

## AC5ob -- exact direction and channel decomposition -- PROVED

The primitive-direction multiplicities are

\[
\boxed{6,6,1,1}
\]

on directions

\[
(1,-1),(1,1),(1,-10),(1,-5).
\]

The endpoint channel-pair counts are

\[
\boxed{
3\text{ in }H_1\!\times H_1,
\quad8\text{ mixed},
\quad3\text{ in }H_{23}\!\times H_{23}.
}
\]

Every primitive direction has first coordinate one. Thus the ordinary reduced slope denominator is one throughout this family; no nontrivial denominator `q>=2` is exposed by the line directions themselves.

## AC5oc -- exact product-carry dispersion -- PROVED

The 14 physical pairs represent exactly

\[
\boxed{11}
\]

distinct product-carry signatures.

Ten signatures occur once. The single repeated signature is the mixed-channel signature

\[
\boxed{((1,23),(2,0))}
\]

and occurs four times.

Hence the maximum exact signature multiplicity is four, substantially sharper for this instance than the ambient divisor ceiling. The family is neither one carry signature nor a purely rich-line repetition.

## AC5od -- endpoint-disjoint extraction -- PROVED

Join fixed endpoints when their pair forms one of the 14 heavy-anchor certificates. The endpoint graph is exactly

\[
\boxed{K_4\sqcup K_4\sqcup K_2\sqcup K_2.}
\]

Therefore its maximum matching number is

\[
\boxed{2+2+1+1=6.}
\]

The lexicographically least maximum matching is retained in the data file. Thus AC1c’s endpoint-disjoint star extraction is exact here: six, not merely a lower bound obtained from maximum degree.

## AC5oe -- six-signature star -- PROVED

Among the maximum endpoint-disjoint matchings, one contains six distinct product-carry signatures. One canonical such matching is

\[
\begin{aligned}
&(1,23)-(23,1),\quad (2,16)-(7,21),\quad (3,21)-(21,3),\\
&(4,29)-(6,9),\quad (7,9)-(8,4),\quad (10,24)-(15,29).
\end{aligned}
\]

Thus endpoint disjointness need not lose carry dispersion in this concrete family.

## AC5of -- payment-safe AC2 continuation -- PROVED

The heavy anchor `(5,19)` is absent from the current two-hyperbola state. Consequently every triple formed by this anchor and one of the 14 fixed pairs is prospective collateral and contributes zero automatic destroyed payment.

The six-edge star of AC5oe is therefore an exact structural AC2 object with six distinct carry signatures, but not yet a paid bank. To enter AC2 payment, each selected pair must receive a separate current owner satisfying the transition-relative physical, coherence and destruction contract.

Absent such owners, the exact continuation is one of:

1. construct a legal repair family whose actual destruction pays the six objects;
2. attach occurrence-faithful source/certificate tokens and solve their compatibility matching;
3. use the six new carry signatures as monotone exposure;
4. return an exact repeated-signature or source-deficient obstruction.

No nontrivial BDA denominator or implicit payment is inferred from the line labels.

## Deterministic audit

Run:

```text
python scripts/verify_ac_p31_heavy_anchor_classification.py
```

Expected ledger:

- physical occurrences: `14`;
- direction counts: `6,6,1,1`;
- channel-pair counts: `3,8,3`;
- product-carry signatures: `11`;
- maximum signature multiplicity: `4`;
- endpoint components: `4,4,2,2`;
- maximum endpoint-disjoint size: `6`;
- maximum distinct signatures in such a matching: `6`;
- primitive direction denominators: `1`;
- owner route: `PROSPECTIVE`.

## Remaining frontier

The next physical task is to construct the repair objects and full incompatibility graph for the six-signature star. A successful compatible family must destroy named current certificates or consume named sources; failure must return a paid neighbourhood overload, a Hall-deficient source core or an unticketed repeated-signature cycle.

AC6 and the general no-three-in-line conjecture remain open.
