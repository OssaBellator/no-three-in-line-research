# Ownership Hall-core localization

The exceptional-label theorem PP3mh routes movement labels through a capacitated
macro host. The heterogeneous Ore test PP3mi is sufficient but not exact. This
chapter records the exact capacitated Hall condition and localizes every routing
failure as a rectangle of high row-defect scores.

## 1. Capacitated macro neighbourhoods

Fix a row-defect threshold \(r\). A movement label \(A\) accepts macro \(i\)
when

\[
\overline d_i(A)\le r,
\]

or, in the score version, when \(\rho_i(A)\le r\). For a set \(X\) of movement
labels, let

\[
N_M(X)=\{i:\text{some }A\in X\text{ accepts macro }i\}.
\]

Every macro has ownership capacity \(W\), and \(T=MW\).

### Theorem PP3mm -- PROVED

A balanced acceptable ownership exists if and only if

\[
\boxed{W|N_M(X)|\ge |X|}
\]

for every set \(X\) of movement labels.

#### Proof

Expand every macro into \(W\) identical copies, as in the ownership host
\(K_r\). The neighbourhood in the expanded host of \(X\) consists of all
\(W\) copies of every macro in \(N_M(X)\), and therefore has size
\(W|N_M(X)|\). Hall's theorem gives the equivalence. ∎

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
\boxed{|X|>W(M-|Y|)}
\]

and every pair in \(X\times Y\) is unacceptable. For the score host,

\[
\boxed{\rho_i(A)>r\qquad((A,i)\in X\times Y).}
\]

Moreover,

\[
\boxed{|X||Y|>\frac{|X|(T-|X|)}W.}
\]

#### Proof

Take a Hall-deficient set \(X\), so

\[
W|N_M(X)|<|X|.
\]

No label in \(X\) accepts a macro outside \(N_M(X)\), proving that
\(X\times Y\) is entirely unacceptable. Since

\[
|N_M(X)|<\frac{|X|}W,
\]

one has

\[
|Y|=M-|N_M(X)|>\frac{T-|X|}W.
\]

Multiply by \(|X|\). ∎

## 3. Fibre-or-rectangle trichotomy

### Corollary PP3mo -- PROVED

Fix \(0<\alpha<1/2\). If balanced acceptable ownership fails, at least one of
the following holds.

1. **Small Hall cluster.** There is a set \(X\) with
   \[
   1\le |X|<\alpha T
   \]
   whose acceptable macro capacity is below \(|X|\).

2. **Macroscopic score rectangle.** There are sets with
   \[
   \alpha T\le |X|\le(1-\alpha)T
   \]
   and every pair in \(X\times Y\) unacceptable, where
   \[
   \boxed{|X||Y|>\alpha^2MT.}
   \]

3. **Nearly dead macro column.** There is at least one macro that is unacceptable
   for the same set of more than \((1-\alpha)T\) movement labels.

#### Proof

Apply PP3mn and split according to \(|X|\). If \(|X|<\alpha T\), alternative 1
holds. In the middle range,

\[
|X||Y|>
\frac{|X|(T-|X|)}W
\ge
\frac{\alpha T\cdot\alpha T}W
=
\alpha^2MT,
\]

which is alternative 2.

Finally suppose \(|X|>(1-\alpha)T\). Hall deficiency implies

\[
|N_M(X)|<\frac{|X|}W\le M,
\]

so \(Y=[M]\setminus N_M(X)\) is nonempty. Every macro in \(Y\) rejects every
label in \(X\), and any one of them gives alternative 3. ∎

The third alternative intentionally guarantees one nearly dead macro column,
not a positive fraction of macros. A Hall set very close to all labels can have a
small completely bad macro complement.

## 4. Score-mass consequence

### Proposition PP3mp -- PROVED

For a score-host Hall rectangle \(X\times Y\),

\[
\boxed{
\sum_{A\in X}\sum_{i\in Y}\rho_i(A)>r|X||Y|.
}
\]

Consequently a macroscopic ownership rectangle forces macroscopic mass in at
least one ingredient of the row score:

- macro-total refill cell-defect mass \(B_i\);
- same-slot anchor row mass \(U_i(A)\);
- or collapse of the movement-label denominator
  \((1-\gamma)R-a_i(A)\).

#### Proof

Every pair in the rectangle has \(\rho_i(A)>r\); sum. Expanding the definition
of \(\rho_i(A)\) gives the listed sources of score mass. ∎

Thus balanced-ownership failure is no longer an abstract assignment problem. It
produces a capacitated Hall core, every middle-sized core is a positive-density
rectangle of explicit controller-defect scores, and every very large Hall set
produces a nearly dead macro column.