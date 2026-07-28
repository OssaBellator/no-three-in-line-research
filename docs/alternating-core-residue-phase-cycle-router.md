# Residue-phase cycle router for cyclic one-sided counters

**Branch:** `research/alternating-core-chain`

AC3vv--AC3vz close triangular one-sided counter dependence. The remaining finite-control case is cyclic dependence through bounded residues: later macro legality may depend on earlier and later counters, but only through a finite residue phase. This note replaces that cyclic dependence by an eventual finite phase orbit and applies one-sided drift to the resulting residue-return block.

The result does not cover increments or guards depending on unbounded absolute counter values outside the displayed lower guards.

## Residue-controlled macro system

Let

\[
 z=(z_1,\ldots,z_q)\in\mathbb Z^q
\]

be additive counters with lower guards. Fix moduli `M_i>=2` and the residue phase

\[
 \phi(z)=(z_1\bmod M_1,\ldots,z_q\bmod M_q)\in\Phi,
 \qquad |\Phi|=\prod_i M_i.
\]

For each finite boundary state and phase `phi`, one complete macro pass has:

- a deterministic next phase `T(phi)`;
- an additive increment vector `v(phi)` satisfying `T(phi)=phi+v(phi) mod M`;
- a lower requirement vector `g(phi)` such that the pass is legal from base `z` whenever `z_i>=g_i(phi)` for every coordinate, after incorporating the pass's internal prefix minima.

All payment-sensitive fields other than `z` and `phi` are retained in the finite boundary state. A changed modulus, transition table, requirement table, physical interpretation or omitted field is an outer reset.

## AC3wa -- finite phase preperiod and cycle -- PROVED

From every starting phase, the deterministic phase orbit has a preperiod and a nonempty directed cycle whose total length is at most

\[
 \boxed{|\Phi|=\prod_i M_i}.
\]

### Proof

Iterate `T` on the finite set `Phi`. Before `|Phi|+1` visited phases, one repeats. The segment before the first repeated phase is the preperiod and the repeated segment is a directed cycle. QED.

## Residue-return block

Fix the eventual phase cycle

\[
 C=(\phi_0,\ldots,\phi_{r-1}),
 \qquad T(\phi_j)=\phi_{j+1\bmod r}.
\]

Define its aggregate drift

\[
 d=\sum_{j=0}^{r-1}v(\phi_j).
\]

For each coordinate, define the exact block requirement

\[
 L_i=\max_{0\le j<r}
 \left(g_i(\phi_j)-\sum_{t<j}v_i(\phi_t)\right).
\]

Thus one cycle block is legal from base `z` whenever `z_i>=L_i` for all `i`.

## AC3wb -- phase return and exact block translation -- PROVED

The aggregate drift obeys

\[
 \boxed{d_i\equiv0\pmod{M_i}}
\]

for every coordinate. One legal traversal of the phase cycle sends

\[
 (\phi_0,z)\longmapsto(\phi_0,z+d),
\]

and every subsequent traversal uses the same finite phase word and the same requirement vector `L`.

### Proof

The phase cycle returns to `phi_0`, while each transition adds `v(phi_j)` modulo `M`. Summing gives the congruences. The additive counter update is the ordinary sum of increments. Because the residue phase and finite boundary state return, the same transition and guard tables apply again. The definition of `L` is exactly the maximum lower base needed over the internal prefixes. QED.

## AC3wc -- signed aggregate drift router -- PROVED

Let a residue-return block be legal from `z`.

1. If some `d_i<0`, then the number of further legal block traversals is at most

   \[
   \boxed{
   \min_{i:d_i<0}
   \left(\left\lfloor\frac{z_i-L_i}{-d_i}\right\rfloor+1\right).
   }
   \]

2. If every `d_i>=0` and at least one is positive, the additive state is strictly monotone and cannot recur exactly.

3. If `d=0`, one block returns the complete additive state exactly.

### Proof

Before traversal number `k`, coordinate `i` equals `z_i+k d_i`. For `d_i<0`, legality requires this to remain at least `L_i`; solving gives the displayed first-failure bound. If all drifts are nonnegative and one is positive, that coordinate never returns. If every drift is zero, the translated state equals the initial state. QED.

Mixed-sign drift is covered by the first alternative: any negative coordinate supplies finite lower headroom even when other coordinates increase.

## AC3wd -- finite cyclic-dependence interface -- PROVED UNDER THE RESIDUE-COMPLETE CONTRACT

Every residue-controlled one-sided history has one continuation:

1. it remains in the finite preperiod of length less than `|Phi|`;
2. its eventual residue-return block has a negative coordinate and therefore a finite exact execution budget;
3. its block drift is componentwise nonnegative and nonzero, giving monotone escape;
4. its block drift is zero, giving an exact finite-state return for the existing payment, restoration-ticket or cycle-space router;
5. or a modulus, transition, requirement, boundary, owner, lineage, legality or physical field changes, giving an explicit reset.

### Proof

Apply AC3wa to reach the eventual phase cycle, AC3wb to form its exact residue-return block and AC3wc to route its aggregate drift. QED.

## AC3we -- updated AC4 frontier -- PROVED AS A REDUCTION

Cyclic guard dependence through a fixed finite residue phase is no longer an unbounded multi-counter obstruction. The unresolved AC4 cases require at least one of:

- guards or increments depending on unbounded absolute values beyond lower requirements;
- dynamically changing moduli or transition dictionaries;
- nonlinear or nonadditive counter updates;
- genuinely replenished physical resources;
- or payment-sensitive fields omitted from the complete boundary state.

## Finite check

`scripts/verify_ac_residue_phase_cycles.py` enumerates and samples residue transition systems with one to three counters, checks finite preperiod/cycle extraction, verifies aggregate phase return, and audits the exact negative-drift headroom formula and the positive/zero-drift alternatives.