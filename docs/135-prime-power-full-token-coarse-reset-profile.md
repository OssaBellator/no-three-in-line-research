# Full-prefix tokens inherit the coarse-reset return profile

CMR389--CMR392 sharpen repeated-token accounting by fixing both endpoint
prefix coordinates.  CMR378--CMR384 compute exact row-token return under coarse
prefix resets.  The two results combine directly: one ancestor reset can return
at most one old matching edge for each source column in the fixed full-token
column prefix.

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

old matching edges in `U_\tau^{(2)}`.

It reintroduces none unless both of the following compatibility conditions
hold:

1. the block column residue agrees with `a modulo p^r`;
2. the block row-fibre residue agrees with `c modulo p^r`.

The same upper bound holds in a peeled residual host and for the
coordinate-dual opposite-layer reset.

### Proof

By CMR378, the only edges reintroduced at full-host level are the old matching
edges of the rematched block.  If the block column residue is incompatible with
`a`, it contains no source column of the full token.  If the row fibre is
incompatible with `c`, it contains no target row of the full token.

When both are compatible, exactly

\[
\frac{t/p^r}{p^{b-r}}
=
\frac{t}{p^b}
\]

columns of the block extend the prescribed depth-`b` column residue `a`.  A
matching has one old edge per such source column, so at most `t/p^b` returned
edges can lie in the full-token universe.  A persistent deletion mask can only
reduce the returned set.  The dual statement interchanges the two matching
classes. ∎

Unlike the row-token profile CMR379, equality is not asserted: the old matching
need not send every compatible source column to the prescribed depth-`b` row
prefix.

## 2. One-pass reset budget

Follow the descending one-pass prefix schedule of CMR381.  Let

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
one block whose column prefix can extend `a`.  The row-fibre condition can only
remove that candidate.  Under the one-pass hypothesis, each compatible
block-layer slot is used at most once.  There are at most `2b` slots, and CMR393
charges at most `t/p^b` returned full-token edges to each.  Combine with the
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

Use CMR394 and substitute the corresponding lower bound on `p^b`.  Also use
`b<=h`. ∎

Thus a single descending prefix pass has a subquadratic—and at the tunable deep
threshold, sublinear up to the initial `t^{2/3}` term—budget for repeated visits
to one exact full token.  Unbounded recurrence must come from repeated reuse of
one ancestor slot, joint-parent resets outside the prefix schedule, or the
fully forced exchange-ancestry branch.

No all-`n` theorem is claimed here.  Per-reset capacities, one-pass sums, and
the two depth specializations are checked in
[`scripts/verify_prime_power_full_token_reset_profile.py`](../scripts/verify_prime_power_full_token_reset_profile.py).
