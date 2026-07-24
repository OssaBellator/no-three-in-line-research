# Dense-domain source-clean square-root macro patches

PP3dn samples every slot from the whole matching pool.  Fixed-pair blockers can
be removed before sampling by restricting each slot to edges whose movement and
refill cells are both safe.  A dense compatibility matching between movement
and refill labels preserves the square-root local-lemma construction.

## 1. Safe edge sets and label compatibility

Let `E` be an `R`-edge matching pool and let `F` be a fixed no-three source set.
Choose `W` new movement-row labels `A_1,...,A_W` and `W` new refill-column labels
`B_1,...,B_W`.

Define

\[
 C_i
 =
 \{e=(x,y)\in E:(x,A_i)
 \text{ lies on no secant through two points of }F\},
\]

and

\[
 D_j
 =
 \{e=(x,y)\in E:(B_j,y)
 \text{ lies on no secant through two points of }F\}.
\]

For `0<gamma<=1`, make a bipartite graph `G_gamma` on the movement and refill
labels by joining `i` to `j` when

\[
 |C_i\cap D_j|\ge\gamma R.
\]

A perfect matching `pi` in `G_gamma` couples movement label `i` to refill label
`pi(i)`.  Create two slots with this label pair and give both slots the source
edge domain

\[
 H_i=C_i\cap D_{\pi(i)}.
\]

Every possible slot value now produces two cells that are fixed-pair safe
against `F`.

## 2. Local-lemma probabilities on unequal domains

Choose every slot independently and uniformly from its domain `H_i`.

### Proposition PP3dz -- PROVED

If every slot domain has size at least `gamma R`, the pair and triple conflict
events from PP3dl satisfy

\[
 \Pr(P_{s,t})\le\frac5{\gamma^2R},
 \qquad
 \Pr(T_{s,t,u})\le\frac8{\gamma^2R}.
\]

#### Proof

For two slots, equality of their selected source edges has probability at most

\[
 \frac{|H_s\cap H_t|}{|H_s||H_t|}
 \le
 \frac1{\gamma^2R}.
\]

Conditioning on one slot value, at most two values of the second slot complete a
mixed two-slot triple in either orientation.  This contributes at most
`4/(gamma R)`, and hence at most `4/(gamma^2 R)`.

For a three-slot triple, after two source edges and one of eight movement/refill
type patterns are fixed, at most one source edge completes the line.  The third
slot therefore contributes at most `8/(gamma R)`, which is no larger than the
stated bound. ∎

## 3. Source-cell-clean macro theorem

### Theorem PP3ea -- PROVED FROM THE STANDARD LOCAL LEMMA

Suppose `G_gamma` contains a perfect matching and

\[
 \boxed{
 48(2W)^2\le\gamma^2R.
 }
\]

Then the pool has a saturated width-`W` patch that:

1. is internally no-three-in-line;
2. uses `2W` distinct source edges;
3. creates no triple consisting of two points of `F` and one patch point.

#### Proof

Use the matched domains above.  PP3dz gives event probability at most
`8/(gamma^2R)`, and PP3dm gives dependency degree at most `2(2W)^2`.  The
rational symmetric local-lemma condition is exactly the displayed inequality.
Avoiding the pair events gives distinct selected edges, and avoiding all pair
and triple events makes the patch internally no-three.  Domain restriction makes
every selected patch cell fixed-pair safe.  Equal-margin bookkeeping is the same
as PP3dn. ∎

### Corollary PP3eb -- PROVED

For sufficiently large `R`, one may take

\[
 \boxed{
 W=\left\lfloor\frac{\gamma\sqrt R}{16}\right\rfloor.
 }
\]

Thus any constant-density compatible label matching gives a source-cell-clean
macro patch of square-root width.

## 4. Conditional spread

Use activity

\[
 x=\frac1{2(2W)^2+1}.
\]

### Theorem PP3ec -- PROVED FROM THE PUBLISHED LLL-DISTRIBUTION THEOREM

If

\[
 24\bigl(2(2W)^2+1\bigr)
 \le
 \gamma^2R,
\]

then the internally clean conditional distribution satisfies, for every
`q`-slot cylinder,

\[
 \boxed{
 \Pr(B)
 \le
 \frac{e^{q/2}}{(\gamma R)^q}.
 }
\]

Consequently every patch cell has probability at most
`2 sqrt(e)/(gamma R)` and every prescribed ordinary pair has probability at
most `4e/(gamma^2R^2)`.

#### Proof

The LLL activity check is the same as PP3dp with `R` replaced by
`gamma^2R` in the conflict probability.  The unconditional probability of a
prescribed slot value is at most `1/(gamma R)`.  A cylinder meets at most
`q(2W)^2` conflict events, so the inflation calculation of PP3dq applies
unchanged. ∎

The patch distribution has all fixed-pair cell certificates removed and retains
fixed-rank spread.  Fixed-anchor patch-pair certificates remain.

## 5. Easy compatibility criteria

### Proposition PP3ed -- PROVED

A balanced bipartite graph with `W` vertices on each side and minimum degree at
least `W/2` has a perfect matching.

#### Proof

For a left set `S` with `|S|<=W/2`, its neighborhood has size at least `W/2` and
therefore at least `|S|`.  If `|S|>W/2` and `|N(S)|<|S|`, any right vertex
outside `N(S)` has all its neighbors in the left complement, whose size is
less than `W/2`, contradicting the minimum-degree assumption.  Hall's theorem
applies. ∎

In particular, if every movement-safe set and every refill-safe set has size at
least `(1-epsilon)R`, then every intersection has size at least
`(1-2epsilon)R`.  The compatibility graph is complete with
`gamma=1-2epsilon`.

## 6. Remaining source-clean obstruction

The fixed-pair cell problem is now reduced to a dense-domain statement:
construct `W=Theta(sqrt(R))` new row and column labels for which `G_gamma` has a
perfect matching with constant `gamma`.

Once this holds, the only source-containing local certificates are
fixed-anchor patch pairs.  Their ordinary two-edge class has
`O(1/R^2)` spread, while the same-edge class has the multiplicative
factorization PP3dv and the random-coupling bound PP3dt.