# Weighted suppression survives endpoint thinning

PX371--PX376 compress a terminal blocker family onto one same-layer/channel
endpoint block.  Every endpoint carries a nonnegative assigned blocker weight,
and moving it away from its current position suppresses all assigned blockers.
The remaining question is whether the square-root/hybrid endpoint thinning used
to control internal rank-three collateral can retain enough of this suppression
weight.

A direct second-moment argument gives the required dichotomy.  Either one
endpoint already carries a large fraction of the thinned suppression scale, or
Bernoulli thinning retains a constant fraction of the expected total weight
with probability greater than one half.  This event can be intersected with
the usual size and internal-collateral events.

## 1. Weighted Paley--Zygmund alternative

Let an endpoint block have weights

\[
w_1,\ldots,w_t\ge0,
\qquad
W=\sum_i w_i.
\]

Retain every endpoint independently with probability `p`, and put

\[
X=\sum_i w_i\mathbf 1_{i\text{ retained}}.
\]

### Theorem PX377 -- PROVED

At least one of the following holds.

1. Some endpoint has

   \[
   \boxed{w_i>\frac{pW}{16}.}
   \]
2. The random retained weight satisfies

   \[
   \boxed{
   \Pr\left(X\ge\frac{pW}{4}\right)\ge\frac9{17}.
   }
   \]

### Proof

Assume the first outcome fails.  Then

\[
\sum_iw_i^2\le\left(\max_iw_i\right)W
\le\frac{pW^2}{16}.
\]

Since `E X=pW`, independence gives

\[
\mathbb E X^2
=p^2W^2+p(1-p)\sum_iw_i^2
\le\frac{17}{16}p^2W^2.
\]

Paley--Zygmund at threshold one quarter of the mean gives

\[
\Pr(X\ge pW/4)
\ge
\left(1-\frac14\right)^2
\frac{(\mathbb EX)^2}{\mathbb EX^2}
\ge
\frac{9}{16}\cdot\frac{16}{17}
=rac9{17}.
\]

\(\square\)

## 2. Simultaneous suppression and internal control

Let `I` be the internal rank-three creation of the allowed rematching sampled
after the retained endpoint set is chosen.  On retained sets too small for the
matching bank, define `I=0`; those outcomes will be discarded by the size
event.

Assume

\[
pt\ge32,
\qquad
\mathbb EI\le\eta pt.
\]

### Theorem PX378 -- PROVED REDUCTION

At least one of the following holds.

1. Some endpoint carries assigned weight greater than `pW/16`.
2. There is a retained endpoint set `J` and an allowed rematching such that

   \[
   \boxed{|J|\ge\frac{pt}{2},}
   \]

   \[
   \boxed{X(J)\ge\frac{pW}{4},}
   \]

   and

   \[
   \boxed{I(J)\le4\eta pt.}
   \]

### Proof

If item 1 fails, PX377 gives the weight event with probability at least
`9/17`.  Markov gives

\[
\Pr(I>4\eta pt)\le\frac14.
\]

Chernoff gives

\[
\Pr(|J|<pt/2)\le e^{-pt/8}\le e^{-4}.
\]

Now

\[
\frac9{17}-\frac14-e^{-4}>0,
\]

so the three desired events occur simultaneously with positive probability.
For that retained set, choose one allowed rematching whose internal creation
is no larger than the conditional average used in `I`. \(\square\)

### Corollary PX379 -- PROVED

Under item 2 of PX378, if

\[
\boxed{W>16\eta t,}
\]

then the retained suppression credit exceeds internal rank-three creation:

\[
\boxed{X(J)>I(J).}
\]

Hence the corrected external blocker forest PX324--PX329 applies to the
coupled parent/endpoint move.

### Proof

The hypothesis gives

\[
X(J)\ge pW/4>4\eta pt\ge I(J).
\]

\(\square\)

## 3. Application to support-cover returns

Use the cover block `V_*` of PX372.  Write `q_ch` for the number of channels,
to distinguish it from the thinning probability `p`.  The cover block has
order `t<=2n` and suppression weight

\[
W\ge\frac{|C|}{2q_{\rm ch}}.
\]

### Theorem PX380 -- PROVED REDUCTION

Suppose the one-variable weighted-cover outcome occurs, so

\[
|C|\ge\frac{Dn}{48}.
\]

Then

\[
\boxed{
\frac{W}{t}\ge\frac{D}{192q_{\rm ch}}.
}
\]

Consequently, whenever the hybrid thinning/rematching estimate gives

\[
\eta<\frac{D}{3072q_{\rm ch}},
\]

PX378--PX379 yield either:

1. a weighted one-point child of weight greater than `pW/16`; or
2. a retained compatible endpoint block whose assigned blocker suppression
   strictly exceeds its internal rank-three creation.

The two-variable cover has the stronger density

\[
\boxed{
\frac{W}{t}\ge\frac{Dn}{128q_{\rm ch}}.
}
\]

### Proof

For the one-variable case,

\[
W\ge\frac{Dn}{96q_{\rm ch}}
\]

by PX375, while `t<=2n`.  Divide to obtain the first display.  The condition
on `eta` is exactly `W>16eta t`.

For the two-variable case, PX375 gives

\[
W\ge\frac{Dn^2}{64q_{\rm ch}},
\]

and again `t<=2n`. \(\square\)

For fixed channel count, PX333 makes `eta=o(1)` on every cover block above the
square-root ambient threshold.  Thus sufficiently large cover blocks close
the internal-gap part of the return sign.  Small cover blocks necessarily
fall into the weighted one-point alternative of PX378 and return to the actual
buffer-cycle bank.

PX377--PX380 remove the last loss caused purely by endpoint thinning: assigned
parent-blocker destruction survives with constant probability and can be
compared directly to the hybrid rank-three ledger.  The remaining persistent
case is a chain of high-weight one-point rank-one returns whose cover blocks
stay below the ambient threshold.

## 4. Verification

Run

```bash
python scripts/verify_product_weighted_suppression_thinning.py
```

The verifier checks the second-moment inequality, the exact `9/17` probability,
the event-intersection constants, and all support-cover density calculations.