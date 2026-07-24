# Directional boundary-shadow cleaning

PP3cm closes same-pool local cleaning, but a patch cell may still lie on a
secant through two points of the opposite matching layer or another fixed source
set.  Counting all such secant pairs separately overpays badly.  A width-two
state only needs one available movement row and one available refill column per
selected source edge.  This chapter compresses the fixed-pair obstruction into
four directional edge counts.

## 1. Cell availability

Let `F` be any fixed no-three-in-line point set in the old grid.  Let `E` be an
`r`-edge matching block, and reserve new coordinates `a,b`.

For an edge `e=(x,y) in E`, define

\[
 M(e)=\{c\in\{a,b\}:(x,c)
 \text{ lies on no secant through two points of }F\},
\]

and

\[
 R(e)=\{c\in\{a,b\}:(c,y)
 \text{ lies on no secant through two points of }F\}.
\]

Call `e` **unusable** if either set is empty.  Among the usable edges define the
four forced classes

\[
 M_a=\{e:M(e)=\{a\}\},
 \qquad
 M_b=\{e:M(e)=\{b\}\},
\]

\[
 R_a=\{e:R(e)=\{a\}\},
 \qquad
 R_b=\{e:R(e)=\{b\}\}.
\]

Write their sizes as `u,m_a,m_b,r_a,r_b`.

## 2. Exact four-edge feasibility

### Proposition PP3co -- PROVED

A four-edge deletion set `D subseteq E` admits a width-two degree state with no
fixed-fixed-patch triple if and only if:

1. `D` contains no unusable edge;
2. `|D intersect M_a|<=2` and `|D intersect M_b|<=2`;
3. `|D intersect R_a|<=2` and `|D intersect R_b|<=2`.

#### Proof

The movement assignment chooses, for every edge of `D`, one allowed label in
`M(e)` and must use each of `a,b` exactly twice.  Four nonempty binary allowed
sets admit such an assignment exactly when no more than two edges are forced to
`a` and no more than two are forced to `b`.  Indeed, include every edge forced
to `a`, exclude every edge forced to `b`, and fill the remaining places from the
flexible edges.  The two inequalities guarantee that exactly two `a` labels can
be chosen.  The other two edges receive `b`.

The refill assignment is independent and has the identical criterion using
`R(e)`.  If both assignments exist, the resulting eight patch cells avoid every
secant through two points of `F` by their definition.  Conversely, an unusable
edge or three edges forced to one label makes the required two-per-new-line
margin impossible. ∎

This proposition handles the entire retained-retained-inserted certificate
class against `F`; no secant multiplicities appear.

### Proposition PP3cw -- PROVED

For a deletion `D` avoiding unusable edges, put

\[
 \mu_a=|D\cap M_a|,
 \qquad
 \mu_b=|D\cap M_b|,
 \qquad
 \mu_*=4-\mu_a-\mu_b,
\]

and define `rho_a,rho_b,rho_*` analogously from `R_a,R_b`.  The exact number of
fixed-pair-blocker-free width-two geometries on `D` is

\[
 \boxed{
 \binom{\mu_*}{2-\mu_a}
 \binom{\rho_*}{2-\rho_a},
 }
\]

with a binomial coefficient interpreted as zero when its lower index is outside
`[0,s]`.

#### Proof

A movement geometry is determined by the two edges assigned to new row `a`.
Every edge of `D intersect M_a` must be chosen, every edge of `D intersect M_b`
must be excluded, and exactly `2-mu_a` of the `mu_*` flexible edges must be
chosen.  This gives the first binomial coefficient.  The refill column choice is
independent and gives the second. ∎

Thus PP3co is the positivity criterion for an exact factored state count.  The
multiplicity is the entropy available for clearing the remaining anchored-pair
patterns.

## 3. A clean-domain density bound

For a nonnegative integer `s`, write `(s)_3=s(s-1)(s-2)`.

### Theorem PP3cp -- PROVED

Let `Gamma_F(E)` be the set of four-edge deletions that admit a blocker-free
width-two degree state against `F`.  Then

\[
 \boxed{
 \frac{|\Gamma_F(E)|}{\binom r4}
 \ge
 1
 -\frac{4u}{r}
 -\frac{4}{(r)_3}
 \left(
  (m_a)_3+(m_b)_3+(r_a)_3+(r_b)_3
 \right).
 }
\]

The right-hand side may be replaced by zero if it is negative.  Every deletion
in `Gamma_F(E)` supports at least one state of the full 36-state bank, so the
corresponding blocker-free full-bank density is at least one thirty-sixth of the
displayed lower bound.

#### Proof

Choose `D` uniformly from `binom(E,4)`.  By a union bound,

\[
 \Pr(D\text{ meets the unusable set})\le\frac{4u}{r}.
\]

For a fixed forced class `Z`, the event `|D intersect Z|>=3` is witnessed by a
three-subset of `D` contained in `Z`.  The expected number of such witnesses is

\[
 \binom43\frac{(|Z|)_3}{(r)_3}
 =
 \frac{4(|Z|)_3}{(r)_3}.
\]

Markov's inequality bounds the probability of the event by this quantity.  Sum
over the four forced classes and apply PP3co.  Each feasible deletion has at
least one balanced movement/refill assignment among the 36 degree states. ∎

### Corollary PP3cq -- PROVED

If

\[
 u=o(r)
\]

and

\[
 m_a,m_b,r_a,r_b=o(r),
\]

then a `1-o(1)` fraction of the four-edge deletions admit a fixed-pair-blocker-free
geometry.  The full 36-state blocker-free density is therefore at least
`1/36-o(1)`.

More quantitatively, if `u<=epsilon r` and every forced class has size at most
`alpha r`, then the feasible deletion fraction is at least

\[
 1-4\epsilon-16\alpha^3+O(1/r).
\]

## 4. What remains after cell cleaning

Once the state domain is restricted by PP3co, every fixed-fixed-patch triple has
been removed.  Only fixed-anchor/patch-pair triples remain locally.

There are at most `4r` same-edge movement/refill candidate pairs and at most
`16 binom(r,2)` candidate pairs controlled by distinct edges.  A line through a
candidate pair contains at most two points of the no-three set `F`.  Hence the
numbers of possible fixed-anchor signatures satisfy

\[
 N_h\le8r,
 \qquad
 N_2\le16r(r-1).
\]

If the blocker-free state domain has density `delta` in the full bank, the
conditioned PP3cg bounds give expected fixed-anchor defect at most

\[
 \boxed{
 \frac8\delta+
 \frac{128}{\delta}\frac{r-1}{r}
 <
 \frac{136}{\delta}.
 }
\]

Thus directional cell cleaning reduces the opposite-layer obstruction from a
quantity that may grow with `m` to a constant-order local anchor problem.  The
constant is intentionally coarse; exact pair feasibility, deletion cancellation,
and protected local trades can reduce it.

## 5. Revised remaining theorem

Combining PP3cm and PP3cp, a universal matching-pool equipartition already gives
same-pool clean density on almost every block.  To finish local preparation it
is now enough to prove, for almost every assigned width-two interval, that:

1. the unusable-edge count is `o(r)`;
2. each one-sided forced class is `o(r)`;
3. the constant-order fixed-anchor obstruction can be removed by geometry
   multiplicity, cycle choices, or protected trades.

This **directional boundary-shadow statement** is strictly weaker than requiring
a sparse secant shadow.  A candidate cell may lie on arbitrarily many source
secants; only the loss of both movement choices or both refill choices for many
source edges is dangerous.