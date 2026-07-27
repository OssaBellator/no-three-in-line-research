# Common ranks for finite scalar-affine phase semigroups

**Branch:** `research/alternating-core-chain`

AC3rk--AC3ro attach one exact scalar-affine map

`f_lambda(h)=A_lambda*h+B_lambda`

to every canonical simple zero-surplus phase-cycle address.  A single map is completely
classified, but arbitrary interleavings may undo one another.  This note isolates two broad
semigroup classes in which a common rank exists for every interleaving:

1. maps sharing one rational fixed centre;
2. translations whose nonzero increments all have one sign.

The result is global across the finite cycle-address family, not merely a bound on consecutive
uses of one word.

## Finite affine family

Let `Lambda` be the finite set of live canonical phase-cycle addresses in one fixed epoch.  For
`lambda in Lambda`, write

`f_lambda(h)=A_lambda*h+B_lambda`,

with `A_lambda,B_lambda in Z`.  Identity cycle words may be quotient-erased.  A change of the
phase graph, edge coefficients, address dictionary or interpretation of `h` is an outer reset.

A **common rational centre** is a reduced rational number

`q=a/d`,  `d>=1`,  `gcd(a,d)=1`,

such that

`f_lambda(q)=q`

for every live address.  Equivalently,

`d*B_lambda=(1-A_lambda)*a`.

For integer `h`, define the integral centred defect

`c=d*h-a`.

## AC3rp -- exact common-centre defect law -- PROVED

If all live affine cycle maps share the rational centre `q=a/d`, then every application of
address `lambda` satisfies

`c'=A_lambda*c`.

Consequently, for any interleaved word

`lambda_1 ... lambda_s`,

`c_s=(prod_(j=1)^s A_(lambda_j))*c_0`.

### Proof

Using `d B_lambda=(1-A_lambda)a`,

`c'=d(A_lambda h+B_lambda)-a`

`=A_lambda(dh-a)+[dB_lambda+(A_lambda-1)a]`

`=A_lambda c`.

Iterate the one-step identity. QED.

Thus every ordering issue disappears after passing to the common centred coordinate: the defect
is multiplied by the product of the visited multipliers.

## AC3rq -- global bounded-defect expansion budget -- PROVED

Assume the common-centre hypothesis and suppose every live multiplier belongs to

`{0,-1,1} union {A in Z:|A|>=2}`.

Along an arbitrary interleaving:

1. if some address with `A_lambda=0` occurs, then `c` becomes zero and remains zero forever;
2. addresses with `|A_lambda|=1` preserve `|c|`;
3. every address with `|A_lambda|>=2` multiplies `|c|` by at least two.

Hence, while a nonzero defect is physically confined to

`1<=|c|<=C`,

the total number of expanding-address occurrences in the entire epoch is at most

`floor(log_2(C/|c_0|))`.

This bound is independent of how the common-centre unit-modulus addresses are interleaved.

### Proof

Apply AC3rp at every step.  A zero multiplier sends the defect to zero, after which every
common-centre map fixes it.  Unit-modulus multipliers preserve the absolute value.  Each
expanding multiplier doubles it at least.  After `r` expanding occurrences,

`|c|>=2^r|c_0|`.

Compare with the physical ceiling `C`. QED.

If the centred defect is unbounded, every expanding occurrence is still an explicit monotone
logarithmic gate: `log_2 |c|` increases by at least one.

## AC3rr -- same-sign translation semigroup -- PROVED

Assume every live map is a translation,

`A_lambda=1`,

and all nonzero increments `B_lambda` have the same sign.  Put

`b_min=min_(lambda:B_lambda!=0)|B_lambda|`.

Then every nonidentity address moves `h` in one strict direction by at least `b_min`.  If

`L<=h<=U`

throughout the epoch, the total number of nonidentity cycle occurrences under arbitrary
interleaving is at most

`floor((U-L)/b_min)`.

Without a physical bound, `h` itself is an explicit monotone common rank.  Identity translations
are quotient stutters.

### Proof

For any interleaved word, the net change is the sum of its increments.  Same-sign nonzero
increments cannot cancel and each contributes magnitude at least `b_min`.  Compare the total
possible displacement with `U-L`. QED.

Mixed-sign translations are the exact residual: they may contain nontrivial zero-sum cancellation
words and require a separate relation, ticket or descent theorem.

## AC3rs -- common-rank affine semigroup router -- PROVED

For the finite live affine cycle-address family, at least one of the following explicit cases
applies:

1. **common rational centre:** use the integral defect `c=dh-a`; this case includes any reset or
   involution maps only when they share that centre with the whole family;
2. **same-sign translation family:** use the monotone coordinate `h`;
3. **mixed-sign translation family:** expose the finite increment set `{B_lambda}` and its
   zero-sum cancellation relations;
4. **mixed-centre affine family:** expose two addresses with no common fixed centre;
5. **changed coefficients or interpretation:** outer reset;
6. **non-affine memory:** outside the scalar-affine theorem.

In cases 1 and 2, every bounded epoch has one common global repetition budget even under arbitrary
interleaving.  In the unbounded case, the displayed defect or translation coordinate is a common
monotone gate unless a zero multiplier reaches the common fixed centre.

### Proof

Test the finite family for the common-centre equations.  If they hold, use AC3rp--AC3rq.  If all
multipliers equal one, inspect the finite increment signs and use AC3rr when they agree.  Failure
of these algebraic tests gives the stated finite residual witnesses.  Individual maps of order
two are not quotiented separately when their centres differ: two such involutions may compose to
a nontrivial translation, so they belong to the mixed-centre branch. QED.

## AC3rt -- conditional closure of ranked affine phase memory -- PROVED UNDER THE COMMON-RANK CONTRACT

Suppose every scalar-affine phase-memory component in one zero-surplus phase epoch is routed by
AC3rs and every live mixed-sign or mixed-centre residual is descending, impossible, ticketed by
its finite exact address, or declared an outer reset.  Then the epoch contains no infinite
nonterminal internal history.

More explicitly:

- common-centre bounded defects admit finitely many expansions;
- same-sign bounded translations admit finitely many nonidentity occurrences;
- common-centre reset maps enter the shared fixed centre permanently;
- common-centre unit-modulus maps preserve the finite centred quotient;
- every remaining extracted cycle spends a finite ticket, decreases a common well-founded rank,
  or exits the epoch;
- the acyclic residue between extracted cycles has the finite bound from AC3rd.

### Proof

Use AC3rq and AC3rr for the two global interleaving budgets.  Absorb only the reset and
unit-modulus maps already controlled by the common-centre coordinate.  Every remaining cycle
occurrence is paid by the declared rank, ticket or exit contract.  Infinite continuation would
force infinitely many bounded expansions, monotone bounded translations, rank decreases or
ticket expenditures. QED.

## Corrected AC4 phase-memory frontier

The unranked affine-semigroup obstruction is now reduced to two exact finite witnesses:

- mixed-sign translation cancellation relations;
- mixed-centre affine maps with no common rational fixed point, including involutions or resets
  whose different centres can generate translations under composition.

Common-centre affine families, same-sign translations, common-centre resets/involutions, bounded
defects and bounded translation ranges now have one global interleaving-safe rank.  Genuinely
nonlinear path memory and changes not recorded as outer resets remain outside the theorem.  The
other AC4 interfaces remain fresh/recreated weighted capacity, unaddressed or nonadditive outputs,
unpaid weighted loss, nonfactoring continuations, recreatable non-source tickets and unresolved
availability/conflict/reverse gates.

## Finite check

`scripts/verify_ac_common_rank_affine_semigroup.py` exhausts small common-centre families and
same-sign translation systems, then samples arbitrary interleavings.  It checks the exact defect
product law, zero-multiplier absorption, global expansion counts, same-sign displacement budgets
and the finite residual classification, including distinct-centre involutions.