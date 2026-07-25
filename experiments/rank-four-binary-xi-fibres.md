# Rank-four binary Xi fibre diagnostic

This finite check accompanies
`docs/178-fixed-centre-rank-four-binary-xi-fibre-localization.md`.
It verifies the exact disjoint-arc and one-centre-arc bookkeeping behind
PP3abv--PP3acb.

Run:

```bash
python scripts/check_rank_four_binary_xi_fibres.py \
  experiments/rank-four-binary-xi-fibres-example.json
```

The stored instance has `N=6`, marked centre `0`, and block size `b=4`, so the
exact remote-arc probability after fixing one centre arc is

```text
(b-3)/((N-2)(N-3)) = 1/12.
```

Every admissible incoming and outgoing centre arc has a partner fibre of total
weight `36`. Its normalized load is therefore exactly `3`, equal to the local
budget, so there is no strictly cheap fibre. Each selected heavy fibre has three
partner arcs of weight `12`; the checker returns a three-edge uniform partner
fan in the dyadic interval `[8,16)`.

For the selected fibre, the checker enumerates all

```text
C(4,2) (4-2)! = 12
```

random-block conditional Hamilton-cycle states and verifies that the exact
average fibre cost is `3`.

Changing `target_fan` from `3` to `4` exercises the multiplicity-core branch.
Changing one incoming pattern weight from `12` to `1` produces a cheap incoming
fibre of normalized load `25/12`.

The diagnostic checks finite identities and the support/multiplicity split. It
does not prove the asymptotic conversion of the resulting partner fan or
high-multiplicity pattern.
