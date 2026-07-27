# Cone alternative for coupled auxiliary-macro resources

**Branch:** `research/alternating-core-chain`

AC3tx--AC3ub close an auxiliary macro cycle when every gross resource creation is paid from a finite
nonreplenishing source stock. The remaining additive obstruction is a finite family of macros which
may transfer units among several unbounded resource coordinates. Coordinatewise consumption need not
be monotone, so no single raw stock is automatically a rank.

This note applies the exact finite-dimensional theorem of alternatives to the macro increment
vectors. Either one positive integer linear functional decreases on every live nonstuttering macro,
or there is a bounded primitive nonnegative circulation witness. The second outcome is an explicit
finite address: it is the precise coupled-resource obstruction that still needs chronological
realization, payment, descent, a ticket or reset.

## Coupled additive macro model

Fix one root-boundary epoch. Let:

- `m in Z_(>=0)^q` be the vector of physical resource stocks, with `q>=1`;
- `Lambda` be the finite live nonstuttering macro dictionary, with `k=|Lambda|>=1`;
- macro `lambda` have fixed gross consumption `c_lambda in Z_(>=0)^q`, gross creation
  `r_lambda in Z_(>=0)^q`, and net vector

  `v_lambda=r_lambda-c_lambda in Z^q`;

- `|v_(i,lambda)|<=B` for every coordinate and macro;
- every macro contain at most `L_macro` completed root-return gates, and every gate contain at most
  `L_gate` underlying control edges.

A macro is legal at `m` only when `m>=c_lambda` coordinatewise and

`m'=m+v_lambda>=0`.

Assume the **coupled additive Markov contract**: the complete macro address contains every field
controlling legality, gross occurrence identities, payment status and the update vector. A change of
the dictionary, vectors, interpretation or omitted field is an outer reset. Quotient stutters,
independent descents and already-ticketed cycles retain their existing routes.

Let `V` be the `q x k` integer matrix whose `lambda`-column is `v_lambda`.

## AC3uc -- common positive resource rank -- PROVED

Suppose there is a vector `w in Z_(>0)^q` and an integer `delta>=1` such that

`w dot v_lambda<=-delta`

for every live macro. Then

`H_w(m)=w dot m`

strictly decreases by at least `delta` on every legal macro. Hence every fixed epoch contains at
most

`floor(H_w(m^(0))/delta)`

live nonstuttering macro executions.

The corresponding contribution is at most

`floor(H_w(m^(0))/delta)*L_macro`

completed root-return gates and at most

`floor(H_w(m^(0))/delta)*L_macro*L_gate`

underlying control edges.

### Proof

For one legal macro,

`H_w(m')-H_w(m)=w dot v_lambda<=-delta`.

The potential is a nonnegative integer because `w,m` are nonnegative integral vectors. Summing the
strict decrease gives the macro count, and the two word-length bounds follow by expansion. QED.

## AC3ud -- exact cone alternative -- PROVED

Exactly one of the following systems has a solution:

1. **strict positive rank:** a rational vector `w in Q_(>0)^q` satisfying

   `w dot v_lambda<0`

   for every `lambda in Lambda`;

2. **nondecreasing circulation:** a nonzero vector `x in Z_(>=0)^k` satisfying

   `Vx>=0`

   coordinatewise.

In the second branch, `x_lambda` is the multiplicity of macro address `lambda`, and `Vx` is the
nonnegative net resource output of the algebraic circulation.

### Proof

Form the `(k+q) x q` matrix `C` whose first `k` rows are the transposes `v_lambda^T` and whose final
`q` rows are `-e_i^T`. Gordan's theorem says exactly one of the systems

`Cw<0`

or

`C^T y=0, y>=0, y!=0`

is solvable. The first system is precisely alternative 1. Write a solution of the second as
`y=(x,z)` with `x in R_(>=0)^k` and `z in R_(>=0)^q`. Then

`Vx-z=0`,

so `Vx=z>=0`. Necessarily `x!=0`, since `x=0` would force `z=0`. The cone is rational because all
coefficients are integral, so a rational solution exists and may be scaled to a nonzero integer
vector. This gives alternative 2.

The alternatives are mutually exclusive: if both existed, then

`w dot Vx=sum_lambda x_lambda(w dot v_lambda)<0`,

while `Vx>=0` and `w>0` would give `w dot Vx>=0`. QED.

## AC3ue -- bounded primitive circulation address -- PROVED

Put

`B_0=max(B,1)`

and

`D_q=ceil(q^(q/2)*B_0^q)`.

Whenever AC3ud returns a nondecreasing circulation, it has a primitive representative `(x,z)` with

`Vx-z=0`, `x,z>=0`,

such that:

1. at most `q+1` entries of the combined vector `(x,z)` are nonzero;
2. every nonzero coefficient is at most `D_q`;
3. the macro multiplicity satisfies

   `|x|_1<=(q+1)D_q`.

A safe stock of exact primitive circulation addresses is

`K_circ=sum_(s=1)^(q+1) binom(k+q,s)*D_q^s`.

### Proof

Choose a support-minimal nonzero solution of

`sum_lambda x_lambda v_lambda-sum_i z_i e_i=0`

and divide all coefficients by their gcd. Its supporting columns form a positive circuit in
`R^q`, hence the support has size at most `q+1`. Circuit coefficients are the absolute maximal
minors of a supporting matrix of rank at most `q`. Every column is either a macro vector, of
Euclidean norm at most `sqrt(q)B_0`, or a unit coordinate vector. Hadamard's inequality therefore
bounds every primitive coefficient by

`(sqrt(q)B_0)^q=q^(q/2)B_0^q`,

and the integer ceiling gives `D_q`. Summing at most `q+1` macro coefficients gives the third bound.
Finally choose the support and then each positive coefficient to obtain the displayed safe address
stock. QED.

The circulation is an algebraic count-vector witness. Its macros need not yet admit one legal
chronological ordering from a common resource state. Chronological realizability is therefore an
explicit physical contract, not an implicit consequence of the cone identity.

## AC3uf -- bounded coupled-resource epochs -- PROVED

In the strict-rank branch, scale a rational separator from AC3ud to a primitive positive integer
vector `w`, and put

`delta=min_lambda(-w dot v_lambda)>=1`.

Then AC3uc gives the exact macro, gate and control-edge budgets. In particular, arbitrary transfers
between resource coordinates cannot prolong the epoch once one positive separator exists.

If every coordinate is physically bounded instead, the exact state stock is finite and the existing
auxiliary-state cycle theorem applies without a separator.

### Proof

Clearing denominators preserves every strict inequality and produces a positive integer vector.
The minimum strict integer decrease is at least one. Apply AC3uc. The bounded-coordinate statement
is ordinary finite-state recurrence on the complete augmented state. QED.

## AC3ug -- coupled-resource cone router -- PROVED UNDER THE DECLARED CONTRACTS

Every finite coupled additive macro family has one continuation:

1. a positive integer common resource rank with an explicit macro/gate/edge budget;
2. a primitive nondecreasing circulation using at most `(q+1)D_q` macro occurrences and one of at most
   `K_circ` exact addresses;
3. finite exact-state closure when every resource coordinate is physically bounded;
4. quotient stutter, independent descent, existing finite ticket or outer reset;
5. or one legality, gross-occurrence, address, update-vector, omitted-field or additivity failure.

In the circulation branch, closure additionally requires the **chronological circulation-extraction
contract**: every infinite unranked legal macro history contains a chronological subhistory whose
count vector contains one primitive circulation address and whose erasure or execution is legal from
the declared boundary state. If every extracted primitive address is impossible, strictly descending,
paid by a finite occurrence-faithful resource ledger, assigned a finite ticket, or declared an outer
reset, then the coupled additive epoch terminates.

### Proof

Apply AC3ud. The rank branch is AC3uc/AC3uf. The obstruction branch is reduced by AC3ue to a finite
bounded algebraic address. The bounded-coordinate and pre-existing cycle routes are unchanged.
Algebraic existence alone does not impose an order on the macros, so the chronological extraction
hypothesis is retained explicitly. Under that hypothesis, an infinite unranked history would force
infinitely many rank decreases, bounded-state returns, ticket expenditures, paid extracted
circulations or resets. QED.

## Corrected AC4 numerical frontier

Several coupled additive macro resources no longer require ad hoc coordinatewise monotonicity. Their
finite increment dictionary either has one interleaving-safe positive integer rank or exposes a
bounded primitive nondecreasing circulation address.

The remaining numerical work is chronological realization and payment of those nondecreasing
circulations, free or cyclically replenished circulation resources, genuinely nonlinear or
nonadditive balances, unbounded zero-sum-free lift residuals, dynamic macro dictionaries, omitted
payment fields and undeclared changes of law.

## Finite check

`scripts/verify_ac_coupled_resource_cone_router.py` exhausts small one- and two-resource increment
families, checking the strict-rank/nondecreasing-circulation alternative and primitive circuit bounds.
It also samples higher-dimensional ranked systems and legal histories, verifying the common-potential
macro count and the expanded gate/control-edge budgets.
