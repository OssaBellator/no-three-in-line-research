# A deletion-minimal line core for the canonical `2 x 5` obstruction

PX23 gives the exact positive defect gap in every unmodified global `2 x 5`
product host. This note extracts a compact SAT certificate from one canonical
crossed host. It is not yet a common symbolic obstruction for all side-five
factors, but it reduces one infeasibility proof from all host lines to thirty-five
explicit line clauses.

Use

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0),
\]

\[
\tau_0=(0,1,3,4,2),
\qquad
\tau_1=(2,0,4,1,3),
\]

and the unmodified `cf` orientation. The host has 40 cells and side ten.
Introduce one Boolean variable per host cell. Keep all 160 width-three clauses
that enforce degree exactly two at every scalar row and column, as in PX10.

## Theorem PX27 — PROVED FINITE

There is a set of 35 real-collinear host triples such that adding only their
line-forbidding clauses to the exact degree-two clauses makes the formula
unsatisfiable. Moreover, the core is deletion-minimal with respect to its line
clauses: deleting any one of the 35 line clauses makes the remaining formula
satisfiable.

The triples are:

```text
((0,0),(1,3),(2,6))   ((0,0),(2,6),(3,9))
((0,0),(3,3),(4,4))   ((0,0),(3,3),(5,5))
((0,0),(4,4),(7,7))   ((0,1),(1,2),(8,9))
((0,4),(3,2),(6,0))   ((0,4),(3,3),(6,2))
((0,5),(2,7),(3,8))   ((0,5),(3,2),(5,0))
((1,1),(3,3),(5,5))   ((1,2),(3,3),(5,4))
((1,3),(2,6),(3,9))   ((1,3),(7,6),(9,7))
((2,6),(4,4),(6,2))   ((2,6),(4,5),(8,3))
((2,6),(5,4),(8,2))   ((2,7),(4,5),(5,4))
((2,7),(5,4),(6,3))   ((2,7),(5,5),(8,3))
((2,8),(4,5),(6,2))   ((2,8),(4,6),(8,2))
((2,9),(4,7),(8,3))   ((3,2),(5,4),(7,6))
((3,2),(6,3),(9,4))   ((3,3),(4,4),(8,8))
((3,3),(5,1),(6,0))   ((3,3),(5,5),(8,8))
((3,8),(7,6),(9,5))   ((4,4),(6,3),(8,2))
((4,4),(7,7),(8,8))   ((4,6),(5,4),(6,2))
((5,0),(6,1),(9,4))   ((5,0),(7,6),(8,9))
((7,9),(8,8),(9,7))
```

### Proof

Construct the exact 160 degree clauses and the 35 negative line clauses. A
standard-library DPLL solver with unit propagation returns unsatisfiable.
Repeat 35 times, each time omitting a different line clause; every reduced
formula is satisfiable. All listed triples are checked to lie in the host and
to have zero integer determinant. \(\square\)

## Interpretation

The core is small compared with the 216 collinear triples in the complete host
formula, and every retained line is necessary relative to this core. It gives a
concrete target for enlarged-host design: the blockwise reversal in PX25 changes
the real placement of the factor cells enough to evade this coupled family of
line constraints.

The next structural goal is to compress the 35-line certificate further into a
coordinate-pattern or projection-signature argument that applies uniformly to
all unmodified `2 x 5` hosts.

## Verification

Run

```bash
python scripts/verify_product_2x5_unsat_core.py
```
