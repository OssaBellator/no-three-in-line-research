# Least-field restoration gates for recurrent bounded-denominator cycles

**Branch:** `research/bounded-denominator-absorbers`

BDA5az--BDA5bf reduce every long same-denominator history to one simple cycle in a finite decorated physical-profile graph and then to one cycle-space chord.  This note gives a complementary cycle-local address.  Every nonconstant exact cycle must leave and later restore one canonical least physical field.  Thus a recurrent cycle cannot remain an undifferentiated word: it exposes one explicit restoration gate that can be paid, descended, ruled out, or ticketed.

The statements are abstract finite-profile facts.  Their use in BDA6 requires the declared fields to be complete physical fields: a change of denominator, direction, board anchor, role, owner, support, operation word, occurrence lineage, or legality interpretation is an outer reset rather than an invisible state change.

## Complete product address

Fix one same-denominator epoch.  Let every decorated physical profile have a complete address

\[
 x=(x_1,\ldots,x_m)\in A_1\times\cdots\times A_m,
\]

where every `A_j` is finite and carries a fixed total order.  The fields may include the physical denominator address, primitive direction, board anchor, finite role, operation label, current owner status, support atom and occurrence-lineage label.

Let

\[
 Z=(v_0,e_0,v_1,e_1,\ldots,v_{\ell-1},e_{\ell-1},v_0)
\]

be a simple directed cycle of distinct vertices.  An edge retains its full decorated operation address, so parallel edges remain distinct.

## BDA5bg -- canonical least changing field -- PROVED

If `Z` is nonconstant, there is a least coordinate

\[
 j(Z)=\min\{j:x_j\text{ is nonconstant on }Z\}.
\]

Let

\[
 a(Z)=\min\{x_j(v):v\in V(Z)\}.
\]

Then the cycle contains both an edge leaving the fibre `x_j=a` and an edge returning to that fibre.

### Proof

The selected coordinate is nonconstant, so the cycle contains a vertex with value `a` and a vertex with a different value.  Traversing the cyclic word from an `a`-vertex therefore eventually leaves the fibre.  Because the word returns to its initial vertex, it later re-enters the same fibre. QED.

## BDA5bh -- canonical leave/restore excursion -- PROVED

Choose the least edge index, in the fixed cyclic edge order, whose tail has `x_j=a` and whose head has `x_j!=a`.  Rotate the cycle so this edge is first.  Let `r` be the first later step at which the selected coordinate returns to `a`.

The resulting subword

\[
 v_0\to v_1\to\cdots\to v_r
\]

satisfies

\[
 x_j(v_0)=x_j(v_r)=a,
 \qquad
 x_j(v_t)\ne a\quad(1\le t<r).
\]

It is the **least-field restoration excursion** of `Z`.  Its restoration gate is the final decorated edge `v_{r-1}->v_r` together with `(j,a)`.

### Proof

BDA5bg supplies at least one exit.  The chosen rotation makes the least exit first.  Finite cyclic return supplies a first later `a`-vertex.  Minimality of `r` gives the strict avoidance statement for the interior vertices. QED.

The address is canonical after fixing the coordinate orders, value orders, edge order and cycle rotation convention.

## BDA5bi -- monotone physical fields forbid recurrence -- PROVED

Suppose the selected field `x_j` is monotone along every legal transition of the epoch, in either one fixed direction, and equality is the only way to return to a previous value.  Then no nonconstant directed cycle can have `j(Z)=j`.

### Proof

The restoration excursion leaves `a` and later returns to `a`.  A monotone sequence returning to its starting value is constant throughout, contradicting the strict interior avoidance in BDA5bh. QED.

This includes strict effective-denominator descent, monotone support deletion, monotone registry growth and any declared one-sided valuation field.

## Restoration resources

Let `E_rec` be the finite set of decorated legal edges which restore some field value after a nonempty excursion.  For `e in E_rec`, retain the exact restoration address

\[
 \rho(e)=(j,a,e).
\]

Parallel operation edges have distinct addresses.

## BDA5bj -- capacity-one restoration tickets close fixed-profile cycles -- PROVED UNDER THE RESTORATION-TICKET CONTRACT

Assume every nonimproving, nondescending and physically possible recurrent cycle may traverse its canonical restoration gate only when the ticket `rho(e)` is unused, and traversal consumes that ticket permanently in the epoch.

Then at most

\[
 \boxed{|E_{\rm rec}|}
\]

such recurrent cycle traversals occur.  More sharply, if only a subset `R subseteq E_rec` is reachable at the fixed denominator and outer profile, the bound is `|R|`.

### Proof

Every recurrent nonconstant cycle has one canonical restoration gate by BDA5bh.  The contract assigns a distinct unused capacity-one resource to each permitted traversal and forbids reuse.  The finite reachable restoration-edge stock bounds the number of traversals. QED.

## BDA5bk -- least-field cycle router -- PROVED UNDER THE COMPLETE-PROFILE CONTRACT

Every simple same-denominator recurrent physical-profile cycle has one of the following continuations:

1. its least changing field is monotone, so the cycle is impossible by BDA5bi;
2. its canonical restoration edge carries current payment;
3. the restoration edge strictly lowers a declared denominator, valuation, support or depth potential;
4. the restoration is physically impossible under the exact occurrence/legality address;
5. the restoration consumes one capacity-one ticket from `E_rec`;
6. or a denominator, direction, board anchor, role, operation, owner, support, lineage, legality or context field omitted from the address changes, giving an explicit outer reset.

Consequently the remaining BDA6 cycle obligation is edge-local.  It is enough to discharge the canonical restoration gate of each reachable least-field class; no proof must analyse an arbitrary diffuse cycle word as a whole.

### Proof

Apply BDA5bg--BDA5bh.  Monotone fields use BDA5bi.  The other declared outcomes are mutually nonexclusive valid continuations for the exact restoration edge.  If none applies while the physical interpretation changes, completeness fails and the least omitted field is returned as an outer reset. QED.

## Updated BDA frontier

The cycle-space chord of BDA5bc and the least-field restoration gate solve different localization problems:

- a chord gives a small global resource stock of size `E-V+c`;
- a restoration gate identifies the exact physical field whose recurrence must be paid or ticketed.

The remaining arithmetic work is to prove payment, descent or impossibility for the reachable restoration classes, especially balanced-floor rank-two/rank-three profiles and unresolved ordinary-role occurrences.

## Finite check

`scripts/verify_bda_least_field_restoration.py` exhausts and samples finite product-state cycles, verifies the canonical leave/restore excursion, checks monotone impossibility and audits capacity-one restoration-ticket counting.