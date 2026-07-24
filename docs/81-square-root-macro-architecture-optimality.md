# Optimality of the disjoint square-root macro architecture

The slab rebalancing PP3gr uses almost maximal pool size and only
`m^{1/20+o(1)}` macro variables.  This chapter shows that those exponents are
forced, up to constants, by any architecture with disjoint source pools and
square-root local width.

## 1. Macro-count lower bound

Suppose `M` pairwise disjoint source pools each have size at most `R`, and one
macro on one pool installs width at most

\[
 C\sqrt R
\]

for some fixed constant `C>0`.  Let the total installed width be `T`.

### Proposition PP3gv -- PROVED

One necessarily has

\[
 \boxed{
 M\ge \frac{T^2}{C^2m}.
 }
\]

#### Proof

The width assumption gives

\[
 T\le CM\sqrt R.
\]

Hence

\[
 R\ge \frac{T^2}{C^2M^2}.
\]

Disjointness gives `MR<=m`, so

\[
 \frac{T^2}{C^2M}
 \le MR
 \le m.
\]

Rearrange. ∎

For

\[
 T=m^{21/40+o(1)},
\]

this yields

\[
 M\ge m^{1/20-o(1)}.
\]

Thus PP3gr attains the smallest possible macro-count exponent in the disjoint
square-root framework.

## 2. Pool-size upper bound

### Corollary PP3gw -- PROVED

At total width `T`, any extremal-scale square-root architecture has

\[
 \boxed{
 R\le \frac{C^2m^2}{T^2}.
 }
\]

At the prime-gap target this is

\[
 R\le m^{19/20+o(1)}.
\]

#### Proof

Since at least one macro is used, the source budget and width inequalities give

\[
 T\le C\frac mR\sqrt R
 =\frac{Cm}{\sqrt R}.
\]

Rearrange. ∎

The slab choice `R=m^{19/20+o(1)}` therefore uses the largest possible local
pool exponent compatible with total width `m^{21/40}`.

## 3. Formal rank-three mass barrier

Assume a rank-three slot event has only the universal probability scale

\[
 O(1/R).
\]

With total width `T`, one slot has `Theta(T^2)` formal partner-slot pairs.

### Proposition PP3gx -- PROVED

Within the disjoint square-root macro framework, the uncompressed formal
rank-three mass scale cannot be smaller than

\[
 \boxed{
 \frac{T^4}{C^2m^2}.
 }
\]

At `T=m^{21/40+o(1)}`, this is

\[
 m^{1/10-o(1)}.
\]

#### Proof

The formal mass scale is `T^2/R`.  Apply PP3gw:

\[
 \frac{T^2}{R}
 \ge
 \frac{T^4}{C^2m^2}.
\]

∎

Consequently, exponent rebalancing alone can never make all rank-three events
summable.  Even the optimal slab balance still needs a geometric or arithmetic
saving of `m^{1/10+o(1)}` in the unrestricted three-slot population.

## 4. Localized mixed-class barrier

The slab theorem PP3gp localizes one mixed class to two macro variables.  Its
formal incident slot count is `Theta(MW^2)`.  Since `W^2=Theta(R)`, the
corresponding `O(1/R)` mass scale is `Theta(M)`.

### Corollary PP3gy -- PROVED

Any disjoint square-root architecture reaching width `T` has localized mixed
mass scale at least

\[
 \boxed{
 \Omega\left(\frac{T^2}{m}\right).
 }
\]

At the prime-gap target this is

\[
 m^{1/20-o(1)}.
\]

#### Proof

The localized coarse mass is `Theta(M)`.  Apply PP3gv. ∎

Thus the `m^{1/20}` saving still needed after slab localization is also optimal
at the exponent level within this architecture.

## 5. Architectural conclusion

The slab balance closes all exponent choices that can be improved merely by
changing `M,R,W` under

\[
 MR\le m,
 \qquad
 W=Theta(\sqrt R),
 \qquad
 MW=T.
\]

The remaining work cannot come from another power-law rebalance.  It must
supply genuine completion-energy compression:

1. an `m^{1/10+o(1)}` saving for unrestricted all-movement, all-refill, and
   three-macro relation families; or
2. an `m^{1/20+o(1)}` saving for the mixed family already localized by slab
   ordering; or
3. a stronger structural cancellation that removes those relation families
   before the weighted local lemma.

This makes the residual exponent gap explicit and proves it is intrinsic to
the current disjoint square-root macro design, not an artifact of the earlier
choice of pool size.
