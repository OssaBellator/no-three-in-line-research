# Protected coset absorbers inside the rectangle product family

PX75--PX77 construct factor-compatible rectangle states which avoid every
prescribed low-height direction.  A single protected state is not enough for a
repair theorem; one also needs many independent states which preserve the
protected constraints.  This chapter installs such a bank on composite moduli.

Let `K` be an additive subgroup of `Z_n` of order `h`.  Its `n/h` cosets
partition the fine-row labels.  For each coset `C`, choose a shift

\[
\delta_C\in K.
\]

Define the cosetwise permutation

\[
\phi_\delta(u)=u+\delta_C
\qquad (u\in C).
\]

Every coset is translated inside itself, so `phi_delta` is a permutation of
`Z_n`.

Fix affine parameters `m,c,s` from PX75 and put

\[
p_s(u)=u+s,
\]

\[
t_\delta(u)=r_\delta(u)
=m\phi_\delta(u)+c\pmod n.
\]

Let

\[
Q_\delta=Q(p_s,t_\delta,r_\delta)
\]

be the resulting rectangle state.

## Theorem PX78 -- PROVED

Let `D` be a finite set of nonaxis primitive directions and suppose

\[
\gcd(m,n)=1,
\qquad
\gcd(b-am,n)=1
\quad((a,b)\in D).
\]

Then every choice of the independent coset shifts `(delta_C)` has all of the
following properties.

1. `Q_delta` is a saturated rectangle state of `4n` points in `[2n]^2`.
2. Every real line in a direction from `D` contains at most two selected points.
3. Changing one coset shift affects only the `h` rectangles indexed by that
   coset and preserves all row and column degrees.
4. The cosets provide exactly

   \[
   h^{n/h}
   \]

   global protected states.
5. Every state is factor-compatible with every saturated side-`n` factor by
   full-symmetric rectangle transport.

### Proof

Because each coset is translated inside itself, `phi_delta` is a permutation.
Multiplication by the unit `m` and addition of `c` show that `t_delta=r_delta`
is also a permutation.  Together with the translation permutation `p_s`, PX43
gives saturation.

Fix `q=(a,b) in D`.  For a top corner of type `(0,0)`, reduction of the line
coordinate modulo `n` gives

\[
\lambda_q(u,t_\delta(u))
\equiv
(b-am)u-am\delta_C-ac
\pmod n,
\qquad u\in C.
\]

Inside one coset, multiplication by the unit `b-am` is a bijection on `K`, and
the extra term `-am delta_C` is a translation by an element of `K`.  Hence the
set of line-coordinate residues contributed by `C` is unchanged from the
affine state `delta_C=0`.

Distinct domain cosets have distinct image cosets because multiplication by the
unit `b-am` permutes the cosets of `K`.  Therefore the complete line-coordinate
map remains a permutation of `Z_n`.  The second top corner differs by the
nonzero integer `-an`, so the exact real line coordinates of all `2n` top
corners remain distinct.  The identical argument applies to the bottom colour;
the row shift `s` contributes only a constant on each formula.  Thus every
protected line has at most one top and one bottom point.

A shift at one coset changes only `t_delta(u)=r_delta(u)` for `u` in that coset,
so only its `h` rectangles move.  Since the new maps remain permutations, all
row and column degrees stay two.  The `n/h` cosets choose their shifts
independently from `h` values, giving `h^(n/h)` states.  PX41 transports every
normalized rectangle state to every factor layer. \(\square\)

## Corollary PX78a -- PROVED

Under the rough-modulus hypothesis of PX77, every additive subgroup of order
`h` installs `n/h` independent `h`-state absorbers while preserving all
primitive directions of height at most `H`.

In particular, after choosing `H` so that

\[
2H(H+1)+1
\]

is below the least prime factor of `n`, all remaining defects have primitive
height greater than `H`, and every remaining compatible-pair transversal
codegree has the PX71 bound

\[
64n^2\left(1+rac{2n}{H}\right).
\]

## 2. What this adds to the general route

The protected low-direction state from PX77 is no longer isolated.  Composite
rough moduli now support an exponential family of factor-compatible states with
independent local coordinates and a polynomial high-direction codegree saving.

The next concentration problem is explicit:

> choose the coset shifts so that every high-direction bad line is avoided,
> while using only the divisor- and height-sensitive overlap bounds among the
> affected cosets.

A local-lemma or resampling proof in this shift space would give exact product
doubling for a new infinite class of rough composite moduli.  Prime moduli still
lack nontrivial additive cosets and require a different entropy source.

## 3. Verification

Run

```bash
python scripts/verify_product_protected_coset_absorbers.py
```

The verifier exhausts the `5^5` protected states for the order-five subgroup of
`Z_25`, checks random larger subgroup banks, and verifies saturation and every
protected real-line occupancy.