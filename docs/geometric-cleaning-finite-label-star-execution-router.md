# Finite-label execution router for surviving current stars

**Branch:** `research/geometric-cleaning`

GC2el--GC2ep turn every installed exact-certificate bank into first-destruction payment, one high
current-pair multiplicity, or a paid endpoint-disjoint current star.  This note removes the pair
branch whenever the complete certificate decoration above one physical triple has a declared finite
stock, and then executes the paid star through the existing one-block matching neutralization.

The result is quantitative: after the survival and anchor losses, either one matching state descends,
one fixed-switch term is heavy, or one new exact prospective certificate retains an explicit fraction
of the original installed birth weight and re-enters the occurrence-faithful lineage router.

## Decorated current-certificate model

Fix one installed alias-aggregated exact-certificate bank of birth weight `W_B` on an `N x N` board,
with `N>=3`.  At a checkpoint write

`W_B=S_B+P_B`

as in GC2ei.

Assume the **finite decorated-triple contract**: in the fixed current context, every unordered
physical triple supports at most `L_cert>=1` complete exact certificate decorations.  A decoration
includes every label, role and context field that distinguishes two current certificate incidences.
Exact aliases of the same decorated physical occurrence are aggregated, and one decorated occurrence
has at most one current lineage.

Put

`Delta_cap=L_cert*(N^2-2)`.

For later exact completion bounds define

`K_tri=binom(N^2,2)`.

For `N>=3`, this dominates the rank-one, rank-two and rank-three completion stocks
`binom(N^2,2)`, `N^2` and `1` from GC2ef.

## GC2eq -- finite decorations cap every current pair multiplicity -- PROVED

For every current physical pair `{z,x}`, the number of surviving decorated exact-certificate
lineages containing that pair is at most

`Delta_cap=L_cert*(N^2-2)`.

### Proof

The third cell has at most `N^2-2` choices.  For each physical triple, the finite decorated-triple
contract allows at most `L_cert` complete addresses.  Alias aggregation and current-lineage
uniqueness permit at most one surviving lineage for each decorated address.  Multiply the two
stocks. QED.

If the displayed cap fails, one exact triple has more than `L_cert` current decorations or one alias,
context or lineage-uniqueness field fails.

## GC2er -- paid star with no high-pair alternative -- PROVED

At every checkpoint, either

`P_B>=W_B/2`,

or there is a paid endpoint-disjoint current star of weight `A_star` satisfying

`A_star>3W_B/[2N^2(2Delta_cap-1)]`.

### Proof

Apply GC2en with `Delta=Delta_cap`.  GC2eq excludes its high-pair alternative.  The remaining two
outputs are first-destruction payment and the displayed current-star bound. QED.

Every selected star member is already a current occurrence-faithful lineage.

## Current-star execution contract

Fix parameters

`rho in (0,1]`,

`epsilon in (0,1)`.

Assume the paid star from GC2er has an occurrence-faithful substar contained in one declared legal
AN matching block of size `t>=7`, with source weight

`a>=rho*A_star`.

Let:

- `F_fix` be the exact fixed-switch collateral;
- `T_r` be the complete prospective rank-`r` certificate inventory, for `r=1,2,3`;
- `E_AN=128*sum_(r=1)^3 T_r/(t)_r`;
- `D` be the exact current source weight destroyed by the matching state.

The single-star matching contract gives

`D>=a`

and

`E[Delta Phi]<=F_fix-D+E_AN<=F_fix-a+E_AN`.

Failure returns the least block, matching, occurrence, inventory, label, context or completeness
field.

## GC2es -- explicit current-star descent margin -- PROVED UNDER THE EXECUTION CONTRACT

If

`F_fix+E_AN<=(1-epsilon)*a`,

then one legal matching state satisfies

`Delta Phi<=-epsilon*a`.

Consequently the decrease is strictly greater than

`3*epsilon*rho*W_B/[2N^2(2Delta_cap-1)]`.

### Proof

The expectation is at most

`F_fix-a+E_AN<=-epsilon*a`.

Some matching state is no larger than its average.  GC2er and `a>=rho*A_star` give the strict
birth-weight bound. QED.

## GC2et -- failed margin localizes to fixed cost or one exact certificate -- PROVED

If the hypothesis of GC2es fails, then at least one of the following holds:

1. **heavy fixed switch**

   `F_fix>(1-epsilon)*a/2`;

2. **heavy exact prospective certificate:** one rank `r in {1,2,3}`, one ordered matching
   prescription and one exact completion give a prospective certificate `Q` of weight

   `h_Q>(1-epsilon)*a/(768*K_tri)`.

In terms of the installed birth weight, the two lower bounds are respectively

`F_fix>3(1-epsilon)rho W_B/[4N^2(2Delta_cap-1)]`

and

`h_Q>(1-epsilon)rho W_B/[512N^2(2Delta_cap-1)K_tri]`.

### Proof

Failure of GC2es means

`F_fix+E_AN>(1-epsilon)*a`.

If the first term exceeds half, use alternative 1.  Otherwise

`E_AN>(1-epsilon)*a/2`.

One of its three rank contributions satisfies

`128*T_r/(t)_r>(1-epsilon)*a/6`,

so

`T_r/(t)_r>(1-epsilon)*a/768`.

There are at most `(t)_r` ordered prescriptions.  One prescription therefore carries raw rank-`r`
weight greater than `(1-epsilon)*a/768`.  GC2ef has at most `K_tri` exact completions over that
prescription, so one exact prospective certificate has the displayed weight.

Finally substitute the strict GC2er star bound and `a>=rho*A_star`.  In the certificate branch,
`3/(2*768)=1/512`. QED.

The exact certificate from alternative 2 enters GC2eg--GC2ep with its complete matching prescription
and physical completion; it is not counted as current payment before installation.

## GC2eu -- finite-label installed-bank execution router -- PROVED UNDER THE DECLARED CONTRACTS

For every installed exact-certificate bank, one of the following nested continuations holds:

1. first-destruction payment is at least `W_B/2`;
2. the finite decorated-triple cap fails at one exact triple or context field;
3. no legal one-block AN substar of fraction `rho` and size at least seven is realized;
4. one current-star matching state decreases `Phi` by more than

   `3*epsilon*rho*W_B/[2N^2(2Delta_cap-1)]`;

5. one fixed-switch collateral term exceeds

   `3(1-epsilon)rho W_B/[4N^2(2Delta_cap-1)]`;

6. one exact prospective certificate has weight greater than

   `(1-epsilon)rho W_B/[512N^2(2Delta_cap-1)K_tri]`

   and re-enters the exact realization and lineage router;
7. or one matching, occurrence, inventory, label, alias, lineage, context or outer-reset contract
   fails at its least exact field.

### Proof

Use GC2eq--GC2er.  Apply the execution contract to the paid current star.  GC2es gives descent and
GC2et gives the two failed-margin branches.  The exact prospective output is installed and tracked by
GC2eg--GC2ep.  All excluded hypotheses are named contract failures. QED.

## Corrected GC frontier

A finite complete decoration stock eliminates the unstructured high current-pair branch.  The
surviving exact-certificate bank now gives first-destruction payment, explicit current-star descent,
a heavy fixed-switch term or one quantitatively heavy exact prospective certificate that re-enters
the lineage machinery.

The remaining geometry is construction of the declared `rho`-fraction AN block in every current-star
role, payment of heavy fixed-switch collateral, control of repeated certificate-feedback loops,
block-tuple overload recursion, unbounded decoration or lineage contexts, isolated-cell prospective
stars, pool depletion, global-context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_finite_label_star_execution.py` samples decorated exact-lineage banks,
survival checkpoints, finite triple-label dictionaries and weighted matching ledgers.  It checks the
`L_cert(N^2-2)` pair cap, the anchor-star constant, the descent margin, the fixed/certificate split,
rank-prescription collapse and the integrated birth-weight constants.