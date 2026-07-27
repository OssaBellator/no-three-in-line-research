# Fixed-interface atoms and thin bases form an exact finite table

CMR1606--CMR1613 reduce the prime-field root branch to reused support, return,
or one exact fixed-interface atom.  CMR1498--CMR1500 show that every such atom
has local prescription rank at most two.  The remaining fixed-interface label is
therefore finite and its response probability is an exact rook ratio.

For any chosen thin-side cap `H`, all residual boards, rank-one/rank-two
fixed-interface prescriptions and rank-one/rank-two/rank-three offspring
prescriptions form a finite rational table.  The table may be cleared to strict
integer inequalities.  This does not prove the table subcritical, but removes an
undefined base row and supplies an exact enumeration target.

Fix response side `d>=1`.  A compatible rank-`r` prescription is a partial
matching of `r` source-target edges.

## 1. Exact prescription stocks in the complete board

Let

\[
R_r(d)=\binom dr^2r!
\]

be the number of rank-`r` partial matchings in `K_{d,d}`.

### Theorem CMR1614 -- PROVED

For every `0<=r<=d`,

\[
\boxed{R_r(d)=\binom dr^2r!.}
\]

In particular, the total number of positive rank-at-most-two prescriptions is

\[
\boxed{
R_{\le2}^+(d)
=d^2+2\binom d2^2.
}
\]

Every residual response host has at most these many compatible labels.

### Proof

Choose the `r` source vertices, choose the `r` target vertices, and choose one of
`r!` bijections between them.  For `r=1,2`, sum the resulting counts. ∎

This is an ambient stock; forbidden edges only reduce it.

## 2. First fixed-interface signatures are finite

Refine one fixed-interface atom by its exact compatible prescription `P` of rank
one or two, its partner type, local-rank pattern, owner layer and any retained
root/fixed-interface labels.  Let the total number of additional finite labels
per prescription be `J`.

### Theorem CMR1615 -- PROVED

Inside one exact owner epoch, the number of first fixed-interface signatures is
at most

\[
\boxed{J\left[d^2+2\binom d2^2\right].}
\]

After adjoining the set of already seen exact signatures to the refined policy
state, first visits are strict finite-state transitions.  Only repeated exact
signatures can remain in a diagonal fixed-interface class.

### Proof

CMR1614 bounds the prescription labels and the other retained coordinates have
at most `J` possibilities.  A monotone seen-signature set acquires each exact
label at most once. ∎

This is a temporal triangular refinement only.  Finite first visits are not by
themselves potential improvement.

## 3. Repetition fixes one exact prescription

Suppose `N` fixed-interface episodes occur in one owner epoch and there are at
most

\[
S=J R_{\le2}^+(d)
\]

exact signatures.

### Theorem CMR1616 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. **Finite signature ancestry**
   \[
   \boxed{N\le(\lambda-1)S.}
   \]
2. **Exact prescription recurrence:** one complete fixed-interface signature,
   including its rank-one or rank-two prescription, occurs at least `lambda`
   times.

### Proof

Pigeonhole over the finite signature stock. ∎

Historical target loads are not added; recurrence identifies repeated access to
one exact row.

## 4. Exact rook probability of a repeated atom

Let a response board be

\[
G=K_{d,d}\setminus F
\]

with at least one perfect matching.  For a compatible allowed prescription `P`
of rank `r<=2`, let `F/P` be the contracted forbidden board after deleting the
sources and targets of `P`.  Write

\[
N_d(F)=|\operatorname{PM}(G)|.
\]

### Theorem CMR1617 -- PROVED

For uniform `Q in PM(G)`,

\[
\boxed{
\Pr(P\subseteq Q)
=
\frac{N_{d-r}(F/P)}{N_d(F)}.
}
\]

Both numerator and denominator are integers, so every repeated fixed-interface
prescription has one exact rational response probability.

### Proof

Perfect matchings containing `P` are in bijection with perfect matchings of the
contracted residual board.  Divide by the total response count. ∎

The rook-polynomial evaluation of CMR1414--CMR1421 or CMR1526--CMR1533 computes
both counts without listing all response matchings.

## 5. Exact classwise offspring row

Let `mathcal B` be any finite offspring credit-class set.  For a fixed exact
interface signature `sigma` and response `Q`, let

\[
c_b(\sigma,Q)\in\mathbb Z_{\ge0}
\]

be the number of genuinely new class-`b` credits created by the selected
execution.  Use any rational response law `nu_sigma` on the executable perfect
matchings of its board.

### Theorem CMR1618 -- PROVED

The fixed-interface offspring row

\[
\boxed{
A_{\sigma b}
=
\mathbb E_{Q\sim\nu_\sigma}c_b(\sigma,Q)
}
\]

is a finite rational vector.  If the law is uniform, each entry has denominator
dividing `N_d(F)`.  Exact last-entering ownership and the response probability of
CMR1617 permit further refinement by owner, rank, height, prefix, carry, return
and selector labels without losing rationality.

### Proof

A finite rational average of nonnegative integers is rational.  Under the
uniform law the common denominator is the response count.  Exact class
refinement partitions each integer count. ∎

Thus the fixed-interface base is an explicit row table, not an unnamed
coefficient.

## 6. Exact finite thin-board stock

Let

\[
\mathfrak R(d)=
\sum_{r=0}^d\binom dr^2r!
\]

be the number of all partial matchings of `K_{d,d}`.

### Theorem CMR1619 -- PROVED

For one side `d`, the following ambient families are finite.

1. perfect opposite matchings: `d!` choices;
2. target edges: at most `d^2` choices;
3. deleted partial matchings: `mathfrak R(d)` choices;
4. positive rank-at-most-two fixed-interface prescriptions:
   `R_{<=2}^+(d)` choices;
5. positive rank-at-most-three offspring prescriptions:
   \[
   \boxed{
   R_{\le3}^+(d)
   =
   d^2+2\binom d2^2+6\binom d3^2.
   }
   \]

Hence a coarse ambient upper bound for normalized fixed-interface board rows is

\[
\boxed{
T_d
=
 d!\,d^2\,\mathfrak R(d)\,
 R_{\le2}^+(d)\,R_{\le3}^+(d).
}
\]

Actual allowed boards and geometric classes form a subset of this finite stock.

### Proof

Items one through four are direct counts, and rank three uses CMR1614 with
`r=3`.  Multiply the ambient choices. ∎

The upper bound intentionally ignores isomorphism reductions and compatibility;
both only shrink the table.

## 7. Thin-side certificate compiler

Fix a finite thin-side cap `H`.  Let `mathcal T_H` be the union of all exact
normalized row types with `1<=d<=H`, including chosen owner, line-height, root,
return, selector and local-line labels.

### Theorem CMR1620 -- PROVED

The set `mathcal T_H` is finite.  Every exact response row is rational and can be
computed by the following finite procedure.

1. enumerate opposite matchings, targets and allowed deletion traces;
2. discard boards without a perfect matching;
3. enumerate rank-one/rank-two fixed-interface prescriptions;
4. compute response counts and contracted counts by rook inclusion-exclusion;
5. enumerate genuinely new rank-one/rank-two/rank-three offspring classes with
   absolute last-entering ownership;
6. form exact rational row entries;
7. clear all row denominators and test the strict integer Lyapunov inequalities.

The existence of a positive rational certificate for this fixed finite table is
decidable by rational linear programming and equivalently by a finite strict
integer system after denominator clearing.

### Proof

CMR1619 gives a finite ambient row stock for each `d<=H`; their finite union is
finite.  CMR1617--CMR1618 give exact rational entries.  CMR1270--CMR1277 give
rational/integer certificate equivalence for a finite nonnegative matrix. ∎

This is a compiler specification, not a claim that the resulting inequalities
always pass.

## 8. Fixed-interface and thin endpoint

### Corollary CMR1621 -- PROVED

The root/fixed-interface and thin base frontier now has the following exact
form.

1. Prime-field root translation reduces to one fixed-interface prescription of
   rank at most two, reused support, or return.
2. The complete rank-at-most-two prescription stock is polynomial in `d`.
3. First exact interface signatures are finite-state transitions.
4. Recurrent interface states fix one exact prescription with an exact rook
   probability.
5. Every classwise offspring row is rational and independently checkable.
6. For every fixed thin cap `H`, the complete base table is finite and admits an
   exact integer-certificate search.

The remaining work is numerical: execute this table for the required thin
regimes, prove the surviving rows subcritical, and glue them to the return,
selector and line-clean certificates.  No all-`n` theorem is claimed.

Prescription stocks, first/repeated signatures, exact contracted matching
probabilities, thin-board counts and rational row arithmetic are checked in
[`scripts/verify_prime_power_fixed_interface_thin_table.py`](../scripts/verify_prime_power_fixed_interface_thin_table.py).
