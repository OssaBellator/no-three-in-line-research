# The strict factor-descent path has finite owner, edge, token, and certificate stock

CMR664--CMR690 close the local structure at one child-product owner.  This
chapter aggregates those local bounds over one complete strict factor-descent
path.  Unless one physical routing edge recurs, the number of routing epochs at
every host stage is polynomial.  Consequently all owner-labelled edge, token,
and forced-certificate stocks on the path are explicit and finite.

Fix a selected descent path beginning with factor side `d` inside a parent of
side

\[
t=p^h.
\]

At each strict child continuation the positive factor side decreases.  Host
changes are monotone matching-preserving deletions and complete-essential-core
contractions.  Routing changes are transitions between vertex-routing skeletons
of a fixed host stage.

Fix an integer recurrence threshold

\[
\lambda\ge2.
\]

The statements below are conditional only on taking the nonrecurrent branch of
CMR674 at each owner stage.  If that condition fails, the recurrent physical
routing edge is already an endpoint.

## 1. Static host stages at one side

### Theorem CMR691 — PROVED

At factor side `m`, the total number of static normalised host stages used by the
combined pure-factor and mixed-child deletion recursions is at most

\[
\boxed{
H_m=2m^2+m+1.
}
\]

### Proof

CMR653 gives at most `m^2+m+1` complete-core contraction and anchored-deletion
stages.  CMR680 contributes at most `m^2` mixed-atom deletions.  Adding the two
bounds gives `H_m`.  Both operations delete edges or contract vertices, so a
physical host stage is not recreated inside the monotone execution. ∎

## 2. Routing epochs at one host stage

### Theorem CMR692 — PROVED

Assume no physical factor edge occurs in `\lambda` entering routing-support sets
at one fixed host stage of side `m`.  Then the number of routing-changing
transitions is at most

\[
\boxed{
R_m(\lambda)
=
\left\lfloor
\frac{(\lambda-1)m^2}{2}
\right\rfloor,
}
\]

and the number of routing epochs at that stage is at most

\[
\boxed{1+R_m(\lambda).}
\]

### Proof

The transition bound is CMR674 with `|E(H)|\le m^2`.  A sequence with `R`
changes has at most `R+1` maximal constant-routing intervals. ∎

## 3. Total owner-routing stage stock

Define

\[
\mathcal O(d,\lambda)
=
\sum_{m=1}^{d}
H_m\bigl(1+R_m(\lambda)\bigr).
\]

### Theorem CMR693 — PROVED

Along one selected strict descent path, either one physical routing edge reaches
the recurrent branch of CMR674 or the total number of owner-labelled
host-and-routing stages is at most

\[
\boxed{
\mathcal O(d,\lambda)
=
\sum_{m=1}^{d}
(2m^2+m+1)
\left(
1+\left\lfloor\frac{(\lambda-1)m^2}{2}\right\rfloor
\right).
}
\]

In particular,

\[
\boxed{
\mathcal O(d,\lambda)
\le
\sum_{m=1}^{d}
(2m^2+m+1)
\left(1+\frac{(\lambda-1)m^2}{2}\right),
}
\]

which is polynomial of degree five in `d` for fixed `\lambda`.

### Proof

At side `m`, CMR691 gives at most `H_m` monotone host stages.  Apply CMR692 to
each host stage.  Strict child recursion visits each positive side at most once,
so sum over `m=1,...,d`. ∎

The owner label includes the factor envelope, current host, contracted core, and
routing skeleton.

## 4. Owner-labelled physical edge and token stock

Define

\[
\mathcal E(d,\lambda)
=
\sum_{m=1}^{d}
H_m\bigl(1+R_m(\lambda)\bigr)m^2.
\]

### Theorem CMR694 — PROVED

In the nonrecurrent-routing branch, the number of owner-labelled physical
factor-edge pairs `(owner,e)` on the complete descent path is at most

\[
\boxed{\mathcal E(d,\lambda).}
\]

Their total labelled nonroot full-token stock is at most

\[
\boxed{
(p+1)(h-1)\mathcal E(d,\lambda).
}
\]

For any family of `J` episodes carrying at least `Q\ge1` owner-edge witnesses
each and any integer `\mu\ge2`, at least one of the following holds.

1. One exact owner-edge pair occurs in at least `\mu` episode witness sets.
2. \[
   \boxed{
   J
   \le
   \frac{(\mu-1)\mathcal E(d,\lambda)}{Q}.
   }
   \]

### Proof

A side-`m` host has at most `m^2` physical edges.  Multiply by the owner-routing
stage bound and sum.  CMR413 gives exactly `(p+1)(h-1)` nonroot token labels per
physical parent edge.

For the recurrence statement, double-count incidences between episodes and the
finite owner-edge stock.  If no owner-edge occurs `\mu` times, total incidence
is at most `(\mu-1)\mathcal E`; it is at least `JQ`. ∎

A recurrent owner edge enters the absence-run, reintroduction, routing-support,
and selected-conflict recreation ledgers already proved earlier.

## 5. Owner-labelled forced-certificate stock

Define

\[
\mathcal C(d,\lambda)
=
\sum_{m=1}^{d}
H_m\bigl(1+R_m(\lambda)\bigr)
\binom{m^2}{3}.
\]

### Theorem CMR695 — PROVED

In the nonrecurrent-routing branch, the total owner-labelled forced-child
certificate stock on the complete descent path is at most

\[
\boxed{\mathcal C(d,\lambda).}
\]

For every integer `\nu\ge2`, a history of `K` forced-certificate episodes
therefore reaches one of:

1. one exact owner-labelled certificate in at least `\nu` episodes;
2. \[
   \boxed{
   K\le(\nu-1)\mathcal C(d,\lambda).
   }
   \]

### Proof

At a side-`m` owner stage, CMR685 gives at most `binom(m^2,3)` physical triples.
Multiply by the owner-routing stage stock and sum.  The recurrence bound is the
pigeonhole principle. ∎

This refines the coarser stage-independent stock in CMR686 by including routing
epoch ownership explicitly.

## 6. Canonical path-length alternative

### Theorem CMR696 — PROVED

Consider a canonical execution which always performs an available
matching-preserving mixed deletion, anchored deletion, or complete-core
contraction before descending to a strict child.  Fix thresholds
`\lambda,\mu,\nu\ge2`.

Before the finite owner stocks `\mathcal O`, `\mathcal E`, and `\mathcal C` are
exhausted, at least one of the following occurs.

1. A globally candidate-conflict-free product state is found.
2. The execution descends to a strict child factor, reducing envelope side and
   factor side.
3. One physical routing edge recurs `\lambda` times at one owner stage.
4. One exact owner-edge witness recurs `\mu` times.
5. One exact owner-labelled forced certificate recurs `\nu` times.
6. A forced certificate escapes through deletion, routing churn, or a genuinely
   entering factor edge.

### Proof

CMR681--CMR683 give the clean/strict-child/forced-certificate alternatives at a
fixed routing stage.  CMR674 and CMR693 handle routing changes.  CMR694 handles
edge-witness episodes, and CMR695 handles certificate episodes.  Escape from a
fixed certificate is CMR688--CMR689. ∎

The theorem is a finite structural scheduler; it does not yet assert that one
of the paid recurrence endpoints lowers the global target-load potential.

## 7. Descending-path normal form

### Corollary CMR697 — PROVED

Every prime-power factor execution has the following owner-labelled normal form.

- Static host operations consume finite deletion/contraction stock.
- Routing changes consume finite entering/leaving edge stock unless one edge
  recurs.
- Fixed routing products become clean, descend strictly, or expose a forced
  certificate.
- Forced certificates consume finite signature stock unless one recurs; escape
  pays deletion, routing churn, or entering-edge support.
- Strict child continuation lowers envelope side by at least a factor of `p`
  and lowers positive factor side.

Thus every unbounded continuation is reduced to recurrence of one exact
owner-edge or one exact forced certificate, with all other structural movement
bounded by the displayed polynomial stocks.

### Proof

Combine CMR691--CMR696 with the strict descent of CMR683. ∎

The remaining prime-power theorem is a **potential conversion theorem** for the
last recurrent owner-edge or forced-certificate endpoints: prove inherited
target-load descent, protected-reserve depletion, permanent deletion ancestry,
full-token return, or closure-envelope expansion.

No all-`n` theorem is claimed.  The polynomial owner-stage, edge, token, and
certificate formulas and their recurrence bounds are checked in
[`scripts/verify_prime_power_descending_path_stock.py`](../scripts/verify_prime_power_descending_path_stock.py).
