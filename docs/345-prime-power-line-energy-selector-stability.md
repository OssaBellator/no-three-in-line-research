# Response selectors are stable below their exact score gap

Let a finite response family have scores `s(q)`. Suppose `q*` is the unique
minimizer and let

\[
g=\min_{q\ne q_*}(s(q)-s(q_*))>0.
\]

A background change adds response-dependent perturbations `d(q)`.

## Theorem CMR1934 -- PROVED

Selector-score change is exactly the corresponding background increment kernel
evaluated on that response.

## Theorem CMR1935 -- PROVED

If

\[
d(q)-d(q_*)<g
\]

for every competitor, `q*` remains the unique minimizer.

## Theorem CMR1936 -- PROVED

When several responses tie, the exact minimizer face is retained. A coarser
single-selector claim is invalid until a tie-breaking certificate is supplied.

## Theorem CMR1937 -- PROVED

A selector switch from `q*` to `q` requires
`d(q)-d(q*)<=-g_q`, where `g_q=s(q)-s(q*)`; equivalently the relative
perturbation must cross the exact response gap.

## Theorem CMR1938 -- PROVED

If every switch consumes at least `epsilon>0` of an accumulated nonnegative
relative-variation budget `V`, then the number of switches is at most
`floor(V/epsilon)`.

## Theorem CMR1939 -- PROVED

One selector row remains valid throughout every background interval on which
the gap inequalities stay strict.

## Theorem CMR1940 -- PROVED

Failures are retained as explicit tie faces or threshold-crossing increment
classes.

## Corollary CMR1941 -- PROVED

Selector stability is a quantitative finite certificate; it is not a global
claim that the same selector works for all backgrounds.

The gap, tie and episode-budget implications are checked in
[`scripts/verify_prime_power_line_energy_selector_stability.py`](../scripts/verify_prime_power_line_energy_selector_stability.py).
