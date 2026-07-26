# Exact row and label collapse inside one negative cross column fibre

**Branch:** `research/sparse-algebraic-spread`

SAS5bx--SAS5cb localize negative mixed curvature to one exact third column after fixing an
endpoint pair, one single-swap-only orientation and one endpoint-incidence type.  This note
finishes the remaining record reconstruction.  Once the primitive row ratio is fixed, only
one positive row scale and one base row remain.  Once the orientation and three exact
columns are fixed, every required label is forced by the unique single-swap state that
satisfies the record.

The result is an exact geometric-label record fibre.  It does not assert that repeated
occurrences of that record are independent or simultaneously repairable.

## Fixed reconstruction address

Fix three distinct exact scope columns and an ordered placement `(i,j,k)` among increasing
row positions.  Fix the primitive row ratio `(A_0,B_0)` from SAS5bx.  Every compatible row
triple has

`r_j=r_i+g*A_0`,

`r_k=r_i+g*B_0`

for one positive integer scale `g`.  Board rows lie in `{0,...,N-1}`.

## SAS5cc -- row scale and base row reconstruct the exact row triple -- PROVED

For fixed `(i,j,k,A_0,B_0)`, the pair

`(g,r_i)`

reconstructs the complete ordered row triple uniquely.  Every valid address has

`1<=g<=N-1`,

`0<=r_i<=N-1`.

Hence the safe number of exact row addresses inside one primitive-ratio class is at most

`N*(N-1)`.

### Proof

The displayed reconstruction equations determine `r_j,r_k` from `g,r_i`.  Since the
original gcd scale is positive and every nonzero row gap has magnitude at most `N-1`, the
scale is at most `N-1`; the base row has at most `N` choices.  Ordering and board range only
remove addresses. QED.

## SAS5cd -- the single-swap orientation forces every required label -- PROVED

Fix the three exact scope columns and one of the two negative-curvature orientations from
SAS5bu.

1. In the omega-only orientation, the required label at every scope column equals its label
   in `kappa^omega`.
2. In the tau-only orientation, the required label at every scope column equals its label
   in `kappa^tau`.

Thus there is exactly one required-label vector compatible with the fixed orientation and
scope.

### Proof

A negative record is satisfied in exactly its named single-swap state and in none of the
other three states.  Satisfaction of a conjunction record means that each required label
equals the actual label at its scope column in that state.  Therefore all three required
labels are forced coordinatewise. QED.

In particular, the outside-all-endpoints third column has its unchanged current label, and
a mate endpoint has the label assigned to it by the satisfying single swap.

## SAS5ce -- finite exact-record stock after column localization -- PROVED

Consider one fixed endpoint-pair/orientation/scope-type fibre with one exact third column.

- If a primitive reconstruction address `(i,j,k,A_0,B_0)` is already fixed, the number of
  exact geometric-label records is at most `N(N-1)`.
- Without a fixed primitive address, first split into the safe stock
  `24(N-1)^2` from SAS5by and then into row scale/base addresses.  The total exact-record
  stock is at most

  `24*N*(N-1)^3`.

No additional label factor is required.

### Proof

Apply SAS5cc inside each primitive address.  SAS5cd reconstructs the label vector rather
than adding choices.  Multiply by the SAS5by address stock only in the second case. QED.

## SAS5cf -- weighted exact-record localization -- PROVED

Let a fixed exact-column fibre carry record weight `V>0`.

1. If its primitive reconstruction address is fixed, one exact geometric-label record
   carries weight at least

   `V/[N*(N-1)]`.
2. Without a fixed primitive address, one exact record carries weight at least

   `V/[24*N*(N-1)^3]`.

### Proof

Partition by the finite exact-record stocks in SAS5ce and apply weighted pigeonhole. QED.

Multiple occurrences with the same rows, columns and required labels remain in the same
exact record fibre and share whatever occurrence capacity the energy model assigns.

## SAS5cg -- uniform quantitative negative-record router -- PROVED

Use the negative cross fibre supplied by SAS5cb from a divisor scale of weight `L_g`.
For every `eta in (0,1)`, if

`C_minus>=eta*L_g`,

then one exact geometric-label record fibre carries weight at least

`eta*L_g/[576*N*(N-1)^3]`.

If the composed move improves, one exact record fibre carries weight strictly greater than

`L_g/[576*N*(N-1)^3]`.

### Proof

In the mate-type branch, SAS5cb supplies an exact-column fibre of weight at least
`eta L_g/24`.  Its primitive address is not yet fixed, so SAS5cf(2) gives

`eta L_g/[24*24*N*(N-1)^3]`.

In the outside-endpoint branch, SAS5cb already includes one primitive reconstruction
address and supplies weight at least `eta L_g/[576(N-1)^2]`.  Apply SAS5cf(1), giving the
same denominator `576*N*(N-1)^3`.  The improving branch uses the strict SAS5cb bounds. QED.

## Corrected SAS6 frontier

The negative mixed-curvature branch now reaches one exact row triple, exact three-column
scope and exact required-label vector with an explicit polynomial retention factor.  Its
remaining issues are occurrence multiplicity, compatibility and energy interaction among
several copies or several exact record fibres.  The other exact-scale obstruction remains
the coprime donor-saturated progression, together with high-incidence and board-boundary
profiles.

## Finite check

`scripts/verify_sparse_negative_cross_exact_record.py` exhausts small row triples and
primitive-ratio classes, checks scale/base reconstruction, exhausts two-swap label states,
verifies label uniqueness for both negative orientations and checks the uniform
`576*N*(N-1)^3` accounting.