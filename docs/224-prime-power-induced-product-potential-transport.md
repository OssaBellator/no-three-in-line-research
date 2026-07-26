# Induced triple potential transports through fixed cores as low-rank boxes

CMR950--CMR957 make same-vertex-set dynamics well founded.  Structural descent
contracts a compatible prescription or enters an exact wall, child, or skeleton
product.  The real-triple potential is not additive across those products, so the
potential must be transported explicitly.

Fixing a compatible core does not create an uncontrolled new interaction.  Every
triple is one of:

- a constant triple contained in the fixed core;
- a pure triple contained in one residual factor;
- an anchored or cross-factor atom whose prescription has rank at most two in
  every touched residual factor.

Occurrence of every nonconstant atom is an exact Cartesian box.  On the current
minimum face, an active coupling atom is either killed by deleting one edge which
some minimum state omits, or all of its residual edges are common to the minimum
face and contract exactly.  After finitely many such responses, the minimum face
has a fixed core conflict or no active coupling atom; in the latter case the
induced potential is additive on every surviving minimum state.

This is a set-family transport theorem.  It does not assert that the contracted
minimum face equals all perfect matchings of one residual host.

Let `A` be a finite set of residual factors with pairwise disjoint labelled edge
sets `E_a`.  Let `\mathcal F_a` be a nonempty equal-cardinality state family on
`E_a`, and let `C` be one fixed compatible labelled prescription disjoint from all
`E_a`.  Put

\[
\mathcal F
=
\left\{
C\sqcup\bigsqcup_{a\in A}R_a:
R_a\in\mathcal F_a
\right\}.
\]

All labelled edges retain their original parent-grid cells.  Let `\Phi` count
physical collinear triples in a full state.

## 1. Exact constant, pure, and coupling decomposition

For a product state

\[
R=C\sqcup\bigsqcup_aR_a,
\]

let:

- `\kappa(C)` count collinear triples contained in `C`;
- `X_a(R_a)` count triples contained entirely in `R_a`;
- `X_\times(\mathbf R;C)` count all remaining triples.

### Theorem CMR958 -- PROVED

For every product state,

\[
\boxed{
\Phi(R)
=
\kappa(C)
+
\sum_{a\in A}X_a(R_a)
+
X_\times(\mathbf R;C).
}
\]

The counted classes are pairwise disjoint and exhaustive.

### Proof

A three-edge subset has a unique support among the disjoint classes
`C,(E_a)_{a\in A}`.  It lies wholly in `C`, wholly in one residual factor, or in
neither type.  Restrict the partition to physical collinear triples. ∎

Thus all nonadditivity is isolated in `X_\times`.

## 2. Coupling atoms have low local rank

A **coupling atom** is a compatible physical collinear triple in

\[
C\cup\bigcup_aE_a
\]

which is contained neither in `C` nor in one `E_a`.  For such an atom `T`, put

\[
T_C=T\cap C,
\qquad
T_a=T\cap E_a.
\]

### Theorem CMR959 -- PROVED

Every coupling atom has nonempty residual part

\[
T^\circ=T\setminus C,
\]

and for every factor

\[
\boxed{|T_a|\le2.}
\]

The possible positive residual rank patterns are:

- `(1)` or `(2)` when the remaining edge or edges are anchored by fixed core
  edges;
- `(2,1)` or `(1,1,1)` across two or three residual factors.

### Proof

If `T^\circ` were empty, the atom would lie in `C`.  If one residual factor
contained all three edges, the atom would be pure in that factor.  The positive
residual ranks sum to `3-|T_C|` and no single factor has rank three. ∎

In particular structural contraction never creates a rank-three obstruction
inside one new residual factor.

## 3. Every coupling atom is an exact product box

For each factor define

\[
\mathcal F_a(T_a)
=
\{R_a\in\mathcal F_a:T_a\subseteq R_a\},
\]

with the full factor family when `T_a` is empty.

### Theorem CMR960 -- PROVED

The product states containing `T` are exactly

\[
\boxed{
\{C\}\times
\prod_{a\in A}\mathcal F_a(T_a).
}
\]

### Proof

The fixed part `T_C` is already present.  The remaining labelled edge classes are
disjoint, so containment of `T` is equivalent to independent containment of every
local prescription `T_a`. ∎

This extends CMR631 and CMR666 to an arbitrary fixed compatible core.

## 4. Explicit finite coupling stock

Let

\[
c=|C|,
\qquad
E=\sum_a|E_a|.
\]

### Theorem CMR961 -- PROVED

The coupling-atom stock is finite and obeys the coarse bound

\[
\boxed{
N_\times(C)
\le
c\binom{E}{2}
+
\binom c2E
+
\binom E3.
}
\]

The final term may be restricted to triples meeting at least two residual factors.

### Proof

A coupling atom has one of three core ranks.  With one fixed-core edge choose two
residual edges; with two fixed-core edges choose one residual edge; with no fixed
edge choose three residual edges.  These choices overcount compatibility,
collinearity, and the exclusion of pure residual triples. ∎

## 5. Further contraction preserves the low-rank form

Let `P` be a compatible labelled prescription common to every state of a
subfamily of `\mathcal F`.  Contract `P` exactly and replace every old triple `T`
by its residual prescription `T\setminus P`.

### Theorem CMR962 -- PROVED

Under contraction, every old triple becomes exactly one of:

1. a constant conflict, when `T\subseteq C\cup P`;
2. a pure residual-factor triple;
3. an anchored or cross-factor residual atom whose local rank in each residual
   factor is at most two;
4. an empty or lower-rank inactive prescription.

Occurrence is preserved exactly:

\[
\boxed{
T\subseteq C\cup P\cup R'
\iff
T\setminus(C\cup P)\subseteq R'.
}

### Proof

Remove the fixed edges from the triple.  Local ranks can only decrease.  The
containment equivalence follows because all removed edges are present in every
contracted state. ∎

Thus induced-objective contraction transports, rather than discards, every
cross-factor term.

## 6. Minimum-preserving coupling deletion or contraction

Let `\mathcal M` be the minimum face of the current product family for the
induced potential.  Let `T` be a coupling atom occurring in at least one state of
`\mathcal M`, and let `T^\circ=T\setminus C`.

### Theorem CMR963 -- PROVED

At least one exact response is available.

1. Some edge `e\in T^\circ` is omitted by a state of `\mathcal M`.  Deleting `e`
   preserves the minimum value and destroys every occurrence of `T`.
2. Every edge of `T^\circ` belongs to every state of `\mathcal M`.  The complete
   residual prescription `T^\circ` is contained in the minimum core and contracts
   exactly, lowering residual state cardinality by `|T^\circ|`.

### Proof

If the residual prescription is not contained in the common minimum core, one of
its edges has a minimum-state counterexample.  Apply CMR911 to delete that edge
while preserving the minimum.  Otherwise every residual edge is common and CMR912
contracts the compatible prescription. ∎

The first branch preserves the exact residual product host when `e` belongs to
one factor host; the second is an exact minimum-face set-family contraction.

## 7. Finite coupling normalization

Repeat CMR963 on the first active coupling atom, residualising the atom stock
after every contraction.

### Theorem CMR964 -- PROVED

Before structural owner exit or strict potential improvement, the normalization
terminates after at most

\[
\boxed{E+k}
\]

responses, where `E` is the initial residual edge-universe size and `k` is the
initial residual state cardinality.

At termination at least one of the following holds.

1. A constant conflict lies entirely in the accumulated fixed core.
2. No nonconstant coupling atom occurs in any surviving minimum state.

### Proof

Every deletion removes a previously available residual edge and occurs at most
`E` times.  Every contraction lowers residual state cardinality by at least one
and occurs with total rank at most `k`.  Restriction cannot activate a previously
inactive atom; contraction only residualises existing atoms.  If an atom loses
all residual edges, it becomes a constant fixed-core conflict.  Otherwise the
finite active stock is eventually exhausted. ∎

## 8. Coupling-normalized structural endpoint

### Corollary CMR965 -- PROVED

After any exact compatible contraction or fixed product decomposition, the
minimum-potential problem reaches at least one of:

1. a fixed-core physical triple certificate;
2. a minimum-preserving deletion of a low-rank coupling edge;
3. exact contraction of a common rank-one, rank-two, or rank-three coupling
   prescription;
4. a minimum face on which
   \[
   \boxed{
   \Phi(R)
   =
   \kappa(C)+\sum_aX_a(R_a)
   }
   \]
   for every surviving minimum state;
5. owner/factor/wall/envelope exit or strict potential improvement.

No product additivity is assumed before branch 4.  The remaining structural
frontier is to turn branch 4 into strict factor descent or to show that the fixed
core certificate in branch 1 forces target-load, wall, reserve, or envelope
progress.  Host representability of contracted minimum faces remains separate.

### Proof

Combine CMR958--CMR964 with the existing exact product and forced-certificate
transport results. ∎

No all-`n` theorem is claimed.  Triple classification, local-rank vectors,
Cartesian boxes, stock bounds, contraction residualisation, minimum-face actions,
and finite normalization are checked in
[`scripts/verify_prime_power_induced_product_potential.py`](../scripts/verify_prime_power_induced_product_potential.py).
