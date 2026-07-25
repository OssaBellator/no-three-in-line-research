# Cross-conflict star localization

PP3pr leaves a growing cross-conflict clique or, more generally, a dense graph
of rectangle pairs whose simultaneous cross orientation creates a geometric bad
box.  Because every rectangle state contains exactly two cells, a rank-two
cross-state bad box has only three witness forms.  This chapter turns a dense
cross-conflict graph into one explicit line or pencil structure.

## 1. Dense cross conflicts give a linear star

Let \(K\) be the number of flexible rectangle variables and let \(G_\times\) be
the graph whose edge \(st\) means that state pair \((1,1)\) is forbidden.

### Proposition PP3ps -- PROVED

If

\[
 |E(G_\times)|\ge cK^2
\]

for a fixed \(c>0\), then some rectangle variable is incident with at least

\[
 2cK
\]

cross-conflict edges.

#### Proof

The average degree is

\[
 \frac{2|E(G_\times)|}{K}\ge2cK.
\]

Take a vertex of at least average degree. ∎

Thus the dense binary alternative always contains a linear star.  A separate
matching extraction is unnecessary at this stage.

## 2. Exact witness taxonomy

Write the cross diagonal of rectangle \(s\) as

\[
 D_s^1=\{a_s,b_s\}.
\]

Fix the residual source and source-valid residual matching, and denote their
union by \(F\).

### Proposition PP3pt -- PROVED

Every rank-two bad box forbidding \(X_s=X_t=1\) has at least one collinear
witness of one of the following forms.

1. **Centre-double form:** both cells of \(D_s^1\) and one cell of \(D_t^1\).
2. **Neighbour-double form:** one cell of \(D_s^1\) and both cells of \(D_t^1\).
3. **Fixed-anchor form:** one cell of \(D_s^1\), one cell of \(D_t^1\), and one
   point of \(F\).

For a star centred at \(s\), there are only finitely many refined witness types:
which of \(a_s,b_s\) is used when the centre contributes one cell, which of
\(a_t,b_t\) is used when the neighbour contributes one cell, and which of the
three forms occurs.

#### Proof

A rank-two bad box depends nontrivially on both rectangle variables.  Its
collinear triple therefore meets both disjoint rectangle supports.  Since each
cross state contains two points, the variable-point multiplicities are either
\(2+1\), \(1+2\), or \(1+1\) together with one fixed point.  The cell choices
within a two-point state give only finitely many refinements. ∎

Consequently a linear cross-conflict star contains a linear substar with one
common refined witness type.

## 3. Centre-double stars give one rich line

### Proposition PP3pu -- PROVED

Suppose a cross-conflict star centred at rectangle \(s\) has \(h\) neighbours,
and every chosen witness is of centre-double form using both cells of
\(D_s^1\).  Then the line

\[
 \ell_s=\overline{a_sb_s}
\]

contains one selected cross-state cell from each of the \(h\) neighbour
rectangles.

Those neighbour cells use pairwise disjoint endpoint resources.

#### Proof

The two centre cells determine the line \(\ell_s\).  Collinearity forces the
chosen cell from every neighbour to lie on this line.  Distinct rectangle
supports are resource-disjoint by PP3ok, so the neighbour cells share no old row
or old column. ∎

Thus a centre-double star is already a rich nonaxis line carrying a matching of
cross cells.

## 4. Neighbour-double stars give a pencil

Fix the one centre cell \(a_s\) used by a refined neighbour-double substar.  For
each neighbour \(t\), let

\[
 \ell_t=\overline{a_tb_t}
\]

be its cross-diagonal line.  The witness condition says \(a_s\in\ell_t\).

### Proposition PP3pv -- PROVED

For every integer \(D\ge1\), one of the following holds.

1. One geometric line through \(a_s\) is the cross-diagonal line of at least
   \(D\) neighbour rectangles.
2. At least \(h/D\) distinct cross-diagonal lines pass through \(a_s\).

In the first case the common line contains \(2D\) resource-disjoint neighbour
cells.  In the second case there is a pencil of at least \(h/D\) distinct lines
through one selected rectangle cell.

#### Proof

Group the \(h\) neighbours by their geometric line \(\ell_t\).  If one class has
size at least \(D\), use it.  Otherwise more than \(h/D\) classes are required.
Resource-disjointness follows from the rectangle extraction. ∎

Taking \(D=\lceil\sqrt h\rceil\) gives either a
\(\sqrt h\)-rich common line or a \(\sqrt h\)-line pencil.

## 5. Fixed-anchor stars give an anchored pencil

Fix the centre cell \(a_s\) and the chosen neighbour cell \(c_t\in D_t^1\) in a
refined fixed-anchor substar.  For every neighbour choose one witness point
\(p_t\in F\) such that

\[
 a_s,c_t,p_t
\]

are collinear.

### Proposition PP3pw -- PROVED

For every integer \(D\ge1\), one of the following holds.

1. One fixed point \(p\in F\) witnesses at least \(D\) star edges.  Then the
   line \(\overline{a_sp}\) contains at least \(D\) resource-disjoint neighbour
   cells.
2. At least \(h/D\) distinct fixed witness points, and hence at least \(h/D\)
   distinct witness lines through \(a_s\), occur.

#### Proof

Group the neighbours by \(p_t\).  A repeated witness point determines one common
line through \(a_s\).  If no point occurs \(D\) times, at least \(h/D\) witness
points are needed.  Two distinct witness points cannot determine the same line
through \(a_s\) unless that line contains both fixed points and \(a_s\); such a
line would contain three points of the already source-valid fixed set when
\(a_s\in F\), or can simply be grouped as one geometric line when
\(a_s\notin F\).  In either formulation the alternatives are a repeated rich
line or many distinct lines through \(a_s\). ∎

For complete formal safety in the second alternative, lines rather than witness
points are the canonical objects; repeated collinear witness points are merged.

## 6. Complete cross-conflict endpoint

### Corollary PP3px -- PROVED

Assume the cross-conflict graph has positive edge density.  Then, after passing
to a linear substar and one refined witness type, at least one of the following
holds.

1. One nonaxis line contains a linear matching of cross-state cells from
   resource-disjoint rectangles.
2. One selected rectangle cell is the centre of a polynomially large pencil of
   neighbour cross-diagonal lines.
3. One selected rectangle cell is the centre of a polynomially large pencil of
   fixed-anchor witness lines.

More quantitatively, a star of size \(h=\Omega(K)\) yields either a line with
\(\Omega(\sqrt K)\) neighbour rectangles or a pencil of
\(\Omega(\sqrt K)\) distinct lines.

#### Proof

Use PP3ps and pigeonhole the finitely many refined forms from PP3pt.  Apply
PP3pu, PP3pv, or PP3pw to the retained substar. ∎

The preferred-orientation binary obstruction is therefore geometric again.  It
is no longer an arbitrary dense signed graph: it is a rich cross line or a
large pencil through one explicit rectangle cell.