# Deep dispersed tokens have simultaneously avoidable line universes

CMR344--CMR346 show that fresh dispersed carry tokens have a finite packing
budget, but leave open the possibility that one exact token is revisited many
times.  In the dispersed regime the complete real-line universe of one token is
small.  In fact, any `p-1` such token universes can be forbidden simultaneously
by the target-specific Hall theorem CMR245.  Thus recurrence of one deep token
is not a local terminal obstruction.

Let

\[
t=p^h
\]

with `p` an odd prime.  Fix two distinct source slices `x_1,x_2`, put

\[
d=x_2-x_1,
\qquad
r=v_p(d),
\]

and fix a Hall-pair token

\[
\tau=(b,c,\theta)
\]

as in CMR344, with the source slices, layer, and parent block understood.  Thus
both endpoint rows are congruent to `c modulo p^b`, their exact first-separation
depth is `b`, and their reduced projective direction is `theta`.

Put

\[
T=\frac{t}{p^b}.
\]

Every row in the residue class `c modulo p^b` is uniquely `c+p^b A` with
`0<=A<T`.

## 1. Exact endpoint-line universe of one token

### Theorem CMR347 — PROVED

The number `U(tau)` of compatible exact Hall endpoint pairs, equivalently real
nonaxis lines, belonging to one token is as follows.

1. If `b<r`, necessarily `theta=[0:1]`, and
   \[
   \boxed{
   U(\tau)=T^2\left(1-\frac{1}{p}\right).
   }
   \]
2. If `b=r` and
   \[
   \theta=[1:s],
   \]
   write
   \[
   \delta\equiv d/p^b\pmod p.
   \]
   If `s` is nonzero, then
   \[
   \boxed{U(\tau)=\frac{T^2}{p}.}
   \]
   If `s=0`, then
   \[
   \boxed{U(\tau)=T\left(\frac{T}{p}-1\right).}
   \]

In every case

\[
\boxed{U(\tau)\le T^2.}
\]

### Proof

Write the endpoint rows as

\[
a=c+p^b A,
\qquad
q=c+p^b B,
\qquad
0\le A,B<T.
\]

If `b<r`, exact first separation at depth `b` means that `B-A` is a unit modulo
`p`.  For every `A`, exactly `T-T/p` values of `B` have a different residue
modulo `p`.  This gives the first formula.

Now let `b=r`.  The projective condition is

\[
B-A\equiv s\delta\pmod p.
\]

For nonzero `s`, every `A` has exactly `T/p` possible values of `B`.  For `s=0`,
there are `T/p` values in the same residue class, but `B=A` is incompatible with
a matching pair and must be removed.  This gives the remaining formulas.

A nonvertical real line meets each of the two fixed source slices in at most one
cell.  Hence an exact endpoint pair and its real line determine each other. ∎

## 2. Deep tokens have at most `t/p` lines

### Corollary CMR348 — PROVED

Assume the token is in the dispersed half of CMR303:

\[
p^b>\sqrt t.
\]

Then

\[
\boxed{U(\tau)\le\frac{t}{p}.}
\]

### Proof

Because `t=p^h` and `p^b` is an integral power of `p`, the strict inequality
`p^b>sqrt(t)` implies

\[
2b\ge h+1.
\]

Therefore

\[
T^2=p^{2h-2b}\le p^{h-1}=\frac{t}{p}.
\]

Apply CMR347. ∎

## 3. Simultaneous elimination of `p-1` recurrent tokens

### Theorem CMR349 — PROVED

Let `tau_1,...,tau_j` be deep dispersed tokens for the same inherited parent
block and designated old target endpoint, where

\[
1\le j\le p-1.
\]

Let `mathcal L(tau_i)` be the complete set of exact real Hall-pair lines in
`tau_i`.  Then there is a target-specific parent permutation which moves the
old target endpoint and avoids every available cell on every line in

\[
\bigcup_{i=1}^j\mathcal L(\tau_i).
\]

### Proof

After duplicate lines are removed, CMR348 gives at most

\[
\sum_{i=1}^j U(\tau_i)
\le
\frac{jt}{p}
\le
\frac{(p-1)t}{p}
=
t-\frac{t}{p}
\]

forbidden nonaxis lines.  Since the parent block is nontrivial, `t>=p`; in the
prime-power applications with a deep token one has `h>=2`, hence `t/p>=p>=3`.
Thus the line count is at most `t-3`, and in particular at most `t-2`.
CMR245 supplies the required target-specific perfect matching. ∎

## 4. Frozen-state token escape

### Corollary CMR350 — PROVED

In a globally minimal positive-potential inherited parent state, fix at most
`p-1` deep dispersed tokens.  There is a target-specific state which destroys
the selected old target and contains no candidate cell on any Hall-pair line
from those tokens.  Consequently at least one of the following holds.

1. The state strictly lowers the global potential.
2. A required replacement certificate is anchored and opens the existing
   alternating continuation.
3. Every candidate-only replacement certificate lies on a real line outside all
   selected token universes.

### Proof

Choose the state from CMR349.  It destroys the old target endpoint.  Global
minimality requires a replacement certificate unless the state improves.  An
anchored certificate gives the second outcome.  A candidate-only certificate
cannot lie on one of the selected token lines because every available cell of
those lines was forbidden. ∎

## 5. Revised dispersed-token endpoint

The temporal pigeonhole in CMR345 no longer ends at anonymous reuse.  Repeated
visits to one deep token expose a complete line universe of size at most `t/p`,
and up to `p-1` such universes are simultaneously removable while the target is
moved.  A frozen continuation must therefore exit the selected token batch,
open an anchored bank, or improve.

This is a one-step and one-batch no-return theorem.  It does not yet prove that
successive batches cannot revisit earlier tokens after coarser repairs.  The
remaining dynamic task is to combine CMR350 with closure-envelope ancestry and
the coarse-to-fine recreation budget.

No all-`n` theorem is claimed here.  Exact token-universe counts and the deep
batch inequality are checked in
[`scripts/verify_prime_power_dispersed_token_universe.py`](../scripts/verify_prime_power_dispersed_token_universe.py).
