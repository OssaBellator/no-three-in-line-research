# Weighted closure of the mixed balanced-floor templates

**Branch:** `research/bounded-denominator-absorbers`

BDA5bu--BDA5bx classify the incidence geometry of every template involving `CD` or `AB`. This note converts that classification into exact weighted overlap and exclusivity statements for context-pair addresses.

A context-pair address is an unordered pair `{X,Y}` of distinct fixed context cells. Two role-side records overlap only when they have the same pair address.

## BDA5by -- one-point line intersections give zero pair overlap -- PROVED

Let two record families require their context pairs to lie respectively on affine lines `L_1,L_2`. If

\[
|L_1\cap L_2|\le1,
\]

then the two families have disjoint context-pair address support.

### Proof

A common address would contain two distinct cells belonging to both lines, contradicting the intersection bound. QED.

## BDA5bz -- nonresonant mixed templates are address-disjoint -- PROVED

For distinct decoder roles, the following mixed templates have zero common context-pair weight:

1. `CD-A` unless `2hv=u(2h+q)`;
2. `CD-B` unless `2(h+q)v=u(2h+q)`;
3. `CD-C` and `CD-D` always;
4. `AB-C` and `AB-D` always;
5. `CD-AB` always.

### Proof

In each nonresonant `CD` versus one-local case, BDA5bu shows that the relevant context lines cannot coincide and hence intersect in at most one cell. BDA5bv gives the same conclusion for `AB-C` and `AB-D`. BDA5bw gives exactly one `CD-AB` intersection point. Apply BDA5by. QED.

## BDA5ca -- resonant and radial weighted decomposition -- PROVED

The only mixed templates that may have nonzero pair-address overlap are:

1. resonant `CD-A`;
2. resonant `CD-B`;
3. radial `AB-A`;
4. radial `AB-B`.

For either such template, let the two role-side weighted address functions be `w_u(e),w_v(e)` after aggregating aliases, and put

\[
O=\sum_e\min\{w_u(e),w_v(e)\}.
\]

Then the two families split losslessly into:

- common line-supported overlap of weight `O`;
- role-`u` exclusive residual of weight `W_u-O`;
- role-`v` exclusive residual of weight `W_v-O`.

For every `0<theta<1`, if `W_u,W_v>=Q`, then either

\[
\boxed{O\ge\theta Q}
\]

or both exclusive residuals are greater than `(1-theta)Q` whenever `O<theta Q`.

### Proof

On a resonance or radial profile, any common pair lies on the coincident declared line. Remove the pointwise minimum address weight from both sides. The residual supports are disjoint and have the displayed weights. QED.

## BDA5cb -- complete weighted off-diagonal router -- PROVED

Every off-diagonal balanced-floor template now has one exact weighted continuation:

1. a local-cell collision profile;
2. a one-local connector-line overlap or two exclusive residual families from BDA5bt;
3. a `CD-A` or `CD-B` arithmetic resonance carrying line overlap, or two exclusive residuals;
4. an `AB-A` or `AB-B` radial-line overlap, or two exclusive residuals;
5. two address-disjoint role families in every remaining mixed template.

Hence all fifteen unordered off-diagonal templates are closed at the weighted incidence level. Remaining BDA6 work is to pay or ticket the resulting connector, resonant and radial line families, realize their owners, and import higher-rank events.

## Finite check

`scripts/verify_bda_mixed_weighted_closure.py` checks the line-intersection-to-address-disjoint implication, the resonance list and the exact pointwise weighted decomposition.