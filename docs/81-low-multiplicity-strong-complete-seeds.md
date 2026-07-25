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

## 1. Seeds through order 23

Use the following permutations in row order:

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

## 3. Orders 29, 31, 37, and 41

The exact searches produced

\[
f_{29}=(11,13,28,18,2,7,23,26,16,9,17,4,1,12,24,19,10,20,5,3,25,27,14,8,15,21,6,22,0),
\]

\[
f_{31}=(0,10,22,5,14,16,9,29,6,26,17,1,18,27,19,23,3,12,2,4,8,13,15,24,20,7,30,21,25,28,11),
\]

\[
f_{37}=(0,10,17,25,21,19,8,32,35,12,36,22,33,31,24,2,7,14,11,15,6,28,20,27,16,30,1,9,4,23,29,26,3,34,13,18,5),
\]

\[
f_{41}=(0,14,28,5,22,39,18,29,11,37,27,7,1,19,38,10,13,16,25,34,2,30,33,17,40,23,31,15,6,9,20,4,36,12,35,26,3,21,24,8,32).
\]

## Theorem PX134 -- PROVED FINITE

Their exact parameters are

| Prime \(p\) | \(\mu(f_p)\) | \(\tau(f_p)\) | \(K_2\) | \(K_3\) |
|---:|---:|---:|---:|---:|
| 29 | 54 | 9 | \(54/29<2\) | \(243/29<9\) |
| 31 | 44 | 6 | \(44/31<2\) | \(174/31<6\) |
| 37 | 54 | 7 | \(54/37<2\) | \(245/37<7\) |
| 41 | 64 | 8 | \(64/41<2\) | \(312/41<8\) |

Thus linear secant multiplicity and constant affine-triangle multiplicity persist
through order 41.

## 4. Orders 43 and 47

The compiled randomized exact-cover search produced

\[
f_{43}=(0,28,21,23,3,12,24,30,13,42,32,4,1,41,26,7,22,15,39,14,11,34,19,38,25,27,8,36,16,33,40,17,35,6,2,18,10,31,9,20,5,37,29),
\]

\[
f_{47}=(0,45,36,41,12,21,7,29,13,1,40,32,5,27,18,3,35,6,17,37,14,16,31,26,4,23,43,34,30,42,11,46,10,39,44,20,9,2,24,15,19,25,38,33,8,22,28).
\]

## Theorem PX135 -- PROVED FINITE

Both maps are strong complete and satisfy

\[
(\mu(f_{43}),\tau(f_{43}))=(76,9),
\]

\[
(\mu(f_{47}),\tau(f_{47}))=(82,9).
\]

Consequently both affine-orbit measures have \(K_2<2\) and \(K_3<9\).
This extends the constant-scale evidence to both residue classes modulo four.

## 5. Order 53

The first exact-cover sample at order 53 already gave

\[
\begin{aligned}
f_{53}={}&(0,27,4,26,48,16,5,13,22,7,3,38,25,41,30,52,1,14,21,31,40,51,43,28,18,11,35,19,10,46,49,32,39,2,23,45,12,8,17,47,36,6,20,15,24,33,50,9,29,44,37,34,42).
\end{aligned}
\]

## Theorem PX136 -- PROVED FINITE

The displayed map is strong complete and satisfies

\[
\boxed{
\mu(f_{53})=80,
\qquad
\tau(f_{53})=7.
}
\]

Hence

\[
K_2=\frac{80}{53}<1.51,
\qquad
K_3=\frac{51\cdot7}{53}<6.74.
\]

This is the strongest large-order seed in the current census. In particular, it
beats the proposed bounds \(\mu\le2p+2\) and \(\tau\le8\) simultaneously.

## 6. Two bounded-complexity refutations

## Theorem PX137 -- PROVED FINITE

Two natural bounded-complexity seed families fail throughout the tested range.

1. There is no nonlinear cubic polynomial \(f\in\mathbb F_p[x]\) for which
   \(f\), \(f-x\), and \(f+x\) are all permutations, for any prime
   \(5\le p\le101\).
2. There is no completed fractional-linear permutation
   \[
   f(x)=\frac{ax+b}{x+d},
   \]
   with the pole completed by the projective value \(a\), for which
   \(f\), \(f-x\), and \(f+x\) are all permutations, over the same prime range.

These are finite refutations, not asymptotic impossibility theorems. They show
that the observed low triangle multiplicity is not coming from either of the
simplest bounded-degree algebraic models.

## 7. Concrete asymptotic conjecture

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

## 8. Verification

Run

```bash
python scripts/verify_product_low_multiplicity_seeds.py
```

The verifier checks strong completeness, computes every secant and affine
triangle bin, reproduces all eleven seed rows, and checks the corrected
lower-bound arithmetic through prime order 101. The cubic and Möbius censuses
are recorded separately in the search notes; their compact repository verifier
is the next reproducibility task.
