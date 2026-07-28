# Common-weight elimination of auxiliary child coordinates

Auxiliary exits may be useful in finite row construction but must eventually be replaced
by certified nonauxiliary obligations. This chapter fixes a one-step weighted elimination
surface over a common recurrent-block certificate.

## Theorem CMR2214 — PROVED AS AN INTERFACE

Every auxiliary state occurring with positive coefficient in any response vector must
have exactly one expansion record

\[
(a,f_a,\{m_{a,t}\}_{t},\text{evidence}),
\]

where `f_a` is a nonnegative fixed load and every target `t` is a known nonauxiliary state
with positive integer multiplicity `m_{a,t}`.

The expansion set covers exactly the positively used auxiliary states.

## Theorem CMR2215 — PROVED

Under the common primitive state weights, an expansion is accepted only when

\[
\boxed{f_a+\sum_t m_{a,t}w_t\le w_a.}
\]

The exact expansion load and weight slack are published. Recursive auxiliary targets are
forbidden in this one-step interface.

## Theorem CMR2216 — PROVED

No response-local destroyed credit may be routed directly to an auxiliary coordinate that
is being eliminated. This prevents retaining a subtraction of `w_a` after replacing its
positive child load by a lower-weight expansion.

## Theorem CMR2217 — PROVED

For response `Q`, every coefficient of auxiliary `a` is replaced by:

- the corresponding multiple of fixed load `f_a`; and
- the corresponding target multiplicities `m_{a,t}`.

The checker publishes the complete transformed nonauxiliary vector and fixed-load
increment for every response.

## Theorem CMR2218 — PROVED

Let `L(Q)` be the original common-weight row load and `L_elim(Q)` the transformed load.
Then responsewise

\[
\boxed{L_{\rm elim}(Q)\le L(Q)}
\]

and therefore

\[
\boxed{\mu_{\rm elim}(Q)\ge\mu(Q).}
\]

Both inequalities are checked exactly for every response in every row.

## Theorem CMR2219 — PROVED

The certificate publishes original and eliminated row minima, total load reduction,
minimum responsewise margin gain and the complete transformed response digest.

If the source block is already a complete strict SCC, one-step elimination preserves
strictness under the same common weights.

## Theorem CMR2220 — HONEST AUXILIARY BOUNDARY

The weighted inequality proves domination of the declared expansion, not its external
transition semantics. The real proof must still show that each auxiliary state genuinely
expands into the declared targets with the declared fixed cost and multiplicities.

## Corollary CMR2221 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_auxiliary_weight_elimination.py` validates exact auxiliary
coverage, nonrecursive target states, common-weight domination, zero auxiliary credit,
responsewise substitution and margin preservation.

The script was syntax-compiled in the publication environment. No genuine auxiliary
expansion table is yet supplied.
