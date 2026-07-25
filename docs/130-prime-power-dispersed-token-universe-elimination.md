# Deep dispersed tokens have simultaneously avoidable line universes

CMR344–CMR346 give a finite packing budget for fresh dispersed tokens, while
CMR347–CMR350 show that static token monotonicity is false and introduce the
necessary edge-reintroduction ledger. The present chapter gives a complementary
one-step fact: in the dispersed regime, the complete real-line universe of one
fixed Hall-pair token is small, and a bounded batch of such universes can be
forbidden simultaneously by CMR245.

Let

\[
t=p^h
\]

with `p` an odd prime. Fix source slices `x_1,x_2`, put

\[
d=x_2-x_1,
\qquad
r=v_p(d),
\]

and fix a Hall-pair token

\[
\tau=(b,c,\theta)
\]

with source slices, layer, and parent block understood. Both endpoint rows are
congruent to `c\pmod{p^b}`, their exact first-separation depth is `b`, and their
reduced projective direction is `\theta`. Put

\[
T=\frac{t}{p^b}.
\]

## 1. Exact endpoint-line universe

### Theorem CMR364 — PROVED

Let `U(\tau)` be the number of compatible exact Hall endpoint pairs—or,
equivalently, their distinct real nonaxis lines—in one token.

1. If `b<r`, then `\theta=[0:1]` and
   \[
   \boxed{U(\tau)=T^2\left(1-\frac1p\right).}
   \]
2. If `b=r` and `\theta=[1:s]`, then
   \[
   \boxed{U(\tau)=\frac{T^2}{p}}
   \]
   for `s\ne0`, while
   \[
   \boxed{U(\tau)=T\left(\frac{T}{p}-1\right)}
   \]
   for `s=0`.

In every case,

\[
\boxed{U(\tau)\le T^2.}
\]

### Proof

Write endpoint rows as

\[
a=c+p^bA,
\qquad
q=c+p^bB,
\qquad
0\le A,B<T.
\]

If `b<r`, exact first separation requires `B-A` to be a unit modulo `p`.
For each `A`, exactly `T-T/p` choices of `B` have another residue modulo `p`.

If `b=r`, write `\delta\equiv d/p^b\pmod p`. The projective condition is

\[
B-A\equiv s\delta\pmod p.
\]

For `s\ne0`, each `A` has exactly `T/p` choices. For `s=0`, there are `T/p`
choices in the same residue class, but `B=A` is incompatible and is removed.
Finally, a nonvertical line meets the two fixed slices in one cell each, so the
endpoint pair determines the real line uniquely. ∎

## 2. Deep-token line bound

### Corollary CMR365 — PROVED

If

\[
p^b>\sqrt t,
\]

then

\[
\boxed{U(\tau)\le\frac{t}{p}.}
\]

### Proof

Since `t=p^h`, the strict inequality implies `2b\ge h+1`. Hence

\[
T^2=p^{2h-2b}\le p^{h-1}=\frac{t}{p}.
\]

Apply CMR364. ∎

## 3. Simultaneous elimination of deep token universes

### Theorem CMR366 — PROVED

Let `\tau_1,\ldots,\tau_j` be deep dispersed tokens for the same inherited
parent block and designated target endpoint, with

\[
1\le j\le p-1.
\]

There is a target-specific parent permutation which moves the old endpoint and
avoids every available cell on every exact Hall-pair line belonging to the
selected tokens.

### Proof

After duplicate lines are removed, CMR365 bounds the union by

\[
\sum_{i=1}^jU(\tau_i)
\le\frac{jt}{p}
\le t-\frac{t}{p}.
\]

A deep token requires `h\ge2`, so `t/p\ge p\ge3`. Thus at most `t-3` lines are
forbidden. CMR245 applies. ∎

## 4. Frozen-state escape

### Corollary CMR367 — PROVED

In a globally minimal positive-potential inherited state, select at most `p-1`
deep tokens. A target-specific state exists which destroys the old target and
uses no candidate cell on any selected token line. Therefore at least one of
the following holds:

1. the state strictly lowers the potential;
2. an anchored replacement certificate opens the existing alternating
   continuation;
3. every candidate-only replacement certificate lies outside all selected token
   universes.

### Proof

Use CMR366. Global minimality requires a replacement certificate unless the
state improves. An anchored certificate gives the second outcome; a
candidate-only certificate cannot lie on a forbidden token line. ∎

This is a one-step, one-batch no-return statement. It does not contradict the
CMR350 two-step return example: a later coarse rematching can reintroduce the
forbidden token edges, and that return is paid by the CMR347 edge inventory.
The remaining dynamic task is to charge such reintroductions and later
coarse-to-fine recreation.

No all-`n` theorem is claimed here. Exact token-universe counts and the deep
batch inequality are checked in
[`scripts/verify_prime_power_dispersed_token_universe.py`](../scripts/verify_prime_power_dispersed_token_universe.py).
