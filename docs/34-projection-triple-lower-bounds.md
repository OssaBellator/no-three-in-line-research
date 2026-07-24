# Quantitative projection triple lower bounds

The projection-dispersion condition PP3u is not only a yes/no obstruction. An
under-dispersed support forces a calculable number of collinear triples in every
state supported there.

## 1. Convex occupancy lemma

Let `q` parallel lines contain a total of `M` selected points. Write

\[
M=qs+r,
\qquad
0\le r<q.
\]

### Lemma PP3w -- PROVED

The number of collinear triples supported on those `q` lines is at least

\[
\boxed{
(q-r)\binom{s}{3}+r\binom{s+1}{3}.
}
\]

#### Proof

If two line occupancies differ by at least two, moving one point from the more
occupied line to the less occupied line does not increase the triple count,
because

\[
\binom{k}{3}-\binom{k-1}{3}=\binom{k-1}{2}
\]

is increasing in `k`. Repeating this balancing operation leaves occupancies
that differ by at most one. Exactly `r` lines then have `s+1` points and the
other `q-r` lines have `s` points, giving the displayed value. ∎

## 2. Row-lift consequence

Let a width-`t` row-lift state contain its required `4t` inserted points, and
let a primitive direction have only `q` level sets across the row-lift support.

### Corollary PP3x -- PROVED

Every such state contains at least

\[
F_t(q)=
(q-r)\binom{s}{3}+r\binom{s+1}{3},
\qquad
4t=qs+r,\quad0\le r<q,
\]

collinear triples in that direction.

When

\[
\frac{4t}{3}\le q<2t,
\]

this simplifies to

\[
\boxed{F_t(q)=4t-2q.}
\]

#### Proof

Apply PP3w to the parallel level sets. In the displayed range the balanced
occupancies are two and three, with exactly `4t-2q` lines of occupancy three.
Each contributes one triple. ∎

For the aligned off-diagonal obstruction, `q=2t-1`, so every state has at least
two slope-`-1` triples. Proposition PP3s only needed one of them.

## 3. Adding distinct directions

Use one sign convention for primitive directions, for example `a>0`. A
collinear triple has a unique primitive direction under this convention.

### Corollary PP3y -- PROVED

Let `mathcal D` be any set of distinct primitive nonaxis directions. If the
row-lift support occupies `q_d` levels in direction `d`, then every state has at
least

\[
\boxed{
\sum_{d\in\mathcal D}F_t(q_d)
}
\]

collinear triples, where terms with `q_d>=2t` may be replaced by zero.

#### Proof

PP3x counts triples separately in each direction. No triple is counted in two
distinct primitive directions. ∎

The analyzer `scripts/analyze_row_lift_projections.py` reports these bounds for
every tested under-dispersed direction and sums them. This gives a fast lower
bound on the minimum certificate count before any permutation-state search.