# Final implication-premise contract

The nineteen semantic obligations describe the proof modules. This chapter fixes the ordinary
mathematical premises that must be assembled into the final implication from the global
quotient to `D(n)=2n`.

## Theorem CMR2342 — PROVED AS AN INTERFACE

The final contract contains exactly ten premises:

1. complete base cases;
2. exhaustive recurrence;
3. preserved state invariants;
4. sound operation selection;
5. sound resource and credit accounting;
6. recurrent-block and auxiliary contraction;
7. sound cross-block assembly;
8. exceptional and hard-core closure;
9. termination; and
10. translation of the quotient conclusion to `D(n)=2n`.

## Theorem CMR2343 — PROVED

Each premise has a fixed exact list of semantic obligation dependencies. A premise may not be
made effective while any required obligation remains unclosed.

## Theorem CMR2344 — PROVED

Every premise has status `proved` or `open`, one proof mode, one artifact locator/digest pair
when proved, and one explanatory note. Open premises require null artifact fields.

All nontermination premises use proof mode `direct`.

## Theorem CMR2345 — PROVED

The termination premise admits three explicit modes:

1. `edgewise-lex`;
2. `semantic-multiset`; or
3. `semantic-well-founded`.

The first mode is effective only when the CMR2334--CMR2341 edgewise certificate is complete.
The semantic modes require an external proof artifact and do not pretend that the stronger
edgewise property is necessary.

## Theorem CMR2346 — PROVED

For every premise, the checker reconstructs declared status, dependency closure, proof-mode
readiness, effective closure and the exact list of open semantic dependencies.

## Theorem CMR2347 — PROVED

The `final_implication_contract_ready` flag requires simultaneously:

- the CMR2310 closure dossier ready;
- exact typed artifact coverage;
- a closed root blocker schedule; and
- all ten implication premises effectively closed.

The checker always publishes

\[
\boxed{\texttt{all\_n\_proved\_by\_checker}=0.}
\]

## Theorem CMR2348 — HONEST FINAL BOUNDARY

A ready contract is a complete, internally linked proof dossier. It does not machine-verify
ordinary mathematical reasoning, source truth or the final implication. Human-readable proof
artifacts still require mathematical review.

## Corollary CMR2349 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_final_implication_premise_contract.py` validates the ten fixed
premises and their composition with closure, artifact, blocker and termination certificates.

The checker was syntax-compiled in the publication environment. No final implication dossier
is claimed ready.
