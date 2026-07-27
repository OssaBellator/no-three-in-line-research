# Changed-signature cycle extraction for sparse swap recycling

**Branch:** `research/sparse-algebraic-spread`

SAS5gq--SAS5gt show that composed-only output becomes current-only payment when the same operation square is viewed from the installed composed state. Therefore any later composed-only return must change an exact operation or record field. This note turns those changes into a finite cycle and chord-ticket interface.

## Complete recycling signature

Under the existing finite-address and realization contracts, let a recycling state retain the complete signature

\[
\sigma=
(\text{operation square},
\text{creator/opposite orientation},
\text{word label},
\text{physical record address},
\text{boundary role},
\text{base-state table fields}).
\]

Let `Sigma_rec` be the resulting finite signature dictionary and put

\[
K_{\rm rec}=|\Sigma_{\rm rec}|.
\]

Every physically realized recycling step is a directed edge between two signatures. Parallel edges retain distinct finite legality or operation labels.

## SAS5gu -- finite changed-signature cycle extraction -- PROVED

Every recycling trajectory with at least `K_rec` transitions contains a closed subwalk and hence a simple directed signature cycle of length at most `K_rec`.

### Proof

A trajectory with `K_rec` edges visits `K_rec+1` signatures, so two are equal. The segment between equal occurrences is a closed directed walk. Repeatedly erase internal closed subwalks until no internal signature repeats. The result is a simple directed cycle and has at most `K_rec` edges. QED.

## SAS5gv -- composed-only recurrence has a genuine field change -- PROVED

A composed-only record cannot form a same-signature self-loop.

More precisely, if the exact operation square and all record-assignment fields are retained after installing the composed move, its table changes from

\[
(0,0,0,1)
\]

to

\[
(1,0,0,0).
\]

Therefore a later composed-only interpretation must change at least one field of `sigma`. Every composed-only signature cycle has length at least two and contains a changed-field edge.

### Proof

This is the table-reversal involution of SAS5gq--SAS5gs. Retaining the same signature forces the reverse-square interpretation, under which the record is current-only. QED.

## Cycle-space tickets

Let the realized decorated signature graph have `K` vertices, `E` edges and `c` underlying connected components. Choose a canonical spanning forest after forgetting orientation but retaining parallel decorated edges. Put

\[
\mu_{\rm rec}=E-K+c.
\]

## SAS5gw -- every recycling cycle exposes a chord ticket -- PROVED

Every directed signature cycle contains an edge outside the spanning forest. The number of such chords is exactly

\[
\boxed{\mu_{\rm rec}=E-K+c.}
\]

If every nonimproving recurrent cycle consumes the least unused chord on that cycle, at most `mu_rec` recurrent cycle traversals occur.

### Proof

A forest contains no undirected cycle, so every directed cycle must use a nonforest edge. A spanning forest has `K-c` edges, giving the count. Capacity-one least-chord tickets are distinct across permitted recurrent traversals by contract. QED.

## SAS5gx -- corrected changed-signature frontier -- PROVED UNDER THE FINITE-SIGNATURE AND CHORD-TICKET CONTRACTS

Every composed-output recycling trajectory has one of four exact outcomes.

1. **Immediate reverse payment:** the same operation square is retained and the bank is current-only.
2. **New signature:** a previously unseen complete recycling signature is entered.
3. **Simple recurrent cycle:** one exact changed-signature cycle of length between `2` and `K_rec` is returned.
4. **Contract failure:** one finite legality, incidence, record, boundary or interaction-independence field fails.

Under capacity-one chord tickets, the recurrent-cycle branch has the explicit budget `mu_rec`.

Thus repeated composed-only recycling is no longer a diffuse trajectory. Remaining work is cycle-local payment/descent and the legality or barrier outputs attached to one exact changed-signature cycle.

## Finite check

`scripts/verify_sparse_changed_signature_cycles.py` exhausts finite signature walks, extracts bounded simple cycles, verifies the composed-only table reversal and checks the spanning-forest chord count on finite signature graphs.
