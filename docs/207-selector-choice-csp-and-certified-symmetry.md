# Selector-choice CSP, conflict learning, and certified symmetry

The side-seven cache verifiers currently split the coordinate search into a
clean-top enumeration followed by a shared active-selector bottom CSP.  That is
an effective exact method, but it still revisits many closely related top
orders.  This chapter records a stronger solver architecture and separates the
proved reduction from the unproved performance expectations.

## 1. One selector-choice coordinate CSP

Fix a finite family `Q` of abstract degree-two selectors in one relative-cycle
host.  Introduce:

- one selector variable `S in Q`;
- two column permutations `A_0,A_1 in Sym([7])`;
- one bottom-row permutation `R in Sym([7])`.

The scalar embedding is the coordinate map of PX504.

### Theorem PX641 -- PROVED REDUCTION

Existence of an embeddable selector in `Q` is equivalent to satisfiability of a
finite CSP with one selector variable, twenty-one permutation-value variables,
three all-different constraints, and forbidden tuples obtained from exact
integer determinants.

### Proof

Given a satisfying assignment, choose the indicated selector and apply
`A_0,A_1,R`; every forbidden determinant tuple is absent, so the resulting
`[14]^2` configuration is no-three.  Conversely, every no-three scalar
embedding chooses one selector and three coordinate permutations and therefore
satisfies every forbidden-tuple constraint. \(\square\)

This formulation searches the selector and its coordinate embedding together.
The current active-selector bit mask is a specialized propagation engine for
the same disjunction.

## 2. SAT encoding

Use one-hot variables

\[
p^g_{u,v},\qquad g\in\{0,1,R\},\quad u,v\in[7],
\]

for the three permutations and one-hot variables `y_F` for `F in Q`.
Permutation rows and values receive exactly-one constraints.  For every
selector `F`, abstract triple `T`, and partial coordinate assignment `alpha`
that makes `T` collinear, add

\[
\neg y_F\ \vee\ \bigvee_{(g,u,v)\in\alpha}\neg p^g_{u,v}.
\]

### Corollary PX642 -- PROVED REDUCTION

The resulting CNF is satisfiable exactly when some selector in `Q` has a
no-three coordinate embedding.  An UNSAT proof from a proof-logging SAT solver
would therefore be an independently checkable obstruction certificate for the
entire shard.

The clause family is finite and can be generated using only integer
determinants.  It is not necessary to enumerate complete triples of
permutations before generating a clause: a clause is emitted as soon as the
variables required by one abstract triple are fixed.

## 3. Logic-based Benders search

A practical hybrid keeps the existing split:

1. the master CSP generates a clean top order;
2. the bottom/selector subproblem decides whether any `R` and selector survive;
3. an infeasible subproblem returns a partial top-assignment conflict;
4. the master records that conflict and skips every top order extending it.

This is a logic-based Benders or conflict-directed decomposition.  The current
verifier returns only a yes/no result for one complete top order.  The missing
implementation step is to minimize an infeasible top assignment by deletion or
assumption-based solving and store the resulting nogood.

**Status: PROPOSED.**  Correctness is immediate if every learned nogood is
rechecked by the exact bottom CSP under the corresponding partial assignment.
No quantitative reduction in the side-seven tree is claimed yet.

## 4. Symmetry quotient

The CSP contains structured permutation symmetry: row interchangeability
inside each one-hot permutation, possible host automorphisms of the relative
cycle graph, and scalar reflections.  The safe workflow is:

1. compute candidate automorphisms of the abstract selector family;
2. verify mechanically that each automorphism preserves host incidence and all
   determinant constraints;
3. impose a lexicographic representative constraint;
4. log or independently verify the dominance argument.

This follows the structure-based symmetry philosophy used by Satsuma for
row-interchangeability, row-column, and Johnson symmetries.  For a publishable
finite obstruction, symmetry constraints should be accompanied by a
machine-checkable dominance or proof log rather than trusted as an unchecked
search shortcut.

**Status: PROPOSED / CERTIFIABLE.**  No unverified symmetry constraint is used
in PX637--PX640.

## 5. External methodological references

- Thomas Prellberg, *Constraint Satisfaction Programming for the
  No-three-in-line Problem*, arXiv:2602.07751, 2026.
- Gaurav Rattan, Markus Anders, Sofia Brenner, *Satsuma: Structure-Based
  Symmetry Breaking in SAT*, SAT 2024.
- Bart Bogaerts, Stephan Gocht, Ciaran McCreesh, Jakob Nordstrom,
  *Certified Symmetry and Dominance Breaking for Combinatorial Optimisation*,
  arXiv:2203.12275.
- Kissat and DRAT-trim provide a standard SAT plus independently checked UNSAT
  proof route; VeriPB supports certified dominance and richer symmetry
  reasoning.

## 6. Immediate implementation order

1. finish multiplicity-19 with the hoisted-incidence verifier;
2. add assumption literals for top assignments;
3. extract and deletion-minimize bottom UNSAT cores;
4. emit the selector-choice CNF for one completed shard;
5. compare raw DFS nodes, learned-core coverage, and proof size;
6. only then add mechanically verified selector-family symmetries.

The purpose of the new route is not merely speed.  It should replace a large
collection of trusted exhaustive runs by compact, independently checkable
obstruction certificates.