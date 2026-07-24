# Blocker-cover state domains

The candidate-level barrier PP3cu shows that independent deletion choices do not
usually cover the source blockers of selected cells.  The strongest unary
response is to condition each block state on covering all of its own
retained-pair blockers.  This chapter gives the exact domain and records its
finite failure on the stored layers.

## 1. Exact source-blocker cover condition

Let `S` be a saturated no-three source, let `P` be one matching layer, and let
`E subseteq P` be an `r`-edge block with one reserved width-two interval.  A
full-bank state chooses a four-edge deletion `D subseteq E` and a width-two patch
`Q` restoring the corresponding row and column deficits.

For a candidate point `z`, let

\[
 \mathcal B_S(z)
 =
 \{\{p,q\}\subseteq S:p,q,z\text{ are collinear}\}.
\]

This is a matching on `S`.

### Proposition PP3cw -- PROVED

The state `(D,Q)` creates no retained-retained-patch triple if and only if

\[
 \boxed{
 D\cap\{p,q\}\ne\varnothing
 \quad
 \text{for every }z\in Q
 \text{ and every }\{p,q\}\in\mathcal B_S(z).
 }
\]

#### Proof

The retained source is `S setminus D`.  A triple with one patch point `z` and two
retained source points exists exactly when one blocker pair in
`mathcal B_S(z)` is disjoint from `D`. ∎

Define the **blocker-cover domain**

\[
 \Omega_B(E)
 =
 \{(D,Q):D\text{ covers every blocker matching of every }z\in Q\}.
\]

Every state in this domain has the same row and column margins because it is a
subfamily of the full 36-state bank.

## 2. Anchor and internal domains

Define:

- `Omega_Q(E)`: states whose inserted patch `Q` is internally no-three;
- `Omega_A(E)`: states for which no retained source point lies on a secant of
  two patch points;
- `Omega_ext(E)=Omega_Q(E) intersect Omega_B(E) intersect Omega_A(E)`.

### Proposition PP3cx -- PROVED

1. Restricting a block variable to any nonempty intersection of these domains
   preserves equal margins.
2. Using `Omega_Q intersect Omega_B` removes the complete `N_1` profile from
   PP3ci.
3. Using `Omega_ext` removes `N_1,N_h,N_2` simultaneously; only cross-block
   profiles remain.
4. A state in `Omega_ext` is exactly a valid one-block extension of `S` into the
   reserved width-two interval.

#### Proof

Equal margins hold state by state in PP3cf.  PP3cw removes precisely the
retained-retained-patch triples.  The definition of `Omega_A` removes precisely
the retained-patch-patch triples.  `Omega_Q` removes internal patch triples.
These are all possible new triple classes because `S` itself is no-three. ∎

This is the cleanest possible unary conditioning route.  It is stronger than
necessary in a multiblock construction, since a blocker endpoint may be deleted
by another block.

## 3. Failure certificate

### Corollary PP3cy -- PROVED

If `Omega_B(E)` is empty, then every full-bank state contains a selected patch
cell `z` and a blocker pair in `mathcal B_S(z)` that is disjoint from its local
four-edge deletion.

If `Omega_ext(E)` is empty, every state has at least one of:

1. an internal patch triple;
2. an uncovered source blocker pair;
3. a retained source anchor on a patch secant.

This trichotomy gives an exact target for state-family enlargement or protected
trades.

## 4. Finite stored-layer obstruction

The script

```bash
python scripts/analyze_blocker_cover_state_domains.py \
  certificates/prime-patching-small.json
```

uses one complete matching layer as the block and enumerates all
`36 binom(n,4)` states.  On the stored certificates:

- the blocker-cover domain is nonempty through side six;
- it is empty on both matching layers at every side seven through ten;
- the complete external domain is empty on every tested layer from side four
  through ten.

Thus retaining all 36 local geometries does not make independent one-block
conditioning viable on the stored larger seeds.  The obstruction is specifically
retained-pair coverage: many internally clean and anchor-clean states remain when
`Omega_B` is already empty.

## 5. Revised use of blocker covers

The finite obstruction does not refute multiblock matching-first patching.  It
shows that blocker covers must be allowed to cross block boundaries or be
supplied by auxiliary trades.

The next exact object is therefore a **blocker-demand CSP**:

- selecting a candidate cell in one block demands deletion of at least one
  endpoint from every additional blocker pair;
- a one-layer-endpoint blocker gives a binary demand between the candidate block
  and the endpoint block;
- a two-layer-endpoint blocker gives a rank-at-most-three demand involving the
  candidate block and the one or two endpoint blocks;
- undeletable other-layer blocker pairs forbid the candidate cell outright.

This demand family inherits endpoint disjointness from the external-point
blocker matching.  A successful theorem must exploit that matching structure
rather than force every demand to be paid inside its controller block.