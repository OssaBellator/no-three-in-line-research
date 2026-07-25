# Rank-three outer roles yield a disjoint fixed-centre path-petal bank

PP3aco--PP3acs convert the rank-three middle rectangle to the existing paid
two-resource-grid frontier. The remaining rank-three-specific branch in PP3abu
is a small exceptional outer-choice core together with a near-complete heavy
predecessor or successor family.

That family has a fixed-centre sunflower geometry. A predecessor pattern

```text
r -> p -> c
```

uses the common centre-column resource of `c` and only three noncentral typed
resources. Dense heavy support therefore contains a linear family of paths whose
noncentral resources are pairwise disjoint. A dyadic count pigeonhole makes their
local `Xi` costs comparable without losing the target bank size.

Bounded-support averaging then closes diffuse noncentral collateral exactly as in
the transition sunflower theorem. Failure is centre-core weight, a global
support-ranked threshold, local path cost at the removal-credit scale, or outer
source/host failure. Thus a small-core heavy outer-role family is no longer an
independent marked-`Xi` frontier.

The predecessor case is stated below. The successor case is its transpose.

## 1. Dense heavy predecessor support

Fix the captive centre `c`. Let `P=P_3(lambda)` be the exceptional predecessor
choice set from PP3abr. Let

```text
E_L^safe
```

be the number of source-valid predecessor paths `r->p->c`, and define

```text
H_L={
 (r,p):
 p notin P,
 r->p->c is source-valid,
 beta_L(r,p)>=lambda/3
}.
```

### Proposition PP3act -- PROVED

One has

```text
|H_L| >= E_L^safe-|P|N-2N.
```

Consequently, if

```text
E_L^safe=(1-o(1))N^2
```

and `|P|=o(N)`, then

```text
|H_L|=(1-o(1))N^2.
```

#### Proof

This is the support statement inside PP3abt. Paths with middle index in `P`
number at most `|P|N`. For each `p outside P`, the definition of `P_3(lambda)`
leaves at most two source-valid predecessor paths with weight below `lambda/3`.
All remaining source-valid paths belong to `H_L`. ∎

If the displayed source-valid density fails, the branch is already the outer
transition source core listed in PP3abu.

## 2. Typed-resource matching extraction

For one heavy path `e=(r,p)`, let its noncentral typed resource set be

```text
A_e={L_r,L_p,R_p}.
```

Every path also uses the common centre resource

```text
C={R_c}.
```

Here `L_x` and `R_x` denote the row-side and column-side endpoint resources of
index `x`.

### Proposition PP3acu -- PROVED

For every family `H` of predecessor paths through `c`, there is a subfamily
`B subseteq H` with

```text
|B| >= |H|/(4N)
```

such that the sets `A_e`, `e in B`, are pairwise disjoint.

#### Proof

Greedily select a path and delete every remaining path sharing one of its
noncentral typed resources. A fixed left resource `L_x` can occur in the first
or middle role, in at most `2N` paths. The two selected left resources therefore
meet at most `4N` paths in total. The selected right resource `R_p` occurs only
when the middle index is `p`, a class already counted among the paths using
`L_p`. Thus one greedy step deletes at most `4N` paths. ∎

Every selected binary pattern consists of the two compatible cells

```text
r->p,
p->c,
```

and the patterns share only `R_c`. They are fixed-centre path petals, pairwise
resource-disjoint outside the centre.

## 3. Slab-optimal bank size

### Corollary PP3acv -- PROVED

Under the dense source-valid hypotheses of PP3act, the heavy predecessor family
contains a disjoint path-petal bank of size

```text
Omega(N)=m^(19/20+o(1)).
```

It therefore contains a subbank of the target size

```text
W=m^(19/40+o(1)).
```

#### Proof

Apply PP3acu to `|H_L|=(1-o(1))N^2` and use `N>>W`. ∎

The same conclusion holds for the successor family with common centre-row
resource `L_c`.

## 4. Comparable local costs

Assume the positive integer path weights are at most polynomial in `m`. Put

```text
L=ceil(log_2(1+max_e beta_L(e)))=m^(o(1)).
```

Partition `H_L` into dyadic classes

```text
2^j <= beta_L(e) < 2^(j+1).
```

### Proposition PP3acw -- PROVED

Some dyadic class contains at least

```text
|H_L|/L
```

paths. That class has a pairwise noncentral-resource-disjoint subbank of size at
least

```text
|H_L|/(4NL)=m^(19/20-o(1)),
```

and hence a `W`-sized subbank. Every retained local path cost lies in one common
factor-two interval.

#### Proof

Pigeonhole the `L` classes by support cardinality and apply PP3acu inside the
largest class. ∎

If polynomial boundedness is unavailable, the same split returns either enough
support in boundedly many levels or one explicit high-multiplicity path core.

## 5. Bounded-support collateral averaging

Let `B` be one selected path-petal bank. For every source or paid pattern `F`,
let `supp(F)` be its typed resource support and suppose

```text
|supp(F)|<=r_0.
```

Give each pattern a nonnegative weight `w(F)`.

### Proposition PP3acx -- PROVED

One has

```text
sum_{e in B}
sum_{F: supp(F) cap A_e != empty} w(F)
<=
r_0 sum_F w(F).
```

Consequently the average petal-touching weight gains a factor `1/|B|`.

#### Proof

The sets `A_e` are pairwise disjoint. A support of size at most `r_0` can meet
at most `r_0` petals. Sum first over petals and then over patterns. This is the
same abstract incidence argument as PP3aaf. ∎

Only patterns supported at the shared centre resource remain undiluted across
the bank.

## 6. Conditional paid path-petal interface

For one petal `e=(r,p)`, fix the two-arc path

```text
r->p->c
```

inside a marked filler block of size `b>=3`. On every fixed selected block there
are exactly

```text
(b-3)!
```

single-cycle completions containing the path. Conditional on the path, every
additional compatible `u`-arc forest has probability at most

```text
1/(b-3)_u,
```

unless it creates a proper directed cycle.

Let `R_e>=R_*>0` be the exact removal credit. Let `S_e,u` be the remaining
source-invalid weight requiring `u` additional arcs, let `J_e^core` be the
centre-core insertion cost, and let `J_e^var` be the petal-touching and other
variable insertion cost after its support-selection factors are included.

### Theorem PP3acy -- PROVED

A source-valid strict decrease exists if

```text
(1/|B|) sum_{e in B} [
  sum_u S_e,u/(b-3)_u
  + (beta_L(e)+J_e^core+J_e^var)/R_*
] < 1.
```

Moreover PP3acx bounds the averaged variable term by

```text
O(W_var/|B|)
```

for the corresponding global bounded-support weight `W_var`, after the fixed
cylinder and endpoint-selection factors are restored.

#### Proof

Choose a petal uniformly and then a uniform conditional single-cycle completion.
The displayed expression bounds one nonnegative source-count-plus-normalized-cost
objective. An outcome below one has no source-invalid event and total insertion
cost below its removal credit. Apply PP3kx. The variable-term estimate is
PP3acx rank by rank. ∎

Thus diffuse noncentral collateral cannot obstruct all petals. Failure is a
centre-core term, global weight at the bank-credit scale, local dyadic path cost
at the removal-credit scale, or residual host/source failure.

## 7. Revised rank-three endpoint

### Corollary PP3acz -- PROVED

At a source-light captive centre, rank-three binary `Xi` weight reduces to one
of:

1. a conditioned cheap five-index chain and residual completion;
2. paid middle-grid selection, weighted grid multiplicity, projective cover, or
   residual grid-host structure;
3. an outer transition source core;
4. a `W`-sized fixed-centre path-petal bank whose noncentral resources are
   pairwise disjoint and whose local costs are comparable;
5. centre-core insertion weight, a global support-ranked threshold, local path
   cost at the petal credit scale, or residual endpoint-host failure.

Therefore the small-core/near-complete heavy outer-role family is no longer an
independent marked-`Xi` frontier. It rejoins the fixed-centre paid-petal,
source-star/resource-bank, and residual-collateral conversion problems already
present in the main ledger.

## 8. Finite diagnostic

The script

```text
scripts/check_rank_three_outer_path_petals.py
```

checks a finite predecessor-path instance. It validates the exceptional core,
source-invalid relation, low-cost-choice bound, dyadic support pigeonhole, and
greedy extraction of paths with pairwise disjoint noncentral typed resources.
The stored example realizes a uniform heavy path family and extracts a maximal
fixed-centre path-petal bank.
