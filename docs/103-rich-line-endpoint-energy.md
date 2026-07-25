# Rich-line endpoint energy

The Hall-localization theorem PP3kp produces a linear bank of designated
recapture lines, each meeting the endpoint rectangle in linearly many cells.
Moving the unchanged endpoint that owns one such line changes the line rather than
merely forbidding all of its cells.  This chapter gives the exact assignment
energy governing that move.

The same calculation applies to source-secant and unary-shadow line banks whenever
the witness candidate attached to each endpoint index remains fixed during the
trade.

## 1. Owner-line load matrix

Let

\[
R_0=\{s_i=(x_i,y_i):i\in[q]\}
\]

be a tied endpoint bank.  Fix candidate points

\[
z_1,\ldots,z_q
\]

and a fixed finite set `A` of endpoint cells whose incidences are being measured.
For every possible replacement

\[
s_{ij}=(x_i,y_j)
\]

define

\[
\boxed{
h_{ij}
=
|\{a\in\mathcal A:
a\ne s_{ij},\ a,z_i,s_{ij}\text{ are collinear}\}|.
}
\]

The current diagonal load and the full assignment energy are

\[
H_0=\sum_i h_{ii},
\qquad
W=\sum_{i,j}h_{ij}.
\]

For a permutation `pi`, put

\[
H(\pi)=\sum_i h_{i,\pi(i)}.
\]

### Proposition PP3lg -- PROVED

Replacing `R_0` by

\[
R_\pi=\{(x_i,y_{\pi(i)}):i\in[q]\}
\]

changes the owner-line incidence multiplicity by exactly

\[
\boxed{H(\pi)-H_0.}
\]

#### Proof

The candidate `z_i`, the target-cell set `A`, and the old column `x_i` attached to
owner `i` remain fixed.  Before the trade, owner `i` contributes `h_ii`; after the
trade it contributes `h_i,pi(i)`.  Sum over `i`. ∎

This is a preparation potential on the endpoint host.  It counts incidences with
multiplicity; overlapping forbidden cells are intentionally charged once for each
owner line containing them.

## 2. Spread-assignment endpoint

Let `mu` be any distribution on source-admissible endpoint permutations supported
on a permitted host.  Assume the one-cell cylinder bound

\[
\Pr_{\pi\sim\mu}[\pi(i)=j]
\le
\frac Kq
\]

for every permitted cell `(i,j)`.

Write

\[
W_\mu
=
\sum_{(i,j)\text{ permitted}}h_{ij}.
\]

### Theorem PP3lh -- PROVED

One has

\[
\boxed{
\mathbb E_{\pi\sim\mu}H(\pi)
\le
\frac Kq W_\mu.
}
\]

Consequently, if

\[
\boxed{
\frac Kq W_\mu<H_0,
}
\]

then some source-admissible endpoint trade strictly decreases the owner-line
incidence multiplicity.

#### Proof

By linearity of expectation,

\[
\mathbb EH(\pi)
=
\sum_{i,j}h_{ij}\Pr[\pi(i)=j]
\le
\frac KqW_\mu.
\]

If the upper bound is below the current integer value `H_0`, at least one state
has smaller load. ∎

The source-valid distribution of PP3jn has `K=O(1)` after the two-scale thinning.
Thus no separate source-collateral term is hidden in this theorem.

## 3. Rich designated-line bank

Suppose the recapture localization PP3kp gives `q` resource-disjoint owner lines,
after restricting to a common endpoint layer and relabelling the retained linear
subbank.  Assume every current line has at least `c q` cells of `A`, where
`0<c<=1`.  Then

\[
H_0\ge c q^2.
\]

Every nonaxis line meets the tied endpoint rectangle in at most `q` cells, so

\[
0\le h_{ij}\le q.
\]

### Corollary PP3li -- PROVED

At least one of the following holds.

1. A source-admissible endpoint permutation decreases the designated-line
   incidence multiplicity.
2. The permitted assignment energy satisfies

   \[
   \boxed{
   W_\mu\ge\frac cK q^3.
   }
   \]

#### Proof

If alternative 2 fails, PP3lh gives

\[
\frac KqW_\mu<cq^2\le H_0.
\]

Apply the theorem. ∎

The second alternative is an extremal three-point-incidence condition: a constant
fraction of the largest possible owner/replacement line energy is present.

## 4. Grid-rich pencil core

Put

\[
\alpha=\min\{1,c/K\}.
\]

Call a permitted assignment `(i,j)` **grid-rich** when

\[
h_{ij}\ge\frac\alpha2q.
\]

### Proposition PP3lj -- PROVED

If

\[
W_\mu\ge\alpha q^3,
\]

then at least

\[
\boxed{
\frac\alpha{2-\alpha}q^2
}
\]

permitted assignments are grid-rich.

#### Proof

Let `N` be the number of grid-rich assignments.  Using `h_ij<=q` on those entries
and `h_ij<alpha q/2` on all others gives

\[
W_\mu
<
Nq+(q^2-N)\frac\alpha2q.
\]

Compare with `alpha q^3` and rearrange:

\[
N\ge\frac\alpha{2-\alpha}q^2.
\]

Replacing the strict inequality by a weak one follows by a limiting argument or
by lowering the threshold infinitesimally. ∎

Thus failure of the first moment does not leave one accidental rich line.  It
forces a quadratic owner/replacement pencil core.

## 5. Compatible matching inside the pencil core

View the grid-rich assignments as a bipartite graph on owner indices and target
row indices.

### Proposition PP3lk -- PROVED

A grid-rich assignment graph with `N` edges contains a matching of size at least

\[
\boxed{
\frac N{2q}.
}
\]

Under PP3lj it therefore contains at least

\[
\boxed{
\frac\alpha{2(2-\alpha)}q
}
\]

pairwise compatible owner/replacement assignments, each defining a line with at
least `alpha q/2` endpoint intersections.

#### Proof

Take a maximal matching of size `r`.  Its `2r` endpoint vertices meet every edge,
while each endpoint vertex has degree at most `q`.  Hence `N<=2rq`.  Rearrange. ∎

This produces a linear bank of endpoint-disjoint, grid-rich second-generation
lines.  It is the exact input needed by a rectangle, tomographic, or another
endpoint-permutation conversion.

## 6. Monotone line-support preparation

### Corollary PP3ll -- PROVED UNDER A UNIFORM CONVERSION HYPOTHESIS

Fix the candidate owners, endpoint coordinate sets, and target-cell set `A`.
Assume that whenever

\[
H_0\ge\eta q^2
\]

there is a source-admissible endpoint permutation satisfying the strict inequality
in PP3lh.  Then repeated trades terminate after finitely many steps at

\[
H_0<\eta q^2.
\]

If the hypothesis is available uniformly for `eta=eta_q=o(1)`, the final
owner-line incidence density is `o(1)`.

#### Proof

The fixed data make `H_0` a nonnegative integer.  Every selected trade strictly
decreases it, so states cannot cycle.  If the process stopped above the threshold,
the hypothesis would supply another decreasing trade. ∎

For designated recapture lines, PP3li--PP3lk sharpen the remaining alternative:
either the obstruction decreases directly, or it regenerates as a linear
compatible bank of lines that are themselves rich in endpoint-grid
intersections.  The missing theorem is now conversion of this grid-rich pencil
bank, not extraction of compatible resources.
