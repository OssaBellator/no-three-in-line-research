# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  The branch has exact structural
and matching-bank reductions, but no theorem yet proves that every positive
minimum of the real-triple potential reaches zero.

The decisive honesty correction remains:

> finite response and structural descent are not the same as potential
> improvement.

A completion must exhibit an actual lower-potential response or an exact
weighted inequality that guarantees one.

## 2. What is structurally closed

The proved chain now contains finite canonical forms for:

1. inherited banks, Hall walls, closure envelopes and exchange ancestry;
2. primitive-height, line-clean, carry, token and cycle-erasure geometry;
3. exact rollback, SCC, protected/free, unit-wall and child products;
4. minimum-face restriction, host-representable contraction and loss ledgers;
5. target handoff, protected execution, loaded-line and star banks;
6. terminal blocker covers and small full-grid bases;
7. last-entering credit ownership and finite rational spectral certificates.

The complete owner system is a finite DAG.  Its reproduction matrix is block
upper triangular, so only the same-owner diagonal blocks require subcritical
certificates.

## 3. Exact same-owner probability law

For one target `e` and opposite matching `O`, use

\[
H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

After relabeling `O` to the identity and `e=(0,1)`, every compatible residual
prescription is assigned parameters

\[
(n,r,q,d,\varepsilon).
\]

The exact forbidden-board rook polynomial gives

\[
r_j=\binom qj+\varepsilon\binom{q-d}{j-1}
\]

and

\[
B_n(P)=
\sum_{j=0}^{n-r}(-1)^j
\left[\binom qj+\varepsilon\binom{q-d}{j-1}\right](n-r-j)!.
\]

Thus

\[
\Pr(P\subseteq R)=
\frac{B_n(P)}{D_n(n-2)/(n-1)}.
\]

There are only `O(n)` exact probability classes per rank.  Exact collateral
and unavailable-edge expectations are finite rook-class dot products.

## 4. Cross-line assignment is solved formally

Each candidate triple has one fixed entering owner before the response is
sampled.  For a response edge `a`, let `g_e(a)` be its conditional expected
owned collateral and `p_e(a)` its marginal.  Then

\[
\mathbb E N(R)=\sum_ap_e(a)g_e(a).
\]

The marginal matrix is doubly stochastic.  Therefore expected collateral is
one bipartite assignment cost, with exact dual

\[
\min\left\{
\sum_x\alpha_x+\sum_y\beta_y:
\alpha_x+\beta_y\ge g_e(x,y)
\right\}.
\]

A dual sum below the destroyed target load forces an improving response.  This
replaces independent line maxima by shared row/column potentials.

Moreover, every `g_e(a)` is computable without enumerating the bank:

\[
c_e(a)=
\sum_{r,q,d,\varepsilon,\eta}
C_e(a;r,q,d,\varepsilon,\eta)\pi_n(r,q,d,\varepsilon),
\qquad
g_e(a)=\frac{c_e(a)}{p_e(a)}.
\]

Here `eta` may record inherited height, line, prefix, quotient and carry data.

## 5. Lattice-capacity reduction

For primitive direction height `h`, define

\[
c_n(h)=
\max\left\{\left\lfloor\frac{n-1}{h}\right\rfloor-1,0\right\}.
\]

The exact owner-line identity gives

\[
\gamma_e(a,R)
\le
\frac12\sum_{b\in E_a(R)}c_n(h(a,b)).
\]

Using exact pair rook probabilities yields a conditional capacity star and

\[
g_e(a)\le\Gamma_e^{\rm elig}(a).
\]

The eligibility indicator is fixed before sampling: a response partner is
eligible exactly when it was in the old matching or follows the owner in the
absolute entering-edge order.

Directions with

\[
h>\frac{n-1}{2}
\]

have coefficient zero.  Thus the unresolved owner mass is supported only on
finitely many low-height directions.

## 6. Prime-power signature endpoint

At side `n=p^k`, every eligible owner-partner pair has one signature

\[
(t,s,\delta,H),
\]

where:

- `t` is fixed or response partner;
- `s=v_p(G)` is first-separation depth;
- `delta` is projective direction modulo `p`;
- `H` is dyadic primitive-height band.

For a fixed owner, at most

\[
2k(p+1)\bigl(1+\lfloor\log_2(n-1)\rfloor\bigr)
\]

classes occur.  A large eligible owner envelope forces one heavy class.  Some
actual response simultaneously realizes at least the ceiling of that class's
conditional mean.

All partners in the class occupy one prefix carry cell, separation depth,
projective direction and height band.  A fixed projective/height class has at
most

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2
\]

exact primitive directions, so the simultaneous class concentrates on one
real line through the owner.

## 7. Genuine remaining inequality

The remaining prime-power theorem is no longer an ownership, product,
matching-probability or independent-line problem.  It is:

> compare the target-credit weight removed by an owner response with the
> weighted offspring produced after executing the forced heavy carry-cell fan
> or loaded real line.

A successful statement must populate a host-uniform same-owner upper quotient
and produce an exact certificate

\[
Av<v.
\]

The existing loaded-line, star, protected-core, prefix, carry-cell and token
responses give the available structural actions.  What is missing is a single
quantitative weighting that makes their offspring subcritical.

## 8. Recommended next lemmas

1. **Heavy-signature response row.**  Starting from the class forced by
   CMR1458--CMR1461, calculate the exact destroyed-credit and created-credit
   vector after loaded-line or carry-cell execution.
2. **Carry-cell Lyapunov weights.**  Choose weights by separation depth, prefix
   occupancy and height so deeper transfer or dispersed cells have strictly
   smaller total weight.
3. **Loaded-line assignment payment.**  Use the shared owner edge and protected
   absorption to avoid charging one entering edge independently on every line.
4. **Exact diagonal certificate.**  Search and then prove a rational/integer
   `Av<v` certificate for the resulting finite classes.
5. **Prime-field and thin blocks.**  Replace missing nonroot prefix depth with a
   direct finite direction/line certificate.
6. **CRT assembly.**  Retain collision/local-line types in each local diagonal
   block and glue through the already-proved owner triangularity.

## 9. Computational priorities

- Enumerate exact owner/rook/signature rows in inherited coordinate sets.
- Record the full offspring vector, not only total `(L,N)`.
- Solve rational linear programs for candidate class weights and export strict
  integer inequalities.
- Measure loaded-signature execution gain by separation depth and prefix cell.
- Test thin and prime-field owner blocks independently before CRT gluing.

## 10. Current proved endpoint

Through **CMR1461**:

- exact prescription probabilities use finite rook classes;
- exact collateral is one shared-edge assignment cost;
- every owner weight is a closed geometric/rook dot product;
- harmonic and integer lattice-capacity pair envelopes are proved;
- high-height directions vanish from the capacity envelope;
- eligible low-height pairs occupy finitely many prime-power carry signatures;
- a heavy signature is simultaneously realized and concentrates on one line.

There is still no complete proof.  The next genuine advance is a subcritical
weighted response row for that loaded signature, not another recurrence or
matching-existence theorem.
