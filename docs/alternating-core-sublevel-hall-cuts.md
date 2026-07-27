# Sublevel Hall cuts for AC5 protected-safe resampling

**Branch:** `research/alternating-core-chain`

AC5ac--AC5af formulate complete current/protected event inventories as endpoint costs on a stationary Hall-flow polytope. This note evaluates that minimum exactly. A failed protected-safe flow must expose one explicit Hall cut into low-event output states.

## One-step endpoint cost

For a certified batch of size `t`, recall

\[
c_t(b)=m_{\rm cur}(b)+t\,m_{\rm high}(b),
\]

where both multiplicities are nonnegative integers. Put

\[
C_t=\max_{b\in B}c_t(b)
\]

and, for `1<=k<=C_t`,

\[
B_{<k}=\{b:c_t(b)<k\}.
\]

Let `r_k` be the maximum number of flawed states in `A` matchable into `B_{<k}`, and define

\[
\delta_k
=
\max_{X\subseteq A}
\bigl(|X|-|N(X)\cap B_{<k}|\bigr)_+.
\]

## AC5ag -- exact optimal AC5 flow cost -- PROVED

The minimum current/protected endpoint cost is

\[
\boxed{
\min_{w\in P(\Gamma)}
\sum_b c_t(b)q_w(b)
=
\sum_{k=1}^{C_t}\bigl(|A|-r_k\bigr)
=
\sum_{k=1}^{C_t}\delta_k.
}
\]

### Proof

Apply SRR2j--SRR2l to the integer endpoint cost `c_t`. QED.

## AC5ah -- protected-safe Hall-cut criterion -- PROVED

If

\[
\boxed{
\sum_{k=1}^{C_t}\delta_k<t|A|,
}
\]

then one stationary resampling state has

\[
N_{\rm high}=0,
\qquad
N_{\rm cur}\le t-1.
\]

### Proof

AC5ag gives a feasible Hall flow of cost strictly below `t|A|`. Apply the AC5ae augmented-cost argument. QED.

Thus the AC5 flow-design task is exactly to prove a sum of low-event Hall deficiencies smaller than `t|A|`.

## Multistep paths

For a multistep repair path put

\[
c_{\rm path}(b)
=
m_{\rm cur}(b)
+
t\sum_jm_{{\rm high},j}(b).
\]

Define `C_path`, `B_{<k}^{path}` and `delta_k^{path}` from this integer cost exactly as above.

## AC5ai -- multistep Hall-cut criterion -- PROVED

If

\[
\boxed{
\sum_{k=1}^{C_{\rm path}}
\delta_k^{\rm path}
<t|A|,
}
\]

then one complete path is protected-safe at every intermediate step and has final current count at most `t-1`.

No independence between steps is required.

### Proof

SRR2l identifies the minimum path endpoint cost with the displayed deficiency sum. Apply AC5af. QED.

## AC5aj -- failed safe flow returns one high-event Hall cut -- PROVED

If no feasible stationary flow satisfies the AC5ae inequality, then

\[
\sum_{k=1}^{C_t}\delta_k\ge t|A|.
\]

Consequently, some threshold `k` and some `X subseteq A` satisfy

\[
\boxed{
|X|-|N(X)\cap B_{<k}|
\ge
\frac{t|A|}{C_t}.
}
\]

Every accessible output outside `B_{<k}` carries combined event multiplicity at least `k`.

The same statement holds for the multistep cost with `C_path` and `delta_k^{path}`.

### Proof

Use AC5ag and pigeonhole the deficiency sum over its `C_t` thresholds. Choose a set attaining the selected deficiency. QED.

## Consequence for AC5

Restricted-menu resampling now has three exact interfaces.

1. Bound every used cylinder's reverse-load ratio.
2. Bound the aggregate min-cost endpoint objective.
3. Prove small Hall deficiency into every low-event endpoint sublevel.

Failure of the third interface is geometric: one flawed-state set cannot reach enough outputs with low current/protected event multiplicity. This is the correct cut object for superregular expansion, pool stability and alternate-switch construction.

## Finite check

`scripts/verify_ac_sublevel_hall_cuts.py` enumerates small Hall-feasible switching graphs, current/protected endpoint inventories and batch sizes. It verifies the exact deficiency-sum cost and the failed-flow threshold localization.
