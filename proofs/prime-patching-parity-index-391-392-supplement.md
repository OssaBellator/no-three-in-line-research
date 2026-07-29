# Prime-patching parity index supplement: `docs/391--395`

This cumulative supplement extends `proofs/prime-patching-parity-index.md`
without replacing its complete history through `docs/390`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bvj--PP3bvl | Joining boundary components has zero cost for aligned majorities and penalty `min(|I_R|,|I_S|)` for opposing majorities; forest recleaning cost telescopes over merge penalties | PROVED | `docs/391-exact-component-merge-calculus-for-boundary-recleaning.md` |
| PP3bvm--PP3bvo | The thirteen violating `m=10` transition count maxima have an exact source-mass/capacity-deficit profile; all mean source masses lie in `[64,128]` | PROVED / VERIFIED FINITELY | `docs/392-exact-m10-hall-transition-count-maximizer-source-mass.md` |
| PP3bvp--PP3bvr | Direct-clean fractional reverse load equals the exact source-set expansion ratio; every rational optimum has a finite fractional layer-bank realization | PROVED | `docs/393-fractional-layer-banks-and-exact-expansion-for-direct-clean-repair.md` |
| PP3bvs--PP3bvu | Independent source and target potentials give an exact two-sided Schur variational formula for localized Hall congestion and an inverse-support criterion | PROVED | `docs/394-two-sided-schur-potentials-for-localized-hall-congestion.md` |
| PP3bvv--PP3bvx | If only `q` nonterminal shell boundaries expand and each is at most `B`, full charge is at most `tau B^q`; exact strong-shell allowances are audited through `m=10` | PROVED / VERIFIED FINITELY (CONDITIONAL ON NONTERMINAL BOUNDS) | `docs/395-sparse-expansive-shell-criteria-through-m10.md` |

## Frontier update

For component-local recleaning, a feasible constraint joining two current
components costs nothing when their weighted majority phases align and otherwise
costs exactly the smaller absolute imbalance. The structural covering-rotation
target is therefore a boundary forest with few opposing-majority merges,
preferably only against low-imbalance components or with every boundary variable
pinned to zero.

For direct-clean repair, the optimal fractional reverse load is exactly

```text
max_(nonempty A subseteq S) |A|/|N(A)|.
```

Every rational optimum is a finite `(L,r)` layer bank of deterministic repair
maps with load `r/L`. Uniform source-subset expansion and fractional layer-bank
construction are therefore equivalent routes to an asymptotic charge margin.

For the `m=10` Hall transition count maxima, maximizing-subset cardinality ranges
from one to 124 while mean source mass remains in `[64,128]`. The obstruction is
capacity reuse. The normalized overlap constant now has an exact two-sided Schur
form `inf P(a,b)Q(a,b)`, allowing independent source and target potentials rather
than only a source-side scaling.

For clean-macro charge, total-excess control is complemented by a sparse-bad-
shell theorem. Under a `3/2` ceiling the exact guaranteed numbers of expansive
nonterminal boundaries are `2,1,4` at `m=8,9,10`; under a doubling ceiling they
are `1,0,2`. A bounded number of exceptional gates can therefore suffice even
when total shell depth grows.

The next available theorem identifier is `PP3bvy`.
