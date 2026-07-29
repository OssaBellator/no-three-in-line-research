# RI frontier pass: conflict-graph physical subbanks

- **RI5br:** every independent component family satisfying local replacement legality is a physical I6 subbank.
- **RI5bs:** maximum conflict degree `Delta` preserves at least `ceil(m/(Delta+1))` components.
- **RI5bt:** weighted retained payment is at least `sum_a w_a/(d(a)+1)`, hence at least `W/(Delta+1)` under bounded degree.
- **RI5bu:** failure is one high-conflict neighbourhood or one exact local readiness defect.

## Remaining frontier

Bound or pay the actual overlap/cross-constraint graph; handle owner payment, repeated-coset correlations, blocker repair and replenishable-source recurrence.

Verifier: `scripts/verify_ri_conflict_graph_subbank.py`.