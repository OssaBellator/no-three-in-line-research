# Potential compactification of shell cycle constraints

`docs/481` separates violated shell cycles and gives a compact circulation dual.
When every cycle requirement is additive over its edges, the exponentially many
cycle inequalities also admit a compact primal formulation using vertex
potentials.

Let directed edge `e=(u,v)` have affine residual

```text
w_e(x)=b_e-sum_r a_(e,r) x_r,
```

where `x_r>=0` are attenuation variables.  The full shell requirement is

```text
sum_(e in C) w_e(x) <= 0
```

for every directed cycle `C`.

## 1. Cycle--potential equivalence

### Theorem PP3cgr -- PROVED / NO-POSITIVE-CYCLE POTENTIAL

All directed cycles have nonpositive residual sum if and only if there is a
vertex potential `h` such that

```text
h_v-h_u >= w_(u,v)(x)
```

for every directed edge `(u,v)`.

#### Proof

Summing the edge inequalities around a cycle telescopes the potential differences
to zero and proves necessity of nonpositive cycle sums.  Conversely, when no
positive cycle exists, add a super-source of zero-weight edges and let `h_v` be
the maximum weight of a simple walk from the super-source to `v`.  Repeating a
nonpositive cycle cannot improve a walk, so the maximum is finite and attained
by a simple walk.  Appending edge `(u,v)` gives `h_v>=h_u+w_(u,v)`. ∎

## 2. Compact attenuation LP and dual

### Theorem PP3cgs -- PROVED / POTENTIAL-FORM SHELL LP

The minimum-cost additive shell attenuation is the finite rational LP

```text
minimize   sum_r c_r x_r
subject to h_v-h_u >= b_e-sum_r a_(e,r)x_r  for every edge e=(u,v),
           x_r>=0,
           h_root=0.
```

Its dual is a nonnegative circulation `f_e` maximizing
`sum_e b_e f_e`, subject to the attenuation-capacity inequalities

```text
sum_e a_(e,r) f_e <= c_r.
```

Equal primal and dual objectives certify the full infinite-looking cycle system.

#### Proof

The preceding theorem proves equivalence between the edge-potential formulation
and all cycle inequalities.  Taking the ordinary LP dual of the compact system
produces flow conservation at every free potential and one capacity inequality
for each attenuation variable.  Rational strong duality gives the certificate. ∎

## 3. Exact separation by maximum cycle mean

### Theorem PP3cgt -- PROVED / MAXIMUM-CYCLE-MEAN WITNESS

For a proposed attenuation `x`, a violated shell cycle exists exactly when the
maximum directed cycle mean of the rational edge weights `w_e(x)` is positive.
An exact maximum-cycle-mean algorithm returns either a positive cycle witness or
a proof that the compact potential system is feasible.

#### Proof

A cycle has positive total residual exactly when its mean residual is positive.
The maximum over finitely many simple cycles therefore has the same sign as the
largest cycle sum.  Rational maximum-cycle-mean algorithms compare only rational
path-weight ratios and return an exact witness. ∎

## 4. Stored exact fixture

The audit `scripts/check_shell_potential_compactification.py` uses a bidirected
triangle with five simple cycles.  At trial attenuation `(1/2,1/2,1/2)`, the
forward triangle has residual sum `3/2` and maximum cycle mean `1/2`.  The compact
LP has optimum attenuation `(1,1,1)` of cost `3`; zero vertex potentials certify
all edge inequalities.  One unit of circulation around the forward triangle
saturates every attenuation capacity and has dual value `3`.

## 5. Prime-patching consequence

Clean-macro shell control now has both an oracle formulation and a compact
potential formulation.  The latter can be inserted directly into larger rational
optimization systems, while the maximum-cycle-mean oracle supplies a concrete
shell loop whenever a proposed attenuation is insufficient.
