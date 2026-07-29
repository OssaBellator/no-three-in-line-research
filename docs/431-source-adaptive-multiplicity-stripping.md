# Source-adaptive multiplicity stripping

`docs/425` optimizes over one global target-multiplicity threshold.  Different
sources may have very different multiplicity tails, so one global threshold can
be unnecessarily restrictive.  This chapter records the exact kernel obtained
when every source chooses its own threshold.

## 1. Adaptive retained neighbourhoods

Let `G=(S,T,E)` be a finite action graph and write

```text
m(y)=#{x in S:y in N(x)}.
```

Choose an integer threshold `h_x>=1` for each source.  Retain

```text
N_h(x)={y in N(x):m(y)<=h_x},
d_h(x)=|N_h(x)|,
```

and assume `d_h(x)>0`.  Let `P_h` choose uniformly from `N_h(x)`.

### Theorem PP3caf -- PROVED / EXACT ADAPTIVE-THRESHOLD COLUMN FORMULA

The reverse load is exactly

```text
lambda(P_h)
 =max_(y in T)
   sum_(x:y in N(x), m(y)<=h_x) 1/d_h(x).
```

#### Proof

A retained incidence from `x` to `y` contributes exactly `1/d_h(x)` to the
column of `y`; deleted incidences contribute zero.  Summing over sources and
maximizing gives the formula. ∎

Consequently the optimum over source-dependent thresholds is never worse than
the best global threshold from `docs/425`.

## 2. Threshold classes

Partition the sources into classes `S_1,...,S_r`.  Every source in `S_i` uses
threshold `h_i` and has retained degree at least `d_i`.  For a target `y`, put

```text
r_i(y)=#{x in S_i:y in N(x), m(y)<=h_i}.
```

### Corollary PP3cag -- PROVED / CLASSWISE ADAPTIVE STRIPPING ENVELOPE

One has

```text
lambda(P_h)
 <=max_y sum_(i=1)^r r_i(y)/d_i.
```

In particular, if `r_i(y)<=c_i` for every target, then

```text
lambda(P_h)<=sum_i c_i/d_i.
```

#### Proof

In class `i`, every retained predecessor contributes at most `1/d_i`.  Sum the
class contributions in the exact column formula. ∎

This allows low-tail and high-tail sources to use different cutoffs without
forcing either class to inherit the other's worst retained degree.

## 3. Overload localization

### Proposition PP3cah -- PROVED / ADAPTIVE-STRIPPING OVERLOAD TARGET

Let nonnegative budgets `rho_i` be assigned to the threshold classes.  If

```text
lambda(P_h)>sum_i rho_i,
```

then some target `y` and some class `i` satisfy

```text
r_i(y)/d_i>rho_i.
```

More exactly, the offending target obeys

```text
sum_i r_i(y)/d_i>sum_i rho_i.
```

#### Proof

Choose a column whose load exceeds the proposed total.  If every class
contribution were at most its budget, their sum would not exceed the total
budget. ∎

Failure is therefore localized to one target and one source-tail class.

## 4. Finite diagnostic

The script

```bash
python scripts/check_source_adaptive_multiplicity_stripping.py
```

exhausts every threshold assignment on a stored action graph, checks the exact
column formula, and exhibits a strict improvement over every global threshold.

The next theorem identifier after this chapter is `PP3cai`.
