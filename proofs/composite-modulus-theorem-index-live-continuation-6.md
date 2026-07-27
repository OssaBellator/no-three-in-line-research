# Live composite-modulus theorem ledger continuation 6

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `composite-modulus-theorem-index-live-continuation-3.md` through CMR1629;
- `composite-modulus-theorem-index-live-continuation-4.md` through CMR1829;
- `composite-modulus-theorem-index-live-continuation-5.md` through CMR1997; and
- this file from CMR1998 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR1998--2005 | Exact side-four base response table, zero-response blocker criterion, three inclusion-minimal transversals, complete eleven-host blocker census, surviving positive-response classification, exact hard-core equivalence, and executable blocker endpoint | PROVED; six base responses split four zero and two positive; three minimal blockers generate exactly eleven canonical hosts with size distribution 3/6/2 and minimum distribution 9/2; ten corruptions rejected | `docs/353-prime-power-rank-three-zero-response-blockers.md` |
| CMR2006--2013 | Two selected hard-core responses, exact line support, selected-response occurrence-deletion minimum, 17-unit deterministic burden, 44-unit uniform comparison, 27-unit policy difference, two-host irreducible raw geometry, and executable correction endpoint | PROVED; eleven hosts split nine one-triple and two four-triple selectors on two exact lines; deterministic/uniform totals 17/44; ten corruptions rejected | `docs/354-prime-power-rank-three-hard-core-correction.md` |
| CMR2014--2021 | Injective allowed-edge host identification, host-ID and record-digest linkage, complete response-list equality, policy-separated response selection, mandatory parent label tuple, source/fibre identity, exact linkage claims, and executable fibre-linkage endpoint | PROVED; 300 linked fibres containing 3,815 response records and 4,096 witnesses accepted, split 150 canonical and 150 declared policies; twelve corruptions rejected | `docs/355-prime-power-raw-host-fibre-linkage.md` |
| CMR2022--2029 | Finite hard-core rollback, exact 10/1 distance split, unique distance-two host, 21 minimum options, restored zero-response and uniform-slack census, exact 12-unit independent rollback distance, policy separation from occurrence correction, and executable rollback endpoint | PROVED; ten hosts need one rollback edge and one needs two; 21 minimum options land in 13 restored hosts; restored slacks are 19 at -2 and 2 at -1; ten corruptions rejected | `docs/356-prime-power-rank-three-hard-core-rollback.md` |
| CMR2030--2037 | Canonical response-line records, exact rank-two and rank-three kernels, rank-one point kernel, complete line-incidence census, seven occupancy profiles, exact background response score, and executable kernel endpoint | PROVED; all 740 hosts and 9,260 responses produce 79,736 line records, 6,485 rank-three occurrences, 39 coordinate-labelled response geometries and seven profiles; ten corruptions rejected | `docs/357-prime-power-response-line-incidence-kernel.md` |
| CMR2038--2045 | Direct/kernel rank agreement, post-response identity, minimizer independence from removed prehistory, deterministic full selector, exact raw-selector penalty, instability criterion, deterministic stress census, and executable background-selector endpoint | PROVED; 400 systems with 5,077 responses and 1,260 background points checked; raw selector changes in 166 cases, has positive penalty in 160, total penalty 239; twelve corruptions rejected | `docs/358-prime-power-background-response-selector.md` |

The branch still does not prove the all-`n` conjecture.

## Exact hard-core alternatives

The eleven positive-minimum side-four hosts admit two exact but incomparable
structural currencies:

1. fixed selected-response occurrence correction: independent burden 17;
2. restoration of canonical deletion restrictions: independent minimum distance 12.

The rollback distribution is

\[
\boxed{10\text{ hosts at distance }1,\qquad1\text{ at distance }2.}
\]

The unique distance-two host is `s4-59ac56096a7f627f`. Minimum rollback restores a
zero-rank-three response but not uniform strictness: the 21 options have restored
slacks `19` at `-2` and `2` at `-1`. Rollback changes the operation and cannot be
charged as witness deletion inside the original row.

## Exact response geometry kernel

For every response `Q`, let `r_Q(L)=|Q cap L|` on every line with at least two response
points. For every background `B`,

\[
W_2(Q;B)=\sum_L\binom{r_Q(L)}2|B\cap L|,
\qquad
W_3(Q)=\sum_L\binom{r_Q(L)}3.
\]

Together with

\[
W_1(Q;B)=\sum_{q\in Q}p_B(q),
\]

this computes the exact new-triple score

\[
N_B(Q)=W_1(Q;B)+W_2(Q;B)+W_3(Q).
\]

The complete kernel digest is

\[
\texttt{b591356b800b44ae1a20c9f57cdad0782aecc43ca0a2ee699c4c0337d3010697}.
\]

## Exact background-dependent selector

For actual pre-response points `P`, removed set `R`, survivor background `B=P\setminus
R`, and destroyed count `T=|D(P,R)|`,

\[
\boxed{\Delta\Psi(Q)=N_B(Q)-T.}
\]

Therefore the response minimizing the literal delta depends only on the linked raw
host and `B`; the removed prehistory changes the sign threshold through `T`, but not
the minimizer. Let `Q_B^*` minimize `N_B` and let `Q_3^*` minimize only `W_3`. The exact
raw-selector penalty is

\[
\pi_B=N_B(Q_3^*)-N_B(Q_B^*)\ge0.
\]

A zero-rank-three response is not a complete selector certificate. The deterministic
stress suite has positive penalty in 160 of 400 systems and changes the selected
response in 166; these are regression facts, not estimates for the real fibres.

## Active frontier

1. Wrap every actual owner/provenance source in the canonical fibre-linkage certificate.
2. Populate true pre-response points, removed sets, survivor backgrounds, entry orders
   and rule-specific transition semantics.
3. Run the exact background-dependent selector on every linked fibre; use `N_B^*<T` as
   the literal improvement test once the true destroyed count is certified.
4. On the nine one-triple hard-core hosts, prove one occurrence payment, a legal
   rollback, or a sharper labelled route.
5. On the two one-response four-triple hosts, prove four units or replace the operation,
   state split, weights, route or auxiliary target.
6. Treat rollback, occurrence correction and selector penalty as separate currencies;
   transfer none across policies without a theorem.
7. Complete deleted-load histograms, pool capacities, gap audits, domination and
   transfer semantics for every genuine operation.
8. Close every recurrent labelled row, eliminate certified auxiliaries and publish the
   denominator-cleared global CRT quotient.
