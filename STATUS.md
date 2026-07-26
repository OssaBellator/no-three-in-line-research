# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open.  This repository does **not** contain a complete proof.

The collision-free theorem ledger is split across

- `proofs/composite-modulus-theorem-index-live.md` through CMR747;
- `proofs/composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `proofs/composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `proofs/composite-modulus-theorem-index-live-continuation-3.md` from CMR1198.

## Structural normal forms

- Same-value host expansions roll back; lowering or infeasible-base expansions peel
  to added minimum-core contraction or strict improvement.
- Between contractions, normalized same-vertex-set hosts are nested decreasing.
- Minimum-core contraction is host-representable after conditioning the complete
  current cylinder on the common prescription.
- Exact protected/free, routing, unit-wall, essential-core, exchange-SCC and child
  products preserve original geometric coordinates.
- Cross-factor triples are constants, pure one-factor atoms, or low-rank Cartesian
  coupling boxes.
- Minimum-selected routing fixes one actual minimum skeleton immediately, so the
  selected path has no routing-recurrence branch.
- Inclusion-minimal response-bank blockers are exact deficiency-one unit Hall walls
  and factor into strict lower-side children.

These statements give finite response and structural descent.  They do not imply
that a positive minimum becomes zero.

## Exact fixed-target collateral expectation

Fix a selected target cell `e`, the opposite-layer matching `O`, and a disjoint
forbidden extension `F` containing `e`.  The response graph

\[
G=K_{n,n}\setminus(O\cup F)
\]

is `(n-2)`-regular.  Put

\[
\kappa_n=\left(\frac n{n-2}\right)^n\le16
\qquad(n\ge4).
\]

Van der Waerden gives

\[
|\operatorname{PM}(G)|
\ge n!\left(\frac{n-2}{n}\right)^n.
\]

A compatible rank-`r` prescription therefore has response-bank probability at
most

\[
\frac{\kappa_n}{(n)_r}
\qquad(1\le r\le3).
\]

If `V_r` counts genuinely new physical triples with residual response rank `r`,
then

\[
\mathbb E N(Q)
\le
\kappa_n
\left(
\frac{V_1}{n}
+
\frac{V_2}{(n)_2}
+
\frac{V_3}{(n)_3}
\right).
\]

Every response removes `e`, so it destroys at least its old target load `D_S(e)`.
Consequently

\[
\kappa_n\mathcal C(S;O,F)<D_S(e)
\]

is an actual strict-improvement criterion.

## Restricted-host penalty and target aggregation

If `b` allowed response edges are unavailable in the current host and `m=Phi(S)`,
then

\[
\kappa_n
\left(
\mathcal C(S;O,F)+\frac{(m+1)b}{n}
\right)<D_S(e)
\]

forces a feasible improving response.  The coefficient `m+1` ensures that a
negative weighted response cannot use an unavailable edge.

The exact target-incidence identity is

\[
\sum_{e\in E(S)}D_S(e)=3\Phi(S).
\]

Optimizing the bank score over extensions for each selected cell gives a finite
global criterion: if the optimized scores sum to less than `3Phi(S)`, one target
bank improves.

## Corrected line energy

Let `S=O union M`, let `M_G=M cap E(G)`, and on a real line `L` put

\[
o_L=|O\cap L|,
\quad
g_L=|G\cap L|,
\quad\m_L=|M_G\cap L|,
\quad
g_L^+=g_L-m_L.
\]

The exact new-collateral counts are

\[
V_1
=
\sum_L\binom{o_L}{2}g_L^+,
\]

\[
V_2
=
\sum_L
 o_L
\left(c_2(G_L)-\binom{m_L}{2}\right),
\]

\[
V_3
=
\sum_L
\left(c_3(G_L)-\binom{m_L}{3}\right).
\]

The subtraction is essential: an allowed response edge may already belong to the
old rematched layer, and triples wholly supported by old edges are not new
collateral.

Every new triple has one absolute last-entering labelled edge owner and one real
line owner.  Fixed-core cells contribute anchored geometry but receive no duplicate
owner charge; exact products assign each entering owner edge to one residual
factor.

## Pointwise local collateral envelope

For an allowed response edge `a`, let

\[
w_S(a)
=
\mathbf1_{a\notin M}
\sum_{L\ni a}\binom{o_L}{2}.
\]

Let `Delta_2(a)` and `Delta_3(a)` be the maximum local rank-two and rank-three new
collateral incidences over bank matchings containing `a`, and define

\[
\Lambda_S(a)
=
w_S(a)+\frac12\Delta_2(a)+\frac13\Delta_3(a).
\]

Every response matching satisfies the pointwise bound

\[
N(Q)\le\sum_{a\in R}\Lambda_S(a).
\]

Hence

\[
N(Q)\le
\mathcal R_\Lambda(G,S)
:=
\min\left\{
\sum_x\max_y\Lambda_S(x,y),
\sum_y\max_x\Lambda_S(x,y)
\right\}.
\]

If `mathcal R_Lambda(G,S)<D_S(e)`, every feasible response in that bank improves;
if the complete bank is blocked, it enters unit-wall descent.

Optimizing over host-feasible extensions gives `beta_H(e)`.  Unless some bank
improves or is blocked,

\[
\sum_{e\in E(S)}\beta_H(e)\ge3\Phi(S).
\]

Therefore one absolute entering edge has local envelope at least

\[
\frac{3\Phi(S)}{2n^2},
\]

forcing a quantitative rank-one, rank-two or rank-three loaded-line/secant-star
certificate.

## Last-creation credit ledger

Every current physical triple has a unique last creation time.  At that transition
it receives one physical owner cell from its least entering labelled edge.

- current potential is the number of live triple credits;
- destroyed triples retire their previous credits;
- created triples issue new credits;
- surviving triples keep their owner;
- removing an owner cell retires every live credit assigned to it;
- layer reassignment without physical absence creates no new credit.

Thus created collateral is immediately legitimate target load for a later response
through its owner cell.

## Reproduction-matrix frontier

At one finite canonical owner, partition live credits into finitely many classes.
Choose one feasible response law for each parent class and define

\[
A_{\sigma\tau}
=
\mathbb E N_\tau(Q).
\]

A positive vector gives strict weighted descent exactly when

\[
Av<v.
\]

For finite nonnegative matrices this is equivalent to

\[
\rho(A)<1.
\]

If `rho(A)<1`, an explicit weight is

\[
v=(I-A)^{-1}\mathbf1.
\]

A successful proof can be certified by exact rational or integer inequalities.
Such certificates tolerate bounded error and glue constructively across genuinely
block-upper-triangular product matrices.  For a fixed weight vector, rowwise
randomization is unnecessary: one deterministic bank row already satisfies every
strict convex-combination inequality.

No theorem yet constructs a globally valid upper offspring matrix with spectral
radius below one.

## Extension-free ambient response family

Varying the forbidden extension through a target cell has the exact union

\[
\bigcup_{F\ni e}
\operatorname{PM}(K_{n,n}\setminus(O\cup F))
=
\operatorname{PM}(K_{n,n}\setminus(O\cup\{e\})).
\]

The reverse inclusion follows because
`K_{n,n}\setminus(O\cup R)` is regular and every remaining edge belongs to a
perfect matching.  This form is appropriate for ambient lower-state searches and
lowering expansions.  Fixed-extension banks remain necessary for pointwise
collateral and blocker-wall arguments.

## Finite full-grid evidence and scope

On the **standard full grids**, and common-affine copies:

- side three has six physical states; every dirty target response is clean;
- every dirty side-four state has an ambient strict target response;
- every dirty side-five state has an ambient strict target response;
- at side six, 189476 dirty ordered states improve immediately, 1184 more escape
  after at most two equal target responses, and 24 ordered states form twelve
  feeder/two-cycle physical traps; the recorded CMF1 clean state gives a two-layer
  lowering expansion from those traps.

These are root/affine finite theorems only.  They do **not** apply by arbitrary
relabeling to scattered residual factors, because real collinearity remains in the
original parent coordinates.  For scattered factors, the inherited-coordinate
bank, local-envelope and spectral analysis remains necessary.

## Corrections retained

- Sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines and stars are not simultaneous families.
- One edge return may serve several neutralisations in one absence run.
- Removing one essential edge gives Hall deficiency exactly one.
- Aggressive batch deletion is branch-local.
- Differently masked leaf unions are not automatically one matching host.
- An empty intersection host has no assigned minimum.
- Conditioning on one support edge does not fix the other two layer labels.
- Static token membership is not restoration payment until an edge returns.
- Finite scheduler termination is not potential improvement.
- Allowed response edges already present in the old layer contribute no new
  rank-one collateral; old rank-two and rank-three subsets must also be subtracted.
- Standard-grid finite classifications do not transfer to scattered residual
  coordinates by relabelling.
- The side-six closed one-layer trap graph has six two-cycles and twelve one-step
  feeders, not fixed points.

## Current open frontier

1. **Subcritical offspring matrix.**  Construct honest line/height/carry and
   fixed-interface credit classes with an upper matrix satisfying `rho(A)<1`, or
   exhibit an exact rational vector `Av<v`.
2. **Product triangularity.**  Prove that last-entering ownership makes unit-wall,
   child and lifted-interface offspring matrices block triangular up to a bounded
   error absorbable by certificate slack.
3. **Prime-field and thin regimes.**  Establish the same certificate without a
   nonroot prefix-depth budget.
4. **Arbitrary side lengths.**  Complete CRT/balanced assembly while retaining
   collision/local-line credit classes.

## Bottom line

There is no complete proof.  Through **CMR1317**, fixed-target bank expectations,
restricted feasibility, corrected line energy, unique collateral ownership,
pointwise local envelopes, live-credit reproduction, exact spectral certificates,
extension-free response unions and standard-grid sides three through six have
precise normal forms.  The next genuine theorem must prove subcritical credit
reproduction in inherited coordinates; finite response and root-grid enumeration
are supporting evidence, not substitutes for that inequality.
