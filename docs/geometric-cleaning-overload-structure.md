# Isolated-cell and exact factor-overload structure for residual latent sources

**Branch:** `research/geometric-cleaning`

GC2s--GC2v pay every fixed-target latent family satisfying aggregate private or
shared target-link capacity dominance.  The remaining cases are genuinely
source-free mass and explicit capacity overload.  This note identifies their
exact current-factor structure.

The source-free class is an isolated-cell rectangle star in the current syndrome
hypergraph.  The underweight classes admit canonical fractional demand matrices
in which every used current factor is overloaded by the same parameter.  Thus no
unclassified source-transfer residual remains.

## Current-factor hypergraph

Let `H_cur` be the current factor hypergraph.  Its vertices are current cells and
its hyperedges are current payable factors `Q`, each with capacity `omega_Q>0`
and rank at most `r`.

Fix a target cell `b`, distinct partner cells `u in U`, and rectangle corrections
`T_u` deleting `b,u`.  The latent witness for `T_u` has weight `lambda_u`.
Every current factor destroyed by `T_u` contains `b` or `u`.

Write

`Link(v)={Q:v in Q}`

and `C(v)=sum_(Q in Link(v)) omega_Q`.

For one partner, let `P_u={Q:u in Q, b notin Q}` and
`C_u=sum_(Q in P_u) omega_Q`.

## GC2w -- source-free corrections are exactly isolated deleted pairs -- PROVED

The correction `T_u` destroys no current factor if and only if

`Link(b)=emptyset` and `Link(u)=emptyset`.

### Proof

A current factor is destroyed exactly when it contains one of the deleted cells
`b,u`.  Thus no factor is destroyed exactly when neither deleted cell belongs to
any current factor. QED.

Consequently, if one source-free partner exists then the common target `b` is
isolated in `H_cur`.  A whole source-free partner family consists of distinct
isolated partner cells attached to the same isolated target.

## GC2x -- source-free mass is a current-syndrome-free rectangle star -- PROVED

Let `U_0` be a retained source-free family of total latent weight

`W_0=sum_(u in U_0) lambda_u`.

Then every deleted endpoint in `{b} union U_0` has current factor capacity zero,
and no positive current payment supported on a deleted endpoint can be assigned
to this family.

The exact residual certificate is therefore the weighted star

`(b,{u:u in U_0},{lambda_u})`

inside the isolated-cell set of `H_cur`, together with the original prospective
secant witnesses.

### Proof

Apply GC2w to every retained partner.  Any current source factor destroyed by the
correction would have to contain `b` or `u`, but both links are empty. QED.

This does not make the latent witness harmless.  It proves only that the witness
is purely prospective relative to the current syndrome and must enter a clean
anchor, arithmetic or alternating classifier rather than a current-factor
payment ledger.

## GC2y -- aggregate-private underweight gives exact factor overload -- PROVED

Fix `kappa>=1` and a family `U_p` such that every partner has `C_u>0` and

`lambda_u>kappa*C_u`.

For each incidence `Q in P_u`, define canonical private demand

`d_(u,Q)=lambda_u*omega_Q/C_u`.

Then:

1. partner `u` sends total demand `lambda_u`;
2. every exact factor `Q` used by at least one partner receives

   `D_Q=sum_(u:Q in P_u) d_(u,Q) > kappa*omega_Q`;
3. every factor receives demand from at most `r` distinct partners;
4. total factor demand is `sum_(u in U_p) lambda_u`.

### Proof

The partner total follows by summing capacities in `P_u`.  If `Q in P_u`, then

`d_(u,Q)=(lambda_u/C_u)omega_Q>kappa*omega_Q`.

Thus one incidence already overloads `Q`, and summing preserves the strict
inequality.  Every contributing partner is a distinct cell of `Q`, so there are
at most `r` contributors.  Double summation gives the total-demand identity.
QED.

Hence aggregate-private failure is not merely a shortage of one large source.
It produces an occurrence-faithful family of exact current factors, each with
demand/capacity ratio greater than `kappa`.

## GC2z -- target-link overload gives a uniform exact anchor overload -- PROVED

Let `F_b=Link(b)` have total capacity

`C_b=sum_(Q in F_b) omega_Q>0`.

For a target-only family of total latent weight `W_b` satisfying

`W_b>kappa*C_b`,

define factor demand

`D_Q=omega_Q*W_b/C_b` for `Q in F_b`.

Then every target-link factor satisfies

`D_Q>kappa*omega_Q`,

the total demand is `W_b`, and every demanded factor contains the same exact
anchor cell `b`.

### Proof

Divide the overload inequality by `C_b` and multiply by `omega_Q`.  Summing over
`F_b` gives total demand `W_b`.  Membership in `F_b` gives the common anchor.
QED.

Thus target-link failure is a uniform weighted overload of one exact current
factor star, not an arbitrary congestion pattern.

## GC2aa -- complete residual structure router -- PROVED

After GC2s--GC2v, every retained residual latent family has one of three exact
forms:

1. a source-free isolated-cell rectangle star from GC2x;
2. an aggregate-private exact factor-overload family from GC2y;
3. a common-target exact anchor-factor overload from GC2z.

In the overload branches every used current factor has demand/capacity ratio
strictly greater than `kappa`.  In the source-free branch every deleted endpoint
has current factor capacity zero.

### Proof

GC2v leaves only source-free, aggregate-private underweight and target-link
overload outcomes.  Apply GC2x, GC2y and GC2z respectively. QED.

The next GC theorem should exploit these structures: route isolated-cell stars to
clean prospective geometry, and feed the exact overloaded factor families into
GC4's labelled overload and Hall-deficiency machinery.  The source-transfer
classification itself is complete under the fixed-target model.

## Finite check

`scripts/verify_geometric_overload_structure.py` exhausts small rank-bounded
factor hypergraphs and weighted partner systems.  It checks the source-free
isolation equivalence, private demand identities, rank reuse, strict overload on
every used factor, uniform target-link overload and the three-way residual
partition.