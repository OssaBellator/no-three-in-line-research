# Finite AN-address extraction and fixed-collateral feedback

**Branch:** `research/geometric-cleaning`

GC2eq--GC2eu reduce every surviving exact-certificate bank to first-destruction payment, a paid
endpoint-disjoint current star, explicit AN descent, aggregate fixed-switch collateral or one exact
prospective certificate.  Two finite interfaces remain visible there: obtaining the declared
`rho`-fraction one-block AN substar, and replacing aggregate fixed-switch collateral by one physical
certificate.

This note closes both interfaces under explicit finite address contracts.  A canonical AN block
address retains a `1/K_AN` fraction of the paid star.  Fixed-only collateral then collapses to one
exact certificate, and every exact feedback output re-enters the existing occurrence-faithful lineage
and finite-signature recycling machinery.

## Finite AN-address model

Fix a paid endpoint-disjoint current star `S` of total occurrence-faithful weight `A_star`.  Let `B_AN`
be a finite ordered set of **AN block addresses**, with

`K_AN=|B_AN|>=1`.

An address records every field needed for one common one-block neutralization:

- the current-star role and anchor orientation;
- the moved block and matching channel;
- the designated source positions;
- the fixed preparation pattern;
- the block size `t>=7`;
- and the complete local legality and certificate-list context.

Assume the **AN address coverage contract**:

1. every current star lineage `Q in S` has a nonempty set `B(Q) subset B_AN` of legal addresses;
2. assigning several endpoint-disjoint lineages to the same address gives one occurrence-faithful
   substar destroyed by the address's common matching family;
3. the forbidden-position degree and all row, column, layer and hard-context constraints remain those
   required by AN1--AN4;
4. exact aliases are aggregated before weights are assigned;
5. failure returns the least uncovered lineage, block, role, channel, preparation or context field.

Assign each lineage to the least address in `B(Q)`.

## GC2ev -- canonical AN-address extraction -- PROVED

One address fibre has source weight at least

`A_star/K_AN`.

Therefore the current-star execution contract of GC2es holds with

`rho=1/K_AN`

for that fibre.

### Proof

The canonical fibres partition the occurrence-faithful star weight because every lineage has a
nonempty address set and is assigned once.  There are at most `K_AN` fibres, so a heaviest fibre has
weight at least their total divided by `K_AN`.  Item 2 of the coverage contract makes that fibre one
legal common AN substar. QED.

No probabilistic averaging is used in this extraction.

## Fixed-only collateral dictionary

For the chosen AN address, let the deterministic fixed preparation create an alias-aggregated family
`P_fix` of exact fixed-only rank-three certificates.  Assume:

- `|P_fix|<=K_fix`, where `K_fix>=1`;
- certificate `p` has weight `f_p>=0`;
- it is absent before the fixed preparation, present afterwards, and remains present in every matching
  state because it uses no moved matching cell;
- the aggregate fixed-switch collateral is exactly

  `F_fix=sum_(p in P_fix) f_p`;

- failure returns the least fixed operation, exact certificate, alias, persistence, label or context
  field.

## GC2ew -- aggregate fixed collateral collapses to one exact certificate -- PROVED

If `F_fix>0`, one exact fixed-only certificate has weight at least

`F_fix/K_fix`.

It is a genuinely realized current occurrence after the fixed preparation and may immediately receive
one lineage tag.

### Proof

At most `K_fix` nonnegative exact certificate weights sum to `F_fix`, so one is at least the average.
The fixed-only persistence clause makes that certificate present in every subsequent matching state.
Its first physical creation is therefore available for occurrence-faithful lineage tagging. QED.

This is a physical certificate statement, not merely a decomposition of a scalar cost.

## GC2ex -- finite-address installed-bank execution bounds -- PROVED UNDER THE ADDRESS CONTRACTS

Use the notation of GC2eq--GC2eu:

`Delta_cap=L_cert*(N^2-2)`

and

`K_tri=binom(N^2,2)`.

For every `epsilon in (0,1)`, an installed bank of birth weight `W_B` has one continuation:

1. first-destruction payment at least `W_B/2`;
2. failure of the finite decoration or AN address coverage contract;
3. one matching state decreases `Phi` by more than

   `3*epsilon*W_B/[2*K_AN*N^2*(2Delta_cap-1)]`;

4. one exact fixed-only certificate has weight greater than

   `3*(1-epsilon)*W_B/
    [4*K_AN*K_fix*N^2*(2Delta_cap-1)]`;

5. one exact matching-dependent prospective certificate has weight greater than

   `(1-epsilon)*W_B/
    [512*K_AN*N^2*(2Delta_cap-1)*K_tri]`;

6. or one matching, occurrence, inventory, alias, lineage, context or outer-reset field fails.

### Proof

GC2ev supplies a legal AN source of weight

`a>=A_star/K_AN`.

Substitute `rho=1/K_AN` into GC2es to obtain alternative 3.

If the margin fails, GC2et gives either

`F_fix>(1-epsilon)*a/2`

or one matching-dependent exact certificate of weight greater than

`(1-epsilon)*a/(768*K_tri)`.

For the fixed branch, GC2ew loses at most `K_fix`.  Use the strict star bound

`A_star>3W_B/[2N^2(2Delta_cap-1)]`

to obtain alternative 4.  The same substitution and `3/(2*768)=1/512` give alternative 5.  All
remaining outputs are the named contract failures. QED.

The two exact-certificate alternatives have different physical origins but enter the same lineage
interface after realization.

## GC2ey -- exact feedback signature import -- PROVED UNDER THE SIGNATURE-RECYCLING CONTRACT

Suppose every exact certificate output of GC2ex belongs to a fixed finite physical signature universe
`P`, with capacities `c_p`, fixed weights and finite context alphabet `X`.  Suppose further that any
successive feedback segment which destroys and recreates only tagged outputs is signature-Markov in
the sense of GC2cs.

Then the active feedback state stock is at most

`N_fb=|X|*prod_(p in P)(c_p+1)`.

Every feedback history with at least `N_fb` tagged-only transitions contains a canonical recycling
cycle.  Under the GC2cw cycle contract, such a segment erases, descends, spends a finite exact ticket or
leaves by an outer reset.

### Proof

Tag each fixed-only output at its deterministic creation and each matching-dependent output when its
realizing matching state is installed.  The hypotheses are exactly the fixed signature, capacity and
signature-Markov assumptions of GC2cs--GC2cw.  Apply GC2ct for the state stock and GC2cv--GC2cw for
cycle extraction and closure. QED.

A segment that destroys an untagged current factor is not tagged-only; it returns to the ordinary
first-destruction or potential-descent ledger instead.

## GC2ez -- finite-address current-star continuation -- PROVED UNDER THE DECLARED CONTRACTS

Every surviving exact-certificate bank has one nested continuation:

1. at least half its birth weight is first-destruction payment;
2. one exact finite-decoration, AN coverage, fixed-certificate or execution field fails;
3. a quantified current-star matching descent occurs;
4. one quantitatively heavy exact fixed-only or matching-dependent certificate is physically realized
   and re-enters the lineage router;
5. a tagged-only feedback epoch closes through the finite signature quotient;
6. or the history leaves through untagged destruction, a well-founded descent or an outer reset.

### Proof

Use GC2ex.  Alternatives 4 and 5 there are occurrence-faithful exact physical certificates after their
respective realization steps, so GC2eg--GC2ep installs and tracks them.  Apply GC2ey whenever the
subsequent feedback segment is tagged-only.  Every excluded case is one of the named failures or
non-tagged exits. QED.

## Corrected GC frontier

A paid current star no longer needs an externally supplied numerical `rho` once every lineage has one
address in a finite complete AN dictionary.  Aggregate fixed-switch collateral likewise becomes one
exact physical certificate, and finite-capacity tagged feedback reduces to the existing signature
quotient.

The remaining geometry is proof of AN address coverage for every physical current-star role, payment
or neutralization of the resulting heavy exact feedback certificate outside tagged-only epochs,
block-tuple overload recursion, unbounded decoration or lineage contexts, isolated-cell prospective
stars, pool depletion, global-context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_an_address_fixed_feedback.py` samples weighted current stars with nonempty
finite address sets, fixed-only exact certificate dictionaries, AN margin ledgers and finite feedback
quotients.  It checks the `1/K_AN` extraction, exact fixed-atom averaging, all integrated birth-weight
constants and the finite feedback-state repetition bound.
