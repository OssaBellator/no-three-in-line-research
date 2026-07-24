# General reservoir patching and seed-load criteria

This chapter removes two restrictions from the first prime-patching endpoint.
First, the clone-space local lemma is formulated for an arbitrary deleted
reservoir, so old-old replacement cells and mixed old/new cells are allowed.
Second, a simple averaging theorem gives a quantitative sufficient condition
for preparing a boundary-only one-strip seed.

Throughout, the retained set is a Euclidean no-three-in-line configuration.
All collinearity statements are over the integers, not modulo a prime.

## 1. Arbitrary-deficit clone formulation

Let `X` be the retained point set. Let `C` be a set of active columns and `R` a
set of active rows. Give each active column `c` a deficit

\[
d_c\in\{1,2\}
\]

and each active row `r` a deficit

\[
e_r\in\{1,2\},
\]

with equal total

\[
N=\sum_{c\in C}d_c=\sum_{r\in R}e_r.
\]

In the prime-patching application, old active coordinates receive the number
of deleted reservoir points on that coordinate, while every new row and column
receives deficit two.

Let `G subseteq C x R` be the candidate cells. It must be disjoint from `X`,
and every cell lying on a secant through two retained points must be excluded
from `G`.

Create `d_c` clones of each active column and `e_r` clones of each active row.
A perfect matching of the resulting complete `K_{N,N}` clone graph supplies
the prescribed deficits.

Let `P` be the set of unordered pairs of cells of `G`, in distinct rows and
columns, whose line contains a point of `X`. Let `T` be the set of collinear
triples of cells of `G` having distinct rows and columns.

Use four kinds of canonical bad event:

1. a clone edge projecting to a cell outside `G`;
2. two disjoint clone edges projecting to the same cell;
3. compatible clone lifts of a pair in `P`;
4. compatible clone lifts of a triple in `T`.

For a bad event `A`, let `F_A` be its defining partial matching. For a clone
vertex `v`, define

\[
L(v)=\sum_{A:\,v\in V(F_A)}\frac1{(N)_{|F_A|}}.
\]

### Theorem PP2f -- PROVED

If `N>=3` and

\[
\max_v L(v)\le\frac1{24},
\]

then there is a patch contained in `G` that fills every prescribed deficit and
whose union with `X` is no-three-in-line.

#### Proof

A uniformly random perfect matching of `K_{N,N}` contains a fixed compatible
partial matching of size `s` with probability `1/(N)_s`. The four event types
above have ranks one, two, two, and three. Their canonical conflict graph is
the Lu--Szekely negative dependency graph.

Put `x_A=2 Pr(A)`. Every event uses at most six clone vertices. If `B` conflicts
with `A`, then the two defining partial matchings conflict at a clone vertex of
`F_A`. Therefore

\[
\sum_{B\sim A}x_B
 \le 2\sum_{v\in V(F_A)}L(v)
 \le 12\cdot\frac1{24}
 =\frac12.
\]

Hence

\[
x_A\prod_{B\sim A}(1-x_B)
 \ge 2\Pr(A)\left(1-\frac12\right)
 =\Pr(A).
\]

The lopsided local lemma gives a perfect matching avoiding every bad event.

After projection, type-one events enforce membership in `G`; type-two events
make projected cells distinct; type-three events exclude triples with one
retained anchor and two inserted cells; and type-four events exclude triples
of inserted cells. Because `G` contains no retained-pair secant cell, triples
with two retained points are also absent. The matching fills every clone and
therefore every prescribed row and column deficit. ∎

This theorem is an exact executable endpoint. It does not assume that all
active coordinates are new or that every deficit equals two.

## 2. Coordinate-level load bound

For an active row or column `v`, define:

- `u(v)`: the number of cells of `(C x R)\G` incident with `v`;
- `pi(v)`: the number of pairs in `P` incident with `v`;
- `tau(v)`: the number of triples in `T` incident with `v`.

Put

\[
u_*=\max_v u(v),\qquad
\pi_*=\max_v\pi(v),\qquad
\tau_*=\max_v\tau(v).
\]

### Corollary PP2g -- PROVED

It is sufficient that

\[
\boxed{
\frac{2u_*}{N}
+\frac1{N-1}
+\frac{8\pi_*}{N(N-1)}
+\frac{32\tau_*}{N(N-1)(N-2)}
\le\frac1{24}.
}
\]

#### Proof

Fix one clone of an active coordinate.

Each unavailable original cell has at most two clone edges containing the
fixed clone, so singleton events contribute at most `2u_*/N`.

A duplicate-cell event containing the fixed clone is possible only when both
endpoint deficits of that cell equal two. For each such opposite coordinate
there are exactly two duplicate events containing the fixed clone. At most
`N/2` opposite coordinates have deficit two, so the total duplicate
contribution is at most

\[
\frac{N}{(N)_2}=\frac1{N-1}.
\]

Each forbidden original pair has at most eight compatible clone lifts
containing the fixed clone: at most two choices at its own opposite endpoint
and at most four choices for the other cell. Each original triple has at most
`2*4*4=32` compatible lifts containing the fixed clone. Summing these four
bounds gives the displayed inequality, which implies PP2f. ∎

### Corollary PP2h -- PROVED

For `N>=200`, the simpler hypotheses

\[
u_*\le\frac N{200},\qquad
\pi_*\le\frac{N^2}{1600},\qquad
\tau_*\le\frac{N^3}{3200}
\]

suffice.

Indeed, the four terms in PP2g are at most

\[
\frac1{100},\qquad
\frac1{199},\qquad
\frac1{199},\qquad
\frac1{98},
\]

whose sum is less than `1/24`.

### Corollary PP2i -- PROVED

For `N>=200`, failure of every patch in the candidate host forces at least one
of

\[
u_*>\frac N{200},\qquad
\pi_*>\frac{N^2}{1600},\qquad
\tau_*>\frac{N^3}{3200}.
\]

Thus an arbitrary-reservoir failure has the same three-way concentration
certificate as the corner-only endpoint: heavy retained-pair shadow, heavy
retained-anchor pair load, or heavy internal triple load.

The script `scripts/analyze_reservoir_patch_loads.py` computes both the exact
clone-weighted load of PP2f and the coarse coordinate load of PP2g for a
specified finite deletion set.

## 3. Averaging over all two-edge one-strip states

Let `S subseteq [m]^2` be saturated and no-three-in-line, and put `q=m+1`.
Consider only the type-two states from Proposition PP1d. Such a state chooses
an unordered pair of old points in distinct rows and columns. There are

\[
K=m(2m-3)
\]

states.

Let `U` be the set of the `2m` noncorner boundary cells

\[
([m]\times\{q\})\cup(\{q\}\times[m])
\]

that lie on at least one secant of `S`.

For every `(x,y) in [m]^2`, call the mixed pair

\[
\{(x,q),(q,y)\}
\]

bad when its line contains a point of `S`. Split the bad mixed pairs into
`Q_occ`, for which `(x,y) in S`, and `Q_empty`, for which `(x,y) notin S`.

### Proposition PP3b -- PROVED

If

\[
\boxed{
\frac{2|U|}{m}
+\frac{|Q_{\rm occ}|+4|Q_{\rm empty}|}{m(2m-3)}
<1,
}
\]

then `S` has a valid boundary-only type-two extension to `[m+1]^2`.

#### Proof

Choose a type-two state uniformly.

Every old point belongs to exactly `2m-3` compatible deletion pairs. Hence
every old point is deleted with probability `1/m`. A top boundary cell is
inserted exactly when one of the two points in its old column is deleted; the
two possibilities are mutually exclusive. Therefore every top or right
boundary cell is inserted with probability `2/m`.

For a fixed mixed pair indexed by `(x,y)`, if `(x,y) notin S`, each of the four
choices consisting of one point in column `x` and one point in row `y` is a
compatible deletion pair. Thus the mixed pair is inserted with probability
`4/K`. If `(x,y) in S`, three of those four choices either repeat the same
point or share its row or column; only the pair of the two other points is
compatible. Its probability is `1/K`.

Let `Z` count selected cells from `U` plus selected bad mixed pairs. The
displayed expression is exactly an upper bound for `E Z`. If it is below one,
some state has `Z=0`, since `Z` is a nonnegative integer.

For that state, no inserted point lies on any old secant, and no selected
mixed pair line contains any old point. The inserted set has no internal
triple by PP1d. Proposition PP2b therefore makes the state a valid extension.
∎

The condition is deliberately stronger than necessary because it forbids a
boundary secant cell even when the chosen deletion pair would clear all its
blockers. Its value is that it converts PP3 seed preparation into two explicit
global counts. The script `scripts/analyze_one_strip_seed_loads.py` evaluates
the bound exactly.

## 4. Revised PP3 target

The general-reservoir endpoint now accepts the actual operations allowed by
PP2: delete old reservoir points, use old-old replacement cells, use mixed
old/new cells, and fill all new coordinates.

For a deletion set `D` and extension width `t`, the active clone size is

\[
N=|D|+2t.
\]

A prepared seed theorem may therefore close PP2 by constructing a candidate
host with

\[
u_*=O(N),\qquad \pi_*=O(N^2),\qquad \tau_*=O(N^3)
\]

with constants below PP2h. The unresolved content is no longer the exact
selection step. It is the geometric preparation or cleaning theorem that
produces these three local bounds for a useful width.
