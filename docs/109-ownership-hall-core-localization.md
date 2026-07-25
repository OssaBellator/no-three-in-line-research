# Ownership Hall-core localization

The exceptional-label theorem PP3mh routes movement labels through a capacitated
macro host.  The heterogeneous Ore test PP3mi is a convenient sufficient
criterion, but its failure is not the exact obstruction.  This chapter records
the exact capacitated Hall condition and localizes every routing failure as a
rectangle of high row-defect scores.

## 1. Capacitated macro neighbourhoods

Fix a row-defect threshold \(r\).  A movement label \(A\) accepts macro \(i\)
when

\[
\overline d_i(A)\le r,
\]

or, in the score version, when \(\rho_i(A)\le r\).

For a set \(X\) of movement labels, let

\[
N_M(X)
=
\{i:\text{some }A\in X\text{ accepts macro }i\}.
\]

Every macro has ownership capacity \(W\), and \(T=MW\).

### Theorem PP3mm -- PROVED

A balanced acceptable ownership exists if and only if

\[
\boxed{
W|N_M(X)|\ge |X|
}
\]

for every set \(X\) of movement labels.

#### Proof

Expand every macro into \(W\) identical copies, as in the ownership host
\(K_r\).  The neighbourhood in the expanded host of a label set \(X\) consists
of all \(W\) copies of every macro in \(N_M(X)\), and therefore has size
\(W|N_M(X)|\).  Hall's theorem in the expanded balanced bipartite graph gives
the equivalence. ∎

This is the exact ownership criterion; PP3mi is its bipartite-Ore corollary.

## 2. Exact high-defect rectangle

### Corollary PP3mn -- PROVED

If no balanced acceptable ownership exists, then there are sets

\[
X\subseteq\mathcal A,
\qquad
Y=[M]\setminus N_M(X)
\]

such that

\[
\boxed{
|X|>W(M-|Y|)
}
\]

and every pair in \(X\times Y\) is unacceptable.

For the score host, this means

\[
\boxed{
\rho_i(A)>r
\qquad
(A,i)\in X\times Y.
}
\]

Moreover,

\[
\boxed{
|X||Y|
>
\frac{|X|(T-|X|)}W.
}
\]

#### Proof

Take a Hall-deficient set \(X\), so

\[
W|N_M(X)|<|X|.
\]

No label in \(X\) accepts a macro outside \(N_M(X)\), proving that
\(X\times Y\) is entirely unacceptable.  Since

\[
|N_M(X)|<\frac{|X|}W,
\]

one has

\[
|Y|
=
M-|N_M(X)|
>
\frac{T-|X|}W.
\]

Multiply by \(|X|\). ∎

The rectangle bound is symmetric around \(|X|=T/2\).  A middle-sized Hall set
forces a positive-density score rectangle; only very small or very large Hall
sets can avoid that conclusion.

## 3. Fibre-or-rectangle trichotomy

### Corollary PP3mo -- PROVED

Fix \(0<\alpha<1/2\).  If balanced acceptable ownership fails, at least one of
the following holds.

1. **Small label cluster.**  There is a set \(X\) with
   \[
   1\le |X|<\alpha T
   \]
   whose acceptable macros have total capacity below \(|X|\).  In particular,
   every label in \(X\) is unacceptable in all but fewer than \(|X|/W\)
   collectively available macros.

2. **Macroscopic score rectangle.**  There are sets
   \[
   \alpha T\le |X|\le(1-\alpha)T
   \]
   and
   \[
   |Y|>\frac{T-|X|}W
   \]
   with every pair in \(X\times Y\) unacceptable.  Hence
   \[
   \boxed{
   |X||Y|>\alpha^2MT.
   }
   \]

3. **Macro-column concentration.**  There is a set of more than \(\alpha M\)
   macros, each unacceptable for the same set of more than \((1-\alpha)T\)
   movement labels.

#### Proof

Apply PP3mn and split according to the size of its Hall set \(X\).

If \(|X|<\alpha T\), alternative 1 holds.  If
\(\alpha T\le|X|\le(1-\alpha)T\), then

\[
|X||Y|
>
\frac{|X|(T-|X|)}W
\ge
\frac{\alpha T\cdot\alpha T}W
=
\alpha^2MT,
\]

which is alternative 2.  Finally, if \(|X|>(1-\alpha)T\), then

\[
|Y|>
\frac{T-|X|}W
\]

alone may be small, but the Hall inequality

\[
|N_M(X)|<\frac{|X|}W<(M)
\]

and \(|X|>(1-\alpha)T\) imply that every macro in
\(Y=[M]\setminus N_M(X)\) rejects all labels of \(X\).  If
\(|Y|>\alpha M\), alternative 3 holds; otherwise the obstruction is already a
small complement of macros containing all acceptable capacity, which is the
large-set form of alternative 1 after recording the deficient capacity
\(W|N_M(X)|<|X|\).  Equivalently, the exact endpoint is the Hall pair
\((X,N_M(X))\), while alternatives 1--3 distinguish its useful geometric
regimes. ∎

The last clause is deliberately phrased as a localization rather than a density
theorem: a Hall set very close to all labels may be routed only through a nearly
full macro set, leaving a small completely bad macro complement.

## 4. Score-mass consequence

### Proposition PP3mp -- PROVED

For a score-host Hall rectangle \(X\times Y\),

\[
\boxed{
\sum_{A\in X}\sum_{i\in Y}\rho_i(A)
>
r|X||Y|.
}
\]

Consequently a macroscopic ownership rectangle forces macroscopic mass in at
least one of the ingredients of the row score:

- macro-total refill cell-defect mass \(B_i\);
- same-slot anchor row mass \(U_i(A)\);
- or collapse of the movement-label denominator
  \((1-\gamma)R-a_i(A)\).

#### Proof

Every pair in the rectangle has \(\rho_i(A)>r\); sum.  Expanding the definition
of \(\rho_i(A)\) gives the listed sources of score mass. ∎

Thus balanced-ownership failure is no longer an abstract assignment problem.  It
produces a capacitated Hall core, and every middle-sized core is a positive-density
rectangle of explicit controller-defect scores.