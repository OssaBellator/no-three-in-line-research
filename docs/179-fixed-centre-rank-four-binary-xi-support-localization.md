# Rank-four binary Xi support avoidance and partner-graph localization

PP3abv--PP3acb reduce fixed-centre rank-four binary `Xi` weight to one
centre-arc partner fibre. A dyadic decomposition of a heavy fibre yields a
uniform partner fan or a high-multiplicity pattern. The multiplicity alternative
is not an independent obstruction: a conditioned single cycle can avoid the
entire positive-weight partner support, regardless of the weights, whenever the
support is sufficiently sparse relative to the exact one-arc cylinder scale.

This chapter replaces weighted multiplicity by an unweighted support threshold.
If support avoidance does not complete the paid trade and the residual terms
retain fixed slack, the partner graph has size `Omega(N^2/b)`. A bipartite
star--matching decomposition then yields either a large partner-resource star or
a large matching of remote arcs whose noncentral endpoint resources are pairwise
disjoint.

The resulting star or fixed-cell petal bank remains a conversion interface. This
chapter does not assert a source-valid paid installation in the residual
concentrated cases.

## 1. Positive-weight partner support

Fix a source-admissible incoming centre arc `r->c`; the outgoing case is
transposed. Let

```text
E_r={u->v: gamma_in(r;u,v)>0}
```

be its positive-weight remote partner support, and put

```text
h_r=|E_r|.
```

Choose the random block and one-arc conditioned Hamilton cycle from PP3abw. Let
`X_r` be the number of arcs of `E_r` selected by the cycle.

Write

```text
kappa_N,b=(b-3)/((N-2)(N-3)).
```

### Proposition PP3acc -- PROVED

One has the exact identity

```text
E[X_r]=kappa_N,b h_r.
```

The same identity holds for an outgoing centre arc.

#### Proof

Every prescribed remote arc disjoint from the fixed centre arc appears with
probability exactly `kappa_N,b` by PP3abw. Sum its indicator over the `h_r`
supported arcs. ∎

The variable `X_r` depends only on the positive support. Pattern multiplicities
and weights play no role in the event `X_r=0`.

## 2. Support-avoiding paid completion

Let `Q_r` be the expected number of all remaining source-invalid canonical
patterns under the same conditioned law. Let `J_r` be the expected insertion cost
of all remaining paid classes, excluding the complete rank-four fibre supported
on `E_r`. Let `R_c>0` be the exact removal credit of the captive centre.

### Theorem PP3acd -- PROVED

If

```text
Q_r + kappa_N,b h_r + J_r/R_c < 1,
```

then one conditioned state is source-valid, selects no arc of `E_r`, and has
remaining insertion cost below `R_c`. In particular its entire rank-four fibre
cost is zero and it gives a strict pool-compatible decrease.

The transposed statement holds for an outgoing centre arc.

#### Proof

Average the nonnegative random variable

```text
(number of source violations) + X_r + (remaining insertion cost)/R_c.
```

Its expectation is below one by PP3acc and the hypothesis. Some outcome has
value below one. The first two summands are nonnegative integers, so both vanish;
the final summand is then below one. Since no supported partner arc is selected,
no rank-four pattern in the fixed fibre occurs, irrespective of its weight.
Apply PP3kx. ∎

Thus a fixed high-multiplicity pattern is automatically removed whenever its
whole support lies in the support-avoidance regime.

## 3. Residual slack forces large support

Fix `tau in (0,1)`. Say that a centre arc has **residual slack `tau`** when

```text
Q_r + J_r/R_c <= 1-tau.
```

### Corollary PP3ace -- PROVED

For a centre arc with residual slack `tau`, at least one of the following holds.

1. A source-valid strict decrease exists and avoids the complete rank-four fibre.
2. The positive partner support satisfies

   ```text
   h_r >= tau/kappa_N,b
       = tau (N-2)(N-3)/(b-3).
   ```

#### Proof

If the support bound in alternative 2 fails, then
`kappa_N,b h_r<tau`. Add this to the residual-slack inequality and apply PP3acd.
∎

Consequently failure of support avoidance is either residual source/paid
concentration or a large unweighted partner graph. Weight multiplicity is no
longer a third case.

## 4. Partner-resource star or remote matching

Regard `E_r` as a bipartite graph whose left vertices are remote arc tails and
whose right vertices are remote arc heads. These are typed endpoint resources,
so the same index on the two sides is treated as two different resources.

### Proposition PP3acf -- PROVED

For every integer `L>=1`, a partner graph with `h` arcs has at least one of:

1. a tail or head resource incident with at least `L` partner arcs;
2. a matching of at least

   ```text
   h/(2L)
   ```

   partner arcs.

In particular, taking `L=ceil(sqrt(h/2))` yields a partner-resource star or a
remote matching of size `Omega(sqrt(h))`.

#### Proof

Take a maximal matching of size `s`. Its `2s` endpoint resources meet every edge.
If every resource degree is below `L`, then `h<2sL`, so
`s>h/(2L)`. Otherwise alternative 1 holds. The square-root choice balances the
two bounds. ∎

In the matching alternative, the binary patterns

```text
{fixed centre arc, remote matching arc}
```

share only the fixed centre cell. Their remote tail/head resource pairs are
pairwise disjoint. This is a fixed-cell petal bank, not a fully resource-disjoint
binary matching.

## 5. Slab-optimal size

Use

```text
N=m^(19/20+o(1)),
b=m^(kappa+o(1)),
0<kappa<19/80,
W=m^(19/40+o(1)).
```

### Corollary PP3acg -- PROVED

For fixed residual slack `tau>0`, failure of support avoidance gives

```text
h=Omega(N^2/b)
 =m^(19/10-kappa+o(1)).
```

The star--matching decomposition PP3acf then produces a partner-resource star or
remote matching of size

```text
Omega(N/sqrt(b))
 =m^(19/20-kappa/2+o(1)).
```

This is asymptotically larger than the marked-bank target `W` throughout the
allowed filler range.

#### Proof

Insert the exact reciprocal of `kappa_N,b` from PP3ace. Taking square roots gives
the second scale. Since `kappa<19/80`,

```text
19/20-kappa/2 > 19/20-19/160 = 133/160 > 19/40.
```

Hence the extracted structured family contains a `W`-sized subfamily. ∎

The large-support alternative is much stronger than the target-size dyadic fan
in PP3aca: it is an unweighted support family of order `N/sqrt(b)` after the
star--matching split.

## 6. Revised rank-four endpoint

### Corollary PP3ach -- PROVED

At a source-light captive centre, rank-four binary `Xi` weight reduces to one of:

1. a one-arc conditioned state that avoids the entire positive partner support
   and completes the paid trade;
2. residual conditioned source or non-rank-four paid concentration at the centre
   credit scale;
3. a partner-resource star of size `Omega(N/sqrt(b))` inside one fixed centre-cell
   fibre;
4. a fixed-cell petal bank of `Omega(N/sqrt(b))` pairwise remote-resource-disjoint
   partner arcs.

Therefore neither a diffuse weighted fibre nor a fixed high-multiplicity
rank-four pattern remains an independent frontier. The exact remaining
rank-four objects are large unweighted partner stars/petal banks or residual
conditioned collateral. They feed the conditional binary-star, Hall,
two-resource, and bounded-support collateral interfaces.

## 7. Finite diagnostic

The script

```text
scripts/check_rank_four_binary_xi_support.py
```

checks a finite partner support. It computes the exact support expectation
`kappa_N,b h`, applies a rational residual-slack threshold, constructs a maximal
bipartite matching, and verifies the star--matching alternative for a supplied
integer `L`. The stored example realizes the large-support remote-matching branch.
