# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open.  This repository does **not** contain a complete proof.

The authoritative collision-free ledger is split across:

- `proofs/composite-modulus-theorem-index-live.md` through CMR747;
- `proofs/composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `proofs/composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `proofs/composite-modulus-theorem-index-live-continuation-3.md` through CMR1485.

CMR1414--CMR1461 was reindexed after concurrent work had occupied
CMR1374--CMR1413.  The concurrent chain was preserved.  CMR1462--CMR1469 was
also retained and corrected so matching side, envelope depth and inherited
coordinate span are not conflated.  Concurrent displacement routing occupies
CMR1470--CMR1477; the complementary private-path payment is CMR1478--CMR1485.

## Structural endpoint

The selected-minimum execution has finite canonical forms for rollback,
minimum-core contraction, nested hosts, selected routing, strict child
products, unit Hall walls, protected/free and exchange-SCC products,
fixed-core lifting, restoration ancestry, target banks and small-side bases.

Every new triple has one absolute last-entering owner.  Product, wall, host and
envelope exits form a finite owner DAG, so

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Only same-owner diagonal blocks still require subcritical certificates.
Structural finiteness does not imply that a positive minimum reaches zero.

## Exact matching-bank and owner law

For response side `d`, target `e` and opposite matching `O`, use

\[
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

After normalizing `O`, every compatible prescription has a finite exact rook
class.  Its completion count is

\[
B_d(P)=
\sum_{j=0}^{d-r}(-1)^j
\left[\binom qj+\varepsilon\binom{q-d_0}{j-1}\right](d-r-j)!,
\]

and

\[
\Pr(P\subseteq R)=
\frac{B_d(P)}{D_d(d-2)/(d-1)}.
\]

Every candidate triple has a fixed entering owner before sampling.  If

\[
p_e(a)=\Pr(a\in R),
\qquad
g_e(a)=\mathbb E[\gamma_e(a,R)\mid a\in R],
\]

then

\[
\mathbb E N(R)=\sum_ap_e(a)g_e(a).
\]

The marginal matrix is doubly stochastic, so expected collateral is one
bipartite assignment cost with an exact rational dual.  Owner weights are
finite geometric/rook dot products and require no perfect-matching enumeration.

## Inherited-coordinate capacity

A residual factor may use scattered coordinates.  Keep separate:

- matching side `d`;
- prime-power envelope side `t=p^k`;
- ambient coordinate span
  \[
  W_\omega=\max\{x_{\max}-x_{\min},y_{\max}-y_{\min}\}.
  \]

For primitive direction height `h`, define

\[
c_\omega(h)=
\max\left\{\left\lfloor\frac{W_\omega}{h}\right\rfloor-1,0\right\}.
\]

Then every entering owner satisfies

\[
\gamma_e(a,R)
\le\frac12\sum_{b\in E_a(R)}c_\omega(h(a,b)).
\]

Exact pair rook probabilities give a conditional eligible envelope
`Gamma_e^{elig}(a)` with

\[
g_e(a)\le\Gamma_e^{\rm elig}(a).
\]

Directions of height above `W_omega/2` contribute zero.

## One-owner and fractional prime-power signatures

Inside envelope `p^k`, every eligible pair has one signature

\[
(t_{\rm pair},s,\delta,H),
\]

where `s` is first-separation depth, `delta` projective direction modulo `p`,
and `H` dyadic primitive-height band.  Put

\[
B_\omega=1+\lfloor\log_2\max\{1,W_\omega\}\rfloor.
\]

At most `2k(p+1)B_omega` classes occur for one owner.  A heavy owner class is
simultaneously realized and concentrates on one loaded real line.

For a feasible fractional candidate packing, the total eligible incidence is
twice the packing mass.  Matching preclusion gives a signature class of mass
at least

\[
\frac{d-2}{3k(p+1)B_\omega}.
\]

After primitive-direction and signed-scale pigeonholing, one exact displacement
class has mass at least

\[
M_0=
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)},
\]

where

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2,
\qquad
S_{\omega,p}(s,H)=
\left\lfloor\frac{W_\omega}{p^sH}\right\rfloor.
\]

The class is a bank of parallel translated owner-partner pairs with one exact
lattice displacement.

## Weighted displacement carry routing

Every exact-displacement incidence has endpoints in one depth-`s` full prefix
cell and in two fixed distinct depth-`s+1` child cells.  Among at most
`p^{2s}` full cells, one carries mass at least

\[
\frac{M_0}{p^{2s}}.
\]

Using the third cell of each candidate as a witness gives an exact weighted
internal/crossing split.

- **Internal branch:** mass at least
  \[
  \frac{M_0}{2p^{2s}}
  \]
  scales injectively to a strict envelope of side `p^{k-s}` when `s>=1`.
- **Crossing branch:** for `s>=1`, one common earlier exit depth `c<s` carries
  mass at least
  \[
  \frac{M_0}{2sp^{2s}}.
  \]
- **Depth zero:** all incidences remain at parent scale.

For fixed structural owner, layer, depth, direction and displacement, there are
exactly `p^{2s}` full-cell tokens.  Across repeated banks, total mass either
consumes fresh tokens or concentrates on one exact absolute token.

## Private path and residual-token payment

For one fixed nonzero displacement, the directed support

\[
a\longmapsto a+\Delta
\]

is a finite path forest.  Alternating its arcs extracts at least half the packed
mass on endpoint-disjoint owner-partner pairs.  Since packed mass on one ordered
pair is at most one, a class of mass `mu` contains at least

\[
\boxed{\lceil\mu/2\rceil}
\]

private pairs.  Their residual supports are pairwise disjoint: one owner edge
per pair in the fixed-partner branch and both endpoints in the response-partner
branch.  Any residual blocker meeting every pair must therefore spend at least
one distinct response edge per pair.

Applied after weighted carry routing, this gives at least

\[
\boxed{\left\lceil\frac{M_0}{4p^{2s}}\right\rceil}
\]

private pairs in the strict internal branch,

\[
\boxed{\left\lceil\frac{M_0}{4sp^{2s}}\right\rceil}
\]

in the earlier-exit branch, and

\[
\boxed{\lceil M_0/2\rceil}
\]

at depth zero.  At nonroot depth the private pairs partition exactly by full
prefix token.  They give either one token containing many private identical-
displacement pairs or many pairwise token-disjoint private witnesses.

## Corrections retained

- Sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines and stars are not simultaneous families.
- One edge return may serve several neutralizations in one absence run.
- Removing one essential edge gives Hall deficiency exactly one.
- Aggressive batch deletion is branch-local.
- Differently masked leaf unions are not automatically one matching host.
- Conditioning on one support edge does not fix the other two layer labels.
- Finite scheduler termination is not potential improvement.
- Old response edges and old subsets create no new collateral.
- Standard-grid classifications do not transfer to scattered residual
  coordinates.
- Geometric capacities and displacement stocks use `W_omega`, not `d`.

## Current open frontier

1. **Strict transfer weights.**  Assign Lyapunov payment to internal scaling and
   earlier-depth crossing transfer.
2. **Private residual payment.**  Compare the CMR1484 private-edge/token cost
   with destroyed parent credit and protected-reserve depletion.
3. **Depth-zero and repeated-token payment.**  Pay parent-scale exact
   translations or repeated absolute full-cell tokens through prefix return or
   quotient/carry collision.
4. **Packed-versus-loaded comparison.**  Compare global routed/private payments
   with the one-owner loaded-line gain and encode a host-uniform rational or
   integer certificate `Av<v`.
5. **Prime-field/thin and CRT endpoints.**  Prove remaining diagonal blocks and
   glue through owner triangularity.

## Bottom line

There is no complete proof.  Through **CMR1485**, matching probabilities,
canonical owner weights, inherited-coordinate capacity, loaded signatures,
fractional exact-displacement banks, weighted carry routing and private
residual-edge/token payment are exact.  The remaining obstruction is the
Lyapunov comparison of strict transfer and private reserve consumption with the
parent credit weight, together with the depth-zero and repeated-token branches.
