# Alternating-core canonical cut-pressure decomposition

This note refines the irreducible-core overlap certificate on the same complete finite integral payment network. It does not construct the geometric network; it turns the exact overlap into named pressure on the canonical minimum cut.

## Contract

Let `C` be the canonical irreducible defect core, with deficit `delta>0`, and let `C=A disjoint_union B` be the canonical split from the preceding block. Every proper subset is payable, so there are full integral flows `f_A` and `f_B` of values `d(A)` and `d(B)`.

Run the canonical maximum-flow algorithm for `C`. Let `R` be the residual-reachable vertex set and let `K+` and `K-` be the original arcs crossing `R -> V\R` and `V\R -> R`. For `e in K+` put

`p_e=f_A(e)+f_B(e)-c_e`,

and for `e in K-` put

`p_e=-(f_A(e)+f_B(e))`.

All physical-source, issued-source, certificate, compatibility and defect addresses are retained.

## AC5dw--AC5ea

1. **Exact signed pressure identity.** The canonical cut has capacity `F(C)=d(C)-delta`, and flow conservation gives
   `sum_{e in K+ union K-} p_e = delta`.
2. **Positive forward witness.** Reverse pressures are nonpositive. Hence the sum of positive pressures on forward cut arcs is at least `delta`; in particular at least one retained forward arc is used above capacity by the two separate full payments.
3. **Heavy canonical arc.** If `m=|K+|`, the least forward arc attaining maximum pressure has
   `p_e >= ceil(delta/m)`.
4. **Physical exclusion route.** Any geometric estimate proving `p_e<=0` on every forward cut arc, or proving total positive pressure below `delta`, excludes the core. A named source account may instead pay that exact pressure.
5. **Singleton and reset clauses.** A singleton core remains a direct shortage. Omitted arcs, merged capacities, suppressed stage/type data, changed physical state or independent reuse of shared capacity is a reset.

## Consequence

The remaining AC5 obstruction is now either a direct singleton shortage or one named physical/source/certificate cut arc with quantified simultaneous pressure. The physical task is to prove that pressure impossible, bound it below the required threshold, or debit it from an occurrence-faithful source.

## Scope

This statement is conditional on the complete fixed network and canonical integral flows. It does not prove AC4, AC5, AC6 or the no-three-in-line conjecture.