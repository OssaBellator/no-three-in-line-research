# Parametric paths for shell cycle attenuation

`docs/487` compactifies all additive shell-cycle requirements into a potential
LP.  Geometric constructions often vary one available edge budget or one
allowed attenuation continuously.  This chapter records the exact piecewise
linear path of optimal shell repairs.

Let `s` be a rational parameter entering the right-hand side or an upper bound
of the compact attenuation LP.

## 1. Rational parametric attenuation fan

### Theorem PP3chj -- PROVED / PIECEWISE-AFFINE SHELL PATH

On every compact rational interval of `s`, the feasible parameter set is a
finite union of rational intervals.  On each interval where one primal--dual
basis remains optimal, the attenuation vector, vertex potentials, dual
circulation, and optimum cost are rational affine functions of `s`.

#### Proof

The compact shell formulation is a finite rational parametric LP.  Every basis
gives rational affine primal and dual candidates.  Its feasibility and
optimality conditions are rational linear inequalities in `s`, hence define an
interval.  There are finitely many bases. ∎

## 2. Breakpoints and sensitivity

### Theorem PP3chk -- PROVED / EXACT CAP PRICE

Suppose `s` is the upper bound of one attenuation variable and the current
basis is nondegenerate.  Inside its stability interval,

```text
d OPT(s)/ds = -z_s,
```

where `z_s` is the optimal dual price of that upper bound.  A breakpoint occurs
when one basic variable, reduced cost, or cycle-separation residual reaches
zero.

#### Proof

Substituting the affine basic solution into the objective gives the standard LP
right-hand-side sensitivity formula.  Primal or dual feasibility can change
only at the listed zero events. ∎

## 3. Oracle continuation certificate

### Theorem PP3chl -- PROVED / FINITE PARAMETRIC CYCLE WALK

Starting from one exact optimal basis, advance to the first rational breakpoint,
pivot within the compact LP, and run the maximum-cycle oracle.  Add any newly
violated simple cycle and continue.

On a compact rational parameter interval this process terminates after finitely
many basis regions and generated simple cycles.  The stored primal basis,
dual prices, breakpoint equations, and oracle outputs form a finite exact path
certificate.

#### Proof

There are finitely many compact-LP bases and finitely many simple cycles.
Between consecutive breakpoint values the active data are constant.  Every
unsuccessful oracle call adds a previously absent cycle, so only finitely many
events occur. ∎

## 4. Stored exact fixture

The audit `scripts/check_parametric_shell_attenuation_path.py` minimizes

```text
x_1+x_2+x_3
```

subject to all three pair sums being at least one and `x_3<=s`.  The exact path
is

```text
0<=s<=1/2:  x=(1-s,1-s,s),  OPT=2-s,
s>=1/2:     x=(1/2,1/2,1/2), OPT=3/2.
```

The cap dual price is one below the breakpoint and zero above it, giving
one-sided value slopes `-1` and `0`.  All 101 rational samples from zero to one
are checked.

## 5. Prime-patching consequence

Shell attenuation can now be transported as a geometric resource changes,
without resolving the full cycle system from scratch.  Exact dual prices say
how much contraction is purchased by one additional unit of an attenuable
edge.
