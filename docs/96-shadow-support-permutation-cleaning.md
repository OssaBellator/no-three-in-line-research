# Shadow-support permutation cleaning

PP3jr bounds residual insertion shadow by its total unary and binary weights.
Weight multiplicity is unnecessary when the support itself is locally sparse. A
permutation cell with any positive residual unary shadow may be forbidden once,
and a compatible pair with any positive binary shadow may be forbidden once.
The permutation local lemma can then make the insertion cost exactly zero.

## 1. Residual shadow supports

Use the regularized endpoint bank and source-validity notation of PP3ja--PP3jn.
Direct designated-credit recapture cells may already have been added to the unary
bad family as in PP3jq.

Define the residual unary shadow support

\[
\mathcal U_{\rm sh}
=
\left\{
(i,j):
\sum_{p\in S_0}w_{\rm res}((x_i,y_j),p)>0
\right\}.
\]

Define the residual binary shadow support

\[
\mathcal B_{\rm sh}
=
\left\{
\{(i,j),(k,l)\}:
\begin{array}{l}
(i,j),(k,l)\text{ are compatible, and}\\
w_V((x_i,y_j),(x_k,y_l))>0
\end{array}
\right\}.
\]

These are simple support families. A cell or pair is counted once regardless of
how many controller entries it blocks.

For a typed left or right endpoint resource `v`, let

\[
d_1(v)
=
|\{a\in\mathcal U_{\rm sh}:v\in a\}|
\]

and

\[
d_2(v)
=
|\{B\in\mathcal B_{\rm sh}:v\in B\}|.
\]

Put

\[
d_1=\max_v d_1(v),
\qquad
d_2=\max_v d_2(v).
\]

## 2. Shadow-support mass

### Proposition PP3jt -- PROVED

Adding every unary shadow-support cell and every binary shadow-support pair to
the PP3ix canonical bad-event family increases its maximum resource mass by at
most

\[
\boxed{
\lambda_{\rm sh}
\le
\dfrac{d_1}{q}
+
\dfrac{d_2}{(q)_2}.
}
\]

#### Proof

A unary cell event has probability `1/q`; a prescribed compatible pair has
probability `1/(q)_2`. Sum the events incident to one typed resource. ∎

### Proposition PP3ju -- PROVED

Every endpoint permutation avoiding `mathcal U_sh` and `mathcal B_sh` has

\[
\boxed{
\mathcal I_{\rm res}=0.
}
\]

If it also avoids the designated recapture support, its complete insertion cost
contains none of the `q` designated credit incidences and no residual unary or
binary shadow incidence.

#### Proof

Every residual insertion-shadow term contains either one inserted cell and one
unchanged source point or two inserted cells. A positive term of the first type
places its selected cell in `mathcal U_sh`; a positive term of the second type
places its selected pair in `mathcal B_sh`. Avoidance removes both classes. The
designated statement is PP3jp. ∎

## 3. Zero-cost paid endpoint theorem

Let `lambda_src` be the PP3ix resource mass of the low-support source-invalid
events after the regularization of PP3jm. Include direct recapture events in
`lambda_src` or charge their additional mass separately through PP3jq.

### Theorem PP3jv -- PROVED

Assume

\[
\boxed{
\lambda_{\rm src}
+
\dfrac{d_{\rm rec}}q
+
\dfrac{d_1}q
+
\dfrac{d_2}{(q)_2}
\le
\dfrac1{24}.
}
\]

Assume also that the conditioned high-support source-validity mass satisfies

\[
\boxed{
9\dfrac{P_4}{q^2}
+
27\dfrac{Q_{\ge4}}{q^3}
<1.
}
\]

Then some endpoint permutation is source-admissible and satisfies

\[
\mathcal I(\pi)=0.
\]

Consequently every resource bank with positive removal credit admits a strict
controller-shadow improvement.

#### Proof

Apply PP3ix to the union of:

- the low-support source-invalid events;
- designated recapture cells;
- `mathcal U_sh`;
- `mathcal B_sh`.

The displayed resource-mass inequality verifies the local lemma. Condition on
avoiding this family. PP3iy supplies `(3/q)^r` spread for the remaining
rank-two and rank-three cylinders. The second displayed inequality and a union
bound give positive conditional probability of avoiding every remaining
high-support source-invalid event.

The resulting permutation is source-admissible. Proposition PP3ju gives zero
insertion cost, while the resource bank has positive removal credit, so PP3id
strictly decreases the potential. ∎

### Corollary PP3jw -- PROVED

On the two-scale source-valid bank of PP3jn, the high-support term is `o(1)` and
`lambda_src=o(1)`. Therefore an improving trade follows whenever

\[
\boxed{
d_{\rm rec}+d_1=o(q),
\qquad
d_2=o(q^2).
}
\]

No weighted estimate for `A_res` or `B_G` is then required.

## 4. Exact support-concentration alternative

### Corollary PP3jx -- PROVED

Fix a small constant `rho>0`. For all sufficiently large `q`, either PP3jv
applies, or at least one of the following holds.

1. **Rich recapture fibre:** `d_rec>=rho q`.
2. **Unary insertion-shadow fibre:** one endpoint row or column contains at least
   `rho q` cells that block some residual controller entry with an unchanged
   source point.
3. **Binary insertion-shadow star:** one typed endpoint resource belongs to at
   least `rho q^2` compatible inserted-cell pairs that block a controller entry.

#### Proof

If none of the three alternatives holds and `rho` is chosen below the remaining
PP3ix mass slack, the shadow-support contribution is at most `O(rho)`. Combine
with the `o(1)` source terms from PP3jn and apply PP3jv. ∎

These are support concentrations, not weight concentrations. Repeated witnesses
of one cell or pair do not make the LLL harder because one forbidden event removes
them all.

## 5. Revised weighted bottleneck

The resource-bank branch no longer needs bounds of the form

\[
A_{\rm res}=o(q^2),
\qquad
B_G=o(q^3)
\]

when their positive supports are locally sparse. Its remaining failure objects
are the three support concentrations in PP3jx.

Thus the global controller-shadow conversion theorem is reduced to:

- the original blocker-star branch;
- dense unary endpoint source shadow;
- rich recapture fibres;
- unary insertion-shadow fibres;
- binary insertion-shadow stars.

Every diffuse weighted residual is eliminated exactly by one permutation local
lemma.