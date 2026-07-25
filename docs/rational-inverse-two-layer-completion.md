# Two-layer installation of rational completion components

**Branch:** `research/rational-inverse-expansion`

RI5f decomposes a scale-localized physical completion debt into internal cycles and boundary paths relative to the current permutation layer. This note closes each boundary path by one explicit cell and then resolves all opposite-layer blockers selected inside the desired target family. Its singleton output is a provisional local obstruction; RI5l subsequently removes it using one auxiliary blocker cell from the full blocker permutation.

## Closed completion components

Let \(M_0\) be the current active permutation matching and \(M_1\) the disjoint blocker-layer permutation matching.

For an internal RI5f cycle \(C\), let \(D_C\) be its target matching.

For a boundary path

\[
P:x_1\to x_2\to\cdots\to x_k\to y,
\qquad y\notin X,
\]

RI5f gives

\[
\tau(x_i)=M_0(x_{i+1})\quad(1\le i<k),
\qquad
\tau(x_k)=M_0(y).
\]

Add the closure cell

\[
\boxed{q_P=(y,M_0(x_1)).}
\]

Define the closed target matching

\[
D_P=
\{(x_i,\tau(x_i)):1\le i\le k\}
\cup\{q_P\}.
\]

The rows of \(D_P\) are exactly the current rows on the columns
\(\{x_1,\ldots,x_k,y\}\). Thus \(D_P\) is a cyclic permutation switch on those columns.

Distinct RI5f components have disjoint column sets after adjoining their distinct outside endpoints, and their current row sets are disjoint. Hence any union \(D\) of closed path targets and internal-cycle targets is a matching on exactly the same rows and columns as the corresponding restriction of \(M_0\).

## RI5h -- opposite-layer derangement decoder -- PROVED

Let

\[
Q=D\cap M_1
\]

be the desired target cells occupied by the blocker layer, and put \(t=|Q|\).

1. If \(t=0\), replace \(M_0\) by \(D\) on the selected components and leave \(M_1\) unchanged.
2. If \(t\ge2\), label
   \[
   Q=\{(c_j,r_j):1\le j\le t\}.
   \]
   Choose any fixed-point-free permutation \(\pi\in S_t\). Replace \(M_0\) by \(D\), remove the blocker cells \(Q\), and insert
   \[
   \boxed{
   \{(c_j,r_{\pi(j)}):1\le j\le t\}
   }
   \]
   in \(M_1\).
3. If \(t=1\), let \(K\) be the unique completion component containing the blocked desired cell. Every other selected component can be installed simultaneously, while \(K\) remains as one explicit one-blocker alternating component within this restricted derangement construction.

In every case the asserted state preserves all rows and columns in both layers and preserves inter-layer disjointness.

### Proof

Every closed path or internal cycle target uses the same row and column sets as the current active matching on its component. The components are row-column-disjoint, so replacing any unblocked collection by its target matching preserves \(M_0\).

Now suppose \(t\ge2\). Since \(Q\subseteq M_1\), its columns \(c_j\) and rows \(r_j\) are pairwise distinct. Removing \(Q\) frees exactly those columns and rows in the blocker layer, and the displayed replacement is a perfect matching between them. The active target cell in column \(c_j\) is \((c_j,r_j)\). A replacement blocker cell in that column is \((c_j,r_{\pi(j)})\), which differs from the active cell because \(\pi(j)\ne j\). Hence the layers remain disjoint. No replacement can meet an active cell in another column.

When \(t=1\), all components other than \(K\) contain no blocker-layer target cell and may be switched directly. Restricting blocker changes to the single freed row and column of \(K\) would force reinsertion of the same blocked cell, so the residual datum for this restricted construction is exactly one blocker. RI5l removes it by adding any second blocker cell as an auxiliary. \(\square\)

## RI5i -- weighted completion-or-single-blocker alternative -- PROVED

Give the selected completion components nonnegative weights, with total \(W\).

- If \(|Q|\ne1\), all weight \(W\) is jointly installable by RI5h.
- If \(|Q|=1\) and the unique blocked component is \(K\), then either
  \[
  \boxed{w(K)>W/2,}
  \]
  producing a heavy provisional one-blocker completion component, or the other components are jointly installable and carry weight at least
  \[
  \boxed{W/2.}
  \]

### Proof

Only the component \(K\) must be left unchanged by the restricted RI5h construction. The directly installable remainder has weight \(W-w(K)\), which is at least \(W/2\) unless \(w(K)>W/2\). RI5l later installs \(K\) as well, subject only to its explicit collateral comparison. \(\square\)

## RI5j -- blocker-derangement bank -- PROVED

For \(t\ge7\), let \(\Omega_t\) be the uniform bank of all fixed-point-free permutations used in RI5h. Then

\[
\boxed{|\Omega_t|\ge t!/128,}
\]

and every prescribed compatible partial blocker replacement of rank \(r\) has probability at most

\[
\boxed{\frac{128}{(t)_r}.}
\]

### Proof

After the desired active target matching \(D\) is fixed, the blocker replacement problem is exactly the forbidden-diagonal permutation bank: column \(c_j\) may use any freed row except \(r_j\). The AN1 counting and cylinder bounds therefore apply verbatim. \(\square\)

## Interface to RI6 and AC3

RI5f--RI5j reduce physical completion to executable component switches and a local blocker-replacement problem. RI5l--RI5p complete and classify the remaining singleton case:

- internal cycles and closed boundary paths install together;
- two or more selected blockers use the RI5h derangement;
- one selected blocker uses the RI5l auxiliary transposition;
- large blocker sets use the RI5j normalized bank;
- failed singleton collateral localizes to RI5o vertical, horizontal, or paired-rectangle channels.

Thus opposite-layer occupancy is fully resolved. The remaining work is the explicit collateral comparison and arithmetic classification of a failed channel/profile output.

## Finite check

`scripts/verify_rational_two_layer_completion.py` exhausts current and target permutations, nonempty partial target blocks, and disjoint blocker permutations through size five. It verifies the RI5f component closure, all three RI5h blocker cases, preservation of both matchings, inter-layer disjointness, and the weighted half-or-heavy provisional singleton alternative.