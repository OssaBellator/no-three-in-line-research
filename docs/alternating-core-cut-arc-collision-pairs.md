# Alternating-core cut-arc collision pairs

This note refines the canonical cut-pressure theorem on the same complete physical/source/certificate network. It converts every named positive-pressure arc into explicit pairs of separately payable defect units that both require that exact capacity.

## Contract

Let `C=A disjoint_union B` be the canonical split of a non-singleton irreducible defect core. Choose the deterministic integral full flows `f_A,f_B` for the two proper subsets, cancel directed flow cycles lexicographically, and then decompose each remaining flow into lexicographically ordered unit source-to-terminal paths. Every path retains its exact defect-unit address and every physical-source, issued-source, certificate and compatibility arc that it uses.

Fix a forward arc `e` of the canonical core minimum cut with capacity `c_e` and positive pressure

`p_e=f_A(e)+f_B(e)-c_e>0`.

## AC5eb--AC5ef

1. **Canonical path decomposition.** The cycle-cancelled integral side flows decompose into unit paths, and exactly `f_A(e)` paths from side `A` and `f_B(e)` paths from side `B` traverse `e`.
2. **Exact collision count.** Since each side flow separately respects `c_e`, `p_e<=min(f_A(e),f_B(e))`. Ordering the `c_e` capacity slots, assigning the `A` paths from the first slot upward and the `B` paths from the last slot downward produces exactly `p_e` doubly occupied slots.
3. **Canonical collision witnesses.** Each doubly occupied slot gives one ordered pair of exact defect-unit paths, one from each side, sharing the complete arc address `e`. The least slot gives a canonical pair together with both path prefixes and suffixes.
4. **Endpoint-class concentration.** If the colliding `A` paths use `a_e` exact defect classes and the colliding `B` paths use `b_e` exact defect classes, one ordered class pair occurs at least `ceil(p_e/(a_e b_e))` times.
5. **Router and reset boundary.** A geometric argument forbidding every cross-side path pair on `e`, or bounding all retained class-pair multiplicities below the required total, excludes the core. Singleton cores remain direct shortages. Omitted path arcs, suppressed terminal units, merged capacities, uncancelled circulation, changed physical state or independent capacity reuse is a reset.

## Consequence

The remaining AC5 obstruction is no longer only an overloaded cut arc. It is one direct defect shortage or one exact pair of separately payable defect paths that collide on a named physical/source/certificate capacity, with a quantified multiplicity when classes repeat.

## Scope

This is conditional on the complete fixed network and deterministic integral flows. It does not construct the geometric compatibility graph and does not prove AC4, AC5, AC6 or the no-three-in-line conjecture.