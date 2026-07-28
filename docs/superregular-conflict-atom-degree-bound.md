# Superregular resampling: conflict-atom degree control

## Scope

This note records SRR2aw--SRR2ba. It converts an exact local conflict-atom inventory into a deterministic weighted executable subfamily bound. It does not prove the geometric atom-load estimates for a concrete switching family.

Let `V` be the finite set of candidate switchings. Candidate `v` has weight `w_v>0` and an exact conflict-atom support `S_v`. Two candidates conflict whenever they share at least one retained atom. Let `lambda_a` be the number of candidates containing atom `a`.

## SRR2aw: degree from exact atoms

For every candidate,

`deg(v) <= sum_{a in S_v} (lambda_a-1)`.

The right side may count the same conflicting candidate more than once, so it is an upper bound without any disjointness assumption.

## SRR2ax: weighted local-minimum bound

The conflict graph has an independent executable subfamily of weight at least

`sum_v w_v/(deg(v)+1)`.

Combining with SRR2aw gives the atom-load form

`sum_v w_v/[1+sum_{a in S_v}(lambda_a-1)]`.

## SRR2ay: uniform rank/load consequence

If `|S_v|<=r` for every candidate and `lambda_a<=Lambda` for every atom, then an executable subfamily retains at least

`W/[1+r(Lambda-1)]`,

where `W=sum_v w_v`.

## SRR2az: threshold integration

The bound may be applied separately at every endpoint-cost threshold after the degree/load transportation estimate. Thus candidate weight lost to exact local conflicts is controlled by the same retained atom dictionary used to define the switching graph.

## SRR2ba: model reset

A pairwise incompatibility not represented by a retained atom, or a genuine higher-order incompatibility not implied by pairwise edges, is returned as a conflict-model reset. It is not silently charged to `Lambda`.

## Remaining frontier

The remaining geometric task is to define the complete atom set for the actual rank-two/rank-three switching family and prove small atom loads together with the forward-degree, reverse-load, perturbation, and conditioning estimates. SRR2, SRR4, and the global conjecture are not proved.