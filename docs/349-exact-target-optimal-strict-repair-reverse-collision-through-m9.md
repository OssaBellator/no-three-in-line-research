# Exact reverse-collision optimisation for target-optimal strict repair through `m=9`

`docs/347` reduces strict-repair predecessor charge to the weighted reverse
indegree of a labelled one-step policy.  This chapter evaluates that quantity
for the target-optimal fixed-sign strict-frustration graph from `docs/334` and
then optimises the policy exactly.

No asymptotic branching or expansion estimate is claimed.

## 1. Orientation-mask decomposition

Fix `m` and an owner-sign mask `e`.  Let `S_e` be the signed Hamilton states
`(rho,e)` satisfying

```text
lambda(rho)>0,
V_e(rho)=lambda(rho).
```

For `x=(rho,e) in S_e`, join `x` to `y=(eta,e)` when `eta` is obtained by one
three-owner successor rotation and

```text
V_e(eta)=lambda(eta)<lambda(rho).
```

These are exactly the target-optimal fixed-sign strict descents audited in
`docs/334`.  Since the sign mask is unchanged, the labelled repair graph is a
disjoint union over the `2^m` masks.

A row-stochastic policy distributes one unit of mass from every source among
its outgoing edges.  Its one-step reverse-collision charge is the largest total
mass entering one target column.

### Proposition PP3bqt -- PROVED / ORIENTATION-FIBRE HALL FORMULA

For one fixed sign mask, the minimum possible maximum target-column load is

```text
gamma_e
 = max_(U subseteq S_e) |U|/|N(U)|.
```

Equivalently, a policy with every target load at most `gamma` exists exactly
when

```text
|U| <= gamma |N(U)|
```

for every source subset `U`.

#### Proof

Give every source supply one and every target capacity `gamma`.  A feasible
fractional transport is exactly a row-stochastic repair policy with column load
at most `gamma`.  The max-flow/min-cut theorem gives feasibility precisely when
every source subset has enough neighbouring capacity, which is the displayed
Hall inequality.  Minimising `gamma` gives the maximum ratio. ∎

For a rational trial `p/q`, a violating subset maximises

```text
q|U|-p|N(U)|.
```

This is a maximum-closure problem: source vertices have weight `q`, target
vertices weight `-p`, and every repair edge is an infinite-capacity implication.
Finite rational Dinkelbach iteration therefore returns `gamma_e` exactly.

## 2. The naive uniform policy

The first audit chooses uniformly among all target-optimal fixed-sign strict
descents from each source.  Exact incoming loads are accumulated over a common
integer denominator.

### Theorem PP3bqu -- VERIFIED FINITELY / UNIFORM REVERSE-COLLISION CENSUS

| `m` | sources | transitions | forward degree range | maximum reverse multiplicity | maximum weighted reverse indegree | columns above one |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 48 | 244 | 3--7 | 1 | `1/3` | 0 |
| 6 | 272 | 2,596 | 5--14 | 4 | `127/252` | 0 |
| 7 | 2,752 | 37,020 | 6--22 | 8 | `5069/5544` | 0 |
| 8 | 93,980 | 1,642,058 | 5--34 | 19 | `22357817/17907120` | 84 |
| 9 | 977,312 | 24,730,616 | 4--50 | 28 | `6619279336199/4658179125600` | 712 |

The corresponding decimal maxima are approximately

```text
m=5: 0.333333,
m=6: 0.503968,
m=7: 0.914322,
m=8: 1.248543,
m=9: 1.421001.
```

Every maximising target column is parity-clean.  Thus uniform random choice is
already insufficient at `m=8`; the obstruction is terminal merging, not failure
of strict descent.

## 3. Exact reweighting removes the finite overload

The Hall optimisation is solved independently in every sign mask and the
largest optimum is then taken over all masks.

### Theorem PP3bqv -- VERIFIED FINITELY / OPTIMAL STRICT-REPAIR CONTRACTION

| `m` | masks containing sources | exact optimal maximum reverse indegree | worst Hall set `|U|/|N(U)|` |
|---:|---:|---:|---:|
| 5 | 28 | `1/3` | `2/6` |
| 6 | 64 | `4/19` | `4/19` |
| 7 | 128 | `1/5` | `4/20` |
| 8 | 256 | `489/1726` | `489/1726` |
| 9 | 512 | `1/4` | `1/4` |

No audited sign mask has optimal charge equal to or above one.  In particular,
there exists a row-stochastic target-optimal fixed-sign strict-repair policy
with

```text
kappa <= 489/1726 < 0.284
```

uniformly through `m=9`.

The worst finite cut is intermediate at `m=8`, using 489 sources and 1,726
target columns.  At `m=9` the absolute worst ratio is again local: one source
has only four admissible lower-frustration targets.

#### Verification

The checker reconstructs the exact pair geometry, all Hamilton cycles, every
optimal sign mask, and every target-optimal fixed-sign strict descent.  For each
mask it runs exact maximum-closure min-cuts until rational Dinkelbach iteration
stabilises.  The source and transition totals reproduce `docs/334` before the
new collision ledgers are accepted. ∎

## 4. Terminal-column consequence

Through `m=9`, target-optimal fixed-sign strict repair terminates in at most
three steps.  Apply `docs/347` to the optimally reweighted policy.

### Corollary PP3bqw -- PROVED / AUDITED ABSORBING WARMNESS BOUND

Let

```text
r = 489/1726.
```

For unit initial signed-state column load, the total parity-clean absorption
column accumulated over all strict depths is at most

```text
r+r^2+r^3
 = 1986421179/5141885176
 < 0.387.
```

At `m=9` alone, the sharper `r=1/4` gives

```text
1/4+1/16+1/64 = 21/64.
```

Terminal fibre regeneration and every subsequent stochastic clean-cycle heat
step can only decrease these bounds.

This is a finite existence result for a fractional policy.  The remaining
asymptotic problem is to prove a geometric Hall bound, or construct comparably
balanced local weights, throughout the logarithmic frustration window.

Compile and run the exact audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_target_optimal_strict_repair_collision.cpp \
  -o /tmp/check_target_optimal_strict_repair_collision

/tmp/check_target_optimal_strict_repair_collision
```

The next theorem identifier after this chapter is `PP3bqx`.
