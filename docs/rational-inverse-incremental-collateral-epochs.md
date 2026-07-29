# Rational-inverse incremental collateral epochs

## Status

This note proves RI5gr--RI5gv under the exact typed repair-collateral compatibility and occurrence-faithful collateral contracts through RI5gq. It does not construct the arithmetic compatibility predicate, prove RI6, or prove the no-three-in-line conjecture.

## Setup

At one repair epoch let `R` be the selected RI repair incidences, `T` the live collateral tokens, and

\[
E=\{(r,t):\operatorname{Compat}(r,t)\}
\]

an exact dictionary computed from the complete owner/charge, arithmetic, source, certificate, defect, epoch and repair-class addresses. Let `d:R->T` be an injective compatible assignment.

At the next epoch write

\[
R'=R^\circ\sqcup\Delta R,
\qquad
T'=T^\circ\sqcup\Delta T.
\]

The unchanged sets contain exactly the records whose complete predicate inputs, physical identity, class, epoch signature and occurrence address are unchanged. Any new, deleted, relabelled or otherwise changed record is outside the unchanged block.

## RI5gr -- unchanged collateral compatibility persists -- PROVED

For every `r in R^circ` and `t in T^circ`,

\[
\boxed{\operatorname{Compat}'(r,t)=\operatorname{Compat}(r,t).}
\]

Therefore the old exact dictionary may be copied on `R^circ x T^circ` without reevaluation.

### Proof

Every deterministic predicate input is unchanged on the two records and the predicate version is unchanged. Hence its truth value is unchanged. QED.

## RI5gs -- boundary-only exact dictionary audit -- PROVED

The only pairs requiring fresh evaluation are

\[
\mathcal B=(\Delta R\times T')\sqcup(R^\circ\times\Delta T),
\]

with exact size

\[
\boxed{|\mathcal B|=|\Delta R|\,|T'|+|R^\circ|\,|\Delta T|.}
\]

If the old dictionary is exact, the unchanged block is copied, and every boundary pair is evaluated exactly, then the next dictionary is exact on `R' x T'`.

### Proof

`R' x T'` is the disjoint union of the unchanged block and the displayed boundary. Apply RI5gr on the first block and the fresh audit on the second. QED.

## RI5gt -- carried collateral matching disturbance -- PROVED

Restrict `d` to unchanged incidences whose assigned collateral tokens remain unchanged. Let

\[
a=|\Delta R|,
\qquad
b=|\{r\in R^\circ:d(r)\notin T^\circ\}|.
\]

The restriction is a compatible next-epoch matching and leaves at most

\[
\boxed{u=a+b}
\]

incidences unmatched.

### Proof

Restriction preserves injectivity and RI5gr preserves every retained edge. Exactly `|R^circ|-b` unchanged incidences remain assigned, while `R'` contains `|R^circ|+a` incidences. QED.

## RI5gu -- bounded reaugmentation or typed Hall core -- PROVED

In the exact next-epoch dictionary, exactly one continuation holds:

1. a complete collateral assignment exists and is reached from the carried matching using at most `u` augmenting paths;
2. no complete assignment exists, its maximum-matching deficit satisfies `1<=delta<=u`, and the preceding typed Hall-core machinery returns the canonical deficient collateral class, saturated old neighborhood and missing-compatibility rectangle;
3. one supposedly unchanged owner/charge, arithmetic, epoch, occurrence or predicate-version field is false.

### Proof

Every augmentation raises matching size by one, and the carried matching leaves at most `u` incidences unmatched. If saturation is impossible, that matching already proves maximum deficit at most `u`. QED.

## RI5gv -- recurrent RI collateral router -- PROVED UNDER THE EPOCH CONTRACT

For a sequence of RI repair epochs, let `B_j` be the changed pair boundary and `u_j` the carried disturbance. Exact dictionaries and compatible assignments can be maintained with at most

\[
\boxed{\sum_j|B_j|}
\]

new compatibility evaluations and at most

\[
\boxed{\sum_j u_j}
\]

augmenting paths. Matching maintenance creates no collateral mass; actual owner/charge debits remain governed by the occurrence-faithful conservation ledger.

Every failure has a first exact form: a missing or spurious boundary edge, false unchanged declaration, omitted arithmetic field, stale epoch, relabelled address, repeated collateral debit, or a canonical Hall core of deficit at most the current `u_j`.

## Corrected RI6 frontier

Recurrent typed collateral assignment is now charged to physical record churn rather than the full compatibility product. Remaining work is to bound actual RI churn, construct the arithmetic predicate on the audited boundary, and discharge the returned collateral Hall cores or source-ledger failures.

## Finite check

`scripts/verify_ri_incremental_collateral_epochs.py` generates exact typed compatibility graphs, mutates incidence and collateral records, verifies unchanged-edge persistence and boundary reconstruction, and checks the carried-matching and deficit bounds.