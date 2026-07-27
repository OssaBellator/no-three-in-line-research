# Product execution of compatible prospective line-cell witnesses

**Branch:** `research/geometric-cleaning`

GC2dm--GC2dq aggregate cross-star bridge, chord and transversal failures into one occurrence-faithful
compatible witness family.  Each witness records an exact block tuple, non-axis line, repeated moved
cell and physical role.  The remaining execution question is whether the prospective local
neutralizations attached to several compatible witnesses can be carried out together without
creating an unrecorded cross term.

This note gives the exact product law.  Under a local-realization and certificate-completeness
contract, compatible witness operations have disjoint source occurrences, independent local choices
and additive expected potential change.  A uniform local margin therefore survives with no further
bank-size loss.

## Compatible witness operations

Let `I` be a compatible witness family returned by GC2do.  Give witness `v` occurrence-faithful weight
`a_v>0`, and put

`A=sum_(v in I) a_v`.

For each `v`, assume a finite nonempty local choice family `Omega_v`.  Every local choice acts only on
the moved blocks and declared fixed support of `v`.

Let:

- `d_v` be current source weight destroyed by every local choice;
- `f_v` be the fixed-switch potential cost of preparing the local move;
- `c_v(pi_v)>=0` be the new local collateral produced by choice `pi_v`;
- `e_v=E_(pi_v in Omega_v)[c_v(pi_v)]`.

Assume the **compatible-witness execution contract**:

1. compatible witness vertices have pairwise disjoint moved star blocks;
2. their exact destroyed source occurrences are disjoint;
3. every local choice remains legal after all other compatible local choices and fixed switches;
4. every prospective certificate meeting two different local moved supports is represented by a
   conflict cause in the GC2dn graph;
5. every remaining new certificate is assigned to exactly one local witness list;
6. the current/prospective and lineage status of every source and created occurrence is explicit;
7. failure of any item returns its least exact block, line, cell-role or global-context field.

Because `I` is compatible, item 4 implies that no declared cross-support certificate survives inside
the selected family.

Choose local states independently from

`Omega_prod=prod_(v in I) Omega_v`.

## GC2dr -- simultaneous legality and source destruction -- PROVED

Every product choice is a legal combined operation.  Its destroyed current source weight is exactly

`D_I=sum_(v in I) d_v`.

No exact source occurrence is spent by two witness operations.

### Proof

Item 3 gives simultaneous legality.  Item 2 makes the local destroyed occurrence sets disjoint, so
their occurrence-faithful weights add exactly.  Operations on other compatible blocks cannot restore
or re-spend one of those named source occurrences by items 1 and 6. QED.

## GC2ds -- exact product expectation law -- PROVED

For the uniformly independent product choice, the expected total potential change is at most

`E[Delta Phi_I]<=sum_(v in I)(f_v-d_v+e_v)`.

If the local certificate lists use exact indicator expectations rather than upper bounds, equality
holds.

### Proof

The fixed preparation costs and destroyed current source terms add by GC2dr.  By items 4 and 5, every
new certificate belongs to one local list and depends on only one local random choice.  Its expectation
is therefore counted in exactly one `e_v`.  Sum the local contributions and use linearity of
expectation. QED.

The theorem is stronger than a union bound over witness pairs: under certificate completeness there is
no cross-witness expectation term at all.

## GC2dt -- summed local-margin descent -- PROVED

Define the local expected descent margin

`m_v=d_v-f_v-e_v`

and the total margin

`M_I=sum_(v in I)m_v`.

If `M_I>0`, some legal product choice lowers the cleaning potential by at least `M_I` relative to the
product average; in particular one product state satisfies

`Delta Phi_I<=-M_I<0`.

More generally, if every witness has

`m_v>=epsilon*a_v`

for one `epsilon>0`, then one product state decreases the potential by at least

`epsilon*A`.

### Proof

GC2ds gives `E[Delta Phi_I]<=-M_I`.  A finite average cannot be strictly below `-M_I` unless some state
is at most that value.  The uniform-margin statement follows from

`M_I>=epsilon*sum_v a_v=epsilon*A`. QED.

## GC2du -- exact local failure localization -- PROVED

Suppose no product state gives strict descent.  Then at least one exact witness `v` satisfies

`d_v<=f_v+e_v`,

or one field of the compatible-witness execution contract fails.

Thus failure of final product execution localizes to one exact tuple/line/cell witness and one of:

1. insufficient current source destruction;
2. excessive fixed-switch cost;
3. excessive local expected collateral;
4. local operation illegality;
5. an unlisted cross-support certificate;
6. or a current/prospective/lineage mismatch.

### Proof

If every local margin were positive, their finite sum would be positive and GC2dt would give a strict
descent state.  Therefore some local margin is nonpositive unless one of the hypotheses used by
GC2dr--GC2ds fails.  Record the least exact failed field in that case. QED.

This removes diffuse final-execution failure: it cannot remain a property of the whole compatible bank
without an exact local or cross-contract witness.

## GC2dv -- quantitative import from cross-tuple regularization -- PROVED UNDER THE LOCAL-MARGIN CONTRACT

Use the notation of GC2dq.  If the non-axis branch returns a compatible prospective family of weight
at least

`W/[2*N^2*ell_N*(2D_out+1)]`

and every selected witness has local margin at least `epsilon` times its occurrence-faithful witness
weight, then one combined cleaning state decreases the potential by at least

`epsilon*W/[2*N^2*ell_N*(2D_out+1)]`.

Otherwise the full cross-tuple branch returns one of:

1. axis collision mass at least `W/2`;
2. a block-tuple overload;
3. a bounded-cause or global-context failure;
4. one exact local witness violating the realization or margin contract.

### Proof

GC2dq supplies the compatible family and its retained weight.  Apply GC2dt and substitute the lower
bound.  Every alternative preceding compatible extraction, together with the exact local failure from
GC2du, is retained unchanged. QED.

## Corrected GC frontier

A compatible prospective cross-tuple witness family is now globally executable once each exact local
line/cell witness has a current source and a positive single-witness margin.  Product execution itself
introduces no additional loss and no diffuse cross term.

The remaining geometric work is therefore narrower:

- construct the local neutralization attached to each bridge, chord or transversal line/cell witness;
- prove a positive local margin or classify the exact failed local budget;
- feed block-tuple overload into labelled GC4 recursion;
- and handle high created-pair multiplicity, identity-sensitive or unbounded lineage recycling,
  isolated-cell prospective stars, pool depletion and global-context resampling.

## Finite check

`scripts/verify_geometric_compatible_witness_product_execution.py` enumerates and samples finite local
choice products with disjoint occurrence ledgers.  It checks exact product expectations, summed-margin
descent, local failure localization and the quantitative substitution from GC2dq.