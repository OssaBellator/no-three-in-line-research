# Contributing

This is research on an open problem. Correctness takes priority over apparent progress.

## Required labels for mathematical claims

Every new theorem or lemma should be marked:

- `PROVED`
- `PROVED UNDER HYPOTHESES`
- `CONDITIONAL`
- `HEURISTIC`
- `REFUTED`

## Proof standard

A proof should:

1. define all objects locally;
2. distinguish Euclidean collinearity from congruence-mod-\(p\) collinearity;
3. state boundary and wrap-around assumptions;
4. track whether a switch is a signed formal trade or an executable binary trade;
5. specify whether rows/columns and protected directions are preserved exactly;
6. identify every use of randomness and the probability space;
7. include a finite check when arithmetic edge cases are plausible.

## Useful computational contributions

- exhaustive search for small primes and block sizes;
- enumeration of Möbius cycles and their window-product profiles;
- counterexample search for proposed expansion inequalities;
- empirical distributions of secant-shadow loads;
- exact CSP/SAT encodings of orbit block states.

## Do not

- label a conditional implication as a proof of \(D(n)=2n\);
- silently replace real grid lines by toroidal fibres;
- assume modular collinearity implies real collinearity;
- assume a large latent secant bank is a bank of currently destroyed defects;
- discard failed lemmas without recording the counterexample.
