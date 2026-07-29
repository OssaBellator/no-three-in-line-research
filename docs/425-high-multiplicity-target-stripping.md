# High-multiplicity target stripping and optimized residual layers

`docs/419` studies the residual action graph after deleting one rooted biclique
core.  This chapter removes the need to guess that core in advance.  For any
multiplicity threshold, delete every target above the threshold.  Either the
remaining graph is already a contracting repair layer, or one source is
incident with many high-multiplicity target hubs.

The statements are general.  They do not prove the required residual degree
profile for prime-patching actions.

## 1. Threshold residual graphs

Let `G=(S,T,E)` be a finite unweighted action graph.  Write

```text
m(y)=#{x:y in N(x)}.
```

For an integer `h>=1`, define the high-multiplicity target set

```text
H_h={y:m(y)>h}
```

and the residual degree

```text
d_h(x)=|N(x)\H_h|,
d_h=min_x d_h(x).
```

### Theorem PP3bzn -- PROVED / HUB-STRIPPING RESIDUAL CONTRACTION

If `d_h>0`, then

```text
lambda_*<=h/d_h.
```

More generally, for a proposed residual degree `d_R`, either every source
retains at least `d_R` targets and

```text
lambda_*<=h/d_R,
```

or some source `x` is adjacent to more than

```text
d(x)-d_R
```

targets of multiplicity greater than `h`.

#### Proof

Use only targets outside `H_h` and choose uniformly among the retained actions.
Every source row has at least `d_h` entries, while every retained target has at
most `h` predecessors.  Its column load is therefore at most `h/d_h`.

For the dichotomy, if a source retains fewer than `d_R` targets, then more than
`d(x)-d_R` of its neighbours lie in `H_h`. ∎

## 2. Optimizing the threshold

### Theorem PP3bzo -- PROVED / MULTIPLICITY-THRESHOLD ENVELOPE

The direct-clean optimum obeys

```text
lambda_*
 <=min_(h:d_h>0) h/d_h.
```

The high-target set also satisfies

```text
|H_h|<=|E|/(h+1).
```

#### Proof

Take the best bound from `PP3bzn`.  Every target in `H_h` contributes at least
`h+1` incidences, so double counting gives the cardinality bound. ∎

The envelope automatically balances two competing effects: increasing `h`
admits more targets but also permits greater reverse reuse.

## 3. Failure produces a multiplicity-tail star

### Theorem PP3bzp -- PROVED / SOURCE-SIDE HUB-TAIL OBSTRUCTION

If

```text
lambda_*>rho,
```

then for every threshold `h` with `d_h>0` one has

```text
d_h<h/rho.
```

Consequently some source `x_h` is adjacent to more than

```text
d(x_h)-h/rho
```

targets whose multiplicity exceeds `h`.

#### Proof

Otherwise `d_h>=h/rho`, and `PP3bzn` would give
`lambda_*<=h/d_h<=rho`.  Choose a source attaining the minimum residual
degree and count its deleted neighbours. ∎

A failed residual-layer certificate therefore supplies a source-side
multiplicity tail at every useful threshold.  This is stronger than one
isolated target hub: the obstruction persists across a range of target
multiplicity scales.

## 4. Revised fractional-layer frontier

After any rooted biclique extraction, apply the threshold envelope to the
remaining targets.

- If one threshold gives `h<d_h`, there is an immediate strict fractional
  layer.
- Otherwise, `PP3bzp` gives a source incident with many residual hubs.
- Those hubs can be fed back into the two-sided rectangle or biclique
  extraction machinery.

This yields an iterative core-stripping procedure with a quantitative stopping
criterion.

## 5. Exact diagnostic

Run

```bash
python scripts/check_high_multiplicity_target_stripping.py
```

The checker enumerates every source subset of a stored action graph, computes
the exact expansion optimum, verifies every threshold envelope, and checks the
tail obstruction below the exact optimum.

The next theorem identifier after this chapter is `PP3bzq`.
