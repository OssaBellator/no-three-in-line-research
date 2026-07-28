# Exact proof-obligation closure for an all-n implication

The finite certificate surface now reaches a source-independent expected family, documented
cross-block state equivalence and a global strict-or-ranked support graph. This chapter fixes
the semantic proof obligations that remain before those interfaces could support an all-`n`
implication.

## Theorem CMR2310 — PROVED AS AN INTERFACE

The checker contains a fixed ordered dependency DAG of nineteen semantic obligations. The
obligations cover source truth and rule exhaustiveness, genuine population, geometry and
policy semantics, active-row/resource/credit semantics, closed recurrent blocks, auxiliary
expansions, cross-block identity and scale semantics, interface/rank exhaustiveness,
exceptional and hard-core closure, and the final implication from the global quotient.

The required IDs and dependency lists are code-defined and cannot be shortened by the input
certificate.

## Theorem CMR2311 — PROVED

Every obligation is recorded as

\[
(\text{ID},\text{status},\text{exact dependencies},
 \text{artifact locator/digest or open blocker},\text{note}).
\]

A `proved` declaration requires an artifact locator and digest. An `open` declaration requires
those fields to be null and must state the remaining blocker.

## Theorem CMR2312 — PROVED

Obligations are processed in topological order. An obligation is closed exactly when

\[
\boxed{
\text{declared proved}\ \land\
\text{every dependency already closed}.
}
\]

A proof claim whose prerequisite remains open therefore cannot close downstream modules.

## Theorem CMR2313 — PROVED

The certificate publishes the complete unclosed set and the current frontier: precisely the
open obligations whose dependencies are already closed. This gives an exact machine-readable
research frontier rather than an informal checklist.

## Theorem CMR2314 — PROVED

The finite-interface gate requires all of the following to refer to the same global family:

- skeleton-derived manifest and exact row bindings;
- complete spanning state-equivalence evidence;
- critical-edge acyclicity and strict-edge coverage of every support cycle; and
- the manifest-relative complete global integer family flag.

## Theorem CMR2315 — PROVED WITH A CONDITIONAL READINESS FLAG

The `all_n_implication_dossier_ready` flag is one only when the finite-interface gate passes
and the root obligation `GLOBAL_QUOTIENT_IMPLIES_ALL_N` is closed through the complete fixed
DAG.

The checker separately and permanently publishes

\[
\boxed{\texttt{all\_n\_proved\_by\_checker}=0.}
\]

## Theorem CMR2316 — HONEST PROOF BOUNDARY

A ready dossier would mean that every named obligation has a supplied artifact and all finite
certificates compose. It would not machine-verify the mathematical truth of those artifacts.
The actual all-`n` theorem may be claimed only after ordinary mathematical review establishes
the genuine rule, data, semantics and final implication.

## Corollary CMR2317 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_all_n_implication_closure.py` validates the three finite endpoint
certificates, enforces the fixed semantic dependency DAG, computes exact closure and frontier
sets, and publishes conditional readiness without ever declaring the conjecture proved.

The checker was syntax-compiled in the publication environment. With the current repository's
missing genuine semantic data, the all-`n` readiness condition remains unsatisfied.
