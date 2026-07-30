# Common-box concatenation of threshold cycles

`docs/533` orders one repeated collection of threshold permutation layers.  A
full construction may switch among several zero-sum macrocycles.  This chapter
gives a phase certificate under which arbitrary concatenation preserves one
all-window discrepancy bound.

A threshold macrocycle `C=(v_1,...,v_T)` has rational resource increments with
`sum_t v_t=0`.  For a chosen cyclic phase, let

```text
P(C)={0,v_1,v_1+v_2,...,sum_(t<=T)v_t}
```

be its prefix-potential set.

## 1. Common prefix box

### Theorem PP3cmr -- PROVED / COMMON-BOX CONCATENATION

Suppose phases are chosen for macrocycles `C_1,...,C_s` so that every prefix set
lies in one axis-aligned box

```text
B=product_j [L_j,U_j].
```

Then every prefix of every finite concatenation of the chosen cycles lies in
`B`.  Every interval residual `R` in the resulting infinite word satisfies

```text
|R_j|<=U_j-L_j
```

for every resource coordinate `j`.

#### Proof

Each completed zero-sum cycle returns the cumulative potential to zero.  A
prefix ending inside the next cycle is therefore exactly one of that cycle's
prefix potentials, hence lies in `B`.  An interval residual is the difference
of two global prefix potentials, so its coordinate range is bounded by the box
width. ∎

## 2. Finite phase optimization

### Theorem PP3cms -- PROVED / THRESHOLD PHASE-BOX ORACLE

For finitely many finite cycles, the minimum common `l_infinity` box width is an
exact finite optimization over their cyclic phases.  For any fixed phase tuple,
the optimal box is obtained by taking coordinatewise minima and maxima of the
union of the prefix sets.

#### Proof

Each cycle has finitely many rotations.  Once rotations are fixed, every box
containing all prefix sets must contain their coordinatewise extrema, and that
extremal box is feasible and minimal.  Exhausting the finite phase product gives
the optimum. ∎

## 3. Exact obstruction certificate

### Theorem PP3cmt -- PROVED / COMMON-BOX LOWER WITNESS

If one coordinate of one macrocycle contains two prefix potentials differing by
`delta`, every common box has width at least `|delta|` in that coordinate.  A
phase search attaining the largest such unavoidable separation is an exact
optimality certificate.

#### Proof

Any containing interval must include both prefix values.  The attained phase
tuple supplies the matching upper bound. ∎

## 4. Stored exact fixture

The audit `scripts/check_threshold_cycle_concatenation.py` uses

```text
C1=((1,0),(0,1),(-1,0),(0,-1)),
C2=((1,1),(-1,0),(0,-1)).
```

All 12 phase pairs are checked.  Exactly three attain common-box width one; the
lexicographic phases are `(0,0)` and place every prefix in `[0,1]^2`.  A
350-slot mixed repetition is then checked directly, and every tested interval
has `l_infinity` residual at most one.

## 5. Prime-patching consequence

Several threshold-cleaning gadgets may now be selected online without paying a
new transient penalty at each switch.  One finite phase-box certificate controls
every prefix and every interval of every concatenated execution.
