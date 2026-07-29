# Minimum-work dynamic programming for interaction expansions

`docs/464` adaptively expands an interaction frontier until its certified error
is small enough.  This chapter solves the complementary optimization problem:
for a fixed scalar error budget, what is the minimum number of prefix expansions
that can possibly suffice?

Let `J` be a finite nonnegative interaction matrix with `rho(J)<1`, and let
`c>=0` be a scalar immediate-output vector.  The exact continuation price is

```text
h=(I-J)^(-1)c.
```

Expanding one atom in state `u` costs one unit, retains its immediate output
`c_u`, and creates child atoms of masses `J_(u,v)`.

## 1. Exact budget recurrence

Let `E_u(k)` be the minimum omitted output achievable from one unit atom in
state `u` using at most `k` expansions.

### Theorem PP3ces -- PROVED / EXACT EXPANSION-BUDGET DP

The values satisfy

```text
E_u(0)=h_u,

E_u(k)=min(
  E_u(k-1),
  min_(sum_v k_v<=k-1) sum_v J_(u,v) E_v(k_v)
).
```

#### Proof

With zero work the whole continuation `h_u` is omitted.  A positive-work plan
either leaves one unit unused or expands the root.  After root expansion, every
child subtree is independent, receives some budget `k_v`, and contributes
`J_(u,v)E_v(k_v)`.  Every feasible plan has exactly one of these forms, and every
listed allocation constructs a feasible plan. ∎

## 2. Minimum-work certificate

### Theorem PP3cet -- PROVED / EXACT ERROR--WORK PARETO CURVE

The sequence `E_u(k)` is nonincreasing.  For tolerance `epsilon`, the smallest
`k` satisfying

```text
E_u(k)<=epsilon
```

is the exact minimum expansion budget.  The stored minimizing allocations
reconstruct an optimal expansion plan, while `E_u(k-1)>epsilon` is a matching
lower certificate that no smaller plan can succeed.

#### Proof

Unused budget proves monotonicity.  Exactness follows from the exhaustive
decomposition in `PP3ces`. ∎

## 3. Several roots and output prices

### Theorem PP3ceu -- PROVED / MULTIROOT BUDGET ALLOCATION

For initial atom masses `beta_u`, the exact omission under total budget `K` is

```text
E_beta(K)=min_(sum_u k_u<=K) sum_u beta_u E_u(k_u).
```

For a vector output matrix `C`, any nonnegative output-price vector `z` reduces
the problem to the scalar immediate output `c=Cz`.  Thus the same dynamic
program gives exact minimum-work certificates for every priced combination of
output coordinates.

#### Proof

Initial root subtrees are independent and omission is linear in atom mass.
Scalarization commutes with the nonnegative interaction expansion. ∎

## 4. Exact audit

Run

```bash
python scripts/check_minimum_work_interaction_dp.py
```

The stored three-state automaton has continuation prices
`(5/57,6/95,1/19)`.  Tolerance `1/100` is impossible with four expansions because
`E_0(4)=1103/91200`, and attainable with five because
`E_0(5)=35/3648`.  The exact root allocation gives three descendant expansions
to state `0` and one to state `1` after expanding the root.
