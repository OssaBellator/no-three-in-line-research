# Witness-bound destroyed-credit routing

CMR2142--CMR2149 introduced response-local child credit vectors bounded by the literal
destroyed-current-triple count. This chapter replaces every positive credit unit by an
explicit assignment from a literal destroyed triple to a nondeleted child-bearing
witness that actually occurs in that response.

## Theorem CMR2166 — PROVED

For one linked operation with pre-response point list `P` and removed index set `R`, the
literal destroyed triples are exactly

\[
\mathcal D(P,R)=
\{T\in\tbinom P3:T\text{ is collinear and }T\cap R\ne\varnothing\}.
\]

Each triple receives a canonical record containing its point indices, point coordinates,
removed indices, exact ID and record digest. The number of records must equal the
destroyed-current-triple count in the linked operation certificate.

## Theorem CMR2167 — PROVED

Every nondeleted owner/fate witness receives a canonical witness record containing its
rank, complete response prescription, background witness data when present, last-entering
owner, fate kind, child state, domination multiplicity when present, exact ID and digest.
Deleted witnesses are excluded because they have no child target.

## Theorem CMR2168 — PROVED

A route assignment for response `Q` is accepted only when

\[
\boxed{(d,w,c)}
\]

satisfies:

1. `d` is one of the literal destroyed-triple records;
2. `w` is one of the nondeleted witness records;
3. the witness prescription is contained in `Q`; and
4. the declared child `c` equals the witness's exact owner/fate child.

Thus a credit cannot be routed to a child that has no actual occurring child-bearing
witness in that response.

## Theorem CMR2169 — PROVED

Within one response, the route assignments are injective on both sides:

\[
\boxed{
\text{one destroyed triple is used at most once, and one target witness is paid at most once.}
}
\]

This gives a literal partial matching between destroyed triples and occurring child
witnesses.

## Theorem CMR2170 — PROVED

For every response and every child state, the number of explicit route assignments to
that child must equal the child coordinate in the CMR2142--CMR2149 response-local credit
vector. Therefore the count-only row margin and the literal witness-bound route have
exactly the same weighted credit

\[
\sum_c w_c r_c(Q).
\]

## Theorem CMR2171 — PROVED

Different responses are alternative operations. The same destroyed triple or witness may
therefore appear in route records for two different responses, but never twice inside
one response record.

The certificate publishes both the maximum routed units in one response and the total
route assignments across the complete alternative-response family. These quantities are
not interchangeable.

## Theorem CMR2172 — HONEST SEMANTIC BOUNDARY

Witness-bound routing proves that every claimed unit is attached to one literal destroyed
triple, one actual occurring nondeleted witness, and that witness's declared child state.

It still does not prove that the owner/fate manifest's state labels have their intended
external mathematical semantics, or that the same physical destruction credit may be
reused across simultaneous rows or different parent operations.

## Corollary CMR2173 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_witness_bound_destroyed_credit_routing.py` composes literal
operation geometry, owner/fate witnesses and labelled row margins, includes deterministic
synthetic route regressions, and rejects twelve independent corruptions.

The script was syntax-compiled in the publication environment. Its full deterministic
suite is embedded for repository execution.
