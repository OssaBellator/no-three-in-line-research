# Two-cycle-free and near-Hamilton signed-cover measures

The complete public/code certificate suite suggests a strong restriction inside the
swapped quarter-turn orbit CSP.  None of its pair permutations contains a
2-cycle, and nine of the thirteen records are either one Hamilton pair cycle or
one fixed pair plus one cycle through every remaining pair vertex.

This chapter makes that restriction exact.  Removing all pair 2-cycles deletes
every duplicate-orbit inequality and costs only a limiting factor `exp(-1/4)`
inside the canonical edge-disjoint signed-cover space.  The Hamilton and
one-fixed near-Hamilton subclasses admit exact path-forest cylinder formulas.
Those formulas expose a simpler probability space, but they also show that the
same `Theta(n log n)` first-moment obstruction survives.

The gain is therefore structural rather than existential: source and target
matching are replaced by a cyclic order, duplicate-orbit constraints vanish,
and only the geometric line capacities remain.

## 1. The two-cycle-free canonical class

Let `C_m` be the number of canonical signed pair permutations on `m` pair
vertices with no pair 2-cycle.  A fixed pair has canonical weight one, a pair
cycle of length at least three has orientation weight `2^ell`, and a 2-cycle is
forbidden.

### Theorem PP3biy -- PROVED

The exponential generating function of the two-cycle-free canonical class is

```text
sum_(m>=0) C_m z^m/m! = exp(-z-2z^2)/(1-2z).
```

If `A_m` is the number of all canonical edge-disjoint signed covers from
PP3bfp, then

```text
C_m/A_m -> exp(-1/4).
```

#### Proof

The labelled permutation cycle construction gives exponent

```text
z + sum_(ell>=3) 2^ell z^ell/ell
= -log(1-2z)-z-2z^2.
```

Exponentiating proves the generating function.  PP3bfp gives

```text
sum A_m z^m/m! = exp(-z-z^2)/(1-2z).
```

Both series have their unique dominant singularity at `z=1/2`; the ratio of
their analytic numerators there is

```text
exp(-1/2-1/2) / exp(-1/2-1/4) = exp(-1/4).
```

∎

### Corollary PP3biz -- PROVED

Every two-cycle-free canonical signed cover is automatically edge-disjoint at
the orbit-block level.  Hence its exact CSP contains no duplicate-orbit
inequalities.

#### Proof

By PP3bfo, only a directed pair 2-cycle can select the same four-cell orbit from
its two endpoints.  If the pair permutation has no 2-cycle, this obstruction is
absent.  Source and target uniqueness are already supplied by the pair
permutation. ∎

Thus restricting to this class removes a complete constraint family at only
constant-factor asymptotic cost.

## 2. Hamilton and one-fixed near-Hamilton covers

Define two subclasses for `m>=4`.

```text
H_m^0: rho is one m-cycle,
H_m^1: rho has one fixed vertex and one (m-1)-cycle.
```

All nonloop pair edges carry independent canonical orientation bits.

### Proposition PP3bja -- PROVED

Their exact sizes are

```text
|H_m^0| = 2^m (m-1)!,
|H_m^1| = m 2^(m-1) (m-2)!.
```

Consequently

```text
(|H_m^0|+|H_m^1|)/(2^m m!)
= 1/m + 1/[2(m-1)]
= (3m-2)/[2m(m-1)].
```

Since `C_m ~ exp(-1) 2^m m!`, the combined family has asymptotic relative size

```text
(|H_m^0|+|H_m^1|)/C_m ~ 3e/(2m).
```

#### Proof

There are `(m-1)!` directed Hamilton cycles on `m` labelled vertices and every
edge has two orientations.  For the one-fixed family, choose the fixed vertex
in `m` ways, choose a directed cycle on the remaining vertices in `(m-2)!`
ways, and orient its `m-1` nonloop edges independently.  The asymptotic follows
from the simple-pole coefficient of PP3biy. ∎

This is only a polynomial restriction of the two-cycle-free class.

### Corollary PP3bjb -- PROVED

The relative-cycle partitions in these two subclasses are completely controlled
by one cycle parity.

For `H_m^0`:

```text
m odd:  [2m],
m even: [m,m] or [m/2,m/2,m/2,m/2].
```

For `H_m^1`, put `ell=m-1`.  The fixed pair contributes `[2]`, and the long
cycle contributes

```text
ell odd:  [2ell],
ell even: [ell,ell] or [ell/2,ell/2,ell/2,ell/2].
```

#### Proof

Apply the exact pair-cycle lift PP3bfm to the unique nontrivial cycle and, in
the one-fixed family, to the fixed pair. ∎

## 3. Exact Hamilton-cycle cylinders

Let `(x)_r=x(x-1)...(x-r+1)`.  A prescribed directed edge set `F` is a directed
path forest when every vertex has indegree and outdegree at most one and `F`
contains no directed cycle.  Suppose `F` has `r` edges, and prescribe one
orientation bit on every edge.

### Theorem PP3bjc -- PROVED

Under the uniform signed Hamilton measure `H_m^0`,

```text
Pr(F is contained) = 1/[2^r (m-1)_r].
```

#### Proof

Contract every directed path of `F`.  The `r` contractions leave `m-r`
labelled supervertices, which admit `(m-r-1)!` directed Hamilton cycles.  Divide
by the total `(m-1)!` cycles and by `2^r` for the prescribed independent signs.
∎

The same contraction argument gives joint probabilities for every compatible
finite collection of prescribed pair assignments.

### Theorem PP3bjd -- PROVED

Under the uniform one-fixed signed measure `H_m^1`, suppose `F` uses `v`
distinct pair vertices.  Then

```text
Pr(F is contained)
= (m-v)/m * 1/[2^r (m-2)_r].
```

#### Proof

The fixed vertex must lie outside the `v` vertices used by `F`, giving `m-v`
choices out of `m`.  On the remaining `m-1` vertices, contracting the `r` path
edges leaves `m-1-r` supervertices and therefore `(m-r-2)!` directed cycles.
Divide by `(m-2)!` and by `2^r`. ∎

## 4. The first-moment barrier survives

Call a generic triple from PP3bga *strongly generic* when its three induced
pair assignments are nonloops and do not form a directed 3-cycle.  The generic
conditions already exclude directed 2-cycles.

### Theorem PP3bje -- PROVED

The number of strongly generic nonaxis collinear triples is

```text
Theta(n^4 log n).
```

For a fixed strongly generic triple `T`, its three signed pair assignments form
a directed path forest.  Therefore

```text
Pr_(H_m^0)(T subset P_sigma) = 1/[8(m-1)_3],
```

and, if its assignments use `v` pair vertices,

```text
Pr_(H_m^1)(T subset P_sigma)
= (m-v)/m * 1/[8(m-2)_3],
```

where `4<=v<=6`.  In both measures the expected number of strongly generic
same-layer collinear triples is

```text
Theta(n log n).
```

#### Proof

PP3bga gives `Theta(n^4 log n)` generic triples.  Triples containing a pair
self-loop contribute at most `O(n^4)`: choose the special cell, a second cell,
and the third column, after which collinearity determines the third row at most
once.  Directed pair 3-cycles contribute `O(n^3)`.  Removing these families
leaves the stated order.

A strongly generic triple fixes three oriented nonloop edges with no directed
cycle, so PP3bjc and PP3bjd apply with `r=3`.  Since `m=n/2`, summing a
`Theta(m^-3)` cylinder probability over `Theta(n^4 log n)` triples gives
`Theta(n log n)`. ∎

Thus the empirically successful cycle family does not make direct first moment
possible.  Its value is the exact cyclic-order representation and the removal
of matching and duplicate-orbit constraints, which may support switchings,
cluster expansion, or distributed repair.

## 5. Finite suite audit

### Proposition PP3bjf -- VERIFIED FINITELY / FRONTIER REFINED

The public/code suite in `experiments/archived-prime-seed-codes.json` contains
thirteen independently verified swapped pair-cycle partitions, for

```text
p=17,19,23,29,31,41,43,47,53,59,61,67,73.
```

All thirteen are pair-2-cycle-free.  The Hamilton cases are

```text
p=17,73,
```

and the one-fixed near-Hamilton cases are

```text
p=23,29,41,47,59,61,67.
```

Hence nine of the thirteen records lie in `H_m^0 union H_m^1`.

The diagnostic also verifies the coefficient formulas through `m=10` and
exhaustively checks the cylinder contractions through `m=8` for every
prescribed path forest of at most three edges:

```text
19,846 full-Hamilton forests,
19,534 one-fixed forests,
39,380 total forests.
```

#### Verification

Run

```bash
python scripts/check_two_cycle_free_near_hamilton_family.py \
  experiments/archived-prime-seed-codes.json \
  experiments/two-cycle-free-near-hamilton-family-audit.json
```

The installed pair-cycle partitions are already independently derived from the
geometric codes by the quarter-turn and signed-orbit diagnostics.  This checker
audits the new cycle restrictions, exact generating-function coefficients, and
path-forest contraction counts. ∎

The next asymptotic route inside swapped action can therefore work directly
with a random cyclic order and signs.  It must still suppress or repair
`Theta(n log n)` generic line defects; no asymptotic existence theorem is
claimed here.
