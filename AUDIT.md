# Independent audit checklist

This repository was assembled from an extended exploratory proof-development conversation. It contains original derivations, conditional reductions, and counterexamples. Before any theorem is cited externally, it should receive an independent line-by-line audit.

## Highest-priority proof audits

1. Candidate-only logarithmic supersaturation: verify the quantifiers on candidate hosts and the primitive-direction count.
2. Anchor-load-to-assignment-conflict conversion: verify compatibility and multiplicity factors.
3. Affine finite-direction constructions: check wrap-around representatives and the implication from toroidal fibre bounds to real lines.
4. Subgroup absorber protected-line multiset equality: check all gcd hypotheses and collision exclusions.
5. Low-syndrome hyperbola averaging: confirm secant-capacity counting treats four-point lines with the intended multiplicity.
6. Möbius secant involution: check exceptional projective points and denominator-zero cases.
7. Cycle extraction script: replace the simple DFS cycle routine with a certified ordered cycle extractor before using its empirical output in a proof.
8. Window-product theorem: distinguish congruence hyperbola membership from real line behaviour.

## Claims already protected by counterexamples

The repository records explicit structural counterexamples to synchronized block completion and wall-expansion termination. These should be retained even if later hypotheses rescue restricted versions.

## Publication policy

Until the audit is complete, use language such as “research note,” “derived lemma,” or “candidate theorem,” not “proof of the conjecture.”
