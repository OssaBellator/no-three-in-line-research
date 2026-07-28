# Reverse-collision contraction for labelled strict repair

`docs/345` proves that every fixed locally coupled repair word is injective and
that inherited-load concentration comes only from collisions between different
words.  This chapter replaces the resulting raw word sum by a stepwise operator
bound.  The controlling quantity is the weighted reverse indegree of the
labelled repair action.

No asymptotic branching estimate for the geometric repair policy is claimed.

## 1. The reverse collision operator

Let `X` be a family of signed Hamilton states.  For each state `x`, let `A(x)` be
the finite set of admissible labelled locally coupled repair steps.  A label
`ell` acts by the partial bijection

```text
Phi_ell:x -> y
```

from PP3bpz.  A repair policy assigns probabilities

```text
p_x(ell)>=0,
sum_(ell in A(x)) p_x(ell)<=1.
```

The missing row mass may represent absorption, rejection, or transfer to a
second action.

For a nonnegative source load `f` on signed states, define the one-step pushed
load

```text
(Rf)(y)=sum_(ell: Phi_ell^(-1)(y) exists)
          f(Phi_ell^(-1)(y))
          p_(Phi_ell^(-1)(y))(ell).
```

Define the weighted reverse indegree

```text
kappa(y)=sum_(ell: Phi_ell^(-1)(y) exists)
           p_(Phi_ell^(-1)(y))(ell),

kappa_*=sup_y kappa(y).
```

### Proposition PP3bqk -- PROVED / EXACT REVERSE COLLISION FORMULA

The displayed expression for `Rf` is exact, and

```text
||Rf||_infinity <= kappa_* ||f||_infinity.
```

#### Proof

For a fixed label, PP3bpz supplies at most one inverse predecessor of `y`.
Therefore the incoming column is exactly the sum over inverse labels shown
above.  Bounding each predecessor load by `||f||_infinity` gives

```text
(Rf)(y)<=||f||_infinity kappa(y).
```

Take the supremum over `y`. ∎

Thus distinct words need not be enumerated.  Their merging is generated one
step at a time by the reverse collision operator.

## 2. Depth-dependent contraction

Allow the policy and admissible labels to depend on the strict-repair depth.
Write `R_j` and `kappa_j` for the step from depth `j` to depth `j+1`.

### Theorem PP3bql -- PROVED / MULTISTEP COLLISION PRODUCT

For every nonnegative initial load `f_0`, the depth-`d` load satisfies

```text
f_d=R_(d-1)...R_0 f_0,

||f_d||_infinity
 <= ||f_0||_infinity product_(j=0)^(d-1) kappa_j.
```

In particular, if `kappa_j<=kappa` at every step, then

```text
||f_d||_infinity<=kappa^d ||f_0||_infinity.
```

#### Proof

Apply PP3bqk successively at each depth. ∎

This is the path-collision analogue of a pointwise heat-kernel estimate: strict
repair itself contracts columns whenever forward randomization dominates
reverse labelled merging.

## 3. Forward branching versus reverse multiplicity

Suppose the policy chooses uniformly from its admissible labels.  Let

```text
B=min_x |A(x)|
```

over the active source states, and let

```text
D=max_y number of labels ell
          whose inverse predecessor exists and is active.
```

### Corollary PP3bqm -- PROVED / DEGREE-RATIO CONTRACTION

Under the uniform policy,

```text
kappa_*<=D/B.
```

Consequently the depth-`d` signed column charge is at most

```text
(D/B)^d
```

for unit initial source load.

More generally, it is enough that every individual transition probability be
at most `1/B`; exact uniformity is unnecessary.

#### Proof

At most `D` inverse labels contribute to one target column, and each has
probability at most `1/B`.  Substitute in PP3bqk and PP3bql. ∎

The ratio uses labelled transitions.  Several labels may share the same source
or target cycle; all such collisions are already counted in `D`.

## 4. Absorption at variable strict depth

Let `g_d` be the load first absorbed into the parity-clean terminal set after
exactly `d` strict steps.  Suppose every strict trajectory has length at most
`h`, as happens when an integer potential decreases at every step.

### Theorem PP3bqn -- PROVED / ABSORBING COLUMN BOUND

If the stepwise reverse collision bounds are `kappa_0,...,kappa_(h-1)`, then

```text
||sum_(d=1)^h g_d||_infinity
 <= ||f_0||_infinity
    sum_(d=1)^h product_(j=0)^(d-1) kappa_j.
```

If every `kappa_j<=kappa`, this becomes

```text
kappa+...+kappa^h.
```

For `kappa<1`, it is at most

```text
kappa/(1-kappa).
```

#### Proof

The first-absorption load at depth `d` is obtained from the unabsorbed depth-`d`
load by deleting coordinates or multiplying them by absorption probabilities
at most one.  This cannot increase the `L^infinity` norm.  Apply PP3bql at each
depth and sum the terminal columns. ∎

The sum is necessary because terminal mass from different strict depths may
collide at the same clean signed state.

## 5. Transfer to inherited-load warmness

Let `L_F` be the complete strict terminal column from `docs/345`, let `h_F` be
the inherited fibre-relative density from `docs/341`, and let `K` be any
stochastic clean-cycle kernel.

### Corollary PP3bqo -- PROVED / BRANCHING-TO-SWITCH-CHARGE INTERFACE

Under the hypotheses of PP3bqn,

```text
||h_F||_infinity
 <= ||L_F||_infinity
 <= sum_(d=1)^h product_(j=0)^(d-1) kappa_j,

||K^t h_F||_infinity
 <= sum_(d=1)^h product_(j=0)^(d-1) kappa_j.
```

For a uniform policy with forward branching at least `B_j` and reverse labelled
multiplicity at most `D_j` at depth `j`, one may substitute

```text
kappa_j<=D_j/B_j.
```

#### Proof

The strict terminal bound is PP3bqn.  PP3bqc says fibre regeneration averages
signed terminal columns, and stochastic clean evolution is an `L^infinity`
contraction. ∎

## 6. Revised predecessor-charge frontier

The inherited-load problem is now reduced to local labelled degree estimates.

1. A fixed word contributes at most one predecessor by `docs/345`.
2. All word collisions are generated by weighted reverse indegrees `kappa_j`.
3. Forward branching `B_j` and reverse multiplicity `D_j` give the explicit
   ratio `D_j/B_j`.
4. If this ratio is uniformly below one, strict repair already contracts column
   charge geometrically before the clean-cycle heat phase.
5. If it is near or above one, the exact obstruction is a concentration of many
   inverse labels on the same signed target, which can be audited or attacked by
   reweighting labels.

The geometric task is therefore sharper than counting all admissible repair
words: construct a covering local-repair policy with large forward choice and
small weighted reverse indegree, preferably throughout the logarithmic
frustration window.

The next theorem identifier after this chapter is `PP3bqp`.
