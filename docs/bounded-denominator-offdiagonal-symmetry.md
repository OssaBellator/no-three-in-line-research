# Role-transpose symmetry for off-diagonal balanced-floor channels

**Branch:** `research/bounded-denominator-absorbers`

BDA5bl--BDA5bn close all six diagonal channel comparisons and leave thirty
off-diagonal ordered pairs from the alphabet

\[
\mathcal W=\{A,B,C,D,CD,AB\}.
\]

The decoder roles `u` and `v` are symmetric before a role is designated as the
payment or obstruction side.  This note quotients the remaining ordered pairs
by that exact transpose.

## BDA5bo -- exact role-transpose involution -- PROVED

For an ordered comparison `(omega_u,omega_v)` with role-side weighted record
families `E_u,E_v`, define

\[
\iota(\omega_u,\omega_v,E_u,E_v,u,v)
=
(\omega_v,\omega_u,E_v,E_u,v,u).
\]

Then `iota` is an involution.  It preserves:

1. total and minimum role-side collateral weights;
2. blocker occupancy type and the common arithmetic profile;
3. every determinant identity after renaming `u` and `v`;
4. wall/non-wall, radial, affine-line and secant incidence relations;
5. physical realizability, provided owner and orientation labels are transposed
   with the roles.

### Proof

The two-state balanced decoder menu is indexed by the two role parameters and
has no preferred role.  Every BDA5m determinant formula is the same polynomial
in the role variable `w`; exchanging the two evaluations exchanges the two
families and no geometric equation.  Applying the exchange twice is identity.
QED.

## BDA5bp -- fifteen unordered off-diagonal templates -- PROVED

The thirty ordered off-diagonal pairs split into fifteen transpose orbits,
each represented by one unordered pair

\[
\boxed{\{\omega,\eta\}\subset\mathcal W,
\qquad\omega\ne\eta.}
\]

Every orbit has size exactly two.

### Proof

There are `6*5=30` ordered off-diagonal pairs.  A fixed point of transpose would
satisfy `omega=eta`, which is excluded.  Hence all orbits have size two and the
orbit count is `30/2=15=binom(6,2)`. QED.

## BDA5bq -- orientation-sensitive output router -- PROVED

It is sufficient to prove one geometric classification theorem for each of the
fifteen unordered channel templates.  When the theorem returns an
orientation-sensitive payment, owner, blocker or context field, retain one
additional bit identifying which member of the unordered pair occurred in role
`u`.

Thus the complete off-diagonal dictionary consists of at most

\[
\boxed{15\text{ geometric templates}\times2\text{ orientations}.}
\]

No proof may silently discard the orientation bit when the continuation is not
role-symmetric.

### Proof

BDA5bo transports every statement for one orientation to the transposed
orientation.  Symmetric conclusions need no extra data; asymmetric conclusions
are reconstructed from the orbit representative and one role bit. QED.

## Corrected BDA6 frontier

The balanced-floor channel geometry now consists of six completed diagonal
cases and fifteen off-diagonal geometric templates, rather than thirty
independent ordered cases.  Remaining work is the actual classification and
payment/realization of those fifteen templates and the higher-rank imports.

## Finite check

`scripts/verify_bda_offdiagonal_symmetry.py` enumerates the channel alphabet,
checks the transpose involution, its orbit count and exact reconstruction from
an unordered representative plus one orientation bit.
