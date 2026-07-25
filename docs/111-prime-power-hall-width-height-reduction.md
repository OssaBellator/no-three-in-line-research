# Hall-width reduction to low primitive height

CMR247 leaves a nontrivial sharp blocker supported on `t-1` real lines and a
Hall rectangle `A times C` with `|A|+|C|=t+1`. If both Hall sides are broad,
those lines must cover many rectangle cells. One line is then long, and every
long grid line has small primitive direction height. Thus broad Hall-boundary
factors belong automatically to the low-height carry regime.

Let

\[
a=|A|,
\qquad
c=|C|,
\qquad
n=\min\{a,c\},
\qquad
m=\max\{a,c\}=t+1-n.
\]

Assume `n>=2`, so the blocker is not the singleton-fan case.

## 1. One blocker line is long

### Theorem CMR271 — PROVED

Let `t-1` nonaxis real lines cover every cell of `A times C` except possibly one
target cell. Then one of the lines contains at least

\[
\boxed{
\left\lceil\frac n2\right\rceil
}
\]

cells of `A times C`.

### Proof

The line family covers at least

\[
ac-1
=
n(t+1-n)-1
\]

distinct rectangle cells. Summing line--rectangle incidences counts every
covered cell at least once, so one of the `t-1` lines contains at least

\[
\frac{n(t+1-n)-1}{t-1}
\]

rectangle cells.

This quantity is at least `n/2`, because

\[
2\bigl(n(t+1-n)-1\bigr)-n(t-1)
=
n(t+3-2n)-2.
\]

Since `n<=m`, one has

\[
2n\le t+1,
\]

and therefore `t+3-2n>=2`. The last expression is at least `2n-2>=2` for
`n>=2`. Taking ceilings proves the theorem. ∎

## 2. Long lines have low primitive height

### Theorem CMR272 — PROVED

Let a nonaxis real line contain `q>=2` cells of the normalized `t` by `t` parent
board, and let its primitive direction height be `K`. Then

\[
\boxed{
(q-1)K\le t-1.
}
\]

Consequently, the line supplied by CMR271 satisfies, for `n>=3`,

\[
\boxed{
K
\le
\frac{2(t-1)}{n-2}.
}
\]

### Proof

Order the board cells on the line by their integer primitive parameter. The
first and last parameters differ by at least `q-1`. In whichever coordinate
realizes the primitive height `K`, their coordinate difference is therefore at
least `(q-1)K`. Both coordinates lie in `[0,t-1]`, proving the first inequality.

CMR271 gives `q>=ceil(n/2)`, so

\[
q-1
\ge
\frac{n-2}{2}.
\]

Substitute this into the first inequality. ∎

## 3. Broad sharp blockers lie below the exact high slice

### Corollary CMR273 — PROVED

Let a sharp target-specific CMR247 blocker have a nontrivial Hall rectangle. At
least one of the following holds.

1. The smaller Hall side has size at most six:
   \[
   \min\{|A|,|C|\}\le6.
   \]
2. One blocking line has primitive direction height strictly below
   \[
   \frac{43t}{100}.
   \]

### Proof

If `n>=7`, CMR272 gives

\[
K
\le
\frac{2(t-1)}{n-2}
\le
\frac{2(t-1)}5
<
\frac{43t}{100}.
\]

Otherwise `n<=6`. ∎

## 4. Revised sharp-blocker geometry

Combining CMR260 and CMR273, the target-specific blocker conversion is reduced
to four explicit possibilities.

1. Same-side singleton fans expand to at least `t` line signatures across the
   three target endpoints.
2. Singleton fans occur on mixed board sides.
3. A nontrivial Hall rectangle has smaller side at most six.
4. The blocker already exposes a line below the exact `0.43t` cleaning
   threshold and hence enters the low-height quotient/carry programme.

Thus every broad nontrivial Hall factor has been charged to low primitive
height. The genuinely geometric residual is finite-width: mixed fans and Hall
rectangles of widths two through six.

No all-`n` theorem is claimed here. The incidence average, width inequality, and
height thresholds are checked in
[`scripts/verify_prime_power_hall_width_height.py`](../scripts/verify_prime_power_hall_width_height.py).
