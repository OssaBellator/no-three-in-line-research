# Common-weight selection across populated candidate operations

CMR2206--CMR2213 publish the complete clause-generated candidate slot set for every
recurrent parent but accept a supplied selection reason. This chapter makes the selected
operation an exact common-weight minimizer across all populated candidates.

## Theorem CMR2230 — PROVED AS AN INTERFACE

Every candidate slot of a declared recurrent parent must carry one complete witness-bound
row certificate. Its parent budget and all child weights must be the exact restrictions of
the common primitive state-weight vector.

## Theorem CMR2231 — PROVED

Candidate rows must cover exactly the complete set

\[
C(p)=\{\text{clause-generated slots with parent }p\}
\]

published by the recurrent-population certificate. Missing candidate rows, duplicate rows
and rows for slots outside `C(p)` are rejected.

## Theorem CMR2232 — PROVED

Each candidate row is bound to the populated fibre assigned to its slot. Slot parent,
fibre ID, host ID, routing certificate and common-weight row data must agree exactly.

## Theorem CMR2233 — PROVED

For candidate slot `s`, define its exact policy value

\[
\lambda_s=\min_Q L_s(Q),
\]

where `L_s(Q)` is the witness-bound row load under the common global weights. The parent
policy minimum is

\[
\lambda_p^*=\min_{s\in C(p)}\lambda_s.
\]

## Theorem CMR2234 — PROVED

The deterministic selected slot is

\[
\boxed{\operatorname*{argmin}_{s\in C(p)}(\lambda_s,\text{slot ID}).}
\]

Thus exact row load is primary and canonical slot ID breaks ties.

## Theorem CMR2235 — PROVED

Every candidate receives the exact nonnegative load gap

\[
\boxed{g_s=\lambda_s-\lambda_p^*\ge0.}
\]

The certificate publishes minimizer counts, selected margins, total and maximum gaps and
the complete load-gap distribution.

## Theorem CMR2236 — HONEST POLICY BOUNDARY

This proves the common-weight minimum policy relative to the supplied complete candidate
row certificates. It does not prove that the common-weight row load is the intended
external mathematical policy, or that the clause-generated candidate universe is the
genuine exhaustive rule.

## Corollary CMR2237 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_common_weight_candidate_policy.py` validates every candidate
row, common-weight restriction, complete slot coverage, populated fibre binding, exact
minimum policy, tie-break and all candidate gaps.

The checker was syntax-compiled in the publication environment. No genuine candidate-row
population is yet supplied.
