# Fixed-axis unary Xi stars yield comparable-cost arc-petal banks

PP3abf--PP3abm reduce a failed fixed-centre rank-two unary `Xi` choice to a
near-complete incoming or outgoing heavy arc star. The apparent fixed-axis
geometry is already a fixed-centre sunflower in typed endpoint resources.

An incoming arc

```text
r -> c
```

uses one variable left resource `L_r` and the common centre resource `R_c`.
Distinct incoming arcs are therefore pairwise resource-disjoint outside the
centre. The outgoing case is transposed. A dyadic support pigeonhole produces a
target-size subbank with comparable local unary costs. Bounded-support averaging
then removes diffuse noncentral collateral, exactly as for transition and
rank-three path petals.

The resulting obstruction is not a fixed row or fixed column as such. It is
centre-core or local arc cost at the removal-credit scale, a global rank-two
unary weight threshold, or residual source/host failure.

## 1. Fixed-axis stars are one-arc petal banks

Fix a captive endpoint index `c`. For the incoming orientation let

```text
H_in(lambda)
=
{r in I_c : a(r,c)>=lambda/2},
```

and for the outgoing orientation let

```text
H_out(lambda)
=
{s in O_c : a(c,s)>=lambda/2}.
```

### Proposition PP3ada -- PROVED

The incoming family has typed endpoint supports

```text
{L_r,R_c},  r in H_in(lambda),
```

and these supports intersect pairwise exactly in the common resource `R_c`.
The outgoing family has supports

```text
{L_c,R_s},  s in H_out(lambda),
```

and these intersect pairwise exactly in `L_c`.

Hence either heavy-star alternative of PP3abk is already a fixed-centre
one-arc petal bank of size `N-o(N)`.

#### Proof

The cell of the arc `r->c` is `(x_r,y_c)`, so its tail and head resources are
`L_r` and `R_c`. Distinct values of `r` give distinct variable left resources.
The outgoing statement is the transpose. PP3abk supplies `N-o(N)` heavy arcs
on one side. ∎

The old-grid description is the same: incoming petals lie on the fixed old row
`y_c`, while outgoing petals lie on the fixed old column `x_c`.

## 2. Comparable-cost target bank

Assume positive arc weights are integers bounded by a polynomial in `m`. Put

```text
L=ceil(log_2(1+max_e a(e)))=m^(o(1)).
```

Partition one heavy star `H` into dyadic classes

```text
2^j <= a(e) < 2^(j+1).
```

### Proposition PP3adb -- PROVED

Some dyadic class `B` has size at least

```text
|H|/L=m^(19/20-o(1)).
```

In particular `B` contains a subbank of size

```text
W=m^(19/40+o(1)).
```

Every retained arc cost lies in one common factor-two interval.

#### Proof

Pigeonhole the `L` dyadic classes. Since `|H|=N-o(N)` and `N/W` is a positive
power of `m`, division by `m^(o(1))` still leaves much more than `W`. ∎

Without polynomial boundedness, the same argument with any finite level
truncation gives either a target-size bounded-level bank or one explicit
high-weight arc core.

## 3. Bounded-support noncentral collateral

For one incoming petal `e=r->c`, write

```text
A_e={L_r}.
```

For an outgoing petal use `A_e={R_s}`. Let `B` be any petal bank and let every
source or paid pattern `F` have typed endpoint support of size at most `r_0`.
Give each pattern nonnegative weight `w(F)`.

### Proposition PP3adc -- PROVED

One has

```text
sum_{e in B}
sum_{F : supp(F) cap A_e != empty} w(F)
<=
r_0 sum_F w(F).
```

Thus the average petal-touching noncentral weight gains a factor `1/|B|`.

#### Proof

The singleton sets `A_e` are pairwise disjoint. A support of size at most `r_0`
can meet at most `r_0` of them. Sum first over petals and then over patterns. ∎

Only patterns supported on the common centre resource remain undiluted across
the bank.

## 4. One-arc conditional single-cycle law

Fix a filler block of size `b>=3` containing the endpoints of one petal arc `e`
and condition on that directed arc.

### Proposition PP3add -- PROVED FROM PP3yy

There are exactly

```text
(b-2)!
```

directed Hamilton cycles containing `e`. Conditional on `e`, every additional
compatible set of `u` arcs has probability

```text
1/(b-2)_u
```

unless the added arcs together with `e` create a proper directed cycle, in
which case the probability is zero.

#### Proof

Contract the prescribed arc to one ordered object. There remain `b-1` cyclic
objects, giving `(b-2)!` directed cyclic orders. Contracting `u` further
compatible arcs gives the displayed ratio. ∎

## 5. Paid averaging across the arc-petal bank

Let `B` be one comparable-cost arc-petal bank. For each `e in B`, classify every
remaining source-invalid canonical pattern by the number `u` of additional
random arcs required after `e` is fixed, and call its count or nonnegative
weight `S_e,u`.

Let

```text
J_e^core
```

be the expected insertion cost supported at the common centre resource, and let

```text
J_e^var
```

contain all petal-touching and other noncentral insertion cost after the correct
selection and cylinder factors are included. Let `R_e>=R_*>0` be the exact
removal credit.

### Theorem PP3ade -- PROVED

A source-valid strict decrease of `Xi` exists whenever

```text
(1/|B|) sum_{e in B} [
  sum_u S_e,u/(b-2)_u
  + (a(e)+J_e^core+J_e^var)/R_*
] < 1.
```

Moreover PP3adc bounds the averaged bounded-support variable term by

```text
O(W_var/|B|)
```

for the corresponding global noncentral weight `W_var`, after restoring its
fixed selection factors.

#### Proof

Choose a petal uniformly from `B`, then choose a uniform conditional
single-cycle completion. PP3add bounds the source-invalid terms. The remaining
summand is normalized expected insertion cost. An outcome below one has no
source violation and total insertion cost below its removal credit, so PP3kx
gives a strict decrease. The variable-term estimate is PP3adc rank by rank. ∎

## 6. Paid trade or a global rank-two unary threshold

Suppose the dyadic bank `B` has

```text
w <= a(e) < 2w
```

for all `e in B`. Let `rho` denote the averaged normalized source, centre-core,
and variable residual objective excluding `a(e)/R_*`.

### Corollary PP3adf -- PROVED

Fix `tau>0` and suppose

```text
rho <= 1-tau.
```

Then at least one of the following holds.

1. **Paid arc-petal completion:**

   ```text
   2w/R_* + rho < 1,
   ```

   so PP3ade gives a strict decrease.

2. **Global rank-two unary weight at bank-credit scale:**

   ```text
   A_2 >= sum_{e in B} a(e)
       >= (tau/2) R_* |B|.
   ```

   In particular, for a target subbank,

   ```text
   A_2 >= (tau/2) R_* W.
   ```

#### Proof

If the first inequality holds, every local arc cost is below `2w` and PP3ade
applies. Otherwise `2w/R_*+rho>=1`; using `rho<=1-tau` gives
`w>=tau R_*/2`. Sum the lower dyadic bound over `B`. ∎

Thus a comparable-cost fixed-axis bank cannot fail diffusely: either one petal
is paid after averaging, or the global support-ranked unary weight is already
at the total bank-credit scale. If `rho` is not bounded below one, the failure
is residual source, centre-core, or nonunary paid concentration.

## 7. Revised rank-two unary endpoint

### Corollary PP3adg -- PROVED

At a source-light captive centre, rank-two unary `Xi` weight reduces to one of:

1. a locally clean cheap two-arc centre segment and the conditional criterion
   PP3abi;
2. a paid average completion through a `W`-sized incoming or outgoing arc-petal
   bank;
3. centre-core, residual source, higher-rank paid, or endpoint-host failure;
4. global rank-two unary weight at the bank-credit scale

   ```text
   A_2=Omega(R_* W).
   ```

Therefore a near-complete fixed-row or fixed-column unary-cost star is no
longer an independent marked-`Xi` frontier. It rejoins the fixed-centre
paid-petal, global support-ranked threshold, and residual centre-core
conversion problems.

## 8. Finite diagnostic

The script

```text
scripts/check_unary_xi_arc_petals.py
```

checks a finite incoming or outgoing heavy star. It verifies the fixed-centre
typed-resource sunflower, dyadic support pigeonhole, target-bank extraction,
the one-arc paid upper bound, and the global-weight lower bound in the failed
paid branch.
