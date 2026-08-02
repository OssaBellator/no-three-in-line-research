# Source-star centre pruning for Hall extraction

`docs/634` gives a sharp 28-resource interface when the partner restriction is a
partial matching and the other two restricted forbidden families have maximum
degree two. This chapter derives the partner-side condition directly from the
stored binary resource-star fixture.

## 1. Exact source-centre catalogue

### Theorem PP3cyi — PROVED / THREE GOOD CENTRES OUT OF FOUR

For `experiments/binary-resource-star-conditioning-example.json`, the four centre
fibres have the following records:

```text
centre  partners  maximum degree  partial matching  residual completions
(0,0)      3            3              no                  0
(0,1)      1            1              yes                 4
(0,2)      0            0              yes                 6
(0,3)      2            1              yes                 3
```

Thus three quarters of the stored centres already satisfy the partner-matching
hypothesis, and the unique bad centre is exactly the unique centre without a
conditional completion.

#### Proof

`scripts/check_hall_source_center_pruning.py` reconstructs the conflict fibres
using the semantics of `scripts/check_binary_resource_star_conditioning.py` and
enumerates all residual perfect matchings. ∎

## 2. Bad-centre pruning formula

### Theorem PP3cyj — PROVED / SOURCE-PRUNED MIXED-DEGREE INTERFACE

Suppose a conditional host has `b` centre resources whose restricted partner
fibres are not partial matchings. If the source and host-defect restrictions have
maximum degree at most two after those centres are removed, then the sharp mixed-
degree Hall pipeline of `docs/634` is available whenever

```text
centred side resources >= 28+b,
opposite side resources >= 28.
```

#### Proof

Delete the `b` bad centre resources. Twenty-eight resources remain on the
centred side, so after selecting the local pair there are twenty-six residual
resources. The collision graph has maximum degree four, hence contains the six-
resource matching-shaped core proved in `docs/634`. The opposite side needs no
centre pruning and retains the original threshold twenty-eight. ∎

## 3. Fixture-typed numerical rate

### Theorem PP3cyk — PROVED / THREE-QUARTER PARTNER-SIDE RATE

A disjoint numerical collection of `t` copies of the stored four-centre fibre
pattern contains exactly `3t` matching-shaped centres and `t` bad centres.
Consequently ten copies are the first integer count supplying at least twenty-
eight good centre resources:

```text
9 copies -> 27 good centres,
10 copies -> 30 good centres.
```

#### Proof

Apply `PP3cyi` independently to each copy. ∎

## Remaining source obligation

`PP3cyk` is only a partner-side counting statement. The repository does not yet
provide ten independent geometric copies with compatible source and host-defect
restrictions, nor an asymptotic bound on bad centres. The Hall row therefore
remains unpromoted.
