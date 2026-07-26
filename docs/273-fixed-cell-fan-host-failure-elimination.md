# Fixed-cell fan host failure collapses to a typed heavy pencil

The thresholded fixed-cell fan theorem PP3ago--PP3agt deletes the partners whose
multiplicity exceeds the credit-per-matching-cell threshold.  Its endpoint still
lists “conditional Hall or endpoint-host failure.”  That phrase is not a separate
frontier in the superregular branch.

If the heavy deletion graph has sublinear maximum degree, standard slicing
preserves a uniform superregular residual host and hence the spread matching law
needed by PP3agp.  If its maximum degree is not sublinear, one endpoint resource
already supports a large uniform heavy partner pencil, which is the typed output
of PP3agq--PP3ags.  Matching failure is an even stronger instance of the latter
case.

This chapter removes the untyped host leaf.  It does not pay the resulting heavy
partner pencil or residual source/off-fan concentration.

## 1. Sparse heavy deletion preserves the host

Let

```text
H=(L,R;E), |L|=|R|=n,
```

be `(epsilon,delta)`-superregular.  Let `D subseteq E` be the heavy partner graph
and write `Delta(D)` for its maximum typed-resource degree.  Choose a function
`eta=eta(n)` with

```text
eta -> 0.
```

### Proposition PP3bba -- PROVED

If

```text
Delta(D)<=eta n,
```

then for every fixed `epsilon'>epsilon`,

```text
H\D is (epsilon',delta-o(1))-superregular.
```

In particular, for all sufficiently large `n`, it is
`(epsilon',delta/2)`-superregular and has a perfect matching.

#### Proof

Every degree loses at most `eta n=o(n)`.  For sets
`X subseteq L`, `Y subseteq R` of size at least `epsilon'n`, the number of
deleted edges in `X x Y` is at most

```text
|X| Delta(D)<=eta n |X|,
```

so the density changes by at most `eta/epsilon'=o(1)`.  Combine this with the
parent regularity discrepancy and the minimum-degree loss. ∎

### Corollary PP3bbb -- PROVED FROM THE EXISTING SUPERREGULAR SPREAD THEOREM

Under PP3bba, the graph `H\D` has the common fixed-rank spread perfect-matching
law required by PP3agp, with a constant depending only on one fixed residual
parameter class.

#### Proof

For large `n`, every sparse-deletion residual is
`(epsilon',delta/2)`-superregular.  Apply the established spread theorem with
these common parameters. ∎

Thus the “required spread perfect-matching law” in PP3agp is automatic whenever
heavy deletion is sublinear at every resource.

## 2. Non-sparse deletion is already the typed obstruction

### Proposition PP3bbc -- PROVED

If PP3bba fails, then one typed endpoint resource is incident with more than

```text
eta n
```

heavy partners.  Every partner `b` in this pencil satisfies

```text
mu(b)>theta=tau C_a/(2n).
```

If `eta=m^{-o(1)}` at the slab-optimal scale, the pencil contains a target
`W`-sized subpencil.

#### Proof

Failure is exactly `Delta(D)>eta n`; choose a resource attaining the maximum.
The multiplicity bound is the definition of the heavy graph.  At the slab scale
`n=m^(19/20+o(1))` and `W=m^(19/40+o(1))`, so
`eta n/W=m^(19/40-o(1))` tends to infinity. ∎

### Proposition PP3bbd -- PROVED

If deleting the heavy graph destroys every perfect matching, then the same typed
heavy-pencil conclusion holds with the fixed positive density bound

```text
Delta(D)>=epsilon(delta-epsilon)n.
```

There is no additional conditional Hall object to retain.

#### Proof

This is the robust Hall deletion theorem PP3agq.  Its conclusion is already a
linear maximum-degree witness in the heavy graph.  Choosing a resource attaining
that degree gives the uniform heavy partner pencil.  A Hall rectangle may certify
why matching failed, but the typed maximum-degree output is always present and is
the stronger frontier object used next. ∎

## 3. Candidate credit carried by the pencil

### Corollary PP3bbe -- PROVED

A heavy pencil `P` of size `h` carries more than

```text
h theta=h tau C_a/(2n)
```

distinct candidate incidences, and admits a factor-two dyadic subpencil after
only an `m^(o(1))` loss at polynomial scales.

#### Proof

Candidate sets of different partners in one fixed choice row or column are
pairwise disjoint by PP3afh.  Sum the strict lower multiplicity bound and apply
PP3agr--PP3ags. ∎

Thus the dense-deletion output is not merely a large endpoint degree; it carries
typed, distinct current-potential credit.

## 4. Revised fixed-cell fan endpoint

### Theorem PP3bbf -- PROVED / CONDITIONAL TYPED PAID ENDPOINTS

A fixed-cell binary fan produced by the dense current-support row has exactly one
of the following outcomes.

1. Heavy deletion has sublinear maximum degree; the residual host is uniformly
   superregular, the spread law is automatic, and PP3agp either pays the light fan
   or exposes source/off-fan concentration.
2. One endpoint resource supports a target-size uniform heavy partner pencil with
   credit-scale distinct candidate incidences.
3. Residual source or off-fan insertion mass is already at the removal-credit
   scale.

It does not terminate in an untyped conditional Hall or endpoint-host failure.

#### Proof

Apply PP3bba--PP3bbb in the sparse case and PP3bbc in the complementary case.
If matching itself fails after deletion, PP3bbd gives the second outcome directly.
Candidate credit is PP3bbe.  These alternatives exhaust the maximum-degree
dichotomy. ∎

### Corollary PP3bbg -- PROVED

For the dense current-support row, fixed-cell fan feasibility is closed.  The
remaining fixed-cell work is payment or conversion of the typed heavy partner
pencil and any explicit source/off-fan concentration; host existence and spread
matching are no longer independent assumptions.

Together with PP3bat--PP3baz, the current row no longer has residual-host leaves
in either the two-resource choice-grid or fixed-cell fan branches.

The arc/path-petal weighted endpoints, dense source-support row, global prime-
minus-one seed theorem, and the no-three-in-line conjecture remain open.

## 5. Finite diagnostic

Run

```bash
python scripts/check_fixed_cell_fan_host_elimination.py \
  experiments/fixed-cell-fan-host-elimination-example.json
```

The checker exhaustively verifies a sparse finite deletion residual and separately
confirms that a non-sparse deletion is reported as a typed maximum-degree heavy
pencil rather than as an unclassified host failure.
