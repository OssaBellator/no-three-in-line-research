# Constant-amplified exact-width slab patches and prime transfer

The fixed-infrastructure theorem PP3avl gives the correct exponent `21/40=0.525`, but
the all-`n` transfer needs two additional quantitative facts.

1. The leading patch-width constant must exceed the constant in the backward
   prime-interval theorem.
2. The patch must have the exact requested width, not merely one preferred width
   `MW`.

Both issues are bookkeeping consequences of the slab architecture.  The constants
`a,b` in PP3gr amplify the leading coefficient arbitrarily, and a full-scale target
width is partitioned among `Theta(M)` macros whose individual widths differ by at most
one.  A heterogeneous hypergeometric allocation gives the same local Ore conclusion.

The final prime transfer deliberately chooses a prime one short-interval farther back,
so the requested patch width is always `Theta(m^0.525)`.  No small-width allocation
regime is needed.

## 1. Arbitrary leading coefficient

Fix the controller-domain density constant `gamma>0`.  PP3gr uses

```text
M=floor(a m^(1/20)),
R=floor(b m^(19/20)),
W=floor(gamma sqrt(R)/16),
```

with fixed `a,b>0` and `ab<1`.

### Proposition PP3awq -- PROVED

For every prescribed constant `K_0>0`, there are fixed `a,b>0` with `ab=1/2` such
that

```text
MW=(K_0+o(1))m^(21/40).
```

One explicit choice is

```text
b=(gamma/(32K_0))^2,
a=1/(2b).
```

#### Proof

The choice gives `ab=1/2`.  PP3gr gives leading coefficient

```text
a gamma sqrt(b)/16
=
gamma/(32 sqrt(b))
=
K_0.
```

Floors contribute only `o(m^(21/40))`. ∎

Thus the exponent-optimal architecture has no fixed upper bound on its leading
constant.  Making `b` smaller shrinks each pool by a fixed factor and increases the
number of disjoint pools by the reciprocal fixed factor.

## 2. Exact partition of one full-scale target width

Let `W` and `M` be the maximal local width and macro count supplied by PP3awq.  Fix an
integer target width `t` with

```text
W<=t<=MW.
```

Put

```text
L=ceil(t/W).
```

### Proposition PP3awr -- PROVED

There are integers `w_1,...,w_L` satisfying

```text
sum_i w_i=t,
W/3<=w_i<=W
```

for all sufficiently large `W`, and any two widths differ by at most one.

#### Proof

Distribute `t` as evenly as possible among `L` parts, using
`floor(t/L)` and `ceil(t/L)`.  Since `L>=t/W`, every part is at most `W`.  Also

```text
t/L>=t/(t/W+1)>=W/2.
```

After the harmless integer floor, every part is at least `W/3` for large `W`. ∎

Every active macro therefore stays at the original square-root scale.  The internal
macro theorem applies because its local-lemma condition is monotone under decreasing
`w_i`.

## 3. Heterogeneous balanced ownership

Let the movement and refill label sets each have exact size

```text
T=t=sum_i w_i.
```

Choose independent uniform ordered partitions into labelled classes of sizes
`w_1,...,w_L`.

### Proposition PP3aws -- PROVED

For a fixed subset `D` of one label set and one macro `i`, the class count satisfies

```text
Pr(X_i(D)>w_i|D|/T+u_i)
<=exp(-2u_i^2/w_i).
```

#### Proof

The `i`-th class is a uniform `w_i`-subset of the `T` labels.  Apply Hoeffding's
inequality for sampling without replacement exactly as in PP3na. ∎

### Theorem PP3awt -- PROVED

Suppose every macro nonedge `(A,B) notin J_i` satisfies

```text
bar_d_i(A)+bar_e_i(B)<=T-h.
```

If positive deviations `u_i` satisfy

```text
2u_i<=w_i h/T
```

for every `i` and

```text
2T sum_i exp(-2u_i^2/w_i)<1,
```

then there are partitions of the prescribed heterogeneous sizes for which every
induced graph

```text
J_i[A_i,B_i]
```

has a perfect matching.

#### Proof

With positive probability all row and column nonneighbor counts are at most their
hypergeometric means plus `u_i`.  For a nonedge of the induced graph, the two induced
nondegrees then sum to at most

```text
(w_i/T)(T-h)+2u_i<=w_i.
```

The local Ore theorem PP3gj gives a perfect matching in each macro.  The classes form
partitions, so every numerical label is used exactly once. ∎

### Corollary PP3awu -- PROVED

For the widths from PP3awr, take

```text
u_i=sqrt(w_i log(4LT)),
h=2T max_i sqrt(log(4LT)/w_i).
```

Then the probability condition holds and

```text
h=o(T).
```

#### Proof

The union bound is at most

```text
2LT(4LT)^(-2)<1.
```

Since every `w_i>=W/3` and `W` is polynomial in `m`,

```text
h/T=O(sqrt(log m/W))=o(1).
```

∎

This is the exact heterogeneous analogue of PP3nb--PP3nc.

## 4. Uniform geometry and failure conversion

### Proposition PP3awv -- PROVED / CONDITIONAL ESTABLISHED SLAB INTERFACES

Let `t` lie in a fixed positive constant-factor band around `m^(21/40)`, and use the
partition PP3awr.  Then all geometric and repair inputs of the fixed-infrastructure
chain remain valid uniformly.

1. Every local width is `Theta(W)` and at most the PP3gr width.
2. The total number of slots is exactly `2t=Theta(MW)`.
3. Patch-only and ordinary source-anchor event counts are no larger than the maximal
   `MW` construction, up to fixed constants.
4. The heterogeneous slack satisfies `h=o(t)`.
5. A failed score condition still supplies numerator mass `Omega(Rt)`.
6. Since `t=Theta(MW)` and `M->infinity`, the fixed-label and fixed-macro resource
   extractions retain target order `Omega(W)`.
7. Every repair is realized by the pool-compatible, activation-safe support chain
   PP3aux--PP3awp.

#### Proof

Items 1--4 are PP3awr--PP3awu and monotonicity of the fixed-rank event counts in the
number of active slots.  The score argument PP3alu--PP3alv uses only the denominator
margin and `T-h=Theta(T)`, giving item 5 with `T=t`.  The resource extraction proofs
PP3alc--PP3alt require `R=Theta(W^2)` and `t/W=Theta(M)->infinity`, which hold throughout
the stated band.  Item 7 is the fixed-infrastructure realization already audited in
PP3awc--PP3awp. ∎

No new local geometric event is introduced by unequal macro widths.

## 5. Exact-width slab theorem

### Theorem PP3aww -- PROVED / CONDITIONAL ESTABLISHED PRIME-PATCHING INTERFACES

Fix constants `0<c_0<c_1`.  Choose the slab coefficient in PP3awq larger than `c_1`.
For every sufficiently large saturated no-three source of side `m` and every integer

```text
c_0 m^(21/40)<=t<=c_1 m^(21/40),
```

the fixed-infrastructure process installs a saturated no-three patch of exact width
`t`.

#### Proof

The lower bound and `M->infinity` imply `t>=W` for large `m`.  The amplified maximal
width exceeds `c_1m^(21/40)`, so `t<=MW`.  Partition `t` by PP3awr, allocate labels by
PP3awt--PP3awu, and apply the uniform fixed-attempt and monotone termination chain from
PP3awv and PP3avj--PP3avk.  Each new row and column label in `{m+1,...,m+t}` is used
exactly once in each of the two balanced patch layers, so the final side length is
exactly `m+t`. ∎

The theorem is conditional on the same already named conversion interfaces as PP3avl;
it removes the additional exact-width and leading-constant assumptions.

## 6. Shifted backward-prime interval

Assume the published short-interval input used in PP4b: every sufficiently large real
`y` has a prime in

```text
[y-y^(21/40),y].
```

For a target side `n`, put

```text
x=n+1,
y=x-x^(21/40).
```

### Proposition PP3awx -- PROVED UNDER THE SHORT-INTERVAL INPUT

There is a prime `p<=y` such that, with `m=p-1` and `t=n-m=x-p`,

```text
x^(21/40)<=t<=x^(21/40)+y^(21/40).
```

Consequently

```text
t=(c+o(1))m^(21/40)
```

for some `c in [1,2]`.

#### Proof

Choose `p in [y-y^(21/40),y]`.  Then

```text
x-y=x^(21/40)
```

and

```text
x-p<=(x-y)+y^(21/40).
```

Also `m/x->1`, so both endpoint powers are `(1+o(1))m^(21/40)`. ∎

The shift deliberately keeps the required patch width away from zero.

## 7. Constant-complete prime transfer

### Theorem PP3awy -- PROVED UNDER THE STATED HYPOTHESES

Assume:

1. every sufficiently large prime `p` supplies a saturated no-three source on
   `[p-1]^2`;
2. the established prime-patching conversion interfaces used in PP3aww hold; and
3. the published exponent-`21/40` backward-prime interval theorem holds.

Then every sufficiently large integer `n` has a saturated no-three set of size `2n`
on `[n]^2`.

#### Proof

Choose `m=p-1` and `t=n-m` by PP3awx.  For large `n`, the ratio
`t/m^(21/40)` lies in any fixed interval containing `[1,2]`, for example
`[1/2,5/2]`.  Choose the amplified slab coefficient larger than `5/2` and apply the
exact-width theorem PP3aww.  The patch extends the prime-minus-one seed to side `n`.
The row bound gives optimality. ∎

This removes the leading-constant gap in PP4b.  A coefficient hidden inside
`Omega(m^0.525)` is no longer being compared with the prime-interval constant.

## 8. Revised global frontier

### Corollary PP3awz -- PROVED

The all-`n` transfer no longer has an independent:

1. patch leading-constant problem;
2. exact full-scale width problem; or
3. small-width patch problem.

The shifted-prime choice uses only exact widths in a full-scale constant-factor band.
The remaining global tasks are:

1. finish the hypothesis audit and consolidation of the conditional prime-patching
   interfaces in PP3aww;
2. prove or import the saturated prime-minus-one seed theorem required in PP3awy; and
3. make the short-interval threshold and finite initial range effective if an explicit
   all-`n` threshold is desired.

The no-three-in-line conjecture remains unproved.
