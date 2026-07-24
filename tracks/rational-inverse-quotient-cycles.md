# Product-coloured quotient cycles and dihedral confinement

RI2j assigns every orbit edge in the \(H\)-coset quotient the target
colour

\[
C=R^{-1}AB,
\qquad
R=rH,
\]

where \(A,B\in Q=\mathbb F_p^\times/H\) are its endpoint cosets.
Consequently a coloured quotient walk is not an arbitrary labelled
graph walk: every colour acts by one explicit involution of the cyclic
group \(Q\).

## RI2k -- exact quotient-walk dynamics

Let

\[
A_0,A_1,\ldots,A_\ell\in Q
\]

be a quotient-support walk and let the edge \(A_iA_{i+1}\) have target
colour \(C_i\).  Then

\[
\boxed{
A_{i+1}=R C_i A_i^{-1}.
}
\]

### Theorem RI2k -- PROVED

For every admissible index,

\[
\boxed{
A_{2j}
=
A_0
\prod_{t=0}^{j-1}C_{2t+1}C_{2t}^{-1},
}
\]

\[
\boxed{
A_{2j+1}
=
R A_0^{-1}
\left(\prod_{t=0}^{j}C_{2t}\right)
\left(\prod_{t=0}^{j-1}C_{2t+1}^{-1}\right).
}
\]

Here an empty product is one.  Equivalently, the colour involutions

\[
\iota_C(A)=RCA^{-1}
\]

satisfy

\[
\boxed{
\iota_D\iota_C(A)=DC^{-1}A.
}
\]

Thus they generate a generalized-dihedral action: two successive
colours act by translation through their ratio.

For a closed walk of even length \(2m\), its colour word necessarily
obeys

\[
\boxed{
\prod_{t=0}^{m-1}C_{2t+1}
=
\prod_{t=0}^{m-1}C_{2t}.
}
\]

For a closed walk of odd length \(2m+1\), its starting coset obeys

\[
\boxed{
A_0^2
=
R
\left(\prod_{t=0}^{m}C_{2t}\right)
\left(\prod_{t=0}^{m-1}C_{2t+1}^{-1}\right).
}
\]

Because \(Q\) is cyclic, a fixed odd colour word has either no closed
walk, one starting coset, or exactly two starting cosets differing by
the unique order-two element of \(Q\).  In particular, a one-colour
support relation is a disjoint union of loops and edges and has no
simple cycle of length at least three.

### Proof

The recurrence is the RI2j colour identity solved for \(A_{i+1}\).
Applying it twice gives

\[
A_{i+2}=C_{i+1}C_i^{-1}A_i.
\]

Induction separately on the even and odd subsequences proves the first
two boxes.  The same two-step calculation is the involution-composition
identity.

Setting \(A_{2m}=A_0\) gives the even colour-product balance.  Setting
\(A_{2m+1}=A_0\) gives the odd square equation.  In a cyclic group of
order \(M\), the kernel of squaring has size
\(\gcd(2,M)\), so every solvable square equation has one or two
solutions.  With one colour \(C\), every vertex has the unique neighbour
\(\iota_C(A)\), and \(\iota_C^2\) is the identity; hence every component
has at most two vertices. \(\square\)

## RI3a -- colour-ratio subgroup confinement

Let \(\mathcal C\subseteq Q\) be the target colours used by one connected
quotient-support component, choose \(C_\ast\in\mathcal C\), and define

\[
\boxed{
L
=
\left\langle
CD^{-1}:C,D\in\mathcal C
\right\rangle
=
\left\langle
CC_\ast^{-1}:C\in\mathcal C
\right\rangle
\leq Q.
}
\]

### Corollary RI3a -- PROVED

If the component contains \(A_0\), then all its source vertices lie in

\[
\boxed{
A_0L
\ \cup\
R A_0^{-1}C_\ast L.
}
\]

The target colours themselves lie in the single coset \(C_\ast L\).
Consequently a component using \(s\) distinct source \(H\)-cosets
satisfies

\[
\boxed{
s\leq2|L|.
}
\]

Let \(\widetilde L\) be the inverse image of \(L\) in
\(\mathbb F_p^\times\).  The corresponding part of the invariant core
is contained in two \(\widetilde L\)-cosets, while its rational image is
contained in one \(\widetilde L\)-coset.

### Proof

The two displayed cosets form an invariant bipartition for every
\(\iota_C\), \(C\in\mathcal C\).  Indeed,

\[
\iota_C(A_0\ell)
=
R A_0^{-1}C_\ast
\bigl(CC_\ast^{-1}\ell^{-1}\bigr)
\in R A_0^{-1}C_\ast L,
\]

and applying \(\iota_C\) to an element of the latter coset returns an
element of \(A_0L\).  Connectivity gives the source containment.
The definition of \(L\) gives
\(\mathcal C\subseteq C_\ast L\), and the size bound follows.
Taking inverse images under
\(\mathbb F_p^\times\to Q\) converts quotient \(L\)-cosets into
\(\widetilde L\)-cosets. \(\square\)

RI3a is an exact simultaneous-structure alternative.  A quotient core
with small colour-ratio subgroup is already confined to two source
cosets and one image coset of one larger subgroup, the format needed by
the coset absorber interface after density is supplied.  If a connected
core occupies many source \(H\)-cosets, then its target colours generate
a ratio subgroup of size at least half that support.  The remaining RI3
work is therefore density/quotient-growth control inside this explicit
dihedral confinement, not classification of arbitrary coloured chains.

`scripts/verify_rational_quotient_cycles.py` exhaustively checks the
walk formulae, parity closure constraints, square-root multiplicities,
one-colour components, and colour-ratio subgroup confinement in small
cyclic quotients.
