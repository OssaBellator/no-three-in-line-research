# Two-sided heavy rectangles from Hall target mass

`docs/418` transfers a backward Hall obstruction to a capacity-weighted target
law and proves that positive mass lands on high-multiplicity targets.  This
chapter transfers that target mass back to the source side.  The result is a
two-sided dense incidence rectangle: many sources devote a definite fraction
of their available capacity to many high-multiplicity targets.

The statements are general.  They do not classify these rectangles in the
prime-patching incidence graph.

## 1. The source-target joint law

Let `U` be a finite source set, let targets have positive capacities `v(y)`,
and put

```text
D(x)=sum_(y in N(x)) v(y).
```

Let `mu` be a probability distribution on `U`.  Define the joint incidence law

```text
J(x,y)=mu(x) v(y)/D(x)  when y in N(x),
       =0                otherwise.
```

Its target marginal is

```text
nu(y)=sum_x J(x,y).
```

For `H subseteq Y`, define the source-side `H` density

```text
g_H(x)=sum_(y in H intersect N(x)) v(y)/D(x).
```

### Proposition PP3bzk -- PROVED / EXACT TWO-SIDED MASS IDENTITY

For every target set `H`,

```text
nu(H)=sum_x mu(x) g_H(x).
```

Thus target mass is exactly the `mu`-average fraction of source capacity devoted
to `H`.

#### Proof

Interchange the source and target sums in the definition of `nu(H)`. ∎

## 2. Heavy-source extraction

Assume

```text
nu(H)>=eta.
```

For `0<=alpha<eta`, put

```text
X_alpha={x:g_H(x)>=alpha}.
```

### Theorem PP3bzl -- PROVED / HEAVY-SOURCE RECTANGLE MASS

One has

```text
mu(X_alpha)>=(eta-alpha)/(1-alpha).
```

#### Proof

Write `s=mu(X_alpha)`.  Since `g_H(x)<alpha` outside `X_alpha` and
`g_H(x)<=1` everywhere,

```text
eta
 <=sum_x mu(x)g_H(x)
 <=alpha(1-s)+s.
```

Rearrange. ∎

Hence a positive target mass cannot be supported only by sources that see an
arbitrarily small fraction of the target set.

## 3. Cardinality and row-degree consequences

Suppose additionally that

```text
max_x mu(x)<=gamma,
max_y nu(y)<=delta,
```

and that every single target atom in one source row satisfies

```text
v(y)/D(x)<=beta.
```

### Theorem PP3bzm -- PROVED / TWO-SIDED HEAVY INCIDENCE RECTANGLE

Under the preceding hypotheses,

```text
|X_alpha|
 >=ceil((eta-alpha)/((1-alpha)gamma)),
```

```text
|H|>=ceil(eta/delta),
```

and every `x in X_alpha` is incident with at least

```text
ceil(alpha/beta)
```

distinct targets of `H`.

#### Proof

The first two bounds divide the corresponding probability masses by the
largest atom.  For the last bound, fewer than `alpha/beta` target atoms, each at
most `beta`, cannot carry row mass `alpha`. ∎

Thus a Hall obstruction that is diffuse on both marginals yields a genuinely
large bipartite rectangle: many sources, many high-multiplicity targets, and a
uniform lower bound on the target degree of every selected source.  If either
cardinality conclusion fails, the obstruction has already localized to one
large source or target atom.

## 4. Revised localized-Hall frontier

The backward-walk branch now has the following alternatives.

1. Large endpoint or target atoms give a bounded collision core.
2. Otherwise, high target multiplicity spreads to a two-sided dense incidence
   rectangle.
3. The rectangle can be attacked by codegree, biclique, or target-reservoir
   arguments.

This connects the Hall-walk frontier directly to the rooted-biclique and
residual-layer frontiers.

## 5. Exact diagnostic

Run

```bash
python scripts/check_hall_heavy_rectangles.py
```

The checker uses exact rational capacities and source weights to verify the
joint-law identity, heavy-source mass, both atom-count bounds, and every
selected row-degree conclusion.

The next theorem identifier after this chapter is `PP3bzn`.
