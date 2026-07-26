# Every robust-surplus episode has a protected execution or a loaded obstruction

CMR1006--CMR1029 route rank-one and higher-rank new-triple surplus into concrete
geometric structures. This chapter collects those routes into one quantitative
episode theorem and records the finite protected-capacity budget across both
permutation layers.

Consider one minimum-robust episode with destroyed target load `D>=1`, positive
integer gap `g>=1`, and `a>=1` entering physical cells. Put

\[
B=\left\lceil\frac{D+g}{2}\right\rceil.
\]

By CMR1007, either at least `B` new triples have entry rank one or at least `B`
have entry rank at least two.

## 1. Rank-one execution scale

Assume the rank-one branch. Define

\[
d
=
\left\lceil\frac{B}{a}\right\rceil.
\]

Fix an integer `R>=3` and put

\[
M
=
\left\lceil
\frac{d}{\binom{R-1}{2}}
\right\rceil.
\]

### Theorem CMR1030 -- PROVED

At least one of the following holds.

1. The old minimum state contains at least `binom(R,3)` target triples on one
   line.
2. One entering cell centres a cell-disjoint geometric secant-star bank of at
   least `M` arms.

### Proof

CMR1010 gives a root supporting at least `d` rank-one triples. Apply CMR1009 with
threshold `R`. ∎

## 2. Layer-polarized rank-one execution

### Theorem CMR1031 -- PROVED

In branch 2 of CMR1030, at least one of the following holds.

1. A common-layer compatible outside-pair subbank has size
   \[
   \boxed{M_0\ge\left\lceil\frac M4\right\rceil.}
   \]
2. A cross-layer rooted paid-pair bank has size
   \[
   \boxed{M_\times\ge\left\lceil\frac M2\right\rceil.}
   \]

In the first branch, define

\[
J=\max\{2,\lceil\sqrt{M_0}\rceil\},
\qquad
R_0=\left\lceil\frac{M_0}{4(J-1)}\right\rceil.
\]

Relative to a protected matching of size `k` in that layer, one obtains a
matching-vertex wall of degree at least `J`, protected growth

\[
\boxed{2\max\{0,R_0-2k\},}
\]

or a core certificate `k>=R_0/2`.

In the cross-layer branch, every arm has an exact rooted line-clean cylinder and
an explicit opposite-layer physical-cell response as in CMR1019--CMR1020.

### Proof

Apply CMR1015--CMR1021. ∎

## 3. Higher-rank execution scale

Assume the higher-rank branch, so `a>=2`. Put

\[
t
=
\left\lceil
\frac{B}{\binom a2}
\right\rceil,
\qquad
h
=
\left\lceil\frac{t+2}{2}\right\rceil.
\]

### Theorem CMR1032 -- PROVED

One entering pair supports at least `t` new triples on one nonaxis line. One
permutation layer contains at least `h` selected cells of that line.

Relative to a protected matching of size `k` in the majority layer, one obtains
protected growth

\[
\boxed{G=\max\{0,h-2k\}}
\]

or the core certificate

\[
\boxed{k\ge\left\lceil\frac h2\right\rceil.}
\]

The bank state also satisfies

\[
\boxed{\Phi(Q)\ge\binom{t+2}{3}.}
\]

### Proof

Use CMR1011--CMR1012 and CMR1022--CMR1027. ∎

## 4. One-episode protected alternative

### Corollary CMR1033 -- PROVED

For every `R>=3`, a minimum-robust episode reaches at least one of:

1. old target-line load `binom(R,3)`;
2. a rank-one matching-vertex wall;
3. rank-one protected growth with the formula of CMR1031;
4. a rank-one protected core with `k>=R_0/2`;
5. a cross-layer rooted paid-pair bank of size at least `ceil(M/2)`;
6. higher-rank protected growth `G` from CMR1032;
7. a higher-rank protected core with `k>=ceil(h/2)`;
8. cubic bank-state line load `binom(t+2,3)`;
9. physical target-cell deletion, restoration payment, host rollback,
   contraction, factor/wall descent, envelope expansion, or strict potential
   improvement.

### Proof

Combine CMR1030--CMR1032 with the complete host and target-handoff responses
CMR926--CMR989. ∎

No anonymous surplus branch remains inside one episode.

## 5. Protected growth has one two-layer capacity

Let the two protected matching sizes initially be `k_0^{(0)}` and `k_0^{(1)}`.
For a monotone sequence of executions, let `G_i` be the number of newly absorbed
protected edges at episode `i`, in whichever layer receives the absorption.

### Theorem CMR1034 -- PROVED

\[
\boxed{
\sum_iG_i
\le
2n-k_0^{(0)}-k_0^{(1)}.
}
\]

### Proof

Each layer protected matching has size at most `n`. Every absorbed edge is new in
its layer and protected sizes are monotone. Sum the two capacities. ∎

This combines heavy-line growth, one-edge line absorption, and two-edge star-arm
absorption in one currency: newly protected matching edges.

## 6. Large-growth episodes are finite

### Theorem CMR1035 -- PROVED

For every integer `G_0>=1`, the number of episodes with `G_i>=G_0` is at most

\[
\boxed{
\left\lfloor
\frac{2n-k_0^{(0)}-k_0^{(1)}}{G_0}
\right\rfloor.
}
\]

### Proof

Apply CMR1034 and divide by `G_0`. ∎

## 7. Failure of protected growth is itself quantitative

### Theorem CMR1036 -- PROVED

If neither layer grows during the protected execution of one robust episode,
then at least one of the following holds.

1. the old state has target-line load `binom(R,3)`;
2. a matching-vertex wall has degree at least `J`;
3. the relevant protected core satisfies `k>=R_0/2` in the rank-one branch;
4. the majority-layer protected core satisfies `k>=ceil(h/2)` in the
   higher-rank branch;
5. the episode lies in the cross-layer rooted bank and must pay one of the
   explicit physical-cell, restoration, rollback, contraction, or owner-exit
   responses of CMR1020.

### Proof

Set the growth alternatives in CMR1031 and CMR1032 equal to zero and retain the
other branches. ∎

## 8. Robust protected-execution endpoint

### Corollary CMR1037 -- PROVED

Along a robust-surplus history, protected growth cannot occur indefinitely.
After the finite two-layer capacity of CMR1034 is spent, every further episode
must produce a loaded old target line, a matching-vertex wall, a large protected
core, a cross-layer rooted paid-pair response, cubic new-state line load, or a
structural/potential exit.

Thus the remaining prime-power obstruction has moved beyond raw new-triple
surplus. It is the large-core/wall and cross-layer rooted-bank endpoint after
protected capacity saturation.

### Proof

Combine CMR1033--CMR1036. ∎

No all-`n` theorem is claimed. Scale formulas, layer polarization, protected
capacity, and episode bounds are checked in
[`scripts/verify_prime_power_robust_surplus_protected_execution.py`](../scripts/verify_prime_power_robust_surplus_protected_execution.py).
