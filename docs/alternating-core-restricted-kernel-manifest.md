# Alternating-core restricted physical kernel manifest

## Status

This note keeps AC as the sole active research focus and proves AC5id--AC5ih. It instantiates the abstract frontier manifest of AC5hy--AC5ic on the largest coherent restricted-menu kernel already present in the historical AC chain:

- exact retained-partner blocker inventories;
- fixed-order partial installation states;
- threshold-cost matching and Hall cores;
- weighted obstruction shortfall banks;
- low-buffer threshold tickets;
- finite recreation tickets;
- finite-strip and residue-phase tail routing.

The result is still contract-qualified. It does not construct the missing geometric blocker sets for every physical menu, prove that every AC state lies in this restricted kernel, prove AC6, or prove the no-three-in-line conjecture.

## Restricted kernel data

Fix one complete boundary and schema version. Let `B=(b_1,...,b_t)` be the fixed ordered target batch, let `P_0` be the initial partner pool, and let `P subseteq P_0` be the retained pool after occurrence-faithful paid depletion. Put `p_*=|P|`.

For every target `b`, retain five exact partner-exclusion sets

\[
X_b^{\rm supp},\quad X_b^{\rm sec},\quad X_b^{\rm line},\quad J_b,\quad N_b
\subseteq P,
\]

with complete physical addresses. The first three are certified by exact support, secant and dangerous-line inventories, while `J_b` is the residual predicate set and `N_b` the declared new-blocker set. Their certificates include numbers `Q_b,L_b` satisfying

\[
|X_b^{\rm supp}|\le |P_0\cap Q_b|,
\quad
|X_b^{\rm sec}|\le 2|Q_b|,
\quad
|X_b^{\rm line}|\le 2|L_b|.
\]

Define

\[
D_b=|P_0\cap Q_b|+2|Q_b|+2|L_b|+|J_b|,
\qquad
\Delta=\max_b(D_b+|N_b|),
\]

and `sigma=p_*-Delta-t`.

Every retained partner, target, exclusion occurrence, endpoint cost, obstruction class, resource coordinate, phase state, ticket and capacity address has a fixed total order.

## AC5id -- exact restricted-menu compatibility compilation -- PROVED UNDER THE EXCLUSION CERTIFICATES

Define

\[
\operatorname{Compat}_{\rm ker}(b,p)=1
\]

exactly when `p in P` and

\[
p\notin
X_b^{\rm supp}\cup X_b^{\rm sec}\cup X_b^{\rm line}\cup J_b\cup N_b.
\]

Then this is a total deterministic compatibility evaluator on `B x P`. Every target has degree

\[
d(b)\ge p_*-D_b-|N_b|\ge p_*-\Delta.
\]

If one exclusion set, occurrence address, target field, partner field or schema version is missing, stale or relabelled, the least such record is returned and no pair outside the certified dictionary is inferred.

### Proof

All five exclusion sets are explicitly enumerated on the complete tagged records, so membership decides every pair. Their union has size at most the sum of the displayed certified bounds, which gives the degree inequality. The fixed product order makes the first incomplete or inconsistent record canonical. QED.

Thus the semantic deficit of this restricted kernel is zero exactly when all five exclusion sets are physically certified for every target.

## AC5ie -- finite partial-installation graph -- PROVED

For `0<=j<=t`, a prefix state is a partial injection

\[
\mu:\{b_1,\ldots,b_j\}\hookrightarrow P
\]

such that every selected pair is compatible. There is a directed edge from `(j,mu)` to `(j+1,mu union {(b_{j+1},p)})` for every unused compatible `p`. Terminal states have `j=t`.

Before compatibility pruning, the exact number of prefix states is

\[
\boxed{
N_{\rm inj}=\sum_{j=0}^{t}(p_*)_j,
}
\]

where `(p_*)_j=p_*(p_*-1)\cdots(p_*-j+1)`. The compatible graph is the induced subgraph on the certified prefix states and therefore has at most `N_inj` states.

Reverse reachability from the terminal layer gives exactly one of:

1. the initial state reaches a complete installation;
2. the least dead prefix and its exact unsatisfied suffix Hall core.

If `sigma>0`, every prefix of length less than `t` has at least `sigma` unused compatible partners, so the initial state reaches a terminal state.

### Proof

For fixed `j`, an unrestricted prefix injection is an ordered choice of `j` distinct partners, hence `(p_*)_j`. Summing over prefix lengths gives the state count. The edge rule is exactly compatible extension. Reverse finite graph search decides extendability. If `sigma>0`, AC5id leaves at least `p_*-Delta` compatible partners for the next target, and fewer than `t` partners are used, so at least `p_*-Delta-t=sigma` choices remain. QED.

## AC5if -- threshold-cost Hall and obstruction-bank router -- PROVED UNDER THE CLASS CERTIFICATES

Give every retained partner or legal installation endpoint an integer cost `c(r)>=0`. For threshold `a`, let `G_a` retain exactly the compatible incidences to endpoints of cost at most `a`, let `nu_a` be its maximum matching size, and put

\[
\delta_a=t-\nu_a.
\]

If the full graph saturates all targets, the minimum total endpoint cost is

\[
\boxed{
C_{\min}=\sum_{a\ge0}\delta_a.
}
\]

If a desired cost budget fails, the least threshold with positive required excess returns its canonical Hall-deficient target set and exact endpoint neighbourhood.

For every conditioned layer `i`, retain reverse load `D_i`, forward degree `d_i`, target ratio `theta`, and exact obstruction label `lambda(i)`. Define

\[
s_i=(\theta D_i-d_i)_+,
\qquad
Q_\lambda=\sum_{i:\lambda(i)=\lambda}s_i.
\]

Then

\[
(\theta\sum_iD_i-\sum_i d_i)_+
\le
\sum_i s_i
=
\sum_\lambda Q_\lambda.
\]

If obstruction class `lambda` has initial capacity `C_lambda`, recorded deposits `D_lambda^{\rm dep}`, and positive debit threshold `tau_lambda`, then the number of paid failures of that class is at most

\[
\left\lfloor
\frac{C_\lambda+D_\lambda^{\rm dep}}{\tau_\lambda}
\right\rfloor.
\]

Hence the complete paid-failure stock is

\[
\boxed{
N_{\rm paid}
\le
\sum_\lambda
\left\lfloor
\frac{C_\lambda+D_\lambda^{\rm dep}}{\tau_\lambda}
\right\rfloor.
}
\]

Insufficient class balance returns the least exact overload. Missing layer identity, relabelled shortfall, negative cancellation or unrecorded deposits return reset.

### Proof

The cost identity is the integral threshold layer-cake formula for minimum-cost bipartite matching. Hall's theorem supplies the canonical deficient set at each threshold. Local positive parts dominate the aggregate positive part, and the exact class partition preserves all shortfall mass. Occurrence-faithful threshold debits give the classwise floor bound. QED.

## AC5ig -- explicit low-buffer, recreation and tail stocks -- PROVED UNDER THE HISTORICAL AC CONTRACTS

Let resource coordinate `i` have low-buffer threshold `beta_i` and, for every `0<=h<beta_i`, a finite stock `U_(i,h)` of capacity-one crossing lineages. Put

\[
K_{\rm low}=\sum_i\beta_i,
\qquad
T_{\rm low}=\sum_i\sum_{h=0}^{\beta_i-1}U_{(i,h)}.
\]

Every exact low-buffer return gives resource-dimension descent, current payment, one of the `T_low` threshold tickets, an explicit recreation gate, or reset.

For a finite occurrence-faithful recreation atom set `A` and decorated restoration-edge set `E_rec`, the restoration-ticket stock is at most

\[
\boxed{T_{\rm rec}=|A||E_{\rm rec}|.}
\]

For a deterministic one-counter tail with finite control set `Q`, modulus `M` and exceptional threshold `H`, the absolute strip contains exactly

\[
S_{\rm strip}=|Q|H
\]

states and the residue-control phase space has

\[
S_{\rm phase}=|Q|M
\]

states. Every tail trajectory reaches a phase cycle within `S_phase` steps. A positive-drift cycle escapes monotonically, a zero-drift cycle is an exact return entering the ticket/payment/reset router, and a negative-drift cycle has the exact finite traversal budget

\[
1+\left\lfloor\frac{b_0-T(C)}{|D|}\right\rfloor.
\]

Thus no low-buffer, recreation or finite-residue tail recurrence remains unclassified inside a fixed kernel epoch.

### Proof

The low-buffer statement is the canonical minimum-face and threshold-lineage router. Recreation tickets are addressed by one atom and one decorated restoration edge. The strip and phase counts are direct products. Determinism on the finite phase set yields an eventual cycle; summing its increments gives the signed-drift trichotomy and the displayed negative-drift budget. QED.

## AC5ih -- restricted-kernel finite episode envelope -- PROVED UNDER A COMPLETE KERNEL

Assume:

1. AC5id gives a total compatibility evaluator;
2. every accepted restricted prefix state and transition is present;
3. the initial state reaches a terminal installation or a canonical minimax terminal in the compiled graph;
4. every restart obeys the AC5hw zero-mass activation rule or spends a funded reset;
5. all obstruction, threshold and recreation capacities are occurrence-faithful.

Let `Psi_ker,*` be the exact maximum mixed-radix AC potential on the compatible restricted graph, including its exact minimax barrier-depth rank. Let `C_reset` be the funded reset stock, `U` the total declared disturbance, and `W_dist` the maximum potential increase per disturbance unit.

Then the number of nonterminal restricted-kernel episodes satisfies

\[
\boxed{
E_{\rm ker}
\le
(C_{\rm reset}+1)\Psi_{\rm ker,*}
+UW_{\rm dist}
+N_{\rm paid}
+T_{\rm low}
+T_{\rm rec}
+S_{\rm strip}
+S_{\rm phase}.
}
\]

Moreover the finite graph constants have the explicit ambient bounds

\[
|V_{\rm ker}|\le N_{\rm inj},
\qquad
D_*\le N_{\rm inj}-1,
\qquad
R_*\le H_*N_{\rm inj}+N_{\rm inj}-1,
\]

where `H_*` is the maximum enumerated defect height.

The compiler output is exactly one of:

- a complete restricted installation and finite episode bound;
- a dead prefix or threshold Hall core;
- a heavy exact blocker/shortfall class;
- an exhausted payment, low-buffer or recreation capacity;
- a finite-strip or phase-cycle route;
- a positive-mass restart activation;
- the least missing physical exclusion, transition, lineage, phase or capacity certificate.

### Proof

Within one reset epoch, supply, credited restart and canonical minimax steps strictly lower the existing AC mixed-radix potential. Paid failures, low-buffer excursions, restoration events, strip returns and phase transients consume the displayed finite occurrence-faithful stocks. Disturbance increases are bounded by `UW_dist`, and every funded reset begins a new epoch with potential at most `Psi_ker,*`. Summing over at most `C_reset+1` epochs proves the envelope. A simple path in a finite graph has length at most `N_inj-1`; substituting that depth bound into the minimax rank formula gives the ambient rank bound. QED.

## Deterministic audit

`scripts/verify_ac_restricted_kernel_manifest.py` checks one coherent restricted kernel per generated system. It verifies:

- exact blocker-set compatibility and degree bounds;
- positive-slack extension and nonpositive-slack overload routing;
- exact partial-injection state counts;
- full matching or Hall failure;
- the threshold layer-cake minimum-cost identity;
- weighted shortfall partition and class overloads;
- low-buffer and recreation stock formulas;
- finite phase extraction and signed drift;
- the expanded restricted-kernel episode envelope.

The deterministic run checks 2,500 systems.

## Main AC frontier

The useful historical AC machinery is now compiled into one restricted physical kernel. The next work is concrete:

1. populate the five exact exclusion sets for actual AC menus;
2. identify which physical states lie in the restricted kernel;
3. enumerate their compatible prefix and repair graphs;
4. compute exact endpoint costs, layer degrees and reverse loads;
5. certify obstruction labels and capacities;
6. certify low-buffer lineages, recreation edges and tail tables;
7. run AC5ih on the resulting physical kernel;
8. enlarge the kernel until every AC macro state is covered, or return the first exact state outside it.

AC6 and the global no-three-in-line conjecture remain open.
