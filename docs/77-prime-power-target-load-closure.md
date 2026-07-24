# Target-load descent for global-baseline alternating closure

CMR123--CMR132 leave two bookkeeping issues:

1. a parent state may already have large excess over the fixed baseline;
2. a new padded endpoint board may destroy fewer triples than its number of
   endpoint columns.

Both are resolved by tracking the **target load** `d`, the number of old triples
certified to disappear in every state of the current bank. High baseline excess
is itself supported on cells changed from the baseline and therefore supplies
the same replacement-touching hypergraph used in the low-excess case.

Let `Phi(S)` denote the number of real collinear triples in a finite point set
`S`.

## 1. Exact baseline-difference identity

Fix a saturated baseline state `S_0` and another saturated state `S`. Put

\[
A=S\setminus S_0,
\qquad
X=S\cap S_0.
\]

Thus `A` is the set of currently selected cells which are new relative to the
baseline, while `X` is the unchanged point set.

### Theorem CMR133 — PROVED

The real triples of `S` which are not triples of `S_0` are exactly the real
triples of `S` which touch `A`. Consequently

\[
\Phi(S)-\Phi(X)
\]

is the number of new triples, and

\[
\boxed{
\Phi(S)-\Phi(S_0)
=
\bigl(\Phi(S)-\Phi(X)\bigr)
-
\bigl(\Phi(S_0)-\Phi(X)\bigr).
}
\]

In particular,

\[
\boxed{
\Phi(S)-\Phi(X)
\ge
\Phi(S)-\Phi(S_0).
}
\]

### Proof

A triple selected in both `S` and `S_0` consists of three cells belonging to
`S cap S_0=X`. Conversely every triple of `X` belongs to both states. Hence the
common triple set is exactly the triple set of `X`.

Every triple of `S` outside that common set contains at least one cell of
`S\setminus S_0=A`, and every triple touching `A` is absent from `S_0` because
that cell is absent. Subtracting the two decompositions around `Phi(X)` gives
the identity. The final inequality follows because
`Phi(S_0)-Phi(X)>=0`. ∎

Thus a state with excess `e` over the baseline contains at least `e` new real
triples touching its active difference set.

## 2. Banks with independent board size and target load

Let

\[
S_*=X_*\cup B
\]

be a parent state carrying an endpoint bank on a board of size `m>=4`. Suppose
every state of the bank destroys a fixed family of at least `d>=1` old triples.
Equivalently,

\[
D:=\Phi(S_*)-\Phi(X_*)\ge d.
\]

Keep one fixed global baseline `S_0` and put

\[
e=\Phi(S_*)-\Phi(S_0).
\]

The board size `m` and target load `d` are now separate parameters.

Define, whenever possible,

\[
\tau(d)
=
\max\left\{
 s\ge4:
 24(s-1)^2(3s-2)\le d
\right\}.
\]

The parameter is defined for `d>=2160`.

### Theorem CMR134 — PROVED

Assume `d>=2160` and no state of the current endpoint bank has potential below
`Phi(S_0)`. Then some saturated state in the global-baseline closure exposes a
new alternating endpoint bank with

\[
\text{board size }m'=\tau(d)
\]

and certified target load

\[
\boxed{
 d'\ge
 \left\lceil\frac{\tau(d)}2\right\rceil.
}
\]

Moreover `d'` may be chosen at most `tau(d)`.

### Proof

There are two cases.

**Low parent excess.** Suppose `e<d/2`. CMR123 applies with `D>=d`. Since no
bank state improves the baseline, every bank state `S_pi` satisfies

\[
\Phi(S_\pi)-\Phi(X_*)
\ge
D-e
>
\frac d2.
\]

Choose any bank state and let `H` be its real triples touching the replacement
matching. By the definition of `tau(d)`,

\[
|H|
\ge
12(\tau(d)-1)^2(3\tau(d)-2).
\]

Apply CMR124 and then CMR131. The resulting bank has board size `tau(d)` and
target load at least `ceil(tau(d)/2)`.

**High parent excess.** Suppose `e>=d/2`. Apply CMR133 to the parent state
`S_*`. Its active difference set relative to `S_0` supports at least

\[
\Phi(S_*)-\Phi(S_0)=e\ge d/2
\]

new real triples. Apply CMR124 to this active difference set and then CMR131.
The same next-bank conclusion follows.

In the direct-star and heavy-line alternatives the target load is exactly
`tau(d)`; in the disjoint-triple alternative it is at least
`ceil(tau(d)/2)`. Restricting the certified target family if necessary makes
`d'<=tau(d)`. ∎

No excess branch and no geometric branch is terminal: all of them either
contain a baseline improvement or expose the next bank.

## 3. Cube-root contraction of target load

### Corollary CMR135 — PROVED

Under the hypotheses of CMR134, the next target load may be chosen so that

\[
1\le d'\le\tau(d)
<
\left(\frac d{12}\right)^{1/3}.
\]

Consequently every globally nonimproving alternating closure reaches target
load below `2160` after `O(log log d_0)` expansions.

### Proof

Only the strict upper bound needs proof. For `s=tau(d)>=4`,

\[
s-1\ge\frac s2,
\qquad
3s-2\ge2s.
\]

Therefore

\[
d
\ge
24(s-1)^2(3s-2)
\ge
12s^3.
\]

CMR134 gives `d'<=s`, proving the recurrence. Iterated cube roots reach an
absolute constant after `O(log log d_0)` steps. ∎

## 4. Reduction of every bounded load to one target

The remaining range does not require separate treatment of the values
`2,...,2159`.

### Theorem CMR136 — PROVED

Assume `N>=4`. Let an endpoint bank have board size `m>=4`, certified target
load `1<=d<2160`, and no state improving `S_0`. Then some saturated state in the
closure exposes a four-endpoint alternating bank with target load exactly one.

### Proof

Again split by parent excess `e`.

If `e<d/2`, CMR123 gives every bank state at least

\[
D-e\ge d-e>0
\]

real triples touching its replacement matching. Choose one such triple in any
bank state.

If `e>=d/2`, then `e>0`; since triple counts are integers, `e>=1`. CMR133 gives
at least one new real triple in the parent state touching its active difference
set. Choose one.

In either case, choose one point of the selected triple and note its permutation
layer. Add arbitrary points of that layer until four endpoints have been
selected; this is possible because the layer has `N>=4` points. CMR128 gives an
allowed perfect matching on the four-endpoint board. Every state moves the
chosen point and therefore destroys the selected triple. The resulting board
has size four and target load one. ∎

### Corollary CMR137 — PROVED

Starting from any endpoint bank of board size at least four and target load
`d_0>=1`, if no state in the alternating closure improves the fixed baseline,
then after

\[
O(\log\log d_0)+1
\]

expansions the closure reaches a bank with

\[
\boxed{
\text{board size }4,
\qquad
\text{target load }1.
}
\]

No disjoint-defect ledger, heavy-line ledger, or excess ledger is required.

### Proof

Apply CMR135 while the target load is at least `2160`, then CMR136 once. ∎

## 5. Exact remaining alternating core

The previously stated repeated-charge and bounded-size tasks collapse to one
universal local problem:

> **Four-endpoint one-target core.** Starting from a saturated state and a
> four-endpoint degree-two forbidden board which destroys one specified old
> triple in every allowed state, prove that the global-baseline closure contains
> a strict improvement, or classify a genuine frozen cycle of such boards.

This core is independent of the original star size and of the depth of the
prime-power prefix node. The other unresolved recursive issue is interaction
with fine structures recreated by later coarse prefix repairs.

No all-`n` theorem is claimed here. The baseline-difference identity and the
target-load recurrence are checked in
[`scripts/verify_prime_power_target_load_closure.py`](../scripts/verify_prime_power_target_load_closure.py).
