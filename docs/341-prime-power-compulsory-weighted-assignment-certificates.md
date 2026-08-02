# Compulsory weighted assignment certificates are complete row artifacts

Fix a finite response host. Every allowed response edge carries all declared
return, selector, collision, local-line, interface and geometric child
coefficients. Each coefficient is evaluated against one positive child weight
before inner or outer assignment optimization.

## Theorem CMR1902 -- PROVED

A complete response table enumerates every allowed response and every compulsory
labelled coefficient attached to it.

## Theorem CMR1903 -- PROVED

Every declared return, selector, collision, local-line, interface and geometric
coefficient is compulsory. Omission is a certificate failure.

## Theorem CMR1904 -- PROVED

Every compulsory coefficient has exactly one positive child-weight lookup before
it contributes to the weighted response score.

## Theorem CMR1905 -- PROVED

Every rank-two and rank-three term has complete compatible inner-dual coverage.

## Theorem CMR1906 -- PROVED

The outer assignment dual is checked on every allowed edge against the complete
weighted edge score.

## Theorem CMR1907 -- PROVED

The parent row is strict exactly when the certified outer objective has positive
slack below the parent weighted budget.

## Theorem CMR1908 -- PROVED

A finite corruption audit rejects missing terms, missing weights, incomplete
inner duals, omitted allowed edges, infeasible outer potentials and nonpositive
row slack.

## Corollary CMR1909 -- PROVED

The certificate artifact consists of the complete response table, positive
weight map, all inner duals, one outer dual and a positive integer or rational
slack. Format completeness is not a claim that every recurrent state already
has such an artifact.

The executable completeness and corruption checks are implemented in
[`scripts/verify_prime_power_compulsory_weighted_assignment.py`](../scripts/verify_prime_power_compulsory_weighted_assignment.py).
