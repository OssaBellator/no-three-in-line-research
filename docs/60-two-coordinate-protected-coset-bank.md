# Two-coordinate protected affine-coset bank

PX89 varies only one translation parameter in each additive coset.  PX91 shows
that this measure has far too much accumulated local certificate mass.  This
chapter adds independent affine freedom to both rectangle coordinates while
preserving every protected line capacity.

The result is the first factor-compatible protected bank with separate local row
and column slopes.

Let `K` be the additive subgroup of `Z_n` of order `h`, and put `q=n/h`.  Use the
canonical coset representatives `c in {0,...,q-1}`, so every element of the
coset `C_c` has a unique form

\[
u=c+x,
\qquad x\in K.
\]

Fix a unit `m modulo n` and a finite set `D` of nonaxis primitive directions
`(a,b)` satisfying

\[
\gcd(b-am,n)=1.
\]

For each coset `C_c`, choose:

- a row slope `A_c` which is a unit modulo `h`;
- a column slope `G_c` which is a unit modulo `h`;
- shifts `sigma_c,delta_c in K`.

Define two coset-preserving permutations by

\[
P(c+x)=c+A_cx+\sigma_c,
\]

\[
\Phi(c+x)=c+G_cx+\delta_c.
\]

All operations on `x in K` are taken in the cyclic group `K`.  Finally put

\[
t(u)=r(u)=m\Phi(u)+c_0\pmod n
\]

for an arbitrary global column shift `c_0`, and take the rectangle state

\[
Q(P,t,r).
\]

## Theorem PX92 -- PROVED

Suppose that for every coset `C_c` and every protected direction `(a,b) in D`,

\[
\gcd(b-amG_c,h)=1
\]

and

\[
\gcd(bA_c-amG_c,h)=1.
\]

Then the resulting rectangle state has all of the following properties.

1. It is saturated, with exactly two points in every scalar row and column.
2. Every real line in a direction from `D` contains at most two selected points.
3. The four parameters of each coset may be chosen independently subject only to
   the displayed local unit conditions.
4. Changing one coset state affects only its `h` rectangles.
5. Every normalized state transports to every saturated side-`n` factor.

### Proof

The local row map `x -> A_cx+sigma_c` and local column map
`x -> G_cx+delta_c` are permutations of `K`.  Since each preserves its coset,
`P` and `Phi` are permutations of `Z_n`.  Multiplication by the unit `m` and
addition of `c_0` make `t=r` permutations, so PX43 gives saturation.

Fix a direction `(a,b)`.  For a top corner of type `(0,0)`, reduction of its
integer line coordinate modulo `n` gives, for `u=c+x`,

\[
\lambda(u,t(u))
\equiv
(b-am)c+(b-amG_c)x-am\delta_c-ac_0
\pmod n.
\]

Inside one coset, the coefficient `b-amG_c` is a unit on `K`, so the residues
are distinct.  Across different cosets, their images modulo `K` are obtained by
multiplication by `b-am`; the global gcd hypothesis makes this a permutation of
the quotient.  Thus the complete top type is injective on real lines.  The
second top corner uses the same residue map because `r=t`, and its exact line
coordinate differs by the nonzero integer `-an`.  Hence all `2n` top corners
occupy distinct real lines of the protected direction.

For a bottom corner, the variable part of the line coordinate inside `C_c` is

\[
(bA_c-amG_c)x.
\]

The second local unit condition gives injectivity inside the coset, while the
quotient map is again multiplication by `b-am`.  The two bottom corner types
differ by `-an`, so all `2n` bottom corners also occupy distinct real protected
lines.

Every protected line therefore contains at most one top and at most one bottom
point.  The independence, support, and factor-transport assertions follow from
the cosetwise definitions and PX41. \(\square\)

## 2. State count for prime-order cosets

Let `h=ell` be prime and let `M_ell(D,m)` be the set of slope pairs

\[
(A,G)\in(\mathbb F_\ell^*)^2
\]

satisfying the two local unit conditions for all directions in `D`.

### Theorem PX93 -- PROVED

If

\[
ell>|D|+1,
\]

then

\[
\boxed{
|M_\ell(D,m)|
\ge
(\ell-1-|D|)^2.
}
\]

Consequently the protected two-coordinate bank contains at least

\[
\boxed{
\left[
\ell^2(\ell-1-|D|)^2
\right]^{n/\ell}
}
\]

global states.

### Proof

Choose `G` first.  For one direction, the equation

\[
b-amG=0\pmod\ell
\]

forbids at most one nonzero value of `G`.  Hence at least
`ell-1-|D|` column slopes remain.

After fixing an admissible `G`, the equation

\[
bA-amG=0\pmod\ell
\]

forbids at most one nonzero value of `A` for each direction.  Thus at least
`ell-1-|D|` row slopes remain.  Multiply the two lower bounds.  Each admissible
slope pair has `ell^2` independent choices of the two shifts, and the `n/ell`
cosets choose independently. \(\square\)

## 3. The first protected example

For

\[
n=25,
\qquad
\ell=5,
\qquad
m=2,
\]

and the two diagonal directions `(1,1)` and `(1,-1)`, the admissible local slope
pairs are exactly

\[
(1,1),
(1,4),
(4,1),
(4,4).
\]

Each of the five cosets therefore has

\[
5^2\cdot4=100
\]

protected local states, rather than the five translation states of PX89.  The
complete bank has `100^5` states.

This is still not asserted to contain a no-three state.  Deterministic sampling
shows substantially smaller residual syndromes than the translation-only bank,
but no asymptotic concentration theorem has yet been proved.

## 4. Revised protected-spread target

PX92 supplies the geometry required by the missing two-coordinate protected
spread theorem.  The remaining probabilistic task is now internal to the slope
and shift variables:

1. prove fixed-rank cylinder bounds for the induced permutations `P,t,r`;
2. bound one-, two-, and three-coset collinearity certificate loads;
3. combine the bounds with PX82 after choosing a height cutoff;
4. apply a local lemma, resampling theorem, or conflict-free matching theorem.

Unlike the translation-only bank, the row and column labels now move
independently.  Prime-order cosets also have quadratically many admissible slope
pairs when `ell` is large relative to the protected direction set.

## 5. Verification

Run

```bash
python scripts/verify_product_two_coordinate_coset_bank.py
```

The verifier checks the exact admissible slope sets, exhausts every local state
in the `Z_25` example one coset at a time, verifies random global states on
larger moduli, and checks saturation and every protected real-line capacity.