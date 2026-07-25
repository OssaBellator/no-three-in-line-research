# Active packet cores close the diffuse selected-defect range

PX223 shows that selected crosses inside one product packet form a matching on
the packet arcs.  Most arcs of a large candidate packet may be irrelevant to
the current defect state.  Retaining only arcs which participate in old
selected crosses produces an **active packet core** of size exactly twice its
old defect load.

This normalization connects packet incidence to actual realized-defect overlap.
Bounded overlap permits one incidence-weighted joint release by PX307--PX309;
high overlap is already a loaded-line or clean-star child by PX303--PX305.

## 1. Active subpackets

Fix a current perfect matching `M` on an order-`h` endpoint block.  For one
anchor-product packet `P_alpha`, let `d_alpha` be its number of selected
packet-certified crosses, as in PX223.

Let `A_alpha` be the set of packet arcs which occur in at least one selected
cross of `P_alpha`.

### Theorem PX310 -- PROVED

For every packet level `alpha`:

1. the selected crosses are pairwise disjoint on packet arcs;
2. the active subpacket `A_alpha` is a partial matching of size
   
   \[
   \boxed{|A_\alpha|=2d_\alpha;}
   \]
3. on the active packet rows and columns, the current matching is exactly the
   disjoint union of the `d_alpha` cross transpositions.

Consequently a no-two-cycle release of `A_alpha` suppresses recurrence of every
old selected defect in that packet, without paying for inactive packet arcs.

### Proof

The disjointness is PX223.  Every selected cross uses two packet arcs, and no
arc occurs in two selected crosses, proving the size identity.  If packet arcs
`r->a` and `s->b` form a selected cross, the current matching contains
`r->b` and `s->a`.  Disjoint selected crosses have disjoint rows and packet
columns, so their cross edges form a perfect matching on the active row and
column sets. \(\square\)

## 2. Active incidence is realized-defect overlap

Let `mathscr A={A_alpha:d_alpha>0}` be the active packet family.  Define its
row/column incidence `B_act` as in PX307.

Let `Lambda_old` be the maximum endpoint-support degree in the family of actual
old selected packet defects, counted as anchor-weighted collinear triples.

### Theorem PX311 -- PROVED

One has

\[
\boxed{B_{\rm act}\le\Lambda_{\rm old}.}
\]

Moreover, if `Q_act` is the number of distinct cross events in all active
subpackets, then

\[
\boxed{Q_{\rm act}\le\frac12B_{\rm act}h^2.}
\]

### Proof

If a row label belongs to `A_alpha`, the unique active packet arc in that row
belongs to one selected cross of `P_alpha`; the corresponding old defect has
that label in its endpoint support.  Within one packet, selected crosses are
disjoint, so a fixed label is charged at most once.  Hence the number of active
packets incident with the label is at most its old-defect support degree.  The
column argument is identical.

The event-energy estimate is PX308 applied to the active packet family. \(\square\)

This is the key causal normalization: packet release complexity is controlled
by defects actually present, not by unrestricted candidate packet size.

## 3. Bounded-overlap active release

### Corollary PX312 -- PROVED

If

\[
B_{\rm act}\le B
\qquad\text{and}\qquad
h\ge32\max(1,\Delta,B),
\]

then all active packet cores admit one joint release family satisfying

\[
\boxed{|\Omega|\ge e^{-4\Delta-4B}h!}
\]

and

\[
\boxed{
\Pr(E\subseteq M')
\le
\frac{e^{4\Delta+4B}}{(h)_r}
}
\]

for every compatible rank-`r` cylinder.

Every old selected packet defect is destroyed by the base movement of the
current matching, and every corresponding active packet cross has probability
zero in the release family.

The conditioned statement holds with residual ordinary degree `Delta+B` and
the PX309 factor.

### Proof

Apply PX307 and PX311.  The current positions are inherited forbidden cells, so
PX235 deletes every old defect meeting the block.  The active no-two-cycle
events suppress their exact packet recurrence by PX238. \(\square\)

## 4. Complete packet strict-sign-or-child interface

Fix a selected-line threshold `K`, a minimum quantitative child order `m_0`, and
put

\[
B=4Km_0.
\]

### Theorem PX313 -- PROVED

Every family of old selected packet defects in an order-`h` decoder block has
one of the following outcomes.

1. **High-overlap geometry.**  `B_act>B`.  Then `Lambda_old>B` by PX311, so PX305
   gives either a selected line with more than `K+1` points or an
   endpoint-disjoint secant star of order greater than `m_0`.
2. **Joint active release.**  `B_act<=B` and
   `h>=32max(1,Delta,B)`.  PX312 releases every active packet core at once with
   constant fixed-rank spread, destroys all old packet defects, and suppresses
   their packet recurrence.  All realized new rank-at-most-three collateral is
   handled by the complete strict-sign-or-child theorem PX306.
3. **Exact terminal packet core.**  `h<32max(1,Delta,B)`.  The complete active
   packet instance is finite and is sent to the exact one- or two-block
   optimizer PX273--PX276 and PX290.

Therefore the former diffuse selected-defect packet range is closed at the
combinatorial decoder level.  It does not require a bounded number of full
candidate packets: only the active defect cores are released.

### Proof

The first case combines PX311 with PX305.  In the second case use PX312 and then
PX306 on the realized external collateral.  The third case has order bounded in
terms of the fixed decoder constants and is exactly enumerable. \(\square\)

This removes the last separate small-packet frontier from the active ledger.
The remaining tasks are trajectory-reset descendants, quantitative assembly of
all constants, and insertion of the terminating decoder into PX63.

## 5. Verification

Run

```bash
python scripts/verify_product_active_packet_core.py
```

The verifier enumerates selected packet crosses under random current
permutations, checks active size `2d`, verifies the active-current transposition
matching, confirms `B_act<=Lambda_old` and `Q_act<=B_act h^2/2`, and tests the
three cases of PX313.