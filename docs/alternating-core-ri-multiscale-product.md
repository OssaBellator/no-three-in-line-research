# Scope-complete product comparison for coherent RI scale banks

**Branch:** `research/alternating-core-chain`

AC3dg--AC3di extract a row-column-disjoint subfamily carrying at least one thirty-first of the paid weight from any coherent scale-dispersion output. Row-column disjointness alone does not make simultaneous closed-I6 repairs legal: boundary closures, blocker auxiliaries, protected conditions, and a collinear triple meeting several scale blocks can still couple them. This note completes the interface by assigning private paid scale buckets, building the canonical AC3v repair-envelope graph, and proving the exact product comparison. Failure of the product comparison returns one of the already classified terms `F,C1,C2,C3,B` at a quantitative paid scale.

## Coherent scale records

Fix one exact normalized complete-fibre profile and all desired finite decorations. Let `S` range over represented physical base-scale cosets. Aggregate every paid complete-fibre occurrence at scale `S` into one nonnegative weight

$$
W_S.
$$

The aggregation partitions the original paid occurrence family by exact physical scale. Let `R_S` denote the complete local repair envelope for scale `S`. It contains:

- the physical source block and every I6 active cell which can occur there;
- every RI5f boundary-path column and closure cell;
- every blocker cell and auxiliary cell which can occur in a legal repair;
- every current paid factor assigned to the scale;
- every cell needed by a local feasibility, protected-bank, or collateral scope.

A scale record is one use of the full closed fixed-edge bank on `R_S`, together with its local state family and its paid bucket.

## AC3dy -- private scale-bucket payment -- PROVED

For distinct physical scale cosets `S!=T`, the aggregated paid buckets are disjoint. Give the scale record at `S` the singleton eligibility set consisting of its own paid bucket. Then every finite subfamily `X` satisfies the exact capacitated Hall identity

$$
\boxed{
|X|
=
\sum_{D\in\bigcup_{S\in X}A_S}c_D.
}
$$

Equivalently, before aggregation, assign one distinguishable capacity unit to every paid occurrence and retain only as many block-level uses as the bucket capacity permits.

Thus every selected scale has a private current-payment resource. Under the capacity-one block ticket convention, one exact scale/profile bank can be opened at most once; a second opening is an explicit repeated-scale resource event handled by AC3b--AC3e.

### Proof

Exact physical scale is one of the retained occurrence fields in AC3ay--AC3be. Aggregation by `S` is therefore a partition of the paid occurrence family. Singleton eligibility sets for distinct partition cells are disjoint, so their capacities sum to the number of selected scale records. This is the displayed Hall identity. AC3f gives the unique charge map. QED.

## Scope-complete scale graph

Start with the row-column-disjoint scale family `J_0` produced by AC3dh. Build the canonical primal graph `G_sc` on `J_0` from the full envelopes `R_S`:

1. join two scales if their envelopes share a cell;
2. join them if one potential-factor scope meets both envelopes;
3. join them if one feasibility or protected constraint meets both envelopes;
4. join them if their private paid buckets overlap.

The fourth condition is vacuous after AC3dy but is retained for compatibility with AC3w.

## AC3dz -- paid scale bank or finite scoped overload -- PROVED

Let the original coherent scale-dispersion family have total paid weight `W`. For every real `K>=1`, one of the following holds.

1. **Scoped paid overload.** One scale `S` has closed-neighbourhood paid load
   $$
   \boxed{
   L(S)>K W_S.
   }
   $$
   AC2d localizes the overload to one finite envelope/factor/constraint incidence label.
2. **Scope-complete multiscale bank.** There is an independent family `I` in `G_sc` with
   $$
   \boxed{
   \sum_{S\in I}W_S
   \ge
   \frac{W}{31K}.
   }
   $$
   Its envelopes and paid buckets are disjoint, every local state installs jointly, and both destroyed payment and created collateral are exactly additive.

### Proof

AC3dh first selects `J_0` with paid weight at least `W/31`. Apply AC2c with parameter `K` to the weighted graph `G_sc`. Its overload alternative is conclusion 1. Otherwise it returns an independent family carrying at least `1/K` of the weight of `J_0`. AC3dy and AC3w give exact payment additivity; AC3v gives joint legality and exact potential additivity. QED.

## Local closed-I6 ledgers

For each selected scale `S`, let

$$
\alpha_S=1-\frac1{m_Sh_S}\ge\frac12
$$

be its paid fixed-edge destruction coefficient. Let

$$
F_S,
\qquad
C_{1,S},C_{2,S},C_{3,S},
\qquad
B_S
$$

be the exact local expected collateral terms in AC3bh, including the complete state-independent union term in `F_S`. Define

$$
G_S=\alpha_S W_S,
$$

$$
H_S=F_S+C_{1,S}+C_{2,S}+C_{3,S}+B_S,
$$

and local expected net gain

$$
\gamma_S=G_S-H_S.
$$

Positive `gamma_S` means that the local bank has negative expected potential drift by `gamma_S`.

## AC3ea -- exact multiscale product expectation -- PROVED

Let `I` be independent in `G_sc`. Choose the local active and conditional blocker state at every `S in I` independently according to its exact closed-I6 bank distribution. Then

$$
\boxed{
\mathbb E[\text{total destroyed paid weight}]
=
\sum_{S\in I}G_S,
}
$$

$$
\boxed{
\mathbb E[\text{total created collateral}]
=
\sum_{S\in I}H_S,
}
$$

and hence

$$
\boxed{
\mathbb E[\text{net paid gain}]
=
\sum_{S\in I}\gamma_S.
}
$$

If

$$
\sum_{S\in I}\gamma_S>0,
$$

one legal product state strictly lowers the paid triple potential.

### Proof

For every deterministic choice of one local state per selected scale, AC3v gives the exact before-and-after potential identity as the sum of the local changes, while AC3w gives exact destroyed-payment additivity. Taking expectation over the finite product distribution preserves the sum. A positive expected gain implies that at least one product state has positive gain. QED.

No independence of individual collateral factors is assumed. The canonical primal graph has already excluded every factor or constraint that could meet two selected envelopes.

## AC3eb -- failed multiscale product router -- PROVED

Retain a scope-complete bank `I` of paid weight

$$
W_I=\sum_{S\in I}W_S.
$$

If no product state improves, then

$$
\sum_{S\in I}H_S
\ge
\sum_{S\in I}G_S
\ge
\frac{W_I}{2}.
$$

Therefore at least one of the five aggregated terms

$$
\sum_SF_S,
\quad
\sum_SC_{1,S},
\quad
\sum_SC_{2,S},
\quad
\sum_SC_{3,S},
\quad
\sum_SB_S
$$

has weight at least

$$
\boxed{
\frac{W_I}{10}.
}
$$

Combined with AC3dz, a coherent scale-dispersion class of original paid weight `W` returns either:

1. an improving legal multiscale product state;
2. one finite scoped overload label;
3. or one named aggregate RI term of weight at least
   $$
   \boxed{
   \frac{W}{310K}.
   }
   $$

The selected aggregate term retains its exact scale on every occurrence and re-enters its proved local router:

- `F` enters AC3cc--AC3da;
- `C1` enters AC3bp--AC3bs;
- `C2,C3` enter AC3bt--AC3cb;
- `B` enters AC3bk--AC3ct.

### Proof

If no deterministic product state improves, the product expectation in AC3ea is nonpositive, giving `sum H_S>=sum G_S`. Nontriviality of every closed bank gives `m_Sh_S>=2`, hence `alpha_S>=1/2` and `sum G_S>=W_I/2`. Pigeonhole the five nonnegative term types. Finally use `W_I>=W/(31K)` from AC3dz. QED.

## Consequence

The coherent scale-dispersion branch no longer stops after row-column extraction. It now has:

- private scale payment and one finite ticket per exact scale/profile bank;
- a complete repair-envelope conflict graph;
- an exact simultaneous product comparison;
- and a quantitative failed-product return to one already classified RI term.

The remaining multiscale work is arithmetic termination of the resulting overload or named aggregate profile, not another simultaneous-installation or payment lemma.

## Finite check

`scripts/verify_ac_ri_multiscale_product.py` exhausts small paid scale partitions and Hall subfamilies, weighted conflict graphs through five vertices, finite local-state product distributions, and failed-bank five-term ledgers. It checks the `1/(31K)` extraction, exact product expectation, the `1/10` failed-product split, and the composed `1/(310K)` constant.