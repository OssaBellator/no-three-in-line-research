# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open.  This repository does **not** contain a complete proof.

The authoritative collision-free theorem ledger is split across:

- `proofs/composite-modulus-theorem-index-live.md` through CMR747;
- `proofs/composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `proofs/composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `proofs/composite-modulus-theorem-index-live-continuation-3.md` through CMR1509.

The CMR1414--CMR1461 range was reindexed after concurrent branch work.
Matching side, prime-power envelope side and inherited coordinate span are
kept distinct throughout the current endpoint.

## Structural and spectral endpoint

Every new physical triple has one absolute last-entering edge owner.
Product, wall, routing, host and envelope exits form a finite owner DAG.
After topological ordering, the complete offspring matrix is block upper
triangular:

\[
\boxed{\rho(A)=\max_i\rho(A_{ii}).}
\]

Only genuinely recurrent same-owner blocks require numerical subcriticality.
Finite structural descent alone is not potential improvement.

CMR1486--CMR1493 refine the owner DAG by recording envelope exponent,
first-separation depth, used absolute tokens and the monotone residual mask.
The following are strict off-diagonal transitions:

1. strict internal scaling;
2. handoff to an earlier exit depth;
3. first use of an absolute token;
4. first use of a private residual edge;
5. every ordinary owner, routing, wall, host or envelope exit.

Once the recurrent core blocks have rational certificates, all finite
off-diagonal collateral glues constructively into one certificate `Av<v`.
No separate contraction estimate is required for strict depth transfer or
first-use resources.

## Exact extension-free bank and owner law

For response side `d`, opposite matching `O` and target edge `e`, use

\[
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

Every compatible residual prescription has an exact finite rook class.
Every candidate triple has one canonical owner before the response is sampled.
If

\[
p_e(a)=\Pr(a\in R),
\qquad
g_e(a)=\mathbb E[\gamma_e(a,R)\mid a\in R],
\]

then

\[
\boxed{
\mathbb E N(R)=\sum_a p_e(a)g_e(a).
}
\]

The marginal matrix is doubly stochastic, so expected collateral is one
bipartite assignment cost with an exact rational dual.  Owner weights are
finite geometric/rook dot products and require no enumeration of all perfect
matchings.

## Inherited-coordinate capacity

A scattered residual factor keeps three separate parameters:

- matching side `d`;
- envelope side `t=p^k`;
- coordinate span
  \[
  W_\omega=
  \max\{x_{\max}-x_{\min},y_{\max}-y_{\min}\}.
  \]

For primitive direction height `h`, define

\[
c_\omega(h)=
\max\left\{
\left\lfloor\frac{W_\omega}{h}\right\rfloor-1,
0
\right\}.
\]

Every entering owner satisfies

\[
\boxed{
\gamma_e(a,R)
\le
\frac12
\sum_{b\in E_a(R)}c_\omega(h(a,b)).
}
\]

Exact pair rook probabilities give the conditional eligible owner envelope.
Directions above `W_omega/2` have zero capacity.

## Fractional packed signatures

Inside envelope `p^k`, every eligible owner-partner incidence has signature

\[
(t_{\rm pair},s,\delta,H),
\]

recording partner type, first-separation depth, projective direction and
dyadic primitive-height band.  Put

\[
B_\omega=
1+\left\lfloor
\log_2\max\{1,W_\omega\}
\right\rfloor.
\]

At a positive minimum, every subthreshold exempt family yields one signature
with packed incidence mass at least

\[
\frac{d-2}{3k(p+1)B_\omega}.
\]

After exact primitive-direction and signed-scale refinement, one displacement
class has mass at least

\[
\boxed{
M_0=
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)}
}
\]

with

\[
D_p(H)=
(p-1)\left\lceil\frac{4H}{p}\right\rceil^2,
\qquad
S_{\omega,p}(s,H)=
\left\lfloor\frac{W_\omega}{p^sH}\right\rfloor.
\]

The class is a weighted bank of parallel translated owner-partner pairs.

## Carry routing and private residual payment

CMR1470--CMR1477 route the exact-displacement mass through one depth-`s`
full-prefix cell.  They produce:

1. strict internal scaling of mass at least
   \[
   M_0/(2p^{2s});
   \]
2. one earlier exit depth, for `s>=1`, of mass at least
   \[
   M_0/(2sp^{2s});
   \]
3. the depth-zero parent branch;
4. or reuse of one absolute full-cell token.

CMR1478--CMR1485 show that a fixed translation support is a path forest.
Alternating its arcs extracts at least half the mass on endpoint-disjoint
pairs.  Their residual supports are disjoint, so a blocker meeting all of
them spends one distinct response edge per pair.

For a private matching of mass `mu_M` and current residual mask `F`,

\[
\boxed{
\max\{|F|,u_F\}\ge\mu_M/2,
}
\]

where `u_F` is the private mass whose residual supports avoid `F`.
Neutralising all unhit supports through this route requires at least
`ceil(u_F)` fresh residual edges.

The response host has exactly

\[
\boxed{|E(H_e)|=d^2-d-1}
\]

edges, so fresh private-edge episodes have a finite monotone stock.

At nonroot depth, private pairs give either one heavy identical-displacement
token or many token-disjoint witnesses.  First-use token episodes are also
finite because exactly `p^(2s)` absolute full-cell tokens exist at depth `s`.
Only repeated-token states remain recurrent.

## Depth-zero root channels

A depth-zero displacement is nonzero modulo `p`.  Fixing the owner's root
residue cell `r` determines:

- a distinct partner child cell `r'`;
- one exact quotient carry
  \[
  q(r)=\frac{r+\Delta-r'}p.
  \]

At most `p^2` root channels occur.  Some channel has mass at least

\[
\boxed{M_0/p^2}
\]

and its pairs are automatically endpoint-disjoint, with no parity loss.

After selected root routing, a fixed partner gives an anchored atom and a
response partner gives a cross-factor atom.  Every residual factor has local
rank at most two.  For `k>=2`, the owner factor has strict side `p^(k-1)`;
for `k=1`, the channel reaches side-one contraction or a fixed-interface
low-rank trigger.

Thus depth zero is no longer an anonymous parent-scale translation.  Its
remaining diagonal object is explicit recurrence of one root channel or
fixed interface.

## Packed versus loaded-owner currencies

For one exact displacement, an owner determines its unique partner.  The
packing constraint gives

\[
\boxed{m_\Delta(a)\le1}
\]

for every owner.

Let `L` be any owner set reserved for loaded-line execution.  Then

\[
\boxed{
\max\{|L|,\mu_{\bar L}\}
\ge
\mu_\Delta/2,
}
\]

where `mu_bar L` is exact-displacement mass on owners outside `L`.

Therefore either:

1. many distinct owners enter the loaded-line ledger; or
2. a quantitatively large translated private family remains on disjoint
   owners.

The second family retains all blocker, token, carry-routing and root-channel
payments.  Loaded-owner and private translated payments have disjoint
canonical owner support and can be added without inclusion-exclusion loss.

This closes only the overlap problem.  It does not yet calibrate either
payment against destroyed parent credit.

## Genuine current frontier

1. **Recurrent-core numerical certificate.**  Prove rational or integer
   contraction for repeated absolute tokens, reused residual supports,
   recurrent root channels/fixed interfaces and loaded-line owners.
2. **Credit calibration.**  Compare one unit of loaded-owner or private
   residual/token payment with destroyed parent credit.
3. **Prime-field and thin cores.**  Complete the fixed-interface and small
   scattered-factor diagonal inequalities.  Nonroot depth transfers are no
   longer present in the prime-field case.
4. **Host-uniform quotient.**  Export the recurrent-core inequalities as an
   exact rational or integer certificate `Av<v`.
5. **Balanced/CRT assembly.**  Retain collision and local-line credit classes
   while gluing the certified diagonal blocks.

## Corrections retained

- Sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines and stars are not simultaneous families.
- One edge return may serve several neutralisations in one absence run.
- Removing one essential edge gives Hall deficiency exactly one.
- Aggressive batch deletion is branch-local.
- Differently masked leaf unions are not automatically one matching host.
- Conditioning on one support edge does not fix the other layer labels.
- Finite scheduler termination is not potential improvement.
- Old response edges and old subsets create no new collateral.
- Standard-grid classifications do not transfer to scattered residual
  coordinates.
- Geometric capacities and displacement stocks use `W_omega`, not `d`.
- Strict transfers and fresh resources are off-diagonal only when the policy
  actually executes the canonical handoff or monotone payment.

## Bottom line

There is no complete proof.  Through **CMR1509**, exact response
probabilities, owner weights, inherited-coordinate capacity, packed
signatures, weighted displacement routing, private residual/token payment,
acyclic transfer gluing, root child channels and owner-disjoint
packed-versus-loaded bookkeeping are proved.

The unresolved obstruction is now numerical and recurrent: certify the
root/fixed-interface, repeated-resource and loaded-line cores against
destroyed parent credit, then complete the host-uniform quotient and CRT
assembly.
