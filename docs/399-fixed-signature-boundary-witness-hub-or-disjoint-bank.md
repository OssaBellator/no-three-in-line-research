# Fixed-signature boundary witnesses: hub or disjoint bank

`docs/398` localizes every large boundary-conflict packing to one canonical
owner/bridge/label signature.  The remaining variation is entirely in the
boundary-component vertices occupying the endpoint and bridge roles of that
signature.  This chapter gives an exact load decomposition on those roles and a
greedy hub-or-disjoint-bank alternative.

The statements are general.  They do not prove that either returned branch is
already a valid prime-patching trade.

## 1. Boundary roles of one fixed signature

Fix one canonical conflict signature `sigma`.  Suppose its witness path uses
`k` owner vertices and `j` boundary-mediated gaps between consecutive owners.
Every path of this signature has

```text
r=2+j
```

boundary vertices: two conflict endpoints and one intermediate bridge vertex
for each boundary-mediated owner gap.  Since `k<=3`, one has

```text
2<=r<=4.
```

Let `F_sigma` be a family of canonical paths of signature `sigma`, carrying
nonnegative packing weights `lambda_P`.  Write

```text
Lambda=sum_(P in F_sigma) lambda_P.
```

For a boundary vertex `z`, define its total path load

```text
L(z)=sum_(P in F_sigma:z in P) lambda_P.
```

For an ordered boundary role `a in {1,...,r}`, define similarly

```text
L_a(z)=sum_(P in F_sigma:z occupies role a of P) lambda_P.
```

Every canonical path is simple, so a boundary vertex occurs at most once on one
path.

### Proposition PP3bwi -- PROVED / EXACT FIXED-SIGNATURE ROLE MASS

For every fixed-signature packing,

```text
sum_z L(z)=r Lambda,
```

and for every ordered boundary role `a`,

```text
sum_z L_a(z)=Lambda.
```

Moreover

```text
L(z)=sum_(a=1)^r L_a(z).
```

#### Proof

Each path contributes its weight once to each of its `r` boundary vertices, so
it contributes `r lambda_P` to the first sum.  It contributes exactly once to
each ordered role sum.  Summing over paths proves the identities.  Simplicity of
the path makes the role decomposition exact. ∎

Thus the full packing weight is replicated only a constant number of times when
it is viewed as boundary-vertex load.

## 2. Hub or boundary-disjoint witness bank

Call two canonical witness paths **boundary-disjoint** when they share no
boundary vertex.  Their owner vertices may coincide; for a fixed signature the
owner skeleton is common by definition.

### Theorem PP3bwj -- PROVED / HUB-OR-DISJOINT FIXED-SIGNATURE BANK

Fix a threshold `H>0`.  Every fixed-signature packing of total weight `Lambda`
has one of the following alternatives.

1. **Boundary hub.** Some boundary vertex satisfies

   ```text
   L(z)>H.
   ```

   More precisely, one ordered role satisfies

   ```text
   L_a(z)>H/r.
   ```

2. **Boundary-disjoint bank.** There are at least

   ```text
   ceil(Lambda/(rH))
   ```

   canonical witness paths that are pairwise boundary-disjoint.

#### Proof

If a boundary vertex has load greater than `H`, the role refinement follows
from

```text
L(z)=sum_a L_a(z)
```

and pigeonholing over the `r` roles.

Assume now that every boundary vertex has load at most `H`.  Greedily choose any
remaining positive-weight path and delete every remaining path sharing a
boundary vertex with it.  A chosen path has `r` boundary vertices.  The total
packing weight deleted in that step is at most

```text
sum_(z in P) L(z)<=rH.
```

Continue until no positive-weight path remains.  If `s` paths were selected,
then the deleted weight is all of `Lambda`, so

```text
Lambda<=s r H.
```

Hence `s>=ceil(Lambda/(rH))`.  The selected paths are pairwise boundary-disjoint
by construction. ∎

This is a weighted statement: no lower bound on an individual packing edge is
required.

## 3. Square-root localization under a component-size cap

Assume every boundary component represented by a vertex has size at most `L`.
The endpoint constraints of the conflict packing imply that every individual
packing edge has weight at most `L`, although bridge loads may still be much
larger.

### Corollary PP3bwk -- PROVED / SQUARE-ROOT HUB-BANK DICHOTOMY

Let a fixed-signature packing have total weight `Lambda>0`, and put

```text
H=sqrt(L Lambda).
```

Then either

```text
some ordered boundary role has load
> sqrt(L Lambda)/r,
```

or there is a pairwise boundary-disjoint bank of size at least

```text
ceil((1/r) sqrt(Lambda/L)).
```

Since `r<=4`, the bank size is at least

```text
ceil((1/4) sqrt(Lambda/L)).
```

Using `PP3bwh`, any covering rotation of exact recleaning cost `c_min>3`
therefore yields one fixed signature with

```text
Lambda>= (c_min-3)/1530,
```

and hence either a fixed-role boundary hub of load larger than

```text
(1/4) sqrt(L(c_min-3)/1530),
```

or a boundary-disjoint witness bank of size at least

```text
ceil((1/4) sqrt((c_min-3)/(1530L))).
```

#### Proof

Insert `H=sqrt(L Lambda)` into `PP3bwj` and use `r<=4`.  The cost form follows
from the fixed-signature packing supplied by `PP3bwh`. ∎

Thus large recleaning cost is no longer only a dense fixed-signature relation.
After a square-root loss it has one of two familiar geometric shapes: a
single-role hub or a bank disjoint outside the common owner skeleton.

## 4. Revised recleaning frontier

The boundary-phase branch now has the following chain.

1. Exact recleaning cost differs from boundary minority mass by at most three.
2. Minority mass is an exact fractional conflict-packing value.
3. One of at most 510 signatures carries a constant fraction of that packing.
4. Within that signature, either one boundary role is heavily reused or there is
   a large witness bank disjoint in every boundary component.

The remaining geometric conversion may therefore treat fixed-role hubs and
boundary-disjoint fixed-signature banks separately.

## 5. Finite diagnostic

The script

```bash
python scripts/check_fixed_signature_boundary_witness_bank.py \
  experiments/fixed-signature-boundary-witness-example.json
```

checks the exact role-mass identities and the hub-or-disjoint greedy bound on a
stored rational packing.

The next theorem identifier after this chapter is `PP3bwl`.
