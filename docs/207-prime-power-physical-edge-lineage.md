# One physical edge has a finite structural owner lineage

CMR814--CMR821 reduce every unbounded normalized context history to one exact
physical edge restored across owner epochs. This chapter bounds the number of
structural owners through which that edge can pass. Exact wall, skeleton, and
child products do not duplicate a selected matching edge: it is either fixed in
the interface or belongs to one unique child factor. A nonfixed continuation
therefore follows one strict side-descending lineage.

Fix an ambient prime-power parent of side

\[
N=p^h.
\]

Let

\[
H_m=2m^2+m+1
\]

be the static normalized host-stage bound from CMR691, and define

\[
A(N)=\sum_{m=1}^{N}H_m.
\]

## 1. Exact products give unique edge ownership

### Theorem CMR822 -- PROVED

In each of the following exact matching products, every edge used by a perfect
matching is assigned uniquely:

1. a protected/free cross-skeleton product CMR619--CMR620;
2. a fixed child-routing product CMR659;
3. an essential unit-wall product CMR734--CMR735;
4. an essential-core contraction product CMR636 or CMR650.

The edge is either

- one fixed skeleton or contracted-core edge; or
- an edge of exactly one residual factor host.

### Proof

Each cited bijection writes a perfect matching as a disjoint union of the fixed
interface/core and perfect matchings on pairwise disjoint factor vertex classes.
Restriction to those classes is unique. In the unit-wall case, edges outside the
factor blocks which point into the already consumed wall target set occur in no
perfect matching, so a selected edge cannot occupy such a position. ∎

Thus factorization never creates two descendants of one selected physical edge.

## 2. A nonfixed edge follows one strict child

### Theorem CMR823 -- PROVED

Suppose a matching-relevant physical edge is not absorbed into the fixed
skeleton or contracted core at a structural transition. Then it belongs to one
unique positive child factor. At a strict child, unit-wall, or essential
contraction transition, that child's side is strictly smaller than the parent
side.

### Proof

Unique ownership is CMR822. Strict child routing lowers positive factor side by
CMR683. Unit-wall children have side sum `m-1` and hence every positive child has
side at most `m-1` by CMR736. Essential contraction removes at least one matching
pair, and double contraction removes two. ∎

If the edge itself is contracted or becomes fixed interface data, the free
lineage terminates and enters the fixed-certificate escape ledger.

## 3. Static host stages along one edge lineage

### Theorem CMR824 -- PROVED

Inside one closure-envelope epoch, one nonfixed physical edge can belong to at
most

\[
\boxed{A(N)=\sum_{m=1}^{N}(2m^2+m+1)}
\]

static normalized host stages before it is contracted, fixed in an interface,
or leaves the active factor.

### Proof

By CMR823, the positive factor side along the edge lineage strictly decreases
whenever the structural factor changes. Hence each side `m` is visited at most
once on the lineage. At side `m`, CMR691 gives at most `H_m` static host stages.
Sum over `m=1,...,N`. ∎

Branching unit-wall trees do not multiply this count because the edge follows at
most one child.

## 4. Envelope-chain edge-lineage bound

### Theorem CMR825 -- PROVED

A closure branch has at most `h+1` envelope epochs. Therefore one labelled
physical edge has at most

\[
\boxed{
L_{\mathrm{edge}}(N,h)
=(h+1)\bigl(A(N)+1\bigr)
}

structural owner slots, including one boundary slot per envelope epoch.

### Proof

Apply CMR824 in each epoch and use CMR174--CMR175 for the `h+1` epoch bound. The
extra one records the transition into or out of an epoch and deliberately
allows an edge to persist across the boundary without identifying the two owner
labels. ∎

The estimate is polynomial of degree three in `N` for fixed `h`.

## 5. Global restoration recurrence concentrates at one owner

### Theorem CMR826 -- PROVED

Suppose one exact labelled physical edge undergoes `R` genuine restorations along
a closure branch. Then one structural owner slot contains at least

\[
\boxed{
\left\lceil
\frac{R}{L_{\mathrm{edge}}(N,h)}
\right\rceil
}
\]

of those restorations.

For every integer `lambda>=2`, either one fixed structural owner sees `lambda`
restorations of the edge or

\[
\boxed{
R\le(\lambda-1)L_{\mathrm{edge}}(N,h).
}
\]

### Proof

Assign every restoration to the current structural owner slot and apply the
pigeonhole principle using CMR825. ∎

Routing and selected-state labels inside one static owner are handled by private
normalization and do not create additional structural slots.

## 6. Fixed-owner concentration has an immediate response

### Theorem CMR827 -- PROVED

At the fixed owner supplied by CMR826, repeated restoration of the same edge
reaches at least one of:

1. immediate bulk redeletion by a surviving stored anchor;
2. absorption into the private union after a nonimproving activation;
3. loss of one anchor edge and forward deletion ancestry;
4. matching-preserving deletion of the recurrent edge;
5. essential contraction or labelled-pair double contraction;
6. exact normalized cycle erasure;
7. strict potential improvement.

Every noncontracting recurrence contributes another genuine restoration and
exact CMR413 token incidence.

### Proof

Apply the fixed-owner alternatives CMR800--CMR821, together with CMR772--CMR776
when the edge belongs to a recurrent target prescription. ∎

Thus global recurrence cannot remain dispersed among endlessly new owners.

## 7. Fixed interface edges have paid escape

### Theorem CMR828 -- PROVED

If the recurrent physical edge becomes part of a fixed skeleton, contracted core,
or forced certificate instead of following a child factor, then its later escape
requires at least one of:

1. skeleton or routing change with entering/leaving support;
2. certificate-edge deletion;
3. essentiality loss supported by a newly entered edge on an affected alternating
   component;
4. contraction or owner/envelope change.

### Proof

Use CMR624--CMR628 for skeleton histories, CMR643--CMR648 and CMR684--CMR690 for
forced-certificate escape, and the contraction/owner alternatives already
recorded in the structural scheduler. ∎

Fixed-interface ownership is therefore an endpoint, not a hidden extra lineage.

## 8. Physical-edge lineage endpoint

### Corollary CMR829 -- PROVED

Every branch-wide recurrent physical edge reaches at least one of:

1. at most `L_edge(N,h)` structural owner slots;
2. one fixed owner with quantitatively recurrent restoration;
3. private absorption and bulk redeletion;
4. anchor-loss or stored-avoidance ancestry;
5. essential contraction, double contraction, or strict child descent;
6. fixed-interface escape payment;
7. one of at most `h` envelope expansions;
8. strict target-potential improvement.

Hence the remaining prime-power return problem is fixed-owner and fixed-edge:
show that an edge which survives every deletion, normalization, contraction, and
interface response forces a final target-load or potential decrease. Owner
proliferation is no longer part of that frontier.

### Proof

Combine CMR822--CMR828 with the global return and active-context endpoints
CMR777--CMR821. ∎

No all-`n` theorem is claimed. Unique product ownership, decreasing edge
lineages, owner-slot arithmetic, and restoration concentration are checked in
[`scripts/verify_prime_power_physical_edge_lineage.py`](../scripts/verify_prime_power_physical_edge_lineage.py).
