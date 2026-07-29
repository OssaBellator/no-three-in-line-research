# Frontier pass: AC frontier manifest compiler

## Active branch

`agent/ac-frontier-manifest-compiler`

Parent: `agent/ac-all-n-inspired-descent` at `96e1194e11fe8bb8cc690f31df5b9b3a5ac025cd`.

Only AC is active. All other branches remain immutable source libraries.

## Theorem block

- **AC5hy:** exact finite frontier-manifest identity and task coverage.
- **AC5hz:** total semantic compilation or exact semantic deficit.
- **AC5ia:** certified repair-graph compilation, reachability and exact minimax constants.
- **AC5ib:** zero-mass restart and unique typed-capacity compiler.
- **AC5ic:** deterministic AC scheduler and complete finite episode bound.

## Main gain

The preceding AC audits verified semantic bases, repair ranks, restarts and potentials on separate synthetic objects. This pass requires one coherent manifest containing all of them. A manifest is accepted only when the same tagged schemas, pair universes, compatibility values, states, transitions, footprints, restart masses and capacity addresses agree globally.

A valid manifest produces:

\[
E
\le
(C_{\rm reset}+1)\Psi_*
+
UW_{\rm dist}
+
C_{\rm pay}
+
C_{\rm ticket}.
\]

An invalid manifest returns the least typed discrepancy. Partial acceptance is forbidden.

## Deterministic audit

Equivalent execution of `scripts/verify_ac_frontier_manifest_compiler.py` checks 2,500 manifests:

- 209 valid complete manifests;
- 209 missing-track witnesses;
- 209 uncovered-pair witnesses;
- 209 semantic conflicts;
- 208 stale-key witnesses;
- 208 omitted-field witnesses;
- 208 shared-state disagreements;
- 208 unsound-key private witnesses;
- 208 malformed-edge witnesses;
- 208 unreachable-state witnesses;
- 208 positive-mass activation witnesses;
- 208 duplicate-capacity witnesses.

On the valid manifests it compiles:

- 20,303 tagged semantic pairs;
- 5,957 irredundant basis keys;
- 5,957 private witnesses;
- 3,244 repair states;
- 3,035 strict minimax moves;
- 3,830 restart-credit units;
- aggregate `Psi_*` 3,285,903;
- aggregate episode bound 13,314,334;
- payment capacity 2,494;
- ticket capacity 1,043;
- reset capacity 642.

All assertions pass.

## Remaining AC6 obligations

1. Build the physical seven-track manifest.
2. Drive semantic deficit to zero.
3. Enumerate the complete physical repair graph and terminal set.
4. Compute exact minimax and mixed-radix constants.
5. Prove zero-mass activation or fund every restart.
6. Enumerate unique physical capacities.
7. Run AC5ic and discharge its first returned obstruction.

AC6 and the global no-three-in-line conjecture remain open.
