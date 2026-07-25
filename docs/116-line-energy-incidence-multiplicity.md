# Line-energy incidence multiplicity

PP3nu reduces failed owner-line improvement to a near-complete incidence design:
for a Hall-derived target set \(\mathcal A\), almost every owner can reach almost
every target cell through some replacement line. This chapter applies the
Szemerédi--Trotter incidence theorem and a multiplicity split. The result is one
geometric line that is simultaneously repeated by many owner assignments and
rich in Hall-target cells.

## 1. Typed owner/replacement lines

For owner \(i\) and replacement index \(j\), let

\[
\ell_{ij}
=
\overline{z_i(x_i,y_j)}.
\]

For each distinct geometric line \(\ell\), define

\[
m(\ell)
=
|\{(i,j):\ell_{ij}=\ell\}|
\]

and

\[
r(\ell)
=
|\mathcal A\cap\ell|.
\]

Let \(\mathscr L\) be the set of distinct typed lines. The full assignment
energy is

\[
\mathcal W
=
\sum_{\ell\in\mathscr L}m(\ell)r(\ell)
=
\sum_{i,j}|\mathcal A\cap\ell_{ij}|.
\]

Also

\[
\sum_{\ell\in\mathscr L}m(\ell)=q^2.
\]

### Proposition PP3nv -- PROVED FROM THE SZEMERÉDI--TROTTER THEOREM

If

\[
\mu=\max_{\ell\in\mathscr L}m(\ell),
\]

then an absolute constant \(C\) satisfies

\[
\mathcal W
\le
C\mu\left(
|\mathcal A|^{2/3}|\mathscr L|^{2/3}
+|\mathcal A|+|\mathscr L|
\right).
\]

In particular,

\[
\mathcal W=O(\mu q^{8/3}).
\]

#### Proof

Every ordinary incidence between \(\mathcal A\) and one distinct line is counted
in \(\mathcal W\) at most \(\mu\) times. Hence

\[
\mathcal W
\le
\mu I(\mathcal A,\mathscr L).
\]

Apply Szemerédi--Trotter and use
\(|\mathcal A|,|\mathscr L|\le q^2\). ∎

This already forces some line multiplicity \(\Omega(q^{1/3})\) when
\(\mathcal W=\Omega(q^3)\), but it does not by itself state that the repeated
line is target-rich. The next theorem supplies both properties.

## 2. Simultaneous multiplicity and target richness

### Theorem PP3nw -- PROVED

Fix constants \(\alpha,\beta>0\) and \(\delta>0\). Suppose

\[
|\mathcal A|\ge\alpha q^2
\]

and

\[
\mathcal W\ge\beta q|\mathcal A|.
\]

For all sufficiently large \(q\), there is a geometric line \(\ell\) satisfying

\[
m(\ell)\ge q^{1/3-\delta}
\]

and

\[
r(\ell)\ge q^{1-\delta}.
\]

#### Proof

Suppose no line has both properties. Split the lines into

\[
\mathscr L_{\operatorname{low}}
=
\{\ell:m(\ell)<q^{1/3-\delta}\}
\]

and its complement.

For the low-multiplicity lines,

\[
\sum_{\ell\in\mathscr L_{\operatorname{low}}}
m(\ell)r(\ell)
\le
q^{1/3-\delta}I(\mathcal A,\mathscr L)
=
O(q^{3-\delta})
\]

by Szemerédi--Trotter.

Every remaining line has multiplicity at least \(q^{1/3-\delta}\), so by the
contrary assumption it has target richness below \(q^{1-\delta}\). Therefore

\[
\sum_{\ell\notin\mathscr L_{\operatorname{low}}}
m(\ell)r(\ell)
<
q^{1-\delta}
\sum_{\ell}m(\ell)
=
q^{3-\delta}.
\]

Thus \(\mathcal W=O(q^{3-\delta})\), contradicting

\[
\mathcal W
\ge
\alpha\beta q^3
\]

for sufficiently large \(q\). ∎

The exponents may approach \(1/3\) and \(1\) arbitrarily closely. No dyadic
loss is needed.

## 3. Resource structure of one common line

Assume the relevant line is nonvertical and nonhorizontal, as in the
noncontroller recapture geometry.

### Proposition PP3nx -- PROVED

If one geometric line \(\ell\) has typed multiplicity \(m(\ell)\), then its
representations

\[
\ell=\ell_{i_1j_1}=\cdots=\ell_{i_sj_s}
\]

use pairwise distinct owner indices \(i_t\) and pairwise distinct replacement
indices \(j_t\). Consequently the endpoint cells

\[
(x_{i_t},y_{j_t})
\]

form a matching in the endpoint-resource graph, and all owner candidate points
\(z_{i_t}\) lie on \(\ell\).

The target cells \(\mathcal A\cap\ell\) also form a matching in the endpoint
rectangle.

#### Proof

For fixed owner \(i\), two distinct replacement rows on the same line through
\(z_i\) would force that line to be vertical. Thus the owner indices are
distinct.

For fixed replacement row \(y_j\), a nonhorizontal line meets that row in at
most one point. Since the old columns \(x_i\) are distinct, the replacement
indices are distinct. This proves the first matching statement. The target-cell
statement is the same nonaxis row-and-column intersection argument as PP3lm. ∎

Thus the obstruction contains two large matching traces on one geometric carrier:
one trace of owner/replacement cells and one trace of Hall-target cells.

## 4. Combined line-energy dichotomy

### Corollary PP3ny -- PROVED

Fix \(\alpha>0\) and \(\delta>0\). Suppose the Hall-derived target set satisfies

\[
|\mathcal A|\ge\alpha q^2
\]

and use the adaptive source-valid derangement of PP3nt. Then at least one of the
following holds.

1. A source-valid endpoint derangement strictly decreases the owner-line load.
2. There is one nonaxis geometric line containing both:
   - at least \(q^{1/3-\delta}\) pairwise resource-disjoint owner/replacement
     endpoint cells and their owner candidate points;
   - at least \(q^{1-\delta}\) Hall-target endpoint cells.

#### Proof

If improvement fails, PP3nu gives

\[
\mathcal W=(1-o(1))q|\mathcal A|.
\]

For sufficiently large \(q\), use PP3nw with any fixed \(\beta<1\), then apply
PP3nx. ∎

This replaces the second-generation grid-rich pencil by one target-rich common
line. The next conversion may work directly on two matching traces carried by
that line.
