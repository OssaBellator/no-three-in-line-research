# Full-prefix token repetition has a two-dimensional edge inventory

CMR381 reduces a long frozen two-slice closure to candidate walls, secant stars,
executable heavy prefix cells, or repeated visits to one exact absolute full
prefix token.  CMR347 gives the correct dynamic accounting principle for
repeated row-prefix tokens.  The full token exposed by CMR357 is sharper: it
fixes both a column prefix and a row prefix, so its candidate-edge stock is
quadratically smaller.

Let

\[
t=p^h
\]

and fix one inherited parent block, one permutation layer, and one full prefix
token

\[
\tau=(b,a,c,\theta),
\qquad
0\le b<h,
\]

where

\[
(a,c)\in
(\mathbb Z/p^b\mathbb Z)^2,
\qquad
\theta\in\mathbb P^1(\mathbb F_p).
\]

For the edge inventory, put

\[
U_\tau^{(2)}
=
\{(x,y)\in[t]^2:
 x\equiv a\pmod{p^b},
 y\equiv c\pmod{p^b}\}.
\]

The direction remains part of the certificate label, although it does not
further shrink the ambient cell stock.

## 1. Exact two-dimensional stock

### Theorem CMR382 — PROVED

The full-token universe has exact size

\[
\boxed{
|U_\tau^{(2)}|
=
\left(\frac{t}{p^b}\right)^2
=
\frac{t^2}{p^{2b}}.
}
\]

Consequently every residual matching host `H` satisfies

\[
\boxed{
|E(H)\cap U_\tau^{(2)}|
\le
\frac{t^2}{p^{2b}}.
}
\]

### Proof

There are exactly `t/p^b` source columns in the prescribed column residue and
`t/p^b` rows in the prescribed row residue.  Their Cartesian product is the
full token universe, and a residual host is a subset of it. ∎

This improves the row-prefix stock `t^2/p^b` from CMR348 by an additional
factor `p^b`.

## 2. Dynamic full-token inventory

Consider an arbitrary sequence of available-edge sets

\[
A_0,A_1,\ldots,A_m
\]

inside one fixed closure-envelope epoch.  A **full-token endpoint visit** is a
step which consumes one currently available Hall endpoint edge from
`U_\tau^{(2)}` and leaves that exact edge absent immediately afterward.  Count
all later reintroductions into the token universe with multiplicity:

\[
I_\tau^{(2)}
=
\sum_{i=1}^m
\left|
(A_i\setminus A_{i-1})
\cap U_\tau^{(2)}
\right|.
\]

### Theorem CMR383 — PROVED

If `D_\tau^{(2)}` full-token endpoint visits occur, then

\[
\boxed{
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}
+
I_\tau^{(2)}.
}
\]

Equivalently,

\[
\boxed{
I_\tau^{(2)}
\ge
D_\tau^{(2)}-
\frac{t^2}{p^{2b}}.
}
\]

### Proof

Apply the dynamic inventory lemma CMR347 with universe
`U=U_\tau^{(2)}` and use the exact initial-stock bound from CMR382.  Every
initial edge and every reintroduced edge can pay for at most one subsequent
consumption before it must be introduced again. ∎

The statement allows arbitrary complete rematching resets.  Such a reset is
charged exactly by the number of token-compatible cells it returns.

## 3. Endpoint, witness, or ancestry at full-token resolution

At a repeated visit assigned to `\tau`, the relevant certificate contains two
Hall endpoint edges in `U_\tau^{(2)}` and at most one further witness edge.
Process it by the same rule as CMR349:

1. if a Hall endpoint is nonessential, delete such an endpoint;
2. if both Hall endpoints are essential but another prescribed edge is
   nonessential, delete that witness edge;
3. if every prescribed edge is essential, attach the CMR217 ancestry links.

### Theorem CMR384 — PROVED UNDER THE CMR349 HYPOTHESES

Assume the residual hosts form a deletion pass beginning with no essential
edge, every deletion retains a perfect matching, and every repeated
`\tau`-visit is processed by the preceding rule.  Let

\[
J_\tau^{(2)},
D_\tau^{(2)},
X_\tau^{(2)},
F_\tau^{(2)}
\]

be respectively the total, token-endpoint, witness-escape, and fully forced
visit counts.  Then

\[
J_\tau^{(2)}
=
D_\tau^{(2)}+X_\tau^{(2)}+F_\tau^{(2)}
\]

and

\[
\boxed{
J_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}
+
I_\tau^{(2)}
+
X_\tau^{(2)}
+
F_\tau^{(2)}.
}
\]

Every fully forced visit has at most three directed ancestry links to strictly
earlier certificates, and the ancestry graph is acyclic within the pass.

### Proof

The three processing cases are exhaustive.  CMR383 bounds the endpoint-paid
visits.  CMR217 supplies at most one ancestry link per prescribed edge and
CMR218 supplies acyclicity. ∎

Thus repetition of one exact full token is no longer free even before a global
coarse-to-fine estimate is available.  After its initial two-dimensional edge
stock is exhausted, every further visit pays a returned exact cell, an
off-token witness deletion, or a strictly earlier ancestry certificate.

## 4. Depth-dependent stock bounds

### Corollary CMR385 — PROVED

For every real `alpha` with `0<=alpha<=1`, if

\[
p^b\ge t^\alpha,
\]

then

\[
\boxed{
|U_\tau^{(2)}|
\le
 t^{2-2\alpha}.
}
\]

In particular:

1. at the cubic-root full-cell threshold `p^b>t^{1/3}` from CMR358,
   \[
   |U_\tau^{(2)}|<t^{4/3};
   \]
2. at the tunable deep threshold `p^b\ge t^{2/3}` used by CMR371,
   \[
   |U_\tau^{(2)}|\le t^{2/3}.
   \]

### Proof

Substitute `p^{2b}\ge t^{2\alpha}` into CMR382. ∎

The remaining dynamic theorem is now precisely quantitative: bound the
full-token reintroduction mass `I_\tau^{(2)}`, the witness-escape mass, or the
width of the acyclic forced-ancestry DAG across successive band and prefix
repairs.  The same estimate would pay the fine structures recreated by later
coarse moves.

No all-`n` theorem is claimed here.  Exact full-token stocks, inventory
inequalities, and threshold specializations are checked in
[`scripts/verify_prime_power_full_token_reintroduction.py`](../scripts/verify_prime_power_full_token_reintroduction.py).
