# Near-transversal rigidity and line deletion past halfway

CMR228 proves that an odd parent block remains free of essential matching edges
after deletion inside half a block's worth of real-line matchings.  The same
Hall-rectangle argument extends beyond halfway once near-full affine
transversals are counted.

## 1. Counting near affine transversals

### Theorem CMR234 — PROVED

Let `A,C` be finite subsets of the real line with

\[
|A|=n,
\qquad
|C|=m\ge n,
\]

and let `r,s` be nonnegative integers.  The number of nonvertical,
nonhorizontal real lines containing at least `n-r` points of `A times C`, under
the additional size condition

\[
m-n\le s,
\]

is at most

\[
\boxed{
2\binom{r+2}{2}\binom{r+s+2}{2}.
}
\]

### Proof

Order both coordinate sets increasingly.  A positive-slope line induces an
order-preserving bijection between the source and target coordinates which it
uses.  At most `r` source coordinates are omitted, so the first two used source
indices both lie among the first `r+2` positions.  The line omits at most

\[
(m-n)+r\le r+s
\]

target coordinates, so its first two used target indices both lie among the
first `r+s+2` positions.

The two chosen source points and their two chosen target images determine the
line.  Hence the number of positive-slope lines is at most

\[
\binom{r+2}{2}\binom{r+s+2}{2}.
\]

For negative slope, use the first two used source positions and the last two
used target positions.  The same bound applies. ∎

For `r=s=0` this recovers the two-transversal bound CMR227.

## 2. A fixed surplus beyond half the block

Fix integers

\[
t=2h+1,
\qquad
r\ge0,
\]

and put

\[
q=h+r.
\]

Define

\[
M_r
=
2\binom{r+2}{2}\binom{3r+2}{2}.
\]

### Theorem CMR235 — PROVED

Assume

\[
\boxed{
h\ge M_r(r+1)-r^2+2.}
\]

Let `L_1,...,L_q` be distinct nonaxis real lines in the normalized parent board,
and let

\[
D\subseteq\bigcup_{i=1}^q E(L_i).
\]

If

\[
H=G_t-D
\]

has a perfect matching, then `H` has no essential edge.

### Proof

Every deleted line is a partial matching, so

\[
\delta(H)\ge(t-1)-q=h-r.
\]

Suppose `e=uv` is essential.  Let `(A,B)` be its Hall factor from CMR210, put

\[
a=|A|=|B|,
\qquad
C=(R\setminus B)\cup\{v\},
\qquad
c=|C|=2h+2-a.
\]

CMR211 gives

\[
h-r\le a\le h+r+1.
\]

Write

\[
a=h+1+d,
\qquad
c=h+1-d,
\]

so

\[
-r-1\le d\le r.
\]

Let

\[
n=\min\{a,c\},
\qquad
m=\max\{a,c\}.
\]

As in CMR228, every cell of `A times C` except `uv` is absent from `H`, and the
old diagonal accounts for at most `n` missing cells.  Hence the deleted lines
must cover at least

\[
R=n(m-1)-1
\]

cells of `A times C`.

Each of the `q` lines contains at most `n` cells of this rectangle.  Relative to
the maximum total `qn`, the available deficiency is therefore at most

\[
qn-R
=
n(r-|d|)+1.
\]

If `|d|=r+1`, this quantity is negative, an immediate contradiction.  Hence
`|d|\le r`, and in particular

\[
m-n=2|d|\le2r.
\]

By CMR234, at most

\[
2\binom{r+2}{2}\binom{3r+2}{2}=M_r
\]

of the lines can meet `A times C` in at least `n-r` cells.  Every other line has
deficiency at least `r+1`.  Thus the total deficiency is at least

\[
(q-M_r)(r+1).
\]

On the other hand,

\[
n(r-|d|)+1\le(h+1)r+1.
\]

The assumed lower bound on `h` gives

\[
(q-M_r)(r+1)>(h+1)r+1,
\]

which is impossible.  Therefore no essential edge exists. ∎

## 3. A growing surplus

For `r\ge1`, the elementary estimates

\[
M_r\le60r^4,
\qquad
r+1\le2r
\]

show that the CMR235 threshold is at most `120r^5+2`.

### Corollary CMR236 — PROVED

Let

\[
h\ge240,
\qquad
\rho(h)=\left\lfloor\left(\frac h{240}\right)^{1/5}\right\rfloor.
\]

For a globally nonimproving inherited parent block of size

\[
t=2h+1,
\]

at least one of the following holds.

1. A residual parent state is covered by a rank-one or rank-two certificate,
   giving an executable anchored alternating continuation by CMR201.
2. There are
   
   \[
   h+\rho(h)+1
   \]
   
   distinct candidate-only real-line signatures, and one parent perfect
   matching avoids every candidate cell on the first
   
   \[
   h+\rho(h)
   \]
   
   lines.

### Proof

Put `r=\rho(h)`.  The displayed estimates imply

\[
M_r(r+1)-r^2+2
\le120r^5+2
\le\frac h2+2
\le h,
\]

so CMR235 applies to any deleted set contained in at most `h+r` distinct line
matchings.

Repeat the construction of CMR229.  Whenever a residual perfect matching is
covered by a candidate-only triple, delete all cells on its real line one at a
time.  Before every cell deletion, the deleted set is contained in at most
`h+r` line matchings and the current host has a perfect matching; CMR235 says
the cell is not essential.  Thus the deletion succeeds.  A later certificate
must use a new line because all cells of the earlier lines are absent.

After deleting `h+r` line matchings, one more residual cover certificate is
either anchored or supplies the `(h+r+1)`-st distinct candidate-only line. ∎

The surplus is modest but unbounded:

\[
\rho(h)=\Omega(h^{1/5}).
\]

Thus a frozen large odd parent cannot be supported by only half a block plus a
fixed number of candidate-only line signatures.

## 4. Revised second-half target

The remaining line-avoidance theorem begins after

\[
\frac{t-1}{2}+\Omega(t^{1/5})
\]

simultaneously deleted real-line matchings.  To advance further, one may sharpen
the near-transversal count in CMR234, or charge the growing family of distinct
lines to primitive-height, quotient, or carry signatures.

No all-`n` theorem is claimed here.  The order-pattern count and the surplus
thresholds are checked in
[`scripts/verify_prime_power_near_transversal_resilience.py`](../scripts/verify_prime_power_near_transversal_resilience.py).
