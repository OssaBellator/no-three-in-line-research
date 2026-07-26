# Returned-edge churn has an exact exchange-pair kernel

CMR395, CMR418--CMR421 and CMR1520 identify edge return as the remaining
currency after finite token stock is exhausted.  The current roadmap asks for a
return-row coefficient.  A selected-state reset already contains the exact
combinatorial carrier for that coefficient.

If an old perfect matching `M` is replaced by a new perfect matching `M'`, every
vacated edge has one canonical entering partner in the same source row and one
canonical entering partner in the same target column.  Every genuinely recreated
credit contains an entering edge.  Assign the credit to its absolute
last-entering owner and then transport that owner to its vacated same-source
predecessor.  This gives an exact returned-edge kernel, not merely a bound by the
total churn magnitude.

The theorem does not prove the kernel subcritical.  It gives the finite exact
row which must be estimated by line, height, prefix, carry and selector classes.

Let

\[
M,
\qquad
M'
\]

be perfect matchings of one finite bipartite host on the same source and target
vertex sets.  Put

\[
E^+=M'\setminus M,
\qquad
E^-=M\setminus M'.
\]

Edges in `E^+` are entering selected edges.  Edges in `E^-` are vacated selected
edges returned to the complementary available host.

## 1. Canonical source and target exchange bijections

For a source vertex `x` whose selected edge changes, write

\[
f_x=(x,M(x))\in E^-,
\qquad
a_x=(x,M'(x))\in E^+.
\]

### Theorem CMR1574 -- PROVED

The map

\[
\boxed{
\pi_{\rm src}:E^-\to E^+,
\qquad
\pi_{\rm src}(f_x)=a_x
}
\]

is a bijection.  Likewise, pairing the old and new selected edges at each target
vertex gives a bijection

\[
\boxed{
\pi_{\rm tgt}:E^-\to E^+.
}
\]

Consequently

\[
\boxed{|E^-|=|E^+|.}
\]

### Proof

At every changed source there is exactly one old selected edge and exactly one
new selected edge.  Unchanged sources contribute neither an entering nor a
leaving edge.  Distinct sources give distinct old and new edges, so the source
map is bijective.  Apply the same argument at target vertices. ∎

The source pairing is used below because it keeps the owner source coordinate
visible.

## 2. Alternating-cycle exchange signature

### Theorem CMR1575 -- PROVED

The symmetric difference

\[
M\triangle M'
\]

is a vertex-disjoint union of even alternating cycles.  For every
`f in E^-`, the pair

\[
\boxed{(f,\pi_{\rm src}(f))}
\]

lies in one common alternating cycle.  Its cycle length is therefore one finite
exchange label.

### Proof

Every vertex in the symmetric difference has degree zero or two: one incident
old edge and one incident new edge.  A finite degree-two bipartite component is
an even cycle, and the two same-source edges are consecutive on that cycle. ∎

No cycle orientation is needed for the source pairing.

## 3. Every recreated credit has one entering owner

Let `C` be one physical credit system whose members are finite selected-edge
sets; in the no-three-in-line application they are physical collinear triples.
Call a credit `C` **recreated** by the transition when

\[
C\subseteq M',
\qquad
C\nsubseteq M.
\]

Retain the absolute entering-edge order used by the last-creation ledger.

### Theorem CMR1576 -- PROVED

Every recreated credit satisfies

\[
\boxed{C\cap E^+\ne\varnothing.}
\]

Hence it has one unique absolute last-entering owner

\[
\boxed{o(C)=\max(C\cap E^+).}
\]

### Proof

If `C` contained no entering edge, every edge of `C subseteq M'` would also lie
in `M`, contradicting `C not subseteq M`.  The fixed absolute order makes the
maximum unique. ∎

This is the exact support statement of CMR418 with the canonical owner retained.

## 4. Transport from entering owner to returned predecessor

For an entering edge

\[
a=(x,M'(x))\in E^+,
\]

define its returned predecessor

\[
\boxed{
p(a)=(x,M(x))
=\pi_{\rm src}^{-1}(a)\in E^-.
}
\]

### Theorem CMR1577 -- PROVED

Every recreated credit `C` is assigned to exactly one returned edge

\[
\boxed{r(C)=p(o(C)).}
\]

The map is deterministic from the transition, absolute owner order and credit.
No recreated credit is lost or assigned twice.

### Proof

CMR1576 gives one owner `o(C) in E^+`.  CMR1574 gives its unique source
predecessor in `E^-`.  Composition gives one returned edge. ∎

Thus return payment may be recorded on the physical edge actually vacated by
the reset while retaining the entering edge which supports the recreated
credit.

## 5. Exact classwise return identity

Let

\[
\beta:C\to\mathcal B
\]

be any finite credit-class map.  It may record residual rank, owner layer,
primitive-height band, prefix/carry data, root/fixed-interface type, selector
state, or any combination.

For `f in E^-` and `b in mathcal B`, define

\[
K_{f,b}(M,M')
=
\left|
\left\{
C:
C\text{ is recreated},
\ \beta(C)=b,
\ r(C)=f
\right\}
\right|.
\]

Let `N_b(M,M')` be the total number of recreated class-`b` credits.

### Theorem CMR1578 -- PROVED

For every class `b`,

\[
\boxed{
N_b(M,M')
=
\sum_{f\in E^-}K_{f,b}(M,M').
}
\]

Equivalently, writing `a=pi_src(f)`,

\[
K_{f,b}(M,M')
=
\left|
\left\{
C:
\beta(C)=b,
\ o(C)=a
\right\}
\right|.
\]

### Proof

CMR1577 partitions the recreated credits by their unique returned-edge charge.
Restrict the partition to class `b` and count.  The equivalent formula is the
definition of `r(C)` through the source pairing. ∎

This is an exact identity, not a union bound.

## 6. Local entering-owner bounds dominate the kernel

For an entering edge `a` and class `b`, let

\[
\Delta_b(a;M,M')
\]

be any upper bound on the number of recreated class-`b` credits whose canonical
owner is `a`.  The exact owner count itself is allowed.

### Theorem CMR1579 -- PROVED

For every returned edge `f` and class `b`,

\[
\boxed{
K_{f,b}(M,M')
\le
\Delta_b(\pi_{\rm src}(f);M,M').
}
\]

Consequently

\[
\boxed{
N_b(M,M')
\le
\sum_{f\in E^-}
\Delta_b(\pi_{\rm src}(f);M,M').
}
\]

### Proof

CMR1578 identifies the exact kernel entry with the owner count at the paired
entering edge.  Apply the chosen owner upper bound and sum. ∎

The existing rook, owner-assignment, line-height, displacement, prefix and carry
bounds therefore apply directly to the return kernel after replacing the
entering owner by its paired returned edge label.

## 7. Honest coarse return upper quotient

Let

\[
\rho(f,\pi_{\rm src}(f),M,M')\in\mathcal R
\]

be any finite returned-exchange signature.  Useful coordinates include:

1. returned-edge and entering-owner geometric classes;
2. alternating-cycle length;
3. owner layer and last-entering order position;
4. residual rank and line-height band;
5. token, prefix, quotient and carry labels;
6. current envelope, root/fixed-interface and thin-factor type.

For a signature `r in mathcal R` and credit class `b`, define the host-uniform
kernel maximum

\[
\boxed{
\widehat K_{r,b}
=
\max
K_{f,b}(M,M')
}
\]

where the maximum ranges over all exact transition entries with signature `r`
in the finite host family under consideration.

### Theorem CMR1580 -- PROVED

If `c_r(M,M')` is the number of returned edges of exchange signature `r`, then

\[
\boxed{
N_b(M,M')
\le
\sum_{r\in\mathcal R}
 c_r(M,M')\widehat K_{r,b}.
}
\]

The matrix `widehat K` is a finite nonnegative integer upper quotient.  For a
rational response law, averaging its exact transition kernels gives a finite
rational return row, and clearing row denominators gives the CMR1332 strict
integer-certificate format.

### Proof

Group the exact identity of CMR1578 by exchange signature and dominate each
entry by its fibre maximum.  Finiteness follows from the finite host, state,
credit and class sets.  Rational averaging and denominator clearing are
standard. ∎

Unlike a bound depending only on `|E^-|`, this quotient retains which entering
owner and which geometric class each returned edge pays for.

## 8. Return-selector coupling endpoint

Use a coarse class map which includes the repeated-return class `R` and one
subunit selector class `S`.  Let

\[
\alpha
\]

be the return-kernel row sum into `R`, and let

\[
\beta
\]

be its row sum into `S`.  Let the selector-to-return cap from CMR1564 be `T`.

### Corollary CMR1581 -- PROVED

The exact recurrent return-selector block is dominated by

\[
\boxed{
\begin{pmatrix}
\alpha&\beta\\
T&0
\end{pmatrix},
}
\]

where `alpha` and `beta` are finite rational sums of the exchange-pair kernel.
It is subcritical exactly when

\[
\boxed{\alpha+\beta T<1.}
\]

Thus the return frontier has been reduced from an undefined churn coefficient
to a finite exchange-signature computation followed by one strict rational or
integer inequality.

### Proof

CMR1580 constructs the return row.  CMR1561 gives the selector row `(T,0)`, and
CMR1562 gives the exact spectral criterion. ∎

The remaining mathematical task is to bound or enumerate the exchange kernel
uniformly in the inherited geometric classes and to prove the displayed
inequality.  No all-`n` theorem is claimed.

Source/target exchange bijections, alternating-cycle labels, exact credit
transport and coarse kernel identities are checked in
[`scripts/verify_prime_power_return_exchange_kernel.py`](../scripts/verify_prime_power_return_exchange_kernel.py).
