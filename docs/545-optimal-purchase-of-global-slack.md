# Optimal purchase of global slack

A compatibility ledger may fail a desired stronger margin even though several
frontiers admit optional refinements.  This chapter turns the choice of which
refinements to invoke into an exact linear optimization with a dual price
certificate.

Frontier `i` can purchase a loss reduction `x_i` with

```text
0<=x_i<=u_i
```

at linear cost `c_i x_i`.

## 1. Fractional-knapsack reduction

### Theorem PP3cnj -- PROVED / MINIMUM-COST SLACK PURCHASE

To obtain total reduction at least `R`, minimum cost is achieved by sorting rows
by increasing `c_i`, saturating cheaper rows first, and using at most one
partially filled row.  A threshold price `lambda` certifies optimality:

```text
c_i<lambda  => x_i=u_i,
c_i>lambda  => x_i=0,
c_i=lambda  => 0<=x_i<=u_i.
```

#### Proof

If `c_i<c_j`, `x_i<u_i`, and `x_j>0`, transferring a positive amount from row
`j` to row `i` preserves total reduction and strictly decreases cost.  Repeating
this exchange yields the sorted form.  The threshold conditions are the primal
and dual complementary-slackness relations for the one-constraint linear
program. ∎

## 2. Strengthened-margin transfer

### Theorem PP3cnk -- PROVED / PURCHASED LEDGER FEASIBILITY

If the original aggregate loss is `E`, a target aggregate loss is `T<E`, and a
purchased vector satisfies

```text
sum_i x_i>=E-T,
```

then the refined ledger has aggregate loss at most `T`.  Combining this with any
remaining perturbation cap below `M-T` gives strict global feasibility.

#### Proof

The refined loss is `E-sum_i x_i`, so the first claim is immediate.  Add the
remaining perturbation bound and compare with `M`. ∎

## 3. Stored exact fixture

### Theorem PP3cnl -- PROVED / UNIQUE SIX-ROW SLACK OPTIMUM

Starting from `E=7/30`, target `T=1/5`, and hence required reduction `R=1/30`,
use the rows

| Row | Capacity | Unit price |
|---|---:|---:|
| Hall | `1/40` | 1 |
| boundary | `1/60` | 2 |
| threshold | `1/80` | 3 |
| prefix | `1/96` | 4 |
| shell | `1/120` | 5 |
| interaction | `1/120` | 6 |

The unique optimum is

```text
x_Hall=1/40,
x_boundary=1/120,
all other x_i=0,
```

with exact cost `1/24`.  The dual threshold price is `lambda=2`.

#### Proof

The Hall row is cheapest and is saturated, leaving reduction `1/120`.  The
boundary row is uniquely next cheapest and supplies exactly that amount.  Any
positive use of a later row can be exchanged into the unused boundary capacity
at lower cost.  The cost is `1/40+2/120=1/24`. ∎

## 4. Stored exact audit

The audit `scripts/check_optimal_slack_purchase.py` reconstructs the greedy and
dual certificates and exhausts the exact `1/480` grid.  It finds one optimum
vector and verifies the strengthened aggregate loss exactly.

## 5. Prime-patching consequence

The global program no longer needs to demand equal improvement from every
frontier.  Once actual refinement costs and capacities are proved, the cheapest
combination can be selected with a finite dual witness.  The stored prices are a
synthetic compatibility fixture, not claims about the final geometric costs.
