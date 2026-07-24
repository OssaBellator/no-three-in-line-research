# Fully source-safe macro domains

PP3ea removes fixed-fixed-patch triples by restricting slot domains.  The same
restriction can also remove the exceptional same-source-edge movement/refill
anchor class.  After that, every remaining source-containing certificate uses
two distinct slot variables.

## 1. Fully safe one-slot domains

Let `F` be the fixed retained source set.  For movement label `A` and refill
label `B`, define

\[
 H_{A,B}^{\rm full}
\]

to be the source edges `e=(x,y)` in the matching pool satisfying all three
conditions:

1. `(x,A)` lies on no secant through two points of `F`;
2. `(B,y)` lies on no secant through two points of `F`;
3. the line through `(x,A)` and `(B,y)` contains no point of `F`.

The third condition is exactly the negation of the product equation PP3dv for
every anchor in `F`.

Make the bipartite label graph `G_gamma^full` by joining `A` to `B` when

\[
 |H_{A,B}^{\rm full}|\ge\gamma R.
\]

### Theorem PP3el -- PROVED

If `G_gamma^full` contains a perfect matching and

\[
 48(2W)^2\le\gamma^2R,
\]

then the matching pool supports a saturated internally no-three width-`W` macro
patch with no source-containing triple controlled by one slot.

Equivalently, the patch has none of the following:

- two fixed points and one patch point;
- one fixed point together with the movement and refill points controlled by one
  source edge.

#### Proof

Couple the labels by the perfect matching and use the full safe sets as the slot
domains.  Their sizes are at least `gamma R`, so the internal product-LLL theorem
PP3ea applies.  Conditions 1 and 2 remove every fixed-pair cell certificate, and
condition 3 removes every same-slot anchored pair certificate. ∎

The conditional distribution has the PP3ec cylinder bounds.

## 2. Ordinary anchor completion codegree

Fix two distinct slots `s,t` with their movement/refill labels and full safe
domains.  For source edges `e` in the first domain and `f` in the second, there
are four candidate point pairs, one choice from `{M_s(e),F_s(e)}` and one from
`{M_t(f),F_t(f)}`.

Define

\[
 \kappa_{s,t}
 =
 \max_{e\in H_s}
 \left|
 \left\{f\in H_t:
 \text{one candidate pair on }e,f
 \text{ has a line meeting }F
 \right\}
 \right|.
\]

### Proposition PP3em -- PROVED

Under independent uniform sampling from the two slot domains, the probability
of an ordinary fixed-anchor conflict between `s,t` is at most

\[
 \boxed{
 \frac{\kappa_{s,t}}{\gamma R}.
 }
\]

#### Proof

Condition on the first slot value `e`.  At most `kappa_{s,t}` values of the
second slot create one of the four candidate-pair lines through a fixed anchor.
The second domain has size at least `gamma R`. ∎

The crude bound is `kappa_{s,t}<=4|F|`, because for a fixed first point, anchor,
and second point type, the required old column or row determines at most one
matching edge.  The useful regime is bounded or slowly growing codegree.

## 3. Integration with the global slot endpoint

### Corollary PP3en -- PROVED

Suppose every full safe slot domain has size at least `gamma R` and every
ordinary anchor codegree satisfies

\[
 \kappa_{s,t}\le\frac8\gamma.
\]

Then every ordinary anchor pair event has probability at most

\[
 \frac8{\gamma^2R},
\]

and may be inserted directly into the global PP3ei event family.

If every slot belongs to at most

\[
 \frac{7\gamma^2R}{1152}+O(1)
\]

ordinary-anchor and cross-macro events in total, PP3ei gives one assignment that
is internally clean and clean against `F`.

#### Proof

Combine PP3em with the codegree hypothesis and apply PP3ej--PP3ei. ∎

## 4. Failure structure

A failure of the fully safe dense-domain route has one of three explicit forms:

1. **cell shadow:** many label pairs lose density because one of their two cells
   is blocked, as in PP3ef;
2. **same-edge product core:** many edges are removed by the factor equation
   `(A-v)(B-u)=(x-u)(y-v)` from PP3dv;
3. **ordinary anchor codegree:** some slot pair and first source edge have many
   second-edge completions through fixed anchors.

The first two are unary domain concentration; the third is a two-slot star.
Protected rectangle/cycle trades may be targeted at exactly the source edges or
anchors supporting these cores.