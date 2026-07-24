# One-strip rigidity and pair-aware prime patching

This chapter sharpens PP2--PP3 in two complementary directions. First, it
classifies every boundary-only `t=1` patch exactly and converts geometric
admissibility into blocker-matching tests. Second, it extends the clone-space
local-load theorem to the old-anchor pair conflicts that occur in a corner
patch of width `t>=2`.

Throughout, `[m]={1,...,m}`, points are written `(x,y)`, and a saturated set has
exactly two points in every row and column.

## 1. Complete degree classification for one new row and column

Let `S subseteq [m]^2` be saturated, put `q=m+1`, delete a set `R subseteq S`,
and suppose every inserted point lies in the new row or new column

\[
U_q=([m]\times\{q\})\cup(\{q\}\times[m])\cup\{(q,q)\}.
\]

### Proposition PP1d -- PROVED

Every saturation-preserving boundary-only patch from `[m]^2` to `[m+1]^2` has
exactly one of the following two forms.

1. **Corner splice.** `R={(x,y)}` and the inserted set is
   \[
   \{(x,q),(q,y),(q,q)\}.
   \]
2. **Two-edge strip switch.** `R={(x_1,y_1),(x_2,y_2)}`, where
   `x_1!=x_2` and `y_1!=y_2`, and the inserted set is
   \[
   \{(x_1,q),(x_2,q),(q,y_1),(q,y_2)\}.
   \]
   The corner `(q,q)` is not inserted.

Consequently there are exactly `2m` type-one degree states and

\[
\binom{2m}{2}-2m=m(2m-3)
\]

type-two degree states.

#### Proof

An old column `x` has only one available boundary cell, `(x,q)`. Therefore at
most one deleted point can lie in an old column. The same argument applies to
old rows. Hence `R` is a matching in the row-column graph, and every deleted
column and row forces its corresponding boundary cell.

Let `z` be the indicator that `(q,q)` is inserted. The new row receives one
point for every deleted old column, plus the corner, so

\[
|R|+z=2.
\]

The new column gives the same equation. Thus either `z=1` and `|R|=1`, or
`z=0` and `|R|=2`. The forced cells are precisely the two displayed forms.
Conversely, direct degree counting shows that both forms preserve saturation.

For the count, there are `2m` choices in type one. In type two, start from all
pairs of old points and remove the `m` same-row pairs and the `m` same-column
pairs. No pair is removed twice because the points are distinct. ∎

This proposition turns every finite boundary-only `t=1` search into a complete
check of only `2m^2-m` forced candidates. Deletion budgets above two add no
states.

## 2. Secants through an external point form a matching

For an external lattice point `z notin S`, define

\[
M_z(S)=\{\{a,b\}\subseteq S:a,b,z\text{ are collinear}\}.
\]

### Proposition PP2a -- PROVED

If `S` is no-three-in-line, then `M_z(S)` is a matching on the vertex set `S`.
After deleting `R subseteq S`, the point `z` lies on no retained old-pair secant
if and only if `R` is a vertex cover of `M_z(S)`.

#### Proof

Two distinct pairs in `M_z(S)` cannot share an endpoint `a`: both pairs would
lie on the unique line through `a` and `z`, producing three collinear points of
`S`. Thus the pairs are vertex-disjoint. A blocker pair survives in `S\R`
exactly when neither endpoint is deleted, which proves the vertex-cover
criterion. ∎

In particular, a type-one splice cannot clear an inserted boundary point with
two blocker secants, and a type-two strip switch cannot clear one with three
blocker secants.

## 3. Exact geometric criterion for one-strip patches

For a type-one or type-two degree state, let `A` be its forced inserted set and
put `X=S\R`. Call a pair in `A` **mixed** if one point lies in the new row and
the other lies in the new column. Axis pairs wholly in the new row or wholly in
the new column cannot contain an old point.

### Proposition PP2b -- PROVED

A boundary-only one-strip degree state is no-three-in-line if and only if both
conditions hold:

1. for every `z in A`, the deletion set `R` is a vertex cover of `M_z(S)`;
2. every mixed-pair line determined by two points of `A` is disjoint from `X`.

The inserted set `A` never contains an internal collinear triple.

#### Proof

Condition 1 is exactly the absence of a triple containing two retained old
points and one inserted point, by PP2a. A triple containing one retained old
point and two inserted points can only use a mixed pair: two top cells determine
the new row, two right cells determine the new column, and neither axis line
contains an old point. This gives condition 2.

In type one, `A` has one top cell, one right cell, and the corner. Its only
possible nonaxis pair is the top-right pair, while the corner makes the other
two pairs horizontal and vertical. In type two, there are two top and two right
cells; any three inserted points contain an axis pair, so no inserted triple is
collinear. ∎

The script `scripts/analyze_one_strip_extensions.py` enumerates all states from
PP1d and verifies the final configurations by exact integer determinants.

## 4. Exhaustive small seed graph

Every saturated configuration is the union of two edge-disjoint permutation
graphs. Therefore enumerating and deduplicating such unions is exhaustive.
The script `scripts/enumerate_one_strip_seeds.py` carries this out for small
labeled grids and applies PP1d to every no-three state.

### Proposition PP3a -- PROVED BY EXHAUSTIVE FINITE CHECK

For labeled grids of side `2<=n<=5`, the exact counts are:

| `n` | Saturated states | No-three states | One-strip extendable states | Directed extensions |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 2 |
| 3 | 6 | 2 | 1 | 1 |
| 4 | 90 | 11 | 4 | 9 |
| 5 | 2040 | 32 | 9 | 9 |

Starting from the unique `n=2` state and allowing every possible boundary-only
one-strip choice at every step, the numbers of reachable states at sides
`2,3,4,5` are respectively

\[
1,2,1,0.
\]

#### Verification argument

The enumeration ranges over all unordered pairs of pointwise edge-disjoint
permutations and deduplicates their unions. Proposition S1 proves that every
saturated state occurs. Every no-three test and every proposed extension is
checked by exact integer determinants. Running

```bash
python scripts/enumerate_one_strip_seeds.py --max-n 5
```

reproduces the table and reachability sequence.

### Candidate design PP3-R1 -- REFUTED

A recursive strategy that adds one boundary row and column at a time, never
inserting an old-old replacement cell, cannot construct all sizes: even after
branching over every possible state, the exact state graph has no path from
`n=2` to `n=5`.

This does not refute wider boundary reservoirs, multi-strip gadgets, or
interior tomographic trades. It does show that seed preparation cannot be
replaced by a universal repetition of the two PP1d moves.

For the certificate corpus on this branch, the exact analyzer finds no
boundary-only one-strip extension for any stored seed with `3<=n<=10`. The
`n=2` seed has two valid degree states leading to the two no-three states at
`n=3`.

## 5. Pair-aware local-load theorem for a wider corner

Now let `t>=2` and let

\[
B=\{m+1,\ldots,m+t\}.
\]

Keep the old no-three core `X subseteq [m]^2` fixed. Let `G subseteq B^2` be a
candidate host such that no cell of `G` lies on a secant through two points of
`X`.

Let `P` be the set of unordered pairs of cells in `G` that are collinear with at
least one anchor in `X`. Such a pair automatically has distinct rows and
columns. Let `T` be the set of nonaxis collinear triples in `G`.

For each new row or column `v`, define:

- `m(v)`: the number of cells of `B^2\G` incident with `v`;
- `pi(v)`: the number of pairs in `P` incident with `v`;
- `tau(v)`: the number of triples in `T` incident with `v`.

Put

\[
m_*=\max_v m(v),\qquad
\pi_*=\max_v \pi(v),\qquad
\tau_*=\max_v \tau(v).
\]

### Theorem PP2c -- PROVED

If

\[
\boxed{
\frac{m_*}{t}
+\frac1{2t-1}
+\frac{8\pi_*}{(2t)(2t-1)}
+\frac{32\tau_*}{(2t)(2t-1)(2t-2)}
\le\frac1{24},
}
\]

then `G` contains exactly `2t` cells with two in every new row and column, and
their union with `X` is no-three-in-line.

#### Proof

Create two clones of every new row and column and expose a uniformly random
perfect matching of `K_{2t,2t}`. Use four kinds of canonical bad event:

1. a chosen lift of a cell outside `G`;
2. two disjoint lifts of the same original cell;
3. compatible lifts of a pair in `P`;
4. compatible lifts of a triple in `T`.

The first, second, third, and fourth event types are specified by partial
matchings of sizes one, two, two, and three. The Lu--Szekely matching-space
negative dependency graph used in Theorem D1 therefore applies unchanged.

For one fixed row clone, omitted cells contribute `m(v)/t`, duplicate-cell
events contribute at most `1/(2t-1)`, every original forbidden pair contributes
`8/(2t)_2`, and every original triple contributes `32/(2t)_3`. The same bounds
hold for column clones. The displayed inequality makes every clone load at most
`1/24`, so the proof of Theorem D1 gives a perfect matching avoiding every bad
event.

After projection, unavailable-cell events exclude old-pair secants, pair events
exclude old-anchor/new-pair triples, triple events exclude internal triples, and
duplicate events make the projected cells distinct. Thus the projection is the
required patch. ∎

### Corollary PP2d -- PROVED

For `t>=100`, the simpler bounds

\[
m_*\le\frac{t}{100},\qquad
\pi_*\le\frac{t^2}{400},\qquad
\tau_*\le\frac{t^3}{400}
\]

suffice.

Indeed, the four load terms are at most

\[
\frac1{100},\quad \frac1{199},\quad \frac1{199},\quad \frac1{98},
\]

whose sum is less than `1/24`.

### Corollary PP2e -- PROVED

For `t>=100`, failure of every corner-only patch in `G` forces at least one of

\[
m_*>\frac{t}{100},\qquad
\pi_*>\frac{t^2}{400},\qquad
\tau_*>\frac{t^3}{400}.
\]

Thus failure has an explicit concentration certificate: a heavy old-pair
shadow, a heavy old-anchor pair load, or a heavy internal triple load on one new
row or column.

The script `scripts/analyze_corner_patch_loads.py` constructs the maximal host
obtained by deleting old-pair-blocked corner cells, counts `m_*`, `pi_*`, and
`tau_*` exactly for modest `t`, and evaluates the theorem's rational load.

## 6. Remaining limitation

PP2c is an endpoint, not a proof of PP2. A near-complete grid host generally has
a logarithmically accumulated candidate-only triple load, so the `tau_*` branch
cannot be ignored. PP3 must prepare a structured bank or a cleaned candidate
host that simultaneously controls all three loads, or use a multiscale repair
process before invoking PP2c.

The new exact target for a corner-only route is therefore:

1. keep old-pair shadow below `t/100` per active coordinate;
2. keep old-anchor pair load below `t^2/400`;
3. remove or absorb enough internal direction families to leave triple load
   below `t^3/400`;
4. preserve a two-per-row/two-per-column completion host throughout.

No claim in this chapter supplies those preparation bounds for the
prime-minus-one construction.
