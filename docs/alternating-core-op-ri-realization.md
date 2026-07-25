# Canonical orbit-phase realization of rational-inverse roles

**Branch:** `research/alternating-core-chain`

AC3ax requires an actual normalized rational-inverse component, complete fibres, and occurrence-dependent scale sets. The canonical orbit-phase geometry supplies those fields for every real two-channel source factor. This note imports the exact OP4g--OP4i identities, preserves current payment, and identifies the physical output as fixed-edge payment rather than completion-component payment.

## AC3ay -- one real two-channel factor gives an exact RI record -- PROVED FROM OP4g

Let

$$
P_x=(x,<a/x>_p),
\qquad
P_u=(u,<a/u>_p),
\qquad
B_z=(z,<b/z>_p)
$$

be a distinct really collinear factor with two points on `H_a` and one point on `H_b`. Put

$$
r=b/a,
\qquad
c=z/x,
\qquad
g=u/x.
$$

Then the factor carries the exact rational-inverse record

$$
g=F_r(c)=c(1-c)/(r-c),
$$

with companion root

$$
c^dagger=tau_r(c)=r(c-1)/(c-r),
$$

and

$$
F_r(c^dagger)=g,
\qquad
cc^dagger=rg.
$$

For every multiplicative subgroup `H`, its quotient labels

$$
A=cH,
\qquad
B=c^dagger H,
\qquad
C=gH,
\qquad
R=rH
$$

satisfy

$$
B=RCA^{-1}.
$$

The reverse same-channel orientation has

$$
c^-=c/g,
\qquad
g^-=g^{-1},
$$

and

$$
\{c^-,tau_r(c^-)\}=g^{-1}\{c,c^dagger\}.
$$

The occurrence also gives its actual base-scale coset

$$
S=xH,
$$

so its physical source, partner, and anchor cosets are exactly

$$
S,
\qquad CS,
\qquad AS.
$$

Finally, real collinearity gives one exact common cross-carry level

$$
kappa_z(x)=kappa_z(u).
$$

Thus a canonical real two-channel factor is arithmetically RI-realized with actual scale and carry provenance. No quotient-to-physical identification is guessed.

### Proof

All rational identities and the cross-carry equality are OP4g. The physical coset identities follow from `u=gx` and `z=cx`. QED.

## AC3az -- compatible orbit bicycle gives one normalized RI component -- PROVED FROM OP4h

Consider an orbit-phase implication bicycle whose source factors all have channel profile `2+1`. Apply the exact OP4h normalization audit.

One of the following occurs.

1. A three-channel factor is found and returns its mixed product-carry routes.
2. Two occurrences require different root cosets and return a root mismatch with full factor and carry provenance.
3. Literal propagation fails and returns a complete finite normalization conflict table.
4. One normalization succeeds. Every used literal receives one quotient label, every occurrence retains one exact ordered channel pair and rational image coset, and every directed occurrence satisfies
   $$
   A_{ell'}=RC_eA_{ell}^{-1}.
   $$

In outcome 4, selecting one fixed quotient edge produces one normalized order-two RI component whose occurrences all retain the AC3ay fields `(a,b,r,c,c^dagger,g,S)` and the exact cross-carry. Outcomes 1--3 remain explicit carry or consistency obstructions and are not called RI absorbers.

### Proof

This is the successful and failed output partition of OP4h, combined occurrence by occurrence with AC3ay. QED.

## AC3ba -- paid complete-fibre versus one-sided-fibre router -- PROVED

Let a factor-conservative paid occurrence family on one certified quotient edge have total weight `W`. Let `P` be the number of represented exact ordered channel pairs. Choose a heaviest channel-pair class of weight `W_0`. Then

$$
W_0\ge W/P.
$$

Inside this class, group occurrences by the exact rational fibre

$$
O(c)=(\{c,tau_r(c)\},F_r(c)).
$$

A fibre is complete when both roots are genuinely witnessed, with the usual one-root convention at a fixed point. Let `W_full` be the total occurrence weight supported on complete fibres and `W_one` the total occurrence weight supported on incomplete fibres.

Then one of the following paid outputs holds.

1. **Paid complete-fibre family:**
   $$
   W_full\ge W/(2P).
   $$
   Every represented fibre has both actual root witness sets, their base-scale coset sets, the fixed quotient edge, and exact carry provenance. This is the arithmetic input to AC3bc.
2. **Paid one-sided family:**
   $$
   W_one>W/(2P).
   $$
   Every represented incomplete fibre returns its witnessed root, image, missing companion root, actual base scales, source factors, and exact carry data.

If the active phase state uses at most `q_act` channels, then

$$
P\le q_act(q_act-1).
$$

Hence one output carries at least

$$
W/(2q_act(q_act-1)).
$$

### Proof

Exact channel-pair classes partition `W`, so the heaviest has weight at least `W/P`. Complete and incomplete fibres partition that class. One part carries at least half its weight. AC3ay supplies the retained fields; OP4i supplies the exact missing-companion convention and channel-pair bound. QED.

## AC3bb -- canonical AC3am-to-RI pre-pairing composition -- PROVED

Let an AC3am common-residual family have total paid weight `W_x`. Assume:

1. at most `R_0` arithmetic role labels;
2. secondary multiplicity threshold `rho>=1`;
3. the selected quotient role is realized by an OP4h-compatible two-channel family;
4. at most `P` ordered channel pairs occur in that role.

Then the role-pure family has weight at least

$$
W_role\ge W_x/(2R_0rho),
$$

with `rho` omitted in the fixed-exclusion and repeated-residual-pair outputs. AC3ba then returns either:

1. paid one-sided rational growth of weight at least
   $$
   W_x/(4R_0rho P),
   $$
   with every missing companion root explicit; or
2. a paid complete-fibre family of the same lower-bound scale, with both root occurrence measures and all actual base scales retained.

The complete side enters AC3bc--AC3be. It is not yet assigned to physical completion components.

### Proof

AC3am loses at most `2R_0rho`; channel-pair localization and the complete-versus-incomplete split lose at most `2P`. QED.

## Consequence for the RI adapter

For canonical orbit-phase quotient roles, the normalized RI component, complete-fibre relation, actual occurrence-dependent scale sets, exact cross-carry provenance, and factor-conservative payment are all supplied by proved OP interfaces.

AC3bc--AC3be then produce a coherent physical fixed-edge class at constant loss or one of the explicit incomplete-fibre, root-imbalance, or scale-dispersion outputs. AC3bf proves the coherent paid root cells are fixed by hyperbola completion, and AC3bg--AC3bj install the I6 bank directly through the common physical closure.

Thus canonical quotient arithmetic and scale pairing are no longer unresolved. The remaining frontier is arithmetic classification of the closed-bank collateral terms and the three explicit escape outputs.

## Finite check

`scripts/verify_ac_op_ri_realization.py` enumerates real two-channel factors over small primes, checks both rational normalizations, quotient-coset identities for every subgroup, actual base-scale cosets, cross-carry equality, and the paid complete/incomplete and composition routers.
