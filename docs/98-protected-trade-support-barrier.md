# Protected direction families force large trade support

PX175 proves that polynomial rectangle-codegree saving requires polynomially
many protected directions.  A possible response would be to retain a local
switching or absorber method inside the simultaneous-rainbow state space.  This
chapter shows that no bounded-support switching can do so.

The result is purely algebraic.  A trade preserving \(s\) distinct linear
colourings must move more than \(s\) rows.

Let \(X=\{x_1,\ldots,x_k\}\subset\mathbb F_p\) be a set of distinct rows, with
\(k<p\).  Suppose two partial matchings use image vectors

\[
y=(y_1,\ldots,y_k),
\qquad
z=(z_1,\ldots,z_k).
\]

Outside \(X\), the two complete matchings are assumed identical.  For one
slope \(c\in\mathbb F_p\), preserving the corresponding linear colouring means

\[
\boxed{
\{y_i-cx_i:i\in[k]\}
=
\{z_i-cx_i:i\in[k]\}
}
\]

as multisets.

## Theorem PX181 -- PROVED

If the displayed multiset identity holds for at least \(k\) distinct slopes
\(c\), then

\[
\boxed{y_i=z_i\quad\text{for every }i.}
\]

Equivalently, every nontrivial trade on \(k<p\) rows preserves at most \(k-1\)
distinct linear colourings.

Thus a nontrivial trade preserving a family \(S\) of slopes must have support

\[
\boxed{k\ge |S|+1.}
\]

### Proof

For every positive integer \(j\le k\), equality of the two colour multisets
gives equality of their \(j\)-th power sums:

\[
\sum_{i=1}^k(y_i-cx_i)^j
=
\sum_{i=1}^k(z_i-cx_i)^j.
\]

Move the right side to the left and regard the result as a polynomial
\(P_j(c)\).  The leading \(c^j\) terms cancel because the row set is the same on
both sides, so

\[
\deg P_j\le j-1.
\]

The polynomial vanishes at every protected slope.  There are at least
\(k\ge j\) such slopes, so \(P_j\) is identically zero.

The coefficient of \(c^{j-1}\) is

\[
j(-1)^{j-1}
\sum_{i=1}^k x_i^{j-1}(y_i-z_i).
\]

Because \(j<p\), its scalar coefficient is nonzero.  Hence for
\(j=1,\ldots,k\),

\[
\sum_{i=1}^k x_i^{j-1}(y_i-z_i)=0.
\]

These are the \(k\) equations of the Vandermonde matrix

\[
\bigl(x_i^{j-1}\bigr)_{j,i=1}^k.
\]

The rows \(x_i\) are distinct, so the matrix is invertible and
\(y_i-z_i=0\) for every \(i\). \(\square\)

## Sharpness at the strong-complete base

The support-four trade PX98 preserves exactly the three fundamental slope
colourings

\[
c=0,
\qquad c=1,
\qquad c=-1.
\]

Thus the bound is sharp for

\[
(k,|S|)=(4,3).
\]

This also explains algebraically why no nontrivial strong-complete trade can
move fewer than four rows, complementing PX102.

## Theorem PX182 -- PROVED

Suppose a simultaneous-rainbow state protects every primitive direction through
height \(H\).  The corresponding set of distinct field slopes has size

\[
|S_H|=\Omega(H^2)
\]

whenever \(H^2=o(p)\).  Therefore every nontrivial trade which stays inside the
fully protected state space has support

\[
\boxed{k=\Omega(H^2).}
\]

In particular, if

\[
H=p^\delta,
\]

then every protected trade has support

\[
\boxed{k=\Omega(p^{2\delta}).}
\]

### Proof

The number of reduced fractions \(b/a\) with

\[
1\le a,b\le H
\]

is \(\Omega(H^2)\).  When \(H^2=o(p)\), distinct reduced rational fractions in
this range remain distinct modulo \(p\).  Each such slope is one of the linear
colourings imposed by direction protection.  Apply PX181. \(\square\)

## 3. Consequences for the remaining proof routes

PX181--PX182 close another tempting shortcut.

1. **Bounded local switches cannot handle PX175.**  Polynomially many protected
   directions force polynomially large switch support.
2. **Fixed-size absorber banks cannot remain fully protected.**  Any absorber
   which changes only \(O(1)\) rows becomes trivial once the number of protected
   slopes exceeds its support.
3. **Growing uniformity is not an artefact of one encoding.**  Even if the
   direction constraints are represented as colours or conflicts rather than
   separate host parts, every exact local move must still see all of them and
   therefore has growing support.
4. **A viable protected process must be global.**  It must use a nibble,
   entropy-completion argument, or a switching flow whose individual paths move
   at least \(\Omega(H^2)\) rows.

The theorem does not rule out a global distribution on protected matchings.
It says that the fixed-support PX98 switching technology cannot be the primary
mixing mechanism once the direction family grows polynomially.

This strengthens the current frontier after PX175.  The direct protected route
now requires both:

- a growing-direction existence/spread theorem; and
- global moves of scale comparable to the number of protected slopes.

The low-syndrome repair route remains qualitatively different because it need
not preserve every low direction during each local move.

## Verification

Run

```bash
python scripts/verify_product_protected_trade_support_barrier.py
```

The verifier exhausts nontrivial trades of support at most four over
\(\mathbb F_7\), checks random larger supports, and verifies that PX98 attains
the sharp support-four/three-slope case.
