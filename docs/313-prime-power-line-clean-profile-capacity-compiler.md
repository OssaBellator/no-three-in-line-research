# Rank/profile capacities compile line-clean rows into integer slack

CMR1590--CMR1597 give exact line-clean integer budgets, and CMR1638--CMR1645
give simple universal floors.  The remaining geometric information arrives as
finite bounds on exact rank/profile/owner/height/token/prefix/carry classes.
This chapter compiles those class capacities into one weighted count.  Either
the complete row lies inside an exact or universal budget, or failure forces one
explicitly large overflow class.

Fix response side `d>=4`, destroyed target load `D>=0`, current potential `m`,
and one line-clean coefficient class represented by the fractional factor

\[
q=u/v.
\]

For residual rank `r in {1,2,3}`, put

\[
c_1=(d-1)(d-2),
\qquad c_2=d-2,
\qquad c_3=1.
\]

Let `X` be a finite exact class set.  Each class `chi` has rank `r(chi)`, actual
corrected candidate count `N_chi`, and proved integer capacity

\[
0\le N_\chi\le C_\chi.
\]

Let the unavailable-edge count satisfy `0<=b<=B`.

## 1. Weighted class-capacity envelope

Define

\[
\widehat W
=
\sum_{\chi\in\mathcal X}c_{r(\chi)}C_\chi
+(m+1)B(d-1)(d-2).
\]

### Theorem CMR1678 -- PROVED

The exact weighted line-clean count satisfies

\[
\boxed{W_d\le\widehat W.}
\]

### Proof

CMR1590 writes `W_d` as the sum of rank costs times exact candidate counts plus
the unavailable-edge cost.  Substitute `N_chi<=C_chi` and `b<=B`. ∎

The classes may retain every finite geometric label needed later.

## 2. Exact side-dependent capacity certificate

Let

\[
B_{d,u,v}(D)
=
\left\lfloor
\frac{D u^d d(d-1)(d-2)-1}{(dv)^d}
\right\rfloor
\]

be the exact CMR1593 budget.

### Theorem CMR1679 -- PROVED

If

\[
\boxed{\widehat W\le B_{d,u,v}(D),}
\]

then every line-clean row consistent with the class capacities is a strict
improvement.

### Proof

CMR1678 gives `W_d<=widehat W`; CMR1593 says improvement is equivalent to
`W_d<=B_{d,u,v}(D)`. ∎

Thus one class-capacity table certifies an entire family of exact hosts.

## 3. Universal floor specialization

Let `B_univ` be the applicable universal budget from CMR1641:

\[
\left\lceil D(d)_3/16\right\rceil-1
\]

for strong traces,

\[
\left\lceil 81D(d)_3/4096\right\rceil-1
\]

for singleton traces, or

\[
\left\lceil D(d)_3/256\right\rceil-1
\]

for endpoint-overlap traces.

### Theorem CMR1680 -- PROVED

The host-uniform condition

\[
\boxed{\widehat W\le B_{\mathrm{univ}}}
\]

certifies strict improvement without evaluating the side-dependent permanent
ratio.

### Proof

Apply CMR1678 followed by CMR1641. ∎

The exact budget may be used whenever the universal floor is too weak.

## 4. Failure forces one weighted overflow class

Separate the weighted contributions into `K` nonnegative integer coordinates:
one for every candidate class and, when `B>0`, one unavailable-edge coordinate.
Write them as

\[
w_1,\ldots,w_K,
\qquad
W_d=\sum_{i=1}^K w_i.
\]

### Theorem CMR1681 -- PROVED

If an integer budget `B_*` fails,

\[
W_d>B_*,
\]

then one coordinate satisfies

\[
\boxed{
w_i\ge
\left\lfloor B_*/K\right\rfloor+1.
}
\]

Consequently its proved capacity must be at least the same threshold.

### Proof

If every coordinate were at most `floor(B_*/K)`, their sum would be at most
`K floor(B_*/K)<=B_*`, a contradiction.  Actual contribution is bounded by its
capacity contribution. ∎

This localizes every failed coarse budget to one finite geometric class or to
the unavailable-edge coordinate.

## 5. Candidate-count consequence

For a candidate class `chi` of rank `r`, its weighted contribution is

\[
w_\chi=c_rN_\chi.
\]

### Theorem CMR1682 -- PROVED

If `chi` witnesses CMR1681 at threshold `L`, then

\[
\boxed{
N_\chi\ge
\left\lceil L/c_r\right\rceil.
}
\]

In particular, rank-three overflow is measured without loss, while rank-one and
rank-two overflow have the exact conversion factors `(d-1)(d-2)` and `d-2`.

### Proof

The inequality `c_rN_chi>=L` is equivalent to the displayed integral ceiling. ∎

The result converts a failed line-clean certificate into a quantitative
candidate concentration statement.

## 6. Unavailable-edge overflow

The unavailable coordinate is

\[
w_b=(m+1)b(d-1)(d-2).
\]

### Theorem CMR1683 -- PROVED

If the unavailable coordinate witnesses CMR1681 at threshold `L`, then

\[
\boxed{
b\ge
\left\lceil
L/[(m+1)(d-1)(d-2)]
\right\rceil.
}
\]

Conversely any proved cap below this ceiling excludes unavailable-edge overflow
and forces the failed budget into a candidate class.

### Proof

Solve the displayed weighted contribution inequality for the integer `b`. ∎

This separates geometric collateral overflow from restricted-host scarcity.

## 7. Mixed exact and bounded class tables

Partition the classes into an exactly enumerated set `E` and a bounded residual
set `R`.  Put

\[
W_E=
\sum_{\chi\in E}c_{r(\chi)}N_\chi
\]

and

\[
\widehat W_{\mathrm{mix}}
=
W_E+
\sum_{\chi\in R}c_{r(\chi)}C_\chi
+(m+1)B(d-1)(d-2).
\]

### Theorem CMR1684 -- PROVED

All conclusions of CMR1679--CMR1683 remain valid with `widehat W` replaced by
`widehat W_mix`.  The exact integer slack is

\[
\boxed{
S_{\mathrm{mix}}
=
D u^d d(d-1)(d-2)
-(dv)^d\widehat W_{\mathrm{mix}}.
}
\]

A positive slack certifies every residual realization covered by the capacities.

### Proof

Use exact contributions on `E`, capacity bounds on `R`, and repeat the proofs of
CMR1678--CMR1683.  The slack is CMR1596 with the mixed upper count. ∎

This allows normalized thin tables to be inserted incrementally while inherited
bounds control the remaining classes.

## 8. Profile-capacity endpoint

### Corollary CMR1685 -- PROVED

Every line-clean geometric class table now has an exact compiler.

1. Weight rank-one, rank-two and rank-three capacities by `c_1,c_2,c_3`.
2. Add the unavailable-edge capacity in the same integer currency.
3. Compare the total with the exact or universal class budget.
4. If the budget passes, publish one positive integer slack.
5. If it fails, retain only the candidate or availability classes meeting the
   explicit overflow threshold of CMR1681--CMR1683.
6. For rooted traces use only the strong or singleton budgets.

The remaining work is to prove sufficiently small inherited capacities or
certify the finitely many overflow classes individually.  No all-`n` theorem is
claimed.

Weighted capacity envelopes, exact/universal budget implications, overflow
localization and mixed-table slacks are checked in
[`scripts/verify_prime_power_line_clean_profile_capacity_compiler.py`](../scripts/verify_prime_power_line_clean_profile_capacity_compiler.py).
