# Line-energy incidence multiplicity

PP3nu reduces failed owner-line improvement to a near-complete incidence design:
for a Hall-derived target set \(\mathcal A\), almost every owner can reach almost
every target cell through some replacement line. This chapter applies the
Szemerédi--Trotter incidence theorem to show that such energy requires a highly
repeated geometric line.

## 1. Typed owner/replacement lines

For owner \(i\) and replacement index \(j\), let

\[
\ell_{ij}
=
\overline{z_i(x_i,y_j)}.
\]

Let \(\mathscr L\) be the set of distinct geometric lines occurring among the
\(q^2\) typed pairs \((i,j)\), and let

\[
\mu
=
\max_{\ell\in\mathscr L}
|\{(i,j):\ell_{ij}=\ell\}|
\]

be the maximum line multiplicity.

The full assignment energy is

\[
\mathcal W
=
\sum_{i,j}|\mathcal A\cap\ell_{ij}|.
\]

### Proposition PP3nv -- PROVED FROM THE SZEMERÉDI--TROTTER THEOREM

There is an absolute constant \(C\) such that

\[
oxed{
\mathcal W
\le
C\mu\left(
|\mathcal A|^{2/3}|\mathscr L|^{2/3}
+|\mathcal A|+|\mathscr L|
ight).
}
\]

#### Proof

For each distinct line \(\ell\), its incidences with \(\mathcal A\) are counted in
\(\mathcal W\) with multiplicity at most \(\mu\). Hence

\[
\mathcal W
\le
\mu\,I(\mathcal A,\mathscr L),
\]

where \(I\) is the ordinary point-line incidence number. Apply the
Szemerédi--Trotter theorem. ∎

Since \(|\mathscr L|\le q^2\) and \(|\mathcal A|\le q^2\), this gives the coarse
universal bound

\[
oxed{\mathcal W=O(\mu q^{8/3}).}
\]

## 2. Dense Hall target sets force repeated lines

### Corollary PP3nw -- PROVED

Fix \(\alpha>0\). Suppose

\[
|\mathcal A|\ge\alpha q^2
\]

and

\[
\mathcal W\ge(1-arepsilon)q|\mathcal A|
\]

for some \(0\learepsilon<1\). Then

\[
oxed{
\mu
\ge
c_\alpha(1-arepsilon)q^{1/3}
}
\]

for a positive constant \(c_\alpha\) depending only on \(\alpha\).

#### Proof

The lower bound on \(\mathcal W\) is at least
\((1-arepsilon)\alpha q^3\). Proposition PP3nv and
\(|\mathcal A|,|\mathscr L|\le q^2\) give

\[
(1-arepsilon)\alpha q^3
\le
C'\mu q^{8/3}.
\]

Rearrange. ∎

Thus the near-extremal alternative PP3nu cannot be supported by essentially
distinct owner/replacement lines.

## 3. Resource structure of one repeated line

Assume every relevant owner line is nonvertical and nonhorizontal, as in the
noncontroller recapture geometry.

### Proposition PP3nx -- PROVED

If one geometric line \(\ell\) has typed multiplicity \(\mu\), then its
representations

\[
\ell=\ell_{i_1j_1}=\cdots=\ell_{i_\mu j_\mu}
\]

use pairwise distinct owner indices \(i_t\) and pairwise distinct replacement
indices \(j_t\). Consequently the endpoint cells

\[
(x_{i_t},y_{j_t})
\]

form a matching in the endpoint-resource graph, and all corresponding candidate
points \(z_{i_t}\) lie on the same geometric line \(\ell\).

#### Proof

For fixed owner \(i\), distinct replacement rows \(y_j\) give distinct lines
through \(z_i\), because the line is not the vertical line \(x=x_i\). Hence the
owner indices are distinct.

For fixed replacement row \(y_j\), a nonhorizontal line meets that row in at
most one point. Since the old columns \(x_i\) are distinct, two representations
on the same line cannot share \(j\). The endpoint cells therefore use distinct
left and right resources. Each defining line contains its candidate \(z_i\). ∎

The repeated-line obstruction is therefore already an endpoint-compatible bank,
not merely a multiplicity count.

## 4. Combined line-energy dichotomy

### Corollary PP3ny -- PROVED

Suppose the Hall-derived target set has density

\[
|\mathcal A|\ge\alpha q^2
\]

for fixed \(\alpha>0\), and use the adaptive source-valid derangement of PP3nt.
Then at least one of the following holds.

1. A source-valid endpoint derangement strictly decreases the owner-line load.
2. There is one nonaxis geometric line containing
   \[
   \Omega_\alpha(q^{1/3})
   \]
   pairwise resource-disjoint owner/replacement endpoint cells and the associated
   owner candidate points.

#### Proof

If improvement fails, PP3nu gives

\[
\mathcal W=(1-o(1))q|\mathcal A|.
\]

Apply PP3nw and then PP3nx. ∎

This replaces the second-generation grid-rich pencil by a single common-line
matching of polynomial size. The next conversion may therefore use a protected
line, rectangle, cycle, or tomographic trade on one explicit geometric carrier.