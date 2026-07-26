# Last-entering credit ownership makes structural offspring matrices triangular

CMR1254--CMR1277 turn the target-versus-collateral problem into a finite
nonnegative offspring matrix.  The remaining product issue is whether anchored
or cross-factor collateral can feed credits back into an earlier structural
owner and thereby destroy block triangularity.

It cannot.  On the canonical selected execution, every nonconstant product move
varies one residual factor at a time.  Every triple created by that move contains
an entering edge of that factor, so its absolute last-entering owner belongs to
that same factor.  Fixed-core and sibling-factor cells may occur in the triple,
but they receive no owner charge.  A triple which survives contraction keeps its
old owner; contraction itself creates no new credit.

The resulting structural owner graph is finite and acyclic.  After ordering its
vertices topologically, the global credit-reproduction matrix is block upper
triangular.  Its spectral radius is therefore the maximum spectral radius of the
same-owner diagonal blocks.  Arbitrarily large but finite cross-factor
collateral in strict descendants changes only the scaling of the Lyapunov
weights, not the subcriticality condition.

## 1. Canonical structural owners

A **structural owner stage** is one normalized host/routing stage of the selected
minimum execution, together with its fixed core and exact product factors.

For a live physical triple credit `T`, let `a(T)` be its absolute labelled
last-entering edge from CMR1215.  If `a(T)` is still variable, its owner is the
unique current factor containing that edge.  If it has become fixed in an
interface, use the unique lifted response-bank owner of CMR1182--CMR1189.

### Theorem CMR1318 -- PROVED

Every live credit has one canonical structural owner `omega(T)`.  While the
physical triple survives, restrictions, conditioning and contraction do not
change `omega(T)`.

### Proof

CMR1214--CMR1219 give one absolute last-entering labelled edge and unique product
factor for every created triple.  A surviving triple receives no new creation
time under restriction or contraction.  If its owner edge becomes fixed,
CMR1182--CMR1189 give one canonical lifted owner obtained from the last stage at
which that edge was active.  Thus the owner is unique and persistent. ∎

## 2. One-coordinate product moves create no sibling or core owners

Let

\[
\mathcal F
=
\left\{
C\sqcup\bigsqcup_{b\in B}R_b:R_b\in\mathcal F_b
\right\}
\]

be an exact product with pairwise disjoint labelled factor edge sets `E_b` and
fixed compatible core `C`.  Freeze every coordinate except one factor `a`, and
compare

\[
S=C\sqcup R_a\sqcup\bigsqcup_{b\ne a}R_b,
\qquad
Q=C\sqcup R'_a\sqcup\bigsqcup_{b\ne a}R_b.
\]

### Theorem CMR1319 -- PROVED

Every newly created physical triple in `Q` contains an edge of

\[
R'_a\setminus R_a.
\]

Its canonical last-entering owner edge lies in `E_a`.  Consequently all new
credits belong to the active factor `a`, even when their triples also meet `C`
or other factors.

### Proof

Every edge outside `E_a` is identical in `S` and `Q`.  A triple present in `Q`
but absent from `S` must therefore contain an edge newly entering through
`R'_a\setminus R_a`.  All entering edges lie in `E_a`, so the least entering edge
of CMR1215 lies there.  Fixed-core and sibling-factor edges are not entering and
cannot own the new credit. ∎

This applies to the pure, anchored and cross-factor rank patterns of
CMR958--CMR960.

## 3. Fixed interfaces do not create upward offspring

### Theorem CMR1320 -- PROVED

Suppose a triple survives after some of its edges enter the fixed core.

1. The surviving triple keeps its previous structural owner.
2. The conditioning or contraction step creates no offspring credit.
3. Any later newly created anchored triple containing fixed-core edges is owned
   by one newly entering residual edge at the current response owner.
4. A target lying wholly in a fixed interface is answered at its canonical
   lifted owner; that is the target's existing owner, not a reverse transition
   from a descendant.

### Proof

The first two statements are the last-creation convention of CMR1254--CMR1257.
For the third, fixed-core edges are present before and after the move, so CMR1319
places the owner on an entering residual edge.  The final statement is exactly
the lifted-owner construction of CMR1182--CMR1189. ∎

Thus contraction cannot manufacture a credit owned by an ancestor or sibling.

## 4. Structural exits are acyclic

Form a directed graph `D_own` whose vertices are the structural owner stages of
one complete selected closure execution.  Add an arc when the execution leaves
one owner for a strict child, unit-wall factor, later normalized host stage, or
later closure-envelope stage.

### Theorem CMR1321 -- PROVED

`D_own` is finite and acyclic.

### Proof

At fixed factor side, normalized host stages are monotone and finite by CMR691
and CMR1098.  A selected child factor has strictly smaller positive side by
CMR1096.  A unit-wall split replaces side `m` by children with side sum `m-1` by
CMR741--CMR747.  The closure-envelope chain has at most `h+1` one-way stages.
Ordering first by closure stage, then by wall-tree ancestry, factor side and
normalized host time gives a strict topological rank on every structural exit. ∎

Repeated same-owner bank responses are not arcs of `D_own`; they belong to one
diagonal block.

## 5. Exact block upper triangularity

At every owner `omega`, choose any finite partition `Sigma_omega` of the credits
owned there and any deterministic or randomized response law for each class.
Let `A` be the expected offspring matrix on the disjoint union

\[
\Sigma=\bigsqcup_\omega\Sigma_\omega.
\]

Order the owners topologically in `D_own`.

### Theorem CMR1322 -- PROVED

The matrix `A` is block upper triangular:

\[
\boxed{
A=
\begin{pmatrix}
A_{11}&B_{12}&B_{13}&\cdots\\
0&A_{22}&B_{23}&\cdots\\
0&0&A_{33}&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix}.
}
\]

Here `A_{ii}` records offspring remaining at the same structural owner, while
`B_{ij}` records credits created after a strict structural exit to descendant
owner `j`.  No block below the diagonal is nonzero.

### Proof

A same-owner response contributes to the diagonal block.  By CMR1319--CMR1320,
new credits produced after a factor or fixed-interface move are owned by the
active current factor and never by a sibling or ancestor.  By CMR1321 every
structural exit goes forward in the topological order. ∎

## 6. Spectral reduction to same-owner blocks

### Theorem CMR1323 -- PROVED

For the finite matrix of CMR1322,

\[
\boxed{
\rho(A)=\max_i\rho(A_{ii}).
}
\]

Therefore the complete owner system is subcritical if and only if every
same-owner diagonal block is subcritical.

### Proof

The characteristic polynomial of a block upper triangular matrix is the product
of the characteristic polynomials of its diagonal blocks. ∎

No uniform bound on the off-diagonal block entries is needed for this spectral
identity.

## 7. Constructive gluing of local certificates

Assume each diagonal block has a positive rational certificate

\[
A_{ii}v_i\le v_i-s_i,
\qquad s_i>0.
\]

### Theorem CMR1324 -- PROVED

There are positive rational scales `c_i` such that

\[
v=(c_1v_1,\ldots,c_tv_t)
\]

satisfies

\[
\boxed{Av<v.}
\]

The scales may be chosen recursively from descendants to ancestors.  Having
chosen `c_j` for `j>i`, it is enough to take

\[
\boxed{
c_i>
\max_k
\frac{
\sum_{j>i}(B_{ij}c_jv_j)_k
}{(s_i)_k}.
}
\]

### Proof

For block row `i`, the diagonal contribution is at most
`c_i(v_i-s_i)`.  The displayed choice makes the total later-block contribution
strictly smaller than `c_is_i`.  Thus row `i` is strictly below `c_iv_i`.
Proceed upward through the finite topological order.  Rational input permits
rational choices. ∎

This is the geometric owner realization of the abstract block gluing in
CMR1267 and CMR1273.

## 8. Triangular product endpoint

### Corollary CMR1325 -- PROVED

For one complete selected prime-power closure execution:

1. last-entering ownership prevents sibling, fixed-core and ancestor duplicate
   offspring;
2. child, unit-wall, normalized-host and envelope exits form a finite owner DAG;
3. the global reproduction matrix is block upper triangular;
4. its spectral radius is the maximum same-owner spectral radius;
5. rational same-owner certificates glue constructively regardless of the size of
   finite cross-factor off-diagonal collateral.

Hence product, unit-wall and lifted fixed-interface coupling do not create a new
spectral obstruction once the same-owner bank blocks are subcritical.  The
remaining quantitative frontier is to construct uniform line/height/carry
classes and prove subcriticality of the same-owner diagonal blocks in inherited
coordinates, together with the prime-field, thin and CRT diagonal blocks.

No all-`n` theorem is claimed.  Product ownership, acyclic owner graphs, block
triangularity, spectral identities and constructive certificate scaling are
checked in
[`scripts/verify_prime_power_last_entering_owner_triangularity.py`](../scripts/verify_prime_power_last_entering_owner_triangularity.py).
