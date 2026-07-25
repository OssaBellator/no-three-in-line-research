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

## RI3b -- parity refinement and the odd-cycle collapse

Let \(\Gamma\) be the underlying connected quotient-support component.
For a subset \(\mathcal A\subseteq Q\), write

\[
\langle\mathcal A\mathcal A^{-1}\rangle
=
\left\langle AB^{-1}:A,B\in\mathcal A\right\rangle.
\]

### Corollary RI3b -- PROVED

If \(\Gamma\) is bipartite with source-vertex parts
\(\mathcal U,\mathcal V\), then

\[
\boxed{
L
=
\left\langle\mathcal U\mathcal U^{-1},
\mathcal V\mathcal V^{-1}\right\rangle.
}
\]

For any \(U_0\in\mathcal U\) and \(V_0\in\mathcal V\),

\[
\boxed{
\mathcal U\subseteq U_0L,
\qquad
\mathcal V\subseteq V_0L,
\qquad
\mathcal C\subseteq R^{-1}U_0V_0L.
}
\]

If \(\Gamma\) is not bipartite, then it contains an odd cycle and

\[
\boxed{
L
=
\left\langle
AB^{-1}:A,B\in V(\Gamma)
\right\rangle.
}
\]

In that case every source vertex and every target colour lie in one
coset each:

\[
\boxed{
V(\Gamma)\subseteq A_0L,
\qquad
\mathcal C\subseteq R^{-1}A_0^2L.
}
\]

After lifting \(L\) to \(\widetilde L\leq\mathbb F_p^\times\), a
nonbipartite invariant component is therefore contained in one source
\(\widetilde L\)-coset and its image is contained in one target
\(\widetilde L\)-coset.  The two-source-coset alternative of RI3a is
needed only in the bipartite case.

### Proof

Along every length-two path with consecutive colours \(C,D\), RI2k
gives

\[
A_{i+2}A_i^{-1}=DC^{-1}\in L.
\]

Connectivity therefore puts ratios of vertices in the same bipartition
part inside \(L\).  Conversely, orient two arbitrary edges from
\(\mathcal U\) to \(\mathcal V\), say \(UV\) and \(U'V'\).  Their
colours obey

\[
\frac{R^{-1}UV}{R^{-1}U'V'}
=
(UU'^{-1})(VV'^{-1}).
\]

Thus every colour ratio belongs to the subgroup generated by the two
within-part ratio sets.  This proves the bipartite subgroup identity,
and its three coset containments follow immediately.

Now suppose \(\Gamma\) has an odd cycle.  In the RI3a containment, each
edge involution exchanges

\[
X=A_0L
\quad\text{and}\quad
Y=RA_0^{-1}C_\ast L.
\]

Following an odd closed walk places \(A_0\) in both \(X\) and \(Y\).
Cosets of one subgroup that intersect are equal, so \(X=Y\), and every
source vertex lies in \(A_0L\).  Hence every source-vertex ratio belongs
to \(L\).  In the reverse direction, a colour ratio is a product of two
source-vertex ratios by the displayed edge-colour calculation, so the
two generated subgroups are equal.  Finally
\(R^{-1}AB\in R^{-1}A_0^2L\) for every edge \(AB\), proving the target
containment. \(\square\)

## RI4a -- exact order-two quotient templates

Suppose now that

\[
L=\{1,\omega\},
\qquad
\omega^2=1,
\qquad
\omega\ne1.
\]

Choose a used target colour \(C_0\), a source vertex \(A\), and put

\[
B=RC_0A^{-1}.
\]

Since \(L\) is generated by the target-colour ratios, the component uses
both colours \(C_0\) and \(C_0\omega\).

### Corollary RI4a -- PROVED

Every source vertex belongs to

\[
\boxed{
\{A,A\omega,B,B\omega\}.
}
\]

Exactly one of the following two templates contains the entire
component.

1. **Alternating square.**  If \(AL\ne BL\), the four displayed
   vertices are distinct.  The only possible quotient edges are
   \[
   \boxed{
   \begin{array}{c|c}
   \text{colour }C_0&
   A\!-\!B,\quad A\omega\!-\!B\omega\\
   \text{colour }C_0\omega&
   A\!-\!B\omega,\quad A\omega\!-\!B.
   \end{array}
   }
   \]
   Thus the component is a connected subgraph of one alternating
   four-cycle.

2. **Loop-and-edge collapse.**  If \(AL=BL\), there are two source
   vertices \(A,A\omega\).  One target colour fixes both vertices and
   supplies the two possible loops; the other swaps the vertices and
   supplies their unique connecting edge.  Thus the component is a
   connected subgraph of this two-loop, one-edge template.

In particular, an order-two colour-ratio component has at most four
source \(H\)-cosets and at most two target \(H\)-cosets.  In the
nonbipartite collapsed case it has at most two source \(H\)-cosets.
After lifting \(L\), the square lies in two source
\(\widetilde L\)-cosets and one target \(\widetilde L\)-coset, while the
collapsed template lies in one source and one target
\(\widetilde L\)-coset.

### Proof

RI3a gives the four-vertex containment and
\(\mathcal C\subseteq C_0L=\{C_0,C_0\omega\}\).  If only one colour
were used, its ratio subgroup would be trivial, so both occur.

For \(\ell\in L\), the two colour involutions obey

\[
\iota_{C_0}(A\ell)=B\ell,
\qquad
\iota_{C_0\omega}(A\ell)=B\omega\ell,
\]

because every element of \(L\) is its own inverse.  When \(AL\) and
\(BL\) are distinct, these formulas give exactly the four edges in the
square and no loops.

If the cosets agree, write \(B=A\varepsilon\) with
\(\varepsilon\in\{1,\omega\}\).  For colour \(C_0\), the induced
permutation of \(\{A,A\omega\}\) is multiplication by
\(\varepsilon\); for colour \(C_0\omega\), it is multiplication by
\(\varepsilon\omega\).  Exactly one of these multipliers is \(1\) and
the other is \(\omega\).  Hence one colour gives the two fixed loops and
the other gives the connecting transposition.  All size and lifted
coset assertions follow. \(\square\)

## RI4b -- paid localization inside the order-two templates

Let \(\mathscr O\) be the set of actual \(\tau_r\)-orbits represented
by one order-two quotient component.  Give each orbit an arbitrary
nonnegative paid weight \(w(O)\), and put

\[
W=\sum_{O\in\mathscr O}w(O).
\]

Aggregate these weights by their quotient edge, including loops.

### Corollary RI4b -- PROVED

In the alternating-square case, one fixed quotient edge carries paid
weight at least

\[
\boxed{\frac W4.}
\]

In the loop-and-edge case, one fixed quotient edge carries paid weight
at least

\[
\boxed{\frac W3.}
\]

In both cases one of the two target colours carries at least \(W/2\).
The selected quotient edge fixes its two endpoint \(H\)-cosets and its
target \(H\)-coset.

The conclusion also applies directly to arbitrary nonnegative point
weights on the invariant core: give an orbit the sum of the weights of
its one or two points.  The resulting orbit weights sum to the original
point weight.

### Proof

RI4a lists at most four quotient edges in the square and at most three
in the collapsed template.  These edge classes partition the actual
orbits, so a heaviest class carries the asserted reciprocal fraction.
There are exactly two possible target colours, giving the \(W/2\)
colour localization.  Every quotient edge has one endpoint-coset pair,
and RI2j fixes its target colour.  Summing point weights over disjoint
involution orbits proves the last assertion. \(\square\)

RI4b supplies the paid finite-channel input missing from the bare RI4
classification.  The remaining RI5 task on the order-two branch is to
lift one fixed normalized endpoint-coset channel to a physical
row-column block and compare its state family; no further quotient
mixture has to be handled.  RI5d--RI5e make the occurrence base scale
and the installed-block audit explicit before the conditional I6 bank
is used.

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
one-colour components, colour-ratio subgroup confinement, the exact
bipartite side-ratio identity, and the odd-cycle one-coset collapse in
small cyclic quotients.  It also enumerates both order-two templates
through larger cyclic quotient groups and checks their paid edge and
colour localization constants.
