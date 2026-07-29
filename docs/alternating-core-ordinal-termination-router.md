# Alternating-core ordinal termination router

## Status

This note keeps AC as the sole active research focus and proves AC5jp--AC5ju. It strengthens the nested-box closure argument by removing the need for uniform maxima of the state-space potential. Uniform maxima remain useful for the explicit numerical bound of AC5jn, but qualitative termination follows from a global lexicographic rank and only finitely many occurrence-faithful exceptional events.

The result remains contract-qualified. It does not construct the physical edge stratification, prove the global rank extension, prove that the exceptional physical-address universe is finite, prove AC6, or prove the no-three-in-line conjecture.

## Global state rank

Assume the cofinal direct-limit graph of AC5jb and an overlap-preserving nonnegative integer repair rank

\[
\rho:V_\infty\longrightarrow\mathbb N
\]

from AC5jj on all scheduled repair-progress edges. Every physical state also retains synchronized deficit `Delta(v)` and restart potential `Theta(v)` as nonnegative integers.

Define the lexicographic rank tuple

\[
L(v)=(\Delta(v),\Theta(v),\rho(v))
\]

and, equivalently, the ordinal

\[
\boxed{
\Phi(v)=\omega^2\Delta(v)+\omega\Theta(v)+\rho(v)<\omega^3.
}
\]

No global upper bound on the three coefficients is assumed.

## AC5jp -- exact internal edge stratification -- PROVED

Every nonterminal internal edge is assigned exactly one of the following types from its complete operation record.

1. **Supply:**
   \[
   \Delta(v')<\Delta(v).
   \]
2. **Credited restart:**
   \[
   \Delta(v')=\Delta(v),
   \qquad
   \Theta(v')<\Theta(v),
   \]
   with zero unaccounted activation mass.
3. **Repair:**
   \[
   \Delta(v')=\Delta(v),
   \quad
   \Theta(v')=\Theta(v),
   \quad
   \rho(v')<\rho(v).
   \]
4. **Exceptional:** one occurrence-faithful payment, ticket, disturbance or funded reset address is consumed.

The compiler rejects the least edge that:

- is labelled supply without lowering `Delta`;
- is labelled credited restart while changing `Delta`, failing to lower `Theta`, or inserting unaccounted mass;
- is labelled repair while changing an earlier component or failing to lower `rho`;
- is labelled exceptional without one live globally addressed occurrence;
- receives two types or no type.

### Proof

The complete source, target and operation records decide all displayed equalities, inequalities, mass fields and consumed addresses. The ordered type rules are mutually exclusive after the first differing rank component is identified. QED.

## AC5jq -- strict ordinal descent of every progress edge -- PROVED

Every supply, credited-restart or repair edge strictly decreases `Phi`.

- A supply edge decreases the coefficient of `omega^2`; arbitrary finite changes in the lower coefficients cannot compensate.
- With equal deficit, a credited restart decreases the coefficient of `omega`; arbitrary finite repair-rank change cannot compensate.
- With equal deficit and restart potential, a repair edge decreases the finite coefficient.

Equivalently,

\[
L(v')<_{\rm lex}L(v).
\]

There is no infinite sequence consisting only of progress edges.

### Proof

The three cases are the definition of lexicographic order on `N^3` and ordinal comparison below `omega^3`. Ordinals are well-founded, so no infinite strict descent exists. QED.

## AC5jr -- finite globally exceptional event stock -- PROVED UNDER THE PHYSICAL-ADDRESS CONTRACT

Let `A_exc` be one finite set of globally unique occurrence addresses for:

- payments;
- threshold and recreation tickets;
- exogenous disturbances;
- funded resets.

Each address `a` has a finite nonnegative multiplicity `c(a)`, and every exceptional edge consumes one previously live unit. Repeated references from different templates or boxes are aliases of the same address.

Then the total number of exceptional edges in any physical trajectory is at most

\[
\boxed{C_{\rm exc}=\sum_{a\in A_{\rm exc}}c(a).}
\]

An address reused after exhaustion, split into aliases, assigned conflicting stocks or types, increased without a named deposit, or introduced outside the declared global universe is returned as the first exceptional-stock obstruction.

### Proof

Occurrence-faithful debits inject exceptional edge occurrences into the finite multiset containing `c(a)` copies of every global address. Alias references do not add copies. QED.

## AC5js -- direct-limit termination without uniform state maxima -- PROVED

Assume:

1. the physical box tower is cofinal;
2. the repair rank extends globally and overlap-preservingly;
3. AC5jp accepts every nonterminal internal edge;
4. AC5jr supplies finite global exceptional stock;
5. terminal, shortage, amplification, monotone-escape and unfunded-schema-reset records leave the internal nonterminal graph.

Then no infinite nonterminal physical AC trajectory exists.

### Proof

Suppose an infinite trajectory existed. By AC5jr, at most `C_exc` of its edges are exceptional. Delete the finite prefix ending at the last exceptional edge. Every later edge is supply, credited restart or repair and therefore strictly decreases `Phi` by AC5jq. This gives an infinite descending ordinal sequence, impossible. QED.

This argument does not require a uniform maximum of `Delta`, `Theta` or `rho` over all boxes. Each individual state has finite coefficients, and only finitely many exceptional jumps can increase them.

## AC5jt -- state-dependent termination certificate and numerical refinement -- PROVED

For one starting state `v_0`, the ordinal value `Phi(v_0)` together with the remaining exceptional multiset is a complete qualitative termination certificate.

If uniform finite coefficient bounds are additionally available, AC5jn converts the ordinal argument into the explicit numerical episode envelope `E_bar`. Without those bounds the ordinal theorem still proves termination but does not claim one uniform natural-number bound valid for every possible starting state in the direct limit.

More generally, after each exceptional edge `e_j` let `v_j` be the new state. The complete finite certificate is the finite list

\[
\bigl((e_1,\Phi(v_1)),\ldots,(e_s,\Phi(v_s))\bigr),
\qquad s\le C_{\rm exc},
\]

plus strict ordinal descent on every interval between these events.

### Proof

Each interval contains only progress edges and hence terminates by well-foundedness. There are finitely many intervals because the exceptional list is finite. AC5jn is the bounded-coefficient numerical specialization. QED.

## AC5ju -- sharpened AC6 obstruction router -- PROVED

Under the bounded-epoch and frontier compilers already established, failure of AC5js returns the first of:

1. a noncofinal physical coordinate or omitted finite trajectory state;
2. a progress-rank cycle or overlap violation from AC5jk;
3. a supply, restart or repair edge failing its rank-component inequality;
4. an exceptional edge without a live physical occurrence;
5. an infinite, relabelled or conflicting exceptional-address universe;
6. an internal edge receiving no valid stratification;
7. a boundary record incorrectly kept internal;
8. a bounded-box template, source, compatibility or boundary-certificate failure.

Uniform divergence of state maxima is no longer an obstruction to qualitative termination. It matters only when an explicit global natural-number episode bound is desired.

### Proof

The list is the ordered negation of AC5js and the prerequisite compilers. AC5jq removes coefficient unboundedness from the qualitative hypothesis, while AC5jr isolates the only permitted nondecreasing interruptions. QED.

## Deterministic audit

`scripts/verify_ac_ordinal_termination_router.py` checks 2,500 generated systems. It verifies:

- exact supply, credited-restart, repair and exceptional stratification;
- strict lexicographic decrease of every progress edge;
- finite global exceptional-address deduplication;
- termination of trajectories with finitely many exceptional jumps;
- canonical failures for a nondecreasing progress edge, conflicting address or unbounded exceptional universe.

## Main AC frontier

Only AC remains active. The remaining physical route to AC6 is now shorter:

1. extract `Delta`, `Theta` and the overlap-preserving rank from actual AC states;
2. stratify every physical internal edge by AC5jp;
3. discharge every returned mislabeled or unclassified edge;
4. declare and conserve the finite global exceptional occurrence universe;
5. prove the bounded-box tower cofinal;
6. apply AC5js for qualitative termination;
7. use AC5jn only if a uniform numerical episode bound is also required.

AC6 and the global no-three-in-line conjecture remain open.
