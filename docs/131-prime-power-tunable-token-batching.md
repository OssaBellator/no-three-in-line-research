# A tunable carry threshold balances heavy load and token batching

CMR303 uses a square-root threshold to balance heavy-cell load and static
support. Dynamic reuse benefits from a tunable threshold: making the deep
region smaller reduces each token's complete line universe and permits larger
simultaneous batches.

Let

\[
t=p^h
\]

and let `\mathcal F` be a common first-separation population of `M` thin-blocker
events as in CMR302. Its separation depth is `b`.

## 1. Discrete tunable split

### Theorem CMR368 — PROVED

Fix an integer `q` with

\[
0\le q<h.
\]

At least one of the following holds.

1. If `b\le q`, some token contains at least
   \[
   \boxed{
   \operatorname{ceil}\left(\frac{M}{p^q}\right)
   }
   \]
   events.
2. If `b\ge q+1`, the population occupies more than
   \[
   \boxed{\frac{Mp^q}{t}}
   \]
   distinct tokens.

### Proof

If `b\le q`, CMR302 gives load at least `M/p^b\ge M/p^q`. If
`b\ge q+1`, its support bound gives more than `Mp^q/t` occupied tokens. ∎

## 2. Deep-token line cost

### Theorem CMR369 — PROVED

Every token in the deep alternative `b\ge q+1` has complete exact Hall-pair
line universe of size at most

\[
\boxed{
W_q(t)=\frac{t^2}{p^{2(q+1)}}.
}
\]

### Proof

CMR364 gives

\[
U(\tau)\le\left(\frac{t}{p^b}\right)^2.
\]

Since `b\ge q+1`, this is at most `W_q(t)`. ∎

## 3. Dynamic batch capacity

### Theorem CMR370 — PROVED

Let

\[
J_q(t)=
\left\lfloor
\frac{(t-2)p^{2(q+1)}}{t^2}
\right\rfloor.
\]

For any collection of at most `J_q(t)` deep tokens, there is a target-specific
parent permutation which moves the designated old endpoint and avoids every
available cell on every exact Hall-pair line from all selected tokens.

### Proof

By CMR369, the union contains at most

\[
J_q(t)W_q(t)\le t-2
\]

lines before duplicate removal. Apply CMR245. ∎

The frozen-state consequence is the CMR367 trichotomy: improvement, anchored
continuation, or a candidate-only replacement line outside the whole selected
batch.

## 4. Cubic-root-balanced specialization

Put

\[
q_*=\left\lceil\frac{2h}{3}\right\rceil-1.
\]

Then

\[
\frac{t^{2/3}}{p}\le p^{q_*}<t^{2/3},
\qquad
p^{q_*+1}\ge t^{2/3}.
\]

### Corollary CMR371 — PROVED

At threshold `q_*`, every common-signature population of size `M` has one of
the following alternatives.

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

Moreover,

\[
\boxed{
J_{q_*}(t)
\ge
\left\lfloor\frac{t-2}{t^{2/3}}\right\rfloor.
}
\]

### Proof

The inequalities defining `q_*` give the heavy and support estimates in
CMR368. CMR369 and `p^{q_*+1}\ge t^{2/3}` give `U(\tau)\le t^{2/3}`. Substitute
the same inequality in the definition of `J_q`. ∎

For width-two and width-three blockers, CMR295–CMR296 give

\[
M=\Omega_p\left(\frac{t}{\log t}\right).
\]

Thus the balanced threshold yields

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

The remaining no-return theorem must show that successive batches cannot
recycle escaped lines through coarser repairs without paying CMR347
reintroduction mass, envelope expansion, exchange ancestry, or the existing
quotient/carry collateral.

No all-`n` theorem is claimed here. Threshold inequalities and exact batch
capacities are checked in
[`scripts/verify_prime_power_tunable_token_batching.py`](../scripts/verify_prime_power_tunable_token_batching.py).
