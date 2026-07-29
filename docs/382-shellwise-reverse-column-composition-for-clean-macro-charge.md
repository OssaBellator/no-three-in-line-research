# Shellwise reverse-column composition for clean-macro charge

The terminal normalizer audits prove contraction for the outer closing shell, while
`docs/350` and `docs/352` reduce the clean-macro geometry to cycle-minimum shells
with at most one shell of orientation correction. This chapter gives the exact
operator statement needed to extend a local shell certificate through the whole
macro horizon.

The result is general. It does not verify nonterminal shell contraction and does
not bound the shell depth asymptotically.

## 1. Reverse-column norm of one shell kernel

Let `X_j` be the clean signed states whose underlying cycle has cycle-minimum
shell index `j`. Let `Q_j(x,y)` be a nonnegative substochastic kernel supported
from `X_j` to `X_{j-1}`. Missing row mass may be assigned to a different action.

Define its reverse-column norm by

```text
kappa_j = max_(y in X_{j-1}) sum_(x in X_j) Q_j(x,y).
```

For a nonnegative incoming load `a_j` on `X_j`, define

```text
a_(j-1)(y) = sum_(x in X_j) a_j(x) Q_j(x,y).
```

### Proposition PP3bui -- PROVED / POSITIVE SHELL OPERATOR NORM

For every nonnegative incoming load,

```text
||a_(j-1)||_infinity
 <= kappa_j ||a_j||_infinity.
```

#### Proof

For each target `y`,

```text
a_(j-1)(y)
 = sum_x a_j(x)Q_j(x,y)
 <= ||a_j||_infinity sum_x Q_j(x,y)
 <= kappa_j ||a_j||_infinity.
```

Taking the maximum over `y` proves the claim. ∎

This statement is insensitive to how the load was created. In particular it
applies to inherited strict-repair load after fibre regeneration.

## 2. Exact multiplication across the macro horizon

Let

```text
Q_h, Q_(h-1), ..., Q_1
```

be consecutive shell kernels, and let their composition send `X_h` to `X_0`.

### Theorem PP3buj -- PROVED / SHELLWISE CHARGE PRODUCT

The composed reverse-column norm obeys

```text
kappa(Q_h Q_(h-1) ... Q_1)
 <= product_(j=1)^h kappa_j.
```

Equivalently, every incoming load satisfies

```text
||a_0||_infinity
 <= [product_(j=1)^h kappa_j] ||a_h||_infinity.
```

#### Proof

Apply `PP3bui` successively at shells `h,h-1,...,1`. ∎

For a fibre-capacity label policy at shell `j`, write

```text
Z_j(x) = sum_(closing labels T from x) F(eta_T),
```

and choose a label with probability `F(eta_T)/Z_j(x)` before regenerating
uniformly in the target fibre. Exactly as in `PP3bsb`, its local column norm is

```text
kappa_j(eta)
 = sum_(x in X_j) m_j(x,eta)/Z_j(x).
```

Therefore an all-shell proof requires only a separate bound on this local
quantity at each cycle-minimum boundary. No path enumeration and no bookkeeping
of intermediate orientations survives the product estimate.

## 3. Relation to cycle-minimum depth and fibre width

The shell index here is `d_min(rho)`, not the exact distance of an individual
orientation. `PP3brg` shows finitely that every nonvalid orientation lies at
distance

```text
d(rho,e) in {d_min(rho), d_min(rho)+1}.
```

Hence two independent statements close the clean-macro trajectory:

1. a bound on the number of cycle-minimum shell transitions;
2. a bound on the product of their reverse-column norms.

The first is geometric; the second is analytic. The adjacent-fibre width result
prevents an unbounded orientation correction from being hidden inside the
cycle-coordinate argument.

## 4. Conditional finite budget at the robust terminal constant

The robust terminal audit gives the relaxed local constant

```text
rho = 54752/55335 < 1.
```

### Corollary PP3buk -- PROVED / CONDITIONAL UNIFORM-SHELL BUDGET

If every adjacent cycle-minimum shell at an audited size admitted a supported
kernel with reverse-column norm at most `rho`, then the complete macro charge
would be at most `rho^h`, where `h` is the cycle-minimum horizon.

For the exact audited horizons `h=3,4,5`, this would give

```text
h=3:
  rho^3
   = 164134532907008/169433679720375
   = 0.9687243597...;

h=4:
  rho^4
   = 8986693945724502016/9375612667326950625
   = 0.9585180473...;

h=5:
  rho^5
   = 492039466916307934380032/518799526946536812834375
   = 0.9484192667....
```

These numbers are conditional illustrations, not audited all-shell charges.
They show that a uniform shell constant below one does not need to improve with
depth: multiplication strengthens the margin.

The remaining exact computational task is now sharply local:

```text
for each adjacent cycle-minimum shell,
audit or prove max_eta sum_x m_j(x,eta)/Z_j(x) < 1.
```

The remaining asymptotic task is to combine a uniform local bound with a bound on
the cycle-minimum shell depth. Neither is proved here.

The next theorem identifier after this chapter is `PP3bul`.
