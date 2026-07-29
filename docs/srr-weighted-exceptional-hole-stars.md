# Weighted exceptional endpoints and source-hole stars

**Branch:** `research/superregular-resampling`

SRR2ak--SRR2an trim endpoints of large hole multiplicity by cardinality. This note gives the weighted form needed when endpoint records carry unequal event costs or protected-event loads.

Fix an endpoint set `S`. Give each endpoint `b` a nonnegative weight `lambda_b`, write

\[
\nu(b)=|\{a:b\in H(a)\}|,
\]

and define the weighted hole mass

\[
\mathcal M_S
=
\sum_{b\in S}\nu(b)\lambda_b
=
\sum_{a\in A}\sum_{b\in S\cap H(a)}\lambda_b.
\]

For `tau>=0`, retain the same exceptional set

\[
T_\tau=\{b\in S:\nu(b)>\tau\}.
\]

## SRR2ao -- weighted exceptional-set bound -- PROVED

The total endpoint weight removed by multiplicity trimming satisfies

\[
\boxed{
\sum_{b\in T_\tau}\lambda_b
\le
\frac{\mathcal M_S}{\tau+1}.
}
\]

### Proof

Every `b in T_tau` has `nu(b)>=tau+1`, so

\[
\mathcal M_S
\ge
\sum_{b\in T_\tau}\nu(b)\lambda_b
\ge
(\tau+1)\sum_{b\in T_\tau}\lambda_b.
\]

Divide by `tau+1`. QED.

## SRR2ap -- source-star concentration -- PROVED

One source `a` satisfies

\[
\boxed{
\sum_{b\in S\cap H(a)}\lambda_b
\ge
\frac{\mathcal M_S}{|A|}.
}
\]

More generally, if the sources are partitioned into `r` declared classes, one class carries at least `mathcal M_S/r` weighted hole mass.

### Proof

Use the second expression for `mathcal M_S` and pigeonhole over sources, or over the declared source classes. QED.

## SRR2aq -- exceptional-weight/source-star dichotomy -- PROVED

Fix a proposed exceptional-weight budget `Lambda>=0`. For every `tau>=0`, one of the following holds:

1. the exceptional endpoints have total weight at most `Lambda`;
2. one source has weighted low-cost hole star greater than
   \[
   \boxed{\frac{(\tau+1)\Lambda}{|A|}.}
   \]

### Proof

If branch 1 fails, SRR2ao implies `mathcal M_S>(tau+1)Lambda`. Apply SRR2ap. QED.

## SRR2ar -- weighted trimmed-flow router -- PROVED

For one cost sublevel `S`, choose `tau`. Then one exact continuation holds:

1. delete `T_tau`, apply SRR2al to the retained set, and charge exceptional endpoint weight at most `mathcal M_S/(tau+1)`;
2. one source carries a weighted hole star at least `mathcal M_S/|A|`;
3. one endpoint violates the proposed multiplicity threshold;
4. the endpoint weights, source-hole incidence, conditioning or event records are not occurrence-faithful.

Thus both cardinality loss and event-weight loss from multiplicity trimming are explicit. Large weighted loss is not diffuse: it concentrates on one source-local hole star.

### Proof

SRR2ak--SRR2al control the retained matching deficiency and SRR2ao controls removed weight. SRR2ap returns the concentrated alternative. QED.

## Corrected SRR3 frontier

The endpoint-multiplicity branch now needs only a bound on weighted total hole mass, or payment of one weighted source-hole star. Remaining geometric work is to bound these masses for actual bounded-cycle switching menus and to connect the returned source star to a current line, blocker, owner or protected-event payment.

## Finite check

`scripts/verify_srr_weighted_exceptional_hole_stars.py` exhausts small weighted hole systems and verifies the exceptional-weight, source-star and dichotomy inequalities.