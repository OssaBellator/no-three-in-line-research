# Periodic deterministic realization of marker controllers

`docs/483` returns an exact rational randomized marker controller after action and
scenario generation terminates.  A geometric construction still needs an
explicit move at every visit to every marker state.  This chapter replaces the
rational randomization by local periodic counters and records the exact finite
prefix discrepancy.

Let `U` be the marker-state set.  At state `u`, the certified controller has
rational action probabilities `pi_(u,a)`.  Let `M_u` be a common denominator.

## 1. Exact periodic realization

### Theorem PP3cgx -- PROVED / LOCAL PERIODIC CONTROLLER

For every state `u`, choose a word `W_u` of length `M_u` containing exactly

```text
M_u pi_(u,a)
```

copies of action `a`.  On the `n`-th visit to `u`, execute the letter of `W_u`
at position `n mod M_u`.

This is a deterministic finite-state controller.  On every complete local
period, its empirical action distribution is exactly `pi_u`, independently of
the order in which different marker states are visited.

#### Proof

The local visit counter advances only when its own state is visited.  In
`M_u` consecutive visits to `u`, every position of `W_u` is used exactly once,
so action `a` occurs exactly `M_u pi_(u,a)` times.  Counters at other states do
not affect this identity.  The product of the local counters is a finite
controller state space. ∎

## 2. Exact prefix discrepancy

### Theorem PP3cgy -- PROVED / LINEAR-OBSERVABLE PREFIX BOUND

Let `G_(u,a,j)` be any rational linear observable, including robust potential
gap, resource consumption, or terminal reverse load.  Define

```text
gbar_(u,j)=sum_a pi_(u,a) G_(u,a,j)
```

and the within-period discrepancy

```text
Delta_(u,j)=max_(0<=r<M_u)
  |sum_(t<r) G_(u,W_u[t],j)-r gbar_(u,j)|.
```

After any `N_u` visits to each state, the deterministic total differs from the
randomized mean total by at most

```text
sum_u Delta_(u,j).
```

The bound is independent of the global interleaving of state visits.

#### Proof

Write `N_u=q_u M_u+r_u`.  Every full period contributes exactly
`M_u gbar_(u,j)`, so only the final prefix of length `r_u` contributes error.
Its absolute error is at most `Delta_(u,j)`.  Summing the signed errors and
using the triangle inequality proves the claim. ∎

## 3. Finite implementation certificate

### Theorem PP3cgz -- PROVED / COUNTER-SCHEDULE AUDIT

A periodic marker implementation is certified by the finite data

1. the rational policy rows `pi_u`;
2. the period words `W_u`;
3. the action counts in every word; and
4. the exact prefix-discrepancy table for every protected observable.

Verification is finite and rational.  Failure identifies one incorrect action
multiplicity, one prefix, one observable, or one counter transition.

#### Proof

The action-count check proves `PP3cgx`.  Exhausting the finitely many proper
prefixes computes every `Delta_(u,j)` and proves `PP3cgy`.  Counter transitions
are a finite deterministic table. ∎

## 4. Stored exact fixture

The audit `scripts/check_periodic_marker_controller_realization.py` uses local
policies `(1/3,2/3)` and `(1/2,1/2)`, realized by periods three and two.  The
product controller has six memory states.  Two robust observables have exact
mean gaps `(1/6,1/6)` and `(1/4,1/4)`, while the mean shared-resource use is
`5/6`.

Across all `961` pairs of local visit counts through thirty, the exact global
prefix errors never exceed `5/6`, `7/6`, and `5/6` for the two gaps and the
resource respectively; all three bounds are attained.

## 5. Prime-patching consequence

A rational marker controller no longer requires fresh randomness or a retained
random seed.  Local cyclic counters realize the certified mean exactly over
complete periods, and the finite prefix table quantifies the only transient
loss under arbitrary boundary-state interleavings.
