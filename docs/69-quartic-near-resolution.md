# Quartic near-resolution and the disjoint-packing barrier

PX104 identifies the affine-root trade supports as a super-simple
\(2-(p,4,3)\) design.  This chapter gives an exact near-resolution of that
design and uses it to build global commuting batches of support-minimal trades.

The construction solves the Hamming-distance requirement from PX101: one batch
can rewrite every row except one.  It also exposes a new limitation.  A measure
built only from disjoint deterministic four-trade packages cannot have constant
rank-three spread.

Let \(p\equiv1\pmod4\) be prime, choose \(i^2=-1\), and put

\[
C_4=\{1,i,-1,-i\}\le\mathbb F_p^\ast.
\]

## 1. Centered form of an affine square

Recall

\[
V=\{0,1,-i,1-i\}.
\]

Put

\[
c_0=\frac{1-i}{2}.
\]

Then

\[
\boxed{
V-c_0
=
c_0 C_4.
}
\]

Indeed,

\[
c_0C_4
=
\left\{
\frac{1-i}{2},
\frac{1+i}{2},
-\frac{1-i}{2},
-\frac{1+i}{2}
\right\}.
\]

Thus every affine-square block has a unique representation

\[
c+qC_4,
\]

where \(c\in\mathbb F_p\) is its centre and \(qC_4\) is a multiplicative coset
of \(C_4\).

## Theorem PX106 -- PROVED

For each centre \(c\in\mathbb F_p\), the family

\[
\mathcal P_c
=
\{c+qC_4:q\in\mathbb F_p^\ast/C_4\}
\]

is a near-parallel class of the affine-square design:

1. it contains exactly \((p-1)/4\) pairwise disjoint blocks;
2. its blocks partition \(\mathbb F_p\setminus\{c\}\);
3. the \(p\) classes \(\mathcal P_c\) partition the complete block set
   \(\mathcal B_i\).

Consequently the affine-square \(2-(p,4,3)\) design is exactly
near-resolvable.

### Proof

The multiplicative cosets of \(C_4\) partition \(\mathbb F_p^\ast\).
Translation by \(c\) therefore makes the blocks in \(\mathcal P_c\) disjoint
and gives union \(\mathbb F_p\setminus\{c\}\).

Every affine square has a unique centre, because \(2\) is invertible and the
sum of its four vertices is four times its centre.  Its centred vertex set is
one coset \(qC_4\).  Thus every design block belongs to exactly one
\(\mathcal P_c\).  The total number of blocks is

\[
p\frac{p-1}{4},
\]

agreeing with PX104. \(\square\)

## 2. Commuting global trade batches

Take the affine root

\[
F(x)=ix+b.
\]

A PX98 trade on the square \(c+qC_4\) changes the four root values from slope
\(i\) about \(c\) to slope \(-i\) about \(c\).  On that block the new map is

\[
x\longmapsto -ix+b+2ic.
\]

### Corollary PX106a -- PROVED

Fix a centre \(c\).  For any subfamily

\[
\mathcal M\subseteq\mathcal P_c,
\]

apply the PX98 trade on every block in \(\mathcal M\).  The trades have disjoint
supports, commute, and produce a strong complete mapping.

The \(2^{(p-1)/4}\) choices of \(\mathcal M\) give distinct mappings.  Explicitly,

\[
G_{\mathcal M}(c)=F(c),
\]

and for \(x\ne c\),

\[
G_{\mathcal M}(x)
=
\begin{cases}
-ix+b+2ic,&x\text{ lies in a selected quartic coset block},\\
 ix+b,&x\text{ lies in an unselected block}.
\end{cases}
\]

Selecting the complete near-parallel class gives the opposite affine root

\[
\boxed{
G_{\mathcal P_c}(x)
=
-ix+b+2ic
}
\]

on every row, including \(x=c\).

### Proof

Every PX98 trade preserves the image, sum-colour, and difference-colour
multisets on its support.  Disjoint supports allow the identities to be
composed independently.  Distinct block subsets differ on the union of their
symmetric difference, so the resulting maps are distinct.

For the full class, every row except \(c\) is flipped to local slope \(-i\).
At the missing row,

\[
-ic+b+2ic=ic+b=F(c),
\]

so the same affine formula holds there as well. \(\square\)

Thus the two affine slope families are connected by a path of exactly

\[
\frac{p-1}{4}
\]

pairwise commuting support-minimal trades.  This globally changes \(p-1\) rows
and meets the Hamming-distance requirement of PX101.

## 3. Exact edge decoder

The square containing a prescribed changed edge is unique.

### Lemma PX106b -- PROVED

Fix a row \(x\) and a target image \(y\ne F(x)\).  There is exactly one
affine-square block \(B\ni x\) whose PX98 trade changes the root edge
\((x,F(x))\) to \((x,y)\).

Its centre is

\[
\boxed{
c
=
x+\frac{y-F(x)}{2i}.
}
\]

### Proof

A trade on a square centred at \(c\) gives

\[
y=-ix+b+2ic.
\]

Subtracting \(F(x)=ix+b\) gives

\[
y-F(x)=2i(c-x),
\]

which determines \(c\).  Once \(c\) and \(x\) are fixed, the multiplicative
coset \((x-c)C_4\) determines the unique square through \(x\). \(\square\)

Equivalently, the \(p-1\) affine squares through one row are in bijection with
the \(p-1\) alternative images in that row.

## 4. Why disjoint square packings do not prove spread

Let a random construction choose an affine root from

\[
\mathcal A_p
=
\{x\mapsto ix+b,\ x\mapsto-i x+b:b\in\mathbb F_p\}
\]

and then apply a matching \(\mathcal M\) of pairwise disjoint affine-square
trades.  Suppose

\[
|\mathcal M|=\frac{p-1}{4}
\]

almost surely, so all but one row are changed.

Every selected square contributes four distinct three-edge cylinders, obtained
by choosing three of its four new cells.

### Theorem PX107 -- PROVED

For every probability distribution of the preceding form, some three-edge
matching cylinder \(E\) satisfies

\[
\boxed{
\Pr(E\subseteq\operatorname{graph}(G))
\ge
\frac1{2p^2}.
}
\]

Consequently its rank-three spread constant obeys

\[
\boxed{
K_3
\ge
\frac{(p)_3}{2p^2}
=
\frac{(p-1)(p-2)}{2p}
=
\Omega(p).
}
\]

Thus disjoint affine-square packings can globally mix the permutation but
cannot by themselves establish the constant rank-three spread required by
PX97.

### Proof

Use labelled certificates \((F,B,T)\), where:

- \(F\) is one of the \(2p\) affine roots;
- \(B\) is one of the \(p(p-1)/4\) affine-square blocks;
- \(T\) is one of the four three-cell subsets of the new PX98 cells on \(B\).

There are

\[
2p\cdot\frac{p(p-1)}4\cdot4
=
2p^2(p-1)
\]

labels.

For every realized pair \((F,\mathcal M)\), each selected block contributes all
four of its labelled three-edge cylinders.  Hence the sum of the probabilities
of the labelled certificate events is

\[
4\mathbb E|\mathcal M|
=
p-1.
\]

At least one labelled event therefore has probability at least

\[
\frac{p-1}{2p^2(p-1)}
=
\frac1{2p^2}.
\]

The corresponding unlabelled three-edge cylinder has probability at least as
large.  Multiplication by \((p)_3\) gives the spread-constant bound. \(\square\)

The obstruction is deterministic packaging: three output edges can be forced
by selecting one four-row trade block.  Randomizing the block matching does not
supply a third independent probability factor.

## 5. Revised switching target

PX106 supplies an exact global path between affine roots and an exponential
hypercube of intermediate strong mappings.  PX107 shows that a probability
measure supported only on disjoint root-square packages remains too
rank-three-correlated.

A successful PX100 flow must therefore use at least one of:

1. overlapping trades after leaving the disjoint-packing cube;
2. trade paths whose later moves depend on earlier nonlinear values;
3. a mixture over larger switching components with no persistent four-edge
   package labels;
4. a second switching layer which splits the deterministic three-edge
   certificates generated by the first square packing.

The next concrete graph problem is to control trades from mappings obtained by
two or more disjoint root squares, where accidental overlapping trades first
become possible.

## 6. Verification

Run

```bash
python scripts/verify_product_quartic_near_resolution.py
```

The verifier checks the exact near-resolution at primes \(5,13,17,29\),
exhausts every fixed-centre hypercube, verifies the opposite-root formula,
checks the unique edge decoder, and reproduces the PX107 lower bound.
