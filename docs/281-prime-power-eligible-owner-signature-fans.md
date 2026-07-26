# Eligible owner pairs form finite prime-power signature fans

CMR1406--CMR1413 give a lattice-capacity pair envelope but temporarily enlarge
the owner-eligible set to every selected response edge.  Eligibility is in fact
fixed before sampling.  Removing ineligible earlier entering edges gives a
sharper exact conditional pair star.  In a prime-power owner, its remaining
pairs have a finite first-separation, projective-direction and height signature.
A heavy signature is realized simultaneously in one response and concentrates
on one real line or a bounded direction fan.

Retain the old matching `M`, the absolute edge order `prec`, and an allowed
edge `a notin M`.  For another allowed response edge `b`, define

\[
\chi_a^M(b)
=
\mathbf 1_{\{b\in M\text{ or }a\prec b\}}.
\]

## Eligibility is response independent

### Theorem CMR1414 -- PROVED

Conditioned on `a in R`, the response-layer cells eligible to accompany owner
`a` are exactly

\[
\boxed{
\{b\in R\setminus\{a\}:\chi_a^M(b)=1\}.
}
\]

Together with the fixed opposite matching `O`, this is precisely the set
`E_a(R)` from CMR1399.

### Proof

A selected response edge in `M` was already present and is not entering, so it
never precedes `a` in the entering-owner order.  A selected edge outside `M`
is entering and is eligible exactly when it follows `a` in the fixed order.
These are the two cases in `chi_a^M`. ∎

## Exact eligible capacity star

Define

\[
\mathscr C_e^{\rm elig}(a)
=
\sum_{\substack{b\in O\\a,b\text{ nonaxis}}}
c_n(h(a,b))
+
\frac1{p_e(a)}
\sum_{\substack{b\in E(H_e)\setminus\{a\}\\
                 \{a,b\}\text{ compatible}\\
                 a,b\text{ nonaxis}}}
\chi_a^M(b)p_e(a,b)c_n(h(a,b)).
\]

### Theorem CMR1415 -- PROVED

Conditioned on `a in R`,

\[
\boxed{
\mathbb E
\left[
\sum_{b\in E_a(R)}c_n(h(a,b))
\ \middle|\ a\in R
\right]
=
\mathscr C_e^{\rm elig}(a).
}
\]

Consequently

\[
\boxed{
 g_e(a)
\le
\Gamma_e^{\rm elig}(a)
:=\frac12\mathscr C_e^{\rm elig}(a)
\le
\Gamma_e^{\rm cap}(a).
}
\]

### Proof

Use CMR1414 and the exact conditional pair probability
`p_e(a,b)/p_e(a)`.  Then condition the realized capacity inequality CMR1407.
Dropping `chi_a^M` recovers the larger envelope of CMR1408--CMR1409. ∎

For `a in M`, the exact owner weight is zero and we set
`Gamma_e^{elig}(a)=0`.

## Unique prime-power pair signature

Assume now that the inherited owner side is

\[
n=p^k.
\]

For a nonaxis pair `a,b`, write

\[
b-a=G(u,v),
\]

where `G>0` and `(u,v)` is a canonically oriented primitive integer vector.
Put

\[
s(a,b)=v_p(G),
\qquad
\delta(a,b)=[u:v]\in\mathbb P^1(\mathbb F_p),
\qquad
H(a,b)=2^{\lfloor\log_2 h(a,b)\rfloor}.
\]

Also record the type `t(a,b)`, equal to `fixed` when `b in O` and `response`
otherwise.

### Theorem CMR1416 -- PROVED

Every eligible owner--partner pair has one signature

\[
\boxed{
\sigma(a,b)=
(t,s,\delta,H).
}
\]

Here `0<=s<=k-1`.  At depth `s`, the two cells occupy the same coordinate
prefix cell, namely the residue of `a` modulo `p^s`; they separate at the next
digit in projective direction `delta`.

### Proof

The integer gcd `G` and primitive direction are unique after fixing the sign
convention.  Since the cells are distinct and lie in a side-`p^k` board,
`v_p(G)<=k-1`.  Division by `p^s` leaves at least one coordinate difference
nonzero modulo `p`, giving the projective direction.  The common residue cell
is forced by `a`, `b` and divisibility by `p^s`. ∎

## Exact signature masses

For one owner edge `a`, define `m_{e,sigma}(a)` as the conditional expected
number of eligible selected partners with signature `sigma`.  Explicitly it is

the number of fixed `O` partners in that class plus

\[
\frac1{p_e(a)}
\sum_b\chi_a^M(b)p_e(a,b)
\]

over response partners in the class.

### Theorem CMR1417 -- PROVED

\[
\boxed{
\mathscr C_e^{\rm elig}(a)
\le
\sum_{\sigma=(t,s,\delta,H)}
 c_{n,H}\,m_{e,\sigma}(a),
}
\]

where

\[
c_{n,H}=\max\left\{\left\lfloor\frac{n-1}{H}\right\rfloor-1,0\right\}.
\]

There are at most

\[
\boxed{
2k(p+1)B_n,
\qquad
B_n=1+\lfloor\log_2(n-1)\rfloor,
}
\]

nonempty signature positions for a fixed owner edge.

### Proof

Within the dyadic band `H<=h<2H`, CMR1413 gives
`c_n(h)<=c_{n,H}`.  Sum the exact fixed and conditional partner masses.
There are two partner types, `k` separation depths, `p+1` projective
directions and `B_n` height bands.  The prefix cell is determined by `a` and
`s`, so it contributes no additional class factor. ∎

## Signature concentration

Let

\[
C_n=2k(p+1)B_n.
\]

### Theorem CMR1418 -- PROVED

If

\[
\Gamma_e^{\rm elig}(a)\ge G_0,
\]

then some nonzero signature class satisfies

\[
\boxed{
\frac12 c_{n,H}m_{e,\sigma}(a)
\ge
\frac{G_0}{C_n}.
}
\]

In particular,

\[
\boxed{
 m_{e,\sigma}(a)
\ge
\frac{2G_0}{C_n c_{n,H}}.
}
\]

### Proof

The nonnegative signature contributions in CMR1417 number at most `C_n` and
upper-bound `2 Gamma_e^{elig}(a)`.  Apply pigeonholing to the actual class
sum defining the envelope. ∎

## Simultaneous realization

### Theorem CMR1419 -- PROVED

For every signature `sigma`, some response `R` containing `a` has at least

\[
\boxed{
\left\lceil m_{e,\sigma}(a)\right\rceil
}
\]

eligible selected partners of that signature.

### Proof

The partner count is a nonnegative integer random variable under the bank law
conditioned on `a in R`, with expectation `m_{e,sigma}(a)`.  Its maximum is at
least the ceiling of its expectation. ∎

All of these partners lie in one prefix carry cell relative to `a`, at one
separation depth and one projective direction.

## Real-direction concentration

Let

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2.
\]

### Theorem CMR1420 -- PROVED

The number of canonically oriented primitive integer directions `(u,v)` with

\[
H\le\max(|u|,|v|)<2H
\]

and one fixed projective class `[u:v]` modulo `p` is at most `D_p(H)`.
Consequently, `K` simultaneously selected partners in one signature class
place at least

\[
\boxed{
\left\lceil\frac{K}{D_p(H)}\right\rceil
}
\]

partners on one real line through `a`.

### Proof

Fix a nonzero scalar `lambda in F_p`.  Each coordinate is restricted to one
residue class modulo `p` inside an interval of length less than `4H`, giving at
most `ceil(4H/p)^2` integer vectors.  Sum over the `p-1` nonzero scalars.
Primitivity, canonical orientation and the dyadic annulus only reduce the
count.  A fixed primitive direction through `a` determines one real line. ∎

If the displayed line receives `r` eligible partners, it contributes exactly
`binom(r,2)` triples owned by `a` in that response.

## Eligible-signature endpoint

### Corollary CMR1421 -- PROVED

A large same-owner edge envelope yields, in one actual response:

1. one separation depth;
2. one prefix carry cell;
3. one projective direction;
4. one primitive-height band;
5. at least the partner population from CMR1418--CMR1419;
6. one real line receiving the CMR1420 fraction of that population.

Thus failure of the assignment certificate no longer produces anonymous
low-height mass.  It produces a simultaneous, owner-labelled carry-cell fan or
a quantitatively loaded real line, both in the exact currencies used by the
existing prefix/carry and loaded-line response machinery.  The remaining task
is to compare the resulting execution gain with the parent credit weight and
to close the corresponding same-owner quotient row.  No all-`n` theorem is
claimed.

The eligibility, signature counts, conditional masses and direction bound are
checked in
[`scripts/verify_prime_power_eligible_owner_signature_fans.py`](../scripts/verify_prime_power_eligible_owner_signature_fans.py).
