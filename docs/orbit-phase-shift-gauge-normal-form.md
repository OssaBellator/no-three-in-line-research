# Gauge normal form for source-coset shifts

**Branch:** `research/orbit-phase-expansion`

OP4ad--OP4ah compress the individual subgroup shifts on each source-coset path
or cycle to one endpoint displacement or holonomy. This note makes that
compression canonical. After rephasing the internal coset coordinates, every
component has all shift on one distinguished terminal edge. In particular, a
zero-holonomy cycle is completely shift-free at the quotient level.

Work in the additive shift group `Z/hZ`. For an arc `u->v` with shift
`sigma(u,v)`, a vertex rephasing `phi` changes the coordinate expression to

\[
\boxed{
\sigma^\phi(u,v)=\sigma(u,v)+\phi(u)-\phi(v).
}
\]

The physical cells are not changed by this notation; only the chosen subgroup
coordinate origin inside each coset is changed. Absolute owner, legality or
context fields that are not invariant under rephasing are retained separately.

## OP4ai -- canonical path gauge normal form -- PROVED

Let

\[
v_0\to v_1\to\cdots\to v_r
\]

be a directed path with edge shifts `sigma_1,...,sigma_r` and endpoint
displacement

\[
\Omega=\sum_{i=1}^r\sigma_i.
\]

Fix both endpoint frames by `phi(v_0)=phi(v_r)=0`. There is a unique internal
rephasing such that

\[
\boxed{
\sigma^\phi_1=\cdots=\sigma^\phi_{r-1}=0,
\qquad
\sigma^\phi_r=\Omega.
}
\]

### Proof

Set recursively

\[
\phi(v_i)=\phi(v_{i-1})+\sigma_i
\qquad(1\le i<r).
\]

Then every first `r-1` transformed shift vanishes. On the last edge,

\[
\sigma_r^\phi
=
\sigma_r+\phi(v_{r-1})-\phi(v_r)
=
\sum_{i=1}^r\sigma_i
=
\Omega.
\]

The vanishing equations determine each internal `phi(v_i)` recursively, so the
normalizing rephasing is unique. QED.

## OP4aj -- canonical cycle gauge normal form -- PROVED

Let

\[
v_0\to v_1\to\cdots\to v_{r-1}\to v_0
\]

be a directed cycle with holonomy `Omega`. Fix the least-addressed vertex
`v_0` as root and set `phi(v_0)=0`. There is a unique root-fixed rephasing such
that all edges except the closing edge have shift zero and the closing edge has
shift `Omega`:

\[
\boxed{
\sigma^\phi_1=\cdots=\sigma^\phi_{r-1}=0,
\qquad
\sigma^\phi_r=\Omega.
}
\]

### Proof

Use the same recursion around the first `r-1` edges. The closing transformed
shift is the sum of all original shifts because its terminal root phase is
zero. Uniqueness again follows recursively. QED.

## OP4ak -- component sums classify gauge orbits -- PROVED

For one fixed directed path with endpoint frames fixed, two shift assignments
are related by an endpoint-fixed rephasing if and only if they have the same
endpoint displacement. For one fixed rooted directed cycle, two assignments
are related by a root-fixed rephasing if and only if they have the same
holonomy.

For a component with `r` arcs, every gauge orbit therefore contains exactly

\[
\boxed{h^{r-1}}
\]

individual shift assignments and has one canonical normal form from OP4ai or
OP4aj.

### Proof

Rephasing telescopes in the component sum, so displacement or holonomy is
invariant. Conversely, assignments with the same invariant have the same
normal form and are related through it. There are `h^(r-1)` assignments with a
fixed sum, since the first `r-1` shifts are arbitrary and determine the last.
QED.

## OP4al -- zero-holonomy and physical-gauge router -- PROVED

Every source-coset component from OP4ah has one continuation.

1. A path is represented by one endpoint displacement on its distinguished
   terminal edge.
2. A nonzero-holonomy cycle is represented by one closing-edge shift `Omega`
   and retains the finite orbit order `h/gcd(h,Omega)` from OP4ag.
3. A zero-holonomy cycle is gauge-equivalent to the completely unshifted cycle.
4. If the canonical rephasing changes an absolute physical owner, occurrence,
   legality, scale, carry or context interpretation, the least changed field is
   returned as an explicit physical-gauge obstruction.

Thus zero holonomy is no longer an unresolved quotient-arithmetic profile. Its
remaining difficulty is physical payment/absorption of the unshifted cycle or
one exact non-gauge-invariant field.

### Proof

The first three routes are OP4ai--OP4ak. The complete physical record is an
ordered finite tuple. If rephasing is not merely a coordinate change for that
record, choose its least changed tuple field; otherwise the canonical normal
form is valid. QED.

## Corrected OP5 frontier

Internal shift arithmetic is now fully normalized. The active source-coset
frontier consists of endpoint displacements, finite nonzero-holonomy orbit
payment, physical payment of unshifted zero-holonomy cycles, and exact
owner/occurrence/legality/scale/carry/context fields that fail gauge invariance.
Incomplete fibres, root-scale imbalance and scale dispersion remain separate
pre-bank outputs.

## Finite check

`scripts/verify_phase_shift_gauge_normal_form.py` exhausts path and cycle shift
words for subgroup orders two through seven and up to five arcs. It verifies
the canonical normal forms, uniqueness, invariant preservation and the exact
`h^(r-1)` gauge-orbit size.
