# Parametric basis regions for threshold kernels

`docs/449` gives finite rational basis certificates for one randomized threshold LP. The same basis also certifies a whole region of nearby source masses and target capacities. This chapter records that parametric structure.

Put a threshold-kernel LP into standard form

```text
minimize c^T u
subject to Cu=r,
           u>=0.
```

Slack variables encode target-load inequalities, while one equality per source encodes its threshold mixture.

## 1. Exact optimality cone

Let `B` be a set of `rank(C)` columns with invertible basis matrix `C_B`. Write

```text
u_B(r)=C_B^(-1)r,
y^T=c_B^T C_B^(-1).
```

### Theorem PP3ccz -- PROVED / PARAMETRIC BASIS CONE

The basis `B` gives an optimal basic solution at right-hand side `r` exactly when

```text
C_B^(-1)r>=0
```

and every nonbasic reduced cost satisfies

```text
c_j-y^T C_j>=0.
```

For fixed `C` and `c`, the second condition is constant and the first condition defines a rational polyhedral cone in `r`.

#### Proof

The first condition is primal feasibility of the basic solution. The vector `y` is the unique dual vector agreeing with the basic costs. The reduced-cost conditions are precisely dual feasibility. Equality of primal and dual values then proves optimality, and the converse is the standard basis optimality criterion. ∎

## 2. Affine value and exact prices

### Theorem PP3cda -- PROVED / BASIS-REGION VALUE FORMULA

Throughout one optimality cone,

```text
OPT(r)=c_B^T C_B^(-1)r=y^T r.
```

Hence every rational displacement `Delta r` that stays inside the cone changes the optimum by exactly

```text
Delta OPT=y^T Delta r.
```

#### Proof

Substitute the basic solution into the objective and use the definition of `y`. ∎

Thus target and source dual prices are not merely first-order derivatives; they are exact finite differences until a cone wall is crossed.

## 3. Localized basis change

### Theorem PP3cdb -- PROVED / FACET AND REDUCED-COST WITNESSES

A right-hand-side path leaves the basis cone only when some basic variable

```text
(C_B^(-1)r)_i
```

reaches zero. A cost path leaves the dual basis region only when some nonbasic reduced cost reaches zero. Therefore every basis change localizes either to one vanishing threshold/slack variable or to one entering reduced-cost threshold.

#### Proof

The primal cone is the intersection of the displayed halfspaces. The dual region is the intersection of the reduced-cost halfspaces. A continuous path can exit only through a boundary facet of one of them. ∎

Enumerating rational bases therefore produces an exact finite polyhedral atlas for a family of nearby threshold-kernel instances.

## 4. Exact audit

Run

```bash
python scripts/check_parametric_threshold_basis_regions.py
```

The fixture checks 160 rational right-hand sides. Exactly 96 lie in the stored basis cone, 16 lie on its active facet, the dual prices are `(1,2,0)`, and both inactive reduced costs equal `2`.
