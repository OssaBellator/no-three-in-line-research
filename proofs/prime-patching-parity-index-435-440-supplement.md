# Prime-patching parity index supplement: `docs/435--440`

This supplement continues the cumulative parity index after `docs/434`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3car--PP3cat | Nonintrinsic stopping levels can be made recoverable by prefix-free schedule codes; the optimal conditioned load is decided by an exact finite Kraft search | PROVED | `docs/435-prefix-coded-stopping-levels.md` |
| PP3cau--PP3caw | A common Hall target core leaves enough residual edges to extract a matching of private marker targets, producing a core-plus-petals repair bank | PROVED | `docs/436-core-plus-private-marker-packings-in-hall-rectangles.md` |
| PP3cax--PP3caz | Sources may randomize among multiplicity thresholds; the optimal load has an exact target-price LP dual and a sparse optimal support | PROVED | `docs/437-randomized-source-threshold-kernels.md` |
| PP3cba--PP3cbc | Optimal corridor codes assign shorter words to heavier banks; the minimax risk lies in a finite candidate set and has a sorted-length certificate | PROVED | `docs/438-canonical-minimax-corridor-codes.md` |
| PP3cbd--PP3cbf | Multiplicative Bellman--Ford is an exact rational shell-rate oracle; rational brackets and multiplicative perturbation reserves follow directly | PROVED | `docs/439-rational-rate-oracles-for-shell-graphs.md` |
| PP3cbg--PP3cbi | Condensation-path resolvent sums admit topological dynamic programs, monotone interval propagation, and linear-time effective-core correction | PROVED | `docs/440-dynamic-programming-on-condensation-resolvents.md` |

## Frontier update

### Boundary recleaning

Stopping levels need not be intrinsically visible in the geometric target.  A
binary prefix code of length `ell_i` for stopping class `i` gives combined load

```text
max_i lambda_i p^(-ell_i).
```

The exact minimax risk is the smallest finite candidate passing Kraft's
inequality.  In the stored four-level audit, lengths `(3,3,2,1)` give the exact
optimum `2/3`.  The remaining geometric task is to realize the schedule symbols
by short clean marker moves.

### Localized Hall transport

A common `q`-target core shared by `F` sources leaves at least

```text
|F|(d-q)
```

residual edges.  Under endpoint degree caps this yields a residual matching of
size at least

```text
ceil(|F|(d-q)/(D+Delta-1)).
```

The selected sources therefore share one conditioned core and each retain a
private target marker outside it.

### Fractional direct-clean layers

The source-adaptive threshold frontier is now an exact linear program.  Its dual
chooses a target-price distribution `z` and charges each source its cheapest
average retained price:

```text
min_alpha lambda(alpha)
 =max_z sum_x min_h z(N_h(x))/d_h(x).
```

The stored nested-threshold graph improves from deterministic optimum `5/6` to
mixed optimum `3/5`; uniform target prices certify optimality.  An optimum needs
at most `|X|+|Y|-1` positive threshold probabilities.

### Support-chord repair words

For unequal bank risks `rho_i`, an optimal prefix code may be chosen with shorter
words on heavier banks.  With `K` banks, all optimal lengths are at most `K-1`,
so the exact risk lies in

```text
{rho_i p^(-ell):1<=i<=K, 1<=ell<=K-1}.
```

The seven-bank audit finds exact optimum `2048/3645` with lengths
`(6,6,5,4,3,2,1)` after sorting bank loads increasingly.

### Clean-macro shells

The Bellman--Ford shell test is now an exact rational rate oracle.  Failure at
`q_-` returns a cycle with product greater than `q_-` to its length; success at
`q_+` returns a rational potential, proving

```text
q_-<mu<=q_+.
```

The stored graph has the certified bracket `(763/1000,191/250]`.  Any edgewise
multiplicative error factor `gamma` merely changes the certified rate from `q`
to `gamma q`.

### Integration

The finite condensation-path sum no longer needs explicit path enumeration.
For a fixed start component,

```text
T_s=R_s,
T_j=[sum_(i<j) T_i A_ij]R_j
```

computes every exact transfer block.  The same recurrence propagates lower and
upper local SCC bounds.  Adding core injection and return blocks gives the full
Schur correction with one pass over the condensation DAG.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_435_440.py
```

or individually with

```bash
python scripts/check_prefix_coded_stopping_levels.py
python scripts/check_hall_core_private_markers.py
python scripts/check_randomized_source_thresholds.py
python scripts/check_canonical_corridor_codes.py
python scripts/check_rational_shell_rate_oracle.py
python scripts/check_condensation_resolvent_dp.py
```

The local audits verify 32 feasible four-level stopping codes, 10,000 Hall
rectangles and 20,993 core orders, an exact mixed-threshold primal--dual pair,
374 monotone seven-bank code vectors, both rational shell-oracle branches, and
an exact five-component condensation dynamic program with rigorous intervals.

The next available theorem identifier is `PP3cbj`.
