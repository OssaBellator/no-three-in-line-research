# Geometric-cleaning clean-height threshold transport

This note records GC2hx--GC2ib.  It equips the cause-to-remedy transport graph with exact nonnegative clean-height costs.

## Contract

Expand every integral cause demand into unit cause copies and every integral remedy capacity into unit remedy copies.  Compatibility is inherited from the complete physical cause/remedy graph.  Each remedy source `s` has an integer clean-height loss `h_s>=0`.

For an integer threshold `t>=1`, retain only remedy copies with `h_s<t`.  Let `nu_t` be the maximum number of cause units assignable in that threshold graph and let

`delta_t=D-nu_t`,

where `D` is total cause demand.

## Results

### GC2hx — integral clean-height assignment

If the complete cause/remedy graph pays all causes, a minimum-clean-height integral assignment exists.

### GC2hy — exact layer-cake identity

The minimum total clean-height loss is

`C_min=sum_{t>=1} delta_t`.

Only thresholds up to the maximum retained remedy cost contribute.

### GC2hz — budget witness

If `C_min>B`, some threshold has positive deficiency, and the canonical alternating Hall core at that threshold is an exact clean-height obstruction.

### GC2ia — zero-loss criterion

All causes can be paid with zero clean-height loss exactly when `delta_1=0`.

### GC2ib — infeasible transport return

If the unrestricted graph cannot assign all cause units, return the canonical cause/remedy Hall cut from GC2hs--GC2hw.  It is not charged as finite clean-height loss.

## Proof

Every assignment edge using a remedy of cost `h` contributes one unit to each threshold `t=1,...,h`.  For a fixed threshold, at least `delta_t` assigned units must use remedies of cost at least `t`.  This gives the lower bound.  The threshold graphs are nested transversal matroids, so the standard greedy augmentation chooses a full assignment whose number of edges at cost at least `t` is exactly `delta_t` simultaneously for every threshold.  Summing gives equality.

## Finite audit

Run:

`python scripts/verify_gc_clean_height_transport.py`

The deterministic audit checks:

- 5,000 cause/remedy systems;
- 2,349 feasible and 2,651 infeasible systems;
- 26,156 cause-demand units;
- 26,113 remedy-capacity units;
- 7,994 height thresholds;
- 16,654 minimum clean-height loss units;
- exactly 16,654 threshold-deficiency units.

## Scope

The theorem requires complete physical compatibility, integral capacities and additive nonnegative height loss attached to remedy sources.  It does not prove the concrete remedy graph, its capacities, or that local cleaning preserves every other invariant.  Untagged feedback and nonadditive height effects return reset.  GC5 and the no-three-in-line conjecture remain open.
