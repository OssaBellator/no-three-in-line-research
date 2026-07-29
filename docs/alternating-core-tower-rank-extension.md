# Alternating-core overlap-preserving tower rank extension

## Status

This note keeps AC as the sole active research focus and proves AC5jj--AC5jo. It repairs the remaining hidden hypothesis in AC5jc: recomputing a minimax rank after every cap enlargement need not preserve the old scheduler or old rank values. The new compiler keeps every certified old rank fixed and solves one finite strict-descent extension problem on the new shell.

The result remains contract-qualified. It does not construct the actual physical progress-edge graph, prove a global rank cap, prove that the global physical capacity-address universe is finite, prove AC6, or prove the no-three-in-line conjecture.

## Progress graph contract

For a bounded box `B_n`, let `P_n subseteq E_n` be the scheduled **strict-progress edges**: supply, credited restart and canonical repair edges that are required to decrease the state rank. Payment, ticket, disturbance and funded-reset edges are accounted separately and are not placed in `P_n`.

Assume a certified rank

\[
\rho_n:V_n\longrightarrow\{0,1,\ldots,R_n\}
\]

satisfying

\[
(u,v)\in P_n\implies \rho_n(u)>\rho_n(v).
\]

After cap enlargement, retain the old vertices and old progress edges literally, add the shell vertices `S=V_(n+1)\setminus V_n`, and declare the complete new progress-edge set `P_(n+1)`.

## AC5jj -- least overlap-preserving rank extension -- PROVED

Keep `rho_n` fixed on `V_n`. Seek nonnegative integer ranks on `S` satisfying

\[
\rho(u)\ge \rho(v)+1
\qquad ((u,v)\in P_{n+1}).
\]

If the complete progress graph is acyclic, process a topological order in reverse. For every shell vertex define

\[
\rho_{\min}(u)
=
\max_{u\to v}\bigl(\rho(v)+1\bigr),
\]

with empty maximum zero. For an old vertex, compute the same required lower bound but keep its old value.

Exactly one of the following occurs:

1. every old value is at least its newly required lower bound; then `rho_min` is the unique componentwise least overlap-preserving extension;
2. the least old vertex `u` has `rho_n(u)` below its new required lower bound; the compiler returns `u`, the least forcing edge and the exact missing rank amount.

### Proof

In a DAG every successor is processed first. Any feasible extension must dominate the displayed successor maximum, so the reverse-topological assignment is componentwise least. Old values are fixed, hence feasibility is exactly the old lower-bound check. QED.

## AC5jk -- strict-progress cycle and rank-cap obstructions -- PROVED

Before AC5jj, compute the canonical least strongly connected component of the complete progress graph.

- If a nontrivial component or self-loop exists, strict rank descent around the directed cycle would give `rho(v)>rho(v)`. The component and its least directed cycle are an exact scheduler obstruction.
- On the acyclic branch, if one shell value from AC5jj exceeds a declared global cap `R_bar`, the least such shell vertex, its forcing descendant chain and exact required value are returned.

Thus the extension compiler outputs exactly one of:

1. a strict-progress cycle;
2. an old-rank overlap violation;
3. a shell rank above `R_bar`;
4. the least valid overlap-preserving extension.

### Proof

Strict inequalities forbid directed cycles. On a DAG AC5jj gives the least possible shell ranks, so if that least value exceeds `R_bar`, no capped extension exists. QED.

## AC5jl -- bounded integer component stabilization -- PROVED

For every box level retain the six nonnegative integer envelope components

\[
X_n=
(\Delta_n^*,\Theta_n^*,R_n^*,C_{{\rm reset},n},C_{{\rm pay},n},C_{{\rm ticket},n}).
\]

Use overlap-preserving state records, the rank extension of AC5jj, and globally addressed capacities, so every component is nondecreasing with `n`.

Assume componentwise global caps

\[
X_{n,j}\le G_j<\infty.
\]

Every strict increase has a canonical least shell state, progress edge or newly referenced physical capacity address witnessing it. The number of strict component increases over the whole tower is at most

\[
\boxed{\sum_j G_j}
\]

when the components begin at zero, and at most `sum_j(G_j-X_(0,j))` in general. Consequently all six components eventually stabilize.

### Proof

A nonnegative integer component bounded by `G_j` can strictly increase at most `G_j-X_(0,j)` times. Fixed shell and address orders choose the first witness at each increase. Summing gives the bound. QED.

## AC5jm -- finite global physical-capacity quotient -- PROVED

Let `A_glob` be one finite set of globally unique physical source, payment, ticket and reset addresses. Every address `a` has one fixed type and stock `c(a)`, including every named deposit permitted by the physical schema.

At level `n`, the selected atlas may reference any subset `A_n subseteq A_glob`, but aliases across templates or levels are the same address. Therefore

\[
C_{{\rm type},n}
=\sum_{a\in A_n\cap A_{\rm type}}c(a)
\le
\sum_{a\in A_{\rm glob}\cap A_{\rm type}}c(a).
\]

The right-hand side is a uniform tower bound independent of the number of boxes and templates.

If a level introduces a genuinely new address outside `A_glob`, changes an old address's type or stock, duplicates one occurrence under a new label, or increases stock without a named deposit, the least address and operation are returned. Such a record is a physical-address-universe failure, not additional free capacity.

### Proof

Every level total is a sum over a subset of one fixed finite map. Alias references do not create new map entries. The discrepancy alternatives are exactly the ways this fixed quotient can fail. QED.

## AC5jn -- uniform scheduler certificate after rank extension -- PROVED

Assume:

1. every shell passes AC5jj--AC5jk with one common rank cap `R_bar`;
2. deficit and restart-potential maxima have global caps `Delta_bar,Theta_bar`;
3. AC5jm supplies global bounds `C_reset,C_pay,C_ticket`;
4. disturbance total and weight have global bounds `U,W_dist`;
5. every bounded atlas is complete and the non-rank scheduler choices agree literally on overlaps.

Define

\[
W_\Delta=(\Theta_{\rm bar}+1)(R_{\rm bar}+1)
\]

and

\[
\Psi_{\rm bar}
=\Delta_{\rm bar}W_\Delta
+\Theta_{\rm bar}(R_{\rm bar}+1)
+R_{\rm bar}.
\]

Then every box has the same valid episode envelope

\[
\boxed{
E_{\rm bar}
=(C_{\rm reset}+1)\Psi_{\rm bar}
+UW_{\rm dist}
+C_{\rm pay}+C_{\rm ticket}.
}
\]

Combined with cofinality, AC5jc applies and no nonterminal direct-limit trajectory has more than `E_bar` steps.

### Proof

AC5jj preserves every old progress rank and assigns bounded ranks to new states. The displayed mixed-radix constants dominate the state-local components in every box. AC5jm supplies fixed capacity bounds, so AC5ir gives the same envelope at every level. AC5jc then gives direct-limit termination. QED.

## AC5jo -- exact tower-divergence router -- PROVED

Run the tower compiler level by level. If AC5jn never becomes available, return the first object in the following order:

1. a strict-progress cycle;
2. an old-rank overlap violation;
3. a shell state requiring rank above the current declared global cap;
4. a new shell witness increasing `Delta^*` or `Theta^*` beyond its declared cap;
5. a new or relabelled physical capacity address;
6. an unbounded disturbance amount or weight;
7. a noncofinal coordinate;
8. a bounded-box atlas or boundary-certificate failure.

If a component has no finite declared cap, retain the sequence of its canonical strict-increase witnesses. An infinite such sequence is the exact reason the uniform AC5jc bound is unavailable; it is not hidden inside a changing box constant.

### Proof

The list is the ordered negation of AC5jn together with cofinality and bounded-box completeness. AC5jl ensures that a component with a valid finite cap can increase only finitely often, so an infinite strict-increase sequence certifies absence of that cap or failure of its physical interpretation. QED.

## Deterministic audit

`scripts/verify_ac_tower_rank_extension.py` checks 2,500 shell extensions. It verifies:

- exact topological rank extension with old ranks fixed;
- strict-progress cycle detection;
- old-to-shell rank violations;
- least shell ranks above a declared cap;
- bounded integer stabilization counts;
- finite global physical-address capacity quotients and alias removal.

## Main AC frontier

Only AC remains active. The remaining tasks are now concrete:

1. enumerate the actual scheduled strict-progress edges on each physical shell;
2. run AC5jj and repair every returned cycle or overlap violation;
3. prove finite global caps for deficit, restart potential and the extended rank;
4. declare the finite global physical capacity-address universe;
5. prove cofinality and bounded disturbances;
6. apply AC5jn--AC5jc, or retain the first divergence witness from AC5jo as the exact AC6 frontier.

AC6 and the global no-three-in-line conjecture remain open.
