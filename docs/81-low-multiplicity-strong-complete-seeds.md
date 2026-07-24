# Low-multiplicity strong-complete seeds beyond order thirteen

PX129 reduces affine-orbit spread to two deterministic graph parameters:

\[
\mu(f)=\max_r\mu_f(r),
\qquad
\tau(f)=\max_{r,t,s}\tau_f(r,t,s).
\]

PX130 gives the first nonlinear example at order thirteen. This chapter records
explicit seeds at the next three prime orders and compares them with universal
counting lower bounds.

## 1. Explicit seeds

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

Each displayed map is strong complete. Their exact affine-orbit parameters are:

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

are permutations. Enumerating all ordered secants and all ordered affine
triangle shapes gives the displayed maxima. PX129 converts them to the orbit
constants. The seeds were found by randomized exact search, but the theorem is
only the deterministic verification of the displayed maps.

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
the same argument with \(x+f(x)\). Thus the ordered pairs are distributed among
only \(p-3\) allowed slopes, proving the first bound.

Fix \(t\ne0,1\). Every ordered pair determines the third row

\[
w=u+t(v-u),
\]

and hence one triple of invariants \((r,t,s)\). The slope \(r\) has at most
\(p-3\) values. Since \(f(w)\) is distinct from \(f(u),f(v)\), the image ratio
\(s\) is neither zero nor one and has at most \(p-2\) values. Averaging gives
the second bound. The final numerical evaluation is direct. \(\square\)

Thus the experimental triangle multiplicities six and eight are within a
constant factor of the absolute optimum. The secant multiplicities are also
within a factor below three of the averaging lower bound.

## 3. Concrete asymptotic conjecture

> **Strong-complete orbit conjecture.** For every sufficiently large odd prime
> \(p\), there is a strong complete mapping \(f_p\) with
> \[
> \mu(f_p)\le2p+2,
> \qquad
> \tau(f_p)\le8.
> \]

By PX129 this would give

\[
K_2\le2+\frac2p,
\qquad
K_3\le8
\]

for one-stage affine-orbit spread. PX131 would then prove the two-direction
protected-rainbow spread theorem at every such prime.

The conjecture is stronger than needed. A polylogarithmic bound on \(\tau(f_p)\),
combined with the polynomial high-direction codegree saving from PX82, may
already suffice after re-optimizing the downstream local-load criterion.

## 4. Verification

Run

```bash
python scripts/verify_product_low_multiplicity_seeds.py
```

The verifier checks strong completeness, computes every secant and affine
triangle bin, reproduces the table, and checks the corrected lower-bound
arithmetic through prime order 101.
