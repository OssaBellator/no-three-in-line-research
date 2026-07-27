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

The branch still does not prove the all-`n` conjecture.

## Exact blocker structure

The undeleted side-four base host has six responses. Their rank-three counts are

\[
0,0,0,1,0,4.
\]

A canonical partial-matching deletion set has positive rank-three minimum exactly
when it hits every one of the four zero-response edge sets and leaves at least one
response. The inclusion-minimal blockers are

\[
\boxed{
\{(0,2),(2,0)\},\quad
\{(0,2),(3,1)\},\quad
\{(1,3),(3,1)\}.
}
\]

Their surviving canonical supersets are exactly the eleven positive-minimum raw
hosts. Thus the hard core is an exact transversal class, not an unexplained list.

## Selected hard-core geometry

Nine hosts select `(3,0,1,2)`, whose one collinear response triple lies on

\[
x-y-1=0.
\]

Two hosts have only `(3,2,1,0)`, whose four points lie on

\[
x+y-3=0
\]

and produce all four constituent triples. Rank-three occurrence deletion with the
selected response fixed therefore has exact independent burden

\[
\boxed{9\cdot1+2\cdot4=17.}
\]

Independent uniform correction of the same eleven `S_3=-3` hosts costs 44 numerator
units. The 27-unit difference compares different policies and cannot be inserted into
a fixed-uniform theorem.

## Canonical fibre linkage

An owner/provenance fibre is linked by reconstructing its raw host from the exact
allowed-edge set. Acceptance requires:

1. the matching canonical `host_id` and record digest;
2. exact equality of the complete response list and denominator;
3. either `canonical-rank3-selector` or `declared-response` policy;
4. a selected response valid under that policy;
5. the ordered nonempty label tuple
   `(provenance, collision, local_line, interface, root, thin, crt)`; and
6. exact source, label, response-list, fibre, and linkage fingerprints.

The checker proves identity, equality and label presence. It does not prove label
semantics, execution of the parent operation, nonretained fate evidence, or recurrent
contraction.

## Active frontier

1. Wrap every actual owner/provenance source in the linkage certificate and reject
   host, response-family, policy or label mismatches.
2. Populate the true pre-response points, removed set, surviving background, entry
   order and rule-specific transition semantics for every linked fibre.
3. On the 729 zero-`m_3` raw hosts, evaluate the canonical selector against the full
   background-dependent literal delta; enumerate all responses when rank-one or
   rank-two geometry changes the minimizer.
4. On the nine one-triple blockers, prove one occurrence cancellation or a sharper
   routed certificate.
5. On the two one-response four-triple blockers, prove four units or change the
   operation, state split, weights or routing.
6. On the other 78 uniform-exceptional hosts, retain the zero-rank-three response but
   certify all background, return, interface and labelled contributions.
7. Compute direct deltas, deleted-load histograms, pool capacities and exact
   capacity/domination gap audits for every genuine operation.
8. Prove all remaining domination, transfer and state-label semantics.
9. Close every labelled recurrent row, eliminate certified auxiliaries and publish
   the global denominator-cleared CRT quotient.
