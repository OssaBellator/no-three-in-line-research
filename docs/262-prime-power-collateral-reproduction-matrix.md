# The target-versus-collateral inequality is a subcritical reproduction-matrix problem

CMR1254--CMR1261 turn every physical triple into a live credit with a unique last
creation and physical owner.  A target response destroys at least one chosen parent
credit and creates a finite vector of offspring credits.  For a fixed finite owner,
this is a nonnegative reproduction matrix.

The correct final inequality is therefore a Perron--Frobenius condition: choose one
feasible response law for every target-credit class so that the expected offspring
matrix has spectral radius below one.  A positive Lyapunov weight then forces an
actual response with smaller weighted live-credit potential.

Fix one finite canonical owner after routing, fixed-core and blocker normalization.
Let

\[
\Sigma=\{1,\ldots,s\}
\]

be any finite partition of its possible live credits.  The finest choice is the
set of exact physical triples; coarser owner, line, height, carry or product
signatures are also allowed when their offspring counts are valid upper bounds.

For every class `sigma`, choose a probability law `mu_sigma` on a feasible response
bank which destroys one designated live credit of class `sigma`.  If no feasible
bank exists, the branch enters the unit-wall descent and no matrix row is required.

Let `N_tau(Q)` be the number of newly created credits of class `tau` in response
`Q`.

## 1. Exact offspring matrix

### Theorem CMR1262 -- PROVED

The chosen response policy defines a finite nonnegative matrix

\[
\boxed{
A_{\sigma\tau}
=
\mathbb E_{Q\sim\mu_\sigma}N_\tau(Q).
}
\]

Every entry is finite.  Surviving old credits do not appear in `A`; they cancel
between the old and new weighted potentials.

### Proof

Every response bank and every side-`n` physical triple universe are finite.  The
last-creation ledger distinguishes new credits from surviving credits exactly by
CMR1257.  Average the finite nonnegative offspring counts. ∎

Extra destroyed credits may be retained as additional gain; the matrix records
only offspring and therefore gives a conservative criterion.

## 2. A subinvariant weight forces expected descent

Let `v in R_{>0}^s` and define the weighted live-credit potential

\[
\mathcal W_v(S)
=
\sum_{\tau=1}^{s}v_\tau C_\tau(S),
\]

where `C_tau(S)` is the number of live credits of class `tau`.

### Theorem CMR1263 -- PROVED

If

\[
\boxed{Av<v}
\]

componentwise, then targeting any live class `sigma` with its chosen bank law gives

\[
\boxed{
\mathbb E
\left[
\mathcal W_v(Q)-\mathcal W_v(S)
\right]
<0.
}
\]

Consequently some feasible response state has strictly smaller weighted live-credit
potential.

### Proof

The targeted response destroys at least the designated parent credit of weight
`v_sigma`.  Surviving credits cancel.  Expected new weighted credit is

\[
\sum_\tau A_{\sigma\tau}v_\tau=(Av)_\sigma<v_\sigma.
\]

Any additional destroyed credits only lower the change.  A negative finite average
has a negative summand. ∎

This is the weighted version of CMR1193--CMR1194.

## 3. Spectral-radius equivalence

### Theorem CMR1264 -- PROVED

For a finite nonnegative matrix `A`, the following are equivalent.

1. There exists `v>0` with `Av<v` componentwise.
2. The spectral radius satisfies
   \[
   \boxed{\rho(A)<1.}
   \]

If `rho(A)<1`, one explicit choice is

\[
\boxed{
v=(I-A)^{-1}\mathbf 1
=
\sum_{k=0}^{\infty}A^k\mathbf 1,
}
\]

for which

\[
Av=v-\mathbf 1<v.
\]

### Proof

If `rho(A)<1`, the Neumann series converges entrywise and gives the displayed
positive vector.

Conversely, if `Av<v`, put

\[
\alpha=\max_\sigma\frac{(Av)_\sigma}{v_\sigma}<1.
\]

Then `Av<=alpha v`.  Conjugating by the diagonal matrix with diagonal `v` gives a
nonnegative matrix with every row sum at most `alpha`, so its spectral radius, and
hence `rho(A)`, is at most `alpha<1`. ∎

Thus the missing weighted inequality is exactly subcriticality of a finite
credit-reproduction system.

## 4. Upper offspring matrices are sufficient

Suppose exact response expectations are difficult, but a nonnegative matrix
`Ahat` satisfies

\[
\mathbb E_{Q\sim\mu_\sigma}N_\tau(Q)
\le
\widehat A_{\sigma\tau}
\]

for every pair of classes.

### Corollary CMR1265 -- PROVED

If

\[
\boxed{\rho(\widehat A)<1,}
\]

then the chosen policy has a positive weight vector which strictly decreases in
expectation under every targeted bank.

### Proof

CMR1264 supplies `v>0` with `Ahat v<v`.  Since `A<=Ahat` entrywise,

\[
Av\le\widehat Av<v.
\]

Apply CMR1263. ∎

The local envelopes CMR1238--CMR1253 are designed to populate such upper rows.

## 5. Finite policy selection

For each class `sigma`, let `mathcal P_sigma` be a finite set of feasible bank laws.
A deterministic policy chooses one law per class; a randomized policy chooses a
convex combination of their offspring rows.

### Theorem CMR1266 -- PROVED

A complete prime-power owner closes under the credit method if there is any row
selection or rowwise convex combination producing a matrix `A` with
`rho(A)<1`.

If every available law for one class is blocked, that class instead enters the
minimal unit-wall factorisation and strict structural descent.

### Proof

The selected rows define CMR1262.  Apply CMR1263--CMR1264.  Complete blockage is
CMR1150--CMR1163. ∎

This is a finite optimization problem at every fixed owner.

## 6. Relation to target-cell bank weights

### Theorem CMR1267 -- PROVED

The open weighted inequality CMR1196 is recovered by taking credit classes to be
exact physical triples and targeting one class at a time.  The scalar bank weights
there are a dual form of a positive vector `v` satisfying `Av<v`.

The target-cell aggregation CMR1248--CMR1253 is a coarser sufficient test: it groups
parent credits by a selected cell and bounds offspring through one local envelope
row.

### Proof

For exact triple classes, the weighted offspring-minus-parent expression in
CMR1263 is precisely

\[
\sum_\tau v_\tau N_\tau(Q)-v_\sigma.
\]

Averaging over the chosen bank law gives the row inequality `(Av)_sigma<v_sigma`.
Grouping classes and replacing exact offspring by local envelopes gives a valid
upper matrix as in CMR1265. ∎

Thus the spectral formulation does not change the target; it organizes the
required weights and offspring estimates.

## 7. Product and wall blocks

### Theorem CMR1268 -- PROVED UNDER THE STATED BLOCK-TRIANGULAR HYPOTHESIS

Suppose an exact product, unit-wall or child decomposition orders the credit
classes so that the resulting upper offspring matrix is block upper triangular:

\[
\widehat A
=
\begin{pmatrix}
A_1&*&\cdots\\
0&A_2&*\\
\vdots&\ddots&\ddots
\end{pmatrix}.
\]

Then

\[
\boxed{
\rho(\widehat A)=\max_j\rho(A_j).
}
\]

Hence subcriticality of every diagonal strict-child block implies subcriticality of
the complete owner.

### Proof

The characteristic polynomial of a block triangular matrix is the product of the
characteristic polynomials of its diagonal blocks.  Its eigenvalues are exactly
the union of the diagonal-block eigenvalues. ∎

The open structural task is to choose last-active owner classes so that cross-factor
collateral is genuinely triangular or is absorbed into a separately bounded
interface block.

## 8. Spectral frontier

### Corollary CMR1269 -- PROVED AS A REDUCTION

The global target-versus-collateral problem now has a precise finite form at every
canonical owner.

1. Choose credit classes and feasible response laws.
2. Bound the expected offspring matrix using exact bank permanents, local envelopes,
   line/height/carry classes, or finite enumeration.
3. Prove the upper matrix has spectral radius below one.
4. Use the resulting positive vector to select an actual lower weighted-potential
   response.
5. Route blocked rows through unit-wall descent and small factors through their
   lifted owners.

This reduction does not prove `rho<1`.  It identifies that inequality as the exact
next quantitative target and gives a finite linear-algebra certificate for any
successful bank weighting.

No all-`n` theorem is claimed.  Offspring matrices, Lyapunov inequalities, Neumann
weights, upper-matrix domination, policy mixtures and block-triangular assembly are
checked in
[`scripts/verify_prime_power_collateral_reproduction_matrix.py`](../scripts/verify_prime_power_collateral_reproduction_matrix.py).
