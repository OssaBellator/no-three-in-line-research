# A fixed relative terminal-normalizer cut through `m=10`

`docs/375` optimizes one cut separately at each audited size.  This chapter asks
whether the cut can instead be prescribed by one dimensionless rule.  The answer
is yes through `m=10`: the same relative threshold `16/5` certifies contraction
at `m=8,9,10`.

The result is finite.  No asymptotic lower bound for terminal normalizers or
uniform relative-threshold theorem is claimed.

## 1. Dimensionless one-threshold criterion

Fix a terminal target cycle `eta`.  Let

```text
z_min = minimum normalizer among all incoming terminal labels,
N_eta = total incoming labelled multiplicity,
```

and fix a real number `q>1`.  Let `z_q` be the first observed normalizer satisfying

```text
z_q >= q z_min.
```

Write

```text
L_eta(q) = #{incoming labels with Z < z_q},
H_eta(q) = #{incoming labels with Z >= z_q}.
```

### Proposition PP3btt -- PROVED / DIMENSIONLESS RELATIVE-CUT ENVELOPE

For every target,

```text
kappa_F(eta)
 <= L_eta(q)/z_min + H_eta(q)/z_q
 <= [L_eta(q) + H_eta(q)/q]/z_min.
```

Equivalently, if

```text
R_eta = N_eta/z_min,
alpha_eta = L_eta(q)/N_eta,
```

then

```text
kappa_F(eta)
 <= R_eta [alpha_eta + (1-alpha_eta)/q].
```

#### Proof

Every low label has normalizer at least `z_min`, while every high label has
normalizer at least `z_q>=q z_min`.  Replacing each reciprocal by the appropriate
lower bound gives the first display.  Substituting `N_eta=L_eta+H_eta` gives the
dimensionless form. ∎

This criterion separates the terminal problem into three quantities with a
common scale: total reverse multiplicity `R_eta`, low-normalizer fraction
`alpha_eta`, and relative threshold `q`.

## 2. One common relative threshold

Set

```text
q = 16/5.
```

At each size, choose the first observed normalizer at least `(16/5)z_min`.

### Theorem PP3btu -- VERIFIED FINITELY / FIXED `16/5` CUT

The complete exact terminal-gate census gives:

| `m` | `z_min` | `(16/5)z_min` | selected observed cut | low/high labels on a maximizing target | exact selected-threshold envelope | dimensionless relaxed envelope |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 1096 | `17536/5` | `3488 | 3524` | `432 / 1152` | `87030/120697 = 0.7210618325...` | `99/137 = 0.7226277372...` |
| 9 | 2976 | `47616/5` | `9520 | 9536` | `1024 / 6144` | `13696/13857 = 0.9883813235...` | `92/93 = 0.9892473118...` |
| 10 | 9872 | `157952/5` | `31520 | 31648` | `896 / 7168` | `193592/610213 = 0.3172531559...` | `196/617 = 0.3176661264...` |

The dimensionless relaxed column uses only

```text
[L + (5/16)H]/z_min,
```

not the exact selected threshold.  Its clean bounds and exact margins are

```text
m=8:  99/137 < 3/4,  margin 15/548;
m=9:  92/93  < 1,    margin 1/93;
m=10: 196/617 < 1/3, margin 29/1851.
```

The maximizing targets have respectively 7, 8, and 9 parity components, with
two tied target cycles in each case.

#### Verification

The regeneration checker instruments the committed terminal normalizer census.
It reconstructs every terminal closing label and exact normalizer, chooses the
first observed normalizer at least `(16/5)z_min`, and computes both:

1. the exact two-segment envelope using the selected observed threshold;
2. the weaker dimensionless envelope replacing that threshold by
   `(16/5)z_min`.

All comparisons use exact integer arithmetic.  The generated C++ compiles with
`-Wall -Wextra -pedantic -fopenmp`; all displayed values are hard-coded Python
regressions. ∎

## 3. Finite common-scale consequence

### Corollary PP3btv -- PROVED / VERIFIED FINITELY / ONE DIMENSIONLESS CUT

A single relative threshold rule certifies terminal contraction at every audited
size `m=8,9,10`:

```text
z_* = first observed normalizer >= (16/5) z_min.
```

Thus the finite contraction does not require size-dependent threshold ratios or
control of a full dyadic profile.  The remaining asymptotic obligation can be
stated as a uniform inequality of the form

```text
L_eta/z_min + (5/16) H_eta/z_min < 1,
```

at the relative level `(16/5)z_min`, together with shell-depth and adjacent-fibre
control.

The finite result does not show that `16/5` remains valid for larger `m`, nor
that this ratio is asymptotically optimal.

Reproduce or verify with

```bash
python scripts/check_terminal_normalizer_fixed_relative_cut.py .

python scripts/check_terminal_normalizer_fixed_relative_cut.py . \
  --regenerate --threads 8 \
  --output /tmp/terminal-normalizer-fixed-relative-cut.json
```

The next theorem identifier after this chapter is `PP3btw`.
