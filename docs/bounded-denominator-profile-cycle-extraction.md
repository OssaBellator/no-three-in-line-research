# Polynomial extraction of recurrent bounded-denominator profile cycles

**Branch:** `research/bounded-denominator-absorbers`

BDA5av--BDA5ay place every determinant-realized, board-anchored, finite-role same-denominator profile in a dictionary of size `O(L_ext n^10)`. This note turns that dictionary bound into an explicit cycle and ticket interface. It does not manufacture payment for a recurrent cycle; it proves that recurrence cannot remain an unstructured infinite history.

## Complete physical profile graph

Fix one same-denominator epoch. Let `V_phys` be the complete physical address set supplied by BDA5ay, including the denominator, primitive direction pair, scalar residue, board anchor and finite external role word. Put

\[
K=|V_{\rm phys}|\le N_{\rm ns}^{\rm tot}=O(L_{\rm ext}n^{10}).
\]

Every realized non-scalar transition has a source profile and a target profile, so it is a directed edge of a multigraph on `V_phys`. Parallel transitions may retain different already-finite operation labels, but the vertex sequence alone is enough for cycle extraction.

## BDA5az -- polynomial recurrent-cycle extraction -- PROVED

Every physical same-denominator transition history containing at least `K` edges contains a closed subwalk. Every closed subwalk contains a simple directed cycle of length at most `K`.

Consequently, a nonterminating same-denominator history yields one exact simple cycle whose vertices all belong to the BDA5ay polynomial address dictionary.

### Proof

A history with `K` edges has `K+1` visited vertices. Since there are only `K` profiles, two visited vertices are equal. The segment between their two occurrences is a closed directed walk. If an internal vertex repeats, delete the closed segment between its first two occurrences. Repeating this deletion terminates and leaves a closed walk with no repeated internal vertex, hence a simple directed cycle. Its number of edges is at most the number `K` of vertices. QED.

## Directed profile tickets

Call a directed profile edge **decorated** when it also retains every finite operation field needed to reconstruct the local move. If the finite operation alphabet has size `L_op`, the total decorated directed-edge stock is at most

\[
\boxed{E_{\rm phys}\le L_{\rm op}K^2.}
\]

The bound is deliberately ambient: legality and arithmetic compatibility only reduce the stock.

## BDA5ba -- capacity-one edge-ticket termination -- PROVED UNDER THE EDGE-TICKET CONTRACT

Assume that within one same-denominator epoch every nonimproving non-scalar transition does one of the following:

1. strictly decreases an integer potential `H`;
2. uses a decorated directed profile edge that has not been used earlier in the epoch; or
3. terminates through an already proved absorber, pivot or impossibility output.

If initially `H=H_0`, then the epoch has at most

\[
\boxed{H_0+E_{\rm phys}}
\]

nonterminal transitions.

### Proof

A strict decrease of the nonnegative integer `H` occurs at most `H_0` times. Every transition of type 2 consumes a distinct capacity-one ticket from a stock of size at most `E_phys`. A transition of type 3 stops the epoch. Summing the two finite budgets proves the bound. QED.

## BDA5bb -- corrected same-denominator recurrence frontier -- PROVED

Under the physical realization and finite-operation contracts, every remaining same-denominator obstruction has one of three exact forms.

1. **Realization failure:** some required anchor, direction, denominator or role is not reconstructed by the BDA5ay physical dictionary.
2. **New-edge history:** the epoch is bounded by the explicit decorated edge stock.
3. **Recurrent simple cycle:** one exact simple directed cycle of length at most `K` repeats after all new-edge tickets are exhausted.

Thus the remaining BDA6 task is cycle-local: pay, descend, erase or ticket one explicit polynomially addressed simple cycle. No diffuse same-denominator history remains.

### Proof

BDA5ay gives the complete vertex stock. BDA5az extracts a simple cycle whenever a history is longer than the vertex stock. Before repetition, every newly used decorated edge consumes one member of the finite edge stock. The only alternative is failure of one of the reconstruction contracts. QED.

## Finite check

`scripts/verify_bda_profile_cycle_extraction.py` exhausts all walks slightly longer than the vertex stock for profile alphabets through size five, extracts a simple directed cycle, checks its length bound and verifies the `K^2` directed edge-ticket stock.
