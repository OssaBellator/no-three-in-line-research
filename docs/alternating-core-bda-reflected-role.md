# Alternating-core adapter for reflected CD roles

**Branch:** `research/alternating-core-chain`

BDA5aa--BDA5ad prove that the reflected scalar `A(2h+q)` has no denominator-visible cancellation tower. This note imports that result into the alternating-core role dictionary and gives the exact finite-profile, slot, and weighted co-anchor interface for reflected `CD` outputs.

## Reflected BDA records

A reflected alternating-core record carries:

- a denominator `2<=q<=Q`;
- a fixed nonzero role coefficient `A`, usually `wab` or `(u-v)ab`;
- a reflected scalar residue `xi mod q`;
- an integer anchor `P` and positive scale `h`;
- the reflected primitive direction `[a:-b]` and any finite role decorations;
- a nonnegative current paid weight;

with

$$
A(2h+q)\equiv xi\pmod q.
$$

Put

$$
g_A=\gcd(2A,q),
\qquad
m_A=q/g_A.
$$

## AC3dj -- exact reflected denominator profile -- PROVED FROM BDA5aa--BDA5ad

Every reflected record has effective denominator

$$
\boxed{
q_{eff}=q/\gcd(2Ah,q),
}
$$

and, when `q_eff>1`, reduced unit

$$
\boxed{
\frac{2Ah}{\gcd(2Ah,q)}
\pmod{q_{eff}}.
}
$$

This is also the exact reduced profile of `A(2h+q)`. No valuation or cancellation label beyond the denominator exponent is permitted or required.

### Proof

This is BDA5aa--BDA5ab with the coefficient `A`. QED.

## AC3dk -- finite reflected-profile localization -- PROVED

Assume `|A|<=B`. Before adding any optional finite role decoration, the exact reflected arithmetic profile

$$
\pi_{ref}=(q,A,xi)
$$

has at most

$$
\boxed{
L^{ref}_{Q,B}
=
(2B+1)\sum_{q=2}^{Q}q
}
$$

possible values. A reflected paid family of total weight `W` therefore contains one exact profile of weight at least

$$
\boxed{W/L^{ref}_{Q,B}.}
$$

If `q` and `A` are already fixed by the role label, only the `q` residues remain.

### Proof

There are at most `2B+1` integer coefficients and `q` residues for a fixed denominator. Sum over `q`, then apply weighted pigeonhole. QED.

## AC3dl -- canonical reflected scalar slots -- PROVED

Fix one represented profile `(q,A,xi)`. Its scales form exactly one residue class modulo

$$
\boxed{m_A=q/\gcd(2A,q).}
$$

Let `h_0` and `h_max` be the smallest and largest represented scales and write

$$
h_j=h_0+jm_A,
\qquad
0\le j<J.
$$

Aggregate equal anchor/scale records into weights `w_{P,j}`. This preserves the exact total profile weight.

A genuine reflected scale pair `h,h+q` corresponds exactly to a slot-index gap

$$
\boxed{g_A,}
$$

because `q=g_A m_A`.

### Proof

BDA5ac gives the single residue class modulo `m_A`. The slot aggregation is a partition. The index difference between `h` and `h+q` is `q/m_A=g_A`. QED.

## AC3dm -- weighted reflected co-anchor router -- PROVED

Fix an atom cap `beta>0`. Either one reflected anchor-slot atom has weight greater than `beta`, or all atoms are capped. In the capped case put

$$
\Omega^{ref}_{g_A}
=
\sum_P\sum_{j=0}^{J-g_A-1}
\min\{w_{P,j},w_{P,j+g_A}\}.
$$

Then

$$
\boxed{
\Omega^{ref}_{g_A}
\ge
\bigl(2S-\beta|\mathcal A|(J+g_A)\bigr)_+,
}
$$

where `S` is the total profile weight and `mathcal A` is the represented anchor set. One of the two parity classes of `g_A`-step edges is scale-disjoint and carries at least half this overlap.

Consequently a reflected profile returns one of:

1. a heavy exact anchor/scale atom;
2. the explicit dispersed-anchor inequality
   $$
   S<(1/2+epsilon)\beta|\mathcal A|(J+g_A);
   $$
3. a paid co-anchored family of genuine reflected pairs `h,h+q` carrying at least
   $$
   \boxed{
   epsilon\beta|\mathcal A|(J+g_A)
   }
   $$
   in one scale-disjoint parity class.

### Proof

The weighted overlap and parity argument of BDA5z is purely the combinatorics of `g`-step edges on interlaced scalar paths. AC3dl supplies the identical structure with `g=g_A`. Substitution gives the bound and the three alternatives. QED.

## Support-faithfulness gate

AC3dm proves paid scalar-pair extraction, not the geometric decoder for a reflected pair. To call outcome 3 executable, the actual alternating role must still prove:

1. the two occurrences at `h` and `h+q` have the claimed common anchor and reflected `CD` support;
2. their full row/column and potential-term conflicts are included in the AC3v conflict graph;
3. one of the BDA rectangle, carry, or descent decoders applies to the reflected pair.

Failure of this gate is an explicit reflected-support profile, not a cancellation-height profile.

## Consequence

The alternating role dictionary no longer needs a special `v_l(2h+q)>E` state. Reflected `CD` outputs use the same finite architecture as the ordinary scalar route:

- finite exact profile;
- one scalar residue class;
- genuine `h,h+q` pair extraction;
- heavy atom, dispersed anchors, or a paid support-audit family.

## Finite check

`scripts/verify_ac_bda_reflected_role.py` checks the finite profile count, reflected congruence slots, exact `g_A` index gap, weighted overlap bound, parity disjointness, and the composition loss after profile localization.