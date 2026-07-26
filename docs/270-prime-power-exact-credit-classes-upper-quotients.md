# Exact credit classes admit rigorous coarse upper quotients

CMR1318--CMR1325 reduce the global spectral problem to same-owner diagonal
blocks.  A same-owner block is still state dependent: two physical targets with
the same line height or residual rank may live in different restricted hosts and
have different feasible response banks.

This chapter removes the need for exact lumpability.  At one finite owner, use
the complete state--target pairs as exact credit classes.  Any proposed geometric
compression -- line height, residual rank, anchor count, layer direction, carry
class, or a combination -- is a map from exact classes to finitely many coarse
classes.  Taking the largest coarse offspring row over every exact class in one
coarse fibre gives a nonnegative upper quotient matrix.  A positive certificate
for that upper quotient lifts automatically to the full exact matrix.

The construction is deliberately finite and exact.  It does not assert that the
resulting coarse matrix is subcritical; it gives the rigorous object on which
that claim must be proved or computationally certified.

## 1. Exact state--credit classes

Fix one structural owner `omega` with finite feasible state family
`F_omega`.  For every state `S in F_omega`, let `T(S)` be its set of live physical
triple credits.  A fixed canonical rule chooses one currently selected labelled
cell through which each target credit is answered.

Define the exact class set

\[
\Sigma_\omega
=
\{(S,T):S\in\mathcal F_\omega,\ T\in\mathcal T(S)\}.
\]

### Theorem CMR1326 -- PROVED

`Sigma_omega` is finite.  For every exact class and every finite rational response
law on its feasible same-owner bank, the expected number of newly created exact
credit classes is a finite rational row.

### Proof

The owner host has a finite labelled edge universe, hence finitely many feasible
states and finitely many physical triples per state.  A finite rational response
law is a finite rational combination of integer offspring counts. ∎

Structural-exit offspring belong to later owner blocks by CMR1322 and are omitted
from the same-owner row.

## 2. The exact same-owner matrix

Choose one rational response law `mu_sigma` for every `sigma in Sigma_omega`.
For exact classes `sigma,tau`, put

\[
A^\omega_{\sigma\tau}
=
\mathbb E_{Q\sim\mu_\sigma}
\bigl[\text{new credits of exact class }\tau\bigr].
\]

### Theorem CMR1327 -- PROVED

`A^omega` is a finite nonnegative rational matrix.  The exact-class weight
potential decreases under every selected response law precisely when there is a
positive vector `u` satisfying

\[
\boxed{A^\omega u<u.}
\]

### Proof

The matrix statement is CMR1262 specialized to the exact classes.  The expected
new weighted credit is the corresponding matrix row dotted with `u`; one parent
credit has weight `u_sigma`. ∎

No geometric information has yet been discarded.

## 3. Arbitrary coarse geometric classes

Let

\[
\pi:\Sigma_\omega\to\overline\Sigma_\omega
\]

be any finite class map.  Useful coordinates include:

1. residual creation rank `r in {1,2,3}`;
2. exact or dyadic primitive line-height band;
3. number of fixed-core or opposite-layer anchors;
4. owner layer and row/column direction;
5. quotient, carry, prefix or thin-signature class;
6. local factor side and selected envelope stage.

For an exact parent class `sigma` and coarse target class `beta`, define

\[
q_{\sigma\beta}
=
\sum_{\tau:\pi(\tau)=\beta}
A^\omega_{\sigma\tau}.
\]

### Theorem CMR1328 -- PROVED

For every exact parent `sigma`, the vector `q_sigma` is the exact expected
coarse offspring row.  The sum over all coarse classes equals the expected total
number of same-owner new credits.

### Proof

The coarse fibres partition the exact offspring classes.  Sum the exact row over
each fibre, then over all fibres. ∎

## 4. Componentwise upper quotient

For coarse classes `alpha,beta`, define

\[
\boxed{
\widehat A_{\alpha\beta}
=
\max_{\sigma:\pi(\sigma)=\alpha}
q_{\sigma\beta}.
}
\]

Empty parent fibres are deleted.

### Theorem CMR1329 -- PROVED

Let `v>0` be a coarse vector and lift it to exact classes by

\[
u_\sigma=v_{\pi(\sigma)}.
\]

If

\[
\boxed{\widehat A v<v,}
\]

then

\[
\boxed{A^\omega u<u.}
\]

### Proof

For an exact parent `sigma` in coarse class `alpha`,

\[
(A^\omega u)_\sigma
=
\sum_\beta q_{\sigma\beta}v_\beta
\le
\sum_\beta\widehat A_{\alpha\beta}v_\beta
<
v_\alpha
=
u_\sigma.
\]

Thus the lifted exact inequality holds row by row. ∎

The componentwise maximum may be conservative, but it is always honest.

## 5. Host-uniform upper quotients

Let `H_alpha` be any finite family of exact hosts, states and targets assigned to
one coarse parent class `alpha`.  Allow the exact state family and feasible bank
to vary with the host.

### Theorem CMR1330 -- PROVED

If `widehat A_{alpha beta}` dominates the expected coarse offspring count for
every exact response row in every member of `H_alpha`, then

\[
\widehat A v<v
\]

is a single certificate valid for all those hosts.

### Proof

The proof of CMR1329 uses only rowwise domination.  It does not require the exact
rows to come from one common host or one common state family. ∎

This is the required logical form for inherited-coordinate line/height classes.

## 6. Weight-dependent deterministic policy selection

An exact class may have several feasible response laws.  For a proposed coarse
weight vector `v`, define the weighted cost of a law `mu` by

\[
C_v(\sigma,\mu)
=
\sum_\beta q_{\sigma,\mu,\beta}v_\beta.
\]

### Theorem CMR1331 -- PROVED

Suppose that for every exact class `sigma` there is at least one feasible law
satisfying

\[
\boxed{
C_v(\sigma,\mu)<v_{\pi(\sigma)}.
}
\]

Choose one such law by fixed-order tie breaking.  The resulting deterministic
row policy has an exact matrix `A^omega` whose lifted weight satisfies

\[
A^\omega u<u.
\]

Randomization among laws gives no additional existence power once `v` is fixed.

### Proof

Choose one strict law for each row and apply the exact row inequality.  If a
convex combination is strict, at least one component law is strict, as in
CMR1274. ∎

Thus certificate search may alternate between a weight vector and deterministic
bank-row selection.

## 7. Exact integer certificate format

Assume all selected response laws have rational probabilities.  Let `d_sigma` be
a common denominator for row `sigma`, and let `N_{sigma beta}` be the integer
coarse offspring total after multiplying by `d_sigma`.

### Theorem CMR1332 -- PROVED

The coarse strict row inequality is exactly

\[
\boxed{
\sum_\beta N_{\sigma\beta}v_\beta
<
d_\sigma v_{\pi(\sigma)}.
}
\]

After clearing the denominators of `v`, the complete certificate is a finite
system of strict integer inequalities.

### Proof

Multiply the rational expected row inequality by its positive row denominator,
then by a common positive denominator for the weights. ∎

This format is independently checkable without floating-point eigenvalues.

## 8. Exact-class and upper-quotient endpoint

### Corollary CMR1333 -- PROVED

At every same-owner diagonal block:

1. complete state--target pairs give a finite exact credit system;
2. every rational response policy gives an exact rational offspring matrix;
3. arbitrary line/height/rank/carry classes define exact coarse row sums;
4. componentwise worst-fibre rows give an honest upper quotient;
5. a positive upper-quotient certificate lifts to all exact states and hosts;
6. deterministic response laws suffice once the weight vector is fixed;
7. the certificate can be stored as strict integer inequalities.

Combined with CMR1322--CMR1325, proving one host-uniform upper quotient
subcritical for each same-owner geometric regime is sufficient for the complete
selected product and wall tree.  The remaining mathematical task is now to
choose the coarse classes so that existing line, primitive-height, quotient and
carry estimates make the upper quotient subcritical, rather than merely finite.

No all-`n` theorem is claimed.  Exact row construction, coarse fibre sums,
upper-quotient lifting, host-uniform domination, deterministic policy selection
and integer certificate conversion are checked in
[`scripts/verify_prime_power_exact_credit_upper_quotients.py`](../scripts/verify_prime_power_exact_credit_upper_quotients.py).
