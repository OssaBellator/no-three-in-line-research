# Fractional layer banks and exact expansion for direct-clean repair

`docs/355` proves that two globally target-disjoint deterministic repair layers
attain the exact `m=10` direct-clean reverse load `1/2`. This chapter gives the
general fractional theorem behind that coincidence. It separates three notions:
source degree, neighbourhood expansion, and finite layer-bank realizability.

The statements are general. They do not prove any new direct-clean expansion
bound beyond the audited range.

## 1. Exact fractional congestion

Let `G=(S,T,E)` be a finite source-target action graph. A supported policy is a
row-stochastic matrix `P` satisfying

```text
P(x,y)>=0,
P(x,y)=0 when xy is not an edge,
sum_y P(x,y)=1 for every x in S.
```

Its reverse-column load is

```text
lambda(P)=max_(y in T) sum_(x in S) P(x,y),
```

and let `lambda_*` be the infimum over all supported policies.

### Theorem PP3bvp -- PROVED / EXACT FRACTIONAL EXPANSION FORMULA

One has

```text
lambda_*
 = max_(nonempty A subseteq S) |A|/|N(A)|.
```

#### Proof

For any supported policy and any nonempty `A subseteq S`, all row mass from `A`
lands in `N(A)`. Hence

```text
|A|
 = sum_(x in A) sum_(y in N(A)) P(x,y)
 <= |N(A)| lambda(P).
```

This proves the lower bound.

For the converse, fix `lambda` satisfying

```text
|A| <= lambda |N(A)|
```

for every `A`. Build a flow network with capacity one from the source vertex to
each `x in S`, infinite capacity on every action edge `x->y`, and capacity
`lambda` from each `y in T` to the sink. A finite cut is determined by a source
subset `A` and must retain `N(A)` on the source side; its capacity is

```text
|S\A| + lambda |N(A)| >= |S|.
```

Thus max-flow/min-cut gives a flow of value `|S|`. Dividing the outgoing flow of
each source by its unit supply produces a supported policy with every target
load at most `lambda`. Taking the least admissible `lambda` proves equality. ∎

This shows that minimum source degree alone is not the upper-bound invariant.
The exact obstruction is a source subset with too small a target neighbourhood.

## 2. Finite fractional layer banks

An `(L,r)` **fractional layer bank** is a family of supported deterministic maps

```text
f_1,...,f_L:S->T
```

such that the total target multiplicity

```text
M(y)=#{(i,x):f_i(x)=y}
```

is at most `r` for every target. Unlike the integral layer packing of `docs/355`,
a target may appear in more than one layer; only its total multiplicity matters.

### Theorem PP3bvq -- PROVED / FINITE BANK REALIZATION OF THE FRACTIONAL OPTIMUM

Every rational supported policy is the uniform average of a finite layer bank.
More precisely, after clearing denominators by an integer `L`, there are maps
`f_1,...,f_L` such that

```text
P(x,y)=#{i:f_i(x)=y}/L.
```

If `P` has maximum column load `lambda` and `L lambda` is integral, this bank is
an `(L,L lambda)` bank.

In particular, the optimum `lambda_*` is rational and is attained by a finite
`(L,r)` bank with

```text
r/L=lambda_*.
```

#### Proof

Choose `L` so that every `LP(x,y)` is an integer. For each source `x`, form a
list containing exactly `LP(x,y)` copies of target `y`; the row-sum condition
makes the list length exactly `L`. Assign its entries arbitrarily to the layer
indices `1,...,L`. This defines the deterministic maps and reproduces `P` after
averaging. Target `y` appears exactly

```text
L sum_x P(x,y)
```

times, giving the multiplicity claim.

The feasible-policy problem is a rational linear program, so it has a rational
optimal extreme point. Apply the construction to that point. ∎

Thus integral target-disjoint layers are the special case `r=1`; fractional
layer banks retain the same finite combinatorial form without demanding perfect
disjointness.

## 3. Expansion and the audited half-charge

### Corollary PP3bvr -- PROVED / EXPANSION-LAYER CONSEQUENCES

If

```text
|N(A)| >= d |A|
```

for every nonempty source subset, then

```text
lambda_* <= 1/d.
```

Conversely, `lambda_*<=1/d` is equivalent to that expansion inequality.
Moreover:

1. a target-disjoint `d`-layer packing is an `(d,1)` bank and certifies
   `lambda_*<=1/d`;
2. if the minimum source degree is `q`, then `lambda_*>=1/q` by applying
   `PP3bvp` to a minimum-degree singleton;
3. when a target-disjoint `q`-layer packing exists, the fractional optimum is
   exactly `1/q`.

#### Proof

The first two statements are immediate from `PP3bvp`; the layer statements
follow from `PP3bvq` and the singleton lower bound. ∎

At `m=10`, `q=2` and the two target-disjoint layers from `docs/353` recover the
exact optimum `1/2`. The asymptotic direct-clean frontier may therefore be
attacked in either of two equivalent fractional forms:

1. prove uniform source-subset target expansion; or
2. construct finite `(L,r)` repair banks with `r/L` uniformly below one.

The next theorem identifier after this chapter is `PP3bvs`.
