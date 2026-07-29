# Alternating-core frontier manifest compiler

## Status

This note keeps AC as the sole active research focus and proves AC5hy--AC5ic. It combines every current AC frontier into one finite, executable manifest:

1. field-complete semantic keys for the seven tagged compatibility interfaces;
2. the finite tagged repair graph and terminal set;
3. exact minimax barrier, depth and mixed-radix constants;
4. restart comparability through fixed infrastructure and zero-mass activation;
5. occurrence-faithful payment, ticket, reset and disturbance capacities.

The result is a **compiler theorem**. It does not construct the missing physical semantic keys or physical repair graph, prove their finite capacities, prove AC6, or prove the no-three-in-line conjecture. It proves that once these data are supplied in one complete manifest, all remaining finite checks and constants are canonical and mechanically auditable; otherwise the least missing certificate is returned.

## Complete AC frontier manifest

A manifest is the finite record

\[
\mathfrak M=
(\Sigma,\Omega,\mathcal K,\Pi,V,T,E,H,\mathcal R,\mathcal C).
\]

Its fields are:

- `Sigma`: the ordered seven-track schema registry with track tags and schema versions;
- `Omega_s`: the complete ordered universe of admissible tagged incidence-token pairs for track `s`;
- `K_s`: finite semantic keys, each retaining its exact support mask, field values, extension set, partial evaluator and physical certificate;
- `Pi`: all shared-state projections and their consistency requirements;
- `V`: the complete finite tagged AC macro/repair state set;
- `T subseteq V`: the terminal states;
- `E`: the declared certified repair transitions, including occurrence-faithful move tokens and footprints;
- `H:V->Z_{\ge0}`: the physical defect/barrier height;
- `R`: every permitted restart record, with fixed-universe mass, retained active entries, removed credit and newly activated entries;
- `C`: typed occurrence-faithful payment, ticket, reset and disturbance capacities.

All sets and fields carry fixed total orders. Capacity addresses are globally unique inside their declared type.

## AC5hy -- exact manifest identity and frontier coverage -- PROVED

The complete ordered serialization of `M` determines every finite object needed by AC5hs--AC5hx. Two manifests are identical exactly when every serialized field agrees.

The manifest covers all current AC frontier tasks:

| Frontier | Required manifest component |
|---|---|
| physical compatibility | `Sigma,Omega,K,Pi` |
| finite repair graph | `V,T,E,H` |
| minimax constants | exact computation from `V,T,E,H` |
| restart comparability | `R` |
| typed capacities | `C` |
| AC finite recurrence | compiled mixed-radix potential and episode bound |

A missing track, changed schema version, omitted field, changed pair universe, unknown state, changed terminal flag, malformed edge, changed footprint, changed restart mass or relabelled capacity address is therefore a concrete manifest discrepancy rather than an implicit outer assumption.

### Proof

Every listed object is finite and ordered. Canonical serialization is injective because it retains every field name, version, value and address. The table is an exhaustive partition of the data used by the preceding AC theorem blocks. QED.

## AC5hz -- total semantic compilation or exact semantic deficit -- PROVED UNDER THE KEY CERTIFICATES

For each track `s`, first reject the least stale schema, omitted field or shared-state disagreement. Then reject the least pair on which two certified partial evaluators disagree.

On the consistent branch, apply AC5hs deterministic greedy selection and reverse deletion. This yields an irredundant basis `B_s` with one private pair per retained key. Put

\[
C_s=\bigcup_{k\in B_s}C_k,
\qquad
U_s=|\Omega_s\setminus C_s|.
\]

Exactly one of the following occurs:

1. `U_s=0`, and the key values compile to a unique total evaluator
   \[
   \operatorname{Compat}_s:\Omega_s\to\{0,1\};
   \]
2. the least uncovered tagged pair is returned;
3. the least overlap conflict is returned;
4. the least stale, omitted, unsound or shared-inconsistent key is returned, with a private witness when applicable.

Across all tracks define

\[
U_{\rm sem}=\sum_s U_s.
\]

Adding a sound version-preserving key without removing certified coverage decreases `U_sem` by exactly the number of newly covered pairs. No evaluator value may be extrapolated outside the certified union.

### Proof

This is AC5hs--AC5ht applied trackwise, with the manifest order resolving every least witness. Full coverage and overlap consistency make the evaluator total and well-defined. Set subtraction gives the exact semantic deficit and its monotone decrement. QED.

## AC5ia -- exact finite repair-graph compilation and constant extraction -- PROVED

Assume every `Compat_s` is total. The compiler accepts a transition `v->w` only when:

1. `v,w in V`;
2. its tagged move token is live in the declared epoch;
3. the corresponding incidence-token pair is compatible;
4. its full footprint and transition certificate are present;
5. its source, target, owner and shared-state projections agree with the manifest.

The least malformed or incompatible edge is returned.

On the accepted graph, reverse reachability from `T` gives exactly one of:

1. every state reaches `T`;
2. the least unreachable state and its closed reachable component.

On the first branch define

\[
B(v)=\min_{P:v\leadsto T}\max_{x\in P}H(x),
\]

let `D(v)` be the shortest length among paths attaining `B(v)`, and put

\[
D_*=\max_{v\in V}D(v),
\qquad
R(v)=B(v)(D_*+1)+D(v).
\]

The compiler returns exact finite values for

\[
B_*,D_*,R_*,
\Delta_*,
\Theta_*
\]

by taking maxima over the enumerated state set. Every canonical minimax move strictly lowers `R`.

### Proof

All edge checks are finite dictionary checks. Reverse graph search decides terminal reachability. The minimax computation is the finite bottleneck shortest-path calculation of AC5hu; its canonical suffix argument gives strict rank descent. Maxima over finite enumerated sets are exact. QED.

## AC5ib -- restart and capacity compiler -- PROVED

For each restart, let the fixed-universe mass change be at most

\[
I-C_{\rm fix},
\]

let removed active entries carry total mass `C_act`, and require every newly activated entry to have zero mass.

The compiler either verifies

\[
\Theta(z')-\Theta(z)
\le
I-C_{\rm fix}-C_{\rm act},
\]

or returns the least newly activated positive-mass entry, fixed-universe change, unexplained inserted mass or retained-entry increase.

For the strict restart branch `I=0` and `C_fix+C_act>0`, the restart lowers `Theta` by at least one.

The capacity compiler separately checks the ordered typed tables for:

- payment occurrences;
- ticket addresses;
- funded resets;
- disturbance events and their maximum potential increase.

It rejects the least duplicate address, negative amount, cross-track migration or untyped debit. Otherwise it returns the exact totals

\[
C_{\rm pay},\quad
C_{\rm ticket},\quad
C_{\rm reset},\quad
U,\quad
W_{\rm dist}.
\]

### Proof

The restart inequality is AC5hw summed over the manifest entries. The capacity tables are finite nonnegative maps on unique addresses, so their totals and first violations are exact. QED.

## AC5ic -- complete finite AC certificate and episode bound -- PROVED UNDER A VALID MANIFEST

Assume AC5hz, AC5ia and AC5ib all accept. Let

\[
W_\Delta=(\Theta_*+1)(R_*+1)
\]

and define

\[
\Psi(v)
=
\Delta(v)W_\Delta+
\Theta(v)(R_*+1)+R(v).
\]

Let

\[
\Psi_*=\max_{v\in V}\Psi(v).
\]

Then the compiler produces one deterministic AC scheduler:

1. use a compatible supply batch when synchronized deficit can fall;
2. otherwise use a zero-insertion credited restart when `Theta` can fall;
3. otherwise take the canonical minimax repair move or its footprint-disjoint batch;
4. otherwise spend one unique payment or ticket capacity;
5. otherwise take one funded infrastructure reset;
6. otherwise return the exact terminal shortage or obstruction.

Every noncapacity, nonreset episode strictly lowers `Psi`. Therefore the number `E` of nonterminal episodes satisfies

\[
\boxed{
E
\le
(C_{\rm reset}+1)\Psi_*
+
UW_{\rm dist}
+
C_{\rm pay}
+
C_{\rm ticket}.
}
\]

The compiler output is thus exactly one of:

- a total compatibility dictionary, complete finite repair graph, exact constants and finite termination bound;
- a completed terminal AC state;
- the least schema, semantic, edge, reachability, restart, capacity or physical-certificate witness.

### Proof

AC5hx proves strict mixed-radix descent for supply, restart and minimax episodes. Disturbance increases are bounded by `UW_dist`; capacity episodes are bounded by their unique address stocks; each funded reset starts an epoch with potential at most `Psi_*`. Summing over at most `C_reset+1` epochs gives the bound. The ordered manifest checks make every failure canonical. QED.

## Deterministic audit

`scripts/verify_ac_frontier_manifest_compiler.py` checks 2,500 coherent and deliberately defective manifests. It validates:

- seven-track semantic compilation and private witnesses;
- exact uncovered, overlap, stale-schema, omitted-field, unsound-key and shared-state routes;
- terminal reachability and malformed-edge detection;
- exact minimax barrier-depth ranks;
- zero-mass restart inequalities;
- positive-mass activation witnesses;
- unique typed capacity tables;
- exact mixed-radix potential and episode bounds.

The deterministic run contains:

- 209 fully valid manifests;
- 2,291 manifests routed to their intended least failure;
- 20,303 tagged semantic pairs in valid manifests;
- 5,957 irredundant semantic keys and private witnesses;
- 3,244 finite repair states;
- 3,035 strict canonical minimax moves;
- 3,830 units of restart credit;
- aggregate `Psi_*` equal to 3,285,903;
- aggregate compiled episode bound 13,314,334;
- payment, ticket and reset capacities 2,494, 1,043 and 642.

## Main AC frontier

Only AC remains active. The compiler has made the remaining tasks concrete data-construction problems:

1. populate the seven exact admissible pair universes `Omega_s`;
2. construct certified semantic keys until `U_sem=0`;
3. enumerate the complete tagged physical state set and certified transition graph;
4. identify terminal AC states and compute the exact `B,D,R` tables;
5. prove every permitted restart has zero-mass activation or a funded reset;
6. enumerate occurrence-faithful payment, ticket, reset and disturbance capacities;
7. run AC5ic on the physical manifest;
8. close AC6 or return the first exact physical obstruction.

The global no-three-in-line conjecture remains open.
