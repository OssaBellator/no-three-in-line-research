# Min-cost stationary resampling for AC5 event inventories

**Branch:** `research/alternating-core-chain`

AC5y--AC5ab transfer spread bounds through a stationary resampling kernel by bounding the reverse-load ratio of every rank-two and rank-three event cylinder. For a fixed complete AC5 inventory there is a sharper aggregate formulation: the whole expected collateral is one linear endpoint cost on the Hall-flow polytope. This allows the flow to be chosen for the actual current/protected inventory rather than for the worst cylinder separately.

## Event-cylinder multiplicities

Let `Omega=A sqcup B` be one local flaw-removal state space and let `w` be a feasible symmetric Hall flow on its switching graph. Put

\[
q_w(b)=\sum_a w_{ab}.
\]

For a line band `J`, let `E_J` be a complete multiset of AC5 event cylinders, including multiplicity when several geometric triples use the same state cylinder. Define

\[
m_J(b)=|\{C\in E_J:b\in C\}|.
\]

## AC5ac -- exact event-inventory flow law -- PROVED

If `N_J` is the number of represented created triples in band `J`, then

\[
\boxed{
\mathbb E_w N_J
\le
\sum_{C\in E_J}\Pr_w(Y\in C)
=
\frac1{|A|}\sum_{b\in B}m_J(b)q_w(b).
}
\]

Equality holds when the inventory has exactly one cylinder for each possible created triple and no two records represent the same triple occurrence.

### Proof

Completeness bounds every created-triple indicator by one representing cylinder indicator. Sum those indicators. SRR2i gives the exact aggregate cylinder sum as the displayed reverse-flow endpoint cost. Exact nonovercounting gives equality. QED.

## AC5ad -- one-band optimal resampling flow -- PROVED

Among all stationary flaw-removal kernels supported on the declared switching graph, the smallest AC5 upper bound for band `J` is

\[
\boxed{
\frac1{|A|}
\min_{w\in P(\Gamma)}
\sum_{ab\in\Gamma}m_J(b)w_{ab}.
}
\]

An optimizer exists and may be chosen rational. Computing it is a min-cost fractional matching problem with cost `m_J(b)` on every edge ending at `b`.

### Proof

Apply AC5ac and minimize its linear endpoint cost over the compact rational Hall polytope. QED.

## Joint current/protected objective

Let `t` be the certified batch size. Put

\[
c_t(b)=m_{\rm cur}(b)+t\,m_{\rm high}(b).
\]

For an output state define

\[
Z=N_{\rm cur}+t\mathbf1_{N_{\rm high}>0}.
\]

Since the protected count is a nonnegative integer,

\[
\mathbf1_{N_{\rm high}>0}\le N_{\rm high}.
\]

## AC5ae -- min-cost protected-safe drift criterion -- PROVED

If one feasible Hall flow satisfies

\[
\boxed{
\sum_{ab\in\Gamma}c_t(b)w_{ab}<t|A|,
}
\]

then one resampled state has

\[
N_{\rm high}=0,
\qquad
N_{\rm cur}\le t-1.
\]

Equivalently, it is sufficient that the minimum `c_t` transportation cost over the Hall-flow polytope be strictly below `t|A|`.

### Proof

AC5ac in the two bands gives

\[
\mathbb EZ
\le
\mathbb EN_{\rm cur}+t\mathbb EN_{\rm high}
\le
\frac1{|A|}\sum_b c_t(b)q_w(b)<t.
\]

Some output has `Z<t`. A protected event would contribute at least `t`, so none occurs. Integrality then gives `N_cur<=t-1`. Apply AC5g--AC5h. QED.

## AC5af -- multistep min-cost import -- PROVED

Suppose one random path has final current inventory multiplicity `m_cur` and protected inventory multiplicities `m_high,j` at its intermediate steps. Define

\[
c_{\rm path}(b)=m_{\rm cur}(b)+t\sum_jm_{{\rm high},j}(b).
\]

If a feasible path-flow representation satisfies

\[
\boxed{
\sum_b c_{\rm path}(b)q_w(b)<t|A|,
}
\]

then one complete path is protected-safe at every intermediate step and has final current count at most `t-1`. No independence between steps is required.

### Proof

Use the augmented variable

\[
Z=N_{\rm cur}+t\sum_j\mathbf1_{N_{{\rm high},j}>0}
\]

and bound each indicator by its event count. AC5ac and linearity give expected `Z<t`; select one path with `Z<t` and use integrality exactly as in AC5p. QED.

## Consequence for AC5

Restricted stationary menus no longer require a uniform per-cylinder ratio when the complete event inventory is known. There are now two valid interfaces.

1. AC5z controls every used cylinder by rank-specific reverse-load ratios.
2. AC5ad--AC5af choose a min-cost Hall flow for the aggregate current/protected endpoint multiplicities.

The second can be strictly sharper because a high reverse load is harmless on a state belonging to few geometric event cylinders.

## Finite check

`scripts/verify_ac_mincost_resampling_import.py` enumerates tiny feasible switching flows, verifies the exact event-multiplicity identity and checks the one-step and multistep augmented-cost implications for finite current/protected inventories.
