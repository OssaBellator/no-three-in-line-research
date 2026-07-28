# Buffered chronological realization of primitive resource circulations

**Branch:** `research/alternating-core-chain`

AC3uc--AC3ug show that a finite coupled additive macro dictionary either has one positive common
resource rank or contains a bounded primitive nondecreasing circulation count vector.  The remaining
gap is chronological: the circulation macros may consume resources at intermediate prefixes, and an
algebraic count vector does not itself order them.

This note supplies a uniform finite buffer.  A Steinitz ordering of the macro net-increment vectors
keeps every macro-boundary prefix above `-2qB`; one additional internal-drawdown allowance makes the
ordered word physically legal.  Thus every primitive circulation address has a canonical bounded
buffered chronological realization whenever macro legality is monotone in the resource coordinates.

## Buffered circulation model

Fix one root-boundary state and a primitive circulation address from AC3ue.  Let:

- `q>=1` be the number of nonnegative integer resource coordinates;
- the circulation contain `n>=1` macro occurrences, listed with repetition as vectors
  `v_1,...,v_n in Z^q`;
- every net increment satisfy `||v_j||_infty<=B`, with `B>=1`;
- the total circulation output be
  `s=sum_j v_j>=0` coordinatewise;
- every macro word contain at most `L_macro` completed root-return gates;
- every completed gate contain at most `L_gate` underlying control edges.

For one macro occurrence `j`, let `u_(j,t)` be the resource increment after the first `t` internal
control edges of that macro, measured from its macro boundary.  Define its coordinatewise internal
drawdown by

`d_(j,i)=max_t (-u_(j,t,i))_+`

and put

`D=max_(j,i)d_(j,i)`.

Assume the **buffered macro-legality contract**:

1. every macro begins and ends at the same finite root-boundary state;
2. all omitted payment, ownership, phase, capacity and legality fields are included in that state;
3. a macro is legal whenever all of its resource coordinates remain nonnegative during its internal
   word;
4. increasing the incoming resource vector cannot make an otherwise identical macro illegal;
5. the net vectors and internal words are fixed inside the epoch;
6. a changed word, changed interpretation, omitted field or nonmonotone resource guard is an outer
   reset or a named contract failure.

## AC3uh -- centred zero-sum reduction -- PROVED

Put

`bar_v=s/n`

and

`y_j=v_j-bar_v`.

Then

`sum_j y_j=0`

and

`||y_j||_infty<=2B`

for every `j`.

### Proof

The first identity is immediate.  Since each coordinate of every `v_j` lies in `[-B,B]`, the
coordinatewise average `bar_v` also lies in `[-B,B]`.  Thus
`|v_(j,i)-bar_v_i|<=2B`. QED.

## AC3ui -- Steinitz macro-boundary ordering -- PROVED USING THE STEINITZ LEMMA

There is a permutation `pi` of the `n` macro occurrences such that every boundary prefix satisfies

`sum_(r=1)^t v_(pi(r))>=-2qB*1`

coordinatewise for `0<=t<=n`.

The final prefix equals `s>=0`.

### Proof

Apply the dimension-`q` Steinitz lemma in the `l_infty` norm to the zero-sum vectors `y_j/(2B)`.
It gives an ordering with

`||sum_(r=1)^t y_(pi(r))||_infty<=q`.

Undo the scaling.  For each prefix,

`sum_(r=1)^t v_(pi(r))
 =sum_(r=1)^t y_(pi(r))+(t/n)s`.

The second term is coordinatewise nonnegative, while the first is coordinatewise at least `-2qB`.
The final sum is `s`. QED.

The theorem uses the standard finite-dimensional Steinitz ordering lemma only; no probabilistic
ordering or asymptotic discrepancy estimate is needed.

## AC3uj -- buffered chronological circulation word -- PROVED UNDER THE LEGALITY CONTRACT

If the incoming resource vector satisfies

`m^(0)>= (2qB+D)*1`

coordinatewise, the Steinitz ordering from AC3ui is a legal chronological macro word.  Every
intermediate resource coordinate remains nonnegative, and the final resource vector is

`m^(n)=m^(0)+s>=m^(0)`.

The word contains at most

`n*L_macro`

completed root-return gates and at most

`n*L_macro*L_gate`

underlying control edges.

### Proof

Before macro `pi(t)`, the accumulated net boundary increment is at least `-2qB` in every coordinate.
Hence its incoming resource vector is at least `D`.  By definition of `D`, every internal prefix of
that macro stays nonnegative.  The root-boundary and monotonicity clauses make the next macro legal
under the same argument.  Induct over the ordered word.  The final identity uses the total sum `s`.
The length bounds are immediate. QED.

## AC3uk -- primitive-address buffer and word bounds -- PROVED

Use the notation of AC3ue:

`D_q=ceil(q^(q/2)*B_0^q)`,  `B_0=max(B,1)`.

Every primitive circulation address has

`n<=N_circ=(q+1)D_q`.

Therefore the uniform resource buffer

`R_buf=2qB+D`

chronologically realizes every primitive address, and every realized word has at most

`N_circ*L_macro`

completed gates and

`N_circ*L_macro*L_gate`

control edges.

If `s=0`, the word is an exact full-resource return.  If `s>0`, it is a legal nondecreasing
resource-production macro whose output is the exact vector `s`.

### Proof

AC3ue gives the occurrence bound.  Apply AC3uj.  The final two cases are the alternatives
`sum_j v_j=0` and `sum_j v_j>0` in at least one coordinate. QED.

## AC3ul -- buffered circulation closure router -- PROVED UNDER THE DECLARED CONTRACTS

Every primitive nondecreasing circulation address from AC3ug has one continuation:

1. the available resource vector dominates `R_buf` and the circulation is realized chronologically;
2. one coordinate has buffer deficit, returning that exact scarce resource coordinate and amount;
3. an exact-return realization is erased, descends, spends a finite ticket or exits the epoch;
4. a positive-output realization is paid by the finite source/resource ledger, bounded by physical
   headroom, descends in an existing rank or exits the epoch;
5. or one root-state, internal-drawdown, resource-monotonicity, legality, omitted-field or outer-reset
   contract fails.

Under finite payment/ticket/headroom budgets for alternatives 3 and 4, no fixed epoch contains
infinitely many realized primitive circulations.

### Proof

AC3uk gives alternatives 1 and 2.  The realized word returns to the same finite boundary state and
has exact resource output `s`, so zero-output and positive-output cases enter the stated existing
closure mechanisms.  Every unresolved physical hypothesis is retained as a named failure.
An infinite fixed epoch would force infinitely many ticket expenditures, rank decreases, paid
positive outputs, bounded-headroom increases or resets. QED.

## Corrected AC4 numerical frontier

Primitive nondecreasing circulation addresses no longer lack chronological words once a uniform
resource buffer and resource-monotone macro legality are available.  Their required buffer is
`2qB+D`, independent of the circulation length, while their word length is bounded by the primitive
circuit stock.

The remaining numerical work is creation or payment of the required scarce buffer, positive-output
circulations with free or cyclically replenished resources, nonmonotone resource guards, genuinely
nonlinear or nonadditive balances, unbounded zero-sum-free lift residuals, dynamic macro dictionaries,
omitted physical fields and undeclared changes of law.

## Finite check

`scripts/verify_ac_buffered_circulation_ordering.py` exhausts small nondecreasing circulation
multisets, finds an ordering whose boundary prefixes stay above the `2qB` Steinitz buffer, and samples
internal macro words to verify the additional drawdown allowance, final output identity and expanded
gate/control-edge bounds.
