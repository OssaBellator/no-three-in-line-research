# Acyclic depth transfers and finite private resources are off-diagonal

CMR1470--CMR1485 give every exact-displacement obstruction two compatible
currencies.

1. Weighted carry routing sends it to strict internal scaling, an earlier exit
   depth, depth zero, or reuse of one absolute token.
2. Private-path extraction supplies endpoint-disjoint residual supports and a
   linear blocker cost.

The remaining question is which of these currencies really belongs to a
same-owner diagonal block.  This chapter proves that strict scaling, strict
depth handoff, first use of a private residual edge, and first use of an
absolute token are all acyclic.  Arbitrarily large finite collateral on those
arcs affects only rational Lyapunov scaling.  It does not affect the spectral
radius.

Only recurrent states which preserve structural owner, envelope side, depth,
residual mask and token inventory remain diagonal.

Retain one extension-free response graph

\[
H_e=K_{d,d}\setminus(O\cup\{e\}),
\]

where `O` is a perfect matching and `e notin O`.  Retain one CMR1479 private
matching `M` of endpoint-disjoint translated pairs.  Its pair weights satisfy

\[
0<w(a,b)\le1.
\]

For one pair let `J(a,b)` be its CMR1480 residual support.

## 1. Existing reserve or fresh private support

Let `F subseteq E(H_e)` be the current monotone residual mask and put

\[
\mu_M=\sum_{(a,b)\in M}w(a,b).
\]

Define the currently unhit private mass by

\[
u_F=
\sum_{\substack{(a,b)\in M\\J(a,b)\cap F=\varnothing}}
w(a,b).
\]

### Theorem CMR1486 -- PROVED

The hit private mass is at most `|F|`, and therefore

\[
\boxed{
u_F\ge\mu_M-|F|.}
\]

Consequently

\[
\boxed{\max\{|F|,u_F\}\ge\frac{\mu_M}{2}.}
\]

If a monotone extension `F' superset F` meets every support which was unhit by
`F`, then

\[
\boxed{
|F'\setminus F|\ge
\#\{(a,b)\in M:J(a,b)\cap F=\varnothing\}
\ge\lceil u_F\rceil.}
\]

### Proof

The supports in the private matching are nonempty and pairwise disjoint by
CMR1480.  One edge of `F` can therefore hit at most one pair.  Every pair has
weight at most one, so the total hit mass is at most `|F|`.  Subtract from
`mu_M`.

The maximum bound follows from

\[
\mu_M\le |F|+u_F.
\]

Every support unhit by `F` needs one edge of `F'\setminus F`, and disjoint
supports need distinct new edges.  The number of unhit supports is at least
the ceiling of their total weight. ∎

This is the exact private-reserve dichotomy: either the current host has
already spent comparable residual capacity, or a comparable private mass
remains outside the mask and costs fresh edges to neutralise through this
route.

## 2. Quantitative routed reserve payment

Let a routed displacement branch have copy mass `m`.  CMR1479 extracts private
mass at least `m/2`.

### Theorem CMR1487 -- PROVED

For every current residual mask `F`, a routed branch of mass `m` satisfies

\[
\boxed{\max\{|F|,u_F\}\ge\frac m4.}
\]

For the CMR1469 mass

\[
M_0=
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)},
\]

the three CMR1475 branches therefore give, respectively,

\[
\boxed{
\max\{|F|,u_F\}
\ge
\frac{M_0}{8p^{2s}},
}
\]

\[
\boxed{
\max\{|F|,u_F\}
\ge
\frac{M_0}{8sp^{2s}}
}
\qquad(s\ge1),
\]

and

\[
\boxed{\max\{|F|,u_F\}\ge\frac{M_0}{4}}
\]

in the depth-zero branch.

### Proof

Apply CMR1486 to private mass at least `m/2`, then insert the three branch-mass
bounds of CMR1475. ∎

## 3. Finite monotone residual-edge stock

### Theorem CMR1488 -- PROVED

The response host has exactly

\[
\boxed{|E(H_e)|=d^2-d-1}
\]

edges.

Inside one monotone-mask owner epoch, suppose private-support neutralisation
episodes require fresh additions `q_1,...,q_r`.  Then

\[
\boxed{\sum_{j=1}^r q_j\le d^2-d-1.}
\]

In particular, episodes which each require at least `q>0` fresh residual edges
occur at most

\[
\boxed{\left\lfloor\frac{d^2-d-1}{q}\right\rfloor}
\]

times before the process must use an already masked support, change owner
stage, or take another structural branch.

### Proof

`K_{d,d}` has `d^2` edges.  The opposite matching removes `d`, and the target
edge is distinct from it.  This proves the host count.

A monotone mask adds each host edge at most once.  CMR1486 assigns distinct
new edges to all fresh private supports in one episode.  Sum over episodes. ∎

No claim is made for a nonmonotone resampling history; such a history belongs
to the existing return and ancestry ledgers.

## 4. Fresh absolute tokens or repeated tokens

Assume first-separation depth `s>=1`.  CMR1476 gives exactly `p^(2s)` absolute
full-cell tokens for fixed structural owner, layer, direction and displacement.
Let `A` be the set of tokens occupied by one private translated bank, and let
`U` be the set already used in the current token epoch.

### Theorem CMR1489 -- PROVED

Put

\[
R=|A|,
\qquad
R_{\rm new}=|A\setminus U|.
\]

Then

\[
\boxed{R\le |U|+R_{\rm new},}
\]

and hence

\[
\boxed{
\max\{|U|,R_{\rm new}\}\ge\left\lceil\frac R2\right\rceil.}
\]

Across a monotone token epoch, strictly fresh token uses total at most
`p^(2s)`.

### Proof

Every occupied token is either already in `U` or fresh.  The reused occupied
tokens form a subset of `U`.  This gives the first inequality and the
half-alternative.  A monotone used-token set can acquire each of the
`p^(2s)` labels only once. ∎

### Theorem CMR1490 -- PROVED

Apply CMR1483 to a private matching of size `Q`.

1. In the heavy branch, one absolute token contains at least
   `ceil(sqrt(Q))` private identical-displacement pairs.
2. In the dispersed branch, let
   \[
   R\ge\lfloor\sqrt Q\rfloor
   \]
   be the number of token-disjoint witnesses.  Then either at least
   `ceil(R/2)` of those tokens are fresh or the epoch has already used at least
   `ceil(R/2)` absolute tokens.

Thus a nonroot private bank either enters one heavy/repeated-token core or
pays a monotone finite token resource.

### Proof

The heavy/dispersed alternative is CMR1483.  Apply CMR1489 in the dispersed
branch. ∎

## 5. The augmented transfer graph is acyclic

Let a refined same-owner state record

\[
\xi=(\omega,k,s,U,F),
\]

where:

- `omega` is the structural owner stage;
- `p^k` is the current envelope side;
- `s` is the active first-separation or exit depth;
- `U` is the monotone absolute-token set;
- `F` is the monotone residual mask.

Choose a topological rank `r(omega)` from CMR1321.  Order refined states
lexicographically by

\[
\boxed{
\bigl(r(\omega),-k,-s,|U|,|F|\bigr).
}
\]

### Theorem CMR1491 -- PROVED

Every one of the following transitions is strict in this order.

1. A structural owner, wall, routing or envelope exit.
2. CMR1474 internal scaling from exponent `k` to `k-s<k`.
3. CMR1473 handoff from depth `s` to one earlier depth `c<s`.
4. First use of one absolute token.
5. First addition of one private residual edge.

Therefore these transitions form a finite directed acyclic graph.  A
transition can remain in one diagonal class only when it preserves owner,
envelope exponent, depth, used-token set and residual mask.

### Proof

The first transition increases `r(omega)`.  Internal scaling strictly decreases
`k`, so `-k` increases.  Earlier-depth handoff strictly decreases `s`, so `-s`
increases.  A fresh token or edge strictly increases the cardinality of a
monotone set.  Earlier coordinates are unchanged in each corresponding case.
The state stock is finite. ∎

The theorem concerns the exact charging/response graph.  It does not claim
that merely identifying a branch executes it; a policy must choose the stated
canonical transfer or resource payment.

## 6. Spectral reduction and constructive rational weights

Partition an exact finite offspring upper quotient by the strongly recurrent
classes of the CMR1491 graph.  Let `A_ii` be its diagonal core blocks and let
all strict transfer/resource entries form blocks above the diagonal.

### Theorem CMR1492 -- PROVED

The refined quotient is block upper triangular and

\[
\boxed{\rho(A)=\max_i\rho(A_{ii}).}
\]

Suppose every recurrent core has a positive rational certificate

\[
A_{ii}v_i\le v_i-s_i,
\qquad s_i>0.
\]

Then all strict scaling, earlier-depth, fresh-token and fresh-edge collateral
glues into one positive rational certificate `Av<v`, regardless of its finite
size.

### Proof

CMR1491 supplies a topological order.  Apply CMR1322--CMR1324 to the resulting
finite block upper triangular matrix. ∎

Thus strict transfer weights do not require a new diagonal contraction
estimate.  They require only finite rational scaling after the recurrent
cores are certified.

## 7. Revised regime endpoint

### Corollary CMR1493 -- PROVED

The current same-owner spectral problem separates exactly as follows.

1. **Nonroot prime-power transfers.**  Strict internal scaling, earlier-depth
   handoff, fresh private-edge payment and fresh-token payment are off-diagonal.
2. **Prime-field envelopes.**  When `k=1`, the only possible separation depth is
   `s=0`; there is no hidden nonroot depth-transfer block.
3. **Recurrent cores.**  The remaining numerical blocks are parent-scale
   depth-zero translation, repeated absolute-token or reused-edge states, and
   the alternative one-owner loaded-line states.
4. **Global gluing.**  Once those recurrent blocks and the thin residual blocks
   have rational certificates, CMR1492 and the structural owner DAG glue all
   prime-power transfer states.  Balanced/CRT assembly remains a later
   geometric interface step.

No all-`n` theorem is claimed.  The advance is that strict depth transfer and
first-use private resources are no longer independent diagonal frontiers.

Private-reserve inequalities, exact host stock, monotone mask and token
budgets, transfer ordering and constructive rational gluing are checked in
[`scripts/verify_prime_power_transfer_resource_triangularity.py`](../scripts/verify_prime_power_transfer_resource_triangularity.py).
