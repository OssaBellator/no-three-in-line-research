# Cycle-space tickets for recurrent bounded-denominator profiles

**Branch:** `research/bounded-denominator-absorbers`

BDA5az--BDA5bb reduce every long same-denominator non-scalar history to a simple directed cycle in the complete polynomial physical-address graph. This note sharpens the remaining ticket stock. A ticket is not needed for every directed edge: one chord outside a spanning forest meets every cycle.

## Decorated physical transition graph

Fix one same-denominator epoch and let

\[
G_{\rm phys}=(V,E)
\]

be the finite directed multigraph of realized decorated physical transitions. Parallel edges are retained when their finite operation labels differ. Put

\[
K=|V|,\qquad E_0=|E|.
\]

Forget orientation but retain every decorated edge as a distinct multigraph edge. Let `c` be the number of connected components and choose a canonical spanning forest `F`, for example by the lexicographically least edge rule.

The set of **profile chords** is

\[
\mathcal C=E\setminus F.
\]

## BDA5bc -- every recurrent cycle contains a profile chord -- PROVED

Every directed cycle in `G_phys` contains at least one edge of `C`. Moreover

\[
\boxed{
|\mathcal C|=E_0-K+c.
}
\]

### Proof

The forest `F` contains exactly `K-c` edges. If a directed cycle used only forest edges, its underlying undirected edges would form a cycle inside a forest, impossible. Hence every directed cycle contains a chord. Subtracting `|F|=K-c` from `E_0` gives the displayed count. QED.

The number

\[
\mu=E_0-K+c
\]

is the cycle rank of the decorated physical graph.

## Canonical chord addresses

Fix a total order on `C`. For every simple directed cycle `Z`, define

\[
\chi(Z)=\min(E(Z)\cap\mathcal C).
\]

This is a complete finite address for the ticket used by the cycle router. It does not assert that the entire cycle is determined by one chord; it supplies one canonical finite resource that every cycle must expose.

## BDA5bd -- capacity-one chord tickets bound recurrent cycles -- PROVED UNDER THE CHORD-TICKET CONTRACT

Assume every nonimproving recurrent simple cycle is permitted only when its canonical chord ticket `chi(Z)` is unused, and traversal consumes that ticket permanently within the epoch.

Then at most

\[
\boxed{\mu=E_0-K+c}
\]

recurrent cycle traversals occur in the epoch.

### Proof

Every recurrent cycle consumes one chord ticket by BDA5bc. The contract forbids reusing the same ticket. There are exactly `mu` tickets. QED.

This replaces the ambient `E_0` edge-ticket stock by the cycle-space stock `mu`.

## BDA5be -- fixed-level walk bound -- PROVED UNDER THE CHORD-TICKET CONTRACT

Assume the integer potential `H` is constant along a segment of the transition history and every first repeated-vertex segment consumes a previously unused canonical chord ticket.

Then the segment has at most

\[
\boxed{K(\mu+1)}
\]

transitions.

### Proof

Cut the walk whenever the current vertex first repeats a vertex since the preceding cut. Each completed piece contains at most `K` edges: before its final edge all visited vertices are distinct. Every completed repeated-vertex piece contains a closed subwalk and therefore a simple directed cycle, so it consumes a new chord ticket. There are at most `mu` such pieces. The final piece has no repeated vertex and has fewer than `K` edges. The displayed bound follows. QED.

## BDA5bf -- nonincreasing-potential epoch bound -- PROVED UNDER THE CHORD-TICKET CONTRACT

Suppose `H` is nonnegative, integer-valued and nonincreasing, with initial value `H_0`. Under the hypotheses of BDA5be, the whole same-denominator epoch has at most

\[
\boxed{
(H_0+1)K(\mu+1)
}
\]

transitions.

### Proof

There are at most `H_0+1` constant-`H` levels. Apply BDA5be to every level and sum. QED.

## Consequence for BDA6

The remaining exact-cycle problem has been reduced further.

- The physical vertex stock is `O(L_ext n^10)`.
- The recurrent resource stock is the cycle rank `E_0-K+c`, not all decorated edges.
- Any failure of chord ticketing returns one explicit least chord whose recurrence still requires payment, descent, erasure or physical impossibility.

Thus a diffuse recurrence can no longer hide in a large edge history. It must reuse one canonical cycle-space resource.

## Finite check

`scripts/verify_bda_cycle_space_tickets.py` enumerates finite decorated directed graphs, including parallel-edge examples, constructs canonical spanning forests, checks that every simple directed cycle contains a chord and verifies the exact cycle-rank count.
