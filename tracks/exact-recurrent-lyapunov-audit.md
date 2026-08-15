# Exact recurrent Lyapunov audit

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Base:** `research/all-n-composite-modulus`

## Status

This branch does **not** prove the no-three-in-line conjecture. It begins a
proof-or-refutation programme focused on the common unresolved point of the
alternating-core, prime-patching and composite-modulus branches:

> construct the complete recurrent repair kernel with exact geometric
> coefficients and prove a strict Lyapunov inequality, or expose a recurrent
> obstruction showing that the present repair architecture cannot terminate.

The affirmative statement `D(n)=2n` is treated as a target, not an assumption.
A valid negative result for a proposed repair system, or a genuine counterexample
to the conjecture, is an acceptable research outcome and must not be hidden by a
coarser upper table or a larger conditional interface.

## Why this branch exists

The three most developed routes now share one structural bottleneck.

- Alternating core has finite routing, Hall, carry, petal and resampling
  interfaces but still needs payment or strict descent on recurrent concentrated
  cores.
- Prime patching has exact degree restoration and a conditional prime-gap
  transfer, but PP3 remains open at concentrated controller, star, petal, shadow,
  cycle and weighted-grid cores.
- Composite modulus has the deepest exact finite-state and assignment machinery,
  including an executable strict-row certificate format, but the actual recurrent
  state population, background profiles, provenance-complete coefficients and
  global strictness remain unfilled.

The missing theorem is therefore not another local routing dichotomy. It is an
**exact recurrent-kernel theorem**.

## Central theorem target

Let `I` be the complete set of recurrent labelled repair states after all proved
strict descendants, terminating states and exact structural products have been
contracted. For parent state `i` and child state `j`, let `A_ij` be the exact
expected number, or a proved provenance-complete upper number, of child copies
created by one legal response to `i`.

The target is a positive rational vector `x` and positive rational row slacks
`epsilon_i` such that

\[
\sum_{j\in I} A_{ij}x_j \le x_i-\epsilon_i
\qquad(i\in I).
\]

Equivalently,

\[
Ax<x.
\]

A finite exact certificate of this form proves that the declared recurrent
kernel is subcritical. It does **not** prove the conjecture unless the following
four obligations are also discharged:

1. **state completeness:** every legal recurrent configuration enters exactly one
   declared state or a proved strict descendant;
2. **coefficient correctness:** every return, selector, line, carry, collision,
   owner, interface, CRT and background contribution is represented exactly or
   by a proved componentwise upper coefficient;
3. **execution closure:** every legal repair step is covered, including
   intermediate-state legality and repeated-host effects;
4. **all-`n` transfer:** the terminated construction reaches prime fields,
   prime powers and arbitrary side lengths without assuming the desired result.

## Research posture

### Proof and falsification have equal priority

Every candidate state compiler must support both outputs:

- a complete strict recurrent block; or
- a minimal failed row, recurrent cycle, missing provenance class, or explicit
  finite geometric state that invalidates the proposed closure.

A failed LP is not automatically a mathematical obstruction, because a declared
upper table may be coarse. It becomes a useful obstruction only after the row is
reconstructed with exact coefficients or after a realizable lower witness is
attached.

### No silent affirmative assumptions

The branch must not assume:

- that `D(n)=2n` is true;
- that every saturated modular state has a terminating Euclidean repair path;
- that finite local success implies uniform all-`n` success;
- that a checker proves more than the manifest it receives;
- that a conditional theorem is an installed construction;
- that workflow configuration is successful execution.

## Work packages

### ERL0 — branch integrity and honesty gates

Maintain machine-readable flags for:

```text
exact_state_extractor_complete = 0
coefficient_provenance_complete = 0
all_recurrent_rows_populated = 0
strict_recurrent_lyapunov_certificate = 0
execution_closure_proved = 0
prime_field_transfer_complete = 0
prime_power_transfer_complete = 0
arbitrary_side_transfer_complete = 0
all_n_proved_by_checker = 0
```

No script may set `all_n_proved_by_checker` to one. A mathematical proof must be
reviewed independently of the arithmetic checker.

### ERL1 — canonical recurrent-state extractor

Build a deterministic extractor from a physical repair state to a canonical
label containing every field that can affect future offspring:

- side, modulus and prime-power depth;
- construction layer and current owner;
- exact active host and protected registry;
- line, carry, collision and local-interface profile;
- background line-height superlevels;
- return, selector and ancestry status;
- parent/child factor and CRT provenance;
- legal operation family and intermediate-state contract.

Two physical states may share a label only after proving that every legal response
has the same labelled offspring law or a common certified upper law.

### ERL2 — exact coefficient compiler

For each canonical parent state:

1. enumerate or symbolically classify every legal response;
2. reconstruct exact child labels after the response;
3. count rank-one, rank-two and rank-three geometric offspring without double
   counting;
4. include return, selector, restoration and protected-reserve costs;
5. preserve rational coefficients exactly;
6. publish the row plus a trace from every nonzero coefficient to its geometric
   source theorem or finite enumeration.

Moment, assignment and occupancy relaxations may be used only when their
background and provenance hypotheses are attached to the row.

### ERL3 — adversarial small-state census

Before scaling the programme, exhaust the smallest nontrivial hosts and search
for:

- exact recurrent cycles;
- rows with spectral radius at least one;
- owner-preserving diagonal blocks that cannot be made strict;
- omitted background-height classes;
- coefficient reductions that merge states with different offspring laws;
- apparent strict rows destroyed by intermediate-state illegality;
- saturated configurations with no move in the installed operation bank.

Every found obstruction receives a minimal JSON witness and a deterministic
checker. The aim is to falsify inadequate state alphabets early.

### ERL4 — strict rational Lyapunov search

After ERL1--ERL3 produce a closed block, solve the exact finite system

\[
Ax<x,
\]

using rational linear programming or denominator-cleared assignment duals.
Publish:

- one positive integer weight per state;
- every exact or upper offspring coefficient;
- all contracted inner and outer assignment duals when used;
- one positive integer slack per row;
- the condensation order for auxiliary blocks;
- the exact manifest digest.

The first success criterion is one **nontrivial complete recurrent block**, not a
toy example and not a block selected after discarding failed states.

### ERL5 — cross-branch transfer audit

Map each strict or failed recurrent class back to the three existing routes.

- **Alternating core:** identify the AC4 payment edge, AC5 event menu or AC6 pool
  state represented by the row.
- **Prime patching:** identify whether the row closes a controller/Ore core,
  source-star or petal bank, chromatic shadow, cycle/theta state, or weighted
  grid/Hall residual.
- **Composite modulus:** identify the exact prime-power owner, background,
  collision, line, interface and CRT labels and the installed operation kinds.

Imports are one-way only when all hypotheses are physically realized. Similar
names or abstract graph isomorphism are not sufficient.

### ERL6 — global closure or architecture refutation

Only after every recurrent block is strict may the branch attempt the global
termination theorem. The final proof must show:

1. every repair trajectory enters the certified finite quotient;
2. strict descendant measures are well founded;
3. recurrent mass decays under the certified Lyapunov function;
4. termination produces a saturated Euclidean no-three-in-line state;
5. the prime, prime-power and arbitrary-side transfers cover every `n`;
6. finite exceptions are supplied by independently checked certificates.

If a complete physical recurrent block has no positive strict supersolution, the
branch must publish that obstruction and reassess the repair architecture rather
than add an unproved escape operation.

## Initial deliverables

This branch begins with:

- `docs/exact-recurrent-state-schema.md`: manifest and proof-obligation schema;
- `scripts/check_exact_recurrent_manifest.py`: exact rational strict-row checker;
- `experiments/exact-recurrent-manifest-example.json`: deliberately incomplete
  toy certificate with honesty flags at zero;
- `.github/workflows/exact-recurrent-lyapunov-audit.yml`: syntax, toy-certificate
  and corruption-regression checks.

The checker verifies arithmetic only. It cannot certify state completeness,
geometric provenance, execution closure, or the all-`n` conjecture.

## First mathematical milestone

Construct the smallest physically realizable recurrent block containing at least
one genuinely concentrated state from the existing frontier—preferably a
same-owner diagonal, fixed-centre star/petal, or recurrent selector state—and do
one of the following:

1. publish a provenance-complete strict manifest for the entire block; or
2. publish an exact realizable failed row or recurrent cycle showing why the
   current operation bank is insufficient.

Until that milestone is met, adding further abstract routing layers is explicitly
out of scope.
