# Fixed-signature localization of boundary conflict packings

`docs/396` gives every opposite-phase boundary pair a parity-odd path witness of
length at most six.  `docs/397` gives an exact fractional packing of such pairs
with total weight equal to the boundary minority mass.  Since a boundary graph
contains at most three owner vertices, the witness paths have only finitely many
owner/bridge/label signatures.  This chapter performs the resulting constant-loss
localization.

The statements are general.  They do not identify which fixed signature is
geometrically useful for a new prime-patching rotation.

## 1. Canonical witness signatures

Fix a total order on the vertices and edges of a feasible boundary graph.  For
every ordered conflict pair

```text
x in X_R^0,
x' in X_R^1,
```

choose the lexicographically first shortest path from `x` to `x'`.  By `PP3bwb`,
the path is simple and uses at most three owner vertices.

Its **signature** records:

1. the ordered list of owner vertices on the path;
2. for each consecutive owner pair, whether the path uses their direct edge or
   one intermediate boundary vertex;
3. the ordered binary label word on all path edges.

The identities of intermediate boundary vertices are not part of the signature.
The endpoint phases force the XOR of the label word to be one.

### Theorem PP3bwf -- PROVED / AT MOST 510 CONFLICT SIGNATURES

If a boundary-graph component contains `r<=3` owner vertices, the number of
possible canonical conflict signatures is at most

```text
S_r
 = sum_(k=1)^r (r)_k 2^k 3^(k-1),
```

where `(r)_k=r(r-1)...(r-k+1)`.  In particular,

```text
S_1=2,
S_2=28,
S_3=510.
```

#### Proof

Suppose the path uses exactly `k` owners.  Their ordered list has `(r)_k`
possibilities.  For a fixed owner list, let `j` of the `k-1` owner gaps use an
intermediate boundary vertex.  There are `binom(k-1,j)` bridge patterns, and the
path then has

```text
ell=k+1+j
```

edges: two endpoint edges, one edge for every direct owner gap, and two edges for
every boundary-mediated gap.  Exactly half of the binary words of length `ell`
have odd XOR, giving `2^(ell-1)=2^(k+j)` label words.  Summing over `j` gives

```text
sum_(j=0)^(k-1) binom(k-1,j) 2^(k+j)
 = 2^k 3^(k-1).
```

Now sum over `k`.  Direct substitution gives `2`, `28`, and `510`. ∎

The constant counts every permitted local parity pattern; it does not depend on
the number or sizes of boundary components.

## 2. Fixed-signature fractional packing

Let `lambda_(x,x')` be a maximum fractional conflict packing from `PP3bwe`, so

```text
sum_(x,x') lambda_(x,x')=q_R.
```

Assign every conflict pair to its canonical witness signature.

### Theorem PP3bwg -- PROVED / FIXED-SIGNATURE PACKING LOCALIZATION

Some one signature class carries fractional packing weight at least

```text
q_R/510.
```

The restriction of `lambda` to that class remains a feasible fractional conflict
packing.  Hence all of its positive-weight pairs admit parity-odd witnesses with:

- one fixed ordered owner list;
- one fixed direct-versus-boundary bridge pattern;
- one fixed edge-label word.

If every boundary component in `R` has size at most `L`, the class contains at
least

```text
ceil(q_R/(510L))
```

distinct positive-weight conflict pairs.

#### Proof

There are at most 510 signature classes by `PP3bwf`; pigeonholing the total
packing weight `q_R` gives one class of weight at least `q_R/510`.  Deleting all
other packing edges can only reduce the load incident to each boundary vertex,
so feasibility is preserved.

Every individual packing edge has weight at most the capacity of either endpoint,
and therefore at most `L`.  A class of total weight at least `q_R/510` must then
contain at least `ceil(q_R/(510L))` positive-weight edges. ∎

Thus a large conflict packing cannot remain an unstructured mixture of local
parity mechanisms.

## 3. Global localization from recleaning cost

The boundary constraint graph has at most `|T|<=3` connected components, because
every graph component contains an owner vertex.

### Corollary PP3bwh -- PROVED / GLOBAL FIXED-SIGNATURE CORE

Let `Q` be total boundary minority mass and `c_min` the exact recleaning cost.
Some graph component and one canonical witness signature carry a feasible
fractional conflict packing of weight at least

```text
Q/1530.
```

Since `c_min<=Q+3`, the same lower bound is at least

```text
max(c_min-3,0)/1530.
```

Under a global boundary-component cap `L`, this fixed-signature core contains at
least

```text
ceil(max(c_min-3,0)/(1530L))
```

distinct conflict pairs whenever the numerator is positive.

#### Proof

One of at most three graph components has minority mass at least `Q/3`.  Apply
`PP3bwg` inside that component, losing at most the factor 510.  The cost form
follows from `Q>=c_min-3`, which is `PP3bvy` rearranged.  Apply the distinct-edge
bound from `PP3bwg`. ∎

## 4. Revised local obstruction

A high-cost covering rotation now yields, with absolute constant loss, a local
core in which every conflict witness has the same owner order, bridge pattern,
and parity-label word.  The remaining geometry may therefore be studied one of
at most 510 finite witness types at a time.

The next conversion target is to show that a large fixed-signature packing either
has small total mass across pair-safe rotations or supplies a new rotation/trade
that clears its common owner skeleton.

The next theorem identifier after this chapter is `PP3bwi`.
