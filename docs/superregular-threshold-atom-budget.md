# Superregular threshold atom-budget composition

This note records SRR2bv--SRR2bz. It turns exact witness-atom burden into a threshold-local executable-weight criterion.

## Contract

At one fixed endpoint-cost threshold, let `G=(V,E)` be the complete conflict graph of feasible switching candidates. Candidate `v` has nonnegative weight `w_v`. Every conflict edge has one retained witness atom from a finite exact dictionary.

For an atom `a`, define its burden by

`B_a = sum_{uv in E witnessed by a} (w_u+w_v)`.

Let `C_a` be a proposed nonnegative atom budget.

## SRR2bv — exact burden partition

Writing `deg(v)` for conflict degree,

`sum_a B_a = sum_v w_v deg(v)`.

Thus no conflict burden is lost when edges are assigned to exact witness atoms.

## SRR2bw — atom-budget dichotomy

Either `B_a<=C_a` for every atom, giving

`sum_v w_v deg(v) <= sum_a C_a`,

or the least atom with `B_a>C_a` is an exact local burden overload.

## SRR2bx — executable-weight bound

Put `W=sum_v w_v` and `B=sum_v w_v deg(v)`. Random-priority thinning and Cauchy--Schwarz give an executable independent family of weight at least

`W^2/(W+B)`.

Under the atom budgets this is at least

`W^2/(W+sum_a C_a)`.

## SRR2by — threshold composition

If the same threshold already retains endpoint weight `W_t`, then exact atom budgets at that threshold may be inserted directly into the endpoint-cost/conflict composition theorem. A small total atom budget yields a positive executable low-cost family.

## SRR2bz — reset boundary

Unwitnessed conflicts, one edge assigned to no atom or several atoms without a fixed partition, omitted higher-order conflicts, negative weights or threshold-changing candidate identities return reset.

## Finite audit

Run:

`python scripts/verify_srr_threshold_atom_budget.py`

The deterministic audit checks 3,500 weighted conflict systems, 19,415 candidates, 14,828 edges, 9,164 atom classes and 3,500 brute-force maximum-independent-weight comparisons.

## Scope

The theorem does not construct the geometric witness-atom dictionary or prove the budgets `C_a`. It gives the exact quantitative endpoint once per-atom geometric burden estimates are available. SRR2, SRR4 and the no-three-in-line conjecture remain open.
