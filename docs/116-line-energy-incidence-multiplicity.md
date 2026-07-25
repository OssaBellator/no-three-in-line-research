# Line-energy incidence multiplicity

PP3nu reduces failed owner-line improvement to a near-complete incidence design:
for a Hall-derived target set \(\mathcal A\), almost every owner can reach almost
every target cell through some replacement line. This chapter applies the
Szemerédi--Trotter incidence theorem and a multiplicity split. The result is a
large family of nonaxis geometric lines, each simultaneously repeated by many
owner assignments and rich in Hall-target cells.

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

## 2. Axis assignments are negligible

In the movement/refill recapture geometry, every candidate point has one new
coordinate and one old coordinate. The current designated blocker line is
nonaxis.

### Proposition PP3nw -- PROVED

At most \(q\) typed owner/replacement pairs define a horizontal or vertical
line. Their total contribution to \(\mathcal W\) is \(O(q^2)\).

#### Proof

For a movement candidate, the new row coordinate prevents a horizontal line.
The old owner column is fixed as \(j\) varies; a vertical line would also contain
the current owner endpoint and would be the automatic controller-containing
axis blocker, contrary to the noncontroller designated line.

For a refill candidate, the new column coordinate prevents a vertical line. A
horizontal line can occur for at most one selected old row \(y_j\) for each
owner. The transposed orientation gives the same bound. Thus there are at most
\(q\) axis typed pairs. Every axis line meets the endpoint target rectangle in at
most \(q\) cells. ∎

Only the \(O(q^2)\) total bound is used below.

## 3. Simultaneous multiplicity and target richness

### Theorem PP3nx -- PROVED

Fix constants \(\alpha,\beta>0\) and \(\delta>0\). Suppose

\[
|\mathcal A|\ge\alpha q^2
\]

and

\[
\mathcal W\ge\beta q|\mathcal A|.
\]

Let \(\mathscr G\) be the family of nonaxis lines satisfying

\[
m(\ell)\ge q^{1/3-\delta}
\]

and

\[
r(\ell)\ge q^{1-\delta}.
\]

For all sufficiently large \(q\), there is a constant
\(c=c(\alpha,\beta)>0\) such that

\[
\sum_{\ell\in\mathscr G}m(\ell)r(\ell)
\ge cq^3.
\]

Consequently,

\[
|\mathscr G|\ge cq,
\qquad
\sum_{\ell\in\mathscr G}m(\ell)\ge cq^2,
\qquad
\sum_{\ell\in\mathscr G}r(\ell)\ge cq^2.
\]

#### Proof

The axis contribution is \(O(q^2)\) by PP3nw. Among nonaxis lines with
multiplicity below \(q^{1/3-\delta}\), Szemerédi--Trotter gives total energy

\[
O(q^{1/3-\delta}q^{8/3})
=
O(q^{3-\delta}).
\]

The remaining nonaxis lines outside \(\mathscr G\) have target richness below
\(q^{1-\delta}\). Their total energy is at most

\[
q^{1-\delta}
\sum_\ell m(\ell)
\le
q^{3-\delta}.
\]

The hypothesis gives

\[
\mathcal W\ge\alpha\beta q^3.
\]

For sufficiently large \(q\), subtracting the three exceptional contributions
leaves at least \(cq^3\) energy on \(\mathscr G\).

A nonaxis line meets the endpoint rectangle in at most \(q\) cells and has typed
multiplicity at most \(q\), as proved below. Therefore

\[
m(\ell)r(\ell)\le q^2.
\]

This gives \(|\mathscr G|\ge cq\). The bounds on the two sums follow from
\(r(\ell)\le q\) and \(m(\ell)\le q\). ∎

Thus near-extremal assignment energy is supported by a positive linear number of
target-rich repeated lines, not one accidental carrier.

## 4. Resource structure of one good line

### Proposition PP3ny -- PROVED

If one nonaxis geometric line \(\ell\) has typed multiplicity \(m(\ell)\), then
its representations

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

Each good line therefore carries two large matching traces: owner/replacement
cells and Hall-target cells.

## 5. Combined line-energy dichotomy

### Corollary PP3nz -- PROVED

Fix \(\alpha>0\) and \(\delta>0\). Suppose the Hall-derived target set satisfies

\[
|\mathcal A|\ge\alpha q^2
\]

and use the adaptive source-valid derangement of PP3nt. Then at least one of the
following holds.

1. A source-valid endpoint derangement strictly decreases the owner-line load.
2. There is a family \(\mathscr G\) of \(\Omega_\alpha(q)\) distinct nonaxis
   lines such that:
   - every line carries at least \(q^{1/3-\delta}\) pairwise
     resource-disjoint owner/replacement endpoint cells and their owner candidate
     points;
   - every line contains at least \(q^{1-\delta}\) Hall-target endpoint cells;
   - the total owner/replacement multiplicity over the family is
     \(\Omega_\alpha(q^2)\).

#### Proof

If improvement fails, PP3nu gives

\[
\mathcal W=(1-o(1))q|\mathcal A|.
\]

For sufficiently large \(q\), apply PP3nx with any fixed \(\beta<1\), then use
PP3ny on every line of \(\mathscr G\). ∎

This replaces the second-generation grid-rich pencil by a positive-density
family of target-rich common-line carriers. The next conversion may exploit the
line family collectively through protected tomography or extract a smaller
executable rectangle/cycle bank from its two matching traces.
