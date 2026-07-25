# Prime-power collapse of radial decoder channels

**Branch:** `research/bounded-denominator-absorbers`

BDA5o--BDA5p identify the primitive directions and signed affine offsets of every rank-one radial-decoder channel. This note applies the BDA3h valuation charts to those formulas. The main point is that the four one-cell channel words do not create four unrelated denominator profiles: modulo the fixed denominator they all reduce to one determinant scalar.

## Channel determinant formulas

Retain

\[
d=(a,b),\qquad H=h+q,
\]

and let the primitive context direction be

\[
e=(r,s).
\]

Put

\[
\delta=\det(d,e)=as-br.
\]

For the four one-cell channel vectors

\[
z_A=(ha,hb),\quad z_B=(Ha,Hb),\quad
z_C=(ha,Hb),\quad z_D=(Ha,hb),
\]

direct expansion gives

\[
\begin{aligned}
\det(z_A,e)&=h\delta,\\
\det(z_B,e)&=h\delta+q\delta,\\
\det(z_C,e)&=h\delta-qbr,\\
\det(z_D,e)&=h\delta+qas.
\end{aligned}
\]

## BDA5q -- denominator-channel collapse -- PROVED

For every primitive context direction \(e\),

\[
\boxed{
\det(z_A,e)\equiv
\det(z_B,e)\equiv
\det(z_C,e)\equiv
\det(z_D,e)
\equiv h\det(d,e)\pmod q.
}
\]

Consequently, in a role-\(w\) one-cell channel the BDA5o signed offset

\[
O_{w,z}(e)=w\det(z,e)
\]

satisfies

\[
\boxed{
O_{w,z}(e)\equiv wh\det(d,e)\pmod q,
}
\]

independently of the channel word \(A,B,C,D\).

### Prime-power visible precision

Fix a prime power

\[
\ell^E\Vert q
\]

and assume the channel is non-wall, so \(\delta\ne0\). Put

\[
\lambda_\ell=\min\{E,v_\ell(h\delta)\}.
\]

If \(\lambda_\ell<E\), then every one-cell channel determinant has the same exact valuation

\[
\boxed{
v_\ell(\det(z,e))=\lambda_\ell,
}
\]

and after division by the visible common power,

\[
\boxed{
\frac{\det(z,e)}{\ell^{\lambda_\ell}}
\equiv
\frac{h\delta}{\ell^{\lambda_\ell}}
\pmod{\ell^{E-\lambda_\ell}}.
}
\]

If \(\lambda_\ell=E\), all four determinants vanish modulo \(\ell^E\). Thus the only loss of prime-power visibility is the scalar valuation of \(h\det(d,e)\); no extra channel-dependent valuation state is needed.

### Proof

The four exact formulas differ from \(h\delta\) by multiples of \(q\), proving the congruence. If \(v_\ell(h\delta)<E\), adding a term divisible by \(\ell^E\) cannot change the valuation or the normalized residue modulo \(\ell^{E-\lambda_\ell}\). If \(v_\ell(h\delta)\ge E\), both the base term and all corrections vanish modulo \(\ell^E\). \(\square\)

## BDA5r -- wall-direction precision -- PROVED

The two mixed wall directions are

\[
e_C=\operatorname{prim}(ha,Hb),
\qquad
e_D=\operatorname{prim}(Ha,hb).
\]

For \(\ell^E\Vert q\), put

\[
k_\ell=\min\{E,v_\ell(h)\}.
\]

If \(k_\ell<E\), both wall directions retain the original radial projective class at the exact remaining precision:

\[
\boxed{
[e_C]=[e_D]=[a:b]
\quad\text{in}\quad
\mathbb P^1(\mathbb Z/\ell^{E-k_\ell}\mathbb Z).
}
\]

If \(k_\ell=E\), the raw vectors \((ha,Hb)\) and \((Ha,hb)\) are zero modulo \(\ell^E\). Their primitive directions then depend on higher integer lifts and are invisible to the denominator residue profile.

### Proof

Suppose \(k_\ell<E\). Since \(H=h+q\),

\[
v_\ell(H)=v_\ell(h)=k_\ell.
\]

Primitivity of \((a,b)\) gives

\[
\min\{v_\ell(a),v_\ell(b)\}=0.
\]

Hence the common \(\ell\)-adic valuation removed when primitive-normalizing either mixed vector is exactly \(k_\ell\). After division by \(\ell^{k_\ell}\), the two coefficients \(h/\ell^{k_\ell}\) and \(H/\ell^{k_\ell}\) are congruent modulo \(\ell^{E-k_\ell}\) and are units there. Any remaining integer gcd contributes only a unit scalar. Both normalized vectors therefore represent \([a:b]\) at that precision.

When \(k_\ell=E\), every raw coordinate is divisible by \(\ell^E\), proving the invisible alternative. \(\square\)

Thus the \(C\)- and \(D\)-wall directions introduce no new projective slope state before the exact \(h\)-content is exhausted. They are the original radial direction viewed through a finite valuation loss.

## BDA5s -- reflected-line offset valuation -- PROVED

For the two-local \(CD\) channel, BDA5o gives primitive direction \((a,-b)\) and signed role offset

\[
O_{CD}(w)=wab(2h+q).
\]

For every prime \(\ell\),

\[
\boxed{
v_\ell(O_{CD}(w))
=
v_\ell(wab)+v_\ell(2h+q).
}
\]

If \(\ell^E\Vert q\) and \(v_\ell(2h)\ne E\), then

\[
\boxed{
v_\ell(2h+q)=\min\{v_\ell(2h),E\}.
}
\]

If \(v_\ell(2h)=E\), then

\[
v_\ell(2h+q)\ge E,
\]

and any further loss is one explicit cancellation height. The separation between the role-\(u\) and role-\(v\) lines has the same scalar form:

\[
O_{CD}(u)-O_{CD}(v)
=(u-v)ab(2h+q).
\]

### Proof

The first identity is multiplicativity of the integer valuation. The two summands \(2h\) and \(q\) have unequal valuations unless \(v_\ell(2h)=E\); in the unequal case the valuation of their sum is the smaller one. In the equal case cancellation may only increase the common valuation. The role-separation formula is immediate. \(\square\)

## Interface to BDA6

The BDA5n balanced-floor output now enters the prime-power charts through only three types of data.

1. **Non-wall one-cell channel.** Record the primitive classes \([d]\) and \([e]\), the visible valuation
   \[
   \min\{E,v_\ell(h\det(d,e))\},
   \]
   and its normalized unit residue. The local channel word adds no prime-power state.
2. **Mixed wall channel.** Record the \(h\)-content loss \(k_\ell\). Before complete invisibility, both mixed directions are the original radial class at precision \(E-k_\ell\).
3. **Reflected \(CD\) channel.** Record the reflected class \([a:-b]\) and the single scalar valuation/cancellation profile of \(wab(2h+q)\).

The \(AB\) channel remains the original zero-offset radial line. Therefore the arithmetic frontier is no longer a comparison among four unrelated decoder directions. It is a finite projective atlas plus the already named common-content and scalar-cancellation towers.

## Finite check

`scripts/verify_bda_role_valuation_collapse.py` exhausts small prime powers, primitive radial and context directions, channel vectors, role scalars, and wall normalizations. It checks all exact determinant formulas, the common modulo-\(q\) residue, visible valuation equality, normalized prime-power residues, mixed-wall projective precision, and the reflected-line valuation alternatives.