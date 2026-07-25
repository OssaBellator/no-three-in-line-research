# Prime-patching frontier addendum: original-reference cascade termination

This addendum continues `proofs/prime-patching-frontier-addendum-193-195.md`
after PP3air. It records the original-reference and target-cycle reductions in
`docs/206` and `docs/207` without replacing the larger historical ledgers.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ais--PP3aix | A fresh-helper single-cycle move increases original-reference defect by exactly `q-1`, preserves the number of defect cycles, keeps all later centres free, and leaves a linear untouched-original helper reservoir | PROVED / CONDITIONAL FRESH-HELPER MARKED INTERFACE | `docs/206-original-reference-single-cycle-defect-growth.md` |
| PP3aiy--PP3aje | A canonical cascade reaches a `Theta(W)` single alternating defect cycle within `O(W/q)=o(W)` generations; before that it completes or exposes a marked-host/base-allocation obstruction | PROVED / CONDITIONAL FRESH-HELPER CASCADE INTERFACE | `docs/207-target-scale-alternating-cycle-cascade-endpoint.md` |

## Exact original-reference coordinate

Fix the original matching layer

```text
M_0={(i,pi_0(i)):i in [m]}
```

and write the current layer as `M_t={(i,pi_t(i))}`. The relative permutation is

```text
sigma_t=pi_0^{-1} o pi_t.
```

Its nontrivial cycles are exactly the alternating cycles of
`M_0 triangle M_t`, and their total row-length is the defect size

```text
S_t=|{i:pi_t(i) != pi_0(i)}|.
```

A seed single-cycle move on `q` untouched original rows creates one defect cycle
of length `q`. Thereafter choose one centre in that defect and `q-1` rows still
fixed by `sigma_t`. Composing with any directed `q`-cycle on the selected rows
splices the helper singleton cycles into the centre cycle. Consequently

```text
S_(t+1)=S_t+q-1
```

and the number of nontrivial defect cycles is unchanged.

Because every controller edge is a fixed original edge, every defect point is
outside the controller infrastructure. All post-seed star centres are therefore
free. While `S_t=o(m)`, a linear reservoir of untouched original helpers remains.
The universal single-cycle cylinder calculations retain the same asymptotic
orders on that reservoir.

## Target-scale finite horizon

Put

```text
R=m^(19/20+o(1)),
W=sqrt(R)=m^(19/40+o(1)).
```

Fix the robust domain margin `xi R` and choose

```text
0<alpha<min{sqrt(xi/8),xi/4}.
```

For any divergent `q=o(W)`, the first generation satisfying

```text
S_t>=alpha W
```

occurs after

```text
t=O(W/q)=o(W)
```

steps, with overshoot below `q`. At that state

```text
S_t=(alpha+o(1))W
```

and all final binary shadow costs less than `xi R/4` in every paired macro
domain.

Hence either final unary support fits the remaining robust margin and direct
allocation completes, or one final new point is a source-star centre of degree

```text
C > 3 xi R/(8S_t)=Omega(W).
```

The chosen bound `alpha<xi/4` makes this larger than the target width.

Under the canonical seed and fresh-helper moves, the whole defect is one relative
cycle. The failure boundary is therefore one alternating cycle of row-length

```text
Theta(W),
```

not an unbounded abstract cascade. Its original/current edge choices form an
exact two-state reference-oscillation variable. Additional ambient alternating
states feed the cycle-bank, mobility-hub, and theta localizations; without them,
the remaining object is the explicit two-state cycle core.

## Revised live frontier

Under fresh-helper single-cycle preparation, abstract cascade termination and
sub-target-depth growth are no longer independent problems. The remaining cases
are:

1. uniform preparation of the fresh-helper marked hosts through source,
   transition, anchor, Hall, alternating-host, and distinguished endpoint
   constraints;
2. failure of the nonshadow `Omega(R)` base-domain margin or global allocation
   criterion;
3. direct treatment of the target-scale reference-oscillation cycle;
4. conversion of that cycle through extra alternating host states, mobility hubs,
   or theta paths;
5. branches that cannot preserve one original reference layer or cannot choose
   untouched original helpers;
6. branches with no robust final allocation that still require one-step monotone
   `Xi` descent.

The no-three-in-line conjecture remains unproved.
