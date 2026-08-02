# The active repair path does not need a growing packet-family parameter

PX217--PX218 and PX443 provide a useful joint release theorem for `k` packet
families, but their cylinder factors contain `e^(O(k))`.  A common cutoff that
tracks only ordinary forbidden degree would therefore be incomplete if the
active repair loop required `k` to grow.

The paired-label repair tree can avoid that issue.  Above the effective
large-block threshold, PX445 pays all rank-two support-four candidate creation
directly by adaptive thinning.  Below the threshold, old selected packet
defects are aggregated by their unique correction transpositions and processed
by PX431--PX435.  Historical label assignments prevent return of a corrected
old defect.  The optional simultaneous packet-release bank is not needed on
this chosen route.

## 1. Large blocks pay support four directly

### Theorem PX471 -- PROVED

On every paired label block satisfying PX445, the full paired rank-two
support-four expected creation is at most

\[
\boxed{\eta s/8.}
\]

Therefore the large-block strict-sign proof may charge this sector directly to
the old destruction and need not extract or jointly release any product packet.

### Proof

This is item 1 of PX445 with the corrected constant.  The packet alternative in
that theorem is optional. \(\square\)

## 2. Selected packet defects need no complement family

### Theorem PX472 -- PROVED REDUCTION

Let an old selected paired packet defect be assigned to its unique source-pair
label transposition by PX429--PX431.  After executing a correction, recreating
that old defect requires both corrected sources to return to their two original
label assignments.

Thus the two historical label positions recorded by the correction suppress
recurrence of the old defect.  No separately maintained packet-complement event
family is required for this correction branch.

Disjoint corrections may be processed by PX434, and a nonimproving correction
returns to clean-star or loaded-line children through PX432--PX435.

### Proof

The old defect used assignments `u->v` and `s->w`.  The correcting
transposition selects `u->w` and `s->v`.  Returning to the same old geometric
certificate requires the original pair `u->v,s->w`; copy choices do not change
that label event.  Both original assignments are recorded historical positions
and remain forbidden.  The remaining statements are PX431--PX435. \(\square\)

This statement concerns recurrence of corrected selected defects.  The joint
release theorem remains available for applications that deliberately forbid an
entire candidate packet level.

## 3. Packet-family-free active branch

### Theorem PX473 -- PROVED REDUCTION

The asymptotic repair loop PX449 may be chosen so that its probability and
cutoff ledger contains no growing packet-family count `k`.

Use the following route.

1. **Above `N^(3/5)`:** apply PX445 and pay paired support four directly.
2. **Nested below-threshold packet child:** aggregate old selected packet defects
   into PX431's correction graph.
3. **Correction recurrence:** use historical label positions as in PX472.
4. **Correction failure:** return to host-compatible clean-star or loaded-line
   label children.
5. **Bounded terminal residue:** use the exact terminal/blocker interfaces,
   without invoking a growing joint packet release.

Consequently the common asymptotic cutoff needs to track the inherited label
forbidden degree and nested depth, but not an additional logarithmic packet
count.

### Proof

PX471 handles the only potentially superlinear candidate support-four sector on
large blocks.  PX472 handles selected old packet defects and their recurrence.
PX435 gives strict sign or a first-generation child.  The nested and terminal
interfaces process the remaining bounded residue.  None of these chosen steps
uses the density factor `e^(-4k)` from PX217 or PX443. \(\square\)

### Corollary PX473a -- PROVED REDUCTION

PX443 is an optional stronger release tool and should not be a dependency of
the effective-cutoff path PX445--PX450.  The dependency manifest and cutoff
audit may set the active packet-family count to zero.

This removes one possible hidden parameter but does not weaken the joint packet
release theorem itself.

## 4. Verification

Run

```bash
python scripts/verify_product_packet_family_free_path.py
```

The verifier checks the direct paired support-four margin, exact historical
return event of a corrected packet pair, and the absence of a `k`-dependent
factor in the selected active-path formulas.
