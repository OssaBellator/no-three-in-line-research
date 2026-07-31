# Shell incidence nullspace and precancellation

`docs/553` maps component residual words through a physical incidence matrix and
finds a zero-reserve aligned phase.  In the stored fixture the two component
words already cancel slot by slot before the incidence map is applied.  This
chapter records the resulting identifiability barrier.

## 1. Incidence-nullspace criterion

### Theorem PP3coz -- PROVED / PHYSICAL SHELL CANCELLATION CRITERION

For component residual `r_t` and physical incidence matrix `P`, the physical
increment is zero at slot `t` exactly when `r_t` lies in `ker P`.  If `r_t=0`
before applying `P`, then every incidence matrix produces the same zero physical
trajectory.

#### Proof

The physical increment is `Pr_t`; its vanishing is the definition of the kernel.
The second statement is immediate from linearity. ∎

## 2. Stored phase is incidence-independent

### Theorem PP3cpa -- PROVED / SHELL PRECANCELLATION DIAGNOSIS

At the selected phase in `docs/553`, the stored component words satisfy

```text
X_t+Y_t=(0,0)
```

for every slot.  Hence the zero startup reserve does not test the supplied
three-by-two incidence matrix: matrices of arbitrary dimension and rank give the
same zero path.

#### Proof

The three slotwise sums are zero.  Apply `PP3coz`.  The checker evaluates four
distinct matrices and obtains zero for all of them. ∎

## 3. Independent shell-extraction contract

### Theorem PP3cpb -- PROVED / NONTRIVIAL SHELL INCIDENCE CERTIFICATE

A geometric shell certificate must derive the incidence entries from physical
resource definitions and audit at least one nonzero component residual outside
the common kernel.  It must then compute the physical prefix trajectory and
minimal reserve.  A fixture that pre-cancels every slot cannot identify the
incidence matrix.

#### Proof

A nonzero residual outside the common kernel distinguishes candidate incidence
maps by their images.  Prefix minima then determine the exact reserve as in
`docs/553`.  Without such a residual, all maps agree on the tested subspace and
are unidentifiable. ∎

## 4. Stored exact audit

The audit `scripts/check_shell_incidence_provenance.py` verifies slotwise
precancellation, tests four incidence matrices that are indistinguishable on the
fixture, and checks that one nonzero residual distinguishes all four.

## 5. Prime-patching consequence

The shell scheduling theorems remain valid.  The current realization task is to
extract a nontrivial physical incidence table and component words from the real
shell system, rather than to optimize another cancelling toy phase.
