# Same-edge anchor domain pruning

The source-clean macro theorem PP3ea removes every fixed-pair blocker by
restricting slot domains.  Its remaining exceptional unary class consists of a
movement point and refill point controlled by the same selected source edge,
together with one fixed source anchor.  The product factorization PP3dv makes
this class removable by a second label-dependent domain restriction.

## 1. Anchor-bad edge sets

Let `E` be an `R`-edge matching pool and let `F` be the fixed retained source
set.  Let

\[
 A_0=\{A_1,\ldots,A_L\},
 \qquad
 B_0=\{B_1,\ldots,B_L\}
\]

be candidate movement-row and refill-column labels.  For a label pair `(A,B)`,
define

\[
 U_{A,B}
 =
 \{e=(x,y)\in E:\exists p=(u,v)\in F
 \text{ with }(A-v)(B-u)=(x-u)(y-v)>0\}.
\]

Thus `e in U_{A,B}` exactly when choosing edge `e` in a slot carrying labels
`(A,B)` creates a same-edge anchored triple.

For fixed-pair safety, retain the notation `C_A,D_B` from PP3ea and define the
refined slot domain

\[
 H_{A,B}
 =
 (C_A\cap D_B)\setminus U_{A,B}.
\]

### Proposition PP3fd -- PROVED

Every value `e in H_{A,B}` simultaneously has the following properties.

1. The movement cell `(x,A)` lies on no secant through two points of `F`.
2. The refill cell `(B,y)` lies on no secant through two points of `F`.
3. No point of `F` is collinear with `(x,A)` and `(B,y)`.

#### Proof

The first two assertions are the definitions of `C_A` and `D_B`.  By PP3dv,
the third type of collinearity occurs exactly when

\[
 (A-v)(B-u)=(x-u)(y-v)>0
\]

for some anchor `p=(u,v) in F`, which is exactly the condition excluded by
`e notin U_{A,B}`. ∎

## 2. Divisor-energy bound on bad label pairs

Define the pool-anchor divisor energy

\[
 \mathcal E(E,F)
 =
 \sum_{e=(x,y)\in E}
 \sum_{p=(u,v)\in F:\,(x-u)(y-v)>0}
 \tau(|(x-u)(y-v)|).
\]

### Proposition PP3fe -- PROVED

One has

\[
 \boxed{
 \sum_{A\in A_0}\sum_{B\in B_0}|U_{A,B}|
 \le
 \mathcal E(E,F).
 }
\]

Consequently, for every `epsilon>0`, the number of label pairs satisfying

\[
 |U_{A,B}|>\epsilon R
\]

is at most

\[
 \boxed{
 \frac{\mathcal E(E,F)}{\epsilon R}.
 }
\]

#### Proof

Fix `e=(x,y)` and `p=(u,v)` with positive product
`N=(x-u)(y-v)`.  By PP3dw, the number of label pairs `(A,B)` satisfying

\[
 (A-v)(B-u)=N
\]

is at most `tau(N)`.  Summing these witness counts over `e,p` dominates the
union count on the left.  The second statement is Markov's inequality for the
nonnegative matrix `|U_{A,B}|`. ∎

This converts the unary same-edge obstruction into the same divisor energy that
already appears in PP3dy, but now at the level of deterministic slot domains.

## 3. Refined compatibility graph

Fix constants `0<epsilon<gamma<=1`.  Form a bipartite graph
`J_{gamma,epsilon}` on chosen movement and refill labels by joining `A` to `B`
when

\[
 |C_A\cap D_B|\ge\gamma R
 \qquad\text{and}\qquad
 |U_{A,B}|\le\epsilon R.
\]

Every edge of this graph has

\[
 |H_{A,B}|\ge(\gamma-\epsilon)R.
\]

### Theorem PP3ff -- PROVED FROM THE STANDARD LOCAL LEMMA

Suppose `J_{gamma,epsilon}` contains a perfect matching on `W` movement and
`W` refill labels and

\[
 \boxed{
 48(2W)^2\le(\gamma-\epsilon)^2R.
 }
\]

Then the pool has a saturated width-`W` macro patch that:

1. is internally no-three-in-line;
2. uses `2W` distinct source edges;
3. creates no triple with two points of `F` and one patch point;
4. creates no triple with one point of `F` and the movement/refill pair controlled
   by one selected source edge.

#### Proof

Match each movement label `A_i` to one refill label `B_{pi(i)}` in
`J_{gamma,epsilon}`.  Give the corresponding two slots the common domain
`H_{A_i,B_{pi(i)}}`, whose size is at least `(gamma-epsilon)R`.

Proposition PP3fd removes the two displayed source-containing classes for every
possible slot value.  Apply PP3ea with density parameter `gamma-epsilon` to
avoid source-edge collisions and all internal pair/triple conflicts.  Equal
margins give saturation. ∎

### Corollary PP3fg -- PROVED FROM THE PUBLISHED LLL-DISTRIBUTION THEOREM

Under the stronger numerical condition

\[
 24\bigl(2(2W)^2+1\bigr)
 \le
 (\gamma-\epsilon)^2R,
\]

the conditional macro distribution satisfies, for every `q`-slot cylinder,

\[
 \boxed{
 \Pr(B)
 \le
 \frac{e^{q/2}}{((\gamma-\epsilon)R)^q}.
 }
\]

In particular, the domain pruning removes both fixed-pair cell events and
same-edge anchored-pair events without losing fixed-rank spread.

#### Proof

Apply PP3ec to the refined domains. ∎

## 4. Direct matching criteria and failure alternative

### Proposition PP3fh -- PROVED

If `J_{gamma,epsilon}` has minimum degree at least `W/2` on both sides, then the
hypothesis of PP3ff concerning a perfect matching holds.

#### Proof

Apply PP3ed. ∎

Suppose the original fixed-pair compatibility graph `G_gamma` is complete on the
chosen labels.  Then failure of the minimum-degree criterion for
`J_{gamma,epsilon}` forces some movement or refill label to have more than
`W/2` partners `(A,B)` with `|U_{A,B}|>epsilon R`.

Thus the remaining unary-anchor obstruction has an explicit dichotomy:

1. a refined dense compatibility matching exists and PP3ff removes the class; or
2. the divisor-energy matrix has a row or column containing `Omega(W R)` bad
   edge-label incidences.

A global energy bound alone controls the number of bad label pairs by PP3fe;
a successful label-allocation theorem may combine that bound with random label
sampling, row/column regularization, or protected trades concentrated on the
exceptional labels.

## 5. Effect on the global slot endpoint

After applying PP3ff, the external-event budget in PP3ei no longer pays for:

- unary fixed-pair patch-cell blockers;
- unary same-edge movement/refill anchor certificates.

The remaining source-containing events are ordinary anchored patch pairs using
two distinct selected source edges, together with cross-macro events.  The
active bottleneck is correspondingly narrowed to proving that each slot belongs
to only `O(R)` such rank-two/rank-three events, within the explicit
`7 gamma^2 R/1152+O(1)` additional-occurrence allowance of PP3ej.