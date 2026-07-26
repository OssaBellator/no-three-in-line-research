# Excess-demand import from latent factor overloads into GC4 structure

**Branch:** `research/geometric-cleaning`

GC2w--GC2aa classify every fixed-target latent residual as an isolated-cell
star or an exact current-factor overload.  This note converts the overload
branches into the weighted anchor-link language of GC4.

The correct structural weight is not the full artificial demand.  It is the
strict excess above the declared capacity multiple `kappa`.  That excess is
positive on every used factor and sums exactly to the corresponding aggregate
dominance failure.  It is an overload-demand weight attached to an exact
current factor, not factor-conservative paid mass.

## Private-overload excess

Fix an aggregate-private underweight partner `u`.  Its private source pool is

`P_u={Q:u in Q, b notin Q}`,

with total capacity

`C_u=sum_(Q in P_u) omega_Q>0`

and latent weight `lambda_u>kappa*C_u`.  GC2y defines

`d_(u,Q)=lambda_u*omega_Q/C_u`.

Define the factor excess

`e_(u,Q)=d_(u,Q)-kappa*omega_Q`.

## GC2ab -- private excess is positive and has an exact total -- PROVED

For every `Q in P_u`,

`e_(u,Q)>0`,

and

`sum_(Q in P_u) e_(u,Q)=lambda_u-kappa*C_u`.

### Proof

The strict underweight inequality gives
`lambda_u/C_u>kappa`, so multiplying by `omega_Q>0` proves positivity.
Summing the definition over `P_u` gives

`lambda_u-kappa*sum_(Q in P_u)omega_Q=lambda_u-kappa*C_u`. QED.

Thus every underweight partner carries a genuine positive overload-demand star
in the current factor hypergraph, anchored at the exact current cell `u`.

## Target-link excess

For a target-only overload, let

`F_b=Link(b)`, `C_b=sum_(Q in F_b)omega_Q>0`

and `W_b>kappa*C_b`.  GC2z defines

`D_Q=omega_Q*W_b/C_b`.

Set

`e_(b,Q)=D_Q-kappa*omega_Q`.

## GC2ac -- target-link excess is positive and has an exact total -- PROVED

For every `Q in F_b`,

`e_(b,Q)>0`,

and

`sum_(Q in F_b)e_(b,Q)=W_b-kappa*C_b`.

Every factor in this excess family contains the same exact target anchor `b`.

### Proof

The ratio `W_b/C_b` is strictly larger than `kappa`.  Multiply by each
`omega_Q` for positivity and sum over `F_b` for the total identity. QED.

## Rank split

Let an excess anchor family at a cell `v` consist of current factors of ranks at
most `r`, with positive excess weights `e_Q` and total excess

`E_v=sum_Q e_Q`.

For `1<=s<=r`, let `E_v^(s)` be the excess carried by rank-`s` factors.

## GC2ad -- one exact rank carries a `1/r` excess fraction -- PROVED

Some rank `s` satisfies

`E_v^(s)>=E_v/r`.

If `s<3`, the output is an exact lower-rank current overload certificate at
anchor `v`.  If `s=3`, the selected factors form a weighted three-uniform
anchor link to which GC4c applies directly.

### Proof

The rank classes partition the positive excess weight.  Weighted pigeonhole
gives the displayed bound.  Every selected factor still contains `v`. QED.

For the geometric-cleaning application `r<=3`, so the only alternatives are a
rank-one/rank-two concentration or a rank-three GC4 input.

## GC2ae -- rank-three overload imports to the GC4 anchor-link dichotomy -- PROVED

Fix `Delta>=1`.  Suppose the rank-three class is selected in GC2ad.  Then one of
the following holds:

1. some exact pair `{v,x}` belongs to more than `Delta` selected current factors;
2. there is a family `S_v` of selected rank-three factors, pairwise disjoint
   outside `v`, carrying excess-demand weight at least

`E_v/[r*(2*Delta-1)]`.

### Proof

GC2ad gives rank-three excess at least `E_v/r`.  Apply the weighted anchor-link
lemma GC4c to the simple rank-three current-factor hypergraph through `v`, using
excess weights `e_Q`.  Its pair-concentration alternative gives route 1; its
matching alternative retains a `1/(2*Delta-1)` fraction of the selected rank
weight, proving route 2. QED.

The weights are occurrence-faithful overload demand attached to exact current
factors.  GC4c accepts arbitrary nonnegative weights and therefore applies
without further geometry.  However, the excess may exceed factor capacity and
is not itself a paid reopening resource.  Entering GC4f--GC4i still requires a
capacity-normalized allocation or use of the excess as a Hall-deficiency
certificate.

## GC2af -- complete overload continuation router -- PROVED

Every private or target-link capacity overload from GC2aa has one exact
continuation:

1. a lower-rank current-factor excess concentration retaining at least `1/r` of
   its anchor excess;
2. a pair-codegree concentration in the rank-three current link;
3. an endpoint-disjoint rank-three overload-demand star retaining at least
   `1/[r(2*Delta-1)]` of the anchor excess.

For a private underweight partner the anchor excess is

`E_u=lambda_u-kappa*C_u`.

For a target-link overload it is

`E_b=W_b-kappa*C_b`.

### Proof

Use GC2ab or GC2ac to construct the positive exact excess family, then apply
GC2ad and GC2ae. QED.

## Corrected GC frontier

The fixed-target source-transfer residuals now terminate at explicit geometric
objects:

- source-free mass is an isolated-cell prospective rectangle star;
- every capacity overload has positive exact demand excess on current factors;
- rank-three excess enters the structural GC4c anchor-link dichotomy;
- lower-rank or high-pair outputs are already concentrated certificates.

The next geometric step is to turn the endpoint-disjoint demand stars into an
explicit weighted Hall-deficiency or capacity-normalized paid family before
running GC4f--GC4k.  The geometric localization of overload demand is closed;
its payment conversion is not.

## Finite check

`scripts/verify_geometric_overload_anchor_import.py` exhausts small rank-bounded
factor stars with rational capacities and demands.  It checks positivity and
exact excess totals, the rank split, pair-codegree alternative and weighted
endpoint-disjoint extraction bound.
