# Exact 2-SAT selection for cycle reservoirs

The matching-reservoir graph from PP3aj is a disjoint union of paths and even
cycles.  When the inserted patch is fixed, all remaining choice lies in the two
alternating matchings of each cycle.  External triple avoidance is therefore an
exact Boolean constraint problem of width at most two.

## 1. Fixed patch and alternating variables

Let `S subseteq [m]^2` be saturated and no-three-in-line.  Choose equal old
coordinate sets `C,Y` such that the induced graph `G_S(C,Y)` has a perfect
matching.  Fix an inserted set `Q` with the following properties.

1. For every perfect matching `D` of `G`, the set
   `(S setminus D) union Q` is saturated on `[m+t]^2`.
2. `Q` is internally no-three-in-line.
3. `Q` is disjoint from every retained point.

The first property is normally a degree statement: every perfect matching
deletes one point from each coordinate in `C` and `Y`, so one fixed patch fills
the same deficit vector for every matching choice.

Path components of `G` have unique perfect matchings.  For every cycle component
`i`, label its two alternating edge classes `0` and `1`, and introduce a Boolean
variable

\[
 \xi_i\in\{0,1\}
\]

meaning that class `xi_i` is deleted.

An old point represented by a cycle edge of class `epsilon` survives exactly
when

\[
 \xi_i=1-\varepsilon.
\]

A forced path-matching edge never survives; a path edge outside the unique
matching always survives; and every source point outside `G` always survives.

## 2. Clauses from external certificates

Consider a collinear triple containing two old source points `x,y` and one
inserted point `z in Q`.

- If one of `x,y` is forced deleted, the certificate is impossible.
- If both survive deterministically, the fixed patch is impossible.
- If survival requires one cycle assignment, avoiding the certificate gives one
  unary clause.
- If survival requires assignments on two distinct cycles, avoiding the
  certificate gives one binary clause.
- If both points lie on one cycle, their required assignments either disagree,
  making simultaneous survival impossible, or agree, giving one unary clause.

A triple with one old anchor and two inserted points is identical but involves
at most one cycle variable.

Thus every possible external triple contributes a clause of size at most two.

### Theorem PP3am -- PROVED

Construct the 2-CNF formula `Phi(S,C,Y,Q)` by adding the clause that negates the
survival conjunction of every external triple certificate.  If one certificate
survives independently of all cycle choices, declare the formula false.

Then the following are equivalent.

1. Some perfect matching reservoir `D` makes
   `(S setminus D) union Q` no-three-in-line.
2. The formula `Phi(S,C,Y,Q)` is satisfiable.

#### Proof

By PP3aj, every perfect matching is determined uniquely by one Boolean choice
on each cycle component together with the forced path matchings.

For one assignment, an external triple is present exactly when each of its old
points survives.  The construction adds the negation of precisely that
conjunction.  Therefore an assignment satisfies every clause if and only if no
external triple survives.

There are no triples wholly inside the retained set because it is a subset of
`S`, and no triples wholly inside `Q` by hypothesis.  Hence absence of all
encoded external certificates is equivalent to the final configuration being
no-three-in-line. ∎

This is a complete selection theorem, not merely a sufficient local-load bound.
The formula can be solved in linear time in its implication graph.

## 3. Immediate consequences

### Corollary PP3an -- PROVED

If every external certificate contains a forced-deleted old point, then every
cycle assignment gives a valid patch.

### Corollary PP3ao -- PROVED

If all surviving constraints are unary, a valid patch exists if and only if no
cycle variable is forced to both values.

### Corollary PP3ap -- PROVED

In general, a valid patch exists if and only if no variable and its negation lie
in the same strongly connected component of the implication graph of `Phi`.

These are the standard exact criteria for 2-SAT applied to PP3am.

## 4. Why geometry-aligned cycles remain promising

PP3al shows that arbitrary cycle entropy does not dilute fixed certificate
probabilities.  PP3am identifies the stronger mechanism that can work:
**logical anticorrelation**.

A cycle is useful when its two alternating classes clear different geometric
certificates in a mutually consistent way.  The target becomes an implication
graph problem rather than a probability problem:

- forced path edges should hit unavoidable blockers;
- cycle parities should make high-load old pairs mutually incompatible;
- the resulting implication graph should avoid contradictory directed cycles.

This permits dense certificate sets when their forbidden assignments have
coherent parity structure.  It is strictly more flexible than requiring every
joint event probability to be small.

## 5. Exact solver

The script

```bash
python scripts/solve_matching_reservoir_2sat.py \
  certificates/prime-patching-small.json \
  experiments/parabolic-variable-bank-n4.json \
  --n 4 --t 2 --columns 1,2,3,4 --rows 1,2,3,4
```

accepts one fixed inserted patch from the supplied JSON, constructs the induced
path/cycle decomposition, generates every external certificate clause, solves
the implication graph, and independently verifies any returned final
configuration with exact determinants.
