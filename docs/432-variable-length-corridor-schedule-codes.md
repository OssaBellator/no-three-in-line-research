# Variable-length corridor schedule codes

`docs/426` uses fixed-length bank codes.  When bank kernels have unequal loads,
a variable-length prefix code can reserve short, safer schedules for the most
expensive banks while assigning longer schedules to lighter banks.

## 1. Prefix-free schedules

Let banks `i=1,...,K` have unconditioned reverse loads `rho_i>0`.  Choose a
`b`-ary prefix-free codeword of length `ell_i>=1` for each bank.  Assume every
schedule symbol retains conditional row mass at least `p`, where

```text
0<p<1.
```

The final target intrinsically records the full codeword.

### Theorem PP3cai -- PROVED / VARIABLE-LENGTH BANK LOAD

The combined scheduled kernel has reverse load at most

```text
max_i rho_i p^(-ell_i).
```

#### Proof

Conditioning through `ell_i` symbols amplifies bank `i` by at most
`p^(-ell_i)`.  Prefix-free codewords are distinct and recover the bank, so the
final bank target supports are disjoint.  Apply `PP3bzz` to the bank classes. ∎

## 2. Exact feasibility at a proposed risk

For `R>0`, define

```text
L_i(R)=floor(log_(1/p)(R/rho_i)).
```

A risk bound `R` permits code length `ell_i` only when

```text
1<=ell_i<=L_i(R).
```

### Theorem PP3caj -- PROVED / EXACT KRAFT RISK TEST

There exists a `b`-ary prefix-free schedule with

```text
rho_i p^(-ell_i)<=R
```

for every bank if and only if

```text
L_i(R)>=1 for every i
```

and

```text
sum_i b^(-L_i(R))<=1.
```

#### Proof

If such a schedule exists, then `ell_i<=L_i(R)`, hence

```text
b^(-ell_i)>=b^(-L_i(R)).
```

Kraft's inequality gives the necessary sum bound.

Conversely, if the displayed conditions hold, choose `ell_i=L_i(R)`.  Kraft's
inequality guarantees a prefix-free `b`-ary code with those lengths, and the
definition of `L_i(R)` gives `rho_i p^(-ell_i)<=R`. ∎

## 3. Optimal schedule risk

### Corollary PP3cak -- PROVED / FINITE OPTIMAL VARIABLE-LENGTH SCHEDULE

The optimal worst-bank risk is the smallest breakpoint value `R` satisfying the
Kraft risk test in `PP3caj`.  It is attained by choosing

```text
ell_i=L_i(R).
```

Only finitely many values need be checked: the breakpoints are

```text
rho_i p^(-ell),
```

for positive integers `ell` up to the first feasible common maximum length.

Thus variable-length schedule design is an exact finite optimization rather
than a heuristic coding choice.

## 4. Finite diagnostic

The script

```bash
python scripts/check_variable_length_corridor_codes.py
```

exhausts binary prefix-code length vectors for seven unequal bank loads and
verifies the exact Kraft risk criterion and optimum.

The next theorem identifier after this chapter is `PP3cal`.
