# Residue correctors for finite interaction lengths

`docs/506` identifies the asymptotic interaction rate polytope and gives an
`O(1/N)` connector bound.  This chapter sharpens a scalarized critical periodic
pattern to an exact optimum in every sufficiently long length residue class.

Let a finite directed interaction graph have rational scalar edge weights `w_e`.
Fix a base state `s`, a rational number `mu`, and a potential `h` such that

```text
c_e=w_e-mu+h_tail(e)-h_head(e) >= 0
```

for every edge.  Suppose a closed critical word `C` at `s` has length `ell` and
zero total reduced cost.

## 1. Product-graph residue defects

### Theorem PP3cjo -- PROVED / FINITE RESIDUE-CORRECTOR ORACLE

On the product graph `V x Z/ell Z`, give every lifted edge its reduced cost
`c_e` and increment the residue by one.  For each residue `r`, let `delta_r` be
the shortest-path cost from `(s,0)` to `(s,r)`.  Then `delta_r` is exactly the
minimum reduced cost of a closed interaction walk at `s` whose length is
congruent to `r mod ell`.

#### Proof

Lifting records precisely the endpoint state and length residue of every walk.
Reduced costs are nonnegative, so an exact finite shortest-path computation
finds the minimum.  Projection and lifting preserve both closedness and cost. ∎

## 2. Exact optimum in every residue class

### Theorem PP3cjp -- PROVED / CRITICAL-CYCLE RESIDUE FORMULA

Let `R_r` be a shortest residue witness of length `d_r`.  For every
`N=d_r+k ell`, `k>=0`, the closed walk

```text
R_r C^k
```

has scalar weight

```text
mu N + delta_r
```

and is optimal among all closed walks at `s` of length `N`.

#### Proof

The potential telescopes on every closed walk, so its weight equals `mu` times
its length plus its total reduced cost.  `R_r C^k` has reduced cost `delta_r`
because `C` has zero reduced cost.  Every competing length-`N` closed walk has
the same residue and reduced cost at least `delta_r` by `PP3cjo`. ∎

## 3. Vector correction certificate

### Theorem PP3cjq -- PROVED / ALL-LENGTH VECTOR RECONSTRUCTION

If each edge also has a rational vector label `v_e` and the scalar weight is
`lambda dot v_e`, then the residue-optimal walk has exact total vector

```text
v(R_r)+k v(C).
```

Its average differs from the critical cycle mean by the explicit residue vector

```text
[v(R_r)-d_r v(C)/ell]/N.
```

The product-graph witness and these totals form a finite certificate for every
length in the residue class.

#### Proof

Vector labels add under concatenation.  Divide the exact total by
`N=d_r+k ell` and subtract `v(C)/ell`. ∎

## 4. Stored exact fixture

The audit `scripts/check_interaction_residue_correctors.py` uses two states and
four edges.  The critical cycle `BC` has length two, vector `(3,1,1)`, and scalar
mean `5/2` under weight `(1,1,1)`.  A potential gives reduced costs

```text
A:1/2, B:0, C:0, D:1/2.
```

The residue defects are `delta_0=0` and `delta_1=1/2`, with odd corrector `A`.
Consequently the exact optimum is

```text
(BC)^(N/2)             for even N,
A(BC)^((N-1)/2)        for odd N,
```

and the odd average scalar overhead is exactly `1/(2N)`.  The script checks
every length through 64 by independent dynamic programming.

## 5. Prime-patching consequence

A critical interaction cycle can now control every finite length, not merely an
asymptotic subsequence.  One finite product-graph computation supplies the exact
boundary defect and an explicit optimal correction word for each length residue.
