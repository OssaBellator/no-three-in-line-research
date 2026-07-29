# Rooted biclique extraction from codegree fans

`docs/407` shows that direct-clean expansion failure produces a root source and
a dyadic fan of other sources sharing comparable numbers of targets with the
root.  This chapter extracts a common target pattern from such a fan.  The
result is a rooted complete bipartite collision core of any prescribed order
up to the fan codegree scale.

The statements are general.  They do not yet convert the extracted biclique
into a new clean repair layer.

## 1. Unweighted rooted bicliques

Let `x` be a root source with

```text
d=|N(x)|.
```

Let `F` be a finite family of other sources satisfying

```text
|N(x) intersect N(x')|>=a
```

for every `x' in F`.

### Theorem PP3byc -- PROVED / ROOTED TARGET-SUBSET BICLIQUE EXTRACTION

For every integer `q` with

```text
1<=q<=a,
```

there is a `q`-element target set

```text
Q subseteq N(x)
```

contained in the neighbourhood of at least

```text
ceil(|F| binom(a,q)/binom(d,q))
```

sources from `F`.

Equivalently, the action graph contains a rooted complete bipartite subgraph
with target side `Q` and source side consisting of the root together with those
fan sources.

#### Proof

Each source `x' in F` contains at least

```text
binom(a,q)
```

`q`-subsets of `N(x)` inside `N(x')`.  Count pairs `(x',Q)` with

```text
Q subseteq N(x) intersect N(x'),
|Q|=q.
```

There are at least `|F| binom(a,q)` such pairs and only `binom(d,q)` possible
sets `Q`.  One target set has at least the ceiling of the average number of
incident fan sources. ∎

For `q=1` this recovers a target hub.  Values `q>=2` produce a genuinely richer
common-target pattern.

## 2. Weighted fan localization

Give each fan source a nonnegative weight `w(x')` and put

```text
W=sum_(x' in F) w(x').
```

### Theorem PP3byd -- PROVED / WEIGHTED ROOTED BICLIQUE MASS

For every `1<=q<=a`, some `q`-target set `Q subseteq N(x)` is contained in fan
sources of total weight at least

```text
W binom(a,q)/binom(d,q).
```

#### Proof

Weight every incidence pair `(x',Q)` by `w(x')`.  Each source contributes its
weight to at least `binom(a,q)` target subsets.  The total weighted incidence
mass is at least `W binom(a,q)`.  Average over the `binom(d,q)` possible target
sets. ∎

This form can be applied directly to fractional obstruction mass rather than
only to the number of fan sources.

## 3. Dyadic fan consequence

Suppose the fan is one level from `PP3bxl`, so for some integer `j`,

```text
a=2^j,
F=F_j(x),
2^j |F|>L_A(x)/(2J),
J=1+floor(log_2 d).
```

### Corollary PP3bye -- PROVED / SINGLE-SCALE ROOTED BICLIQUE CORE

For every `1<=q<=2^j`, one `q`-target set in `N(x)` is shared by at least

```text
ceil(
 |F_j(x)| binom(2^j,q)/binom(d,q)
)
```

fan sources.

In particular, when `j>=1`, two targets are shared by at least

```text
ceil(
 |F_j(x)| 2^j(2^j-1)/[d(d-1)]
)
```

fan sources.  Using the dyadic load inequality, the non-ceiled quantity is
strictly larger than

```text
L_A(x)(2^j-1)/[2J d(d-1)].
```

#### Proof

Apply `PP3byc` with `a=2^j`.  For `q=2`, use

```text
binom(2^j,2)/binom(d,2)
 =2^j(2^j-1)/[d(d-1)]
```

and multiply the strict inequality

```text
2^j |F_j(x)|>L_A(x)/(2J)
```

by `(2^j-1)/[d(d-1)]`. ∎

The direct-clean obstruction is therefore no longer only one busy target or
one high-codegree root.  At a single overlap scale it contains a common target
pattern of controlled order, which can be used as the fixed core of a new
repair template or trade.

## 4. Finite diagnostic

Run

```bash
python scripts/check_rooted_biclique_extraction.py
```

The script exhausts roots, fan subfamilies, and target-subset orders in a stored
action graph, comparing the exact strongest common-target multiplicity with the
unweighted and weighted averaging bounds.

The next theorem identifier after this chapter is `PP3byf`.
