# Acyclic multi-step elimination of auxiliary states

CMR2214--CMR2221 eliminate one auxiliary layer directly into nonauxiliary states. This
chapter permits auxiliary targets provided the complete expansion graph is finite and
acyclic, and computes the fully expanded nonauxiliary obligations exactly.

## Theorem CMR2238 — PROVED AS AN INTERFACE

The expansion table must cover exactly the recursive closure of all auxiliary states that
occur with positive coefficient in a recurrent response vector. No unused expansion and no
missing recursively referenced auxiliary are accepted.

## Theorem CMR2239 — PROVED

The auxiliary dependency graph has an edge `a -> b` when the expansion of auxiliary `a`
contains auxiliary target `b`. The graph must be acyclic; a canonical topological order is
published.

## Theorem CMR2240 — PROVED

Every local expansion satisfies the common-weight domination inequality

\[
\boxed{f_a+\sum_t m_{a,t}w_t\le w_a,}
\]

where targets may be auxiliary or nonauxiliary. Local weighted load and local slack are
checked exactly.

## Theorem CMR2241 — PROVED

Reverse topological substitution produces one effective expansion

\[
a\rightsquigarrow F_a+\sum_{u\text{ nonauxiliary}}M_{a,u}u
\]

for every eliminated auxiliary. All effective multiplicities and fixed loads are
nonnegative integers, and the effective weighted load is at most `w_a`.

## Theorem CMR2242 — PROVED

No response-local destroyed credit may be routed to any auxiliary coordinate in the full
recursive elimination closure. Credit on nonauxiliary coordinates is retained unchanged.

## Theorem CMR2243 — PROVED

Every response vector is fully substituted into a nonauxiliary vector and a signed net
fixed offset. Responsewise,

\[
\boxed{L_{\rm full}(Q)\le L(Q),\qquad \mu_{\rm full}(Q)\ge\mu(Q).}
\]

The transformed selector, minimizer count and exact margin are recomputed after complete
elimination.

## Theorem CMR2244 — PROVED WITH HONEST BOUNDARY

If the source block is a complete strict SCC and every transformed row remains strict,
acyclic elimination preserves strictness under the same common weights. This is weighted
algebraic substitution only; the real proof must still establish every auxiliary
transition and multiplicity semantically.

## Corollary CMR2245 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_acyclic_auxiliary_elimination.py` validates recursive expansion
coverage, DAG structure, local and effective domination, zero auxiliary credit, complete
response substitution and strictness preservation.

The checker was syntax-compiled in the publication environment. No genuine expansion DAG
is yet supplied.
