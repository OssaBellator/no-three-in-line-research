# Residual expansion after rooted-biclique conditioning

`docs/413` extracts a set of sources sharing a small common target core. A
common core is useful only if the actions outside it still expand. This chapter
gives the exact residual criterion: delete the common targets, use every
remaining action uniformly, and either obtain contraction or expose a second
high-multiplicity target outside the core.

The statements are general. They do not prove the required residual degree for
prime-patching biclique cores.

## 1. Common-core deletion

Let `F` be a nonempty source set in an unweighted action graph. Suppose every
source contains a common target set

```text
C subseteq N(x),
|C|=q.
```

Define the residual reservoir

```text
R(x)=N(x)\C
```

and residual target multiplicity

```text
m_R(y)=#{x in F:y in R(x)}.
```

### Theorem PP3byv -- PROVED / RESIDUAL BOUNDED-REUSE LAYER

Assume

```text
|R(x)|>=d_R>0
```

for every source and

```text
m_R(y)<=h_R
```

for every residual target. Then the uniform residual policy has reverse load
at most

```text
h_R/d_R.
```

Consequently the residual action graph has

```text
lambda_*<=h_R/d_R
```

and contracts whenever `d_R>h_R`.

#### Proof

Each source assigns probability at most `1/d_R` to any residual target. At most
`h_R` sources reach that target, so its column load is at most `h_R/d_R`. ∎

The common biclique core is never used by this policy. It serves only to define
a structured source tranche on which the residual actions are audited.

## 2. Degree inherited from the original graph

### Corollary PP3byw -- PROVED / BICLIQUE-CORE DELETION ENVELOPE

If the original action degree satisfies

```text
|N(x)|>=d_0
```

for every `x in F`, then

```text
|R(x)|>=d_0-q.
```

Hence, when `d_0>q`,

```text
lambda_*<=h_R/(d_0-q).
```

Strict contraction follows from

```text
d_0-q>h_R.
```

#### Proof

Deleting the `q` common targets removes at most `q` neighbours from each source.
Apply `PP3byv`. ∎

This quantifies the tradeoff in the biclique order: a larger common core gives
more structure but consumes more residual degree.

## 3. Failure dichotomy

### Theorem PP3byx -- PROVED / SECOND-HUB OR RESIDUAL CONTRACTION

Fix proposed parameters `d_R` and `h_R`. For a rooted biclique source family
`F`, exactly one of the following audit outcomes occurs:

1. every source has at least `d_R` residual actions and every residual target has
   multiplicity at most `h_R`, yielding load at most `h_R/d_R`;
2. some source has fewer than `d_R` residual actions;
3. some target outside the common core is reached by at least `h_R+1` sources.

Thus failure of the residual contraction audit returns either a low-residual-
degree source or a **second target hub** outside the extracted core.

#### Proof

If neither obstruction 2 nor obstruction 3 occurs, the hypotheses of `PP3byv`
hold and outcome 1 follows. The three outcomes exhaust the audit. ∎

## 4. Revised direct-clean frontier

A direct-clean Hall failure now yields a rooted common-target biclique. After
conditioning on that core, the next step is finite and explicit:

1. delete the common target core;
2. count residual actions per source;
3. count residual target multiplicities.

Either the residual graph contracts immediately or the obstruction becomes a
second target hub, creating a richer two-core collision object.

## 5. Exact diagnostic

Run

```bash
python scripts/check_residual_biclique_expansion.py
```

The checker enumerates all source subsets of a stored common-core graph and
verifies exact residual expansion, the uniform load bound, and the second-hub
dichotomy.

The next theorem identifier after this chapter is `PP3byy`.
