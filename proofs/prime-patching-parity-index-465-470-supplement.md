# Prime-patching parity index supplement: `docs/465--470`

This supplement continues the cumulative parity index after `docs/464`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ced--PP3cef | Marker-controller synthesis remains a finite rational LP under finitely many adversarial transition scenarios; sparse robust policies and localized separating witnesses are exact | PROVED | `docs/465-robust-marker-controllers-under-polyhedral-uncertainty.md` |
| PP3ceg--PP3cei | Proper Hall colors retain list-controlled reverse load under symbol errors and erasures; Reed--Solomon tags attain the exact Singleton length | PROVED | `docs/466-error-and-erasure-resilient-hall-color-tags.md` |
| PP3cej--PP3cel | Degenerate threshold walls form finite connected basis fans; exact tangent tests and lexicographic zero-length pivots give canonical continuations | PROVED | `docs/467-degenerate-basis-fans-for-threshold-kernels.md` |
| PP3cem--PP3ceo | Equal-risk banks quotient the unequal-symbol code recurrence to multiplicity vectors, reducing the exact state space and pruning whole labeled split orbits | PROVED | `docs/468-symmetry-quotients-for-unequal-symbol-code-search.md` |
| PP3cep--PP3cer | Monomial shell perturbations admit exact face-preserving slopes, radical-free competitor breakpoints, and a finite critical-face walk | PROVED | `docs/469-exact-line-searches-between-shell-critical-faces.md` |
| PP3ces--PP3ceu | Interaction-prefix expansions have an exact finite budget dynamic program, minimum-work error certificates, and multiroot scalarized allocation | PROVED | `docs/470-minimum-work-dynamic-programming-for-interaction-expansions.md` |

## Frontier update

### Boundary recleaning

Marker-controller synthesis is now robust against finitely many adversarial
transition rows.  Every state solves one rational LP over action probabilities.
A basic robust policy is sparse, and failure returns a nonnegative scenario--
potential price vector defeating every candidate action.  The stored fixture has
the unique robust mix `(1/2,1/2)` and separator margin `1/10` at the impossible
rate `2/5`.

### Localized Hall transport

Hall color tags now tolerate both altered and erased marker symbols.  List
ambiguity `L_(t,e)` gives load `L_(t,e)/d`, while distance
`delta>2t+e` preserves private load `1/d`.  For `p^k` colors the optimal tag
length is `k+2t+e`, attained by Reed--Solomon evaluation when that length is at
most `p`.

### Fractional direct-clean layers

Degenerate threshold walls are handled by the complete finite fan of primal--
dual feasible bases.  At the wall, a basis continues forward exactly when every
zero basic coordinate has nonnegative directional derivative.  Zero-length
pivots connect the wall fan, and a lexicographic search gives a canonical next
basis.  The stored wall at `t=1/2` has three bases and two forward continuations.

### Support-chord repair words

Equal bank risks are now quotiented before unequal-symbol code search.  With
multiplicities `m_i`, the exact subset recurrence needs only

```text
product_i(m_i+1)-1
```

orbit states.  The stored eight-bank instance shrinks from `255` labeled states
to `47` count states while preserving exact optimum `1/2`.

### Clean-macro shells

A descent direction on a critical face now has an exact algebraic line search.
Integer edge exponents make every competitor equality a rational binomial, and
cross powers determine the winning side without radicals.  The stored two-cycle
face reaches a stationary self-loop at the exact breakpoint `x=5/4`, the positive
root of `16x^2-25`.

### Integration

Adaptive interaction expansion now has a minimum-work counterpart.  A finite
dynamic program computes the least omitted output after every expansion budget.
The first budget meeting the tolerance is therefore optimal, with the preceding
budget value providing a matching impossibility certificate.  The stored
three-state automaton needs exactly five expansions to reach error `1/100`.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_465_470.py
```

or individually with

```bash
python scripts/check_robust_marker_controller_synthesis.py
python scripts/check_error_erasure_hall_tags.py
python scripts/check_degenerate_threshold_basis_fan.py
python scripts/check_symmetry_reduced_unequal_code_dp.py
python scripts/check_shell_face_line_search.py
python scripts/check_minimum_work_interaction_dp.py
```

The local audits verify the unique robust controller and rational separator,
`5,880` corrected Hall-tag observations, `101` degenerate basis-path points, the
`47`-state symmetry quotient, `101` exact shell line-search points, and the exact
minimum five-expansion interaction certificate.

The next available theorem identifier is `PP3cev`.
