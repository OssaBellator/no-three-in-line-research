# Aligned-anchor carry cells

This chapter exploits the Euclidean carry filter inside the aligned-anchor alternative of the common-ratio conversion theorem. It proves that a large aligned-anchor multiplicity must come from either many distinct carry signatures or an explicit perfect-interpolation carry cell.

Throughout, `p` is an odd prime. All nonzero field elements are represented by integers in `{1,...,p-1}`.

Fix

\[
a,g,\lambda\in\mathbb F_p^*,
\qquad g\ne1,
\]

and write

\[
h=\langle g^{-1}\rangle_p,
\qquad
m=\langle \lambda g^{-1}\rangle_p.
\]

For a base parameter `x`, put

\[
y=\langle a/x\rangle_p.
\]

The three aligned points are

\[
U_x=(x,\langle hy\rangle_p)\in H_{a/g},
\]

\[
V_x=(\langle gx\rangle_p,y)\in H_{ag},
\]

and

\[
W_x=(\langle\lambda x\rangle_p,\langle my\rangle_p)
\in H_{a\lambda^2/g}.
\]

Thus `U_x,V_x,W_x` are exactly the switched pair and its modularly aligned opposite-channel anchor.

## 1. Coordinate and scalar carries

Define coordinate carries

\[
A=\left\lfloor\frac{gx}{p}\right\rfloor,
\qquad
D=\left\lfloor\frac{\lambda x}{p}\right\rfloor,
\]

\[
B=\left\lfloor\frac{hy}{p}\right\rfloor,
\qquad
C=\left\lfloor\frac{my}{p}\right\rfloor.
\]

Then

\[
\langle gx\rangle_p=gx-pA,
\quad
\langle\lambda x\rangle_p=\lambda x-pD,
\]

\[
\langle hy\rangle_p=hy-pB,
\quad
\langle my\rangle_p=my-pC.
\]

Define scalar carries

\[
\mu=\frac{gh-1}{p},
\qquad
\nu=\frac{gm-\lambda}{p},
\qquad
\rho=\frac{h\lambda-m}{p}.
\]

All of these quantities are integers.

Put

\[
\eta=-\mu+\nu+\rho,
\]

\[
\alpha=B(g-\lambda)+C(1-g),
\]

\[
\beta=A(h-m)+D(1-h),
\]

and

\[
\gamma=-AB+AC+BD.
\]

### Theorem CA1 — PROVED

The exact real determinant is

\[
\boxed{
\det(U_x,V_x,W_x)
=
p\bigl(\eta xy+\alpha x+\beta y+p\gamma\bigr).
}
\]

Consequently, the aligned modular triple is a genuine real collinearity if and only if

\[
\boxed{
\eta xy+\alpha x+\beta y+p\gamma=0.
}
\]

### Proof

Substitute

\[
U_x=(x,hy-pB),
\]

\[
V_x=(gx-pA,y),
\]

and

\[
W_x=(\lambda x-pD,my-pC)
\]

into the affine determinant. The coefficient of `xy` before using the scalar carry identities is

\[
-gh+gm+h\lambda-\lambda-m+1.
\]

Using

\[
gh=1+p\mu,
\quad gm=\lambda+p\nu,
\quad h\lambda=m+p\rho
\]

turns this coefficient into `p eta`. Collecting the remaining terms gives the displayed formula. \(\square\)

## 2. Factorisation inside one carry signature

A **carry signature** is a quadruple

\[
\sigma=(A,B,C,D).
\]

For fixed `g,lambda`, the values `eta,alpha,beta,gamma` are fixed on every signature.

### Theorem CA2 — PROVED

Suppose a carry signature is nondegenerate, meaning

\[
(\eta,\alpha,\beta,\gamma)\ne(0,0,0,0).
\]

Then the number of base points `(x,y) in H_a` in that signature for which `U_x,V_x,W_x` are real-collinear is at most

\[
\mathfrak d(p)
=
2+2\max_{1\le n\le16p^4}\tau(n),
\]

where `tau` is the divisor function. In particular,

\[
\boxed{\mathfrak d(p)=p^{o(1)}.}
\]

### Proof

If `eta != 0`, the carry equation factors as

\[
\boxed{
(\eta x+\beta)(\eta y+\alpha)
=
\alpha\beta-\eta p\gamma.
}
\]

If the right side is nonzero, each signed divisor determines at most one integer pair `(x,y)`, giving at most `2 tau(|N|)` solutions. If it is zero, one of the two factors vanishes, giving at most two solutions.

If `eta=0`, the carry equation is the real line

\[
\alpha x+\beta y+p\gamma=0.
\]

When `(alpha,beta) != (0,0)`, the monochromatic line cap for `H_a` gives at most two points. When `alpha=beta=0`, nondegeneracy forces `gamma != 0`, so there is no solution.

The carry bounds imply

\[
|\eta|<3p,
\quad |\alpha|,|\beta|<2p^2,
\quad |\gamma|<3p^2,
\]

and hence

\[
|\alpha\beta-\eta p\gamma|<16p^4.
\]

The classical divisor bound gives the final asymptotic statement. \(\square\)

## 3. Perfect affine carry alignment

Define interpolation residuals

\[
R_x=(\lambda-1)A-(g-1)D
\]

and

\[
R_y=\eta y+(g-\lambda)B-(g-1)C.
\]

### Theorem CA3 — PROVED

The residuals satisfy

\[
(g-1)W_{x,1}
-(g-\lambda)U_{x,1}
-(\lambda-1)V_{x,1}
=
pR_x,
\]

and

\[
(g-1)W_{x,2}
-(g-\lambda)U_{x,2}
-(\lambda-1)V_{x,2}
=
pR_y.
\]

Therefore

\[
\boxed{R_x=R_y=0}
\]

means that `W_x` lies at the exact real affine parameter

\[
t=\frac{\lambda-1}{g-1}
\]

on the line through `U_x,V_x`. Such a point is automatically a genuine aligned-anchor collinearity.

Every degenerate carry signature is perfectly aligned: if

\[
\eta=\alpha=\beta=\gamma=0,
\]

then every point realising that signature satisfies `R_x=R_y=0`.

### Proof

The two displayed identities follow by expanding the represented coordinates. For the second coordinate, the scalar discrepancy is

\[
(g-1)m-(g-\lambda)h-(\lambda-1)
=
p\eta.
\]

For the final assertion, `eta=alpha=0` gives `R_y=0`. Also

\[
(g-1)\frac{\det(U_x,V_x,W_x)}p
=
\bigl((g-1)x-pA\bigr)R_y
-
\bigl((1-h)y+pB\bigr)R_x.
\]

The determinant vanishes on a degenerate signature. The factor

\[
(1-h)y+pB
=
y-\langle hy\rangle_p
\]

is nonzero because `h != 1`. Hence `R_x=0`. \(\square\)

### Carry-slab classification

Let

\[
d=\gcd(g-1,\lambda-1).
\]

The equation `R_x=0` is equivalent to

\[
A=\frac{g-1}{d}t,
\qquad
D=\frac{\lambda-1}{d}t
\]

for an integer

\[
0\le t\le d.
\]

Thus perfect alignment can occur only in at most `d+1` source-coordinate carry slabs. The remaining condition `R_y=0` cuts these slabs by an explicit target-coordinate carry equation.

## 4. Aligned-anchor multiplicity dichotomy

Let `X` be a set of base parameters. Let

\[
\Lambda_{g,\lambda}(X)
=
|\{x\in X:\det(U_x,V_x,W_x)=0\}|.
\]

Let `s_nd` be the number of nondegenerate carry signatures realised by points of `X`, and let `E_deg` be the number of points of `X` lying in degenerate signatures.

### Theorem CA4 — PROVED

\[
\boxed{
\Lambda_{g,\lambda}(X)
\le
\mathfrak d(p)s_{nd}+E_{deg}.
}
\]

Consequently, a large aligned-anchor class has one of two explicit explanations:

1. **carry dispersion:** it occupies many distinct nondegenerate carry signatures;
2. **perfect carry alignment:** a large subset lies in degenerate signatures and is exactly affine-interpolated between the switched endpoints.

### Proof

Apply Theorem CA2 separately to every nondegenerate signature and sum. Theorem CA3 identifies every remaining degenerate-signature point as perfectly aligned. \(\square\)

## 5. Integration with the alternating closure inequality

The aligned-anchor obstruction `Lambda` in the weighted conversion theorem is no longer anonymous. For each channel/root signature `(b,lambda)`, Theorem CA4 gives

\[
\Lambda
\le
p^{o(1)}\times
(\text{number of nondegenerate carry signatures})
+
(\text{perfect-alignment mass}).
\]

Thus the aligned branch of alternating closure reduces to two narrower targets:

- prove that carry-signature complexity grows under repeated red/blue propagation; or
- classify and absorb the perfect-interpolation carry slabs.

The remaining unquantified part of the closure inequality is the secant-star load `Theta`. The conic-pencil theorem gives its modular baseline, while the next step must obtain an analogous carry-cell decomposition for pairs of outside channels through one inserted candidate point.

The checker

```bash
python scripts/verify_aligned_carry.py --prime 17
```

verifies the exact determinant, factorisation, and interpolation identities exhaustively for a chosen odd prime. It is a finite sanity check, not a proof for arbitrary `p`.
