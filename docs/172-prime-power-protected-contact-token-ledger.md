# Protected-core contact histories pay finite edge stock, a token wall, or one exact persistent contact

CMR571--CMR576 reduce dynamic canonical-selector failure to a finite absorption
chase.  Every irreducible recurrent edge is blocked by one protected partial
matching

\[
P=Q_L\cup R
\]

and therefore shares a source or target vertex with a protected edge.

This chapter gives the exact temporal ledger for those contacts.  At one
protected state of residual side `n` and protected size `k`, there are at most
`2k(n-1)` possible blocked edges.  Hence a long contact history either repeats
one exact edge or uses many distinct physical edges.  Distinct contacts
concentrate on one protected source or target vertex, producing the same row/
column star and full-prefix token alternatives as CMR512--CMR516.  Exact edge
incidence is paid once per physical contact edge; repeated use after a return
pays the reintroduction ledger.

Fix one protected selector state `P` of size

\[
k=|P|\ge1
\]

inside an inherited parent of side

\[
t=p^h.
\]

Its residual matching side is `n`.  A **contact episode** records one blocked
canonical allowed edge `f`, unavailable at that episode, together with one
CMR573 contact label

\[
(f,r,\varepsilon),
\qquad
r\in P,
\qquad
\varepsilon\in\{\mathrm{source},\mathrm{target}\}.
\]

## 1. Exact finite contact universe

### Theorem CMR582 — PROVED

The number of possible physical blocked edges at the protected state `P` is at
most

\[
\boxed{
N_{\mathrm{ct}}(P)
\le
2k(n-1).
}
\]

More precisely, every blocked edge belongs to the union of the `k` protected
source stars and the `k` protected target stars, after deleting each protected
matching edge itself.

### Proof

A blocked edge meets at least one protected vertex by CMR572--CMR573.  At one
protected source vertex there are at most `n-1` residual edges other than its
edge of `F_P`; the same holds for one protected target vertex.  Sum over the
`2k` vertices.  Edges meeting two protected vertices may be counted twice, so
the result is an upper bound. ∎

The contact label is finer than the physical edge, but one physical edge has at
most two labels, one for each protected endpoint it meets.

## 2. Recurrence or distinct contact stock

Suppose `J` contact episodes occur at the same protected state.  For a blocked
edge `f`, let `\mu(f)` be its episode multiplicity.

### Theorem CMR583 — PROVED

For every integer `\lambda>=2`, at least one of the following holds.

1. **Exact contact recurrence.**  Some blocked edge occurs in at least
   `\lambda` contact episodes.
2. **Finite contact history.**
   \[
   \boxed{
   J
   \le
   2(\lambda-1)k(n-1).
   }
   \]
3. **Large distinct contact support.**  The set `B` of distinct blocked edges
   used by the episodes satisfies
   \[
   \boxed{
   |B|
   \ge
   \left\lceil\frac{J}{\lambda-1}\right\rceil.
   }
   \]

The third conclusion is the quantitative form available whenever the first
fails; together with CMR582 it implies the second.

### Proof

If no edge occurs `\lambda` times, every nonzero multiplicity is at most
`\lambda-1`, so

\[
J=\sum_f\mu(f)
\le
(\lambda-1)|B|.
\]

Rearrange for the support bound and then use CMR582. ∎

Thus nonrecurrent protected contact is already polynomially bounded at each
chase state.

## 3. Distinct contacts form a protected wall

### Theorem CMR584 — PROVED

Let `B` be any nonempty set of distinct blocked edges at `P`.  Some protected
source or target vertex is incident with at least

\[
\boxed{
d
ge
\left\lceil\frac{|B|}{2k}\right\rceil
}
\]

distinct members of `B`.

Those `d` cells form one row or column contact wall.  Their exact labelled
nonroot full-token incidence in a parent of side `t=p^h` is

\[
\boxed{
d(p+1)(h-1).
}
\]

### Proof

The `2k` protected vertices cover `B` by CMR573.  Pigeonhole gives the degree
bound.  CMR413 assigns exactly `(p+1)(h-1)` labelled full-token incidences to
every physical edge, and the wall edges are distinct. ∎

The incidence count is physical stock: it does not assume that all contact
edges are unavailable simultaneously.

## 4. Full-prefix heavy or dispersed contact tokens

Fix one protected row wall of `d` distinct contact edges; the column case is
symmetric.  At a nonroot depth `b`, partition the varying target coordinates by
residue modulo `p^b`.

### Theorem CMR585 — PROVED

For every integer threshold `H>=2`, at least one of the following holds.

1. **Heavy protected contact token.**  One full-prefix token contains at least
   `H` distinct wall edges.
2. **Dispersed protected contact tokens.**  At least
   \[
   \boxed{
   \left\lceil\frac{d}{H-1}\right\rceil
   }
   \]
   distinct full-prefix token cells are occupied.

With

\[
H=\lceil\sqrt d\rceil
\]

and the trivial interpretation for `d=1`, the wall gives either one token
containing at least `\lceil\sqrt d\rceil` contact edges or at least
`\lfloor\sqrt d\rfloor` distinct occupied contact tokens.

### Proof

This is the exact residue-class partition from CMR512--CMR515.  If no class has
size `H`, every occupied class has size at most `H-1`, so the displayed number
of classes is necessary. ∎

The selected token namespace includes the protected-selector state, envelope,
depth, absolute prefix coordinates, layer, and direction.  Hence the token
charge cannot migrate anonymously between chase states.

## 5. Exact recurrent contacts

### Theorem CMR586 — PROVED

If one exact blocked edge `f` occurs in at least `\lambda` contact episodes,
then for every integer `\sigma>=2` at least one of the following holds.

1. **Reintroduction payment.**
   \[
   \boxed{
   I(f)
   \ge
   \left\lceil\frac{\lambda}{\sigma-1}\right\rceil-1.
   }
   \]
2. **Persistent protected contact.**  One continuous-absence interval contains
   at least `\sigma` selected occurrences of the fixed contact signature
   \[
   \boxed{(P,f,r,\varepsilon).}
   \]

In the second branch, `f` enters the persistent-blocker/cross machinery of
CMR522--CMR545 with its protected-selector owner fixed.

### Proof

Apply the absence-run theorem CMR519 to the selected occurrences of `f`.  The
contact edge and protected state are fixed throughout the selected stage, so a
long absence run fixes the full displayed signature. ∎

## 6. Revised canonical-selector endpoint

Combining CMR575--CMR586, every dynamic canonical-selector history reaches at
least one of:

1. the polynomial nonrecurrent absorption-chase bound;
2. static low-height line, secant-star, matching-wall, heavy-prefix, dispersed-
   carry, or disjoint-deletion geometry;
3. reintroduction/full-token return payment;
4. a protected row/column wall with heavy or dispersed full-token support;
5. one exact persistent protected contact.

The fourth branch uses distinct physical edge stock, while the fifth has one
fixed edge and therefore cannot be double-counted as fresh reserve.

The remaining prime-power frontier is payment for the last exact persistent
contact and temporal reuse of one fixed protected token/wall certificate.  The
expected exits are the already developed persistent-cross alternatives,
protected-reserve depletion, deletion ancestry, or strict envelope expansion.

No all-`n` theorem is claimed.  Contact-universe counts, multiplicity bounds,
wall concentration, token partition arithmetic, and absence-run recurrence are
checked in
[`scripts/verify_prime_power_protected_contact_tokens.py`](../scripts/verify_prime_power_protected_contact_tokens.py).
