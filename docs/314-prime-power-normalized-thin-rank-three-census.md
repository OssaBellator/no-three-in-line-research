# Exact normalized rank-three offspring census through side five

CMR1662--CMR1669 execute the normalized fixed-interface response census through
side five and determine exact rank-one and rank-two prescription caps.  The
remaining fixed-interface and line-clean offspring rows may also contain
residual-rank-three prescriptions.  This chapter extends the same exhaustive
census to rank three.

The normalized host is

\[
H_d=K_{d,d}\setminus(I_d\cup\{(0,1)\}),
\]

with a deleted partial matching `X subseteq H_d`, executable board

\[
G_X=H_d\setminus X,
\]

and residual `S_{d-2}` canonicalization.  A rank-three prescription is a
three-edge partial matching contained in at least one response matching.

## 1. Ambient rank-three prescription stock

### Theorem CMR1686 -- PROVED

The complete bipartite board `K_{d,d}` has exactly

\[
\boxed{
R_3(d)=6\binom d3^2
}
\]

rank-three prescriptions.

### Proof

Choose three source vertices, choose three target vertices and choose one of the
`3!` bijections between them. ∎

Every normalized response host has at most this many compatible rank-three
labels.

## 2. Side three is forced in rank three

### Theorem CMR1687 -- PROVED

Across the four canonical executable side-three hosts:

1. there are exactly `4` extendable rank-three prescription instances;
2. every instance is the unique perfect matching of its host; and
3. every instance has probability one and belongs to exact contraction.

### Proof

CMR1663 and CMR1665 show that every executable side-three host has one response.
Its only rank-three prescription is the complete response matching itself. ∎

Thus no stochastic rank-three side-three row remains.

## 3. Side-four rank-three census

### Theorem CMR1688 -- PROVED

Across the 45 canonical executable side-four hosts:

1. there are exactly
   \[
   \boxed{448}
   \]
   extendable rank-three prescription instances;
2. exactly
   \[
   \boxed{28}
   \]
   are forced;
3. every nonforced instance satisfies
   \[
   \boxed{
   \Pr(P\subseteq Q)\le\frac12;
   }
   \]
4. the cap `1/2` is attained.

### Proof

For every canonical host, enumerate all response permutations and every
three-edge subset of each response.  Deduplicate prescriptions, count containing
responses and divide by the exact host denominator.  Separate numerator equal to
the denominator and maximize the remaining fractions. ∎

Forced instances enter the existing common-prescription contraction branch.

## 4. Side-five rank-three census

### Theorem CMR1689 -- PROVED

Across the 124 canonical executable side-five hosts:

1. there are exactly
   \[
   \boxed{15017}
   \]
   extendable rank-three prescription instances;
2. none is forced;
3. every instance satisfies
   \[
   \boxed{
   \Pr(P\subseteq Q)\le\frac14;
   }
   \]
4. the cap `1/4` is attained.

### Proof

Use the same exact numerator/denominator enumeration as CMR1688 on every
canonical side-five host. ∎

The rank-three cap is strictly smaller than the side-five rank-one and rank-two
caps.

## 5. Complete nonforced probability table through side five

### Theorem CMR1690 -- PROVED

After forced contractions are removed, the normalized matching-level
prescription caps are:

| side | rank one | rank two | rank three |
|---:|---:|---:|---:|
| 3 | no stochastic row | no stochastic row | no stochastic row |
| 4 | `3/4` | `2/3` | `1/2` |
| 5 | `2/3` | `2/5` | `1/4` |

Every displayed side-four and side-five cap is attained.

### Proof

Combine CMR1665--CMR1667 with CMR1687--CMR1689. ∎

This table controls every residual prescription rank used by the current
line-clean and fixed-interface offspring rows.

## 6. Uniform expectation capacities

Let one corrected geometric class on a canonical host contain `N_1,N_2,N_3`
nonforced prescriptions of ranks one, two and three.

### Theorem CMR1691 -- PROVED

The following matching-level expectation bounds hold.

### Side four

\[
\boxed{
A_{\rm class}
\le
\frac34N_1+rac23N_2+rac12N_3.
}
\]

### Side five

\[
\boxed{
A_{\rm class}
\le
\frac23N_1+rac25N_2+rac14N_3.
}
\]

### Proof

Sum the corresponding prescription probability caps from CMR1690 inside one
current response row. ∎

No historical response rows are added.

## 7. Exact integer numerator capacities

Let one canonical host have response denominator

\[
Z=|\operatorname{PM}(G_X)|.
\]

### Theorem CMR1692 -- PROVED

After forced prescriptions are removed, one may use the following integer
numerator capacities.

### Side four

\[
\boxed{
C_4(Z;N_1,N_2,N_3)
=
N_1\left\lfloor\frac{3Z}{4}\right\rfloor
+N_2\left\lfloor\frac{2Z}{3}\right\rfloor
+N_3\left\lfloor\frac{Z}{2}\right\rfloor.
}
\]

### Side five

\[
\boxed{
C_5(Z;N_1,N_2,N_3)
=
N_1\left\lfloor\frac{2Z}{3}\right\rfloor
+N_2\left\lfloor\frac{2Z}{5}\right\rfloor
+N_3\left\lfloor\frac{Z}{4}\right\rfloor.
}
\]

If `a_class` is the exact expectation numerator over denominator `Z`, then

\[
\boxed{a_{\rm class}\le C_d(Z;N_1,N_2,N_3).}
\]

### Proof

Each prescription numerator is an integer and is bounded by its probability cap
times `Z`; hence it is at most the corresponding floor.  Sum over the class. ∎

These capacities feed directly into the selector gap compiler CMR1646--CMR1653
and the line-profile capacity compiler CMR1678--CMR1685.

## 8. Rank-three thin-census endpoint

### Corollary CMR1693 -- PROVED

The normalized thin matching-level census through side five is complete for all
residual ranks one through three.

1. Side three has only forced contraction prescriptions.
2. Side four has exact nonforced caps `3/4`, `2/3`, `1/2`.
3. Side five has exact caps `2/3`, `2/5`, `1/4` and no forced prescriptions.
4. Every canonical host denominator is already tabulated by CMR1663.
5. Every geometric class has an explicit integer numerator capacity once its
   rank counts are known.

The remaining thin work is geometric offspring classification on these
canonical hosts and any larger side not eliminated structurally.  No all-`n`
theorem is claimed.

All `15,465` extendable rank-three prescription instances on canonical sides
four and five, together with the four forced side-three instances (`15,469`
total), are checked in
[`scripts/verify_prime_power_normalized_thin_rank_three_census.py`](../scripts/verify_prime_power_normalized_thin_rank_three_census.py).
