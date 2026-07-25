# Prime-patching frontier addendum: original-reference cascade termination

This addendum continues `proofs/prime-patching-frontier-addendum-193-195.md`
after PP3air. It records the original-reference, target-cycle, and chord-host
reductions in `docs/206` through `docs/208` without replacing the larger
historical ledgers.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ais--PP3aix | A fresh-helper single-cycle move increases original-reference defect by exactly `q-1`, preserves the number of defect cycles, keeps all later centres free, and leaves a linear untouched-original helper reservoir | PROVED / CONDITIONAL FRESH-HELPER MARKED INTERFACE | `docs/206-original-reference-single-cycle-defect-growth.md` |
| PP3aiy--PP3aje | A canonical cascade reaches a `Theta(W)` single alternating defect cycle within `O(W/q)=o(W)` generations; before that it completes or exposes a marked-host/base-allocation obstruction | PROVED / CONDITIONAL FRESH-HELPER CASCADE INTERFACE | `docs/207-target-scale-alternating-cycle-cascade-endpoint.md` |
| PP3ajf--PP3ajl | A target-scale Hamilton defect-cycle host has either a sublinear chord feedback hub, a rooted chord-cycle star, a distinct-signature cycle bank, concentrated backbone support/cost, or the bare two-state oscillation core | PROVED / CONDITIONAL ALTERNATING-HOST INTERFACE | `docs/208-hamilton-defect-cycle-chord-localization.md` |

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
exact two-state reference-oscillation variable.

## Chord localization of the target cycle

Normalize the original edges of the target cycle to loops and the current defect
to one Hamilton successor cycle. Every other allowed off-diagonal host edge is a
chord. Let `L=Theta(W)` be the cycle length and `e` the number of chords.

If `e=o(L)`, all chord endpoints together with one Hamilton vertex form an
explicit feedback hub of size at most

```text
2e+1=o(L).
```

If `e=Omega(L)`, the chord tail--head graph gives one of:

```text
Omega(sqrt(L))
```

chords through one endpoint, or `Omega(sqrt(L))` chords with distinct tails and
heads. Each chord plus its Hamilton return path is a canonical alternating-cycle
state. In the distinct-signature family every chord arc has marginal `1/s`, and
all remaining multiplicity is exact support overlap on the Hamilton backbone.

Thus a target-cycle host is reduced to a small mobility hub, a rooted cycle star,
a distinct-signature one-variable bank, concentrated backbone arc/pair/triple
support or cost, or the bare original/current two-state oscillation.

## Revised live frontier

Under fresh-helper single-cycle preparation, abstract cascade termination,
sub-target-depth growth, and an unspecified target-scale alternating host are no
longer independent problems. The remaining cases are:

1. uniform preparation of the fresh-helper marked hosts through source,
   transition, anchor, Hall, and distinguished endpoint constraints;
2. failure of the nonshadow `Omega(R)` base-domain margin or global allocation
   criterion;
3. payment or direct allocation for a sparse-chord mobility hub;
4. source/support/cost concentration on a rooted chord-cycle star or
   distinct-signature cycle bank;
5. the bare two-state reference oscillation when the target cycle has no useful
   chords;
6. branches that cannot preserve one original reference layer or cannot choose
   untouched original helpers;
7. branches with no robust final allocation that still require one-step monotone
   `Xi` descent.

The no-three-in-line conjecture remains unproved.
