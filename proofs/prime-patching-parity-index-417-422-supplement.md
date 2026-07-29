# Prime-patching parity index supplement: `docs/417--422`

This supplement continues the cumulative parity index after `docs/416`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3byp--PP3byr | Independent petal-marker channels tensorize their repair degree while tuple-target ambiguity is controlled by the strongest marker; conditioning costs only inverse retained tuple density | PROVED | `docs/417-tensorized-petal-marker-reservoirs.md` |
| PP3bys--PP3byu | Backward Hall endpoint mass transfers exactly to capacity-weighted target multiplicity and yields either many high-multiplicity targets or concentrated target merging | PROVED | `docs/418-endpoint-to-target-transfer-for-hall-obstructions.md` |
| PP3byv--PP3byx | Deleting a rooted biclique target core leaves a residual bounded-reuse repair layer; failure exposes low residual degree or a second target hub outside the core | PROVED | `docs/419-residual-expansion-after-rooted-biclique-conditioning.md` |
| PP3byy--PP3bza | Corridor-bank word kernels have load `h/q` within a bank and `gh/q` after combining bank colors; safety conditioning costs only inverse retained word density | PROVED | `docs/420-colored-corridor-word-kernels.md` |
| PP3bzb--PP3bzd | A finite shell-state graph admits a multiplicative potential exactly when all directed cycle products obey the proposed geometric rate; rational cycles and potentials are exact certificates | PROVED | `docs/421-cycle-product-criterion-for-shell-potentials.md` |
| PP3bze--PP3bzg | Contractive transient type blocks can be eliminated exactly by a nonnegative Schur complement; finite excursion truncation has an explicit geometric tail reserve | PROVED | `docs/422-schur-complement-elimination-for-type-loads.md` |

## Frontier update

### Boundary recleaning

Several small petal markers now amplify multiplicatively. If channel `i` gives
at least `q_i` choices and a marker value decodes to at most `h_i` sources, then
the tuple action graph has

```text
lambda_*<=min_i h_i / product_i q_i.
```

One intrinsic petal marker makes the numerator one. Two binary marker channels
then give exact load `1/4`, and three give `1/8`, provided all tuples survive.
The next geometric audit can search for short sequential words retaining two or
three marker coordinates rather than one large reservoir.

### Localized Hall transport

The backward endpoint distribution now feeds a capacity-weighted target law
with exact expectation

```text
E[n_U(Y)]=sum_x mu(x)r_0(x).
```

Endpoint mass `p` above raw threshold `theta` puts target mass at least

```text
p(theta-phi)/(M-phi)
```

on multiplicity above `phi`. Collision energy or maximum target atom then
controls how many distinct target hubs occur. A persistent obstruction is now
localized on both sides of the incidence graph.

### Fractional direct-clean layers

After extracting a common target core `C`, delete it and audit only residual
actions. If every source retains at least `d_R` actions and every residual
target is reused by at most `h_R` sources, then

```text
lambda_*<=h_R/d_R.
```

Failure returns a low-residual-degree source or a second target hub outside
`C`. This creates an iterative core-extraction route rather than stopping at
one rooted biclique.

### Support-chord repair words

For every vertex-disjoint corridor bank, `q` valid local words and within-bank
predecessor multiplicity `h` give load `h/q`. If a final target lies in at most
`g` bank supports, the complete colored family has load

```text
gh/q.
```

An intrinsic bank marker makes `g=1`, so neither the number of corridor colors
nor the number of dyadic types appears in the contraction constant.

### Clean-macro shells

A finite shell-state quotient has an exact obstruction criterion. A positive
`q`-potential exists exactly when every directed cycle `C` satisfies

```text
product_(e in C) p_e<=q^|C|.
```

Thus the optimal finite-state rate is the maximum cycle geometric mean. Failure
returns an explicit noncontracting cycle; success may be recorded by exact
rational cycle products or one rational strict potential.

### Integration

A type matrix with transient/core block form

```text
M=[A B; C D]
```

and `rho(A)<1` contracts exactly when the effective core matrix

```text
S=D+C(I-A)^(-1)B
```

contracts. The correction sums every transient excursion. Enumerating only
excursions of length below `T` is rigorous when the geometric tail fits inside
the remaining core-potential margin.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_417_422.py
```

or individually with

```bash
python scripts/check_tensorized_petal_marker_reservoirs.py
python scripts/check_hall_endpoint_target_transfer.py
python scripts/check_residual_biclique_expansion.py
python scripts/check_colored_corridor_word_kernels.py
python scripts/check_shell_cycle_product_potential.py
python scripts/check_type_schur_elimination.py
```

The local audits verify exact expansion of full and conditioned three-marker
products, exact endpoint-target transfer, every residual source subset of a
stored biclique graph, sharp bank-support overlap, all simple cycles of a
rational shell graph, and exact rational Schur elimination with a depth-four
tail reserve.

The next available theorem identifier is `PP3bzh`.
