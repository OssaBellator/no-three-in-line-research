# Depth-aware AM--GM shell expansion budgets

`docs/387` bounds a product of nonterminal shell norms from their total positive
excess, but its geometric-series estimate ignores the number of shell boundaries.
AM--GM gives the sharp product bound at fixed depth and raises the common audited
excess budget from `2/5` to `3/5`.

No nonterminal shell norm or asymptotic shell-depth bound is proved here.

## 1. Sharp depth-aware product

Let `tau<1` be the terminal-shell norm.  For the `r` earlier boundaries put

```text
delta_j=max(kappa_j-1,0),
E=sum_j delta_j.
```

### Proposition PP3bvg -- PROVED / DEPTH-AWARE EXCESS PRODUCT

For `r>=1`,

```text
product_j kappa_j
 <= product_j(1+delta_j)
 <= (1+E/r)^r.
```

Hence the full trajectory has norm at most

```text
tau(1+E/r)^r
```

and contracts whenever

```text
E<r(tau^(-1/r)-1).
```

For `r=0`, the earlier-shell product is one.

#### Proof

The first inequality is immediate.  The `r` numbers `1+delta_j` have arithmetic
mean `1+E/r`; AM--GM gives the second inequality.  Multiplication by `tau` and
rearrangement give the criterion. ∎

At fixed `r` and `E`, equal distribution of the positive excess is the worst
case, so the AM--GM bound is sharp from those two data alone.

## 2. Exact audited total budgets

The audited horizons `h=3,4,5` have `r=2,3,4` nonterminal boundaries.

### Theorem PP3bvh -- PROVED / VERIFIED FINITELY / CLEAN TOTAL BUDGETS

The following total positive-excess bounds imply full-horizon contraction:

```text
m=8:  E<=6/5,
m=9:  E<=3/5,
m=10: E<=2.
```

The corresponding AM--GM factors are

```text
m=8:  (1+(6/5)/2)^2=(8/5)^2,
m=9:  (1+(3/5)/3)^3=(6/5)^3,
m=10: (1+2/4)^4=(3/2)^4.
```

After multiplication by the exact terminal factors, the reduced bounds are

```text
m=8:
  46989326298877776695103968
  /47374254259236084350795625
  =0.9918747436...;

m=9:
  406616023430754819367780545483294984597292560691
  /410268399261622977419876586128462215837799400000
  =0.9910975941...;

m=10:
  47276550455881871882352184583946271968537909
  /60166841283680893227929821793540106430105600
  =0.7857575609....
```

All comparisons are exact and are checked by the accompanying verifier.  These
are total budgets, not per-shell ceilings.

## 3. Common three-fifths budget

### Corollary PP3bvi -- PROVED / VERIFIED FINITELY / COMMON `3/5` RESERVE

At every audited size, the full trajectory would contract under

```text
sum_(nonterminal j) max(kappa_j-1,0)<=3/5.
```

The exact AM--GM composed bounds are

```text
m=8:
  19089413808919096782385987
  /29153387236452974985105000
  =0.6547923112...;

m=9:
  406616023430754819367780545483294984597292560691
  /410268399261622977419876586128462215837799400000
  =0.9910975941...;

m=10:
  1469990795124937656603257520684012077105290776941
  /5415015715531280390513683961418609578709504000000
  =0.2714656563....
```

The `m=9` case is limiting.  This strictly improves the common `2/5` certificate
from `PP3buy` by using the already audited shell depth.

## 4. Revised frontier

The analytic targets are now nested:

1. exact compensated product below the terminal reserve;
2. sharp depth-aware AM--GM control of total excess;
3. the common finite total budget `3/5`;
4. the simpler common per-shell ceiling `6/5`.

Thus a geometric depth bound converts an additive shell-excess estimate directly
into a multiplicative charge bound.

Verify with

```bash
python scripts/verify_terminal_shell_depth_aware_excess.py .
```

The next theorem identifier after this chapter is `PP3bvj`.
