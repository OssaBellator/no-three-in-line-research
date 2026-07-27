# Linked operation geometry and full response selectors

CMR2014--CMR2021 certify canonical fibre identity. CMR2038--CMR2061 certify exact background-dependent response selection. This chapter composes those surfaces with literal before/after operation geometry, so one object must agree on the source, survivor background, destroyed threshold and every response delta.

## Theorem CMR2062 -- PROVED

A linked operation certificate accepts only when the fibre-linkage source manifest is identical to the source used by the direct response-delta and response-pool bundle. Thus allowed edges, response family, entry order, witness fates and source fingerprint are shared exactly.

## Theorem CMR2063 -- PROVED

The background-selector point list must equal, in order, both the linked source background and the point list surviving the direct certificate's declared removals.

## Theorem CMR2064 -- PROVED

Let `T` be the literal number of current triples destroyed by the declared removal. For every response in the common response order, the composed certificate verifies

\[
\boxed{\Delta\Psi(Q)=N_B(Q)-T.}
\]

It also verifies equality of the independent rank-one, rank-two and rank-three counts.

## Theorem CMR2065 -- PROVED

The lexicographically first direct-delta minimizer equals the lexicographically first full background selector. Subtracting the response-independent constant `T` preserves the entire minimizer set and tie-break.

## Theorem CMR2066 -- PROVED

The linked operation is strictly improving for the real-triple potential exactly when

\[
\boxed{N_B^*<T.}
\]

The certificate records `N_B^*`, `T`, the exact minimum delta and the selected response.

## Theorem CMR2067 -- PROVED

Let `Q_pol` be the response chosen by the linked parent policy. The exact policy penalty is

\[
\boxed{\pi_{\rm pol}=N_B(Q_{\rm pol})-N_B^*\ge0}.
\]

The policy-selected delta is `N_B(Q_pol)-T`. The policy is the deterministic full selector exactly when the responses agree, and it has minimum value exactly when `pi_pol=0`.

Policy penalty is not deletion credit, rollback distance, uniform slack or labelled routing slack.

## Theorem CMR2068 -- PROVED

A fixed 240-system suite, split evenly between canonical-rank-three and explicit declared policies, verifies:

- 2,944 complete responsewise compositions;
- 3,363 primitive witnesses;
- 819 survivor-background points;
- 589 destroyed current triples;
- 230 strictly improving full selectors;
- 90 exact policy/full-selector matches;
- 106 policies attaining the minimum value;
- total declared-policy penalty 262; and
- total raw rank-three-selector penalty 148.

The policy-penalty distribution is `[[0,106],[1,74],[2,29],[3,9],[4,14],[5,5],[6,2],[10,1]]`. These are deterministic interface tests, not empirical claims about the actual parent rule.

## Corollary CMR2069 -- PROVED

`scripts/check_prime_power_linked_operation_selector.py` validates arbitrary composed certificates and rejects fourteen independent corruptions of host identity, labels, source fingerprints, removal geometry, response choices, thresholds and penalties.

Passing proves exact linkage and finite scalar geometry. It does not prove that the declared parent operation is legally executable, that state labels have their asserted semantics, or that a selected child lies in a strictly contracted labelled recurrent block.
