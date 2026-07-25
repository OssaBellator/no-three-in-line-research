# Refined rooted-trace ancestry fixes one paid pair and one line-clean selector

CMR540 leaves one deliberately unpaid branch: recurrence of a trace cell in one
row or column arm of a persistent blocker.  The trace cell need not be
unavailable, so unavailable-edge inventory cannot be charged directly.

A rooted trace episode contains more canonical data than CMR540 records.  It
comes from one boundary-rooted secant-star arm, one chosen outside endpoint,
and therefore one fixed compatible paid pair.  Adding the rooted center and
paid partner to the ancestry signature fixes the paid line and the universal
line-clean cylinder geometry.  Repetition then becomes a CMR531 weighted
selector problem with paid-edge surcharge at most two, regardless of whether
the trace cell is available.

## 1. Refined rooted-trace signatures

Work in one envelope epoch of side `m`.  A rooted trace episode has:

- a rooted secant-star center `a`;
- a chosen paid partner `z`, so
  \[
  Z=\{a,z\}
  \]
  is the CMR494 compatible paid pair;
- the nonaxis paid line
  \[
  L=L(a,z);
  \]
- a persistent blocker
  \[
  e=(u,v);
  \]
- a trace cell `w\in Q_L` in row `u` or column `v`, with `w\ne e`;
- an arm label
  \[
  \varepsilon\in\{\mathrm{row},\mathrm{column}\}.
  \]

Define the **refined rooted-trace signature**

\[
\widehat\Sigma_{\mathrm{tr}}
=
(E,a,z,e,w,\varepsilon),
\]

where `E` is the envelope-epoch label.

### Theorem CMR541 — PROVED

A refined rooted-trace signature determines:

1. the fixed compatible paid pair
   \[
   \boxed{Z=\{a,z\}};
   \]
2. the fixed nonaxis paid line
   \[
   \boxed{L=L(a,z)=L(a,w)};
   \]
3. the persistent central incidence slot `(e,w,\varepsilon)`;
4. the universal CMR492 line-clean cylinder geometry associated with `Z` and
   `L`.

### Proof

The paid pair and its joining line are part of the signature.  The trace cell
lies in the paid-line trace `Q_L`, so `a,z,w` are collinear.  Compatibility and
nonaxiality are CMR494.  CMR492 depends only on the compatible paid pair, its
line, and a choice of residual forbidden-matching extension; thus the
full-parent cylinder geometry is fixed by `Z,L`. ∎

The current restricted host and the adaptive forbidden-matching extension may
still vary.  The paid pair and the line being cleaned do not.

## 2. Finite refined-signature stock

### Theorem CMR542 — PROVED

Inside one envelope epoch of side `m`, the number of possible refined
rooted-trace signatures is at most

\[
\boxed{
\widehat N_{\mathrm{tr}}(m)
\le
2m^4(m-1)^2.
}
\]

Across a closure-envelope chain in a root parent of side `t=p^h`,

\[
\boxed{
\widehat{\mathcal N}_{\mathrm{tr}}
\le
2(h+1)t^4(t-1)^2.
}
\]

### Proof

Choose the rooted center `a` in `m^2` ways and the persistent central cell `e`
in `m^2` ways.  Choose one of two arm labels and one of at most `m-1`
noncentral trace cells in that arm.

Once `a` and `w` are fixed, their nonaxis line is fixed.  Such a line meets
each source row and target column at most once, so it contains at most `m`
parent-block cells.  Excluding `a` leaves at most `m-1` possibilities for the
paid partner `z`.  Multiplying gives the one-epoch bound.

There are at most `h+1` epochs by CMR535, and every epoch side is at most
`t`. ∎

The bound deliberately ignores collinearity, compatibility, and residual-trace
restrictions which can only reduce the stock.

## 3. Finite rooted-trace ancestry or exact recurrence

### Theorem CMR543 — PROVED

Fix an integer `\lambda\ge2`.  For `J_{\mathrm{rtr}}` rooted trace episodes
along one closure branch, at least one of the following holds.

1. **Finite refined trace ancestry.**
   \[
   \boxed{
   J_{\mathrm{rtr}}
   \le
   2(\lambda-1)(h+1)t^4(t-1)^2.
   }
   \]
2. **Exact refined-signature recurrence.**  One fixed signature
   \[
   \widehat\Sigma_{\mathrm{tr}}
   =
   (E,a,z,e,w,\varepsilon)
   \]
   occurs in at least `\lambda` episodes.

### Proof

If no refined signature occurs `\lambda` times, every signature multiplicity
is at most `\lambda-1`.  Multiply by the global stock from CMR542. ∎

Thus the CMR540 trace-recurrence branch can be refined without any availability
assumption on `w`.

## 4. Recurrent refined trace signatures are fixed selectors

Suppose one refined signature recurs.  At any selected occurrence, let

\[
c_Z=|Z\setminus E(G)|
\in\{0,1,2\}
\]

be the current paid-pair restoration surcharge.  After deleting the paid-pair
endpoints, let `B_L` be the unavailable allowed residual edge set and let
`A_L` be the CMR333 collateral expectation bound.

### Theorem CMR544 — PROVED

At every occurrence of the recurrent refined signature and for every integer
`q\ge1`, one line-clean completion satisfies

\[
\boxed{
X_L(\delta)+\frac{T_Z(\delta)}q
\le
A_L+\frac{c_Z}{q}+\frac{|B_L|}{q(n-1)}.
}
\]

Consequently, at least one of the following holds.

1. **Cheap clean execution.**
   \[
   \boxed{
   X_L(\delta)=0,
   \qquad
   T_Z(\delta)<q.
   }
   \]
2. **Fixed-line weighted obstruction.**
   \[
   \boxed{
   A_L+\frac2q+\frac{|B_L|}{q(n-1)}
   \ge1.
   }
   \]

The second branch returns the same frozen-collateral or unavailable-inventory
alternatives as CMR504--CMR516.

### Proof

Apply CMR531 to the fixed pair `Z` and line `L`.  Since `c_Z\le2`, failure of
the cheap-clean conclusion implies

\[
A_L+\frac{c_Z}{q}+\frac{|B_L|}{q(n-1)}\ge1,
\]

which implies the displayed weaker obstruction with `2/q`.  Apply
CMR504--CMR516 to that obstruction. ∎

No property of the trace-cell availability is used.

## 5. Unified persistent-cross ancestry endpoint

### Corollary CMR545 — PROVED

Fix `\lambda\ge2` along one closure branch in a root parent of side `t=p^h`.
Persistent-cross ancestry reaches at least one of the following endpoints.

1. **Finite pair ancestry.**
   \[
   J_{\mathrm{pair}}
   \le
   (\lambda-1)(h+1)t^2(t-1)^2.
   \]
2. **Pair reintroduction or fixed selector.**  One pair signature recurs and
   reaches CMR539.
3. **Finite rooted-trace ancestry.**
   \[
   J_{\mathrm{rtr}}
   \le
   2(\lambda-1)(h+1)t^4(t-1)^2.
   \]
4. **Fixed rooted-trace selector.**  One refined rooted-trace signature recurs
   and reaches CMR544.

Thus every recurrent persistent-cross branch is reduced to reintroduction
payment or a fixed compatible paid pair and fixed paid line governed by the
same weighted selector.

### Proof

Use CMR537--CMR539 for pair episodes and CMR543--CMR544 for rooted trace
episodes. ∎

## 6. Revised frontier

The trace-cell provenance gap left after CMR540 is closed.

- Trace cells are still not declared unavailable.
- Refining the ancestry label fixes the rooted center, paid partner, paid pair,
  paid line, central blocker, trace cell, arm, and envelope epoch.
- Nonrecurrent rooted-trace ancestry has polynomial stock.
- Recurrent rooted-trace ancestry becomes a fixed CMR531 selector with surcharge
  at most two.

The remaining prime-power frontier is now one common endpoint: repeated failure
of a fixed compatible-pair line-clean selector.  By CMR544, every failure
already returns frozen rank-zero/rank-one collateral or unavailable-edge
inventory.  What remains is to convert repeated occurrences of those returned
obstructions into protected-reserve depletion, full-token return,
quotient/carry concentration, deletion ancestry, or strict envelope expansion,
without double counting between selector signatures.

No all-`n` theorem is claimed.  Refined signature determinacy, stock bounds,
multiplicity arithmetic, and surcharge inequalities are checked in
[`scripts/verify_prime_power_refined_trace_ancestry.py`](../scripts/verify_prime_power_refined_trace_ancestry.py).
