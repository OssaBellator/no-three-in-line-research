# Dense Hall cores survive adaptive thinning

The adaptive source-valid bank PP3nr is chosen by random endpoint thinning. The
incidence localization PP3ny assumes that the Hall-derived target set remains
quadratically dense on the retained endpoint coordinates. This chapter supplies
that connection and combines it with the target-rich common-line theorem.

## 1. Dense cell sets in a random tied subbank

Let

\[
\mathcal A_Q\subseteq[Q]^2
\]

be a set of endpoint cells satisfying

\[
|\mathcal A_Q|\ge\alpha Q^2
\]

for fixed \(\alpha>0\). Choose a uniform \(q\)-subset \(I\subseteq[Q]\), and put

\[
X_I=|\mathcal A_Q\cap I^2|.
\]

### Proposition PP3nz -- PROVED FROM BOUNDED DIFFERENCES ON THE UNIFORM SLICE

For \(q\longrightarrow\infty\) and \(q=o(Q)\),

\[
\Pr\left(X_I<\dfrac\alpha2q^2\right)=o(1).
\]

#### Proof

At most \(Q\) cells of \(\mathcal A_Q\) are diagonal. Therefore

\[
\mathbb E X_I
\ge
\dfrac{(q)_2}{(Q)_2}(\alpha Q^2-Q)
=
(\alpha-o(1))q^2.
\]

Exchanging one selected index with one unselected index changes \(X_I\) by at
most \(4q\), because only cells using one of the two exchanged indices can
change. The standard bounded-differences inequality on the uniform \(q\)-subset
slice gives

\[
\Pr(|X_I-\mathbb EX_I|>t)
\le
2\exp\left(-c\dfrac{t^2}{q^3}\right)
\]

for an absolute constant \(c>0\). Take \(t=\alpha q^2/3\). The right side is
\(\exp(-\Omega_\alpha(q))=o(1)\), while the expectation exceeds
\(5\alpha q^2/6\) for sufficiently large \(q\). ∎

Only the vanishing tail is used; constants in the slice inequality are
irrelevant.

## 2. Joint choice with source diagnostics

### Theorem PP3oa -- PROVED

Use the adaptive size \(q\) from PP3nq. There is a \(q\)-subset \(I\) such that
simultaneously:

1. \(|\mathcal A_Q\cap I^2|\ge\alpha q^2/2\);
2. the unary forbidden graph has \(o(q)\) edges;
3. the anchored transition family has \(o(q)\) events;
4. the normalized high-support source-validity expression is \(o(1)\).

#### Proof

By PP3nz, condition 1 fails with probability \(o(1)\). The sum of the unary
count divided by \(q\), transition count divided by \(q\), and normalized
high-support expression has expectation \(o(1)\), by PP3nq and PP3jl. Markov's
inequality says that this sum is \(o(1)\) with probability \(1-o(1)\) after
choosing a deterministic error threshold tending to zero sufficiently slowly.
The two high-probability events intersect. ∎

## 3. Density after cleanup

### Corollary PP3ob -- PROVED

After deleting all indices incident with unary edges or transition events as in
PP3nr, the retained bank has size

\[
q'=(1-o(1))q
\]

and the retained target set satisfies

\[
|\mathcal A_{q'}|
\ge
(\alpha/2-o(1))q^2
=
\Omega_\alpha((q')^2).
\]

#### Proof

Deleting one endpoint index removes at most \(2q\) cells from a tied endpoint
rectangle. Since only \(o(q)\) indices are deleted, at most \(o(q^2)\) target
cells disappear. Apply PP3oa. ∎

## 4. Fully connected line-conversion endpoint

### Corollary PP3oc -- PROVED

Fix \(\delta>0\). Let a macroscopic Hall rectangle contain a quadratic recapture
target core on a resource bank of size \(Q\). After adaptive thinning and
complete source-validity cleanup, at least one of the following holds.

1. A source-valid endpoint derangement strictly decreases the owner-line load.
2. One nonaxis geometric line contains both:
   - at least \((q')^{1/3-\delta}\) pairwise resource-disjoint
     owner/replacement endpoint cells and their owner candidate points;
   - at least \((q')^{1-\delta}\) retained Hall-target endpoint cells.

#### Proof

PP3oa--PP3ob preserve a fixed positive target density. Apply PP3nt, PP3nu, and
the strengthened PP3ny on the retained bank. ∎

Thus the line-energy chain no longer assumes that a dense Hall core survives the
secondary thinning. The final structured alternative is one target-rich common
line carrying two large matching traces.
