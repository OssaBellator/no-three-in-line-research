# Divisor-scale structure inside a donor-saturated singleton fibre

**Branch:** `research/sparse-algebraic-spread`

SAS5bd--SAS5bh reduce the singleton companion obstruction to one heavy exact defect
fibre `F_z`.  That fibre either has a safe donor or is donor-companion saturated.
The remaining records are still arithmetically organized: because the defect column
`z` is fixed, the absolute singleton dilation parameter must divide the fixed column
difference `|z-x|`.

This note partitions the heavy fibre by that exact divisor scale.  One scale retains
a divisor-fraction of the fibre weight.  It either admits a donor which repairs the
whole scale class, or the complete donor class lies in one arithmetic progression
and satisfies one primitive coprimality condition.

## Fixed heavy singleton fibre

Fix one original swapped column `x`, one singleton mirror word, one failing defect
role and one exact defect column `z!=x`.  Put

`D=|z-x|>=1`.

For a record in `F_z`, write its primitive singleton parameterization in the
orientation where the defect coefficient is `A_0` and the companion coefficient is
`B_0`:

`z=x+A_0*s`,

`c=x+B_0*s`,

with `gcd(|A_0|,|B_0|)=1` and `s!=0`.

The word and ordered row roles fix the sign of `A_0`; hence the sign of `s` is fixed
throughout the fibre.  Write that sign as `epsilon in {+1,-1}`.

For every positive divisor `g` of `D`, let `F_(z,g)` be the record subfamily with
`|s|=g`, and let

`L_g=sum_(Q in F_(z,g)) w(Q)`.

## SAS5bi -- every record lies on a divisor scale -- PROVED

For every record in `F_z`,

`|s| divides D`.

More precisely, in the scale class `|s|=g` one has the fixed defect coefficient

`A_0=(z-x)/(epsilon*g)`.

### Proof

The identity `z-x=A_0*s` has nonzero integer factors.  Therefore `|s|` divides
`|z-x|=D`.  Since the sign of `s` is `epsilon`, substitution gives the displayed
coefficient. QED.

Thus the fibre has at most `tau(D)` nonempty divisor-scale classes, where `tau` is
the positive-divisor function.

## SAS5bj -- one exact divisor scale retains heavy fibre weight -- PROVED

Some divisor `g|D` satisfies

`L_g >= L(z)/tau(D)`.

Using the elementary bound `tau(D)<=2*sqrt(D)`, one may choose `g` with

`L_g >= L(z)/(2*sqrt(D))`.

### Proof

The divisor-scale classes partition the fibre weight and there are at most `tau(D)`
of them.  Weighted pigeonhole gives the first bound.  Pair every divisor below
`sqrt(D)` with its complementary divisor above `sqrt(D)` to obtain the second. QED.

## Companion set at one scale

For a selected scale `g`, define

`C_(z,g)={c(Q):Q in F_(z,g)}`

and its donor-labelled part

`C_(z,g)^ell=C_(z,g) intersect D_ell`.

Every companion in this class has the form

`c=x+epsilon*g*B_0`

with

`gcd(|A_0|,|B_0|)=1`.

## SAS5bk -- heavy scale repair or scale saturation -- PROVED WITH ORIGINAL-SWAP COMPOSITION

For the heavy divisor scale supplied by SAS5bj, exactly one of the following holds:

1. there is a donor

   `r in D_ell \ ({x,y} union C_(z,g))`,

   and the composed move `omega union {z,r}` repairs every record in
   `F_(z,g)` simultaneously, hence repairs weight at least `L_g`;
2. no such donor exists, and

   `D_ell\{x,y} subseteq C_(z,g)`.

   In this case every donor outside the original swap satisfies

   `r congruent x (mod g)`

   and, writing

   `B_r=(r-x)/(epsilon*g)`,

   one has

   `gcd(|A_0|,|B_r|)=1`.

### Proof

If the donor lies outside the complete companion set of the selected scale, it is
outside the scope of every selected record.  The original swap fixes the swapped
literal and the donor transposition supplies the required label at `z`, so the whole
scale class is repaired as in SAS5ay.

If no safe donor exists, every donor outside `{x,y}` occurs as a companion in the
scale class.  Its companion representation gives the congruence and primitive
coprimality statements. QED.

This is stronger than whole-fibre saturation: either a divisor-fraction of the heavy
fibre repairs, or that same heavy divisor class already contains every available
donor companion.

## SAS5bl -- progression-capacity bound for a saturated scale -- PROVED

Assume the saturation alternative in SAS5bk and let `d=|D_ell|`.  Then

`d-2 <= 1+floor((N-1)/g)`.

In particular, when `d>=4`,

`g <= floor((N-1)/(d-3))`.

Hence a donor class of density `d>=delta*N+2` forces

`g < 1/delta`

up to the displayed integer rounding.

### Proof

Every donor outside `{x,y}` lies in the board interval and in the residue class
`x mod g`.  An interval of `N` consecutive columns contains at most
`1+floor((N-1)/g)` members of one residue class.  There are at least `d-2` retained
donors.  Rearranging the inequality gives the bound for `d>=4`. QED.

The coprimality restriction from SAS5bk can only reduce the number of available
progression slots.

## SAS5bm -- quantitative saturated-fibre divisor router -- PROVED

Let the heavy exact fibre from SAS5bg have load

`L(z) > h*W/[8*b*d*(N-1)^2]`.

Then one divisor `g|D` gives one of:

1. an original-plus-donor move repairing record weight strictly greater than

   `h*W/[8*b*d*(N-1)^2*tau(D)]`;
2. an exact donor-saturated scale class of the same weight lower bound, with fixed
   dilation magnitude `g`, fixed defect coefficient

   `A_0=(z-x)/(epsilon*g)`,

   every donor outside `{x,y}` lying in the progression `x+g*Z`, and the capacity
   bound from SAS5bl.

Using `tau(D)<=2*sqrt(D)`, both retained scale weights are strictly greater than

`h*W/[16*b*d*(N-1)^2*sqrt(D)]`.

### Proof

Apply SAS5bj to the heavy fibre and then SAS5bk.  Substitute the lower bound from
SAS5bg.  SAS5bl supplies the progression-capacity statement in the saturated branch.
QED.

## Corrected SAS6 frontier

The donor-saturated singleton obstruction is no longer an arbitrary collection of
row triples.  A divisor-fraction of its weight now lies in one exact dilation scale.
That class either repairs or forces the complete donor class into one congruence
progression with a fixed primitive defect coefficient.

The remaining work is to compare the composed move with the original energy inside
that exact scale, exploit the coprime coefficient set, and handle high-incidence and
board-boundary profiles.

## Finite check

`scripts/verify_sparse_saturated_fibre_divisor_scale.py` exhausts small fixed-defect
singleton systems, primitive shapes, divisor scales, donor sets and weight vectors.
It checks divisibility, fixed coefficients, divisor-weight localization, whole-scale
repair, progression/coprimality saturation and the progression-capacity bound.
