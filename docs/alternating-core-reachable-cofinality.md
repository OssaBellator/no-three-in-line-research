# Alternating-core reachable cofinality by fair overflow expansion

## Status

This note keeps AC as the sole active research focus and proves AC5kb--AC5kg. It discharges the cofinality interface of AC5jb and AC5js for trajectories reachable from one chosen physical AC initial state. The tower need not enumerate every formally possible finite state. It must expose every finite reachable trajectory prefix, and the total deterministic operation compiler makes this an exact fair-queue statement.

The result remains contract-qualified. It does not construct the actual physical reachable graph, prove fairness of an external implementation, prove the rank or exceptional-stock contracts, prove AC6, or prove the no-three-in-line conjecture.

## Reachable operation contract

Fix one physical initial state `v_0`, one schema version, fixed finite operation and interpretation dictionaries, and the canonical box tower of AC5iw. Every operation address at an interior state has a complete deterministic physical successor record before cap truncation.

For an operation `o` at state `v`, let

\[
s(v,o)=(s_1,\ldots,s_d)
\]

be the complete finite vector of all capped successor coordinates: resources, balances and the tail coordinate. This vector is retained even when AC5iu reports only the least upper-bound failure first.

A noninternal operation is **expandable** exactly when it is otherwise legal, stays in the fixed schema, is not terminal, shortage, amplification, monotone escape or reset, and has a finite successor vector.

## AC5kb -- full successor exposure vector -- PROVED

For every expandable boundary operation, the complete operation record determines the unique least cap vector

\[
L^+(v,o)_i=\max(L_i,s_i(v,o))
\]

that makes this exact operation internal.

After enlarging to any cap vector dominating `L^+(v,o)`, the old source state and operation address produce the identical physical successor `s(v,o)`. If several coordinates exceed their old caps, the full vector resolves them simultaneously; repeatedly returning only the least coordinate is an equivalent finite refinement.

The compiler returns the least missing successor coordinate, omitted physical choice or inconsistent increment if the full vector cannot be reconstructed.

### Proof

The operation address fixes every update before cap comparison. Membership of the successor in a box is coordinatewise domination. AC5iw preserves the source and operation interpretation under cap enlargement. QED.

## AC5kc -- fair reachable-overflow queue -- PROVED

At box level `n`, maintain the ordered queue `Q_n` of expandable overflow records whose source states are already interior. A queue policy is **fair** when every record that remains pending is selected after finitely many later selections.

When record `(v,o)` is selected, enlarge the box to dominate `L^+(v,o)`, retain all old interior certificates, insert its exact successor, and expose all operations from newly interior states. Duplicate records with the same source and operation address are one queue entry.

For every finite set of currently pending records, processing each coordinate directly to the maximum required value drains that set after finitely many cap updates. The shell increments telescope exactly as in AC5ja.

A record omitted from the queue, duplicated under a new address, or postponed forever has a canonical source, operation and queue-age witness.

### Proof

Each selected finite successor vector requires a finite componentwise enlargement and then becomes internal by AC5kb. Finite current batches drain by AC5iz--AC5ja. Fairness is exactly the assertion that no persistent entry is starved. QED.

## AC5kd -- reachable-prefix cofinality -- PROVED UNDER FAIRNESS

Let

\[
v_0\xrightarrow{o_0}v_1\xrightarrow{o_1}\cdots\xrightarrow{o_{\ell-1}}v_\ell
\]

be any finite physical trajectory using only internal or expandable operations and remaining in the fixed schema. Under the fair queue policy, some box contains every state and edge of this trajectory.

Consequently the nested tower is cofinal for the physical graph reachable from `v_0`.

### Proof

Induct on the trajectory length. The initial state lies in the first box. Suppose a box contains the prefix through `v_i`. If the next operation is already internal, it contains `v_(i+1)`. Otherwise its complete expandable record is placed in the queue. Fairness eventually selects it, and AC5kb inserts the identical successor. A finite trajectory requires only finitely many such selections, so one later box contains its whole prefix. QED.

This is the exact cofinality needed to rule out an infinite trajectory from `v_0`; unreachable formal states need not be enumerated.

## AC5ke -- reachable graph and certificate preservation -- PROVED

Let `G_n` be the interior graph reachable from `v_0` inside box `n`. Under fixed-schema fair expansion:

1. `G_n` is an induced certified subgraph of `G_(n+1)` on its old reachable vertices;
2. every old compatibility value, edge record, rank value, template certificate and physical exceptional address remains unchanged;
3. a previously expandable operation either becomes its exact interior edge or remains the same pending operation until a sufficient enlargement;
4. terminal and permanent obstruction records remain terminal or permanent.

Thus the reachable direct-limit graph

\[
G_{\rm reach}=\bigcup_n G_n
\]

is a well-defined physical graph, and every finite path in it lies in one level.

### Proof

AC5iw gives no regression on old interiors, AC5jy preserves the exception registry, and AC5kb fixes the successor of every refined overflow operation. Reachable-prefix cofinality gives the finite-path statement. QED.

## AC5kf -- initial-state ordinal termination certificate -- PROVED

Assume, on the fair reachable tower:

1. repair ranks extend overlap-preservingly;
2. every internal reachable edge passes AC5jp;
3. the fixed global exceptional universe passes AC5jv--AC5jz;
4. every nonexpandable boundary record passes AC5jh.

Then no infinite nonterminal physical trajectory starts at `v_0`.

### Proof

If such a trajectory existed, every finite prefix would lie in one reachable box by AC5kd. Hence it defines an infinite path in `G_reach`. AC5jz gives finitely many exceptional edges, and all remaining edges strictly decrease the ordinal of AC5jq. AC5js gives the contradiction. QED.

No absolute cofinality over unreachable states and no uniform coefficient bound are required.

## AC5kg -- exact reachable-cofinality failure router -- PROVED

Failure of the fair reachable construction returns the first of:

1. an expandable operation with an omitted or inconsistent successor coordinate;
2. a reachable overflow record not inserted into the queue;
3. a persistent queue record starved by the selection policy;
4. a cap change that alters schema, dictionaries or physical interpretation;
5. an operation falsely labelled terminal, shortage, escape or reset although its fixed-schema finite successor exists;
6. a duplicate or relabelled source-operation queue address;
7. a shell rank, edge-stratification, exception-ledger or boundary-certificate failure from the earlier compilers.

A physical successor requiring an actually infinite coordinate or a genuinely new dictionary belongs to a different schema boundary and is returned explicitly rather than treated as cap overflow.

### Proof

The list is the ordered negation of the complete successor, queue fairness, fixed-schema and prerequisite-certificate hypotheses. AC5kb--AC5kf cover every accepted branch. QED.

## Deterministic audit

`scripts/verify_ac_reachable_cofinality.py` checks 2,500 generated reachable systems. It verifies:

- full finite successor vectors;
- fair least-record expansion;
- exact inclusion of every reachable finite state;
- telescoping shell counts;
- automatic internal refinement after enlargement;
- canonical omitted-coordinate, starvation, schema-change and false-boundary witnesses.

## Main AC frontier

Only AC remains active. The remaining physical tasks are now the direct contracts of AC5kf:

1. serialize the actual reachable operation graph from the chosen AC initial state;
2. run the fair overflow queue and complete each new shell;
3. extend the repair rank over every reachable shell;
4. stratify every reachable internal edge;
5. compile the fixed global exceptional source/claim network;
6. certify every permanent boundary route;
7. apply AC5kf, or retain the first AC5kg witness as the exact AC6 obstruction.

AC6 and the global no-three-in-line conjecture remain open.
