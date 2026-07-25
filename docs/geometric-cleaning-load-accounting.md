# Partner blockers, latent-shadow obstruction, and exceptional-anchor charging

This note proves the combinatorial accounting needed around GC1--GC3.  The
geometric task is to establish the numerical blocker and charge bounds for
the actual rectangle candidate sets.

## GC1a -- exact blocker union bound

Fix a target \(b\) and a common proposed partner pool \(P\).  Let

\[
I_{\rm coll}(b),\quad
I_{\rm high}(b),\quad
I_{\rm block}(b),\quad
I_{\rm core}(b)
\]

be the partners forbidden respectively by layer collision, creation of a
height-\(\geq2H\) line, installed absorber blocks, and active-core
contracts.

### Lemma GC1a -- PROVED

If

\[
|I_j(b)|\leq\delta_j|P|
\]

for all four blocker types, then \(b\) has at least

\[
\boxed{
\left(1-\delta_{\rm coll}-\delta_{\rm high}
-\delta_{\rm block}-\delta_{\rm core}\right)|P|
}
\]

individually admissible partners.

The same conclusion holds uniformly for a target batch when the four
bounds hold for every target with the same pool \(P\).

### Proof

The inadmissible set is contained in the union of the four blocker sets.
The union bound gives its size at most
\(\sum_j\delta_j|P|\).  Every partner outside that union satisfies all four
admissibility conditions. \(\square\)

Thus the corrected GC1 problem has four separate geometric estimates.  The
installed-block wall from the preceding note shows that
\(\delta_{\rm block}<1\) cannot be omitted or inferred from bounded block
size alone.

## GC2 wall -- uniform latent shadow survives small target deletion

Let \(A\) be a set of unchanged anchors and \(B\) a target batch.  Write
\(w(a,b)\geq0\) for the contribution of target \(b\)'s candidate cells to
the pair-shadow at anchor \(a\).  After deleting targets
\(D\subseteq B\), the residual abstract load is

\[
\lambda_D(a)=\sum_{b\in B\setminus D}w(a,b).
\]

### Proposition GC2-wall -- PROVED

Suppose one anchor \(a_0\) has

\[
w(a_0,b)\geq L
\quad\text{for every }b\in B.
\]

Then every deletion set with \(|D|\leq\epsilon|B|\) leaves

\[
\boxed{
\lambda_D(a_0)\geq(1-\epsilon)|B|L.
}
\]

In particular, the cap \(\lambda_D(a_0)\leq Cn\) is impossible when
\((1-\epsilon)|B|L>Cn\).

### Proof

At least \((1-\epsilon)|B|\) target contributions remain, and each is at
least \(L\). \(\square\)

This proposition explains why an unweighted latent secant bank cannot be
"cleaned" merely by deleting a small fraction of targets.  In the actual
GC2 trichotomy, such a uniformly high anchor must be converted into the
paid endpoint-disjoint bank or structured-core outcome.  The conversion
must use current syndrome incidence; the numerical cap cannot hold by
averaging alone.

## GC3b -- exceptional anchors are bounded by paid charge

Suppose the process creates distinct exceptional anchors over a sequence
of batches.  Assume:

1. declaring an anchor exceptional is accompanied by at least
   \(\theta n\) units of paid syndrome incidence;
2. each unit of original syndrome incidence is used for at most \(R\)
   exceptional-anchor declarations; and
3. the total original paid incidence available to this accounting is
   \(W\).

### Lemma GC3b -- PROVED

The number of distinct newly exceptional anchors is at most

\[
\boxed{\frac{RW}{\theta n}.}
\]

### Proof

If \(m\) anchors are declared, their declarations require at least
\(m\theta n\) charged incidences.  Assumption 2 permits at most \(RW\)
charges in total.  Hence \(m\theta n\leq RW\). \(\square\)

Together with GC3a, this gives two auditable stability budgets:

- permanent partner loss is bounded by paid potential descent;
- exceptional-anchor creation is bounded by paid incidence with explicit
  reuse multiplicity.

GC3 remains open until the geometric switch construction supplies
constants \(\kappa,\theta,R\) compatible with the scale-local entry
potential.
