# Bounded-horizon Hamilton descent and exact `m=7` reachability

The complete flaw kernel from `docs/307` deletes every selected bad triple, but
one targeted move need not lower a raw defect potential. This chapter isolates
the exact replacement needed for termination: bounded-horizon strict descent.
It then extends the complete directed reachability census from `m<=6` to
`m=7`.

At `m=7` the signed Hamilton family again contains valid no-three states. Every
one of its `92,160` states reaches a valid state, and every nonvalid state reaches
a strictly lower total triple count within at most four targeted moves.

No uniform asymptotic horizon is proved.

## 1. Bounded-horizon descent implies termination

Let `Omega` be a finite state space, let `Phi:Omega->Z_{>=0}`, and let every
state have a specified set of legal directed moves.

### Proposition PP3bkm -- PROVED

Suppose there is an integer `D>=1` such that every state `x` with `Phi(x)>0`
has a legal directed path

```text
x=x_0 -> x_1 -> ... -> x_r,
```

with

```text
1<=r<=D,
Phi(x_r)<Phi(x).
```

Then there is a deterministic move policy that reaches `Phi=0` from every
initial state in at most

```text
D Phi(x_0)
```

moves.

#### Proof

For each positive-potential state, choose one certified path of length at most
`D` ending at lower potential. Follow the chosen path, then restart the rule.
After each block of at most `D` moves, the nonnegative integer potential drops
by at least one. There are at most `Phi(x_0)` such blocks. ∎

For total collinear triple count on a selected set of `4m` cells, the trivial
bound

```text
Phi <= C(4m,3)
```

shows that a uniform constant descent horizon would already give a polynomial
termination bound. The missing step is proving such a horizon uniformly in
`m`, not the final telescoping argument.

## 2. Exact `m=7` directed flaw graph

### Theorem PP3bkn -- VERIFIED FINITELY

For `m=7`, the signed Hamilton state space has

```text
2^7 (7-1)! = 92,160
```

states. Exactly `36` have no selected collinear triple. In the directed graph of
all currently flaw-targeted orientation flips and successor rotations:

```text
directed edges                         4,427,088
states reaching the valid set             92,160
maximum distance to the valid set              4
```

The exact distance distribution is:

| distance | states |
|---:|---:|
| 0 | 36 |
| 1 | 1,576 |
| 2 | 31,112 |
| 3 | 58,712 |
| 4 | 724 |

Thus every signed Hamilton state at `m=7` admits some flaw-targeted path to a
valid no-three state.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_combined_flaw_reachability_m7.cpp \
  -o /tmp/check_hamilton_combined_flaw_reachability_m7
/tmp/check_hamilton_combined_flaw_reachability_m7
```

The checker independently constructs all `720` anchored Hamilton cycles and all
`128` orientation vectors, groups every selected point pair by exact primitive
integer line equation, records every bad-triple owner set, builds the complete
forward and reverse CSR graphs, and performs reverse breadth-first search from
the `36` valid states. ∎

## 3. Four-step strict descent through `m=7`

### Proposition PP3bko -- VERIFIED FINITELY / LOOK-AHEAD DESCENT

For every `4<=m<=7`, let `B_3` be total selected collinear triple count and let
`B_min(m)` be its minimum over the signed Hamilton family. Every state with

```text
B_3 > B_min(m)
```

has a flaw-targeted path of length at most four to a state with strictly smaller
`B_3`.

The exact strict-descent horizon distributions are:

| `m` | horizon 1 | horizon 2 | horizon 3 | horizon 4 | maximum |
|---:|---:|---:|---:|---:|---:|
| 4 | 44 | 36 | 0 | 0 | 2 |
| 5 | 612 | 104 | 36 | 0 | 3 |
| 6 | 6,832 | 736 | 28 | 0 | 3 |
| 7 | 85,448 | 5,936 | 692 | 48 | 4 |

For `m=4,5,7`, `B_min(m)=0`, so PP3bkm yields a deterministic terminating
finite policy. At `m=6`, `B_min(6)=4`; the Hamilton subfamily itself contains no
valid state, so the same statement only reaches its four-triple optimum.

#### Verification

The earlier Python checker verifies the complete directed graphs for `m<=6`.
The dedicated `m=7` checker additionally stores the forward graph and performs
bounded breadth-first searches from every nonminimal one-step local minimum.
The combined exact ledger is

```text
experiments/hamilton-combined-flaw-reachability-m7-results.json.
```

∎

## 4. Revised scheduling frontier

### Corollary PP3bkp -- PROVED / FRONTIER SHARPENED

For the combined support-one and support-three flaw kernel, the finite obstacle
is no longer targetability or existence of short escaping paths through
`m=7`. The asymptotic scheduling problem can be stated as follows:

> Prove a uniform bound `D`, or a sufficiently controlled nonconstant bound, on
> the flaw-targeted strict-descent horizon for an integer potential that vanishes
> exactly on valid states.

Possible routes include a geometrically weighted potential, a witness-sequence
charge for paths of length at most `D`, or a regeneration argument that makes
long escape paths sufficiently rare. The finite value `D=4` through `m=7` is
evidence, not an asymptotic theorem.
