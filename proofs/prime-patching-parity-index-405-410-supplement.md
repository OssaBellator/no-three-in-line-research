# Prime-patching parity index supplement: `docs/405--410`

This supplement continues the cumulative parity index after `docs/404`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bxd--PP3bxf | A fixed-signature boundary packing has bounded boundary-set multiplicity and contains a sunflower whose common boundary core has at most three vertices while all remaining petals are disjoint | PROVED | `docs/405-sunflower-localization-for-fixed-signature-boundary-witnesses.md` |
| PP3bxg--PP3bxi | Every finite-depth Hall ratio is a convex average of preceding ratios; failure propagates along a nested overlap path and places quantitative endpoint mass on raw-congestion sources | PROVED | `docs/406-backward-averaging-and-bad-paths-for-hall-walk-certificates.md` |
| PP3bxj--PP3bxl | Rooted codegree load is exactly excess target multiplicity; direct-clean expansion failure forces a target hub and a single-scale common-target fan | PROVED | `docs/407-target-hubs-and-dyadic-codegree-fans-for-direct-clean-failure.md` |
| PP3bxm--PP3bxo | One dyadic support-chord type has short two-arc corridors and yields either a cycle-vertex hub or a square-root-sized bank of vertex-disjoint corridors | PROVED | `docs/408-corridor-hubs-and-disjoint-banks-for-dyadic-support-chord-types.md` |
| PP3bxp--PP3bxr | Scale-dependent invariant drops bound the complete shell exceedance tail; rational threshold and power-law profiles give horizon-free product criteria | PROVED | `docs/409-scale-sensitive-invariant-budgets-for-shell-products.md` |
| PP3bxs--PP3bxv | Block reverse loads form nonnegative type matrices that compose elementwise, absorb type-dependent conditioning diagonally, and admit spectral-radius contraction | PROVED | `docs/410-typed-load-matrices-for-multistage-frontier-composition.md` |

## Frontier update

### Boundary recleaning

The hub branch and disjoint-bank branch from `docs/399` are now unified.
For one fixed signature, the boundary sets contain a sunflower.  In the
worst four-role case its size is at least

```text
ceil(((c_min-3)/(881280 L))^(1/4)).
```

All witness paths share one boundary core of size at most three and are
boundary-disjoint outside it.  The remaining geometric classification has
only finitely many core-role patterns.

### Localized Hall transport

The depth ratios satisfy the exact local recursion

```text
r_t(x)=sum_(x') pi_t(x,x') r_(t-1)(x').
```

A failed depth-`t` certificate contains a nested length-`t` bad path ending at
a source with excessive raw average target multiplicity.  If a depth ratio is
near the global raw maximum, a quantified fraction of backward-walk mass ends
on the raw-maximal set.

### Fractional direct-clean layers

For a root source,

```text
sum_(x'!=x) codeg(x,x')
 =sum_(y in N(x))(m_A(y)-1).
```

Thus expansion failure forces an actual target column reused by many sources.
After one logarithmic localization, it also forces many neighbours sharing
comparable numbers of targets with the root.

### Support-chord repair words

A fixed dyadic chord type with indices `j_A,j_B` lies in a two-arc corridor of
size at most

```text
2^(j_A+1)+2^(j_B+1).
```

A large weighted family either concentrates on one cycle vertex or contains a
bank of vertex-disjoint corridors.  Local repair words may therefore be built
independently on the bank branch.

### Clean-macro shells

If an expansion factor above `u` forces invariant drop at least `eta(u)`, then

```text
q(u)<=J_0/eta(u)
```

and the whole positive shell product is bounded by

```text
exp(J_0 integral du/[u eta(u)]).
```

A power-growing drop profile gives a horizon-free exponential bound, while
the rational threshold version remains exactly machine-checkable.

### Integration

Every stage can now export a block load matrix.  Compatible stages obey

```text
M_(PQ)<=M_P M_Q,
```

type-dependent conditioning is a diagonal penalty, and a repeated type
envelope contracts whenever its spectral radius is below one.  This can
retain sparse transition structure that is invisible to scalar overlap
bounds.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_405_410.py
```

or individually with

```bash
python scripts/check_fixed_signature_boundary_sunflowers.py
python scripts/check_overlap_walk_backward_averaging.py
python scripts/check_direct_clean_target_hubs.py \
  experiments/direct-clean-target-hub-example.json
python scripts/check_support_chord_corridor_banks.py
python scripts/check_scale_sensitive_shell_invariants.py
python scripts/check_typed_load_matrix_composition.py
```

The local audits cover 33,792 uniform set families, exact depth-six backward
walk distributions, every source subset of the stored action graph, 3,858
support-chord configurations through cycle length twelve, 625 rational shell
profiles, and exact rational typed-kernel compositions.

The next available theorem identifier is `PP3bxw`.
