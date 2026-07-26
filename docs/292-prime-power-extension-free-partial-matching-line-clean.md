# Extension-free response graphs survive arbitrary partial-matching deletion

CMR1406--CMR1413 classify every minimal blocker of the extension-free response
host.  The exact cut formula has a stronger consequence which was not used
there: no such Hall cut can itself be a partial matching once the response side
is at least four.  Therefore an arbitrary partial matching may be deleted from
the extension-free host without destroying all perfect matchings.

This applies in particular to every set of cells on one nonaxis real line.  A
loaded owner line can consequently be cleaned while still avoiding the fixed
opposite matching and the original target edge.  The conclusion is local: it
kills the same-owner, same-line collateral coordinate, but does not yet bound
all off-line offspring.

Fix a response side `d>=4`, a perfect matching `O` of `K_{d,d}`, and an edge
`e notin O`.  Put

\[
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

Relabel the two vertex classes so that `O` is the identity and write
`e=(u,v)` with `u ne v`.

## 1. Every Hall cut exceeds matching capacity

Let `A` be a set of `k` source vertices and let `B` be a set of

\[
z=d-k+1
\]

target vertices.  Put

\[
Q=E(H_e)\cap(A\times B).
\]

Write

\[
s=|A\cap B|,
\qquad
\delta=\mathbf 1_{\{u\in A,\ v\in B\}}.
\]

### Theorem CMR1510 -- PROVED

Let

\[
m=\min\{k,z\},
\qquad
M=\max\{k,z\}.
\]

Then

\[
\boxed{|Q|=kz-s-\delta\ge m+1.}
\]

### Proof

The exact formula is CMR1406: the rectangle has `kz` cells, the normalized
opposite matching removes exactly `s`, and the target removes `delta`.
Since `s<=m` and `delta<=1`,

\[
|Q|\ge kz-m-1=m(M-1)-1.
\]

Also `k+z=d+1>=5`.  If `m=1`, then `M>=4`; if `m>=2`, then `M>=3`.
In both cases

\[
m(M-2)\ge2,
\]

so `m(M-1)-1>=m+1`. ∎

### Corollary CMR1511 -- PROVED

No nonempty Hall-cut core `Q` in `H_e` is a partial matching.

### Proof

A partial matching contained in `A times B` has at most
`min(k,z)=m` edges, whereas CMR1510 gives `|Q|>=m+1`. ∎

## 2. Arbitrary partial-matching deletion preserves a response

### Theorem CMR1512 -- PROVED

For every partial matching

\[
X\subseteq E(H_e),
\]

the graph

\[
\boxed{H_e\setminus X}
\]

has a perfect matching.

### Proof

Assume not and choose an inclusion-minimal blocker `Q subseteq X`.  The minimal
blocker theorem CMR1151/CMR1406 writes `Q` as one exact Hall-cut core
`E(H_e) cap (A times B)` with `|B|=d-|A|+1`.  Since `X` is a partial matching,
so is `Q`, contradicting CMR1511. ∎

The statement allows `X` to have any size up to `d`; it is not a small-deletion
estimate.

## 3. Target-safe deletion of one complete nonaxis line

Let `K` be a nonaxis real line in the inherited physical grid and define its
allowed response trace

\[
X_K=E(H_e)\cap K.
\]

### Theorem CMR1513 -- PROVED

`X_K` is a partial matching.  Hence

\[
\boxed{\operatorname{PM}(H_e\setminus X_K)\ne\varnothing.}
\]

### Proof

A nonaxis line meets every source row and every target column in at most one
grid cell, so its cells form a partial matching.  Apply CMR1512. ∎

### Theorem CMR1514 -- PROVED

Every response

\[
R\in\operatorname{PM}(H_e\setminus X_K)
\]

simultaneously satisfies

\[
R\cap O=\varnothing,
\qquad
e\notin R,
\qquad
R\cap K=\varnothing.
\]

Thus it preserves saturation with the fixed opposite layer, destroys every old
target containing `e`, and selects no response-layer cell on `K`.

### Proof

The first two properties define `H_e`; the third follows from deleting `X_K`.
The target-destruction statement is CMR1306. ∎

## 4. Exact line-local collateral removal

### Theorem CMR1515 -- PROVED

For a line-clean response `R` from CMR1514,

\[
\boxed{(O\cup R)\cap K=O\cap K.}
\]

Consequently every physical triple supported entirely on `K` after the response
is an `O`-only triple already present in the fixed opposite layer.  The number
of new collateral triples supported entirely on `K` is exactly zero.

### Proof

The response contributes no cell on `K`; the opposite layer is fixed.  Any
three-cell subset of the resulting line trace is therefore contained in `O` and
was present before the response. ∎

### Theorem CMR1516 -- PROVED

Suppose CMR1461 produces an owner-labelled loaded signature on a real line `K`
through entering owner `a`.  There is a target-safe response in which the
same-owner, same-line collateral coordinate is zero.

More explicitly, choose

\[
R\in\operatorname{PM}(H_e\setminus X_K).
\]

Then `a notin R`, no allowed response partner on `K` is selected, and no new
candidate triple with canonical owner `a` supported on `K` occurs.

### Proof

The owner `a` is an allowed response cell on `K`, so `a in X_K` and is omitted.
CMR1514 omits every other allowed response cell on `K`.  A candidate owned by
`a` must contain `a`, hence none occurs.  CMR1515 removes every other new
line-local triple. ∎

This does not claim that the chosen response has no off-line collateral.

## 5. Extension-free line-clean endpoint

### Corollary CMR1517 -- PROVED

The loaded-line recurrent row has an exact target-safe policy with zero
same-owner, same-line offspring.  Therefore a host-uniform recurrent-core
quotient need not place a mandatory self-loop on that coordinate.

The unresolved numerical terms are the off-line offspring of the line-clean
response, repeated-token/reused-edge rows, recurrent root/fixed-interface rows,
and their comparison with destroyed parent credit.  No all-`n` theorem is
claimed.

Hall-cut excess, exhaustive partial-matching deletion and nonaxis line traces are
checked in
[`scripts/verify_prime_power_extension_free_partial_matching_line_clean.py`](../scripts/verify_prime_power_extension_free_partial_matching_line_clean.py).
