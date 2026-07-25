# Repeated carry tokens are paid by edge reintroduction or exchange ancestry

CMR344--CMR346 show that fresh dispersed carry tokens have a finite static
budget. Static token counting alone does not give a no-return theorem: two
old-cell-clean complete rematchings can return a permutation layer exactly to
its starting state. The correct dynamic quantity is therefore not the number
of token names, but the number of candidate edges available under one token,
plus the number of times deleted token edges are later reintroduced.

This chapter gives that exact inventory identity. It also separates a repeated
thin-token visit into three outcomes: a token-endpoint deletion paid by the
inventory, an off-token witness deletion, or a fully forced certificate with a
CMR217 ancestry link.

Let

\[
t=p^h
\]

and fix one inherited parent block and one permutation layer. Fix an absolute
row-prefix direction token

\[
\tau=(b,c,\theta),
\qquad
0\le b<h,
\qquad
c\in\mathbb Z/p^b\mathbb Z.
\]

The direction `theta` labels the thin certificate. For the edge inventory, put

\[
U_\tau
=
\{(x,y)\in [t]^2:y\equiv c\pmod{p^b}\}.
\]

Thus every Hall endpoint of a thin event assigned to `tau` lies in `U_tau`.
The direction is retained in the certificate label even though it does not
shrink the ambient endpoint stock.

## 1. Dynamic edge-inventory lemma

### Theorem CMR347 — PROVED

Let `A_0,A_1,...,A_m` be available-edge sets inside a finite universe `U`.
Some transitions are **visits**: at a visit one chosen edge

\[
e_i\in A_{i-1}\cap U
\]

is consumed, and the next set does not contain `e_i`. Other transitions may
delete arbitrary edges or reintroduce edges. Count reintroductions with
multiplicity:

\[
I_U
=
\sum_{i=1}^m
\left|(A_i\setminus A_{i-1})\cap U\right|.
\]

If `D_U` visits consume edges of `U`, then

\[
\boxed{
D_U
\le
|A_0\cap U|+I_U.
}
\]

Equivalently,

\[
\boxed{
I_U
\ge
D_U-|A_0\cap U|.
}
\]

### Proof

Give every edge of \(A_0\cap U\) one initial token. Every reintroduction of an
edge of `U` creates one additional token. A visit consumes one currently
present edge and hence consumes one token. An edge cannot be consumed again
until it has been reintroduced, so no token can pay twice. Therefore the
number of visits is at most the initial stock plus the reintroduction stock. ∎

The statement permits arbitrary host resets. Their only relevant contribution
is the number of \(0\to1\) edge returns inside `U`.

## 2. Exact stock under one row-prefix token

### Theorem CMR348 — PROVED

For the token `tau` above,

\[
\boxed{
|U_\tau|
=
\frac{t^2}{p^b}.
}
\]

Consequently every initial residual host `H` satisfies

\[
\boxed{
|E(H)\cap U_\tau|
\le
\frac{t^2}{p^b}.
}
\]

### Proof

There are exactly `t/p^b` rows congruent to `c modulo p^b`, and every such row
has `t` possible columns. A residual host is a subset of the full candidate
board. ∎

Combining CMR347 and CMR348, `D_tau` token-endpoint deletions obey

\[
\boxed{
D_\tau
\le
\frac{t^2}{p^b}+I_\tau,
}
\]

where `I_tau` counts reintroductions of candidate cells in `U_tau`.

## 3. Endpoint, witness, or ancestry

Consider a certificate-directed residual-host process. At a visit assigned to
`tau`, the certificate contains two Hall endpoint edges in `U_tau` and at most
one further witness edge. Classify the visit as follows.

1. **Token-paid.** At least one Hall endpoint is nonessential; delete such an
   endpoint while retaining a perfect matching.
2. **Witness escape.** Both Hall endpoints are essential, but another prescribed
   edge is nonessential; delete that off-token edge.
3. **Fully forced.** Every prescribed edge is essential; apply CMR217.

### Theorem CMR349 — PROVED UNDER HYPOTHESES

Assume the residual hosts form a CMR215--CMR218 deletion pass beginning at a
host with no essential edge, every deletion retains a perfect matching, and
every repeated `tau`-visit is processed by the preceding rule. Let
`J_tau,D_tau,X_tau,F_tau` be respectively the total, token-paid, witness-escape,
and fully forced visit counts. Then

\[
J_\tau=D_\tau+X_\tau+F_\tau
\]

and

\[
\boxed{
J_\tau
\le
\frac{t^2}{p^b}
+I_\tau
+X_\tau
+F_\tau.
}
\]

Every fully forced visit has at most three directed ancestry links to strictly
earlier peeled certificates, and those links are acyclic inside the deletion
pass.

### Proof

The three cases are exhaustive. CMR347--CMR348 bound `D_tau`. CMR217 gives at
most one ancestry link for each prescribed edge of a rank-`1/2/3` fully forced
certificate, and CMR218 gives acyclicity. ∎

Thus a long repeated-token history has a precise payment decomposition. After
the initial `t^2/p^b` endpoint stock is exhausted, every further visit is paid
by

- a returned token-compatible candidate edge;
- an off-token witness deletion; or
- a fully forced ancestry certificate.

This does not yet bound those three dynamic terms, but it removes uncharged
fresh-token repetition from the fixed-envelope problem.

## 4. Static token monotonicity is false

### Theorem CMR350 — PROVED; STATIC NO-RETURN CLAIM REFUTED

For every block size `t>=2` and every permutation layer `f`, there is a second
permutation layer `g` such that

1. `f` and `g` use no common cell;
2. the complete rematching `f to g` moves every old point;
3. the complete rematching `g to f` also moves every old point; and
4. after the two steps, every occupied cell, carry token, and geometric
   certificate determined by the layer is restored exactly.

### Proof

Choose any derangement `sigma` of `[t]` and put

\[
g=f\circ\sigma.
\]

Since `sigma(x) != x` and `f` is injective,

\[
g(x)=f(\sigma(x))\ne f(x)
\]

for every row `x`; hence the first rematching is old-cell-clean. The inverse
`sigma^{-1}` is also a derangement, and composing `g` with `sigma^{-1}` returns
`f`, again moving every current point. The final occupied cell set is exactly
the initial one, so every state-only token statistic is restored. ∎

Therefore CMR344 cannot be promoted to a global monotone potential by declaring
a token permanently spent after its first use. The reintroduction term in
CMR347 is necessary, not an artefact of the proof.

## 5. Revised frontier

Inside one monotone deletion pass, token-paid repetition is finite and CMR218
prevents circular forced ancestry. Across rematching resets, exact two-cycles
show that neither property alone gives termination. The next theorem must
control at least one of the following quantities:

1. token-edge reintroduction mass `I_tau`, charged to the coarse repair that
   restores the edge;
2. witness-escape mass `X_tau`, routed through the CMR310--CMR342 closest-pair
   and prefix-bank classification; or
3. the width of the fully forced CMR217 ancestry DAG.

A successful coarse-to-fine recreation estimate would bound the first term and
simultaneously address the repeated-token and recreated-fine-star bottlenecks.

No all-`n` theorem is claimed here. Exact prefix stocks, the dynamic inventory
inequality, the forced-or-paid arithmetic, and the universal two-step return are
checked in
[`scripts/verify_prime_power_token_reintroduction_ledger.py`](../scripts/verify_prime_power_token_reintroduction_ledger.py).
