# Optimized bounded-forbidden matching spread

PX196 uses the uniform local-lemma witness `x=2/t` and obtains the convenient
but crude density factor `e^(-4Delta)`.  The same canonical bad-event system
supports a nearly optimal witness.  The resulting cylinder factor tends to
`e^Delta` as the block order grows and is uniformly at most `e^(2Delta)` with
two units of slack beyond the existing `8Delta` threshold.

Let `F` be a forbidden-position graph on a balanced `t x t` bipartite grid, with
maximum row and column degree at most `Delta`.  Write `Omega_F` for the allowed
perfect matchings.

## 1. Optimized lopsided-local-lemma witness

### Theorem PX232 -- PROVED

Assume

\[
\boxed{t\ge8\Delta.}
\]

Put

\[
\boxed{x=\frac1{t-4\Delta}}
\]

and

\[
\boxed{
\mathcal C(t,\Delta)
=
\left(1-\frac1{t-4\Delta}\right)^{-\Delta t}.
}
\]

Then

\[
\boxed{
|\Omega_F|
\ge
\frac{t!}{\mathcal C(t,\Delta)}.
}
\]

Consequently every compatible prescribed partial matching `E` of rank `r`
satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{\mathcal C(t,\Delta)}{(t)_r},
}
\]

for `M` uniform on `Omega_F`.

Moreover,

\[
\boxed{
\mathcal C(t,\Delta)
=
\exp\left(\Delta+O\left(\frac{\Delta^2+\Delta}{t}\right)\right)
}
\]

at fixed `Delta`, and if

\[
\boxed{t\ge8\Delta+2,}
\]

then

\[
\boxed{
\mathcal C(t,\Delta)\le e^{2\Delta}.
}
\]

### Proof

For every forbidden cell `e`, let `A_e` be the event that a uniformly random
permutation uses `e`.  Then

\[
\Pr(A_e)=\frac1t.
\]

The canonical conflict graph is a negative dependency graph, and every event
has at most `2Delta-2` neighbours.  It is enough to verify the stronger
inequality with exponent `2Delta`:

\[
\frac1t
\le
x(1-x)^{2\Delta}.
\]

Bernoulli's inequality gives

\[
x(1-x)^{2\Delta}
\ge
x(1-2\Delta x)
=
\frac{t-6\Delta}{(t-4\Delta)^2}.
\]

The last quantity is at least `1/t` exactly when

\[
t(t-6\Delta)
\ge
(t-4\Delta)^2,
\]

which reduces to `t>=8Delta`.  The lopsided local lemma therefore applies.
Its standard lower bound gives

\[
\Pr(\text{no forbidden cell})
\ge
(1-x)^{|F|}
\ge
(1-x)^{\Delta t}
=
\frac1{\mathcal C(t,\Delta)}.
\]

Multiplying by `t!` proves the family-size estimate.  At most `(t-r)!`
permutations contain `E`, yielding the cylinder bound.

For the asymptotic expression, expand `-log(1-x)` with
`x=1/(t-4Delta)`.  For the uniform estimate use

\[
-\log(1-x)
\le
\frac{x}{1-x}
=
\frac1{t-4\Delta-1}.
\]

Thus

\[
\log\mathcal C(t,\Delta)
\le
\frac{\Delta t}{t-4\Delta-1}
\le
2\Delta
\]

when `t>=8Delta+2`. \(\square\)

The factor `e^(4Delta)` in PX196 may therefore be replaced throughout by the
order-sensitive factor `mathcal C(t,Delta)` and, with minimal extra slack, by
`e^(2Delta)`.

## 2. Residual and conditioned cylinders

### Theorem PX233 -- PROVED

Let `E_0` be an extendable compatible partial matching of rank `a`, and put

\[
n=t-a.
\]

If `n>=8Delta`, then `E_0` has at least

\[
\boxed{
\frac{n!}{\mathcal C(n,\Delta)}
}
\]

allowed extensions.  Under the conditional uniform measure, every compatible
residual rank-`r` partial matching `E_1` satisfies

\[
\boxed{
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\le
\frac{\mathcal C(n,\Delta)}{(n)_r}.
}
\]

If `n-r>=8Delta`, the matching lower cylinder bound is

\[
\boxed{
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\ge
\frac1{\mathcal C(n-r,\Delta)(n)_r}.
}
\]

### Proof

Delete the exposed rows and columns.  The residual forbidden graph has the same
maximum degree `Delta`.  Apply PX232 in orders `n` and `n-r`, exactly as in the
proofs of PX198--PX199. \(\square\)

Thus sequential exposure preserves the improved constant; it does not revert
to `e^(4Delta)`.

## 3. Universal substitution in the collateral ledger

### Corollary PX234 -- PROVED

Every occurrence of `e^(4Delta)` in the unconditioned cylinder-based bounds
PX225 and PX229--PX231 may be replaced by

\[
\boxed{
\mathcal C(s,\Delta)
}
\]

for a retained block of order `s>=8Delta`.  In particular, if
`s>=8Delta+2`, then

\[
\mathbb E T_{1,2}
<
e^{2\Delta}Km(s-1),
\]

\[
\mathbb E T_{2,2}
\le
\frac12e^{2\Delta}L_Z,
\]

\[
\mathbb E T_{2,3}
\le
e^{2\Delta}L_Z(s-2),
\]

and

\[
\mathbb E T_{3,3}
\le
\frac13e^{2\Delta}.
\]

The adaptive support-four choice can be strengthened to

\[
\boxed{
q_*
=
\min\left\{
\frac1{\log(2t)},
\frac{t}{1024e^{2\Delta}N\mathfrak d(N)}
\right\},
}
\]

provided the retained order is at least `8Delta+2`.  Under the corresponding
size hypotheses, it still gives

\[
\boxed{
\mathbb E T_{2,4}\le\frac{s}{2}.
}
\]

### Proof

Every cited estimate was obtained by summing compatible cylinders and using
only the upper bound `e^(4Delta)/(s)_r`.  Substitute PX232.  For the explicit
uniform displays use `mathcal C(s,Delta)<=e^(2Delta)`.

For support four, the proof of PX225 gives

\[
\frac{\mathbb E T_{2,4}}s
\le
512\mathcal C(s,\Delta)
\frac{qN\mathfrak d(N)}t.
\]

The displayed choice of `q_*` and the uniform `e^(2Delta)` estimate make this at
most `1/2`. \(\square\)

## 4. Quantitative effect

At fixed recursion depth:

- the cylinder loss is asymptotically `e^Delta`, not `e^(4Delta)`;
- the threshold constant in adaptive support-four thinning loses `e^(2Delta)`
  rather than `e^(4Delta)`;
- every exact small-sector coefficient improves by the same exponential factor;
- conditioning retains the improvement.

This does not yet prove strict negative drift, but it removes one half of the
previous exponent loss without changing the bank or introducing additional
structure.

## 5. Verification

Run

```bash
python scripts/verify_product_optimized_spread.py
```

The verifier checks the optimized witness inequality at and above the sharp
`8Delta` threshold, the exact density factor, its `e^(2Delta)` envelope, the
asymptotic exponent, and all substitutions in PX234.
