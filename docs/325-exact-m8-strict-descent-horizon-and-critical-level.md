# Exact `m=8` strict-descent horizon and the critical defect level

`docs/319` proves that every `m=8` signed Hamilton state reaches validity within
five targeted moves.  That gives a five-step strict-descent upper bound for
`Psi=B_3/4`, but does not show whether a lower-defect state is always reachable
sooner.  This chapter computes the exact strict-descent distance for every state.

No uniform asymptotic horizon is claimed.

## 1. Incremental lower-level reverse search

Let `G` be the directed flaw-targeted graph and let `phi` be any integer-valued
potential.  List its attained values increasingly as

```text
a_0<a_1<...<a_t.
```

### Proposition PP3bmz -- PROVED / INCREMENTAL DESCENT SEARCH

There is an exact incremental algorithm for all distances

```text
d_down(x)=dist_G(x,{y:phi(y)<phi(x)}).
```

Maintain reverse-graph distances to the union of already activated lower levels.
Immediately before activating level `a_i`, the maintained distance of every
state on that level is exactly `d_down`.  Then set all states of level `a_i` to
distance zero and propagate only improving reverse-BFS relaxations.

#### Proof

Before level `a_i` is activated, the active target set is exactly
`{y:phi(y)<a_i}`.  Multi-source reverse BFS computes directed distance to that
set.  Adding the next level can only decrease distances, and ordinary queue
relaxation from the new zero-distance sources computes distance to the enlarged
union.  Induction over the levels proves the claim. ∎

Unlike a separate BFS for every potential value, this method reuses all previous
relaxations and never materializes the full edge set.

## 2. Exact strict-descent distribution at `m=8`

### Theorem PP3bna -- VERIFIED FINITELY / SHARP FIVE-STEP HORIZON

For `m=8`, with `phi=B_3` or equivalently `Psi=B_3/4`, every nonvalid signed
Hamilton state reaches a strictly lower potential state.  The exact distribution
is

| strict-descent distance | states |
|---:|---:|
| 1 | 1,232,660 |
| 2 | 53,444 |
| 3 | 3,616 |
| 4 | 448 |
| 5 | 44 |

Thus the maximum strict-descent horizon is exactly five.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_strict_descent_horizon_m8.cpp \
  -o /tmp/check_hamilton_strict_descent_horizon_m8
/tmp/check_hamilton_strict_descent_horizon_m8
```

The checker reconstructs all `1,290,240` states and their pair/triple owner masks,
uses the exact implicit predecessor tests of PP3bma, and performs the incremental
search of PP3bmz over all 46 defect levels.  It verifies the stored ledger
`experiments/hamilton-strict-descent-horizon-m8.json`. ∎

## 3. The five-step obstruction is confined to `B_3=4`

### Corollary PP3bnb -- VERIFIED FINITELY / CRITICAL LEVEL ISOLATED

All 44 states requiring five moves to lower the potential lie at

```text
B_3=4,
Psi=1.
```

The complete strict-descent distribution on that smallest positive level is

```text
1 step:   4 states,
2 steps: 32 states,
3 steps: 88 states,
4 steps:204 states,
5 steps: 44 states.
```

Every state with `B_3>=40` has an immediate targeted move to a lower defect
level.

#### Proof

These are direct level-by-level outputs of the verified incremental search. ∎

The difficult finite states are therefore not high-defect configurations.  They
are near-valid states whose single quarter-turn orbit of bad triples cannot be
removed without temporary collateral defects.

## 4. Exact finite termination policy

### Corollary PP3bnc -- VERIFIED FINITELY / BOUNDED-HORIZON POLICY

At `m=8`, repeatedly choose a shortest targeted walk to a lower value of `Psi`.
This policy reaches validity after at most

```text
5 Psi(x_0)=5B_3(x_0)/4
```

targeted moves.

Since the largest audited defect is `B_3=184`, the resulting universal finite
bound is at most 230 moves.  The direct distance-to-validity result PP3bmb is much
stronger numerically—at most five moves—but the displayed form is the exact
finite analogue of the desired asymptotic telescoping argument.

#### Proof

PP3bna supplies a decrease of at least one in the nonnegative integer `Psi`
within at most five moves.  Apply the bounded-horizon lemma PP3bkm. ∎

## 5. Revised descent frontier

The finite horizon sequence is now

```text
m<=7: maximum strict-descent horizon at most 4,
m=8:  maximum strict-descent horizon exactly 5.
```

The location of the sharp witnesses suggests three focused asymptotic routes:

1. classify one-orbit defect states and construct a bounded collateral-repair
   sequence;
2. weight the potential by geometric type so the first move from a `Psi=1`
   state is already descending;
3. prove that every local minimum has a bounded alternating path through a
   controlled family of temporary defects;
4. compare the critical 44 states with parity-clean macro moves rather than the
   unrestricted fresh-sign rotation;
5. determine whether the horizon remains bounded at `m=9` on a sampled or
   compressed state family before attempting the full state graph.
