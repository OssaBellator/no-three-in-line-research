# Alternating-core all-n inspired descent compiler

## Status

This note keeps AC as the sole active research focus and proves AC5hs--AC5hx by adapting three reusable mechanisms from the frozen all-n branches:

- the semantic-key covers and private witnesses from the side-seven product census;
- the minimax barrier and complete optimal-path profiles from the side-six repair graph;
- the fixed-infrastructure, zero-mass-activation restart potential from prime patching.

The all-n branches remain source libraries. This note does not continue their finite classifications, import their numerical state counts as AC constants, construct the six physical compatibility evaluators, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Fix one finite AC macro epoch with the tagged full-record schemas of AC5hn--AC5hr. For track `s`, let `Omega_s` be the finite ordered universe of admissible tagged incidence-token pairs whose physical compatibility must be decided. Let `Omega` be the disjoint union of the seven `Omega_s`.

A semantic key `k` consists of:

1. one exact track and schema version;
2. a support mask and retained field values;
3. a certified extension set `C_k subseteq Omega_s`;
4. a deterministic partial evaluator `phi_k:C_k->{0,1}`;
5. the exact theorem, program, or physical lemma certifying that evaluator.

Keys on different tracks never overlap.

## AC5hs -- deterministic irredundant semantic basis -- PROVED

Let `K` be a finite ordered family of semantic keys on one track and put

\[
C=\bigcup_{k\in K}C_k.
\]

First reject the least pair on which two key evaluators disagree. On the consistent branch, apply deterministic maximum-uncovered greedy selection, with the fixed key order breaking ties, until the selected keys cover `C`. Then process the selected keys in reverse greedy order and delete every key whose removal preserves the union.

The resulting basis `B` satisfies:

1. `union_{k in B} C_k=C`;
2. its evaluators are consistent on every overlap;
3. it is irredundant;
4. every retained key `k` has a private pair

   \[
   z_k\in C_k\setminus\bigcup_{j\in B\setminus\{k\}}C_j.
   \]

### Proof

Greedy selection terminates because each step covers at least one previously uncovered element of the finite target union `C`. Reverse deletion preserves `C` by construction. If a retained key had no private pair, its extension would lie in the union of the other retained extensions and it would have been deleted. Overlap consistency was checked before selection and is inherited by the subfamily. QED.

The private pairs are executable regression witnesses: changing or deleting one retained semantic clause must change the answer on its private pair.

## AC5ht -- fail-closed compatibility compilation -- PROVED UNDER THE KEY CERTIFICATES

For track `s`, let `B_s` be the AC5hs basis and `C_s` its covered union.

If `C_s=Omega_s`, every retained field is present, every key certificate is sound on its complete tagged records, and the partial evaluators agree on overlaps, then

\[
\operatorname{Compat}_s(z)=\phi_k(z)\qquad(z\in C_k)
\]

is a well-defined total evaluator on `Omega_s`.

Otherwise the compiler returns the least of:

1. an uncovered pair in `Omega_s\setminus C_s`;
2. an overlap with conflicting evaluator values;
3. an omitted field or stale schema version;
4. an unsound key certificate, localized by its private witness;
5. a shared-state projection disagreement.

Define the semantic deficit

\[
U_s=|\Omega_s\setminus C_s|.
\]

Adding a sound, version-preserving key without removing old coverage decreases `U_s` by exactly the number of newly covered pairs. No result from the measured union may be extrapolated to the uncovered complement.

### Proof

Consistency makes the displayed definition independent of the chosen covering key. Full coverage makes it total. Every failed hypothesis has the stated least finite witness. The formula for `U_s` is set subtraction. QED.

This imports the useful lesson of the all-n semantic census without importing its model-specific 115-key basis or its small measured coverage fraction.

## AC5hu -- minimax barrier-depth repair rank -- PROVED

Let `G=(V,E)` be a finite directed AC repair graph, let `T subseteq V` be the terminal states, and let

\[
H:V\to\mathbb Z_{\ge0}
\]

be a declared defect or barrier height. Assume `v` can reach `T`. Define

\[
B(v)=\min_{P:v\leadsto T}\max_{x\in P}H(x),
\]

and let `D(v)` be the minimum path length among paths attaining barrier `B(v)`. Set `B(t)=H(t)` and `D(t)=0` for `t in T`. Choose the first edge of the lexicographically least path attaining `(B(v),D(v))`.

For its next state `w`,

\[
B(w)\le B(v),
\]

and if `B(w)=B(v)`, then

\[
D(w)<D(v).
\]

If `D_*` bounds `D` on the finite reachable graph, then

\[
R(v)=B(v)(D_*+1)+D(v)
\]

strictly decreases on every canonical repair move.

### Proof

The suffix beginning at `w` of an optimal path from `v` reaches `T` without exceeding barrier `B(v)`, so `B(w)<=B(v)`. If equality holds, that suffix is a barrier-optimal path for `w` of length `D(v)-1`, hence `D(w)<=D(v)-1`. If the barrier drops, the coefficient `D_*+1` dominates every possible increase in `D`; if it does not, `D` drops. QED.

This converts the finite all-n minimax diagnostics into an AC theorem: uphill repairs are permitted, but the pair `(minimum required barrier, remaining optimal depth)` is strictly descending.

## AC5hv -- optimal-move Hall and footprint batching -- PROVED UNDER THE EXISTING AC CONTRACTS

For each active AC fibre `f`, let `O_f` be the set of occurrence-faithful move tokens realizing a canonical AC5hu next move. Form the bipartite graph between active fibres and their tokens.

Exactly one of the following occurs:

1. the graph has a matching saturating all active fibres;
2. the canonical maximum matching returns a nonempty Hall-deficient fibre set and its exact missing-token cut.

In the saturated branch, choose one token per fibre. If each selected move footprint has size at most `h` and each physical primitive lies in at most `beta` selected footprints, the existing AC footprint-conflict theorem extracts a pairwise footprint-disjoint family `I` satisfying

\[
|I|\ge
\left\lceil
\frac{|F|}{h(\beta-1)+1}
\right\rceil,
\]

where `F` is the active fibre set. The simultaneous batch lowers

\[
\sum_{f\in F}R(v_f)
\]

by at least `|I|`.

### Proof

The matching/Hall alternative is finite Hall theory with the fixed AC order. The footprint extraction is the previously proved bounded-conflict greedy theorem. Every extracted move is canonical for its fibre and therefore lowers its AC5hu rank by at least one. Footprint disjointness gives simultaneous legality under the existing commutation contract. QED.

This uses all-n optimal-choice reserve without assuming a uniform branching lower bound: forced fibres are allowed, while incompatible simultaneous choices return a named Hall or footprint obstruction.

## AC5hw -- zero-mass restart comparability -- PROVED

Fix one infrastructure epoch. Let `P` be a fixed finite candidate-incidence universe and let `Q_z` be the state-dependent active-entry set at state `z`. Give all incidences nonnegative integer masses and define

\[
\Theta(z)
=
\sum_{p\in P}m_z(p)
+
\sum_{q\in Q_z}n_z(q).
\]

For a transition `z->z'`, suppose:

1. the fixed-universe term changes by at most `I-C_fix`, where `I` is inserted mass and `C_fix` is destroyed credited mass;
2. retained active entries do not gain mass;
3. removed active entries carry total old mass `C_act`;
4. every newly activated entry has zero mass in `z'`.

Then

\[
\boxed{
\Theta(z')-\Theta(z)
\le I-C_{\rm fix}-C_{\rm act}.
}
\]

In particular, if `I=0` and `C_fix+C_act>0`, the restart strictly lowers `Theta`, even if controller pairings, active menus, or optimal-move choices change.

A newly activated positive-mass entry, changed fixed universe, or newly inserted fixed-universe mass is returned with its exact incidence and source as a restart obstruction or funded outer reset.

### Proof

Sum the fixed-universe inequality. Retained active entries contribute a nonpositive change. Removed entries subtract `C_act`; new entries contribute zero. QED.

This is the AC-native version of the prime-patching restart principle: comparability needs fixed infrastructure plus zero-mass activation, not one universal table of every latent active entry.

## AC5hx -- strict AC macro potential and finite-episode envelope -- PROVED UNDER FINITE COMPLETENESS CONTRACTS

Fix a finite infrastructure epoch with complete AC5ht compatibility evaluators and a complete finite repair graph. Let

- `Delta` be synchronized matching deficit, bounded by `Delta_*`;
- `Theta` be the AC5hw restart potential, bounded by `Theta_*`;
- `R_tot=sum_f R(v_f)` be total AC5hu repair rank, bounded by `R_*`.

Put

\[
W_\Delta=(\Theta_*+1)(R_*+1)
\]

and

\[
\Psi
=
\Delta W_\Delta
+
\Theta(R_*+1)
+
R_{\rm tot}.
\]

Then:

1. an AC supply batch lowering `Delta` by at least one strictly lowers `Psi`, even if the lower coordinates reset within their bounds;
2. a zero-insertion paid restart preserving `Delta` and lowering `Theta` by at least one strictly lowers `Psi`, even if `R_tot` resets to `R_*`;
3. a minimax repair batch preserving `Delta,Theta` lowers `Psi` by at least its batch size;
4. incomplete semantics, a Hall shortage, footprint conflict, positive-mass activation, stale schema, or physical incompatibility terminates with its exact witness.

Let `Psi_*` be the maximum displayed potential in an epoch. Suppose there are at most `C_reset` funded infrastructure resets, total declared disturbance `U`, each disturbance unit increases `Psi` by at most `W_dist`, and nondecreasing payment/ticket episodes have total capacities `C_pay,C_ticket`. Then the number `E` of nonterminal episodes satisfies

\[
\boxed{
E
\le
(C_{\rm reset}+1)\Psi_*
+
U W_{\rm dist}
+
C_{\rm pay}
+
C_{\rm ticket}.
}
\]

### Proof

The mixed-radix coefficients make the three progress cases strict scalar descents. Within one epoch, the number of such descents is at most the starting potential plus declared disturbance increases. Payment and ticket episodes are bounded by their occurrence-faithful capacities. A funded reset starts a new epoch with potential at most `Psi_*`; there are at most `C_reset+1` epochs. Sum. QED.

Thus an infinite AC recurrence now requires one concrete failure: incomplete semantic coverage, an unbounded or incomplete repair graph, positive-mass activation at restart, unbounded disturbance/reset supply, or a failed physical compatibility/capacity contract.

## Finite check

`scripts/verify_ac_all_n_inspired_descent.py` checks deterministic semantic-basis compression, private witnesses, exact uncovered complements, minimax barrier-depth descent, optimal-token matching/Hall routing, footprint-disjoint extraction, zero-mass restart inequalities and mixed-radix macro-potential descent on 2,500 generated systems.

## Main AC frontier

Only AC remains active. The next work is now sharply ordered:

1. build semantic keys for the six physical `Compat_s` evaluators and expand their exact covered unions;
2. construct the finite AC repair graph on complete tagged macro states;
3. compute or bound `B,D,Delta_*,Theta_*,R_*`;
4. prove zero-mass activation for every permitted controller/menu restart;
5. instantiate disturbance, payment, ticket and reset capacities;
6. apply AC5hx to close finite recurrence and then AC6.

The global no-three-in-line conjecture remains open.
