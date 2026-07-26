# Large protected cores descend through one minimum skeleton class

CMR617--CMR697 give exact protected/free skeleton products, product-conflict
rectangles, pure-factor recursion, strict prefix routing, and finite owner stock.
CMR958--CMR981 later show how an actual minimum and its induced real-triple
objective pass through those products without assuming global additivity.

This chapter records the combined endpoint. A large protected matching does not
create an uncontrolled terminal branch. Choose one actual minimum state, retain
its cross skeleton, normalize every low-rank coupling atom on the surviving
minimum face, and descend through one coordinate factor. The resulting factor
then enters complete essential-core contraction and strict child-prefix routing.

Let the residual side be `n`, let the protected matching have size `k`, and put

\[
u=n-k.
\]

Use the canonical protected/free skeleton decomposition of CMR617--CMR622.

## 1. A chosen minimum selects one skeleton class

### Theorem CMR1038 -- PROVED

The complete cylinder is a finite disjoint union of cross-skeleton classes. If
`S` is an actual minimum-potential state and `Gamma(S)` is its skeleton, then
restriction to the class

\[
\mathcal F_{\Gamma(S)}
\]

preserves `S` and its minimum value.

### Proof

Every state has one unique cross skeleton by CMR619--CMR620. The class containing
`S` is a subfamily which still contains the known minimum, so CMR902 applies. ∎

No union of different skeleton masks is treated as one product.

## 2. Exact minimum product inside the selected skeleton

Let the selected skeleton have flow size `c`. Put

\[
a=k-c,
\qquad
b=u-c.
\]

### Theorem CMR1039 -- PROVED

The selected class has the exact representation

\[
\boxed{
\mathcal F_{\Gamma(S)}
\cong
\{\Gamma(S)\}
\times
\operatorname{PM}(H_I)
\times
\operatorname{PM}(H_J).
}
\]

The real-triple objective on this product is the induced objective obtained by
lifting factor matchings to the original parent board. The state `S` remains a
minimum for that induced objective.

### Proof

The product is CMR619--CMR620. Minimum inheritance follows from CMR1038 and the
induced-objective restriction identity CMR906. ∎

The objective is not asserted to be factor-additive before coupling
normalization.

## 3. Coupling atoms normalize on the selected minimum face

### Theorem CMR1040 -- PROVED

Inside the selected skeleton product, every mixed real-triple atom has local rank
at most two in each touched factor and occurs on one exact Cartesian rectangle.
On the current minimum face, repeated canonical responses perform one of:

1. minimum-preserving deletion of a noncommon atom edge;
2. host-representable contraction of the atom's residual minimum-core
   prescription;
3. a fixed core/skeleton conflict;
4. strict potential improvement or structural exit.

Before an exit, the process uses at most the residual host-edge stock in deletions
and at most the residual state cardinality in contractions.

### Proof

Apply CMR629--CMR635 and the minimum-face coupling normalization
CMR958--CMR965. Host representability is CMR974--CMR981. ∎

## 4. One selected minimum descends into a coordinate factor

### Theorem CMR1041 -- PROVED

After coupling normalization, freeze every factor coordinate of `S` except one.
The variable-coordinate fibre contains `S` and `S` remains minimum for the exact
one-factor induced objective.

Every former cross-factor atom becomes constant or an anchored prescription of
rank at most two in that factor. Finite deletion/contraction normalization leaves
one of:

1. a pure residual obstruction in the protected factor;
2. a pure residual obstruction in the free factor of side at most `u`;
3. a fixed certificate;
4. strict factor/owner descent or potential improvement.

### Proof

Use CMR966--CMR973 after CMR1040. ∎

Thus the minimum face itself need not factor.

## 5. Large protected size gives a sparse interface stock

### Theorem CMR1042 -- PROVED

The selected cross skeleton has interface size at most `2u`, and the complete
skeleton stock satisfies

\[
\boxed{
N_{\mathrm{sk}}(k,u)
\le
(u+1)n^{4u}.
}
\]

For fixed or bounded free codimension `u`, both the skeleton stock and every mixed
atom stock are polynomial in `n`.

### Proof

Apply CMR621--CMR622 and CMR630. ∎

The small free factor is therefore an explicit bounded carrier, not an anonymous
large-dimensional obstruction.

## 6. Pure factors enter essential-core and strict-prefix recursion

### Theorem CMR1043 -- PROVED

Let a pure residual factor have side `d`. Its complete essential core contracts
exactly. The remaining core-free host admits at most `d^2` canonical
matching-preserving deletion rounds before a fixed certificate or smaller
residual factor is reached.

A nontrivial residual factor has a deepest full prime-power prefix envelope and a
finite vertex-routing skeleton stock. Fixing one recurrent routing skeleton
factors the matching family over strict child prefix cells. Every noncertificate
continuation strictly decreases factor side or prefix-envelope depth.

### Proof

Use CMR649--CMR663 and CMR677--CMR683. ∎

## 7. Host changes inside the recursion are well founded

### Theorem CMR1044 -- PROVED

At every fixed vertex set encountered in CMR1043, the minimum-anchor host history
normalizes to a finite monotone restriction segment interrupted only by:

1. minimum-core contraction;
2. exact rollback of an added batch;
3. a lost minimum edge and forward ancestry;
4. strict potential improvement;
5. factor, routing, wall, or envelope exit.

No restoration-only loop survives normalization.

### Proof

Apply CMR926--CMR957 at each recursion node. ∎

## 8. Large-protected-core endpoint

### Corollary CMR1045 -- PROVED

The large-protected-core branch of CMR1017, CMR1027, and CMR1036 reaches at least
one of:

1. a finite selected-skeleton stock bounded by CMR1042;
2. coupling deletion or host-representable minimum-core contraction;
3. a pure free-factor obstruction of side at most `u=n-k`;
4. a pure protected-factor obstruction entering essential-core and strict-prefix
   descent;
5. a fixed physical certificate and target handoff;
6. paid routing/skeleton change, owner/envelope exit, or strict potential
   improvement.

Hence protected-core largeness is no longer an unresolved terminal condition.
The remaining post-saturation obstruction is concentrated in matching-vertex
walls, loaded target lines, and the cross-layer rooted paid-pair response after
all exact product descents have been applied.

### Proof

Combine CMR1038--CMR1044 with CMR617--CMR697 and CMR958--CMR981. ∎

No all-`n` theorem is claimed. Skeleton selection, minimum preservation, sparse
interface arithmetic, coordinate descent, and recursion budgets are checked in
[`scripts/verify_prime_power_large_protected_core_minimum_descent.py`](../scripts/verify_prime_power_large_protected_core_minimum_descent.py).
