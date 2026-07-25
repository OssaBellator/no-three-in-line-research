# Fixed-centre rank-two unary Xi arc-star localization

The single-cycle marked-filler theorem leaves rank-two unary `Xi` weight as one
possible paid core at a fixed captive centre. This weight has a simpler local
geometry than a general support-ranked obstruction. A directed Hamilton cycle
uses exactly one incoming and one outgoing arc at the marked centre. Once those
two arcs are fixed, the remaining state is a conditional single-cycle
completion with an exact spread law.

The sparse middle-transition relation then gives an exact dichotomy. Either one
locally source-clean incoming/outgoing pair has small deterministic unary `Xi`
cost, or almost every admissible arc on one side of the centre has cost at least
half the available local budget. The latter is a fixed-row or fixed-column
weighted arc star.

This chapter localizes the rank-two unary `Xi` core. It does not yet convert the
resulting heavy fixed-axis star.

## 1. Directed unary Xi arc weights

Let one controller pool have tied endpoint indices `V`, with `|V|=N`, and write
the matching point of index `i` as

```text
(x_i,y_i).
```

Selecting the endpoint-permutation arc

```text
i -> j
```

inserts the point `(x_i,y_j)`. Aggregate every rank-two unary `Xi` insertion
pattern supported on this directed arc into the nonnegative integer weight

```text
a(i,j).
```

Fix the marked endpoint `c`. Then, by the support-rank definition,

```text
D_A,2(c)
=
sum_{r!=c} a(r,c) + sum_{s!=c} a(c,s).
```

### Proposition PP3abf -- PROVED

A single-cycle state containing `c` selects exactly one incoming arc `r->c` and
one outgoing arc `c->s`, with `r,s,c` distinct. Its deterministic rank-two unary
`Xi` cost involving `c` is exactly

```text
a(r,c)+a(c,s).
```

#### Proof

Every permutation has one predecessor and one successor at `c`. A single cycle
has no fixed point and no transposition, so the predecessor and successor are
distinct from `c` and from each other. Rank-two unary patterns use one directed
arc, hence the patterns involving `c` are precisely those on the selected
incoming and outgoing arcs. ∎

## 2. Locally source-clean two-arc segments

Let

```text
I_c={r!=c: the arc r->c is unary-source-admissible},
O_c={s!=c: the arc c->s is unary-source-admissible}.
```

Let `M_c` be the forbidden middle-transition relation from PP3zj:

```text
(r,s) in M_c
```

when the two-step path `r->c->s` is source-invalid through a retained anchor.
Call `(r,s)` a **locally clean centre pair** when

```text
r in I_c,
s in O_c,
r!=s,
(r,s) notin M_c.
```

### Proposition PP3abg -- PROVED

If `d_U(c)=o(N)`, then

```text
|I_c|=N-o(N),
|O_c|=N-o(N).
```

Together with PP3zj,

```text
|M_c|<=2mD_m+2N=o(N^2),
```

so the number of locally clean centre pairs is `(1-o(1))N^2`.

#### Proof

Every missing incoming or outgoing arc contributes a unary forbidden incidence
whose support contains `c`; hence the total number of missing incident arcs is
at most `d_U(c)=o(N)`. Remove the diagonal pairs and the `o(N^2)` middle
relation from `I_c x O_c`. ∎

## 3. Exact conditional single-cycle law

Fix a selected filler block `B` of size `b` containing distinct indices
`r,c,s`, and condition on the path

```text
r -> c -> s.
```

### Proposition PP3abh -- PROVED

The number of directed Hamilton cycles on `B` containing both prescribed arcs is

```text
(b-3)!.
```

Conditional on this path, every additional compatible set of `u` directed arcs
has probability

```text
1/(b-3)_u
```

unless the additional arcs together with `r->c->s` create a proper directed
cycle, in which case the probability is zero.

#### Proof

Contract the three-vertex directed path to one ordered object. There remain
`b-2` cyclic objects and therefore `(b-3)!` directed cyclic orders. Every
additional compatible arc that does not close a proper directed cycle contracts
two current objects. With `u` additional arcs the count is `(b-u-3)!`; divide
by `(b-3)!`. ∎

Thus fixing the centre pair retains the same fixed-rank conditional spread law
as a uniform single cycle, with effective denominator `b-3`.

## 4. Conditional paid completion criterion

For a locally clean centre pair `(r,s)` on a fixed selected block, classify every
remaining source-invalid canonical pattern by the number `u` of additional
random arcs required after `r->c->s` is fixed. Let

```text
S_{r,s,u}
```

be the number of such patterns, for `0<=u<=3`. Let `J_{r,s}` be the exact expected
remaining `Xi` insertion cost, excluding the deterministic rank-two unary cost
on the two fixed arcs. Let `R_c>0` be the exact removal credit obtained by moving
`c`.

### Theorem PP3abi -- PROVED

If

```text
sum_{u=0}^3 S_{r,s,u}/(b-3)_u
+
[a(r,c)+a(c,s)+J_{r,s}]/R_c
<1,
```

then one conditional single-cycle completion is source-valid and has total `Xi`
insertion cost below `R_c`. Hence it gives a strict pool-compatible decrease of
`Xi`.

#### Proof

Choose a uniform conditional single-cycle completion. Proposition PP3abh gives
the displayed upper bound for every remaining source-invalid pattern; a proper
directed cycle has probability zero. The second term is normalized expected
paid cost. An outcome below one has no source-invalid event and paid cost below
`R_c`. Apply the exact insertion-cost-minus-removal-credit identity PP3kx. ∎

The criterion separates the deterministic local rank-two unary cost from every
remaining source and paid term.

## 5. Cheap centre pair or one-sided heavy star

Fix a positive local budget `lambda`. Define

```text
L_in(lambda)={r in I_c: a(r,c)<lambda/2},
L_out(lambda)={s in O_c: a(c,s)<lambda/2}.
```

### Theorem PP3abj -- PROVED

At least one of the following holds.

1. There is a locally clean centre pair `(r,s)` with

   ```text
   a(r,c)+a(c,s)<lambda.
   ```

2. Every distinct pair in

   ```text
   L_in(lambda) x L_out(lambda)
   ```

   belongs to `M_c`, and therefore

   ```text
   |L_in(lambda)| |L_out(lambda)| - N <= |M_c|.
   ```

   In particular,

   ```text
   min(|L_in(lambda)|,|L_out(lambda)|)
   <= sqrt(|M_c|+N).
   ```

#### Proof

If a distinct low-incoming/low-outgoing pair is not in `M_c`, it is locally
clean and its two arc weights sum to less than `lambda`, giving alternative 1.
Otherwise every such distinct pair is middle-forbidden. At most `N` pairs have
the same index on both sides, so the displayed product bound follows. The square
root bound is immediate. ∎

### Corollary PP3abk -- PROVED

At the slab-optimal pool scale

```text
N=m^(19/20+o(1)),
```

if no locally clean pair has rank-two unary cost below `lambda`, then one of the
following holds:

```text
a(r,c)>=lambda/2
```

for all but `m^(1/2+o(1))` unary-admissible incoming arcs, or

```text
a(c,s)>=lambda/2
```

for all but `m^(1/2+o(1))` unary-admissible outgoing arcs.

If `d_U(c)=o(N)`, the selected side contains `N-o(N)` heavy arcs.

#### Proof

Insert the divisor bound

```text
|M_c|<=2mD_m+2N=m^(1+o(1))
```

into PP3abj. Its square root is `m^(1/2+o(1))=o(N)`. Apply PP3abg to the
admissible side. ∎

## 6. Fixed-axis geometry of the heavy star

### Proposition PP3abl -- PROVED

The two heavy-star alternatives have exact fixed-axis geometry.

1. An incoming star consists of inserted cells

   ```text
   (x_r,y_c),
   ```

   all on the fixed old row `y_c`.
2. An outgoing star consists of inserted cells

   ```text
   (x_c,y_s),
   ```

   all on the fixed old column `x_c`.

Every heavy cell carries rank-two unary `Xi` weight at least `lambda/2`.
Consequently a failed cheap-pair choice produces total fixed-axis arc weight

```text
Omega(lambda N).
```

#### Proof

This is the definition of the endpoint-permutation cell associated with a
directed arc. Corollary PP3abk supplies `N-o(N)` heavy arcs on one side. ∎

The remaining object is therefore not an arbitrary weighted unary fibre. It is
a near-complete fixed-row or fixed-column family of replacement cells, each
carrying candidate-line incidence weight at the paid scale.

## 7. Revised rank-two unary Xi endpoint

### Corollary PP3abm -- PROVED

The rank-two unary `Xi` alternative at a source-light captive centre reduces to
one of:

1. a locally clean two-arc centre segment whose deterministic unary `Xi` cost is
   below the available local budget, followed by the conditional paid criterion
   PP3abi;
2. conditional residual source or higher-rank `Xi` concentration after fixing
   that cheap segment;
3. a near-complete incoming fixed-row arc-cost star;
4. a near-complete outgoing fixed-column arc-cost star.

The unstructured rank-two unary weighted fibre is no longer an independent
frontier. The exact remaining unary-`Xi` obstruction is a fixed-axis rich-cost
star or residual concentration under a conditioned two-arc completion.

## 8. Finite diagnostic

The script

```text
scripts/check_unary_xi_arc_star.py
```

checks a finite directed-cost instance, finds a cheap locally clean centre pair
when one exists, otherwise verifies the low-set product bound and identifies the
heavy side. For small instances it also enumerates Hamilton cycles containing a
selected two-arc centre segment and checks the exact `(b-3)!` count.
