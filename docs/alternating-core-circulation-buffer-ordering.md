# Buffered chronological realization of primitive resource circulations

**Branch:** `research/alternating-core-chain`

AC3uc--AC3ug reduce every finite coupled additive macro dictionary to either one positive common
resource rank or one bounded primitive nondecreasing circulation count vector.  The remaining gap is
chronological: an algebraic multiset of macro addresses need not be executable from the current
resource stock.

This note closes that gap under a resource-monotone legality contract.  A canonical ordering of the
primitive multiset is legal whenever each resource coordinate contains an explicit finite buffer.  If
that buffer is absent, one exact scarce resource coordinate is returned.

## Buffered macro model

Fix one root-boundary state and a finite macro dictionary `Lambda`.  Every macro address `lambda`:

- returns to the same finite root-boundary state;
- has net resource increment `v_lambda in Z^q` with `|v_(lambda,i)|<=B`;
- contains at most `L_macro` completed root-return gates;
- each gate contains at most `L_gate` underlying control edges;
- has an exact internal resource-prefix path `p_(lambda,t) in Z^q`, measured from the resource state at
  the beginning of the macro.

Put

`P=max_(lambda,t,i) (-p_(lambda,t,i))_+`.

Thus a macro beginning with at least `P` units in every coordinate never crosses below zero during its
internal word.

Assume the **resource-monotone macro-legality contract**:

1. the finite boundary state is identical before every macro in the circulation;
2. a macro is legal whenever every resource coordinate remains nonnegative at every internal prefix;
3. no upper resource guard, zero test beyond nonnegativity, hidden ownership field or omitted balance
   changes legality;
4. the dictionary, prefix paths and resource interpretation are fixed in the epoch;
5. failure of these conditions or a change of law is an outer reset or named contract failure.

Let `x in Z_(>=0)^k` be one primitive circulation address from AC3ue, so

`Vx>=0`.

Write

`n=|x|_1`.

The AC3ue bound gives

`n<=(q+1)D_q`.

Fix one total order on `Lambda` and form the **canonical circulation word** by listing each address
`lambda` exactly `x_lambda` times in that order.

## AC3uh -- canonical net-prefix deficit bound -- PROVED

Every prefix of the canonical circulation word has resource displacement at least

`-(n-1)B`

in every coordinate.  The complete word has nonnegative net displacement `Vx`.

### Proof

Before the final macro, a prefix contains at most `n-1` macro occurrences.  Each occurrence decreases
one fixed coordinate by at most `B`, so the prefix displacement in that coordinate is at least
`-(n-1)B`.  The final displacement is `Vx>=0`. QED.

The argument does not require a favourable ordering; the fixed canonical order is enough because the
primitive occurrence stock is already bounded.

## AC3ui -- explicit chronological resource buffer -- PROVED UNDER THE LEGALITY CONTRACT

If the initial resource vector satisfies

`m_i>=(n-1)B+P`

for every coordinate `i`, then the complete canonical circulation word is legal.  During the word no
resource coordinate becomes negative, and after the word

`m'=m+Vx>=m`

coordinatewise.

The chronological realization uses at most

`n*L_macro`

completed root-return gates and at most

`n*L_macro*L_gate`

underlying control edges.

### Proof

Immediately before any macro, AC3uh gives resource stock at least `m_i-(n-1)B>=P`.  The definition of
`P` therefore keeps every internal prefix nonnegative.  The resource-monotone legality contract makes
each macro legal in sequence.  The final inequality is `Vx>=0`; the length bounds follow by expanding
the `n` macro occurrences. QED.

## AC3uj -- uniform primitive-circulation buffer -- PROVED

Put

`H_circ=((q+1)D_q-1)B+P`.

Every primitive circulation address from AC3ue is chronologically executable whenever

`m_i>=H_circ`

for every resource coordinate.  Otherwise one exact coordinate satisfies

`m_i<H_circ`.

Thus failure of the uniform buffer is a finite scarce-coordinate witness, not an unstructured ordering
obstruction.

### Proof

Use `n<=(q+1)D_q` in AC3ui.  If the coordinatewise hypothesis fails, choose the least deficient
coordinate. QED.

## AC3uk -- nondecreasing circulation gate -- PROVED

Under the uniform buffer, executing one primitive circulation returns to the same finite boundary state
and does not decrease any physical resource coordinate.  Consequently it is one exact chronological
nondecreasing return gate with:

- one of at most `K_circ` primitive count-vector addresses;
- canonical word length at most `(q+1)D_q` macros;
- completed-gate length at most `(q+1)D_q L_macro`;
- control-edge length at most `(q+1)D_q L_macro L_gate`.

A free executable circulation may repeat forever.  Termination therefore still requires one of:

1. quotient-stuttering of the complete physical effect;
2. an independent well-founded descent;
3. occurrence-faithful payment from a finite source ledger;
4. a finite exact ticket;
5. impossibility after one use;
6. or an outer reset.

### Proof

AC3ui gives legal execution and coordinatewise nondecrease.  AC3ue supplies the address and occurrence
bounds.  The final list is exactly the remaining closure contract for a recurrent nondecreasing gate.
QED.

## AC3ul -- buffered coupled-resource router -- PROVED UNDER THE DECLARED CONTRACTS

Every primitive nondecreasing circulation returned by AC3ug has one continuation:

1. the current resources dominate `H_circ`, so its canonical chronological word executes with the
   explicit macro/gate/edge bounds of AC3uk;
2. one exact resource coordinate is below `H_circ`;
3. one internal-prefix, resource-monotonicity, finite-boundary, address or additivity field fails;
4. or a declared reset occurs.

In alternative 1, the circulation is no longer merely algebraic.  It is a physical chronological return
which must be erased, paid, descended, ticketed, made impossible or reset by the existing cycle
machinery.

### Proof

Apply AC3uj.  In the full-buffer branch use AC3ui--AC3uk.  Every excluded hypothesis is retained as the
named failure or reset branch. QED.

## Corrected AC4 numerical frontier

Primitive nondecreasing resource circulations no longer have a generic chronological-ordering gap under
resource-monotone legality.  A buffer of `((q+1)D_q-1)B+P` in every coordinate realizes one canonical
word, while insufficient stock localizes to one scarce coordinate.

The remaining numerical work is payment or exclusion of executable nondecreasing circulation gates,
cyclically replenished resources, legality depending on upper guards or hidden balances, genuinely
nonlinear/nonadditive updates, unbounded zero-sum-free lift residuals and dynamic macro dictionaries.

## Finite check

`scripts/verify_ac_circulation_buffer_ordering.py` exhausts small circulation multisets and samples
higher-dimensional macro systems with internal prefix paths.  It checks the canonical net-prefix bound,
the full-buffer legality inequality, coordinatewise nondecreasing return and all expanded word-length
bounds.
