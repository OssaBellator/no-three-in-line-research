# Superregular weighted atom-burden concentration

This note records SRR2bq--SRR2bu. It localizes large weighted conflict burden to one exact witnessed interaction atom and gives an average-degree execution bound.

## Contract

Let `G` be the complete pairwise shadow of the feasible switching conflict hypergraph. Candidate `v` has positive weight `w_v`. Every shadow edge has one retained witness atom from a finite dictionary `A`, and every witness atom is present in both endpoint supports.

For each atom `a`, define its weighted burden

`L_a = sum_{uv witnessed by a} (w_u + w_v)`.

Let `W = sum_v w_v` and `B = sum_v w_v deg(v)`.

## Theorem block

### SRR2bq — exact burden partition

`B = sum_a L_a`.

### SRR2br — heavy atom localization

If `B > 0`, some exact witness atom satisfies `L_a >= B/|A|`. The least maximizing atom is canonical.

### SRR2bs — weighted average-degree execution

The weighted local-minimum argument and Cauchy--Schwarz give an executable independent family of weight at least

`W^2/(W+B)`.

### SRR2bt — uniform atom-burden corollary

If every exact atom has burden at most `M`, then `B <= |A|M` and the executable weight is at least

`W^2/(W+|A|M)`.

### SRR2bu — reset boundary

An unwitnessed conflict edge, an omitted interaction atom, negative candidate weight, or a higher-order incompatibility absent from the complete shadow returns reset.

## Proof

Each edge contributes `w_u+w_v` once to `B` and once to the burden of its retained witness atom, proving SRR2bq. Averaging proves SRR2br. The random-priority bound is `sum_v w_v/(deg(v)+1)`; weighted Cauchy--Schwarz gives at least `W^2/(W+B)`.

## Remaining physical work

The result reduces conflict control to constructing the complete geometric witness-atom dictionary and bounding each exact weighted atom burden.