# Quotient boundary for rational collision saturation

The collision involution from RI0 turns the large-index part of RI2 into
an exact cut problem on the subgroup quotient.  This identifies the
structured object that must be classified when the universal half-image
bound is nearly sharp.

Fix \(r\in\mathbb F_p^\times\setminus\{1\}\) and write

\[
D_r=\mathbb F_p^\times\setminus\{1,r\},
\qquad
\tau_r(x)=\frac{r(x-1)}{x-r}.
\]

The map \(\tau_r\) is an involution of \(D_r\), and its orbits are the
fibres of \(F_r\).  Let \(H\leq\mathbb F_p^\times\), and list all
multiplicative cosets as

\[
\mathbb F_p^\times=H_0\sqcup\cdots\sqcup H_{m-1}.
\]

Define the collision quotient matrix

\[
J_{ij}
=
\bigl|\{x\in H_i\cap D_r:\tau_r(x)\in H_j\}\bigr|.
\]

## RI2f -- collision quotient boundary identity

### Theorem RI2f -- PROVED

The matrix \(J\) is symmetric and has exact row sums

\[
\boxed{
J_{ij}=J_{ji},
\qquad
\sum_jJ_{ij}=|H_i\cap D_r|.
}
\]

For a set \(S\subseteq\{0,\ldots,m-1\}\), put

\[
D_S=D_r\cap\bigcup_{i\in S}H_i.
\]

Let

- \(P_S\) be the number of nonfixed two-point \(\tau_r\)-orbits wholly
  contained in \(D_S\);
- \(f_S\) be the number of fixed points of \(\tau_r\) in \(D_S\); and
- \(B(S)\) be the directed cut weight
  \[
  B(S)=\sum_{\substack{i\in S\\j\notin S}}J_{ij}
  =|\{x\in D_S:\tau_r(x)\notin D_S\}|.
  \]

Then

\[
\boxed{
|D_S|=2P_S+f_S+B(S)
}
\]

and

\[
\boxed{
|F_r(D_S)|=P_S+f_S+B(S).
}
\]

Equivalently, the exact excess above the half-image bound is

\[
\boxed{
2|F_r(D_S)|-|D_S|=f_S+B(S).
}
\]

### Proof

The involution maps the set counted by \(J_{ij}\) bijectively to the set
counted by \(J_{ji}\), proving symmetry.  Every point of
\(H_i\cap D_r\) has one \(\tau_r\)-image in exactly one quotient coset,
which proves the row sum.

Partition \(D_S\) by its full \(\tau_r\)-orbit.  An internal nonfixed
orbit contributes two points, a fixed orbit contributes one, and a
crossing orbit contributes exactly its one endpoint in \(D_S\).  This
gives the first identity.

The fibres of \(F_r\) are precisely the \(\tau_r\)-orbits.  Each
internal pair therefore contributes one image, each fixed point one
image, and each crossing endpoint one image.  Two distinct crossing
endpoints in \(D_S\) cannot have the same image, since they would then
be involution partners and form an internal pair.  This proves the
second identity; subtraction gives the final box. \(\square\)

## Structural consequence

If

\[
|F_r(D_S)|\leq\frac{|D_S|}{2}+L,
\]

then

\[
\boxed{
B(S)+f_S\leq2L.
}
\]

Thus collision saturation is exactly a low-boundary union of quotient
vertices, up to the at most two fixed points of the Möbius involution.
The genuinely large-index RI2 problem may therefore be phrased as
expansion or classification of low-conductance cuts in the explicit
symmetric integer matrix \(J\).  A component with zero boundary is a
union of complete \(\tau_r\)-orbits and is the precise finite
coset-chain object to pass to RI3--RI5.

This theorem does not prove that every nonexceptional quotient cut has
large boundary.  It replaces the informal exceptional-chain target by
an exact weighted quotient graph and an equality whose deficit must be
explained.

`scripts/verify_rational_quotient_boundary.py` exhaustively checks the
matrix identities and all quotient cuts of small index, together with
all cuts of size or co-size at most three at larger index, through small
primes.
