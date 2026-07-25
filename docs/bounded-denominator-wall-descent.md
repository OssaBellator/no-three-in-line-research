# Effective denominator descent for mixed decoder walls

**Branch:** `research/bounded-denominator-absorbers`

BDA5r measures the prime-power visibility lost by the mixed wall directions

\[
\operatorname{prim}(ha,(h+q)b),
\qquad
\operatorname{prim}((h+q)a,hb).
\]

The losses at different primes assemble into one canonical divisor reduction. Complete prime-power invisibility is not a new unbounded direction: it is exactly cancellation of the common denominator content.

## BDA5t -- canonical wall-denominator descent -- PROVED

Let

\[
g=\gcd(h,q),
\qquad
h=g h_0,
\qquad
q=g q_0.
\]

Then

\[
\gcd(h_0,q_0)=1
\]

and the two mixed primitive directions satisfy

\[
\boxed{
\operatorname{prim}(ha,(h+q)b)
=
\operatorname{prim}(h_0a,(h_0+q_0)b),
}
\]

\[
\boxed{
\operatorname{prim}((h+q)a,hb)
=
\operatorname{prim}((h_0+q_0)a,h_0b).
}
\]

Thus the effective denominator of a mixed wall is

\[
\boxed{
q_0=\frac q{\gcd(h,q)}.
}
\]

If \(g>1\), this is a strict divisor of \(q\). If \(g=q\), then \(q_0=1\) and the wall directions reduce to the denominator-one adjacent forms

\[
\boxed{
\operatorname{prim}(h_0a,(h_0+1)b),
\qquad
\operatorname{prim}((h_0+1)a,h_0b).
}
\]

At every prime \(\ell\mid q_0\), the reduced scale \(h_0\) is an \(\ell\)-adic unit. Hence BDA5r sees the original radial projective class at full \(\ell\)-power precision for the reduced denominator. No second common-content descent remains.

### Proof

Since \(h+q=g(h_0+q_0)\), both coordinates of each raw mixed vector contain the common factor \(g\). Primitive normalization is unchanged after removing a common nonzero factor, proving the two identities.

The definition of \(g\) gives \(\gcd(h_0,q_0)=1\). Therefore no prime dividing \(q_0\) divides \(h_0\), so the BDA5r loss parameter is zero at every prime power of \(q_0\). If \(g>1\), then \(q_0<q\); if \(g=q\), substitution gives the denominator-one formulas. \(\square\)

## Prime-power interpretation

For \(\ell^E\Vert q\), BDA5r removes exactly

\[
\ell^{\min\{E,v_\ell(h)\}}
\]

from the visible denominator precision. Multiplying these losses over all primes gives

\[
\boxed{
\prod_{\ell^E\Vert q}
\ell^{\min\{E,v_\ell(h)\}}
=
\gcd(h,q)=g.
}
\]

The surviving prime-power moduli multiply to \(q_0\). Thus the local valuation charts and the global gcd descent are exactly the same operation.

## Interface to BDA6

A heavy mixed-wall profile now has only two exits.

1. **Proper denominator descent:** \(q_0<q\), so the profile delegates to the absorber track for the strict divisor \(q_0\).
2. **Coprime terminal wall:** \(q_0=q\), equivalently \(\gcd(h,q)=1\), so every prime-power chart has full projective precision and the wall is already in the finite BDA3i atlas.

The extreme case \(q_0=1\) is an explicit adjacent-integer radial geometry rather than an invisible residue state. Consequently mixed wall directions cannot support an infinite same-denominator valuation recursion.

This theorem does not by itself prove induction across all denominators; it supplies the exact strict-divisor or coprime terminal interface required for such an induction.

## Finite check

`scripts/verify_bda_wall_descent.py` exhausts small denominators, scales, and primitive directions. It checks both primitive-vector identities, the product of prime-power losses, strict divisor descent, the coprime terminal condition, and the denominator-one adjacent forms.