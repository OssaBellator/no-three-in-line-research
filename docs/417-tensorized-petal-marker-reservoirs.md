# Tensorized petal-marker reservoirs

`docs/411` turns one sunflower petal reservoir into a fractional repair layer.
This chapter shows that several independently retained petal markers amplify the
degree multiplicatively while target reuse is controlled by the strongest
single marker. The result gives a concrete reason to search for two or three
small marker-preserving choices instead of one very large reservoir.

The statements are abstract source-target interfaces. They do not construct
marker-preserving prime-patching moves.

## 1. Product marker channels

Let `S` be a finite source set. For each marker channel `i=1,...,k`, let
`R_i(x)` be a nonempty finite set of marker values available from source `x`.
Assume

```text
|R_i(x)|>=q_i
```

for every source, and every marker value in channel `i` belongs to at most
`h_i` source reservoirs.

A **tensorized target** is a tuple

```text
(y_1,...,y_k) in product_i R_i(x).
```

The action graph joins `x` to every such tuple.

### Theorem PP3byp -- PROVED / TENSORIZED MARKER LOAD

The tensorized action graph has minimum source degree at least

```text
Q=product_i q_i
```

and every target tuple is adjacent to at most

```text
h=min_i h_i
```

sources. Hence its optimum fractional reverse load satisfies

```text
lambda_*<=h/Q.
```

In particular, it is a strict contraction whenever `Q>h`.

#### Proof

The degree statement is the Cartesian-product count. If a target tuple is
adjacent to a source, then that source lies in the decoder set of each one of
its coordinates. Its source multiplicity is therefore at most the smallest
coordinate decoder multiplicity, namely `h`. The uniform policy on all tuple
targets gives each source action mass at most `1/Q`, so every target column has
load at most `h/Q`. Equivalently, apply the bounded-reuse criterion from
`docs/411`. ∎

The important point is that target reuse does not multiply with the number of
channels. The tuple retains every marker simultaneously, so one low-reuse
coordinate already controls the source ambiguity.

## 2. Exact disjoint-marker optimum

### Corollary PP3byq -- PROVED / EXACT MULTIMARKER AMPLIFICATION

Suppose some channel is an intrinsic petal marker, meaning its marker reservoirs
are pairwise disjoint across sources. Then `h=1` and

```text
lambda_*<=1/Q.
```

If every source has exactly `Q` tuple targets, then

```text
lambda_*=1/Q.
```

#### Proof

The intrinsic marker channel has `h_i=1`, so `PP3byp` gives the upper bound.
A minimum-degree singleton gives the lower bound `lambda_*>=1/Q` by the exact
fractional expansion formula `PP3bvp`. ∎

Thus two binary petal markers already give exact load `1/4`; three give `1/8`.
The markers need not be individually rich.

## 3. Conditioning and marker loss

Often only part of the Cartesian product survives the clean or pair-safe
constraints. Let `G(x)` be the retained tuple set and assume

```text
|G(x)|>=alpha Q
```

for a common `alpha>0`.

### Theorem PP3byr -- PROVED / CONDITIONED TENSOR RESERVOIR

If every retained tuple is still decoded by at most `h` sources, then the
uniform retained policy obeys

```text
lambda<=h/(alpha Q).
```

Consequently strict contraction follows from

```text
alpha Q>h.
```

If this criterion fails for a proposed family of marker channels, then at least
one of the following geometric obstructions occurs:

1. some source retains fewer than `alpha Q` clean tuples;
2. some final target erases enough marker information to be reachable from more
   than `h` sources.

#### Proof

Each retained action has probability at most `1/(alpha Q)`. A target receives
contribution from at most `h` sources, proving the load bound. The obstruction
statement is the contrapositive of the two hypotheses. ∎

## 4. Revised petal frontier

The sunflower branch now has a multiplicative construction target. It is enough
to find a bounded number of small local choices whose final clean target retains
all marker coordinates. A single intrinsic coordinate prevents source
collisions, while the remaining coordinates multiply the repair degree.

This suggests auditing two-step and three-step petal-local words before seeking
a large one-step reservoir.

## 5. Exact diagnostic

Run

```bash
python scripts/check_tensorized_petal_marker_reservoirs.py
```

The checker enumerates every source subset in a stored three-channel action
graph and verifies the exact load, the tensor bound, and a conditioned
subfamily.

The next theorem identifier after this chapter is `PP3bys`.
