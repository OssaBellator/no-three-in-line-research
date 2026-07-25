# Full-prefix token repetition has a two-dimensional edge inventory

CMR388 reduces a long frozen two-slice closure to candidate walls, secant stars,
executable heavy prefix cells, or repeated visits to one exact absolute full
prefix token. A full token fixes both column and row prefixes, so its edge stock
is quadratically smaller than the row-prefix stock in CMR348.

Let

\[
t=p^h
\]

and fix one inherited parent block, one layer, and one full token

\[
\tau=(b,a,c,\theta),
\qquad
0\le b<h,
\]

where

\[
(a,c)\in(\mathbb Z/p^b\mathbb Z)^2,
\qquad
\theta\in\mathbb P^1(\mathbb F_p).
\]

Put

\[
U_\tau^{(2)}
=
\{(x,y)\in[t]^2:
 x\equiv a\pmod{p^b},
 y\equiv c\pmod{p^b}\}.
\]

## 1. Exact two-dimensional stock

### Theorem CMR389 — PROVED

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

There are `t/p^b` source columns and `t/p^b` rows with the prescribed
prefixes. Their Cartesian product is the token universe. ∎

## 2. Dynamic full-token inventory

Consider available-edge sets `A_0,A_1,\ldots,A_m` inside one fixed envelope
epoch. A full-token endpoint visit consumes one currently available Hall
endpoint edge in `U_\tau^{(2)}` and leaves it absent immediately afterward. Let

\[
I_\tau^{(2)}
=
\sum_{i=1}^m
\left|(A_i\setminus A_{i-1})\cap U_\tau^{(2)}\right|
\]

count later reintroductions with multiplicity.

### Theorem CMR390 — PROVED

If `D_\tau^{(2)}` endpoint visits occur, then

\[
\boxed{
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}+I_\tau^{(2)}.
}
\]

Equivalently,

\[
\boxed{
I_\tau^{(2)}
\ge
D_\tau^{(2)}-\frac{t^2}{p^{2b}}.
}
\]

### Proof

Apply the CMR347 dynamic inventory lemma to `U_\tau^{(2)}` and use CMR389.
Every initial or reintroduced edge pays for at most one subsequent consumption
before it must be introduced again. ∎

## 3. Endpoint, witness, or ancestry

At a repeated token visit, process the certificate as in CMR349: delete a
nonessential Hall endpoint if possible; otherwise delete a nonessential witness;
if every prescribed edge is essential, attach the CMR217 ancestry links.

### Theorem CMR391 — PROVED UNDER THE CMR349 HYPOTHESES

Assume the residual hosts form a deletion pass beginning with no essential
edge, every deletion retains a perfect matching, and every repeated visit is
processed by the preceding rule. Let

\[
J_\tau^{(2)},D_\tau^{(2)},X_\tau^{(2)},F_\tau^{(2)}
\]

be total, endpoint-paid, witness-escape, and fully forced visit counts. Then

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
+I_\tau^{(2)}
+X_\tau^{(2)}
+F_\tau^{(2)}.
}
\]

Every fully forced visit has at most three links to strictly earlier
certificates, and the ancestry graph is acyclic inside the pass.

### Proof

The three cases are exhaustive. CMR390 bounds endpoint-paid visits; CMR217 and
CMR218 give the ancestry assertions. ∎

## 4. Depth-dependent stock bounds

### Corollary CMR392 — PROVED

For every `0\le\alpha\le1`, if

\[
p^b\ge t^\alpha,
\]

then

\[
\boxed{|U_\tau^{(2)}|\le t^{2-2\alpha}.}
\]

In particular:

1. at `p^b>t^{1/3}`, the stock is below `t^{4/3}`;
2. at `p^b\ge t^{2/3}`, the stock is at most `t^{2/3}`.

### Proof

Substitute `p^{2b}\ge t^{2\alpha}` into CMR389. ∎

Thus repetition of one full token is no longer free. After its initial
quadratic-prefix stock is exhausted, every further visit pays a returned exact
cell, an off-token witness deletion, or a strictly earlier ancestry
certificate.

No all-`n` theorem is claimed here. Exact stocks, inventory inequalities, and
threshold specializations are checked in
[`scripts/verify_prime_power_full_token_reintroduction.py`](../scripts/verify_prime_power_full_token_reintroduction.py).
