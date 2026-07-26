# Spread-bank expectation criteria for AC5

**Branch:** `research/alternating-core-chain`

AC5g--AC5k turn reverse-scale compatibility into a finite-menu filter.  A menu
state is retained exactly when it creates no protected-band triple, and the
survivors need expected current-band triple count below the certified batch
size.  This note supplies a quantitative bridge from the spread distributions
of `docs/02-reverse-scale-switching.md` to that filter.

The key point is that protected safety and current-band drift should not be
proved independently by selecting two different states.  A single augmented
badness variable combines them.  If the expected current-band count plus the
batch size times the protected failure probability is below the batch size,
one state simultaneously passes both tests.  The same argument handles every
intermediate state of a multistep installation.

## Spread event systems

Let `B` be a certified target batch with

\[
t=|B|\ge1,
\]

and let `P` be a partner pool of size `p`.  Let `sigma` be a random compatible
injection from `B` to `P`.  Assume the law is **`K/p`-spread**: for every set of
`k` distinct prescribed target-partner pairs,

\[
\Pr(\text{all prescribed pairs occur})
\le
\left(\frac Kp\right)^k.
\]

Every resulting state has a complete physical AC3v envelope and an exact
created-triple ledger.  Rank-one line events are assumed to have been removed
by the individual partner-admissibility test.  For a line band `J`, let

- `E_{2,J}` be a finite inventory of possible new triples in `J` whose
  occurrence is certified by two distinct prescribed target-partner pairs;
- `E_{3,J}` be the analogous inventory requiring three distinct prescribed
  pairs.

The inventory is **complete** when every newly created triple in the band is
represented by at least one event in the appropriate family.  Overcounting is
allowed.

Put

\[
M_{2,J}=|E_{2,J}|,
\qquad
M_{3,J}=|E_{3,J}|.
\]

## AC5l -- spread-event expectation bound -- PROVED

For every complete event inventory in a line band `J`, the expected number
`N_J` of newly created triples in that band satisfies

\[
\boxed{
\mathbb E N_J
\le
\left(\frac Kp\right)^2M_{2,J}
+
\left(\frac Kp\right)^3M_{3,J}.
}
\]

### Proof

For each possible triple choose one representing event from the complete
inventory.  Its indicator is bounded by the indicator that its two or three
prescribed target-partner pairs all occur.  The spread hypothesis bounds those
probabilities by `(K/p)^2` or `(K/p)^3`.  Sum the indicators.  If the inventory
contains several representations of one triple, retaining all of them only
increases the upper bound. QED.

The theorem is agnostic about how the event inventory is counted.  The geometry
of the sparse-batch theorem gives the useful inventory estimates below.

## Current and protected bands

At dyadic scale `H`, write

- `cur` for lines with `H <= h(L) < 2H`;
- `high` for lines with `h(L) >= 2H`.

For a random menu state put

\[
X_{\rm cur}=N_{\rm cur}(S^-,S_\sigma),
\qquad
X_{\rm high}=N_{2H}(S,S_\sigma).
\]

Suppose

\[
\mathbb E X_{\rm cur}\le\Gamma_{\rm cur},
\qquad
\mathbb E X_{\rm high}\le\Gamma_{\rm high}.
\]

## AC5m -- protected survivor mass and conditional current expectation -- PROVED

The protected-band survivor event has probability at least

\[
\boxed{
\Pr(X_{\rm high}=0)
\ge
1-\Gamma_{\rm high}.
}
\]

When `Gamma_high<1`, the survivor law is nonempty and

\[
\boxed{
\mathbb E[X_{\rm cur}\mid X_{\rm high}=0]
\le
\frac{\Gamma_{\rm cur}}{1-\Gamma_{\rm high}}.
}
\]

### Proof

Since `X_high` is a nonnegative integer,

\[
\Pr(X_{\rm high}>0)
\le
\mathbb E X_{\rm high}
\le
\Gamma_{\rm high}.
\]

This proves the survivor bound.  Also

\[
\mathbb E[X_{\rm cur};X_{\rm high}=0]
\le
\mathbb E X_{\rm cur}
\le
\Gamma_{\rm cur}.
\]

Divide by the survivor probability. QED.

## AC5n -- one-shot protected-safe drift criterion -- PROVED

If

\[
\boxed{
\Gamma_{\rm cur}+t\Gamma_{\rm high}<t,
}
\]

then one menu state satisfies simultaneously

\[
\boxed{
X_{\rm high}=0,
\qquad
X_{\rm cur}\le t-1.
}
\]

Hence it passes AC5g and AC5h, preserves every settled higher band and strictly
decreases `Psi_H`.

### Proof

Define

\[
Y=X_{\rm cur}+t\mathbf1_{X_{\rm high}>0}.
\]

Markov's elementary indicator bound gives

\[
\mathbb EY
\le
\Gamma_{\rm cur}+t\Gamma_{\rm high}
<t.
\]

Some state has `Y<t`.  A state with `X_high>0` has `Y>=t`, so the selected state
has `X_high=0`.  Then `Y=X_cur<t`; integrality gives `X_cur<=t-1`.  Apply
AC5g--AC5h. QED.

Equivalently, when `Gamma_high<1`, the displayed condition is

\[
\Gamma_{\rm cur}<t(1-\Gamma_{\rm high}),
\]

which makes AC5m's conditional expectation strictly below `t`.

## Import of the sparse-batch inventories

For a line family `J`, let `ell_J` be a common upper bound on the number of grid
cells on one line in that family.  Let `N<=tp` be the candidate-cell inventory
parameter used in the sparse-batch theorem.  Split the two-choice events into:

- `A_{2,J}` anchored pair-shadow events retained explicitly;
- `U_{2,J}` remaining two-choice line events.

Let `U_{3,J}` be the three-choice event inventory.  Assume the exact geometric
bounds proved for the spread bank:

\[
U_{2,J}\le4\ell_JN,
\qquad
U_{3,J}\le8\ell_JN^2.
\]

## AC5o -- S5-compatible band bounds -- PROVED UNDER THE DECLARED INVENTORY HYPOTHESES

For either band `J in {cur,high}`, put

\[
\Gamma_J
=
\left(\frac Kp\right)^2
(A_{2,J}+U_{2,J})
+
\left(\frac Kp\right)^3U_{3,J}.
\]

Then

\[
\boxed{
\mathbb E N_J\le\Gamma_J
}
\]

and, using `N<=tp`,

\[
\boxed{
\Gamma_J
\le
\left(\frac Kp\right)^2A_{2,J}
+
\frac{4K^2\ell_Jt}{p}
+
\frac{8K^3\ell_Jt^2}{p}.
}
\]

For the current band one may use

\[
\ell_{\rm cur}\le1+\left\lfloor\frac{n-1}{H}\right\rfloor,
\]

while for the protected band the sharper bound is

\[
\ell_{\rm high}\le1+\left\lfloor\frac{n-1}{2H}\right\rfloor.
\]

Thus the explicit sufficient AC5 condition is

\[
\boxed{
\Gamma_{\rm cur}+t\Gamma_{\rm high}<t.
}
\]

### Proof

Use the event inventory

\[
M_{2,J}=A_{2,J}+U_{2,J},
\qquad
M_{3,J}=U_{3,J}
\]

in AC5l.  Substitute the two geometric inventory bounds and `N<=tp`:

\[
\left(\frac Kp\right)^2U_{2,J}
\le
\frac{4K^2\ell_Jt}{p},
\]

and

\[
\left(\frac Kp\right)^3U_{3,J}
\le
\frac{8K^3\ell_Jt^2}{p}.
\]

The line-length bounds are the descending-scale geometry of
`docs/02-reverse-scale-switching.md`.  Apply AC5n for the last statement. QED.

The hypotheses deliberately require a complete event inventory.  Individual
partner admissibility alone does not remove a protected triple using cells from
two or three different repairs; those events must appear in `E_{2,high}` or
`E_{3,high}` and therefore in the AC3v scale filter.

## Multistep spread installations

Let one random menu choice determine a full installation path

\[
S_0=S,S_1,\ldots,S_m.
\]

For step `j` let

\[
X_{{\rm high},j}=N_{2H}(S_{j-1},S_j),
\]

and let `X_cur` be the final current-band count relative to `S^-`.  Suppose

\[
\mathbb EX_{\rm cur}\le\Gamma_{\rm cur},
\qquad
\mathbb EX_{{\rm high},j}\le\Gamma_{{\rm high},j}.
\]

## AC5p -- simultaneous intermediate-safety and final-drift criterion -- PROVED

If

\[
\boxed{
\Gamma_{\rm cur}
+t\sum_{j=1}^{m}\Gamma_{{\rm high},j}
<t,
}
\]

then one complete installation path satisfies

\[
\boxed{
X_{{\rm high},j}=0
\quad(1\le j\le m),
\qquad
X_{\rm cur}\le t-1.
}
\]

Every intermediate state is upper-`2H`-clean by AC5k, and the final state
strictly decreases `Psi_H` by AC5h.

### Proof

Use the augmented integer variable

\[
Y=X_{\rm cur}
+t\sum_{j=1}^{m}
\mathbf1_{X_{{\rm high},j}>0}.
\]

Its expectation is at most the displayed left side, because
`Pr(X_high,j>0)<=E X_high,j`.  Choose a path with `Y<t`.  Any failed
intermediate step contributes at least `t`, so every indicator vanishes.  The
remaining integer `X_cur` is at most `t-1`.  Apply AC5k and AC5h. QED.

This is stronger than checking only the final protected count.  It directly
matches multistep BDA, RI, phase and petal banks whose intermediate states must
preserve installed higher-scale resources.

## Consequence

For any installed AC menu carrying a `K/p`-spread law, the AC5 audit is reduced
to explicit event inventories and one numerical inequality.

1. Count complete two-choice and three-choice triple events separately in the
   current and protected bands.
2. Apply AC5l or the S5-compatible bounds of AC5o.
3. Verify
   \[
   \Gamma_{\rm cur}+t\Gamma_{\rm high}<t
   \]
   for an atomic menu, or AC5p's summed version for a multistep path.
4. If the inequality fails, retain the responsible anchored pair-shadow,
   two-choice or three-choice event class; do not discard it as generic
   collateral.

The remaining geometry is now quantitative: establish sufficiently small
`A_{2,J}`, partner-spread constant `K`, pool depletion and cross-repair event
inventories uniformly after earlier switches.  These are precisely the GC1--GC3
partner and anchor-load obligations.

## Finite check

`scripts/verify_ac_spread_scale_audit.py` exhausts finite menu count pairs,
checks survivor and conditional-expectation inequalities, verifies the one-shot
and multistep augmented-badness criteria, audits the S5 substitution over a
parameter grid, and retains counterexamples whenever one attempts to select
protected safety and current drift from different states.
