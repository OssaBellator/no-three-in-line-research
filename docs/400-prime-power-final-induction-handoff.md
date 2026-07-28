# Final documentary handoff to an all-n induction proof

The semantic obligation DAG, typed premise artifacts and quotient refinement identify all proof
components. This chapter fixes the final six assertions that an ordinary induction proof must
review and assemble.

## Theorem CMR2374 — PROVED AS AN INTERFACE

The handoff contains exactly six assertions:

1. the complete base domain is established;
2. the nonbase recurrence covers every case;
3. state and resource invariants are preserved;
4. every recurrence branch terminates;
5. exceptional and hard-core cases are closed; and
6. the quotient conclusion translates to `D(n)=2n`.

## Theorem CMR2375 — PROVED

Each assertion has a fixed exact list of final-premise dependencies. Supplied input cannot omit
or reorder those dependencies.

## Theorem CMR2376 — PROVED

Every assertion has status `proved` or `open`, one mathematical statement, one explanatory note
and an artifact locator/digest pair exactly when declared proved.

## Theorem CMR2377 — PROVED

An assertion is effective exactly when

\[
\boxed{
\text{declared proved}\ \land\
\text{every dependent final premise is effective}.
}
\]

A handoff claim cannot bypass an open premise.

## Theorem CMR2378 — PROVED

The handoff composes the exact same obligation artifact registry, global-family skeleton and
state-equivalence evidence as the final premise and semantic-refinement certificates. It also
requires acyclic dependency-aligned artifact support.

## Theorem CMR2379 — PROVED WITH A CONDITIONAL READY FLAG

The `final_induction_handoff_ready` flag requires simultaneously:

- the CMR2342--CMR2349 final premise contract ready;
- exact typed premise-artifact coverage;
- acyclic and dependency-complete semantic artifact support;
- complete state and row semantic refinement; and
- all six handoff assertions effective.

The checker always publishes `all_n_proved_by_checker = 0`.

## Theorem CMR2380 — HONEST FINAL HANDOFF BOUNDARY

A ready handoff is an internally linked documentary proof package. It does not machine-check
ordinary mathematical reasoning or authorize a theorem claim without mathematical review.

## Corollary CMR2381 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_final_induction_handoff.py` validates the six fixed assertions and
all cross-certificate identity, premise, artifact-support and semantic-refinement gates.

The checker was syntax-compiled in the publication environment. No final induction handoff is
claimed ready.
