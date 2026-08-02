# All-n product track: packet strict-sign and trajectory-reset stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`all-n-product-terminal-core-stage.md`](all-n-product-terminal-core-stage.md).
PX294--PX314 sharpen both unresolved branches. Trajectory-saturated terminal
cores now reset through a historical back edge or cyclic ancestor layer, or
reduce to a dense antichain child with an explicit path-forest depth excess.
Diffuse packet defects now aggregate by correcting transposition and satisfy a
Bernoulli strict-sign-or-clean-star theorem above a linear residual.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Historical back-edge reset | **AVAILABLE** | PX294 releases one ancestor edge reversing an allowed path and closes a principal cycle. |
| No-back-edge terminal structure | **REDUCED** | PX295--PX298 bound the full reachability closure by `m Delta_0` and extract a historically dense antichain child. |
| Full/cyclic ancestor layer | **ABSORBED** | PX299 and PX311 turn one releasable cyclic historical layer into a principal reset. |
| Frozen trajectory child | **DEPTH-CERTIFIED** | PX312--PX314 force a path-forest decomposition and explicit ancestor-depth excess. |
| Diffuse packet geometry | **DECODED** | PX300--PX304 give a heavy disjoint correction bank or a selected-point clean star. |
| Packet higher-order collateral | **CONTROLLED** | PX305--PX306 show that any positive first-order gap survives all support-two and support-three creation by Bernoulli thinning. |
| Packet first-order obstruction | **DECODED** | PX307--PX309 turn excessive first-order load into a prospective-cell clean star. |
| Large diffuse packet mass | **STRICT-SIGN-OR-CHILD** | PX310 gives strict improvement or a clean star when `D_pkt>=12hK^2`. |
| Linear packet residue | **OPEN** | `D_pkt<12hK^2`; terminal instances are subpower-exact, but the nonterminal linear regime still needs a deterministic descent or child charge. |
| Path-forest trajectory templates | **OPEN** | Enumerate and absorb templates meeting the PX313 depth threshold. |
| Diffuse clean-star/radial linear sector | **OPEN** | The general first-order sign outside packet corrections remains to be proved. |
| Infinite exact closure | **OPEN** | No all-side product closure follows yet. |

## 1. Trajectory reset hierarchy

For a cycle-free terminal core with allowed digraph `A`:

1. an allowed cycle gives PX287;
2. a historical reverse of an allowed path gives PX294;
3. otherwise the transitive closure has at most `m Delta_0` comparable pairs;
4. longest-path levels give an antichain `Q` of order

   \[
   s\ge
   \left\lceil
   \frac{m}{\max(1,H_0)}
   \right\rceil,
   \qquad
   \binom{H_0}{2}\le m\Delta_0;
   \]

5. `Q` contains at least `s(s-1-Delta_0)` releasable historical cells;
6. a cyclic historical layer resets `Q`; otherwise every layer is a path forest
   and

   \[
   d\ge
   \left\lceil
   \frac{s(s-1-\Delta_0)}{s-1}
   \right\rceil.
   \]

The terminal obstruction is therefore a sparse poset together with a dense,
long path-forest decomposition, not an arbitrary forbidden graph.

## 2. Packet strict-sign hierarchy

Let `D_pkt` be old anchor-weighted packet mass and `K` the relevant line
occupancy bound.

1. Aggregate defects by their unique correcting transposition.
2. At correction degree threshold `R`, either a selected-point clean star has
   order at least `R/K`, or a disjoint correction matching carries weight at
   least `D_pkt/(2R-1)`.
3. Bernoulli activation of that matching has expectation

   \[
   -pW+pC_1+p^2C_2+p^3C_3.
   \]

4. A positive gap `W-C_1` forces strict improvement.
5. If prospective packet cells have no clean star of order `T`, then

   \[
   C_1<|Q|K(2T+1).
   \]

6. Taking `R=KT` proves strict improvement or a clean-star child whenever

   \[
   D_{\rm pkt}>3hK^2T^2.
   \]

In particular, PX310 leaves only `D_pkt<12hK^2` unresolved.

## Immediate frontier

1. **Linear packet residue.** Combine bounded correction weights with the exact
   terminal optimizer or a deterministic local transposition descent.
2. **Path-forest census.** Enumerate minimal no-reset coloured path-forest
   decompositions for small `Delta_0` and identify a composite two-level reset.
3. **General Bernoulli bank.** Extend PX305 from packet corrections to disjoint
   clean-star/radial endpoint moves; prove their first-order gap or structural
   child outcome.
4. **Closure conversion.** Insert the completed packet branch and the reduced
   terminal branch into the PX63 product induction.

## Verification

```bash
python scripts/verify_product_historical_backedge_antichain.py
python scripts/verify_product_packet_correction_dichotomy.py
python scripts/verify_product_packet_bernoulli_strict_sign.py
python scripts/verify_product_trajectory_depth_or_reset.py
```

All four verifiers pass locally. The classical no-three-in-line conjecture and
exact infinite product closure remain open.
