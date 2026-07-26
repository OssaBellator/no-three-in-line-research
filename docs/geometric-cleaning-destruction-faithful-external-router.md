# Destruction-faithful external payment and multiplicative density overload

**Branch:** `research/geometric-cleaning`

GC2br--GC2bv replace the globally normalized GC2g row by the exact raw gain row of one
rectangle event.  The remaining raw-row failure was split into source-free capacity and a
destroyed-factor capacity/gain-density overload.  The source-free branch is not a genuine
payment source: an event can charge only current factors that it actually destroys.

This note imposes that physical eligibility wall, removes all source-free pseudo-capacity
from the Hall system, and converts the only remaining deficit into one exact multiplicative
capacity/gain-density certificate.

## One-event destroyed-factor system

Fix one current hard-legal rectangle event `j`.  Let `D_j` be the finite set of exact
current factor occurrences destroyed by `j`.  For `p in D_j`, let `w_p>0` be its current
factor weight.  Put

`Dsum_j=sum_(p in D_j)w_p`,

`lambda_j=g_j/Dsum_j`,

where `g_j>0` is the event's exact current gain.  The raw one-event gain row is

`q_p=lambda_j*w_p`

on `D_j` and zero outside it.

Let `P_ext` be a finite external resource-occurrence set with declared Hall capacities
`c_p>=0`.  Define the destruction-faithful eligible set

`E_j=P_ext intersect D_j`,

and put

`C_dest=sum_(p in E_j)c_p`,

`Z_dest=sum_(p in E_j)min(c_p,q_p)`.

The forced residual demand from GC2bg is `R_star>0`.

## GC2bw -- destruction-faithful eligibility wall -- PROVED

Every gain-certified correction--factor charge for event `j` is supported on `D_j`.
Consequently every physically valid external payment allocation must satisfy

`x_p=0`

for `p notin D_j`.

Capacity on `P_ext\D_j` is therefore not event payment.  Counting it in a Hall system is
only a relaxation and cannot certify descent or complete payment for `j`.

### Proof

A current correction--factor charge is defined by faithful destruction of the charged
current factor occurrence by the same correction event.  If `p notin D_j`, the event does
not destroy `p`, so the occurrence has no correction--factor incidence in the row of `j`.
The exact raw row also has `q_p=0` there.  Hence every gain-certified amount is zero outside
`D_j`. QED.

This removes the source-free branch of GC2bu rather than attempting to repair it.

## GC2bx -- corrected one-event Hall/overlap trichotomy -- PROVED

Exactly one of the following holds:

1. `C_dest<R_star`; then the destruction-faithful external system has an exact one-event
   Hall deficit `R_star-C_dest>0`;
2. `C_dest>=R_star` and `Z_dest>=R_star`; then the proportional raw-row allocation gives
   executable descent greater than `(1-1/theta)W`;
3. `C_dest>=R_star>Z_dest`; putting

   `Delta_dest=R_star-Z_dest>0`,

   one has the exact destroyed-factor excess identity

   `sum_(p in E_j)(c_p-q_p)_+=C_dest-Z_dest>=Delta_dest`.

### Proof

The cases are the three possible comparisons of `C_dest` and `Z_dest` with `R_star`, with
`Z_dest<=C_dest`.  The first is the one-event Hall inequality on the physically eligible
set.  The second is GC2bs restricted to `E_j`.  In the third,

`c_p-min(c_p,q_p)=(c_p-q_p)_+`

for every `p in E_j`; sum and use `C_dest>=R_star`. QED.

No source-free term remains because GC2bw removed every ineligible coordinate before the
Hall comparison.

## GC2by -- multiplicative capacity/gain-density certificate -- PROVED

Assume the third alternative of GC2bx.  Then one exact destroyed factor occurrence
`p_* in E_j` satisfies

`c_(p_*)/q_(p_*) >= C_dest/Z_dest`

and hence

`c_(p_*)/q_(p_*) >= R_star/(R_star-Delta_dest)>1`.

Equivalently,

`c_(p_*)/w_(p_*)`

`>=lambda_j*R_star/(R_star-Delta_dest)>lambda_j`.

### Proof

For `p in E_j`, `q_p>0`.  Coordinates with `c_p=0` contribute nothing.  Write

`m_p=min(c_p,q_p)`.

Then

`C_dest=sum_p m_p*(c_p/m_p)`

and `Z_dest=sum_p m_p`.  Therefore one coordinate has ratio at least the weighted average
`C_dest/Z_dest`.  Since `C_dest>=R_star` and
`Z_dest=R_star-Delta_dest`, the second bound follows.  A ratio greater than one forces
`c_p>q_p`, so `c_p/q_p=c_p/(lambda_j w_p)`. QED.

This is stronger than the previous additive statement: it records the exact factor by
which physical Hall capacity exceeds the event's own gain density.

## GC2bz -- role and occurrence localization of destroyed-factor excess -- PROVED

Suppose the eligible destroyed occurrences have at most `T_dest` exact physical roles.
One role carries additive excess at least

`Delta_dest/T_dest`.

If every role fibre has at most `B_dest` occurrences, one exact destroyed occurrence has

`(c_p-q_p)_+ >= Delta_dest/(T_dest*B_dest)`.

The same occurrence may be chosen from a role whose maximum multiplicative ratio is at
least the role's capacity-to-overlap ratio.

### Proof

Partition the nonnegative masses `(c_p-q_p)_+` by role and apply GC2bx, then partition the
selected role by occurrence.  For the multiplicative refinement, repeat the weighted-average
argument of GC2by inside the selected role. QED.

The role identifies the physical factor occurrence and destruction role; equal line or
label data do not merge separate factors.

## GC2ca -- complete destruction-faithful external router -- PROVED

For the forced external residual of every capacity-deficient event star, exactly one of
the following destruction-faithful continuations holds:

1. an exact one-event Hall deficit on the factors actually destroyed by `j`;
2. raw-event overlap at least `R_star`, giving executable descent greater than
   `(1-1/theta)W`;
3. one exact destroyed-factor role, and under a fibre cap one exact occurrence, carrying
   both additive deficit and a multiplicative capacity/gain-density ratio greater than one.

Thus source-free external capacity is no longer a live geometric-cleaning branch.  The
remaining external obstruction is physical and event-local: a factor destroyed by `j`
has too much Hall capacity relative to the gain density that `j` can certify on it.

### Proof

Apply GC2bw before forming the Hall system, then use GC2bx--GC2bz. QED.

## Corrected GC frontier

The endpoint-disjoint high-ratio star now routes to normalized payment, atomic or zero
capacity, lower-rank concentration, high pair codegree, a destruction-faithful Hall deficit,
raw-event descent, or one exact destroyed-factor capacity/gain-density overload.

The next live obligation is geometric classification or repair of that destroyed-factor
overload.  Other open interfaces remain lower-rank and high-pair execution, isolated-cell
prospective stars, pool depletion, global context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_destruction_faithful_external_router.py` exhausts small event
rows and rational capacity systems and samples larger ones.  It checks removal of
source-free coordinates, the corrected Hall/overlap trichotomy, the exact additive excess,
the multiplicative density certificate and role/occurrence localization.
