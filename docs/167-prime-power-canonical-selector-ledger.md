# Canonical fixed-selector cylinders separate static collateral from dynamic unavailability

CMR546--CMR551 show that repeated failure of one fixed line-clean selector has
finite obstruction stock unless an exact unavailable edge or conflict atom
recurs.  A further normalization removes even the changing-collision-profile
ambiguity.

The residual paid-line trace is fixed once the envelope epoch, compatible paid
pair, and paid line are fixed.  Extend that trace by one deterministic
order-preserving matching of the unused residual vertices.  This gives a
canonical forbidden perfect matching, hence one time-independent derangement
cylinder and one time-independent rank-zero/rank-one collateral profile.
Only current availability changes.

Consequently every canonical selector signature is of exactly one type.

- Its fixed collateral profile is already large.  This static obstruction is
  charged once to the signature, not once per temporal occurrence.
- Its fixed collateral profile is below threshold.  Then every failed
  occurrence contains a positive number of unavailable edges from one fixed
  residual universe, so finite stock or exact edge recurrence applies.

This is the desired no-double-counting ledger between selector signatures.

## 1. Canonical forbidden matching

Fix one envelope epoch of side `m`, one compatible paid pair

\[
Z=\{z_1,z_2\},
\]

and its nonaxis paid line `L`.  Delete the paid-pair endpoints and put

\[
n=m-2.
\]

Let `Q_L` be the residual partial matching consisting of all remaining parent
cells on `L`.  Order the residual source and target vertices by their inherited
grid coordinates.

### Theorem CMR552 — PROVED

There is a canonical perfect matching

\[
\boxed{F_\Sigma}
\]

of the residual `K_{n,n}` extending `Q_L`: keep every edge of `Q_L`, list the
unused source vertices and unused target vertices in increasing order, and
match the two lists position by position.

The associated canonical line-clean cylinder

\[
\mathcal D_\Sigma
=
\{\delta\in\operatorname{PM}(K_{n,n}):\delta\cap F_\Sigma=\varnothing\}
\]

has exact size

\[
\boxed{|\mathcal D_\Sigma|=D_n}
\]

and depends only on the selector signature

\[
\Sigma=(E,Z,L),
\]

not on the current restricted host.

Every state in the cylinder contains the paid pair and avoids every other
parent cell of `L`.

### Proof

`Q_L` is a partial matching because `L` is nonaxis.  Its unused source and
target sets have equal cardinality, so the displayed order-preserving pairing
extends it to a perfect matching.

Relabel `F_\Sigma` as the identity.  Perfect matchings avoiding it are exactly
the `D_n` derangements.  Every residual cell of `L` lies in `Q_L` and is
therefore forbidden.  All choices use only `E,Z,L` and the fixed coordinate
orders. ∎

The canonical extension need not minimize restoration.  Its purpose is a
time-consistent accounting face.

## 2. Time-independent collateral profile

Let

\[
U_\Sigma=E(K_{n,n})\setminus F_\Sigma.
\]

Define fixed integers

\[
V_0(\Sigma),\qquad V_1(\Sigma)
\]

as the numbers of candidate-only collinear triples allowed by `U_\Sigma` which
respectively use zero or one paid-pair cells.  Put

\[
S_\Sigma
=
\frac{V_0(\Sigma)}{(n)_3}
+
\frac{V_1(\Sigma)}{(n)_2},
\qquad
A_\Sigma=\frac{30}{11}S_\Sigma.
\]

At temporal occurrence `j`, let

\[
B_{\Sigma,j}
=
U_\Sigma\setminus E(G_j)
\]

be the currently unavailable canonical allowed edges.

### Theorem CMR553 — PROVED

The values

\[
\boxed{
V_0(\Sigma),\ V_1(\Sigma),\ S_\Sigma,\ A_\Sigma
}
\]

are constant throughout the envelope epoch.

For every occurrence and every integer `q>=1`, some canonical-cylinder
completion satisfies

\[
\boxed{
X_\Sigma(\delta)
+
\frac{T_\Sigma(\delta)}q
\le
A_\Sigma
+
\frac{c_{Z,j}}q
+
\frac{|B_{\Sigma,j}|}{q(n-1)},
}
\]

where

\[
c_{Z,j}=|Z\setminus E(G_j)|\le2.
\]

Hence failure of a canonical cheap-clean execution implies

\[
\boxed{
A_\Sigma
+
\frac2q
+
\frac{|B_{\Sigma,j}|}{q(n-1)}
\ge1.
}
\]

### Proof

The paid pair, paid line, canonical forbidden matching, and allowed residual
host are fixed by `\Sigma`, so the conflict counts are fixed.

Under the uniform law on `\mathcal D_\Sigma`, every allowed residual edge has
marginal `1/(n-1)` by CMR502, and CMR333 bounds expected collateral by
`A_\Sigma`.  Add the deterministic paid-edge surcharge and average.  The
failure inequality follows from `c_{Z,j}\le2`. ∎

Thus all temporal variation has been moved into one physical unavailable-edge
set.

## 3. Static collateral or quantitative unavailable inventory

### Theorem CMR554 — PROVED

Fix

\[
q\ge4
\]

and define the canonical selector slack

\[
\Delta_\Sigma
=
1-\frac2q-A_\Sigma.
\]

Exactly one of the following two selector types occurs.

1. **Static collateral signature.**
   \[
   \boxed{\Delta_\Sigma\le0.}
   \]
   Equivalently,
   \[
   \boxed{
   S_\Sigma
   \ge
   \frac{11}{30}
   \left(1-\frac2q\right).
   }
   \]
2. **Dynamic availability signature.**
   \[
   \boxed{\Delta_\Sigma>0.}
   \]
   Every failed occurrence then satisfies
   \[
   \boxed{
   |B_{\Sigma,j}|
   \ge
   H_\Sigma
   :=
   \left\lceil
   q(n-1)\Delta_\Sigma
   \right\rceil
   \ge1.
   }
   \]

### Proof

The two signs of `\Delta_\Sigma` are exhaustive.

In the nonpositive case, substitute
`A_\Sigma=(30/11)S_\Sigma` and rearrange.

In the positive case, CMR553 gives

\[
\frac{|B_{\Sigma,j}|}{q(n-1)}
\ge
1-\frac2q-A_\Sigma
=
\Delta_\Sigma.
\]

Use integrality. ∎

Static collateral is now attached once to `\Sigma`; repeating the same selector
does not create a new collateral charge.

## 4. Dynamic selector histories

Suppose `\Sigma` is a dynamic availability signature and `J_\Sigma` failed
occurrences are selected.  For an edge `f\in U_\Sigma`, put

\[
\mu_\Sigma(f)
=
|\{j:f\in B_{\Sigma,j}\}|.
\]

### Theorem CMR555 — PROVED

For every integer `\lambda>=2`, at least one of the following holds.

1. **Labelled edge recurrence.**  Some fixed canonical allowed edge `f` is
   unavailable in at least `\lambda` failed occurrences of `\Sigma`.
2. **Finite dynamic history.**
   \[
   \boxed{
   J_\Sigma
   \le
   \frac{(\lambda-1)|U_\Sigma|}{H_\Sigma}
   \le
   \frac{(\lambda-1)n(n-1)}{H_\Sigma}.
   }
   \]

In the recurrence branch, CMR519 yields absent-to-present reintroduction
payment or one continuous-absence interval containing many occurrences.

### Proof

Every failed occurrence contains at least `H_\Sigma` edges of `B_{\Sigma,j}`.
Double counting gives

\[
J_\Sigma H_\Sigma
\le
\sum_f\mu_\Sigma(f).
\]

The canonical allowed universe has

\[
|U_\Sigma|=n^2-n=n(n-1)
\]

edges.  If no edge occurs `\lambda` times, every multiplicity is at most
`\lambda-1`.  Rearrange. ∎

Unlike CMR547, this uses the exact fixed allowed universe rather than the full
residual square.

## 5. Global selector-signature stock

CMR536 bounds epoch-labelled persistent pair signatures, and CMR542 bounds
refined rooted-trace signatures.  Each such ancestry signature determines a
compatible paid pair and paid line, hence one canonical selector signature.

### Theorem CMR556 — PROVED

Along one closure branch in a root parent of side

\[
t=p^h,
\]

the total number `N_\Sigma` of canonical selector signatures arising from
persistent pair or refined rooted-trace ancestry satisfies

\[
\boxed{
N_\Sigma
\le
(h+1)t^2(t-1)^2
+
2(h+1)t^4(t-1)^2.
}
\]

Consequently:

1. the number of static collateral profiles is at most `N_\Sigma`;
2. for dynamic signatures and every `\lambda>=2`, either one labelled pair
   `(\Sigma,f)` occurs in at least `\lambda` failed occurrences, or the total
   number `J_{\mathrm{dyn}}` of dynamic failed occurrences satisfies
   \[
   \boxed{
   J_{\mathrm{dyn}}
   \le
   (\lambda-1)t^2N_\Sigma.
   }
   \]

A sharper weighted form is

\[
\boxed{
\sum_{\Sigma\ \mathrm{dynamic}}
J_\Sigma H_\Sigma
\le
(\lambda-1)t^2N_\Sigma
}
\]

unless a labelled pair recurs `\lambda` times.

### Proof

Add the pair-signature stock from CMR536 and the refined rooted-trace stock
from CMR542.  Mapping ancestry signatures to selectors may identify several
labels, so their sum remains an upper bound.

Each selector has at most `t^2` residual physical edges.  If every labelled
pair `(\Sigma,f)` occurs at most `\lambda-1` times, double count all dynamic
failure-edge incidences:

\[
\sum_\Sigma J_\Sigma H_\Sigma
\le
(\lambda-1)t^2N_\Sigma.
\]

Since every `H_\Sigma>=1`, the unweighted bound follows. ∎

The selector label prevents one physical edge in two different paid-line
cylinders from being charged as the same state.

## 6. Canonical fixed-selector endpoint

### Corollary CMR557 — PROVED

Every persistent-cross selector history reaches at least one of the following
endpoints.

1. **Finite ancestry stock.**  Pair and rooted-trace ancestry obey the CMR545
   polynomial bounds.
2. **Static canonical collateral.**  One canonical signature satisfies
   \[
   S_\Sigma
   \ge
   \frac{11}{30}
   \left(1-\frac2q\right).
   \]
   Its complete rank-zero/rank-one conflict profile is fixed and is charged
   once to `\Sigma`.
3. **Finite dynamic availability history.**  The bounds of CMR555--CMR556
   hold.
4. **Reintroduction payment.**  One labelled canonical edge is repeatedly
   unavailable across distinct absence runs.
5. **Persistent canonical blocker.**  One fixed pair `(\Sigma,f)` remains
   unavailable throughout one interval containing many failures.

### Proof

Apply CMR545 to obtain finite ancestry or a fixed selector.  Canonicalize it by
CMR552.  Classify it by CMR554.  Apply CMR555 locally and CMR556 globally to
dynamic signatures, followed by CMR519 in the recurrence branch. ∎

## 7. Revised frontier

The double-counting problem between selector signatures is closed.

- Every selector has one fixed canonical cylinder.
- Every selector has one fixed collateral profile.
- A high collateral profile is charged once, regardless of temporal
  recurrence.
- A low collateral profile forces unavailable edges from one fixed universe.
- Dynamic histories have polynomial labelled stock unless one exact
  selector-edge pair recurs.

The immediate prime-power frontier has two canonical objects only:

1. a static fixed rank-zero/rank-one collateral profile attached to one paid
   pair and paid line;
2. a persistent unavailable edge inside one canonical cylinder.

The first should be converted by the existing modular-syndrome,
quotient/carry, mixed-fan, line-energy, and target-load machinery.  The second
returns to the persistent-blocker, reserve-depletion, deletion-ancestry, or
envelope-expansion machinery, now with a fixed selector label and no ambiguity
about which cylinder owns the charge.

No all-`n` theorem is claimed.  Canonical extension, fixed-profile identities,
slack arithmetic, exact allowed-edge counts, and global labelled-stock bounds
are checked in
[`scripts/verify_prime_power_canonical_selector_ledger.py`](../scripts/verify_prime_power_canonical_selector_ledger.py).
