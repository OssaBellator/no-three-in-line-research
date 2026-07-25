# Full-prefix tokens inherit the coarse-reset return profile

CMR394--CMR397 sharpen repeated-token accounting by fixing both endpoint
prefix coordinates. CMR378--CMR384 compute row-token return under laminar and
recursive coarse prefix resets. The two results combine directly: one ancestor
reset can return at most one old matching edge for each source column in the
fixed full-token column prefix.

Let

\[
t=p^h
\]

and fix one absolute full token

\[
\tau=(b,a,c,\theta),
\qquad
1\le b<h.
\]

Its edge universe is

\[
U_\tau^{(2)}
=
\{(x,y):x\equiv a\pmod{p^b},
 y\equiv c\pmod{p^b}\}.
\]

Consider an old-cell-clean rematching of one depth-`r` prefix block, where
`0\le r<b`.

## 1. One ancestor reset

### Theorem CMR398 — PROVED

One depth-`r` one-layer prefix rematching reintroduces at most

\[
\boxed{\frac{t}{p^b}}
\]

old matching edges in `U_\tau^{(2)}`. It reintroduces none unless

1. the block column residue agrees with `a\pmod{p^r}`;
2. the block row-fibre residue agrees with `c\pmod{p^r}`.

The same bound holds in a peeled residual host and for the coordinate-dual
opposite-layer reset.

### Proof

By the exact host-churn theorem CMR382, the only full-host edges reintroduced
are old matching edges of the rematched block. An incompatible column block
contains no source extending `a`; an incompatible row fibre contains no row
extending `c`.

When both conditions hold, exactly

\[
\frac{t/p^r}{p^{b-r}}=\frac{t}{p^b}
\]

columns extend the prescribed depth-`b` column prefix. A matching has one old
edge per such source column. A persistent deletion mask can only reduce the
returned set. ∎

Unlike the exact row-token profile in CMR382, equality is not asserted: a
coarse matching need not send every compatible source to the chosen depth-`b`
row prefix.

## 2. One-pass reset budget

Follow the descending one-pass prefix schedule with the post-exposure ancestor
accounting of CMR383. Let

\[
I_\tau^{(2),\mathrm{coarse}}
\]

be the full-token reintroduction mass caused by all later coarser prefix resets.

### Theorem CMR399 — PROVED UNDER THE ONE-PASS HYPOTHESIS

For every full token,

\[
\boxed{
I_\tau^{(2),\mathrm{coarse}}
\le
\frac{2bt}{p^b}.
}
\]

Consequently,

\[
\boxed{
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}
+
\frac{2bt}{p^b}.
}
\]

If only the measured layer is rematched, both factors `2` may be removed.

### Proof

For each coarser depth `r=0,\ldots,b-1` and each moving layer, at most one block
can satisfy the CMR398 column-prefix condition; the row-fibre condition may
remove that block. In a one-pass schedule every compatible depth-layer slot is
used at most once. There are at most `2b` slots, each returning at most
`t/p^b` edges. Combine with the full-token inventory CMR395. ∎

## 3. Deep full-token visit bounds

### Corollary CMR400 — PROVED UNDER THE ONE-PASS HYPOTHESIS

1. If `p^b>t^{1/3}`, then
   \[
   \boxed{
   D_\tau^{(2)}
   <
   t^{4/3}+2h\,t^{2/3}.
   }
   \]
2. If `p^b\ge t^{2/3}`, then
   \[
   \boxed{
   D_\tau^{(2)}
   \le
   t^{2/3}+2h\,t^{1/3}.
   }
   \]

### Proof

Apply CMR399 and substitute the corresponding lower bound on `p^b`, using
`b\le h`. ∎

## 4. Exact reset-occurrence factorization

For every coarser depth `r<b` and layer `\ell`, let

\[
A_{\tau,r,\ell}^{(2)}
\]

count rematchings, after token exposure, of the unique depth-`r` block which can
satisfy both CMR398 compatibility conditions. Put

\[
A_\tau^{(2)}
=
\sum_{r=0}^{b-1}\sum_{\ell=0}^1A_{\tau,r,\ell}^{(2)}.
\]

### Theorem CMR401 — PROVED

For an arbitrary number of recursive prefix resets,

\[
\boxed{
I_\tau^{(2),\mathrm{coarse}}
\le
\frac{t}{p^b}A_\tau^{(2)}.
}
\]

If every compatible ancestor depth-layer slot is rematched at most `m` times,
then

\[
\boxed{
I_\tau^{(2),\mathrm{coarse}}
\le
\frac{2bmt}{p^b}
}
\]

and

\[
\boxed{
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}
+
\frac{2bmt}{p^b}.
}
\]

Conversely, failure of either multiplicity bound forces one of the at most
`2b` compatible ancestor slots to be rematched more than `m` times.

### Proof

CMR398 contributes at most `t/p^b` for each counted reset. The multiplicity
hypothesis gives `A_\tau^{(2)}\le2bm`; apply CMR395. The final assertion is the
contrapositive. ∎

Thus repeated use of one exact ancestor slot is the only unbounded recursive
prefix source.

## 5. Aggregate labelled return mass

### Corollary CMR402 — PROVED UNDER THE ONE-PASS HYPOTHESIS

Summing over every nonroot full token in the parent block gives

\[
\boxed{
\sum_{\theta\in\mathbb P^1(\mathbb F_p)}
\sum_{b=1}^{h-1}
\sum_{a,c\bmod p^b}
I_{(b,a,c,\theta)}^{(2),\mathrm{coarse}}
\le
2(p+1)t
\sum_{b=1}^{h-1}bp^b.
}
\]

In particular,

\[
\boxed{
\sum_\tau I_\tau^{(2),\mathrm{coarse}}
<
\frac{2(p+1)}{p-1}h t^2,
}
\]

so the direction-labelled aggregate is `O_p(t^2\log t)`.

### Proof

At depth `b` there are `p^{2b}` prefix pairs and `p+1` directions. Multiply by
the CMR399 per-token bound `2bt/p^b`, obtaining `2(p+1)btp^b`, and sum. Finally,

\[
\sum_{b=1}^{h-1}bp^b
<
h\sum_{b=1}^{h-1}p^b
<
\frac{ht}{p-1}.
\]

∎

This is deliberately a labelled upper bound: one returned edge may be counted
once for every direction.

A canonical descending prefix pass therefore has subquadratic per-token stock
at deep scales and `O_p(t^2\log t)` aggregate labelled return mass. The
remaining dynamic sources are repeated use of one ancestor slot, joint-parent
or band resets outside the prefix schedule, and fully forced exchange ancestry.

No all-`n` theorem is claimed here. Per-reset capacities, reset multiplicity,
one-pass sums, and depth specializations are checked in
[`scripts/verify_prime_power_full_token_reset_profile.py`](../scripts/verify_prime_power_full_token_reset_profile.py).
