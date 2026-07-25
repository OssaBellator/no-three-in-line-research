# One harmonic-packet sweep preserves the quadratic-log token budget

CMR388 cleans every intermediate-height family of harmonic weight below `3/2`,
and CMR389 cleans any two dyadic bands beginning at height at least five.
CMR403 bounds the full-token edge return of each resulting one-layer
whole-parent reset. Therefore a complete sweep through paired dyadic bands has
only logarithmically many resets and fits inside the same quadratic-logarithmic
full-token budget as one descending prefix pass.

Let

\[
t=p^h
\]

and fix `\eta>0`. Consider the nonempty dyadic bands

\[
[H,2H),
\qquad
H=2^j,
\qquad
\max\{5,t^\eta\}\le H\le t-1.
\]

Let `B_\eta(t)` be their number.

## 1. Packet count

### Theorem CMR406 — PROVED

The bands may be partitioned into

\[
\boxed{
P_\eta(t)
=
\left\lceil\frac{B_\eta(t)}2\right\rceil
}
\]

harmonic packets, each exactly cleanable by one target-specific parent
permutation for all sufficiently large `t`. Moreover,

\[
\boxed{
P_\eta(t)
\le
\left\lceil\frac{1+\log_2t}{2}\right\rceil.
}
\]

### Proof

Pair the dyadic bands arbitrarily. Every two-band packet is cleanable by CMR389.
If one band remains, its harmonic weight is below `3/4`, so CMR388 applies.
There are at most `1+\log_2t` positive dyadic lower endpoints below `t`. ∎

This is an existence statement for one state per packet; it does not assert
that sequential installation preserves earlier packets.

## 2. Per-token packet-sweep return

Fix one full token

\[
\tau=(b,a,c,\theta),
\qquad
1\le b<h.
\]

A packet sweep installs one one-layer exact covering state for each packet.

### Theorem CMR407 — PROVED

The full-token reintroduction mass caused by one packet sweep satisfies

\[
\boxed{
I_\tau^{(2),\mathrm{packet}}
\le
\frac{P_\eta(t)t}{p^b}.
}
\]

### Proof

Each packet installation replaces one whole-parent matching and returns at most
`t/p^b` token edges by CMR403. Sum with multiplicity. ∎

## 3. Combined deep-token visit bound

### Corollary CMR408 — PROVED UNDER THE ONE-PASS PREFIX HYPOTHESIS

Suppose one closure epoch contains one descending prefix pass and one harmonic
packet sweep. Then

\[
\boxed{
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}
+
\frac{(2b+P_\eta(t))t}{p^b}.
}
\]

At the deep threshold `p^b\ge t^{2/3}`,

\[
\boxed{
D_\tau^{(2)}
\le
t^{2/3}
+
\left(
2h+
\left\lceil\frac{1+\log_2t}{2}\right\rceil
\right)t^{1/3}.
}
\]

### Proof

Combine the prefix-pass return bound CMR399 with CMR407, then add the exact
initial stock from CMR394 through the dynamic inventory CMR395. Use `b\le h`
and CMR406. ∎

Thus one exact packet sweep has the same deep-token order as one prefix pass.
The unresolved issue is recurrence of cleaned bands, not excessive one-sweep
edge return.

## 4. Aggregate labelled packet budget

### Theorem CMR409 — PROVED

Summed over every nonroot full token and every projective direction, one packet
sweep has return mass below

\[
\boxed{
\frac{(p+1)P_\eta(t)}{p-1}t^2.
}
\]

Consequently one prefix pass plus one packet sweep has total direction-labelled
full-token return mass

\[
\boxed{O_p(t^2\log t).}
\]

### Proof

At depth `b`, there are `(p+1)p^{2b}` full tokens. CMR407 contributes
`P_\eta(t)t/p^b` to each, so the depth contribution is

\[
(p+1)P_\eta(t)tp^b.
\]

Summing gives

\[
(p+1)P_\eta(t)t
\sum_{b=1}^{h-1}p^b
<
\frac{(p+1)P_\eta(t)}{p-1}t^2.
\]

CMR402 gives `O_p(t^2\log t)` for the prefix pass and CMR406 gives
`P_\eta(t)=O(\log t)`. ∎

The packet sweep introduces no new superquadratic token-return scale. A complete
closure theorem must still show that packet installation does not recreate an
unbounded number of earlier packet conflicts, or that such recreation pays
repeated packet states, target load, or exchange ancestry.

No all-`n` theorem is claimed here. Packet counts, per-token coefficients, and
aggregate sums are checked in
[`scripts/verify_prime_power_harmonic_packet_sweep.py`](../scripts/verify_prime_power_harmonic_packet_sweep.py).
