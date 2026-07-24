# Low-multiplicity strong-complete seeds beyond order thirteen

PX129 reduces affine-orbit spread to two deterministic graph parameters:

\[
\mu(f)=\max_r\mu_f(r),
\qquad
\tau(f)=\max_{r,t,s}\tau_f(r,t,s).
\]

PX130 gives the first nonlinear example at order thirteen. This chapter records
explicit seeds at later prime orders and compares them with universal counting
lower bounds.

## 1. Explicit seeds through order 23

Use the following permutations in row order.

\[
f_{17}=(0,9,4,10,7,14,16,2,6,15,11,5,8,12,1,3,13),
\]

\[
f_{19}=(13,9,17,6,1,11,8,14,0,2,5,15,10,12,4,16,7,3,18),
\]

\[
f_{23}=(2,6,12,14,11,21,18,20,0,4,8,10,16,9,5,1,19,17,15,13,3,22,7).
\]

## Theorem PX132 -- PROVED FINITE

Each displayed map is strong complete. Together with the PX130 seed, their exact
affine-orbit parameters are:

| Prime \(p\) | \(\mu(f_p)\) | \(\tau(f_p)\) | \(K_2=\mu/p\) | \(K_3=(p-2)\tau/p\) |
|---:|---:|---:|---:|---:|
| 13 | 28 | 8 | \(28/13<3\) | \(88/13<7\) |
| 17 | 28 | 6 | \(28/17<2\) | \(90/17<6\) |
| 19 | 32 | 6 | \(32/19<2\) | \(102/19<6\) |
| 23 | 44 | 8 | \(44/23<2\) | \(168/23<8\) |

For each displayed permutation, exact enumeration verifies that

\[
f,
\qquad x-f(x),
\qquad x+f(x)
\]

are permutations. Enumerating all ordered secants and ordered affine triangle
shapes gives the displayed maxima. PX129 converts them to the orbit constants.

## 2. Universal counting lower bounds

## Theorem PX133 -- PROVED

Every strong complete mapping of \(\mathbb F_p\) satisfies

\[
\boxed{
\mu(f)\ge
\left\lceil\frac{p(p-1)}{p-3}\right\rceil.
}
\]

For every fixed \(t\in\mathbb F_p\setminus\{0,1\}\),

\[
\boxed{
\max_{r,s}\tau_f(r,t,s)
\ge
\left\lceil
\frac{p(p-1)}{(p-3)(p-2)}
\right\rceil.
}
\]

The latter lower bound equals \(3\) at \(p=7\), and equals \(2\) for every
prime \(p\ge11\).

### Proof

There are \(p(p-1)\) ordered pairs \((u,v)\) with \(u\ne v\). Their secant
slope cannot be zero because \(f\) is a permutation. It cannot be \(1\),
because that would repeat a value of \(x-f(x)\), and it cannot be \(-1\), by
the same argument with \(x+f(x)\). Thus the pairs are distributed among only
\(p-3\) allowed slopes.

Fix \(t\ne0,1\). Every ordered pair determines

\[
w=u+t(v-u)
\]

and hence one triple of invariants \((r,t,s)\). The slope has at most \(p-3\)
values and the image ratio has at most \(p-2\) values. Averaging proves the
second bound. The final numerical evaluation is direct. \(\square\)

## 3. Order 29

The compiled exact four-trade search produced

\[
f_{29}=
(11,13,28,18,2,7,23,26,16,9,17,4,1,12,24,19,10,20,5,3,25,27,14,8,15,21,6,22,0).
\]

## Theorem PX134 -- PROVED FINITE

The displayed order-29 map is strong complete and satisfies

\[
\boxed{
\mu(f_{29})=54,
\qquad
\tau(f_{29})=9.
}
\]

Consequently its affine-orbit distribution has

\[
K_2=\frac{54}{29}<2,
\qquad
K_3=\frac{243}{29}<9.
\]

Thus linear secant multiplicity and constant affine-triangle multiplicity persist
at the next tested prime. The triangle constant is one above the proposed bound
of eight, so PX134 supports the asymptotic scale but does not prove the sharp
conjectured constant.

### Proof

Direct exact enumeration verifies strong completeness and computes every secant
and affine-triangle bin. \(\square\)

## 4. Concrete asymptotic conjecture

> **Strong-complete orbit conjecture.** For every sufficiently large odd prime
> \(p\), there is a strong complete mapping \(f_p\) with
> \[
> \mu(f_p)\le2p+2,
> \qquad
> \tau(f_p)\le8.
> \]

By PX129 this would give \(K_2\le2+2/p\) and \(K_3\le8\). PX131 would then
prove the two-direction protected-rainbow spread theorem at every such prime.
A polylogarithmic bound on \(\tau\) may already suffice after re-optimising the
downstream local-load criterion.

## 5. Verification

Run

```bash
python scripts/verify_product_low_multiplicity_seeds.py
```

The verifier checks strong completeness, computes every secant and affine
triangle bin, reproduces all five seed rows, and checks the corrected lower-bound
arithmetic through prime order 101.
