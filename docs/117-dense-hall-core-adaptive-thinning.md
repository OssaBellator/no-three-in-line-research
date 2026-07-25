# Dense Hall cores survive adaptive thinning

The adaptive source-valid bank PP3nr is chosen by random endpoint thinning. The
incidence localization PP3ny assumes that the Hall-derived target set remains
quadratically dense on the retained endpoint coordinates. This chapter supplies
that missing connection.

## 1. Dense cell sets in a random tied subbank

Let

\[
\mathcal A_Q\subseteq[Q]\times[Q]
\]

be a set of endpoint cells satisfying

\[
|\mathcal A_Q|\ge\alpha Q^2
\]

for fixed \(\alpha>0\). Choose a uniform \(q\)-subset \(I\subseteq[Q]\), and put

\[
X_I=|\mathcal A_Q\cap(I	imes I)|.
\]

### Proposition PP3nz -- PROVED FROM PERMUTATION BOUNDED DIFFERENCES

For \(q	o\infty\) and \(q=o(Q)\),

\[
\boxed{
\Pr\left(X_I<rac\alpha2q^2ight)=o(1).
}

#### Proof

At most \(Q\) cells of \(\mathcal A_Q\) are diagonal. Therefore

\[
\mathbb E X_I
\ge
rac{(q)_2}{(Q)_2}igl(\alpha Q^2-Qigr)
=
(\alpha-o(1))q^2.
\]

Represent \(I\) by the first \(q\) entries of a uniform random permutation of
\([Q]\). Exchanging one selected index with one unselected index changes \(X_I\)
by at most \(4q\): only cells using one of the two exchanged indices can change.
The standard bounded-differences inequality for random permutations gives

\[
\Pr\left(|X_I-\mathbb EX_I|>tight)
\le
2\exp\left(-crac{t^2}{q^3}ight)
\]

for an absolute constant \(c>0\). Take \(t=\alpha q^2/3\). The right side is
\(\exp(-\Omega_\alpha(q))=o(1)\), and the expectation exceeds
\(5\alpha q^2/6\) for all sufficiently large \(m\). ∎

Only the vanishing tail is used; constants in the permutation inequality are
irrelevant.

## 2. Joint choice with source diagnostics

### Theorem PP3oa -- PROVED

Use the adaptive size \(q\) from PP3nq. There is a \(q\)-subset \(I\) such that
simultaneously:

1. 
   \[
   |\mathcal A_Q\cap(I	imes I)|
   \ge
   rac\alpha2q^2;
   \]
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
\boxed{
|\mathcal A_{q'}|
\ge
\left(rac\alpha2-o(1)ight)q^2
=
\Omega_\alpha((q')^2).
}

#### Proof

Deleting one endpoint index removes at most \(2q\) cells from a tied endpoint
rectangle. Since only \(o(q)\) indices are deleted, at most \(o(q^2)\) target
cells disappear. Apply PP3oa. ∎

## 4. Fully connected line-conversion endpoint

### Corollary PP3oc -- PROVED

Let a macroscopic Hall rectangle contain a quadratic recapture target core on a
resource bank of size \(Q\). After adaptive thinning and complete source-validity
cleanup, at least one of the following holds.

1. A source-valid endpoint derangement strictly decreases the owner-line load.
2. One nonaxis geometric line contains
   \[
   \Omega(q^{1/3})
   \]
   pairwise resource-disjoint owner/replacement endpoint cells and their owner
   candidate points.

#### Proof

PP3oa--PP3ob preserve a fixed positive target density. Apply PP3nt, PP3nu, and
PP3ny on the retained bank. ∎

Thus the line-energy chain no longer assumes that a dense Hall core survives the
secondary thinning; it is preserved jointly with every source-validity
requirement.