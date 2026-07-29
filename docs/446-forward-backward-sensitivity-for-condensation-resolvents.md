# Forward--backward sensitivity for condensation resolvents

`docs/440` computes the transient correction by a topological dynamic program.
This chapter adds exact forward and backward prices.  They identify which local
SCC resolvents and condensation edges control the final core load.

## 1. Forward and backward dynamic programs

Order transient components topologically.  Let `R_i` be the local SCC
resolvent, `A_ij` the intercomponent block, `B_i` the core injection, and `C_i`
the core return.  Define

```text
U_i=B_i+sum_(h<i) F_h A_hi,
F_i=U_i R_i,
```

and backwards

```text
V_i=C_i+sum_(j>i) A_ij G_j,
G_i=R_i V_i.
```

The transient correction is

```text
K=sum_i F_i C_i=sum_i B_i G_i.
```

### Theorem PP3cby -- PROVED / EXACT EDGE SENSITIVITY

For one intercomponent block perturbation `A_uv -> A_uv+H`, with every other
block fixed,

```text
Delta K=F_u H G_v.
```

#### Proof

Every condensation path uses the edge `u->v` at most once.  Split every path
containing that edge into its core-to-`u` prefix, the perturbed block, and its
`v`-to-core suffix.  Summing prefixes gives `F_u`; summing suffixes gives `G_v`.
∎

## 2. Local resolvent sensitivity

### Theorem PP3cbz -- PROVED / EXACT SCC-RESOLVENT SENSITIVITY

For one local resolvent perturbation `R_i -> R_i+H`,

```text
Delta K=U_i H V_i.
```

#### Proof

Every condensation path visits component `i` at most once.  Split paths at the
local resolvent exactly as in `PP3cby`. ∎

The two formulas are exact finite differences, not merely first-order
approximations.

## 3. Simultaneous monotone uncertainty

### Theorem PP3cca -- PROVED / ALL-UPPER SENSITIVITY ENVELOPE

Let several nonnegative blocks increase by `Delta A_uv` and `Delta R_i`.  Compute
forward and backward prices using the all-upper block collection.  Then

```text
0<=K^+-K
 <=sum_(u,v) F_u^+ Delta A_uv G_v^+
   +sum_i U_i^+ Delta R_i V_i^+.
```

#### Proof

Raise the blocks one at a time.  `PP3cby` and `PP3cbz` give an exact telescoping
sum evaluated at mixed intermediate configurations.  Nonnegativity makes every
mixed forward and backward factor entrywise at most its all-upper counterpart.
∎

This supplies a rigorous prioritization rule: the largest forward--backward
products identify the local SCC or bridge bounds worth sharpening first.

## 4. Exact diagnostic

Run

```bash
python scripts/check_condensation_resolvent_sensitivities.py
```

The script verifies six exact edge sensitivities, five exact local-resolvent
sensitivities, equality of the forward and backward correction formulas, and a
simultaneous three-block all-upper envelope on a five-component DAG.

The next theorem identifier after this chapter is `PP3ccb`.
