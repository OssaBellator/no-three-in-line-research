# Mod-six target cleaning above height `0.42t`

CMR266 uses only parity to reduce the totient-weighted part of the high-direction
load. Residues modulo six give a stronger elementary sieve. Over each complete
six-height block, the available divisibility bounds average to `2/3`, with only
quadratic endpoint and monotonicity losses. This lowers the exact
candidate-only cleaning boundary to `0.42t`.

Retain the normalized odd target-specific parent board. Put

\[
m=\frac{t-1}{2},
\qquad
h_t(K)=K(t-K).
\]

## 1. A six-residue totient bound

### Theorem CMR278 — PROVED

For every integer interval

\[
H\le K\le m
\]

with `H>=2`, one has

\[
\boxed{
\sum_{K=H}^{m}\varphi(K)(t-K)
\le
\frac{2}{3}\sum_{K=H}^{m}K(t-K)
+
\frac{10}{9}t^2.
}
\]

### Proof

On the six residue classes modulo six, use

\[
\frac{\varphi(K)}{K}
\le
\begin{cases}
1/3,&K\equiv0\pmod6,\\
1,&K\equiv1\pmod6,\\
1/2,&K\equiv2\pmod6,\\
2/3,&K\equiv3\pmod6,\\
1/2,&K\equiv4\pmod6,\\
1,&K\equiv5\pmod6.
\end{cases}
\]

The first line uses divisibility by both two and three; the remaining lines use
one divisor or the trivial bound.

Partition the interval into complete aligned six-term blocks and at most five
unpaired terms at each end. On one complete block, subtract `2/3` from the six
coefficients. The deviations are

\[
-\frac{1}{3},
\quad
\frac{1}{3},
\quad
-\frac{1}{6},
\quad
0,
\quad
-\frac{1}{6},
\quad
\frac{1}{3}.
\]

Their positive and negative masses are both `2/3`. Since `h_t(K)` is increasing
for `K<=m`, the excess over the `2/3` baseline is at most

\[
\frac{2}{3}\bigl(h_t(k+5)-h_t(k)\bigr)
\le
\frac{10}{3}t.
\]

There are at most `t/12` complete blocks, contributing at most `5t^2/18`.
There are at most ten endpoint terms. For each, the excess over the `2/3`
baseline is at most

\[
\frac{1}{3}h_t(K)
\le
\frac{t^2}{12}.
\]

Their total is at most `5t^2/6`. Adding the two errors gives `10t^2/9`. ∎

## 2. Sieve-refined vertex load

### Corollary CMR279 — PROVED

Let

\[
\frac{t-1}{3}<H\le m,
\]

and define

\[
S(H)=\sum_{K=H}^{m}K(t-K),
\qquad
R(H)=\sum_{K=H}^{m}(t-2K).
\]

Then every parent board vertex satisfies

\[
\boxed{
T_3(w)
\le
\frac{4}{3}S(H)
+
\frac{20}{9}t^2
+
2(t-1)R(H).
}
\]

### Proof

CMR261 gives

\[
T_3(w)
\le
2\sum_{K=H}^{m}\varphi(K)(t-K)
+
2(t-1)R(H).
\]

Apply CMR278 to the totient sum. ∎

## 3. Explicit `0.42t` threshold

Put

\[
H_3=\left\lceil\frac{21t}{50}\right\rceil.
\]

### Theorem CMR280 — PROVED

For every odd

\[
t\ge1575,
\]

every parent board vertex satisfies

\[
\boxed{
\frac{1}{t}+
\frac{T_3(w)}{(t)_3}
<
\frac{1}{24}
}
\]

when `T_3(w)` counts only candidate-only triples of primitive height at least
`H_3`.

### Proof

The function `x(t-x)` is increasing on the relevant interval, so

\[
S(H_3)
\le
\int_{21t/50}^{(t+1)/2}x(t-x)\,dx
=
\frac{1859}{93750}t^3+
\frac{1}{8}t^2-
\frac{1}{24}.
\]

The function `t-2x` is decreasing, giving

\[
R(H_3)
\le
\int_{21t/50-1}^{(t-1)/2}(t-2x)\,dx
=
\frac{4}{625}t^2+
\frac{4}{25}t+
\frac{3}{4}.
\]

Substituting these bounds into CMR279 gives

\[
T_3(w)
\le
\frac{5518}{140625}t^3
+
\frac{30331}{11250}t^2
+
\frac{59}{50}t
-
\frac{14}{9}.
\]

The remaining margin below `1/24` is at least

\[
\frac{
2731t^3-4298725t^2+2141250t-500000
}{
1125000t(t-1)(t-2)
}.
\]

The numerator is positive at `t=1575`. Its derivative and second derivative are
positive there, and the second derivative remains increasing, so it stays
positive thereafter. ∎

### Corollary CMR281 — PROVED

For every odd parent block with

\[
t\ge1575,
\qquad
H\ge\left\lceil\frac{21t}{50}\right\rceil,
\]

there is a complete target-specific parent permutation which omits `z_*` and
contains no compatible candidate-only triple of primitive height at least `H`.

### Proof

Apply CMR249 with the target singleton event and the indicated high-slice
rank-three events. CMR280 verifies the local-load condition. ∎

## 4. Protected-line reserve

### Theorem CMR282 — PROVED

Let `t` be odd with

\[
t\ge1983,
\]

and put

\[
R_3(t)=\left\lfloor\frac{t}{2000}\right\rfloor.
\]

For every family of at most `R_3(t)` distinct nonaxis real lines, there is a
complete parent permutation which

1. omits `z_*`;
2. avoids every available cell on the protected lines;
3. avoids every candidate-only triple of primitive height at least
   `ceil(21t/50)`.

### Proof

The protected lines contribute matching-vertex singleton load at most `1/2000`.
Using the CMR280 estimate, the remaining margin is at least

\[
\frac{
4337t^3-8594075t^2+4280250t-1000000
}{
2250000t(t-1)(t-2)
}.
\]

The numerator is positive at `t=1983`; its derivative and second derivative are
positive there and remain increasing. CMR249 therefore supplies the required
permutation. ∎

### Corollary CMR283 — PROVED

Let a globally minimal positive-potential inherited parent block have odd size
`t>=1983`, and fix one endpoint `z_*` of an old target triple. Then either

1. a target-specific state creates a rank-one or rank-two certificate and hence
   exposes an anchored alternating continuation; or
2. there are `R_3(t)+1` distinct candidate-only real-line signatures, all of
   primitive height below `ceil(21t/50)`, and one target-specific state avoids
   the first `R_3(t)` lines together with the entire higher slice.

### Proof

Iterate CMR282. Every candidate-only replacement line is new because every
available cell on the protected lines is forbidden, and it lies below the
cleaned height threshold. ∎

## 5. Revised intermediate-height endpoint

Using only divisibility by two and three, the exact target-specific
candidate-only cleaning boundary is now

\[
0.42t.
\]

A linear protected-line reserve survives at the same threshold. Further
constant improvement is possible with larger residue sieves, but the geometric
remaining problems are more important: mixed singleton fans, width-two chords,
width-three almost-disjoint triples, and the low-height quotient/carry ledger.

No all-`n` theorem is claimed here. The six-residue block inequality, polynomial
thresholds, and exact discrete loads are checked in
[`scripts/verify_prime_power_mod_six_height.py`](../scripts/verify_prime_power_mod_six_height.py).
