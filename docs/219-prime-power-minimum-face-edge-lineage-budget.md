# Minimum-face closure gives a branch-wide budget for one physical edge

CMR822--CMR829 prove that one labelled physical edge has only

\[
L_{\mathrm{edge}}(N,h)
=
(h+1)\bigl(A(N)+1\bigr)
\]

structural owner slots along a prime-power closure branch.  CMR910--CMR917 close
the edge at one fixed owner: it is deleted against a minimum state which avoids
it, or it belongs to the complete minimum core and contracts.

Combining these statements gives a simple global amortisation for one actual
minimum-anchor execution.  Each structural owner slot receives at most one
uncharged first closure of the edge.  Every later active appearance at that slot
requires a genuine physical restoration, unless the edge enters the minimum core
and its free lineage terminates by contraction.

This theorem applies to one executed branch, not to parallel hypothetical
children of the completeness tree.  Parallel branches are handled by the leaf
compression and support-batching results CMR894--CMR901 and CMR870--CMR893.

Fix an ambient prime-power parent of side

\[
N=p^h,
\]

and put

\[
L=L_{\mathrm{edge}}(N,h).
\]

Fix one labelled physical edge `e` and follow its unique structural lineage.
Call an occurrence **active** when the current minimum-anchor scheduler actually
processes `e` by deletion, conditioning, contraction, or a target/context response.

## 1. One free closure per owner slot

### Theorem CMR918 -- PROVED

At one structural owner slot, the first active occurrence of `e` reaches one of:

1. `e` lies outside the current minimum core and is deleted while preserving a
   minimum state;
2. `e` lies in the minimum core and contracts, terminating the free edge lineage;
3. strict potential improvement or structural owner exit occurs first.

If branch 1 occurs, every later active occurrence of `e` at the same owner slot
requires at least one genuine restoration after that first deletion.

### Proof

The first two branches are CMR914.  Once branch 1 deletes the edge, it remains
absent until a physical zero-to-one transition.  Owner exit and improvement are
the remaining scheduler endpoints. ∎

## 2. Active occurrences force restoration count

Suppose the free lineage visits `s` owner slots and has `J` active occurrences,
with no minimum-core contraction.  Let `R` be the number of genuine restorations
of `e` between those occurrences.

### Theorem CMR919 -- PROVED

One has

\[
\boxed{
R\ge J-s
}
\]

and therefore

\[
\boxed{
R\ge J-L.
}
\]

### Proof

At each visited owner slot, charge its first active occurrence for free.  Every
remaining occurrence at that slot follows the minimum-preserving deletion from
CMR918 and therefore needs a restoration.  Summing over the `s` nonempty slots
gives `R\ge J-s`; CMR825 gives `s\le L`. ∎

The bound remains valid if an edge first arrives absent: its first later active
appearance is already a restoration, so the free-slot allowance only overcounts.

## 3. Threshold form

### Theorem CMR920 -- PROVED

For every integer `\lambda\ge2`, before minimum-core contraction, at least one of
the following holds.

1. One fixed structural owner slot sees at least `\lambda` genuine restorations of
   `e`.
2. The number of active occurrences satisfies
   \[
   \boxed{J\le\lambda L.}
   \]

### Proof

If branch 1 fails, each of the at most `L` owner slots contains at most
`\lambda-1` restorations.  Thus `R\le(\lambda-1)L` by CMR826.  CMR919 gives
`J\le R+L\le\lambda L`. ∎

## 4. Exact token payment

### Theorem CMR921 -- PROVED

Absent contraction, `J` active occurrences of `e` carry labelled nonroot
full-token incidence at least

\[
\boxed{
\max\{0,J-L\}(p+1)(h-1).
}
\]

If one fixed owner sees `\lambda` restorations, those restorations alone carry

\[
\boxed{
\lambda(p+1)(h-1)
}
\]

labelled incidences.

### Proof

Apply CMR413 to the restoration lower bound in CMR919.  The fixed-owner statement
is the same identity restricted to those `\lambda` restoration occurrences. ∎

## 5. A recurrent fixed-owner edge still deletes or contracts

### Theorem CMR922 -- PROVED

At the recurrent owner supplied by CMR920, every restoration of `e` has one of
the following responses relative to the current minimum face.

1. `e` remains outside the minimum core and is deleted again while preserving the
   current minimum value;
2. `e` enters the minimum core and contracts, lowering residual state cardinality;
3. another edge or the owner changes, or strict potential improvement occurs.

If the first branch occurs repeatedly, every repetition is a distinct paid
absence run and no uncharged fixed-owner structural progress is obtained.

### Proof

Apply CMR914 after each restoration.  CMR915 gives the paid absence-run statement.
The remaining changes are the dynamic exits already listed in CMR917. ∎

## 6. Total active-edge episode bound without recurrence

There are at most `2N^2` labelled physical edges in the ambient two-layer board.

### Theorem CMR923 -- PROVED

Fix `\lambda\ge2`.  Along one minimum-anchor execution, suppose

1. no labelled physical edge contracts through the minimum core;
2. no fixed structural owner sees `\lambda` restorations of one edge; and
3. no strict potential or structural exit is charged.

Then the total number `K` of active edge occurrences satisfies

\[
\boxed{
K\le2N^2\lambda L_{\mathrm{edge}}(N,h).
}
\]

### Proof

CMR920 bounds active occurrences of each labelled physical edge by `\lambda L`.
Sum over at most `2N^2` labels. ∎

This is an execution-history bound, not a count of nodes in the complete
parallel branch tree.

## 7. Minimum-core contractions have finite total rank

### Theorem CMR924 -- PROVED

Along a nested same-owner minimum-face segment whose states initially have
cardinality `k`, the total rank contracted through successive complete minimum
cores is at most

\[
\boxed{k.}
\]

For a saturated two-layer side-`N` state this is at most `2N`.  After owner or
factor descent, the corresponding residual cardinality is smaller.

### Proof

This is CMR916, applied after every strict core-growth event.  Exact contraction
removes the newly common rank and residual cardinality never increases inside the
segment. ∎

## 8. Minimum-face edge-lineage endpoint

### Corollary CMR925 -- PROVED

Every active labelled edge along one minimum-anchor prime-power execution reaches
at least one of:

1. at most `L_{\mathrm{edge}}(N,h)` uncharged first-owner closures;
2. minimum-preserving deletion;
3. exact minimum-core contraction and strict residual-cardinality descent;
4. quantitatively recurrent restoration at one fixed owner;
5. exact full-token incidence proportional to all appearances beyond the owner
   stock;
6. another physical-edge change, fixed-interface escape, owner/factor/wall
   descent, or envelope expansion;
7. strict potential improvement.

Consequently the fixed-owner, fixed-edge recurrence is no longer an unclassified
local obstruction in minimum-anchor mode.  What remains is to place an
unconditional capacity or target-load decrease on the accumulated full-token
incidence, and to control how the minimum face changes under structural owner
exits.

### Proof

Combine CMR918--CMR924 with the unique edge lineage and interface-escape results
CMR822--CMR829. ∎

No all-`n` theorem is claimed.  Owner-slot charges, restoration lower bounds,
threshold arithmetic, token incidence, global active-edge sums, and core-rank
budgets are checked in
[`scripts/verify_prime_power_minimum_face_edge_lineage.py`](../scripts/verify_prime_power_minimum_face_edge_lineage.py).
