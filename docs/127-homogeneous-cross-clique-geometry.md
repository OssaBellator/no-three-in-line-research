# Homogeneous cross-clique geometry

PP3po gives a growing cross-conflict clique when the preferred all-cross
orientation cannot be made pairwise compatible.  Pigeonholing only at one star
centre gives the line/pencil alternatives PP3px.  A second fixed-colour Ramsey
step makes the witness type homogeneous on every pair of a growing subclique.
The two inserted-triple witness forms then collapse to one common line.

## 1. Witness-homogeneous subclique

Let \(H\) be a cross-conflict clique.  Order its variables.  For every pair
\(s<t\), choose one witness for the bad state pair \((1,1)\), refined as in PP3pt:

- centre-double or neighbour-double;
- which one of the two cells is used when a rectangle contributes one point;
- fixed-anchor form together with the chosen local cell on each side.

There are finitely many such types.

### Proposition PP3py -- PROVED FROM THE FIXED-COLOUR RAMSEY THEOREM

Every growing cross-conflict clique contains a growing subclique on which the
chosen refined witness type is the same for every ordered pair.

#### Proof

Colour each pair by its refined witness type and apply the fixed-colour Ramsey
bound. ∎

The fixed anchor point itself is not part of the colour; only the local witness
form is homogenised.

## 2. Homogeneous centre-double cliques

For rectangle \(s\), let

\[
 D_s^1=\{a_s,b_s\},
 \qquad
 L_s=\overline{a_sb_s}.
\]

Assume that for every ordered pair \(s<t\), the witness uses both cells of
\(D_s^1\) and the same designated cell \(a_t\) of the upper rectangle.  Thus

\[
 a_t\in L_s.
\]

### Proposition PP3pz -- PROVED

If such a homogeneous clique has at least four variables, then all but at most
one of its cross diagonals lie on one common geometric line.  More precisely,
either

\[
 L_1=L_2=\cdots=L_{h-1},
\]

or the clique has size at most three.

#### Proof

For every \(t\ge3\), the point \(a_t\) lies on both \(L_1\) and \(L_2\).  If
\(L_1\ne L_2\), their intersection contains at most one point, so
\(a_3=a_4\), contradicting disjoint rectangle supports.  Hence \(L_1=L_2=L\).

Now suppose inductively that \(L_1=\cdots=L_{r-1}=L\) for some \(r<h\).  The
point \(a_r\) lies on \(L\).  For every \(t>r\), the point \(a_t\) lies on both
\(L\) and \(L_r\).  If \(L_r\ne L\), then all those \(a_t\) equal the unique
intersection \(L\cap L_r=a_r\), again contradicting disjoint supports as soon
as two such upper variables exist.  Therefore \(L_r=L\) whenever \(r\le h-1\).
∎

Thus a growing homogeneous centre-double clique contains a growing matching of
complete cross diagonals on one line.

## 3. Homogeneous neighbour-double cliques

Assume instead that for every ordered pair \(s<t\), the witness uses the same
designated cell \(a_s\) of the lower rectangle and both cells of the upper
rectangle.  Thus

\[
 a_s\in L_t.
\]

### Proposition PP3qa -- PROVED

If the clique has at least three variables, then

\[
 L_3=L_4=\cdots=L_h
\]

is one common line.  In particular a growing clique contains a growing matching
of complete cross diagonals on one geometric line.

#### Proof

For every \(t\ge3\), the line \(L_t\) contains the two distinct points
\(a_1,a_2\).  They are distinct because rectangle supports are disjoint.  Hence
\(L_t=\overline{a_1a_2}\) for every \(t\ge3\). ∎

The two inserted-triple witness forms therefore have the same asymptotic
endpoint: a common line carrying both cells of many cross diagonals.

## 4. Homogeneous fixed-anchor cliques

The remaining homogeneous type chooses one cell \(c_s\in D_s^1\) from every
lower rectangle and one cell \(d_t\in D_t^1\) from every upper rectangle.  For
each pair \(s<t\), there is a fixed point \(p_{st}\in F\) satisfying

\[
 c_s,d_t,p_{st}
 \quad\text{collinear}.
\]

### Definition

Such a system is a **complete fixed-anchor secant design**.  Its variable cells
are resource-disjoint, and every ordered cross pair is blocked by a point of the
fixed residual configuration.

### Proposition PP3qb -- PROVED

After unit-clause preprocessing, every line
\(\overline{c_sd_t}\) in a complete fixed-anchor secant design contains exactly
one fixed witness point.

#### Proof

It contains at least one by definition.  If it contained two distinct points of
\(F\), then the selected variable cell \(c_s\) together with those two fixed
points would form a collinear triple whenever rectangle \(s\) is in cross state.
That would forbid state one by a unit clause, contrary to flexibility. ∎

Thus duplicate fixed witnesses on one secant are impossible; each blocked pair
has one geometrically determined fixed anchor.

No claim is made here that the anchors \(p_{st}\) are distinct.  Repetition of
one anchor forces many variable cells onto lines through that anchor and is
already a pencil concentration of the type PP3pw.

## 5. Complete homogeneous-clique endpoint

### Corollary PP3qc -- PROVED

A growing cross-conflict clique contains a growing subclique of one of the
following two forms.

1. **Common cross line:** one nonaxis line contains complete cross diagonals from
   a growing resource-disjoint rectangle family.
2. **Complete fixed-anchor secant design:** one selected cross cell per local
   side is chosen so that every ordered variable pair has a unique fixed anchor
   on its secant.

#### Proof

Apply PP3py.  Centre-double and neighbour-double types give alternative 1 by
PP3pz and PP3qa.  The remaining type is alternative 2, with uniqueness from
PP3qb. ∎

The arbitrary cross-conflict clique has therefore been eliminated.  Its only
non-line realization is a complete secant design blocked point-by-point by the
fixed residual configuration.