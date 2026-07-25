# Unary density to superregular cross blocks

PP3sn closes every rectangle bank whose non-designated unary maximum degree is
sublinear.  A single linear star does not prevent this conclusion when the total
unary support has vanishing density: delete the few rectangles carrying high
interaction degree first.

This chapter converts the natural density hypothesis

\[
|E(F)|=o(H^2)
\]

into the maximum-degree hypothesis of PP3sn.  The true hard-unary obstruction is
therefore positive-density support, not an isolated high-degree resource.

## 1. From endpoint edges to rectangle interactions

Let \(F\) be the non-designated unary-forbidden endpoint graph on the resources
of a resource-disjoint rectangle bank of size \(H\).  Let \(\Gamma_F\) be the
rectangle interaction graph PP3si: two rectangles are adjacent when \(F\)
contains a cell in either cross resource block between them.

### Proposition PP3sp -- PROVED

One has

\[
|E(\Gamma_F)|\le |E(F)|.
\]

#### Proof

Every interaction edge has at least one witnessing endpoint edge of \(F\).
Choose one witness for each interaction edge.  One endpoint cell belongs to one
unique ordered pair of rectangle resource blocks, so distinct interaction edges
receive distinct witnesses. ∎

Multiplicity of unary witnesses can only make \(F\) larger.

## 2. Sparse-graph maximum-degree regularization

### Proposition PP3sq -- PROVED

Let \(\Gamma\) be a graph on \(H\) vertices with

\[
|E(\Gamma)|=o(H^2).
\]

There is a set \(Z\) of \(o(H)\) vertices such that

\[
\Delta(\Gamma-Z)=o(H).
\]

#### Proof

Write

\[
\eta_H=\frac{|E(\Gamma)|}{H^2}=o(1).
\]

Choose a positive sequence \(\epsilon_H\to0\) with

\[
\frac{\eta_H}{\epsilon_H}\to0;
\]

for example \(\epsilon_H=\sqrt{\eta_H}\) when \(\eta_H>0\).
Delete every vertex of degree above \(\epsilon_HH\).  The number deleted is at
most

\[
\frac{2|E(\Gamma)|}{\epsilon_HH}
=
2\frac{\eta_H}{\epsilon_H}H
=
o(H).
\]

Every remaining degree is at most \(\epsilon_HH=o(H)\). ∎

If rectangle resources must be deleted as whole blocks, this is already the
correct unit of deletion.

## 3. Complete sparse-unary regularization

### Theorem PP3sr -- PROVED

Suppose

\[
|E(F)|=o(H^2).
\]

After deleting \(o(H)\) rectangles, the remaining bank satisfies the hypotheses
of PP3sn.  Consequently it decomposes, after another \(o(H)\) loss, into a
growing number of growing-credit blocks whose directional cross hosts are
near-complete superregular and have fixed-rank spread.

#### Proof

Proposition PP3sp gives

\[
|E(\Gamma_F)|=o(H^2).
\]

Apply PP3sq and delete its exceptional rectangles.  The remaining interaction
graph has maximum degree \(o(H)\).  Since every rectangle interaction degree is
an upper bound for the number of bad cross-block partners, use PP3sj--PP3sn on
the remaining bank. ∎

The initial and block-partition losses are both lower order.

## 4. Zero-density hard unary support is closed

### Corollary PP3ss -- PROVED

In the superregular recapture branch, vanishing-density non-designated unary
support is not a remaining obstruction.  It may contain isolated linear stars,
but deleting \(o(H)\) rectangles removes all such stars and leaves a
superregular growing-block state space.

#### Proof

Apply PP3sr. ∎

This is the rectangle-block analogue of the endpoint-degree regularization
PP3is and the support-core pruning PP3ke.

## 5. Exact hard-unary alternative

### Corollary PP3st -- PROVED

Failure of unary regularization implies

\[
|E(F)|=\Omega(H^2).
\]

Equivalently, a positive fraction of the possible rectangle cross cells is
hard-unary forbidden, counted as simple support.

Such a dense support contains one of the existing geometric cores:

- a macroscopic Hall rectangle;
- a linear family of rich witness lines;
- or a positive-density endpoint-resource star/matching core after PP3kh.

#### Proof

The density conclusion is the contrapositive of PP3sr.  Apply the Hall and
support-core localizations PP3ko--PP3kt and PP3kd--PP3kh to the dense forbidden
family. ∎

The final sentence is a localization interface, not a conversion theorem.

## 6. Revised rectangle frontier

### Corollary PP3su -- PROVED

For a superregular recapture-line rectangle bank, all of the following are
closed:

- arbitrary original signed signatures;
- bounded and growing-depth local contradictions;
- irregular cross hosts under sublinear maximum degree;
- isolated linear unary stars;
- every hard-unary support of density \(o(1)\).

The remaining rectangle-level obstructions are:

1. positive-density hard-unary support and its Hall/line/resource cores;
2. source or shadow weight concentrated in the paid growing-block expression
   PP3sg;
3. failure of the adaptive high-support source estimate after block selection.

Thus the rectangle branch has returned to two quantitative objects: dense hard
support or dense paid weight.