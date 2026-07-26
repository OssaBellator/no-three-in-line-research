# Exact-displacement mass splits cleanly from loaded-owner execution

CMR1492 reduces the spectral problem to recurrent cores.  Two currencies remain
inside those cores:

1. a global exact-displacement packing dispersed over owners; and
2. a one-owner loaded-line response.

They must not be counted twice.  A fixed exact displacement makes this
separation especially simple: one owner determines one partner.  The packing
constraint therefore puts at most one unit of exact-displacement mass on one
owner.

Consequently any set of owners reserved for loaded-line execution removes at
most one unit of packed mass per owner.  The complement remains a translation
forest and retains the private-path, token and root-channel payments already
proved.  This chapter closes the combinatorial overlap problem.  It does not
supply the still-missing numerical comparison between either currency and the
destroyed parent credit.

Retain one feasible fractional candidate packing `z_T` and one exact-
displacement incidence class with fixed partner type and displacement

\[
b=a+\Delta.
\]

Let

\[
\mu_\Delta=\sum_T z_Tm_\Delta(T),
\]

where `m_Delta(T)` is one when `T` contributes the distinguished
owner-partner incidence and zero otherwise.

## 1. One exact displacement gives one pair per owner

For an owner `a`, put

\[
m_\Delta(a)=
\sum_{T:a(T)=a}z_Tm_\Delta(T).
\]

### Theorem CMR1502 -- PROVED

For every owner,

\[
\boxed{m_\Delta(a)\le1.}
\]

Moreover, all positive mass owned by `a` lies on the single ordered pair

\[
\boxed{(a,a+\Delta).}
\]

Hence an exact-displacement class of mass `mu_Delta` uses at least

\[
\boxed{\lceil\mu_\Delta\rceil}
\]

distinct canonical owners as well as that many distinct ordered pairs.

### Proof

The displacement fixes the partner once the owner is fixed.  Every candidate
owned by `a` contains the residual owner edge `a`, so the fractional packing
constraint on `a` gives

\[
\sum_{T:a(T)=a}z_T\le1.
\]

The exact-displacement subfamily has no larger mass.  Summing the unit owner
bounds proves the support count. ∎

This strengthens the general CMR1465 bound `mu/2` on owner support for a
signature before exact displacement is fixed.

## 2. Exact exclusion of loaded owners

Let `L` be any set of owners assigned to a loaded-line or other one-owner
execution.  Define

\[
\mu_L=\sum_{a\in L}m_\Delta(a),
\qquad
\mu_{\bar L}=\mu_\Delta-\mu_L.
\]

### Theorem CMR1503 -- PROVED

\[
\boxed{\mu_L\le|L|}
\]

and

\[
\boxed{\mu_{\bar L}\ge\mu_\Delta-|L|.}
\]

Consequently

\[
\boxed{
\max\{|L|,\mu_{\bar L}\}\ge\frac{\mu_\Delta}{2}.
}
\]

### Proof

Sum CMR1502 over `L`, then use

\[
\mu_\Delta=\mu_L+\mu_{\bar L}
\le |L|+\mu_{\bar L}.
\]

∎

Thus either the loaded-line ledger already contains many distinct owners or a
comparable packed mass remains completely outside those owners.

## 3. Private pairs survive owner exclusion

Remove every pair whose owner lies in `L`.  The remaining pair family still
has displacement `Delta` and total mass `mu_bar L`.

### Theorem CMR1504 -- PROVED

The unloaded pair family contains an endpoint-disjoint subfamily of mass at
least

\[
\boxed{\frac{\mu_{\bar L}}2}
\]

and cardinality at least

\[
\boxed{\left\lceil\frac{\mu_{\bar L}}2\right\rceil.}
\]

Therefore at least one of the following holds:

1. \[
   \boxed{|L|\ge\mu_\Delta/2;}
   \]
2. there is an endpoint-disjoint translated family, using no owner of `L`, of
   mass at least
   \[
   \boxed{\mu_\Delta/4.}
   \]

Every residual blocker meeting all supports in branch 2 spends at least the
number of displayed private pairs.

### Proof

Deleting arcs from a translation path forest leaves a path forest.  Apply the
alternating parity extraction CMR1479 to the unloaded mass.  Combine with
CMR1503 and use CMR1480 for the blocker payment. ∎

The loaded-line and private-reserve currencies are now literally
owner-disjoint.

## 4. Nonroot token alternatives remain disjoint from loaded owners

Assume first-separation depth `s>=1`.  Apply the full-prefix token partition to
the private family from CMR1504.

### Theorem CMR1505 -- PROVED

In branch 2 of CMR1504, for every integer threshold `H>=2`, the unloaded
private family yields either:

1. one full-prefix token containing at least `H` endpoint-disjoint
   identical-displacement pairs whose owners avoid `L`; or
2. at least
   \[
   \boxed{
   \left\lceil
   \frac{\lceil\mu_{\bar L}/2\rceil}{H-1}
   \right\rceil
   }
   \]
   pairwise token-disjoint private witnesses whose owners avoid `L`.

Every blocker meeting the selected witnesses has at least the number of
witnesses, and none of that payment is assigned to a loaded owner.

### Proof

Apply CMR1482 to the unloaded private matching supplied by CMR1504. ∎

The fresh-versus-repeated token dichotomy of CMR1489--CMR1490 may then be
applied without sharing an owner with the loaded-line branch.

## 5. Root channels avoid the parity loss

Assume the exact displacement has depth zero.  Partition the unloaded pairs
by source residue modulo `p`.

### Theorem CMR1506 -- PROVED

At least one of the following holds.

1. \[
   \boxed{|L|\ge\mu_\Delta/2;}
   \]
2. some root source channel, using no owner of `L`, has mass at least
   \[
   \boxed{
   \frac{\mu_\Delta}{2p^2}
   }
   \]
   on automatically endpoint-disjoint pairs.

In branch 2 the channel contains at least

\[
\boxed{
\left\lceil\frac{\mu_\Delta}{2p^2}\right\rceil
}
\]

distinct private pairs and has the deterministic quotient carry and
cross-child normalization of CMR1494--CMR1501.

### Proof

If branch 1 fails, CMR1503 gives unloaded mass greater than
`mu_Delta/2`.  Pigeonhole that mass over at most `p^2` source residues.  CMR1495
gives endpoint-disjointness and CMR1494 gives the quotient channel. ∎

Unlike CMR1504, the root-channel branch loses no additional parity factor.

## 6. Additive bookkeeping without double counting

Let `P_load(a)` be any certified nonnegative payment assigned by a loaded-line
policy to an owner `a in L`.  Let `P_priv(a,b)` be any certified nonnegative
payment assigned to an unloaded private pair.

### Theorem CMR1507 -- PROVED

The combined payment

\[
\boxed{
\sum_{a\in L}P_{\rm load}(a)
+
\sum_{\substack{(a,b)\text{ selected private}\\a\notin L}}
P_{\rm priv}(a,b)
}
\]

has disjoint canonical owner support.  No candidate incidence in the exact-
displacement class contributes to both sums.

The same statement holds after nonroot token selection or depth-zero root-
channel selection.

### Proof

The first sum uses owners in `L`; the second uses owners outside `L`.
CMR1502 assigns every exact-displacement incidence to one canonical owner.
Token and root-channel refinements only partition the unloaded family. ∎

This theorem is bookkeeping, not a numerical lower bound on either payment.

## 7. Quantitative splice after carry routing

Let a CMR1475 routed branch have mass `m`, and let `L` be the owner set chosen
for loaded-line execution at that stage.

### Theorem CMR1508 -- PROVED

For the strict internal branch, at least one holds:

\[
\boxed{
|L|\ge\frac{M_0}{4p^{2s}}
}
\]

or there is an unloaded private translated family of mass at least

\[
\boxed{
\frac{M_0}{8p^{2s}}.
}
\]

For the earlier-exit branch, when `s>=1`, at least one holds:

\[
\boxed{
|L|\ge\frac{M_0}{4sp^{2s}}
}
\]

or there is an unloaded private translated family of mass at least

\[
\boxed{
\frac{M_0}{8sp^{2s}}.
}
\]

For the depth-zero branch, at least one holds:

\[
\boxed{|L|\ge\frac{M_0}{2}}
\]

or there is an unloaded root channel of mass at least

\[
\boxed{
\frac{M_0}{2p^2}.
}
\]

All private/token/root-channel payments in the second alternatives are
owner-disjoint from the loaded-line payment.

### Proof

The internal and earlier-exit branch masses are at least
`M_0/(2p^(2s))` and `M_0/(2sp^(2s))`.  Apply CMR1503--CMR1504.  The depth-zero
branch has mass at least `M_0`; apply CMR1506. ∎

## 8. Packed-versus-loaded endpoint

### Corollary CMR1509 -- PROVED

The overlap part of the packed-versus-loaded frontier is closed.

For every exact-displacement obstruction and every chosen loaded-owner set,
one has an exact alternative:

1. many distinct owners are assigned to the loaded-line ledger; or
2. a quantitatively large translated private family remains on other owners,
   retaining its blocker, token, carry-routing and root-child payments.

The two payments have disjoint canonical owner support and therefore may be
added in a future same-owner Lyapunov inequality without inclusion-exclusion
loss.

What remains open is genuinely numerical:

- assign a destroyed-credit value to one loaded owner and to one private
  residual/token payment;
- prove the recurrent root-channel, repeated-token/reused-edge and
  fixed-interface core inequalities;
- assemble those values into a host-uniform rational or integer certificate.

No all-`n` theorem is claimed.

Owner-unit bounds, loaded-owner exclusion, unloaded private extraction,
root-channel concentration and disjoint bookkeeping are checked in
[`scripts/verify_prime_power_owner_disjoint_packed_loaded.py`](../scripts/verify_prime_power_owner_disjoint_packed_loaded.py).
