# Alternating-core kernel coverage atlas

## Status

This note keeps AC as the sole active research focus and proves AC5ii--AC5im. It extends the restricted physical kernel of AC5id--AC5ih from one menu to a finite atlas of overlapping certified kernels.

The purpose is to advance every current AC frontier at once:

1. compatibility coverage is tracked by exact tagged-pair unions;
2. physical macro-state coverage is tracked by exact state unions;
3. transition coverage is tracked by exact certified-edge unions;
4. local dead ends may be rescued by explicit cross-kernel bridges;
5. shared payment, ticket, reset and disturbance resources are deduplicated by physical address;
6. the union graph receives one exact minimax rank and one finite episode bound.

The result remains contract-qualified. It does not enumerate the complete physical AC universe, construct all historical menu records, prove atlas coverage is complete, prove AC6, or prove the no-three-in-line conjecture.

## Atlas data

Fix one physical AC infrastructure epoch with complete schema version `v`. Let

\[
\mathcal P=(\Omega,V,T,E,H,\mathcal C)
\]

be the declared finite physical universe, where:

- `Omega` is the complete ordered set of admissible tagged compatibility pairs;
- `V` is the complete ordered physical macro-state set;
- `T subseteq V` is the terminal set;
- `E subseteq V x V` is the complete certified transition set;
- `H:V->Z_{>=0}` is the physical defect/barrier height;
- `C` is the globally addressed typed capacity table.

An atlas consists of finitely many ordered kernel templates `K_alpha`. Every template retains:

- the exact schema version;
- a template kind and complete template parameters;
- a tagged pair set `Omega_alpha` with evaluator values;
- a physical state set `V_alpha` with all retained state fields;
- a certified edge set `E_alpha` with footprints, source/target records and restart metadata;
- references to globally addressed payment, ticket, reset and disturbance entries.

The historical AC mechanisms enter through the following finite template registry.

| Template kind | Required physical records | Canonical output |
|---|---|---|
| direct exclusion | support, secant, dangerous-line, residual and new-blocker sets | total target--partner evaluator or least missing exclusion |
| layered incidence | exact layers, conditioning deletions, endpoint identities and reverse loads | union degree, threshold Hall core or duplicate-endpoint witness |
| pool shadow | initial blockers, paid depletion, new blockers, new-cell sets and charged pair-shadow incidences | retained density, charged threshold crossing or missing event atom |
| occurrence-slot repair | defect uses, faithful slots, compatibility and repair-extension incidences | complete assignment or deficit-sized repair transversal |
| source/certificate flow | physical sources, issued sources, certificates, defect demands and compatibility | complete integral flow or canonical mixed cut |
| recurrence | low-buffer lineages, recreation edges, finite guards, residue phases and tail tables | payment, ticket, descent, finite headroom, exact return or reset |

A template may combine several rows. No row supplies a physical constant unless all of its required records occur in the same schema version.

## AC5ii -- exact template serialization and overlap agreement -- PROVED

The complete ordered serialization of a template determines its pair values, state records, edge records and capacity references. Two occurrences of the same physical address in different templates are compatible exactly when their complete records agree.

The atlas compiler rejects the least of:

1. a stale template version;
2. a state record disagreeing in terminal flag, height, deficit, restart mass, owner, zone or another retained field;
3. a compatibility pair receiving two evaluator values;
4. an edge receiving two footprints, source/target records or restart descriptions;
5. a capacity address receiving two types, amounts, weights or lineage records.

On the accepted branch, overlapping templates define one unambiguous physical record on every overlap.

### Proof

Every object is finite, ordered and field-complete. Equality of canonical serializations is equality of every named field. The fixed atlas and address orders select the least discrepancy. QED.

## AC5ij -- exact pair, state and edge coverage deficits -- PROVED

On the overlap-consistent branch define

\[
\Omega_{\rm atl}=\bigcup_\alpha\Omega_\alpha,
\qquad
V_{\rm atl}=\bigcup_\alpha V_\alpha,
\qquad
E_{\rm atl}=\bigcup_\alpha E_\alpha.
\]

The exact atlas deficits are

\[
U_{\rm pair}=|\Omega\setminus\Omega_{\rm atl}|,
\qquad
U_{\rm state}=|V\setminus V_{\rm atl}|,
\qquad
U_{\rm edge}=|E\setminus E_{\rm atl}|.
\]

Exactly one of the following occurs:

1. all three deficits vanish and the atlas union equals the declared physical pair/state/edge universe;
2. the least uncovered compatibility pair is returned;
3. the least uncovered physical state is returned;
4. the least uncovered certified transition is returned;
5. a template contains an unknown nonphysical pair, state or edge, which is returned first.

Adding a sound version-preserving template without deleting old records decreases each deficit by exactly the number of newly covered physical objects of that type.

### Proof

This is finite set union and subtraction after AC5ii makes the union records well-defined. The decrement identity follows because adding a set removes exactly its previously uncovered elements from the complement. QED.

Thus kernel enlargement is now measurable: coverage progress is an exact integer, not a qualitative claim.

## AC5ik -- union reachability, bridge certification and cross-kernel rescue -- PROVED

Assume `U_pair=U_state=U_edge=0`. A **bridge edge** is a physical transition whose source and target have different retained kernel-zone labels or whose canonical least covering templates differ.

Every bridge must be present as an ordinary certified physical edge. If it changes active infrastructure, it must also satisfy exactly one of:

1. every newly activated entry has zero mass;
2. the edge names one funded globally addressed reset.

An implicit template switch is not an edge and cannot be used.

Run reverse reachability from `T` in the union graph `(V,E_atl)`. Exactly one of the following occurs:

1. every state reaches `T`;
2. the least unreachable state and its closed reachable component are returned;
3. the least bridge with positive unaccounted activation mass or missing reset is returned.

A state may fail to reach `T` inside its canonical local template but reach `T` in the union. Such a state is a **cross-kernel rescue** and is not a Hall or recurrence obstruction.

On the fully reachable branch, the exact minimax quantities

\[
B(v)=\min_{P:v\leadsto T}\max_{x\in P}H(x),
\]

`D(v)` equal to the shortest path length among paths attaining `B(v)`, and

\[
R(v)=B(v)(D_*+1)+D(v)
\]

are computed on the union graph. Every canonical union move strictly lowers `R`.

### Proof

Bridge legality is a finite edge-record check plus the zero-mass restart theorem. Reverse graph search decides reachability. A local failure is irrelevant when a union path exists. The minimax rank is AC5hu applied to the finite union graph. QED.

## AC5il -- global capacity deduplication and source conservation -- PROVED

Let `A` be the set of globally unique physical capacity addresses appearing in the accepted atlas. Each address has one type and one nonnegative amount. Repeated template references are aliases, not additional stock.

Define

\[
C_{\rm pay}=\sum_{a\in A_{\rm pay}}c(a),
\qquad
C_{\rm ticket}=\sum_{a\in A_{\rm ticket}}c(a),
\qquad
C_{\rm reset}=\sum_{a\in A_{\rm reset}}c(a),
\]

and for disturbance addresses

\[
U=\sum_{a\in A_{\rm dist}}c(a),
\qquad
W_{\rm dist}=\max_{a\in A_{\rm dist}}w(a).
\]

These are sums over unique physical addresses. In particular

\[
\sum_\alpha C_\alpha
\]

is generally invalid because one source, ticket or certificate may be cited by several templates.

If an address is reused after debit, split into two template-local copies, relabelled, given two types or increased without a named physical deposit, the compiler returns the least address and operation as a conservation failure.

### Proof

The capacity table is one finite map from physical addresses to typed amounts. Aliases refer to the same map entry and therefore contribute once. Occurrence-faithful debits and the existing source/certificate conservation law forbid duplication, splitting and source-less replenishment. QED.

This is the atlas analogue of certificate-source conservation and is essential when pool, repair and recurrence templates share the same physical source ledger.

## AC5im -- complete atlas certificate and finite episode envelope -- PROVED UNDER A COMPLETE PHYSICAL ATLAS

Assume AC5ii--AC5il accept and the physical state records contain synchronized deficit `Delta(v)` and restart potential `Theta(v)`. Let

\[
\Delta_*=\max_v\Delta(v),
\qquad
\Theta_*=\max_v\Theta(v),
\qquad
R_*=\max_vR(v).
\]

Put

\[
W_\Delta=(\Theta_*+1)(R_*+1)
\]

and

\[
\Psi(v)=\Delta(v)W_\Delta+\Theta(v)(R_*+1)+R(v),
\qquad
\Psi_*=\max_v\Psi(v).
\]

The deterministic atlas scheduler uses:

1. a compatible supply transition lowering `Delta`;
2. otherwise a zero-insertion credited restart lowering `Theta`;
3. otherwise the canonical union minimax move or a footprint-disjoint batch;
4. otherwise one globally unique payment or ticket debit;
5. otherwise one globally unique funded reset;
6. otherwise the exact terminal shortage or atlas witness.

Every noncapacity, nonreset episode strictly lowers `Psi`. Hence

\[
\boxed{
E_{\rm atl}
\le
(C_{\rm reset}+1)\Psi_*
+UW_{\rm dist}
+C_{\rm pay}
+C_{\rm ticket}.
}
\]

If template `alpha` has an ambient finite state bound `N_alpha`, then exact state deduplication gives

\[
|V|=\left|\bigcup_\alpha V_\alpha\right|
\le\sum_\alpha N_\alpha,
\qquad
D_*\le |V|-1.
\]

The output is exactly one of:

- a total compatibility atlas, complete physical union graph, exact ranks, deduplicated capacities and finite episode bound;
- a completed terminal state;
- the least stale, conflicting, uncovered, unreachable, bridge, restart, capacity or physical-certificate witness.

### Proof

AC5ij identifies the union with the declared physical universe. AC5ik supplies a finite reachable graph and strict minimax rank. AC5il supplies the correct global resource totals without double counting. AC5hx/AC5ic then give the mixed-radix episode envelope. The state and depth bounds are finite-union and simple-path bounds. QED.

## Deterministic audit

`scripts/verify_ac_kernel_coverage_atlas.py` checks 2,500 generated atlases. It verifies:

- exact overlap agreement and canonical first conflicts;
- exact pair, state and edge deficits;
- explicit bridge certification and zero-mass/funded-reset routing;
- cross-kernel rescue of local dead states;
- exact union minimax ranks;
- globally deduplicated capacity totals;
- exact mixed-radix atlas episode bounds;
- intended routing of stale, conflicting, uncovered, illegal-switch, capacity-conflict and unreachable cases.

## Main AC frontier

Only AC remains active. The next physical work is now organized by atlas rows:

1. enumerate the actual physical pair and state universes for one bounded AC epoch;
2. instantiate direct-exclusion, layered-incidence, pool-shadow, repair, source-flow and recurrence templates from historical AC records;
3. compute `U_pair,U_state,U_edge` after each template insertion;
4. certify every cross-template bridge and zero-mass activation or funded reset;
5. deduplicate all physical source, payment, ticket and reset addresses;
6. run AC5im on the first complete atlas;
7. enlarge the atlas until all deficits vanish, or use the least uncovered object as the next concrete frontier.

AC6 and the global no-three-in-line conjecture remain open.
