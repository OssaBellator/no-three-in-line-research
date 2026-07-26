# Induced triple potential transports through fixed cores as low-rank boxes

CMR950--CMR957 make same-vertex-set dynamics well founded. Structural descent
contracts a compatible prescription or enters an exact wall, child, or skeleton
product. The real-triple potential is not additive across those products, so its
cross-factor terms must be transported explicitly.

Fixing a compatible core creates only constant conflicts, pure factor conflicts,
and anchored or cross-factor atoms of local rank at most two. Every nonconstant
atom occurs on an exact Cartesian box. On the minimum face, an active coupling
atom is killed by a minimum-preserving edge deletion or its residual prescription
is common and contracts exactly. In the contraction branch the continuation is
on the minimum face itself; no commonness in nonminimum states is assumed.

This is a set-family transport theorem. It does not assert that the contracted
minimum face equals all perfect matchings of one residual host.

Let `A` index residual factors with pairwise disjoint labelled edge sets `E_a`.
Let `\mathcal F_a` be nonempty equal-cardinality state families on those sets and
let `C` be one fixed compatible labelled prescription disjoint from all `E_a`.
Put

\[
\mathcal F
=
\left\{
C\sqcup\bigsqcup_{a\in A}R_a:
R_a\in\mathcal F_a
\right\}.
\]

All edges retain their original parent-grid cells, and `\Phi` counts physical
collinear triples.

## 1. Exact constant, pure, and coupling decomposition

For `R=C\sqcup\bigsqcup_aR_a`, let `\kappa(C)` count triples in `C`, let
`X_a(R_a)` count triples wholly in factor `a`, and let `X_\times` count all
remaining triples.

### Theorem CMR958 -- PROVED

\[
\boxed{
\Phi(R)
=
\kappa(C)+\sum_{a\in A}X_a(R_a)+X_\times(\mathbf R;C).
}
\]

The classes are pairwise disjoint and exhaustive.

### Proof

A three-edge subset has a unique support among the disjoint classes
`C,(E_a)_{a\in A}`. It lies wholly in `C`, wholly in one residual factor, or in
neither type. Restrict to physical collinear triples. ∎

## 2. Coupling atoms have low local rank

A coupling atom `T` is a compatible physical collinear triple contained neither
in `C` nor in one `E_a`. Put

\[
T_C=T\cap C,
\qquad
T_a=T\cap E_a,
\qquad
T^\circ=T\setminus C.
\]

### Theorem CMR959 -- PROVED

The residual part is nonempty and

\[
\boxed{|T_a|\le2}
\]

for every factor. Up to factor order, the positive residual-rank patterns are:

- `(1)` when two fixed-core edges anchor one residual edge;
- `(2)` or `(1,1)` when one fixed-core edge anchors two residual edges;
- `(2,1)` or `(1,1,1)` when no fixed-core edge occurs.

### Proof

An empty residual part would put `T` inside `C`. Three edges in one residual
factor would make it pure. The listed integer partitions exhaust the remaining
core ranks zero, one, and two. ∎

Thus no coupling term has rank three in one residual factor.

## 3. Every coupling atom is an exact product box

Define

\[
\mathcal F_a(T_a)=\{R_a\in\mathcal F_a:T_a\subseteq R_a\},
\]

using the full factor family when `T_a` is empty.

### Theorem CMR960 -- PROVED

The product states containing `T` are exactly

\[
\boxed{
\{C\}\times\prod_{a\in A}\mathcal F_a(T_a).
}
\]

### Proof

The fixed part is automatic. Containment of the residual parts is independent
across the disjoint factor edge classes. ∎

## 4. Explicit finite coupling stock

Let

\[
c=|C|,
\qquad
E=\sum_a|E_a|.
\]

### Theorem CMR961 -- PROVED

The coupling-atom stock obeys

\[
\boxed{
N_\times(C)
\le
c\binom E2+inom c2E+inom E3.
}
\]

The final term may be restricted to triples meeting at least two residual
factors.

### Proof

Overcount by core rank: choose one fixed and two residual edges, two fixed and one
residual edge, or three residual edges. ∎

## 5. Further contraction preserves the low-rank form

Let `P` be a compatible labelled prescription common to every state of a
subfamily. Contract it and residualise every old triple.

### Theorem CMR962 -- PROVED

Every old triple becomes one of:

1. a constant conflict inside the enlarged fixed core;
2. a pure residual-factor triple;
3. an anchored or cross-factor atom of local rank at most two;
4. an empty or lower-rank inactive prescription.

Occurrence is preserved exactly:

\[
\boxed{
T\subseteq C\cup P\cup R'
\iff
T\setminus(C\cup P)\subseteq R'.
}
\]

### Proof

Remove the fixed edges from the triple. Local ranks only decrease, and all
removed edges occur in every contracted state. ∎

## 6. Minimum-preserving coupling deletion or contraction

Let `\mathcal M` be the minimum face of the current induced-potential family and
let `T` be a coupling atom occurring in at least one state of `\mathcal M`.

### Theorem CMR963 -- PROVED

At least one exact response is available.

1. Some edge `e\in T^\circ` is omitted by a state of `\mathcal M`. Deleting `e`
   preserves the minimum value and destroys every occurrence of `T`.
2. Every edge of `T^\circ` belongs to every state of `\mathcal M`. Restrict to
   `\mathcal M`, contract the complete residual prescription, and lower residual
   state cardinality by `|T^\circ|`.

### Proof

If the residual prescription is not in the common minimum core, one edge has a
minimum-state counterexample and CMR911 gives minimum-preserving deletion.
Otherwise the prescription is common to the minimum face, so CMR912 gives exact
set-family contraction on that face. ∎

The first branch preserves an exact product host when `e` lies in one factor
host. The second branch deliberately makes only a minimum-face set-family claim.

## 7. Finite coupling normalization

Repeat CMR963 on the first active coupling atom. After a contraction, continue on
the contracted minimum face and residualise the atom stock.

### Theorem CMR964 -- PROVED

Before structural owner exit or strict potential improvement, the process stops
after at most

\[
\boxed{E+k}
\]

responses, where `E` is the initial residual edge-universe size and `k` is the
initial residual state cardinality. At termination:

1. a constant conflict lies in the accumulated fixed core; or
2. no nonconstant coupling atom occurs in any surviving minimum state.

### Proof

Each deletion removes one previously available residual edge and occurs at most
`E` times. Contractions have total rank at most `k`. Minimum-preserving deletion
restricts the minimum face and cannot activate a previously inactive atom;
contraction only residualises existing atoms. An atom with no residual edges
becomes constant. ∎

## 8. Coupling-normalized structural endpoint

### Corollary CMR965 -- PROVED

After any exact compatible contraction or fixed product decomposition, the
minimum-potential problem reaches at least one of:

1. a fixed-core physical triple certificate;
2. minimum-preserving deletion of a low-rank coupling edge;
3. exact contraction of a common rank-one, rank-two, or rank-three coupling
   prescription on the minimum face;
4. a surviving minimum face on which
   \[
   \boxed{
   \Phi(R)=\kappa(C)+\sum_aX_a(R_a)
   }
   \]
   for every minimum state;
5. owner/factor/wall/envelope exit or strict potential improvement.

No product additivity is assumed before branch 4. The remaining structural
frontier is to turn branch 4 into strict factor descent, or to route the fixed
core certificate of branch 1 into target-load, wall, reserve, or envelope
progress. Host representability of contracted minimum faces remains separate.

No all-`n` theorem is claimed. Triple classification, local-rank vectors,
Cartesian boxes, stock bounds, contraction residualisation, minimum-face actions,
and finite normalization are checked in
[`scripts/verify_prime_power_induced_product_potential.py`](../scripts/verify_prime_power_induced_product_potential.py).
