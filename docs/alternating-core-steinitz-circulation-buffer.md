# Steinitz-buffer realization of primitive resource circulations

**Branch:** `research/alternating-core-chain`

AC3uc--AC3ug show that every finite coupled additive macro dictionary has either one positive common
resource rank or a bounded primitive nondecreasing circulation count vector. The remaining gap is
chronological: an algebraic multiset of root-return macros need not be executable in an arbitrary
order.

This note gives a sufficient physical ordering theorem. After centring the primitive circulation,
Steinitz ordering keeps every resource prefix within a universal coordinate deficit. A finite
internal-prefix buffer for the macro dictionary then makes the ordered circulation genuinely legal.

## Buffered root-macro model

Fix one root-boundary epoch and one primitive circulation address `x` from AC3ue. Expand it as a
multiset of `n=|x|_1` root-return macros with net resource increments

`v_1,...,v_n in Z^q`.

Write

`s=sum_j v_j>=0`

coordinatewise and assume

`||v_j||_infty<=B`

for every occurrence. The circulation-address theorem gives

`n<=(q+1)D_q`.

For each macro word and every internal prefix, record its resource displacement. Let

`b_int=max_(macro,prefix,i) (-prefix_displacement_i)_+`.

Assume the **resource-complete root-macro contract**:

1. all macros begin and end at the same finite auxiliary boundary state and primitive lift;
2. the displayed resource vector is the only unbounded ordering-sensitive field;
3. a macro is legal whenever its starting resource vector is coordinatewise at least `b_int`;
4. its exact internal prefix displacements and net increment are those in the fixed dictionary;
5. all other guards, ownership fields, payment fields and context fields are present in the finite
   boundary state;
6. a changed word, increment, internal prefix, guard or interpretation is an outer reset.

Put

`beta=2qB+b_int`.

## AC3uh -- centred Steinitz ordering -- PROVED

There is an ordering `pi` of the `n` macro occurrences such that every net-resource prefix

`p_t=sum_(j=1)^t v_(pi(j))`

satisfies

`p_(t,i)>=-2qB`

for every coordinate `i` and every `0<=t<=n`.

### Proof

Put

`u_j=v_j-s/n`.

Then `sum_j u_j=0`. Since `0<=s_i/n<=B`, every centred vector satisfies

`||u_j||_infty<=2B`.

The Steinitz lemma in dimension `q`, applied in the infinity norm, gives an ordering with

`||sum_(j=1)^t u_(pi(j))||_infty<=2qB`

for every prefix. But

`p_t=sum_(j=1)^t u_(pi(j))+(t/n)s`.

The second term is coordinatewise nonnegative, so every coordinate of `p_t` is at least `-2qB`.
QED.

Fix the existing total order on exact macro occurrences and choose the lexicographically least ordering
with the displayed prefix bound. This makes the Steinitz ordering canonical. Repeated macro addresses
are treated as distinct occurrences while ordering and are merged again after the chronological word is
fixed.

## AC3ui -- buffered chronological realization -- PROVED UNDER THE ROOT-MACRO CONTRACT

If the starting resource vector satisfies

`m_i>=beta`

for every coordinate, the AC3uh ordering is a legal chronological execution of the complete primitive
circulation. Throughout the execution every macro starts with at least `b_int` units of every
resource, every internal prefix remains nonnegative, and the final resource vector is

`m'=m+s>=m`.

The chronological word contains at most

`(q+1)D_q`

root-return macros, at most

`(q+1)D_q L_macro`

completed gates and at most

`(q+1)D_q L_macro L_gate`

underlying control edges.

### Proof

Before the `(t+1)`st macro, AC3uh gives boundary resources at least

`m_i-2qB>=b_int`.

The internal-prefix definition of `b_int` makes that macro resource-legal. The other legality fields
are fixed by the contract. Induct through the ordered occurrences. The final increment is `s>=0`.
The length bounds use AC3ue and the fixed macro/gate word bounds. QED.

## AC3uj -- exact zero-output return or positive resource output -- PROVED

For a buffered realized primitive circulation exactly one of the following holds:

1. `s=0`, and the chronological word returns to the exact root boundary state, primitive lift and
   resource vector;
2. `s!=0`, and total physical resource stock increases by at least one.

In the first branch the word is an exact chronological return and may be erased, descended, ticketed
or reset by the existing auxiliary-cycle contract. In the second branch every occurrence receives
its exact circulation, macro and resource-coordinate output address.

### Proof

The root, finite boundary state and primitive lift return by the macro contract. The resource vector
changes by `s`. If `s=0`, the complete boundary state returns exactly. Otherwise `s` is a nonzero
nonnegative integer vector, so `sum_i s_i>=1`. QED.

## AC3uk -- bounded or source-paid positive-output closure -- PROVED

Suppose every positive-output circulation is either:

- physically confined by coordinate ceilings `m_i<=C_i`; or
- occurrence-faithfully charged to a finite nonreplenishing source ledger under AC3tx--AC3ub.

In the bounded case, the number of positive-output circulation executions is at most

`sum_i (C_i-m_i^(0))`.

In the source-paid case their gross created units and execution count obey the AC3ty--AC3tz source
budgets. Zero-output returns use their existing finite cycle route.

### Proof

Every positive-output execution raises total resource stock by at least one and never decreases any
coordinate at its boundary. Under coordinate ceilings, total available headroom bounds the count.
Under source payment, apply the gross occurrence accounting and telescoping source bounds from
AC3tx--AC3tz. QED.

## AC3ul -- buffered circulation router -- PROVED UNDER THE DECLARED CONTRACTS

Every primitive nondecreasing circulation address from AC3ue has one continuation:

1. a starting buffer `m_i>=b_int+2qB` realizes a chronological word of at most `(q+1)D_q` macros;
2. a zero-output realized word is an exact root-boundary return;
3. a positive-output realized word spends finite cap headroom or an occurrence-faithful source debit;
4. some coordinate has `m_i<b_int+2qB`, giving an exact low-buffer coordinate/value witness;
5. or one internal-prefix, root-state, guard, address, resource, ownership, context or outer-reset field
   fails.

Thus chronological extraction is no longer an independent assumption for resource-complete root
macros above the explicit buffer. The residual is low-buffer behaviour and macro dictionaries whose
legality depends on unrecorded or nonresource ordering data.

## Corrected AC4 numerical frontier

Primitive nondecreasing resource circulations now admit a canonical bounded-deficit ordering. Above
the finite buffer `b_int+2qB`, they are actual chronological root words; zero-output words are exact
returns and positive-output words are bounded by cap headroom or the source-payment ledger.

The remaining numerical work is low-buffer circulation behaviour, free or cyclically replenished
positive outputs, nonlinear or nonadditive balances, macro legality depending on hidden ordering
state, unbounded zero-sum-free lift residuals, dynamic dictionaries and undeclared changes of law.

## Finite check

`scripts/verify_ac_steinitz_circulation_buffer.py` exhausts and samples small nonnegative-sum vector
multisets. It searches for a chronological ordering with the stated `2qB` coordinate deficit, checks
the internal buffer, exact zero/positive-output split and the bounded-headroom execution count.
