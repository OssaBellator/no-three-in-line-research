# Exact denominator profile of the reflected CD scalar

**Branch:** `research/bounded-denominator-absorbers`

BDA5s writes the reflected two-local offset as

$$
O_{CD}(w)=wab(2h+q).
$$

At the level of the integer valuation, `2h+q` can have cancellation above a prime-power divisor of `q`. That extra height is invisible to the denominator profile. This note replaces the apparent cancellation tower by an exact gcd, reduced-unit, and scalar-slot description.

## Setup

Let

$$
A=wab
$$

for one reflected role, or

$$
A=(u-v)ab
$$

for the separation of two roles. The relevant scalar is

$$
X_A(h)=A(2h+q).
$$

## BDA5aa -- exact reflected denominator content -- PROVED

For every integers `A,h` and positive denominator `q`,

$$
\boxed{
\gcd(X_A(h),q)=\gcd(2Ah,q).
}
$$

In particular,

$$
\boxed{
\gcd(wab(2h+q),q)=\gcd(2wabh,q),
}
$$

and

$$
\boxed{
\gcd((u-v)ab(2h+q),q)=
\gcd(2(u-v)abh,q).
}
$$

### Proof

The two integers satisfy

$$
X_A(h)-2Ah=Aq.
$$

They are therefore congruent modulo `q`. Two congruent integers have the same gcd with the modulus. QED.

## Prime-power form

For every prime power

$$
\ell^E\Vert q,
$$

BDA5aa is equivalent to

$$
\boxed{
\min\{E,v_\ell(A(2h+q))\}
=
\min\{E,v_\ell(2Ah)\}.
}
$$

Thus even when

$$
v_\ell(2h+q)>E,
$$

there is no additional denominator-visible state.

## BDA5ab -- exact reduced unit profile -- PROVED

Put

$$
G_A(h)=\gcd(2Ah,q)
$$

and

$$
q_A(h)=q/G_A(h).
$$

If `q_A(h)>1`, then

$$
\boxed{
\gcd\left(\frac{A(2h+q)}{G_A(h)},q_A(h)\right)=1,
}
$$

and

$$
\boxed{
\frac{A(2h+q)}{G_A(h)}
\equiv
\frac{2Ah}{G_A(h)}
\pmod{q_A(h)}.
}
$$

Hence the complete denominator-visible reflected profile consists of:

1. the effective denominator `q_A(h)`;
2. the reduced unit residue `2Ah/G_A(h) mod q_A(h)`.

No cancellation-height label is needed.

### Proof

BDA5aa gives

$$
G_A(h)=\gcd(A(2h+q),q).
$$

Dividing the scalar and modulus by their exact gcd gives the coprimality assertion. Since `A(2h+q)-2Ah=Aq`, division by `G_A(h)` gives the displayed congruence modulo `q/G_A(h)`. QED.

## BDA5ac -- reflected scalar congruence and slot spacing -- PROVED

Fix `A,q` and a residue `xi mod q`. Put

$$
d_A=\gcd(2A,q),
\qquad
m_A=q/d_A.
$$

The congruence

$$
A(2h+q)\equiv xi\pmod q
$$

has no solution unless

$$
d_A\mid xi.
$$

When it is soluble, its solutions form exactly one residue class modulo

$$
\boxed{m_A=q/\gcd(2A,q).}
$$

Consequently, if

$$
1\le h_1<\cdots<h_K\le H
$$

all have the same reflected scalar residue, then

$$
\boxed{
H\ge 1+m_A(K-1),
}
$$

and

$$
\boxed{
K\le 1+\left\lfloor\frac{H-1}{m_A}\right\rfloor.
}
$$

### Proof

Modulo `q`, the reflected congruence is exactly

$$
2Ah\equiv xi\pmod q.
$$

The standard linear-congruence criterion gives solubility precisely when `d_A` divides `xi`, and then gives one class modulo `q/d_A`. Distinct positive representatives in one class differ by at least `m_A`, proving the spacing bounds. QED.

## BDA5ad -- cancellation towers are denominator-invisible -- PROVED

For the reflected role offset and for every two-role separation, any valuation increase of `2h+q` above the exponent visible in `q` affects only the unreduced integer offset. It cannot change:

1. the effective denominator;
2. the reduced unit residue;
3. the reflected scalar slot spacing;
4. the finite transition profile modulo `q`.

The reflected `CD` channel therefore enters BDA6 through the same finite scalar machinery as the non-wall channels: an exact gcd divisor, a reduced unit, and one arithmetic progression of admissible scales.

### Proof

The first two claims are BDA5aa--BDA5ab, and the third is BDA5ac. Every finite denominator transition is determined by the scalar modulo `q`, so the fourth follows from

$$
A(2h+q)\equiv2Ah\pmod q.
$$

QED.

## Interface consequence

BDA5s remains the exact integer valuation statement, but its apparent equal-valuation cancellation case does not enlarge the denominator profile alphabet. Repeated reflected offsets now route to:

- a strict effective-denominator divisor through `G_A(h)`;
- a coprime reduced unit at `q_A(h)`;
- or a repeated scalar class spaced by `q/gcd(2A,q)`.

The reflected scalar is therefore no longer a separate arithmetic bottleneck. Remaining work lies in the affine-anchor/dispersed-anchor alternatives, higher-rank collateral, and termination of the finite transition graph.

## Finite check

`scripts/verify_bda_reflected_scalar.py` exhausts signed role coefficients, scales and denominators, checks the exact gcd and prime-power truncation identities, verifies the reduced-unit profile, and compares every reflected congruence solution set with its predicted single scalar-slot class.