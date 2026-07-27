# Weighted batching inside localized sparse parameter chains

**Branch:** `research/sparse-algebraic-spread`

SAS5dr--SAS5dv localize every nonimproving heavy-record peel to one primitive line, primitive
dilation, designated divisor scale or positive fixed-third-column class.  The remaining data are
integer parameters.  SAS5u--SAS5w give an unweighted support-density theorem; this note adds the
weighted version needed for the quantified peel outputs.

The result extracts a heavy atom or a disjoint family of adjacent parameter pairs whose total
bottleneck weight is explicit.  A final arithmetic lemma also quantifies the prime obstruction in a
dense coprime donor progression.

## Weighted interval model

Let

`I={s_0,s_0+1,...,s_0+J-1}`

be an interval of `J>=1` integer parameter slots.  Missing or invalid records are represented by
weight zero.  Give slot `s` weight `w_s>=0` and put

`W=sum_(s in I) w_s>0`.

For a threshold `a>0`, define the heavy core

`H_a={s in I:w_s>=a}`

and write `K_a=|H_a|`.

## SAS5dw -- weighted heavy-core size -- PROVED

Assume every slot has weight at most `M`, where `M>=a`.  Then

`sum_(s in H_a) w_s>=W-J*a`

and therefore

`K_a>=ceil((W-J*a)/M)`

whenever `W>J*a`.

### Proof

Every slot outside `H_a` has weight strictly less than `a`, so the total light weight is less than
`J*a`.  The heavy core therefore carries more than `W-J*a`; weaken this to the displayed inequality.
Since every heavy slot has weight at most `M`, at least `(W-J*a)/M` heavy slots are required. QED.

## SAS5dx -- weighted adjacent-pair matching -- PROVED

Let `H subseteq I` have `K` slots, each of weight at least `a`.  Put

`E=max{0,2K-J-1}`.

Then at least `E` adjacent interval edges have both endpoints in `H`, and at least

`q=ceil(E/2)`

of those edges can be selected with pairwise disjoint endpoints.  For every such selection `P`,

`sum_((s,s+1) in P) min{w_s,w_(s+1)}>=a*q`.

### Proof

SAS5w gives at least `E` occupied adjacent edges and a matching of size at least `ceil(E/2)`.
Every selected endpoint lies in `H`, so both endpoint weights are at least `a`; summing the pairwise
minimum gives the final inequality. QED.

This bottleneck mass is the amount that can be assigned injectively to both members of each adjacent
pair.

## SAS5dy -- concrete average-scale router -- PROVED

Set

`a=W/(4J)`,

`M=4W/(3J)`,

`K_0=ceil(9J/16)`,

`E_0=max{0,2K_0-J-1}`,

`q_0=ceil(E_0/2)`.

Then one of the following holds:

1. one parameter has weight greater than `4W/(3J)`; or
2. there are at least `q_0` pairwise endpoint-disjoint adjacent parameter pairs and their total
   bottleneck weight is at least
   
   `W*q_0/(4J)`.

### Proof

If alternative 1 fails, apply SAS5dw.  The slots of weight at least `W/(4J)` carry at least
`3W/4`, and each carries at most `4W/(3J)`.  Hence their number is at least `ceil(9J/16)`.  Apply
SAS5dx. QED.

For `J>=8`, the exact formula gives `q_0>=1`; for longer intervals it gives a linear-size common-step
matching.

## SAS5dz -- primitive line and dilation batching -- PROVED

Consider one localized primitive family from SAS5du.

1. **Double-scope line:**
   
   `(r(s),c(s))=(r_0,c_0)+s(A_0,D_0)`.

2. **Singleton dilation:**
   
   `(c_j(s),c_k(s))=(x+A_0s,x+B_0s)`.

Let `I` be the full board-valid parameter interval from SAS5u, with length

`J<=1+floor((N-1)/M_shape)`,

where `M_shape` is the primitive height.  Extend the localized record weights by zero to all of `I`.
Then SAS5dy gives either:

- one exact parameter of weight greater than `4W/(3J)`; or
- `q_0` disjoint adjacent parameter pairs of total bottleneck weight at least `W q_0/(4J)`.

Every selected pair has the same geometric increment:

- `(A_0,D_0)` in the line case;
- `(A_0,B_0)` in the dilation case.

### Proof

The board-valid slots form one integer interval by SAS5u.  Apply SAS5dy.  The common-increment
identities are the exact parameterizations. QED.

Thus the batched original and donor repair outputs now carry weighted common-step pairs, not merely
an unweighted dense support.

## Positive fixed-third-column chains

Fix three exact scope columns, one row-position assignment and one primitive row ratio
`(A_0,B_0)`.  After fixing the positive row scale `g`, the valid base rows `r_i` form an integer
interval of length at most `N`.

For a positive outside-endpoint class from SAS5dt, the primitive ratio is already fixed.  Splitting
by the at most `N-1` scales selects one base-row chain carrying at least `V/(N-1)` of its weight.

For a positive mate-type fixed-third-column class, first split by the safe `24(N-1)^2` primitive
addresses from SAS5by and then by scale.  One base-row chain carries at least

`V/[24(N-1)^3]`.

## SAS5ea -- positive base-row batching -- PROVED

Apply SAS5dy to the selected base-row chain of length `J<=N`.  Then either one exact row triple has
weight greater than `4W_chain/(3J)`, or there are `q_0` disjoint adjacent base-row pairs with total
bottleneck weight at least

`W_chain*q_0/(4J)`.

All selected pairs translate the complete row triple by the same vector `(1,1,1)` while preserving
the exact three-column scope, primitive ratio and required-label vector.

### Proof

For fixed scale and primitive ratio, increasing the base row by one increases all three rows by one.
The board-valid base rows form an interval.  Apply SAS5dy.  Required labels are already forced by the
selected curvature orientation once the physical scope is fixed. QED.

This turns the positive fixed-column branch into a common-translation batch or one heavy exact
record.

## Coprime coefficient slots

Let `A_0!=0` be the fixed primitive denominator in a donor-saturated progression.  Suppose `K`
occupied coefficient slots lie in an interval of `J` consecutive integers and every occupied
coefficient is coprime to `A_0`.  Put `h=J-K`.

## SAS5eb -- dense coprime progression excludes small prime factors -- PROVED

For every prime `p` dividing `A_0`,

`K<=J-floor(J/p)`.

Equivalently,

`floor(J/p)<=h`.

In particular, every prime divisor of `A_0` satisfies

`p>J/(h+1)`.

### Proof

Every interval of `J` consecutive integers contains at least `floor(J/p)` multiples of `p`.
Those slots cannot be occupied because their coefficients are not coprime to `A_0`.  This gives the
first two inequalities.  If `p<=J/(h+1)`, then `floor(J/p)>=h+1`, a contradiction. QED.

Thus near-saturation of a coprime donor progression forces the least prime factor of the primitive
denominator to be large; small-prime denominators leave a quantitative hole budget.

## Corrected SAS6 frontier

Every localized one-parameter output now yields one of:

- a heavy exact parameter;
- a weighted disjoint batch of adjacent parameters with one common geometric increment;
- or, in the coprime saturated branch, an explicit lower bound on every prime factor of the
  primitive denominator.

The remaining work is no longer weighted density extraction.  It is simultaneous executability and
cross-pair energy accounting for the common-step batches, comparison of heavy parameters with the
opposite energy side, and the high-incidence/reflected-boundary profiles.

## Finite check

`scripts/verify_sparse_weighted_parameter_chain_batching.py` exhausts small weighted intervals and
coprime coefficient systems, then samples larger localized families.  It checks the heavy-core mass,
adjacent matching count, bottleneck-weight inequality, common-step parameter identities, base-row
translation and the prime-exclusion bound.