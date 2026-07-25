# Exact slack in finite-width Hall blockers

CMR273 reduces a sharp nontrivial Hall blocker either to low primitive height or
to smaller Hall-side width at most six. The finite-width cases have an exact
incidence slack. Almost every blocking line must be a full transversal of the
smaller Hall side. Widths four through six then produce linearly many lines
below height `t/3`; only widths two and three remain distinct geometric
obstructions.

Let \(A\times C\) be the Hall rectangle from CMR247, and put

\[
n=\min\{|A|,|C|\},
\qquad
m=\max\{|A|,|C|\}=t+1-n.
\]

Let `\mathcal L` be the `t-1` blocking lines. For \(L\in\mathcal L\), write

\[
i(L)=|L\cap(A\times C)|.
\]

Every nonaxis line is a partial matching, so

\[
i(L)\le n.
\]

## 1. Exact deficiency-plus-overlap budget

### Theorem CMR274 — PROVED

Define the line deficiency

\[
D
=
\sum_{L\in\mathcal L}(n-i(L))
\]

and the repeated-incidence mass

\[
\Omega
=
\sum_{z\in A\times C}
\max\{0,\deg_{\mathcal L}(z)-1\}.
\]

Then

\[
\boxed{
D+\Omega
\le
n(n-2)+1.
}
\]

Consequently all but at most `n(n-2)+1` blocking lines meet the Hall rectangle
in exactly `n` cells.

### Proof

The line family covers every Hall-rectangle cell except possibly the target
cell, so its union contains at least

\[
nm-1
\]

cells. The total line--rectangle incidence count is

\[
I
=
\sum_{L\in\mathcal L}i(L).
\]

By definition,

\[
D=n(t-1)-I,
\qquad
\Omega
=I-\left|\bigcup_{L\in\mathcal L}(L\cap(A\times C))\right|.
\]

Therefore

\[
D+\Omega
=
n(t-1)-\left|\bigcup_{L\in\mathcal L}(L\cap(A\times C))\right|
\le
n(t-1)-(nm-1).
\]

Using `m=t+1-n`, the right side becomes

\[
n(t-1-m)+1
=
n(n-2)+1.
\]

Every nonfull line contributes at least one unit to `D`, proving the final
assertion. ∎

## 2. Widths four through six are linearly low-height

### Corollary CMR275 — PROVED

Assume `4<=n<=6`. At least

\[
\boxed{
t-2-n(n-2)
}
\]

blocking lines contain `n` Hall-rectangle cells. Every such line has primitive
height at most

\[
\boxed{
\frac{t-1}{n-1}
\le
\frac{t-1}{3}
<
\frac{43t}{100}.
}
\]

In particular the explicit full-transversal counts are

\[
\begin{array}{c|c}
n&\text{guaranteed full lines}\\
\hline
4&t-10\\
5&t-17\\
6&t-26
\end{array}
\]

whenever these lower bounds are positive.

### Proof

CMR274 leaves at least

\[
(t-1)-\bigl(n(n-2)+1\bigr)
=
t-2-n(n-2)
\]

full lines. A full line contains `n` board cells, so CMR272 gives

\[
(n-1)K\le t-1.
\]

For `n>=4`, the remaining inequalities follow. ∎

Thus widths four, five, and six are not separate high-height blocker types:
they already supply a linear population to the low-height carry ledger.

## 3. Exact width-three residual

### Corollary CMR276 — PROVED

If `n=3`, then

\[
D+\Omega\le4.
\]

At least

\[
\boxed{t-5}
\]

blocking lines contain three Hall-rectangle cells. Each such full line is itself
a compatible candidate-only collinear triple. Across the entire blocker there
are at most four total units of nonfull-line deficiency and repeated
Hall-rectangle incidence.

### Proof

Substitute `n=3` into CMR274. A nonaxis line containing all three cells has
three distinct source and target coordinates and hence is one compatible
candidate-only triple. ∎

Width three is therefore an almost-disjoint population of `t-O(1)` actual
candidate triples supported on the same three Hall slices.

## 4. Exact width-two residual

### Corollary CMR277 — PROVED

If `n=2`, then

\[
D+\Omega\le1.
\]

At least

\[
\boxed{t-2}
\]

blocking lines contain both Hall-slice cells. Every such line has at least one
additional compatible candidate cell outside the Hall rectangle, because it is
a candidate-only certificate line but can contain at most two cells inside the
width-two rectangle.

Thus a width-two sharp blocker is a two-slice chord system of size `t-2`, with
at most one total deficiency or overlap unit, together with external third-point
witnesses.

### Proof

Substitute `n=2` into CMR274. Every full line contains the two Hall-slice cells.
A blocker line is supplied by a candidate-only triple, so it contains at least
three compatible parent-board cells. The third cell lies outside the Hall
rectangle. ∎

## 5. Revised sharp-blocker endpoint

Combining CMR260, CMR273, and CMR274--CMR277, the sharp blocker problem is reduced
to the following explicit classes.

1. Mixed source/target singleton fans.
2. Width-two chord systems with external witnesses and at most one slack unit.
3. Width-three systems with at least `t-5` actual full candidate triples and at
   most four slack units.
4. A linear family of primitive-height-below-`t/3` lines, already assigned to
   the low-height carry programme.

This removes widths four through six as independent obstructions. The next
geometric theorem should convert the width-two external-witness system or the
width-three almost-disjoint triple system into an alternating bank, an envelope
expansion, or a bounded carry-signature charge.

No all-`n` theorem is claimed here. The exact slack identities and all width
specializations are checked in
[`scripts/verify_prime_power_thin_hall_slack.py`](../scripts/verify_prime_power_thin_hall_slack.py).
