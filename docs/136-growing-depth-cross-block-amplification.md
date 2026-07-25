# Growing-depth cross-block amplification

PP3rv amplifies through every fixed number of levels.  Because the bad-partner
degree bound PP3rt is independent of block size, the depth may grow slowly with
the bank.  This produces blocks whose individual removal credit tends to
infinity while retaining a growing number of independent blocks.

## 1. Choosing a growing block scale

Let the original rectangle bank have size \(H\), and let the non-designated
unary-forbidden endpoint graph have maximum degree \(d=o(H)\).

### Proposition PP3ry -- PROVED

There is a power of two \(b=b(H)\) satisfying

\[
b\longrightarrow\infty,
\qquad
bd=o(H),
\qquad
\frac Hb\longrightarrow\infty.
\]

#### Proof

When \(d>0\), choose the largest power of two not exceeding

\[
\sqrt{H/d}.
\]

Since \(H/d\to\infty\), this power tends to infinity.  Also

\[
\frac{bd}{H}
\le
\sqrt{d/H}
\longrightarrow0,
\]

and

\[
\frac Hb
\ge
\sqrt{Hd}
\]

when \(d\ge1\), which tends to infinity.  If \(d=0\), choose the largest power of
two not exceeding \(\sqrt H\). ∎

Write

\[
b=2^k.
\]

Then \(k\to\infty\), although slowly.

## 2. Total loss over growingly many rounds

At amplification round \(r\), the current block size is \(2^r\).  Corollary
PP3ru leaves at most \(4d+1\) current blocks unmatched.

### Theorem PP3rz -- PROVED

Using the block size \(b=2^k\) from PP3ry, one may perform all \(k\) amplification
rounds and retain

\[
(1-o(1))\frac Hb
\]

resource-disjoint level-\(b\) blocks.

The number of original rectangles discarded over all rounds is

\[
O(db+b)=o(H).
\]

#### Proof

At round \(r\), every unmatched current block contains \(2^r\) original
rectangles.  Hence that round discards at most

\[
(4d+1)2^r
\]

original rectangles.  Summing for \(0\le r<k\) gives

\[
O((d+1)2^k)=O(db+b).
\]

Proposition PP3ry makes this \(o(H)\).  The surviving original rectangles are
partitioned into blocks of size \(b\), giving the displayed block count. ∎

Thus both the block size and the number of blocks tend to infinity.

## 3. Growing credit and exact local state space

### Corollary PP3sa -- PROVED

The retained level-\(b\) bank has:

- \(b\to\infty\) designated removal-credit units per block;
- \(2b\) left and \(2b\) right resources per block;
- a nonempty unary-safe local state set;
- exact rank-at-most-three bad boxes among blocks;
- exact unary/binary insertion cost among blocks;
- a growing number \((1-o(1))H/b\to\infty\) of independent blocks.

#### Proof

Combine PP3rz with PP3rq, PP3rs, and the finite-state interface PP3qw. ∎

The formal unpruned local state count at the final round is

\[
((b)!)^2,
\]

because a level-\(b\) block is formed by pairing two level-\(b/2\) blocks, each
having \(b\) resources on one side.  Only the nonempty unary-safe subset is
retained.

## 4. Revised hierarchy endpoint

### Corollary PP3sb -- PROVED

Under sublinear unary endpoint degree, the hierarchy cannot fail merely because
a fixed block size is too small.  It contains a scale \(b\to\infty\) with both:

\[
\text{credit per block}\to\infty
\]

and

\[
\text{number of blocks}\to\infty.
\]

Failure of paid completion at this scale requires one of:

1. a growing family of locally impossible level-\(b\) state sets;
2. unary or binary block-state cost comparable with the total credit
   \(\Theta(bH/b)=\Theta(H)\);
3. residual matching shadow comparable with that credit;
4. failure of the high-support source estimate after growing-scale reservation;
5. a non-diffuse multistate interaction that persists when both local alphabet
   size and block credit grow.

The remaining hierarchy is therefore a genuinely growing-scale weighted object,
not only an infinite list of fixed-depth obstructions.