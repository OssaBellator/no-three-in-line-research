# Simultaneous witness-bound credit nonreuse

CMR2166--CMR2173 make routed credit injective inside one alternative response. This
chapter fixes the separate global audit needed when several selected rows are active in
one declared execution.

## Theorem CMR2198 — PROVED AS AN INTERFACE

A selected execution record fixes an execution ID and a canonically ordered family of
active rows. Each row declares an operation-instance ID, a resource-scope ID and one
validated witness-bound routing certificate.

The response used by the audit is not user-selected: it is the deterministic response
selected by the embedded recurrent-row margin certificate.

## Theorem CMR2199 — PROVED

For a literal destroyed triple `d` in resource scope `s`, define the global resource key

\[
\boxed{R(s,d)=\operatorname{SHA256}(s,\text{canonical point triple of }d).}
\]

Thus two rows in the same scope referring to the same physical point triple identify the
same resource even when their local point indices or destroyed IDs differ.

## Theorem CMR2200 — PROVED

For a target witness `w` in operation instance `o`, define the global obligation key

\[
\boxed{O(o,w)=\operatorname{SHA256}(o,\text{witness ID},\text{child}).}
\]

This distinguishes equal-looking obligations in genuinely different operation instances
while identifying repeated payment of one witness obligation inside the same instance.

## Theorem CMR2201 — PROVED

Every selected route assignment is expanded to one exact record containing its local
destroyed ID, witness ID and child together with its global resource and obligation IDs.
The selected assignment family is fully digested.

## Theorem CMR2202 — PROVED

Across the complete declared simultaneous execution,

\[
\boxed{R(s,d)\text{ is injective over selected assignments}.}
\]

No literal destroyed resource in one scope may pay two selected row obligations.

## Theorem CMR2203 — PROVED

Across the same execution,

\[
\boxed{O(o,w)\text{ is injective over selected assignments}.}
\]

No child-bearing witness obligation may be paid more than once.

## Theorem CMR2204 — HONEST SCOPE BOUNDARY

The certificate proves nonreuse only relative to the supplied execution partition,
operation-instance IDs and resource scopes. It does not prove that two differently named
scopes are physically independent or that the selected rows are the genuine simultaneous
obligations of the parent theorem.

## Corollary CMR2205 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_simultaneous_credit_nonreuse.py` validates every embedded route,
selects the deterministic row responses, reconstructs global resource and obligation IDs,
requires both global injectivity conditions and publishes exact scope and child censuses.

The script was syntax-compiled in the publication environment.
