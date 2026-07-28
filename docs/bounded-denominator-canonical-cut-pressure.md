# Bounded-denominator canonical cut-pressure decomposition

This note refines the irreducible restoration-core overlap certificate on the same complete primitive-potential network. It turns the exact overlap into named pressure on the canonical arithmetic minimum cut.

## Contract

Let `C` be the canonical irreducible restoration core with deficit `delta>0`, and let `C=A disjoint_union B` be its canonical split. Proper subsets are fully payable by integral primitive-potential flows `f_A,f_B`.

For the canonical maximum flow of `C`, let `R` be the residual-reachable set. On every original forward cut arc `e: R -> V\R`, set `p_e=f_A(e)+f_B(e)-c_e`; on every reverse crossing `e: V\R -> R`, set `p_e=-(f_A(e)+f_B(e))`. Retain every physical-potential, source-potential, gain, compatibility and restoration address.

## BDA5fh--BDA5fl

1. The signed cut pressures satisfy `sum_e p_e=delta`.
2. Reverse pressures are nonpositive, so positive forward pressure totals at least `delta` and some retained arithmetic cut arc is over capacity under the two separate payments.
3. If `m` forward arcs cross the cut, the least maximum-pressure arc has pressure at least `ceil(delta/m)`.
4. A local gain or primitive-potential estimate proving all forward pressures nonpositive, or total positive pressure below `delta`, excludes the core; otherwise the exact pressure must be charged to a named physical potential source.
5. Singleton restoration cores remain direct shortages. Omitted gain fields or arcs, merged sources, changed denominator state or independent potential reuse is a reset.

## Consequence

The remaining BDA obstruction is one direct restoration shortage or one quantified physical/source-potential cut-arc overload. The arithmetic task is to rule out or pay that exact named pressure.

## Scope

This is conditional on the complete fixed network and canonical integral flows. It does not prove BDA6 or the no-three-in-line conjecture.