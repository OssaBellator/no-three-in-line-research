# Donor-reservoir coverage and concentrated blocker causes

**Branch:** `research/geometric-cleaning`

GC2fk--GC2fo neutralize one heavy current lineage whenever a nonempty legal balanced-donor menu is
available.  This note makes donor availability quantitative.  With one fixed target endpoint, the
rectangle cause-degree formulas of GC3j--GC3n give constant load for collision and line causes and at
most three times the support size for every target-disjoint bounded physical cause.

After those explicit physical budgets are exhausted, every donor shortage is forced through one
current-target-common hard atom or one global context/generator atom.

## Singleton-target donor model

Fix one heavy current lineage and one movable current endpoint `x` in a permutation layer.  Let `P` be
a candidate donor set of size

`p=|P|`,

with distinct donor rows and columns.  For each `u in P`, the balanced transposition of `x` with `u` is
either legal or receives one occurrence-faithful **least blocking cause**.

Partition the possible least causes into:

- `C_coll`: opposite-layer collision cells used only in inserted-cell roles;
- `C_line`: exact non-axis current or protected line atoms;
- `C_supp`: bounded physical-support atoms `q` with support `Q_q`, where `x notin Q_q`;
- `C_tgt`: bounded physical-support or hard atoms whose support contains `x`;
- `C_ctx`: global context or generator atoms not mediated by one bounded physical support or line.

The canonical cause fibres partition the illegal donors.  Assume all source, label, lineage, operation
and context fields needed to distinguish physical causes are included.  A missing field is returned
rather than merged into these cause classes.

Let `D` be the legal donor set and `d=|D|`.

## GC2fp -- singleton rectangle cause caps -- PROVED

For the singleton target set `{x}`:

1. every collision cause in `C_coll` blocks at most two donor assignments;
2. every exact non-axis line cause in `C_line` blocks at most two donor assignments;
3. every `q in C_supp` blocks at most

   `3|Q_q|`

   donor assignments.

### Proof

Use the rectangle assignment notation of GC3j with target-batch size `t=1` and partner set `P`.
Collision cells used only in inserted roles have degree at most two.  GC3l gives line degree at most
`2t=2`.  For `q in C_supp`, GC3k gives

`Delta(q)<=p|Q_q intersect {x}|+|Q_q intersect P|+2|Q_q|`.

The first term vanishes because `x notin Q_q`, and `|Q_q intersect P|<=|Q_q|`, giving `3|Q_q|`. QED.

## GC2fq -- explicit bounded-physical donor budget -- PROVED

Put

`D_phys=2|C_coll|+2|C_line|+3 sum_(q in C_supp)|Q_q|`.

At most `D_phys` candidate donors are canonically blocked by causes in
`C_coll union C_line union C_supp`.

### Proof

Sum the three caps from GC2fp.  Since least-cause fibres are disjoint, no illegal donor is counted twice.
QED.

## GC2fr -- legal reservoir or target/global concentration -- PROVED

Define the residual donor shortage

`R_don=(p-d-D_phys)_+`.

The target-common and global cause fibres carry total load at least `R_don`.  Consequently, if

`K_res=|C_tgt|+|C_ctx|>0`,

one exact target-common hard atom or global context/generator atom blocks at least

`R_don/K_res`

donor assignments.

If `K_res=0`, then

`d>=p-D_phys`.

### Proof

There are `p-d` illegal donors.  GC2fq accounts for at most `D_phys` of them using bounded physical
causes disjoint from the target.  Every residual illegal donor is canonically assigned to `C_tgt` or
`C_ctx`.  Sum those fibres and apply weighted pigeonhole.  If there is no residual cause class, the
residual must vanish. QED.

The target-common branch is physical: one exact hard support contains the current endpoint `x`.  It is
not silently treated as a generic bounded-support blocker.

## GC2fs -- automatic nonempty donor menu -- PROVED

If `C_tgt=C_ctx=emptyset` and

`p>D_phys`,

then the legal donor menu is nonempty.  More generally it contains at least

`p-D_phys`

donors.

Therefore GC2fl--GC2fm apply with no donor-count loss: for every `epsilon in (0,1)`, one legal donor swap
descends by at least `epsilon h`, or one exact rank-one/rank-two feedback certificate has weight greater
than

`(1-epsilon)h/K_swap`.

### Proof

The reservoir bound is GC2fr.  The final alternatives are exactly GC2fl--GC2fm; their operation-addressed
pigeonhole cancels the donor count. QED.

## GC2ft -- donor-reservoir cause router -- PROVED UNDER THE DECLARED CONTRACTS

Every heavy current lineage in the singleton-target two-layer host has one continuation:

1. `p>D_phys` and a legal donor menu of size at least `p-D_phys>=1`, hence the descent/feedback router
   of GC2fo;
2. `R_don>0` and one exact target-common hard atom or global context/generator atom with donor load at
   least `R_don/K_res`;
3. `p<=D_phys`, so the explicit bounded physical cause budget can cover the whole candidate reservoir
   and no nonempty legal menu follows from counting alone;
4. or one cause-completeness, occurrence, support, line, donor, legality, label, context or outer-reset
   field fails.

### Proof

If `R_don>0`, apply GC2fr to obtain alternative 2.  Otherwise `d>=p-D_phys`.  When `p>D_phys`, this is
positive and GC2fs/GC2fo give alternative 1.  When `p<=D_phys`, the count supplies only alternative 3.
Every excluded hypothesis is retained as alternative 4. QED.

## Corrected GC frontier

Inside the direct two-layer singleton-target host, donor scarcity is no longer diffuse.  All
collision, non-axis-line and target-disjoint bounded-support causes have the explicit budget `D_phys`;
any excess shortage localizes to one current-target-common hard atom or one global context/generator
atom.

The remaining geometry is payment or neutralization of those concentrated target/global blockers,
small reservoirs dominated by the explicit bounded physical budget, repeated non-tagged feedback
cycles, roles not represented by a singleton rectangle target, block-tuple overload recursion, pool
depletion and local superregular resampling.

## Finite check

`scripts/verify_geometric_donor_reservoir_cause_router.py` samples singleton-target permutation
rectangles and canonical blocker partitions.  It checks collision and line degree two, the
`3|Q|` target-disjoint support bound, the exact `D_phys` reservoir inequality and the residual
pigeonhole into target-common/global causes.
