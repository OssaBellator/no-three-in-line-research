# A collision-free local chamber bank and the support obstruction

BDA1 supplies canonical \(q\)-strip labels.  This note proves the
row-column state-bank part of BDA2 for any selected chamber block and shows
why one bounded block cannot, without an additional concentration
hypothesis, destroy a constant fraction of an arbitrarily large chamber.

## BDA2a -- local permutation bank

Select \(t\geq7\) current cells from one permutation layer,

\[
A=\{(c_i,r_i):1\leq i\leq t\},
\]

all lying in one fixed \(q\)-strip class.  The \(c_i\) and \(r_i\) are
pairwise distinct.  A replacement state is a perfect matching between
\(C=\{c_i\}\) and \(R=\{r_i\}\).

Forbid:

1. every original diagonal position \((c_i,r_i)\); and
2. every position occupied by the other permutation layer.

The resulting forbidden-position set \(F\) has degree at most two in every
row and column.

### Theorem BDA2a -- PROVED

There are at least \(t!/128\) replacement states.  Every such state:

- preserves the active row and column sets exactly;
- is disjoint from the other permutation layer;
- moves every selected chamber cell;
- is supported on exactly the selected rows and columns.

For a uniform state and every compatible prescribed matching \(Q\) of
rank \(r\),

\[
\Pr(Q\subseteq M)\leq\frac{128}{(t)_r}.
\]

Consequently, every original paid certificate containing a selected
chamber cell is removed as an exact certificate.  If \(R_r\) counts
potential new collinear triples using exactly \(r\) replacement cells and
\(3-r\) unchanged points, their expected number is at most

\[
128\left(
\frac{R_1}{t}
+\frac{R_2}{t(t-1)}
+\frac{R_3}{t(t-1)(t-2)}
\right).
\]

### Proof

The two forbidden positions are the old-layer matching and the
other-layer matching, so \(F\) has row and column degree at most two.  AN1
gives the count and cylinder bound.  A replacement is a perfect matching
on the same row and column sets.  Avoiding the second forbidden matching
gives layer disjointness, while avoiding the diagonal removes every old
selected cell.

An original certificate containing a selected cell cannot remain the same
three-point certificate because that cell is absent.  For new
certificates, sum the AN1 cylinder probability over the \(R_r\) compatible
rank-\(r\) prescriptions. \(\square\)

Taking \(t=7\) gives a uniformly bounded local family.  The theorem is
independent of \(q\); the \(q\)-strip data are needed in BDA3 to bound the
counts \(R_r\) and coordinate many blocks.

## BDA2b -- bounded support cannot destroy dispersed mass

Call a paid certificate **cell-private** if it contains a chamber cell
which occurs in no other paid certificate and the certificate is destroyed
only when that cell is removed.

### Proposition BDA2b -- PROVED

Fix constants \(h\) and \(c>0\).  If a chamber contains \(M>h/c\)
cell-private paid certificates on distinct chamber cells, no trade
supported on at most \(h\) active rows can destroy a \(c\)-fraction of all
the certificates.

### Proof

Such a trade removes at most one current-layer chamber cell in each of its
active rows, hence at most \(h\) of the private cells.  It destroys at most
\(h<cM\) of the certificates. \(\square\)

This is a support-counting obstruction, not a claim that every geometric
perfect chamber realizes the private pattern.  It shows the exact missing
input: BDA2 must either prove that paid chamber incidence concentrates on
one bounded block, or return a **bank/parallel union** of bounded trades.
The latter is the natural interface to BDA3.

`scripts/verify_bda_local_bank.py` exhaustively checks the cyclic
two-forbidden-matching regression and all observed cylinder events for
\(t=7,8\).
