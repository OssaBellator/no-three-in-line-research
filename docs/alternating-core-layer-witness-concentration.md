# Alternating-core layer-witness concentration

This note records AC5bt--AC5bx. It is a deterministic reduction for the layered restricted-menu incidence envelope; it does not estimate any geometric layer parameter by itself.

## Contract

Fix a thresholded restricted-menu transport graph assembled from finitely many retained layers `i in I`. For layer `i`, retain:

- a forward-degree lower bound `d_i`;
- an exact conditioning loss `b_i`;
- an endpoint-overlap excess `o_i`;
- a reverse-load bound `D_i`.

Set

`a_i = d_i - b_i - o_i`, `A = sum_i a_i`, and `D = sum_i D_i`.

The complete-layer contract requires that the union graph has left degree at least `A` and right reverse load at most `D`. Every endpoint deletion, overlap and reverse incidence must occur in exactly one retained layer field.

## Theorem block AC5bt--AC5bx

1. The global relative deficiency is
   `eta = (1-A/D)_+` when `D>0`.
2. If every positive-load layer satisfies `a_i >= (1-epsilon)D_i`, then
   `A >= (1-epsilon)D`.
3. Conversely, if `A<D`, some positive-load layer satisfies
   `(D_i-a_i)_+/D_i >= (D-A)/D`.
4. Thus every failed global degree/reverse-load budget returns a canonical bad layer carrying at least the global relative deficiency.
5. The returned layer may be passed to the exact layer inventory. A missing layer field, negative zero-load contribution or unrecorded overlap is a model reset, not a paid obstruction.

The proof is the weighted-average identity
`sum_i (D_i-a_i) = D-A`, with negative local deficits discarded only in the favourable direction.

## Consequence

The AC5 endpoint task no longer requires estimating all layers simultaneously. It is enough to prove a uniform local ratio, or to classify and pay the least layer whose local ratio violates the desired bound. The existing threshold Hall-cost theorem and Hall-core obstruction bridge then apply unchanged.

## Finite audit

Run:

`python scripts/verify_ac_layer_witness_concentration.py`

The audit generates finite layer systems and verifies both the uniform-local-to-global implication and the exact bad-layer witness inequality.

## Scope

This result assumes the layer partition and all incidence corrections are complete. It does not prove the required geometric bounds, obstruction capacities, AC5, AC6 or the no-three-in-line conjecture.
