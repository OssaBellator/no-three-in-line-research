# Full-prefix tokens inherit the coarse-reset return profile

CMR389--CMR392 sharpen repeated-token accounting by fixing both endpoint
prefix coordinates. CMR378--CMR384 compute row-token return under laminar and
recursive coarse prefix resets. The two results combine directly: one ancestor
reset can return at most one old matching edge for each source column in the
fixed full-token column prefix.

Let

\[
t=p^h
\]

and fix one absolute full prefix token

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

\[
0\le r<b.
\]

## 1. One ancestor reset

### Theorem CMR393 — PROVED

One depth-`r` one-layer prefix rematching reintroduces at most

\[
\boxed{
\frac{t}{p^b}
}
\]

old matching edges in `U_tau^(2)`.

It reintroduces none unless both of the following compatibility conditions
hold:

1. the block column residue agrees with `a modulo p^r`;
2. the block row-fibre residue agrees with `c modulo p^r`.

The same upper bound holds in a peeled residual host and for the
coordinate-dual opposite-layer reset.

### Proof

By the exact host-churn statement CMR382, the only edges reintroduced at
full-host level are old matching edges of the rematched block. If the block
column residue is incompatible with `a`, it contains no source column of the
full token. If the row fibre is incompatible with `c`, it contains no target
row of the full token.

When both are compatible, exactly

\[
\frac{t/p^r}{p^{b-r}}
=
\frac{t}{p^b}
\]

columns of the block extend the prescribed depth-`b` column residue `a`. A
matching has one old edge per such source column, so at most `t/p^b` returned
edges can lie in the full-token universe. A persistent deletion mask can only
reduce the returned set. The dual statement interchanges the two matching
classes. ∎

Unlike the row-token profile in CMR382, equality is not asserted: unless the
recursive depth-`b` descendant row fibre is retained, the old matching need not
send every compatible source column to the prescribed depth-`b` row prefix.

## 2. One-pass reset budget

Follow the descending one-pass prefix schedule of CMR380, with the sharper
post-exposure ancestor accounting of CMR383. Let

\[
I_\tau^{(2),\mathrm{coarse}}
\]

be the full-token edge reintroduction mass caused by all later coarser prefix
resets.

### Theorem CMR394 — PROVED UNDER THE ONE-PASS HYPOTHESIS

For every full token,

\[
\boxed{
I_\tau^{(2),\mathrm{coarse}}
\le
\frac{2bt}{p^b}.
}
\]

Consequently the number of full-token endpoint visits satisfies

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

At each coarser depth `r=0,...,b-1` and in each moving layer, there is at most
one block whose column prefix can extend `a`. The row-fibre condition can only
remove that candidate. Under the one-pass hypothesis, each compatible
block-layer slot is used at most once. There are at most `2b` slots, and CMR393
charges at most `t/p^b` returned full-token edges to each. Combine with the
initial-stock inventory CMR390. ∎

## 3. Deep full-token visit bounds

### Corollary CMR395 — PROVED UNDER THE ONE-PASS HYPOTHESIS

1. If
   \[
   p^b>t^{1/3},
   \]
   then
   \[
   \boxed{
   D_\tau^{(2)}
   <
   t^{4/3}+2h\,t^{2/3}.
   }
   \]
2. If
   \[
   p^b\ge t^{2/3},
   \]
   then
   \[
   \boxed{
   D_\tau^{(2)}
   \le
   t^{2/3}+2h\,t^{1/3}.
   }
   \]

### Proof

Use CMR394 and substitute the corresponding lower bound on `p^b`. Also use
`b<=h`. ∎

Thus a single descending prefix pass has a subquadratic—and at the tunable deep
threshold, sublinear up to the initial `t^(2/3)` term—budget for repeated visits
to one exact full token.

## 4. Exact reset-occurrence factorization

For every coarser depth `r<b` and moving layer `ell`, let

\[
A_{\tau,r,\ell}^{(2)}
\]

be the number of old-cell-clean rematchings, after the token is exposed, of the
unique depth-`r` block which can satisfy both CMR393 compatibility conditions.
If no such block exists, put this count equal to zero. Define

\[
A_\tau^{(2)}
=
\sum_{r=0}^{b-1}\sum_{\ell=0}^1
A_{\tau,r,\ell}^{(2)}.
\]

### Theorem CMR396 — PROVED

For an arbitrary number of recursive prefix resets,

\[
\boxed{
I_\tau^{(2),\mathrm{coarse}}
\le
\frac{t}{p^b}A_\tau^{(2)}.
}
\]

Fix `m>=0`. If every compatible ancestor depth-layer slot is rematched at most
`m` times after the token is exposed, then

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

Conversely, failure of either displayed multiplicity bound forces one of the at
most `2b` compatible ancestor slots to be rematched more than `m` times.

### Proof

CMR393 contributes at most `t/p^b` for every counted reset, proving the
factorization. There are `b` coarser depths and at most two moving layers, so
the multiplicity hypothesis gives `A_tau^(2)<=2bm`. Apply CMR390 for the visit
bound. The final statement is the contrapositive. ∎

CMR396 identifies the only unbounded recursive-prefix source exactly: repeated
use of one fixed compatible ancestor slot.

## 5. Aggregate labelled return mass

### Corollary CMR397 — PROVED UNDER THE ONE-PASS HYPOTHESIS

Summing over every nonroot full token in the parent block gives

\[
\boxed{
\sum_{\theta\in\mathbb P^1(\mathbb F_p)}
\sum_{b=1}^{h-1}
\sum_{a,c\bmod p^b}
I_{(b,a,c,\theta)}^{(2),\mathrm{coarse}}
\le
2(p+1)t
\sum_{b=1}^{h-1}b p^b.
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

so the direction-labelled aggregate is `O_p(t^2 log t)`.

### Proof

At depth `b` there are `p^(2b)` prefix pairs `(a,c)` and `p+1` directions.
Multiply this count by the per-token CMR394 bound `2bt/p^b`, obtaining
`2(p+1)bt p^b`. Sum over `b`. Finally,

\[
\sum_{b=1}^{h-1}b p^b
<
h\sum_{b=1}^{h-1}p^b
<
\frac{h t}{p-1}.
\]

∎

This is deliberately a labelled upper bound: one returned edge may be counted
once for every direction. Geometric direction support can only reduce the true
mass.

## 6. Revised frontier

A canonical descending prefix pass cannot freely replenish repeated full
tokens. At cubic depth, one token has total executable endpoint stock at most
`t^(2/3)+O(h t^(1/3))`; globally, all labelled full-token returns in the pass
have `O_p(t^2 log t)` mass. For unrestricted histories, excessive return forces
repeated use of one exact ancestor slot.

The remaining dynamic sources are therefore:

1. a monotone payment for repeated use of that slot;
2. joint-parent or exact-band resets outside the recursive prefix schedule;
3. the width of the fully forced exchange-ancestry branch.

No all-`n` theorem is claimed here. Per-reset capacities, reset multiplicity,
one-pass sums, and depth specializations are checked in
[`scripts/verify_prime_power_full_token_reset_profile.py`](../scripts/verify_prime_power_full_token_reset_profile.py).
