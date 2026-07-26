# Prime-field root channels are singleton support states

CMR1494--CMR1501 reduce every depth-zero exact translation to one source-root
channel with deterministic partner residue and quotient carry.  For envelope
exponent `k>=2`, selected child normalization is strict and therefore
off-diagonal.  The only potentially recurrent root case is the prime field
`k=1`.

At `k=1`, the root residue is the complete physical cell.  A fixed source
channel therefore contains at most one ordered translated pair, not a family of
parent-scale copies.  Its residual support has one or two edges.  First use of
those labels is finite resource; recurrence preserves one exact support and
belongs to reused-support/return bookkeeping or to one exact fixed-interface
atom.

Thus anonymous prime-field root translation is not an additional broad diagonal
row.

Fix a prime `p`, the side-`p` envelope

\[
\Omega_p=\{0,\ldots,p-1\}^2,
\]

and one nonzero exact displacement `Delta` of first-separation depth zero.  Let
`E_Delta` be a weighted family of ordered pairs `(a,b)` in the envelope with
`b=a+Delta`.

## 1. A root residue is the complete source cell

For `k=1`, write as in CMR1494

\[
a=r+pA.
\]

### Theorem CMR1606 -- PROVED

Every source cell satisfies

\[
\boxed{A=(0,0),\qquad a=r.}
\]

Likewise, for the partner decomposition `b=r'+pB`,

\[
\boxed{B=(0,0),\qquad b=r'.}
\]

Consequently a fixed source-residue root channel contains at most one ordered
pair.

### Proof

All coordinates of `a` and `r` lie in `{0,...,p-1}` and are congruent modulo
`p`, so they are equal.  Exact division then gives `A=0`.  Apply the same
argument to `b,r'`.  Since `Delta` and `a` determine `b`, the channel contains at
most one pair. ∎

The quotient carry identity becomes `0=0+q(r)` whenever the pair remains inside
the side-`p` box, so the realized prime-field channel has zero quotient motion.
The carry label remains useful only as provenance of the parent displacement.

## 2. Exact global pair stock

### Theorem CMR1607 -- PROVED

Across all nonzero exact prime-field channels, the number of ordered distinct
source-partner pairs is exactly

\[
\boxed{p^2(p^2-1).}
\]

For one fixed displacement, at most `p^2` channels are nonempty.

### Proof

There are `p^2` choices for the source cell and `p^2-1` choices for a distinct
partner cell.  Every ordered distinct pair determines one exact displacement.
For fixed displacement, each source determines at most one partner. ∎

Thus the complete prime-field root-pair inventory is polynomial in the envelope
side.

## 3. Every channel has support size at most two

Use the CMR1496 residual support

\[
J(a,b)=
\begin{cases}
\{a\},&b\text{ is fixed in the opposite layer},\\
\{a,b\},&b\text{ is a response partner}.
\end{cases}
\]

### Theorem CMR1608 -- PROVED

For every nonempty prime-field root channel,

\[
\boxed{1\le |J(a,b)|\le2.}
\]

The support is completely determined by the ordered pair and partner type.

### Proof

The channel has one pair by CMR1606.  Insert its partner type into the displayed
definition. ∎

No hidden root-channel multiplicity remains after the exact pair is fixed.

## 4. First support labels are finite resources

Consider a sequence of prime-field root-channel executions inside one fixed
physical owner epoch.  Label a support edge **first** when it has not appeared
in the support of an earlier selected execution in the epoch; otherwise label
that incidence **reused**.

### Theorem CMR1609 -- PROVED

If `N_first` and `N_reuse` count support incidences with multiplicity, then

\[
\boxed{N_{\rm tot}=N_{\rm first}+N_{\rm reuse}.}
\]

Moreover

\[
\boxed{N_{\rm first}\le p^2}
\]

for one physical response layer, and more sharply it is bounded by the exact
available response-edge universe of the current host.

After adjoining the used support-label set to the refined state, every first
support use is a strict finite-resource transition.  Only reused support labels
can remain diagonal.

### Proof

Every physical support edge is first at most once.  A side-`p` layer has `p^2`
physical cells.  Adding a new label strictly enlarges a finite monotone set, as
in CMR1491 and CMR1560. ∎

This does not declare support use free; it places first use off-diagonal.

## 5. Exact prime-field terminal signature

Every CMR1498 root candidate has partner type

\[
\tau\in\{\text{fixed},\text{response}\}
\]

and one positive local-rank pattern among

\[
\mathcal P=\{(1),(2),(1,1),(2,1),(1,1,1)\}.
\]

Define the exact terminal signature

\[
\sigma=(a,b,\tau,\pi),
\qquad\pi\in\mathcal P.
\]

### Theorem CMR1610 -- PROVED

The total number of exact prime-field terminal signatures is at most

\[
\boxed{10p^2(p^2-1).}
\]

For a fixed displacement it is at most `10p^2`.

### Proof

Use CMR1607 for the ordered-pair stock, two partner types, and five listed rank
patterns. ∎

Some combinations are geometrically impossible; the displayed number is an
honest universal upper bound.

## 6. Batching fixes one exact terminal state

Suppose `J` prime-field root episodes occur in one owner epoch.  For an exact
signature `sigma`, let `m(sigma)` be its multiplicity.

### Theorem CMR1611 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. **Finite root ancestry**
   \[
   \boxed{J\le(\lambda-1)10p^2(p^2-1).}
   \]
2. **Exact terminal recurrence**: one signature `sigma` occurs in at least
   `lambda` episodes.

For one fixed displacement, the first bound improves to

\[
\boxed{J\le(\lambda-1)10p^2.}
\]

unless one exact signature recurs `lambda` times.

### Proof

Pigeonhole over the signature stocks of CMR1610. ∎

Historical episodes are used only to identify one repeated exact policy class;
their target loads are not added.

## 7. Recurrent signature splice

### Theorem CMR1612 -- PROVED

Fix one exact recurring prime-field signature `sigma=(a,b,tau,pi)`.
Before it can remain an independent diagonal root row, at least one of the
following exact alternatives applies.

1. A support label in `J(a,b)` is first in the epoch, giving the strict resource
   transition of CMR1609.
2. The support is reused.  Its response-layer reintroduction and recreation
   offspring are recorded by the returned-edge exchange kernel of
   CMR1574--CMR1589; non-return mask reuse remains in the already isolated reused-
   support class.
3. The side-one anchored or cross-factor prescription deletes or contracts as in
   CMR1500.
4. One exact fixed-interface atom remains and is retained with its partner type
   and local-rank pattern.
5. A later owner, wall, host or structural exit occurs.
6. Strict potential improvement occurs.

Hence prime-field translation itself supplies no additional diffuse recurrent
coordinate.

### Proof

CMR1606 fixes the pair, CMR1608 fixes its support, and CMR1609 separates first
from reused support.  CMR1500 gives the exhaustive side-one terminal outcomes.
CMR1577--CMR1589 record recreated response credits supported by a returned edge.
All later-owner and structural exits are already off-diagonal. ∎

The exact fixed-interface atom in branch four remains a genuine base-row
frontier; the surrounding root translation does not.

## 8. Prime-field root endpoint

### Corollary CMR1613 -- PROVED

The recurrent depth-zero prime-field branch has the following exact normal form.

1. Every root channel is one ordered pair with support size one or two.
2. The full pair and terminal-signature stocks are polynomial in `p`.
3. First support labels are finite-resource transitions.
4. Excess recurrence fixes one exact pair, partner type and local-rank pattern.
5. Reused response support enters the return exchange kernel; other reuse remains
   in the explicit reused-support class.
6. Side-one deletion and contraction are terminal structural operations.
7. Only one exact fixed-interface atom may remain as a new prime-field base row.

Thus the broad “recurrent root channel” label should be removed from the
prime-field quotient.  The remaining numerical base is the finite fixed-
interface table together with already explicit return/reused-support rows.  No
all-`n` theorem is claimed.

Singleton channels, ordered-pair stocks, support labels, terminal signatures,
batching and first-use/reuse decompositions are checked in
[`scripts/verify_prime_field_root_channel_support_splice.py`](../scripts/verify_prime_field_root_channel_support_splice.py).
