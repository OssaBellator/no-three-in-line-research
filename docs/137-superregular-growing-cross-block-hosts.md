# Superregular growing cross-block hosts

PP3rz produces growing level-\(b\) blocks under the sole assumption \(d=o(H)\),
but their unary-safe local state sets may be irregular.  A stronger conclusion
holds below the square-root unary threshold.  Taking \(b\asymp\sqrt H\) makes the
non-designated unary degree \(o(b)\).  The only remaining possible high degree in
a directional cross host comes from concentrated designated-recapture cells,
whose total number is only \(O(b)\).  Deleting \(o(b)\) original rectangles
removes that concentration and leaves a near-complete superregular host.

## 1. Square-root block scale

Let a rectangle bank have size \(H\to\infty\), and let the non-designated unary
endpoint graph have maximum degree

\[
d=o(\sqrt H).
\]

Choose a power of two \(b\) satisfying

\[
b=(1+o(1))\sqrt H
\]

up to a factor between one and two.

### Proposition PP3sc -- PROVED

Hierarchical amplification retains

\[
(1-o(1))\frac Hb
\]

level-\(b\) blocks.

#### Proof

The total amplification loss is \(O(bd+b)\) by PP3rz.  Since
\(b=\Theta(\sqrt H)\) and \(d=o(\sqrt H)\), this is \(o(H)\). ∎

Both the block size and the number of blocks are \(\Theta(\sqrt H)\) up to
lower-order factors.

## 2. Recapture-degree pruning inside one final block

A final level-\(b\) block is obtained by pairing two level-\(b/2\) children.  In
each cross direction the complete host has side size \(b\).  Direct designated
recapture deletes at most one edge for each of the \(b/2\) owners in the source
child, hence at most \(b/2\) edges in total.

Fix a threshold

\[
t=b^{2/3}.
\]

Call a target resource recapture-heavy when it is incident with more than \(t\)
direct-recapture edges.

### Proposition PP3sd -- PROVED

Each directional host has at most

\[
O(b^{1/3})
\]

recapture-heavy target resources.

Deleting every original rectangle containing one of these resources, and then
deleting \(O(b^{1/3})\) additional rectangles to equalize the two child sizes,
leaves

\[
b'=(1-o(1))b
\]

resources per directional side and retains \((1-o(1))b\) designated owner
credits in the combined block.

#### Proof

The sum of the direct-recapture degrees on the target side is at most \(b/2\).
Therefore the number exceeding \(b^{2/3}\) is at most

\[
\frac{b/2}{b^{2/3}}=O(b^{1/3}).
\]

One original rectangle contains only two resources on each side, so deleting
all rectangles meeting heavy resources removes \(O(b^{1/3})\) rectangles.
Balance the two children by deleting the same order from the larger one.  Every
deleted rectangle costs one designated owner credit, hence only \(o(b)\) credit
is lost. ∎

## 3. Near-complete forbidden degree

Let \(G_\to\) be either pruned directional host.  Its forbidden complement
contains:

- non-designated unary edges of maximum degree at most \(d\);
- direct-recapture edges of left degree at most one;
- direct-recapture target degree at most \(b^{2/3}\).

### Theorem PP3se -- PROVED

The complement of \(G_\to\) has maximum degree

\[
O(d+b^{2/3})=o(b').
\]

Consequently \(G_\to\) is superregular with density \(1-o(1)\).

#### Proof

The degree statement is the union bound on the two forbidden families after
PP3sd.  Since \(d=o(b)\) and \(b^{2/3}=o(b)\), the maximum forbidden degree is
\(o(b')\).  Apply the near-complete-host superregularity theorem PP3ip. ∎

Both cross directions satisfy the same conclusion.

## 4. Spread local state distribution

Choose independently a uniform perfect matching in each pruned directional
superregular host.  Their union is a unary-safe cross state of the level-\(b\)
block.

### Corollary PP3sf -- PROVED FROM SR1

For every fixed \(r\), any prescribed compatible collection of \(r\) selected
cross-block cells occurs with probability

\[
O(b^{-r})
\]

under the product state distribution.

#### Proof

Split the prescribed cells between the two cross directions.  SR1 gives
\(O(b^{-r_1})\) and \(O(b^{-r_2})\) probabilities for the two fixed-rank
cylinders.  Independence and \(r_1+r_2=r\) give the result. ∎

Thus the growing block has the same fixed-rank spread scale as a dense endpoint
permutation bank, while directly preserving \((1-o(1))b\) designated credits.

## 5. Paid growing-block interface

For one pruned level-\(b\) block, let:

- \(P_b\) count fixed-anchor bad edge pairs;
- \(Q_b\) count inserted collinear triples;
- \(A_b\) and \(B_b\) be unary and binary insertion-shadow weights;
- \(R_b\ge(1-o(1))b\) be the designated removal credit.

### Theorem PP3sg -- PROVED

There is a constant \(K\) such that a source-admissible strict paid state exists
whenever

\[
K^2\frac{P_b}{b^2}
+
K^3\frac{Q_b}{b^3}
+
\frac1{R_b}
\left(
K\frac{A_b}{b}
+
K^2\frac{B_b}{b^2}
\right)
<1.
\]

#### Proof

Use the spread distribution PP3sf.  The expected number of source-invalid
rank-two and rank-three patterns is bounded by the first two terms, and the
expected insertion cost divided by credit is bounded by the last two terms.
The integer-plus-normalized-cost argument of PP3io gives a state with no source
violation and cost below credit. ∎

This theorem applies block by block or after adding the block choices to a
higher-level product distribution.

## 6. Revised unary-degree frontier

### Corollary PP3sh -- PROVED

In the sparse-unary superregular recapture branch, if

\[
d=o(\sqrt H),
\]

then the hierarchy contains a growing family of growing-credit superregular
blocks with fixed-rank spread.  Failure of conversion requires concentration in
one of the normalized quantities of PP3sg.

Therefore an irregular hierarchical state space is needed only when either:

- the unary maximum degree is at least square-root scale;
- or the source/shadow weights are concentrated at the growing block-credit
  scale.

The sub-square-root unary regime has returned to an explicit paid spread
matching theorem.