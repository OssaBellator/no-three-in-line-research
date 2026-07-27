# Bottom-permutation triple covers for low-multiplicity selectors

The current side-seven verifier enumerates clean top orders and then runs one
shared active-selector bottom CSP. For multiplicity two, the selector disjunction
can be separated exactly after the top order is fixed. This yields a compact
certificate target: cover all `5,040` bottom permutations for each selector by
explicit collinear edge triples.

## 1. Exact coverage formulation

Fix one top signature, one clean top assignment, and one radix orientation. For a
selector `F` and an abstract edge triple `T` contained in `F`, define

\[
C_F(T)\subseteq\operatorname{Sym}([7])
\]

to be the bottom permutations for which the three scalar points induced by `T`
are collinear.

### Theorem PX960 -- PROVED REDUCTION

The fixed selector `F` has no clean bottom completion if and only if

\[
\boxed{
\bigcup_{T\in\binom{E(F)}3}C_F(T)
=
\operatorname{Sym}([7]).
}
\]

Any subfamily of triples whose coverage sets already have full union is an
independently recheckable infeasibility certificate for `F` under the fixed top
assignment and orientation.

### Proof

A bottom permutation is rejected exactly when the scalar configuration of `F`
contains at least one collinear triple. Such a triple is one of the abstract
three-edge subsets of `F`, and the bottom permutation lies in its coverage set.
Thus every bottom permutation is rejected exactly when the displayed union is
all of `Sym([7])`. A stated subcover is checked by recomputing the integer
determinant for every covered permutation. \(\square\)

## 2. Selector separation

Let `Q` be the selector family sharing the fixed top signature.

### Corollary PX961 -- PROVED REDUCTION

The shared bottom/selector subproblem is infeasible if and only if every
selector `F in Q` has a full bottom-permutation triple cover.

In particular, for multiplicity two, one may replace one two-bit active-mask
search by two explicit coverage certificates. The active-mask solver may still
be faster operationally, but the coverage form is a smaller and more transparent
proof target.

### Proof

The subproblem is satisfiable exactly when there exists a pair `(F,R)` with
`F in Q` and bottom permutation `R` producing no collinear triple. Negating this
existential statement gives: for every `F`, every `R` is rejected by some triple
of `F`. Apply PX960 selector by selector. \(\square\)

## 3. Deterministic greedy measurement

The executable

`scripts/measure_product_side_seven_bottom_triple_cover.cpp`

performs the following exact experiment for any multiplicity, case, orientation,
and clean-top prefix:

1. regenerate the exact support-twenty selector layer;
2. enumerate all `5,040` bottom permutations;
3. compute the exact coverage bitset of every abstract triple;
4. greedily choose the triple with maximum uncovered gain, using lexical
   generation order to break ties;
5. abort if any selector has an uncovered bottom permutation;
6. emit the selected cover sizes, shared triple dictionary size, repeated-cover
   dictionary size, and deterministic digest.

The greedy cover is not claimed minimum. Its role is to measure whether explicit
subcovers are substantially smaller than one rejection witness per
selector-permutation obligation. Every chosen cover can be replayed without
trusting the greedy search.

A second executable,

`scripts/measure_product_side_seven_bottom_certificate_dictionary.cpp`,

retains the older first-bad-triple dictionary format and now supports arbitrary
multiplicity, case, orientation, and top-order prefix. Comparing the two formats
separates dictionary reuse from genuine set-cover compression.

## 4. Immediate certificate frontier

1. run both generators on multiplicity-two case zero in all four orientations;
2. measure cover-size and dictionary saturation over increasing top-order
   prefixes;
3. deletion-minimize or exactly optimize the greedy covers when their size is
   small;
4. deduplicate repeated cover patterns across top orders and selector pairs;
5. combine bottom covers with assumption-minimized top nogoods;
6. promote only certificates whose stored triples are independently replayed.

This route changes the proof object, not the mathematical search space. It does
not imply that the remaining multiplicity-two or multiplicity-one selectors are
infeasible.

## 5. Verification commands

```bash
g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_bottom_certificate_dictionary.cpp \
  -o /tmp/m2-dictionary

/tmp/m2-dictionary 2 0 0 8

g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_bottom_triple_cover.cpp \
  -o /tmp/m2-cover

/tmp/m2-cover 2 0 0 1
```
