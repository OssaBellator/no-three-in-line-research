# Facet-normal adapter for threshold schedules

The threshold row in `docs/543--548` is expressed in quotient resource
coordinates, while the final geometric construction is constrained by many
individual threshold inequalities.  This chapter gives the exact linear adapter
from a common discrepancy box to those inequalities.

Let a residual resource vector be `z in Q^r`.  The actual threshold inequalities
are affine functionals whose residual parts are

```text
f_k(z)=c_k dot z,
```

where the finite coefficient rows `c_k` are obtained from the geometric facet
normals after quotienting constants and conserved coordinates.

## 1. Dual box bound

### Theorem PP3cob -- PROVED / THRESHOLD FACET-NORMAL ADAPTER

If every interval residual satisfies

```text
|z_j|<=w_j,
```

then every actual threshold functional satisfies

```text
|f_k(z)|<=sum_j |c_(k,j)| w_j.
```

Thus a finite matrix of facet coefficients converts a quotient discrepancy box
into simultaneous bounds for every geometric threshold inequality.

#### Proof

Apply the triangle inequality to `c_k dot z` and use the coordinate bounds. ∎

## 2. Common boxes survive arbitrary gadget switching

### Theorem PP3coc -- PROVED / SWITCHED THRESHOLD FACET CERTIFICATE

Suppose finitely many zero-sum macrocycles have phases whose prefix sets lie in
one box of coordinate widths `w`.  Then every interval of every arbitrary
concatenation of those cycles satisfies all threshold inequalities with loss at
most

```text
Delta=max_k sum_j |c_(k,j)|w_j.
```

If an endpoint or seam contributes at most `gamma/N`, the ledger row
`Delta+epsilon` is valid from every `N>=ceil(gamma/epsilon)`.

#### Proof

`PP3cmr` bounds every interval residual by the common box widths.  Apply
`PP3cob` to each facet and add the endpoint term. ∎

## 3. Finite adapter verification

### Theorem PP3cod -- PROVED / THRESHOLD NORMAL-MATRIX AUDIT

For a fixed finite geometric threshold system, the adapter consists of:

1. a matrix expressing each residual threshold normal in quotient coordinates;
2. a finite phase certificate for the macrocycles;
3. the exact dual box products `sum_j |c_(k,j)|w_j`.

All three parts are checked by rational arithmetic.  A failed representation
returns a threshold normal outside the declared quotient span; a failed budget
returns the specific facet attaining the excess.

#### Proof

The normal representations are finite linear identities.  The phase search is
finite by `PP3cms`, and the dual products are finite rational sums. ∎

## 4. Stored exact fixture

The audit `scripts/check_threshold_facet_adapter.py` uses the two cycles from
`docs/539`.  Exactly three of their twelve phase pairs fit in a common box of
width `(1,1)`.  Three stored threshold normals are

```text
(1/48,1/96),
(-1/96,1/48),
(1/120,-1/120).
```

Their maximum dual box loss is `1/32`.  With one unit of endpoint price,

```text
1/32+1/N<=1/24
```

for every `N>=96`.  The audit checks every interval in a 170-step mixed
concatenation against every stored facet.

## 5. Prime-patching consequence

The threshold realization gap is reduced to extracting the finite normal matrix
of the actual geometric inequalities and checking that the chosen quotient
coordinates span it.  Once that matrix is known, the common-box schedule gives
all inequalities at once.  The stored normals are an adapter fixture, not yet
the normals of the final prime-patching construction.
