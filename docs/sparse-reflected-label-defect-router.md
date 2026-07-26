# Balanced donor routing for reflected-label defects

**Branch:** `research/sparse-algebraic-spread`

SAS5z--SAS5ad show that a destruction record either has a valid mirror repair or
fails at one reflected board or label role.  A heavy reflected-label role is not
an arbitrary mismatch family: every defect column needs one fixed block label,
and the balanced colouring contains exactly `d` donor columns of that label.

This note converts diffuse reflected-label defects into a large bank of
pairwise-disjoint balance-preserving donor swaps.  It does not claim that the
whole bank is improving; cross-record geometric collateral is isolated by an
explicit conflict graph.

## Fixed reflected-label role

Fix one physical swap `{x,y}`, one destruction word, its mirror repair word, and
one failing non-swapped row position.  Every retained mirror record has:

- one reflected defect column `z`, distinct from `x,y`;
- one required block label `ell` at `z`;
- current label `kappa(z) != ell`;
- at most one other non-swapped scope column besides `z`.

Give each record nonnegative weight.  Let the colouring be balanced with exactly
`d` columns of every label.

## SAS5ae -- one required label retains a `1/b` fraction -- PROVED

If the fixed reflected-label role has total weight `W` and there are `b` block
labels, one required label `ell` carries weight at least

`W/b`.

### Proof

The required-label classes partition the role.  Weighted pigeonhole gives the
claim. QED.

Fix such a label and let `W_ell` be its weight.  Aggregate records by their defect
column.  Let `L(z)` denote the total weight at column `z`.

## SAS5af -- heavy defect column or many distinct defect columns -- PROVED

For every threshold `mu>0`, either:

1. one exact column-label address `(z,ell)` has `L(z)>mu`; or
2. the role uses at least

`ceil(W_ell/mu)`

 distinct defect columns.

### Proof

If every column load is at most `mu`, `k` distinct columns carry total weight at
most `k*mu`.  Rearranging gives the displayed bound. QED.

The first outcome is an exact recurrent balanced-colour discrepancy.  The
second is the diffuse case.

## Donor columns and safe transpositions

Let

`D_ell={q:kappa(q)=ell}`,

so `|D_ell|=d`.  Every defect column lies outside `D_ell`.

For a mirror record at defect column `z`, a donor `q in D_ell` is **locally
safe** when:

- `q` is not `x` or `y`;
- `q` is not the other non-swapped scope column of that record, when such a
  column exists.

Swapping the labels at `z,q` puts label `ell` at `z`, leaves the two original
swap columns unchanged, leaves every other column of that mirror record
unchanged, and preserves global label multiplicities.

Every record excludes at most three donors: `x`, `y`, and one other scope
column.

## SAS5ag -- diffuse defects give a disjoint donor-swap bank -- PROVED

Let `Z` be any set of `k` distinct defect columns for one required label `ell`.
There is a family of pairwise column-disjoint locally safe transpositions

`{z_i,q_i}`

of size at least

`min(k,(d-3)_+)`,

where every `z_i` is a distinct member of `Z` and every donor `q_i` is distinct.

### Proof

Order the defect records.  Greedily match them to unused donors.  Before the
`j`-th successful choice, at most `j` donors have been used and the current
record excludes at most three more.  As long as `j<d-3`, at least one donor
remains.  The process therefore reaches `min(k,d-3)` choices.  Defect columns
are not donor columns, so all transposition endpoints are distinct. QED.

Thus, in the diffuse alternative of SAS5af, the bank size is at least

`min(ceil(W_ell/mu),(d-3)_+)`.

## Cross-record conflict graph

A donor transposition chosen for record `Q_i` may still alter a column used by a
different mirror record `Q_j`.  Join two chosen transpositions when an endpoint
of either lies in the scope of the other's record.  An independent set gives a
simultaneously locally safe subbank.

Assume every column belongs to the scopes of at most `Delta` retained mirror
records.

## SAS5ah -- bounded incidence gives a compatible donor subbank -- PROVED

The cross-record conflict graph has maximum degree at most

`2*Delta+3`.

Consequently it has an independent set of size at least

`|B|/(2*Delta+4)`,

where `B` is the disjoint donor-swap bank from SAS5ag.

### Proof

A chosen transposition has two endpoint columns.  Each endpoint lies in at most
`Delta` retained record scopes, producing at most `2*Delta` conflicts through
other records containing its endpoints.  Its own record has at most three scope
columns, and because all chosen transpositions are endpoint-disjoint, at most
three other transpositions can use those columns as endpoints.  Hence the
maximum degree is at most `2*Delta+3`.  Greedy colouring with one more colour
gives an independent set of the stated size. QED.

The bound is deliberately safe; overlaps counted in both directions only make
the true degree smaller.

## SAS5ai -- reflected-label defect router -- PROVED

A reflected-label defect family of total weight `W` yields one of:

1. one required label class of weight at least `W/b` and one exact defect column
   of load greater than `mu`;
2. a pairwise-disjoint donor-swap bank of size at least

   `min(ceil(W/(b*mu)),(d-3)_+)`;
3. under column-scope incidence at most `Delta`, a simultaneously locally safe
   subbank of size at least the preceding quantity divided by `2*Delta+4`.

### Proof

Apply SAS5ae, then SAS5af.  The heavy case gives route 1.  In the diffuse case,
SAS5ag gives route 2, and SAS5ah gives route 3 under the incidence cap. QED.

## Corrected SAS6 frontier

Heavy mirror-label failure now has a precise continuation:

- a recurrent exact column-label discrepancy;
- a large bank of disjoint balance-preserving donor swaps;
- or, after a bounded-incidence audit, a compatible subbank which corrects the
  selected mirror literals simultaneously.

What remains is to compare the destroyed and repaired geometric weights of this
subbank and bound new collinear triples created through donor columns.  The
balanced-colour supply and first compatibility extraction are no longer open.

## Finite check

`scripts/verify_sparse_reflected_label_defects.py` exhausts small balanced
colourings, defect records and donor exclusions.  It checks the heavy/diffuse
column split, greedy donor matching, endpoint disjointness and the
`2*Delta+3` conflict-degree bound.