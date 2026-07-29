# Exact line searches between shell critical faces

`docs/463` finds a descent direction while several shell cycles are tied.  The
next task is to determine exactly how far that direction remains valid and which
cycle becomes critical next.  Monomial perturbations make this line search
algebraic and radical-free.

For each shell edge `e`, perturb its gain by

```text
p_e(x)=p_e x^(d_e),
```

where `d_e` is an integer and `x>0`.  A cycle `C` then has product

```text
P_C(x)=P_C x^(D_C),
D_C=sum_(e in C)d_e.
```

## 1. Motion inside one critical face

### Theorem PP3cep -- PROVED / FACE-PRESERVING MONOMIAL DIRECTION

Let `F` be the active critical cycles at `x=1`.  If

```text
D_C/ell_C=s
```

is the same for every `C in F`, then those cycles remain tied for every `x` until
a competitor reaches them.  On that interval the shell rate is

```text
mu(x)=mu(1)x^s.
```

#### Proof

Each active cycle rate is
`P_C^(1/ell_C)x^(D_C/ell_C)=mu(1)x^s`. ∎

## 2. Radical-free next breakpoint

### Theorem PP3ceq -- PROVED / EXACT COMPETITOR BREAKPOINT

Fix one active cycle `C_*` and a competitor `D`.  Their equality is equivalent
to

```text
x^(D_* ell_D-D_D ell_*)
 =P_D^(ell_*)/P_*^(ell_D).
```

After clearing a negative exponent, this is a binomial with rational
coefficients.  Cross-power comparisons determine on which side the competitor
wins without extracting radicals.  The next critical-face breakpoint is the
smallest root `x>1` among competitors that can overtake.

#### Proof

Raise the two cycle-rate expressions to the common power
`ell_* ell_D` and collect the powers of `x`. ∎

## 3. Finite face walk

### Theorem PP3cer -- PROVED / FINITE MONOMIAL FACE DECOMPOSITION

Along one monomial direction, the positive `x`-axis is divided into finitely
many intervals on which the active critical-cycle set is constant.  Exact
cross-power comparisons and the breakpoint binomials enumerate the intervals
and their active sets.

#### Proof

In the variable `log x`, every cycle log-rate is affine.  Two affine functions
cross at most once, and the shell graph has finitely many simple cycles. ∎

## 4. Exact audit

Run

```bash
python scripts/check_shell_face_line_search.py
```

The stored graph begins with two tied critical cycles of slope `-1`.  A stationary
self-loop joins them at the exact root of `16x^2-25`, namely `x=5/4`.  The audit
checks `101` rational parameter points across the breakpoint.
