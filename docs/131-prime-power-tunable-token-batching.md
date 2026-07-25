# A tunable carry threshold balances heavy load and token batching

CMR303 uses the square-root threshold because it balances heavy-cell load and
static cell support.  For dynamic reuse, a different balance is useful.  A
threshold near `t^(2/3)` leaves smaller individual line universes, allowing a
batch of order `t^(1/3)` dispersed tokens to be removed simultaneously.

Let

\[
t=p^h
\]

and let `F` be a common first-separation population of `M` thin-blocker events
as in CMR302.  Its separation depth is `b`, and its occupied row-prefix cells
are the tokens at that depth and fixed projective direction.

## 1. Discrete tunable carry split

### Theorem CMR351 — PROVED

Fix an integer threshold

\[
0\le q<h.
\]

At least one of the following holds.

1. **Shallow heavy cell:** if `b<=q`, some occupied token contains at least
   \[
   \boxed{
   \operatorname{ceil}\left(\frac{M}{p^q}\right)
   }
   \]
   events.
2. **Deep dispersion:** if `b>=q+1`, the population occupies more than
   \[
   \boxed{
   \frac{Mp^q}{t}
   }
   \]
   distinct tokens.

### Proof

If `b<=q`, CMR302 gives a cell of size at least `M/p^b>=M/p^q`.  If
`b>=q+1`, CMR302 gives support at least `Mp^b/t>Mp^q/t`. ∎

## 2. Complete line cost of a deep token

### Theorem CMR352 — PROVED

Every token in the deep alternative `b>=q+1` has complete exact Hall-pair line
universe of size at most

\[
\boxed{
W_q(t)=\frac{t^2}{p^{2(q+1)}}.
}
\]

### Proof

CMR347 gives

\[
U(\tau)\le\left(\frac{t}{p^b}\right)^2.
\]

Since `b>=q+1`, this is at most `W_q(t)`. ∎

## 3. Dynamic batch capacity

### Theorem CMR353 — PROVED

Let

\[
J_q(t)
=
\left\lfloor
\frac{(t-2)p^{2(q+1)}}{t^2}
\right\rfloor.
\]

For any collection of at most `J_q(t)` deep tokens, there is a target-specific
parent permutation which moves the designated old endpoint and avoids every
available cell on every exact Hall-pair line from all selected tokens.

### Proof

By CMR352 the total number of distinct lines, even before duplicate removal, is
at most

\[
J_q(t)W_q(t)
\le t-2.
\]

Apply CMR245 to their union. ∎

The same frozen-state trichotomy as CMR350 follows: improvement, anchored
continuation, or a candidate-only replacement line outside the whole selected
batch.

## 4. Cubic-root-balanced specialization

Put

\[
q_*=\left\lceil\frac{2h}{3}\right\rceil-1.
\]

Then

\[
\frac{t^{2/3}}{p}
\le
p^{q_*}
<
t^{2/3}
\]

and

\[
p^{q_*+1}\ge t^{2/3}.
\]

### Corollary CMR354 — PROVED

At the threshold `q_*`, every common-signature population of size `M` has one
of the following alternatives.

1. A carry cell contains more than
   \[
   \boxed{\frac{M}{t^{2/3}}}
   \]
   events.
2. The population occupies more than
   \[
   \boxed{\frac{M}{p\,t^{1/3}}}
   \]
   deep tokens, and every such token has at most
   \[
   \boxed{t^{2/3}}
   \]
   exact Hall-pair lines.

Moreover

\[
\boxed{
J_{q_*}(t)
\ge
\left\lfloor\frac{t-2}{t^{2/3}}\right\rfloor.
}
\]

Thus at least `floor((t-2)/t^(2/3))` selected deep token universes can be
removed simultaneously.

### Proof

The inequalities defining `q_*` give

\[
p^{q_*}<t^{2/3}
\]

for the heavy alternative and

\[
p^{q_*}\ge t^{2/3}/p
\]

for the support alternative in CMR351.  CMR352 and
`p^(q_*+1)>=t^(2/3)` give `U(tau)<=t^(2/3)`.  Substitute the same inequality in
the definition of `J_q`. ∎

For a width-two or width-three blocker, CMR295--CMR296 give

\[
M=\Omega_p\left(\frac{t}{\log t}\right).
\]

The specialization therefore yields, up to constants depending only on `p`,

\[
\boxed{
\text{heavy load }\Omega_p\left(\frac{t^{1/3}}{\log t}\right)
}
\]

or

\[
\boxed{
\text{deep support }\Omega_p\left(\frac{t^{2/3}}{\log t}\right),
\qquad
\text{batch capacity }\Omega(t^{1/3}).
}
\]

## 5. Revised reuse target

The dispersed branch now has a scale of dynamic batching rather than only a
static token count.  The remaining no-return theorem must show that successive
batches cannot recycle their escaped replacement lines through coarser repairs
without paying envelope expansion, exchange ancestry, or the existing
quotient/carry collateral.

No all-`n` theorem is claimed here.  The threshold inequalities and exact batch
capacities are checked in
[`scripts/verify_prime_power_tunable_token_batching.py`](../scripts/verify_prime_power_tunable_token_batching.py).
