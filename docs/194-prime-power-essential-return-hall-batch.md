# Essential target-edge returns expose canonical unit Hall walls

CMR720--CMR726 attach one missing edge of a stored avoiding matching to every
essential return of a previously deleted target edge. Hall's theorem gives a
more precise normal form. Removing one essential edge from a matchable host
leaves a matching of size exactly one below perfect, so every Hall obstruction
has deficiency exactly one. The returned edge is the unique current edge which
repairs the missing neighbour of that cut.

Fix a balanced bipartite vertex set of side `m`. Let

\[
e=(u,v)
\]

be essential in a matchable host `H`, and put

\[
G=H-e.
\]

Let `M_0` be the stored earlier perfect matching which avoided `e`.

## 1. Removing one essential edge has matching deficiency one

### Theorem CMR727 -- PROVED

The maximum matching number of `G` is

\[
\boxed{\nu(G)=m-1.}
\]

Consequently

\[
\boxed{
\max_{X\subseteq L}
\bigl(|X|-|N_G(X)|\bigr)=1.
}
\]

### Proof

Every perfect matching of `H` contains `e`. Removing `e` from one such matching
leaves a matching of size `m-1` in `G`, so `nu(G)>=m-1`. Since `e` is essential,
`G` has no perfect matching, and therefore `nu(G)<=m-1`. Equality follows.
The deficiency form of Hall's theorem gives the second identity. ∎

Thus a larger Hall-deficiency batch cannot occur after removing only one
essential edge.

## 2. Every deficient cut is a unit wall repaired by e

Let `X` be any Hall-deficient source set in `G` and write

\[
Y=N_G(X).
\]

### Theorem CMR728 -- PROVED

One has

\[
\boxed{|Y|=|X|-1,}
\qquad
\boxed{u\in X,}
\qquad
\boxed{v\notin Y.}
\]

Moreover

\[
\boxed{N_H(X)=Y\cup\{v\}.}
\]

Hence `e` is the unique edge of `H` from `X` to the target complement of `Y`.

### Proof

CMR727 makes every positive Hall deficiency equal to one. If `u` were not in
`X`, adding `e` to `G` would not enlarge the neighbour set of `X`, so `H` would
also violate Hall. Thus `u` lies in `X`. If `v` belonged to `Y`, adding `e`
would again leave the neighbour set unchanged, with the same contradiction.
Therefore `v` is outside `Y`, and the only edge added in passing from `G` to `H`
is `e=(u,v)`, giving the displayed neighbour identity. ∎

The wall is exact and owner-local: its missing neighbour is the target endpoint
of the returned essential edge.

## 3. Canonical minimal unit wall

Choose the lexicographically first inclusion-minimal Hall-deficient source set
`X`, and put `Y=N_G(X)`.

### Theorem CMR729 -- PROVED

For every `x` in `X`,

\[
\boxed{N_G(X\setminus\{x\})=Y.}
\]

If `|X|>=2`, every target vertex in `Y` has at least two neighbours in `X`.
If `|X|=1`, then `X={u}` and `Y` is empty, so the source endpoint of `e` is
isolated in `G`.

### Proof

By inclusion-minimality, `X\setminus\{x\}` is not deficient. Its neighbour set
is contained in `Y`, while

\[
|X\setminus\{x\}|=|X|-1=|Y|.
\]

Hall's inequality therefore forces equality of the neighbour set with `Y`.
If some `y` in `Y` had only one neighbour `x` in `X`, then removing `x` would
remove `y` from the neighbour set, contradicting the equality. The singleton
case follows from `|Y|=|X|-1=0` and CMR728. ∎

Thus a nontrivial unit wall has no target leaf on its deficient side.

## 4. The stored avoiding matching supplies a missing wall edge

Define

\[
F_{X,Y}
=
\{(x,M_0(x)):x\in X,\ M_0(x)\notin Y\}.
\]

### Theorem CMR730 -- PROVED

The set `F_{X,Y}` is nonempty, is a matching contained in `M_0`, and every one
of its edges is absent from `H`.

### Proof

The `|X|` targets `M_0(X)` are distinct, while `Y` has size `|X|-1`, so at least
one stored matching target lies outside `Y`. If such an edge belonged to `H`, it
would also belong to `G`, because `M_0` avoids `e`; its target would then lie in
`N_G(X)=Y`, a contradiction. ∎

Choose the first edge of `F_{X,Y}` in the stored matching order and call it the
canonical blocking witness `f`.

## 5. Finite canonical wall stock or exact recurrence

The canonical unit-wall signature is

\[
\Sigma_{\mathrm{wall}}
=
(
\text{owner},
 e,
 X,
 Y,
 f
).
\]

The set `X`, the set `Y`, and the witness `f` are chosen deterministically from
the owner and `e`.

### Theorem CMR731 -- PROVED

At a fixed owner stage of side `m`, there are at most

\[
\boxed{m^2}
\]

canonical unit-wall signatures. For every integer `lambda>=2`, a history of `K`
essential-return episodes at that owner reaches one of:

1. one exact signature in at least `lambda` episodes;
2. 
   \[
   \boxed{K\le(\lambda-1)m^2.}
   \]

### Proof

There is at most one deterministic wall signature for each physical essential
edge `e`, and the host has at most `m^2` edges. Apply the pigeonhole principle.
∎

No exponential stock of arbitrary Hall witnesses is charged.

## 6. Escape from a persistent unit wall is an entering cross-cut edge

Fix one recurrent signature `(e,X,Y,f)` at an unchanged owner. The avoiding host
`G=H-e` has no edge from `X` to the target complement of `Y`.

### Theorem CMR732 -- PROVED

Suppose a later matchable owner state avoids the forced use of `e` or no longer
has the same unit Hall wall. Then at least one of the following has occurred.

1. A new or restored edge enters from `X` to the target complement of `Y`.
2. An endpoint of the cut is contracted, giving strict side descent.
3. The factor, routing, envelope, or host owner changes.

If the canonical stored witness `f` itself is repeatedly absent and present, its
absence runs satisfy

\[
\boxed{\rho(f)\le1+I(f),}
\]

so repeated returns pay the existing reintroduction ledger.

### Proof

As long as the owner and vertex sets are fixed and no edge is added from `X`
outside `Y`, the neighbour set of `X` remains contained in `Y`, whose size is
`|X|-1`; Hall deficiency persists. Hence any same-owner escape requires a
cross-cut addition. Contraction and owner change are the other structural ways
to leave the statement. The absence-run identity is CMR519. ∎

The added cross-cut edge has exact entering-edge and full-token incidence.

## 7. Essential-return unit-wall endpoint

### Corollary CMR733 -- PROVED

Every essential return of a previously deleted target edge reaches at least one
of the following.

1. A singleton forced source row, when the canonical wall has `|X|=1`.
2. A robust unit Hall wall with every target in `Y` having at least two neighbours
   in `X`.
3. Finite canonical wall stock.
4. One exact recurrent unit-wall signature.
5. A new or restored cross-cut edge with entering-edge and token payment.
6. Reintroduction of the canonical stored witness edge.
7. Strict contraction or owner change.

Therefore removing one essential returned edge never creates a large-deficiency
mystery. It creates one exact deficiency-one wall, canonically owned by the
returned edge. The next structural action is the exact matching factorisation
across that unit wall after the essential edge is contracted.

### Proof

Use CMR727--CMR730 for the wall structure, CMR731 for finite stock or recurrence,
and CMR732 for escape. ∎

No all-`n` theorem is claimed. Unit matching deficiency, minimal-wall
robustness, canonical missing-edge witnesses, and recurrence bounds are checked
in
[`scripts/verify_prime_power_essential_return_hall_batch.py`](../scripts/verify_prime_power_essential_return_hall_batch.py).
