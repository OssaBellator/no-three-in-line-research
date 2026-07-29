# Frontier pass: AC ordinal termination router

## Active branch

`agent/ac-ordinal-termination-router`

Parent: `agent/ac-tower-rank-extension` at `cd0c77dc2e52fa5bb9a5a4546fff4eee11fc8fdb`.

Only AC is active. Historical AC, RI, BDA, GC, OP, SRR, SAS and all-n branches remain immutable source libraries.

## New theorem block

- **AC5jp:** exact supply, credited-restart, repair and exceptional edge stratification.
- **AC5jq:** strict descent of the ordinal `omega^2 Delta + omega Theta + rho` on every progress edge.
- **AC5jr:** finite globally deduplicated exceptional occurrence stock.
- **AC5js:** direct-limit termination without uniform state maxima.
- **AC5jt:** state-dependent ordinal certificate and numerical specialization.
- **AC5ju:** sharpened AC6 obstruction router.

## Logical gain

Uniform maxima of deficit, restart potential and repair rank are no longer required for qualitative termination. The state rank

\[
\Phi(v)=\omega^2\Delta(v)+\omega\Theta(v)+\rho(v)
\]

strictly decreases on every supply, credited-restart or repair edge. Payment, ticket, disturbance and funded-reset edges may interrupt this descent only by consuming one unit from a finite globally addressed exceptional stock.

After the last exceptional edge, any infinite trajectory would be an infinite descending sequence of ordinals below `omega^3`, which is impossible. Uniform coefficient bounds remain useful only for the explicit natural-number episode bound of AC5jn.

## Deterministic audit

Equivalent execution of `scripts/verify_ac_ordinal_termination_router.py` checks 2,500 systems:

- valid progress edges: `64,249`;
- supply edges: `20,868`;
- credited-restart edges: `21,227`;
- repair edges: `22,154`;
- sampled exceptional edges: `35,259`;
- valid finite-stock systems: `1,000`;
- globally unique exceptional stock: `16,331`;
- raw aliased exceptional references: `40,851`;
- alias amount removed: `24,520`;
- simulated progress steps: `14,841`;
- simulated exceptional interruptions: `1,309`;
- total terminating trajectory steps: `16,150`;
- nondecreasing progress-edge failures: `500`;
- conflicting exceptional-address systems: `500`;
- unbounded exceptional-address-universe systems: `500`.

All assertions pass.

## Remaining AC frontier

1. Stratify every actual physical internal edge.
2. Extend the repair rank consistently across the physical tower.
3. Compile the finite global exceptional occurrence universe.
4. Prove cofinality.
5. Apply AC5js, retaining the first AC5ju witness if a contract fails.

AC6 and the global no-three-in-line conjecture remain open.
