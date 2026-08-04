# Autoprompter continuity handoff

Checkpoint time: 2026-08-04T21:18:00+10:00 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line program
across boundary, Hall, threshold, prefix, shell, and integration frontiers. The
all-`n` theorem remains open. Finite corrected chains, conditional packing
interfaces, algebraic hidden mixtures, and finite coordinate lifts are not
all-length coordinate constructions.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Canonical completed tranches: `docs/651--656`, `docs/657--662`,
  `docs/663--668`, `docs/669--674`, `docs/675--680`, and `docs/681--686`.
- In-progress tranche: `docs/687--692`.
- Completed in current tranche: boundary `docs/687`, Hall `docs/688`, threshold
  `docs/689`, prefix `docs/690`, shell `docs/691`.
- Current theorem range in this tranche: `PP3ddt--PP3deh`.
- Next available theorem identifier: `PP3dei`.
- Latest shell theorem commit before this continuity update:
  `2fe5c59d118e2040ba98f1e9076c1130f184c8dd`.

## Current tranche progress

### Boundary — `docs/687-nineteenth-low-frontier-budget-six-obstruction.md`

Theorems `PP3ddt--PP3ddv`.

- The 13 minimum-five attempts contain 68 minimum cores; the 46 minimum-six
  attempts contain 442 minimum cores.
- Every minimum-five core is uncorrectable at budgets five and six; every
  minimum-six core is uncorrectable at budget six.
- Exact new rejected replacement counts total `4,405,440`.
- Together with `docs/681`, all 60 raw attempts and all 515 minimum cores with
  transversal at most six are obstructed through deletion budget six.
- Any corrected nineteenth transition needs budget at least seven, a raw attempt
  of minimum at least seven, or a changed repertoire/state representation.

Reproducibility: `scripts/check_boundary_nineteenth_low_frontier_obstruction.py`.

### Hall — `docs/688-hall-packet-transfer-matrix.md`

Theorems `PP3ddw--PP3ddy`.

- Exact left/right boundary occupancy tables compose by a max-plus transition
  matrix; a `K`-packet chain has exact retained count
  `max_B (v tensor M^(K-1))[B]`.
- The asymptotic retained count per packet is the maximum cycle mean of the
  reachable transfer-state graph.
- The checker exhausts all 1,024 simple five-vertex packets and verifies 4,096
  packet-chain values against direct maximum independent sets.
- Exact transfer improves uniform interface charging in 3,060 checks, by as much
  as six vertices at four copies.
- A smallest strict Hall example reaches 28 centres in nine packets rather than
  thirteen under the additive charge.

Reproducibility: `scripts/check_hall_packet_transfer_matrix.py`.

### Threshold — `docs/689-threshold-identity-window-density.md`

Theorems `PP3ddz--PP3deb`.

- Among all 126 four-layer type multisets from `{I,P1,...,P5}`, all 70
  identity-free types are legal and all 56 identity-containing types are illegal.
- A cyclic schedule of `K` minimum batches has at most `5K-3` legal four-windows;
  a contiguous identity block attains the bound.
- The exact minimum illegal-window count is `3K+3`; the optimal asymptotic legal
  density is `5/8`.
- Exhaustive identity-position censuses for `K=1,2,3` contain 56, 8,008, and
  1,307,504 cases and attain maxima 2, 7, and 12.

Reproducibility: `scripts/check_threshold_identity_window_density.py`.

### Prefix — `docs/690-all-optimal-prefix-short-compositions.md`

Theorems `PP3dec--PP3dee`.

- The complete physical family contains 104 minimum-crossing matchings, two
  deletion classes, and exactly 144 optimal radius-four routes per case.
- Every optimal route succeeds for every ordered composition of eleven with at
  most three runs; there are 56 such compositions.
- The exact audit contains `1,677,312` coordinate embeddings with no failures or
  mixed-run collinear triples.
- Uniform maximum coordinates are 120 for deletion `{0,2}` and 154 for deletion
  `{3,5}`.

Reproducibility: `scripts/check_prefix_all_optimal_short_compositions.py`.

### Shell — `docs/691-shell-connector-augmentation.md`

Theorems `PP3def--PP3deh`.

- The exact connector problem for disconnected positive support is the minimum-cost
  nonnegative integer augmentation satisfying componentwise balance and all
  directed cut constraints.
- After directed shortest-path closure, the optimum equals the minimum directed
  Hamiltonian-tour cost; shortest connector paths can be strictly cheaper than a
  direct-edge tour.
- If one disconnected positive bundle has robust gain `G`, optimal connector loss
  is `L*`, and setup is `S`, the least repetitions are
  `floor((S+L*)/G)+1`.
- The checker exhausts all 729 three-component directed cost matrices with costs in
  `{1,2,3}`; the balanced augmentation and metric-tour optima agree in every case.
- Metric closure strictly improves direct tours in three cases, by one unit.

Reproducibility: `scripts/check_shell_connector_augmentation.py`.

## Prior canonical tranche: `docs/681--686`

- Boundary: the unique minimum-four nineteenth attempt has five cores, all
  obstructed through budget six.
- Hall: defect-incidence line graphs give exact degree-two odd-path retention and
  safe additive packet-interface bounds.
- Threshold: 19,834 minimum endpoint batches share one rigid primitive aggregate
  with twelve identity layers.
- Prefix: all 104 physical matchings and all 1,024 compositions pass the
  deterministic first optimal route, totaling 212,992 audits.
- Shell: robust circulation is an exact rational LP; connected balanced support
  clears to one Euler walk and disconnected support pays an unspecified connector
  loss.
- Integration: candidate completion is `25/30`; all rows remain
  `fixture_derived`; no row is promoted; fixed point and slack are unchanged;
  geometric closure is false.

Theorems in that tranche are `PP3ddb--PP3dds`.

## Validation status

- Boundary, Hall, threshold, prefix, and shell standalone audits passed in isolated
  local execution in roughly five, one, nine, twenty-eight, and one second.
- The complete historical chained runner remains unavailable because a full local
  checkout cannot be obtained; direct clone attempts cannot resolve `github.com`.

## Decisions

- Treat executable checker output and independent exact reconstruction as
  authoritative when stale prose or assertions disagree.
- Do not search boundary budget seven naively; require symmetry, exact-cover,
  repeated-row, or state-signature pruning.
- Use the exact Hall transfer matrix when packet boundary states are available.
- Treat the threshold `5/8` density as an obstruction for the forced rolling
  four-window alphabet, not for larger windows or genuinely hidden operations.
- Treat the prefix all-route theorem as bounded to compositions with at most three
  runs and the fixed thirteen-pair source.
- Use directed metric closure before charging shell connector loss.
- Preserve one canonical theorem chapter, checker, certificate, and parity row per
  frontier number.
- Promote no row without a recurrent or asymptotic coordinate source path.

## Current blockers

- Boundary: every raw minimum core with transversal at most six is obstructed
  through budget six; no corrected nineteenth transition exists.
- Hall: no coordinate packet family supplies actual resource lists, defect labels,
  packet boundaries, and repeatable geometric transfer states.
- Threshold: minimum-batch rolling schedules retain illegal exposure density at
  least `3/8`; no larger-window or genuinely hidden operation is known.
- Prefix: 968 longer compositions remain unaudited for all 144 routes; there is no
  recurrence between source sizes.
- Shell: no coordinate macro graph supplies the positive components, connector
  costs, and robust burden polytope required by the exact augmentation theorem.
- Integration: all rows and coupling coefficients remain fixture-derived.

## Uncommitted work

- No completed repository change is intentionally left only in chat.
- Failed exploratory searches and unproved budget-seven repairs are not promoted.

## Exact next steps

1. Continue theorem numbering at `PP3dei` and build `docs/692`.
2. Integration: update the evidence gate, certificate, parity supplement, and
   chained runner; preserve `25/30`, the fixed point, and closed gate absent a
   promoted coordinate path.
3. Begin the next tranche at `PP3del` only after the canonical `687--692` map and
   runner are verified.
4. Run the complete historical chain when a full checkout becomes available,
   verify the remote head, and refresh this handoff.

## Conventions

Continue on `research/all-n-prime-patching`; use exact arithmetic and reviewable
commits; commit each completed logical unit promptly; separate candidate completion
from geometric evidence; and state explicitly that the all-`n` theorem remains open.
