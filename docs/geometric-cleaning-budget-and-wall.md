# Protected-wall obstruction and the exact partner budget

This note closes one required falsification case and isolates a quantitative
invariant needed by GC1 and GC3.

## GC1 obstruction -- installed blocks can cover the pool

### Proposition GC1-wall -- PROVED

GC1 is false without a bound on the coordinates occupied by installed
absorber or active-core blocks.

### Proof

Use rows and columns indexed by \(\mathbb Z/n\mathbb Z\). Let one
permutation layer be

\[
R=\{(i,i):i\in\mathbb Z/n\mathbb Z\}
\]

and take the target batch \(B=\{(0,0)\}\). A rectangle switch with a
possible partner \((j,j)\), \(j\ne0\), must remove that partner and replace
the two diagonal cells by \((0,j)\) and \((j,0)\).

Install immutable active-core blocks covering every point
\((j,j)\), \(j\ne0\). (They may be grouped into any fixed bounded block
size; singleton blocks are not essential.) Every possible partner is now
unavailable solely because moving it violates an installed block. Thus the
target has zero admissible partners in every pool of current-layer points.

For any fixed constant \(c>0\), choose a dyadic \(H\geq1/c\). Then
\(|B|=1\leq cH\), so the stated size hypothesis of GC1 holds, while its
\(\Theta(n)\) partner conclusion fails. A second permutation layer can be
chosen arbitrarily; it cannot restore a partner forbidden by the installed
blocks. \(\square\)

The counterexample does not use high-line creation or layer collisions.
Those restrictions can only remove additional partners.

## Necessary protection-load hypothesis

Any corrected GC1 statement must include, or derive from paid incidence, a
bound of the following kind. For each target \(b\), if \(P_0\) is the
proposed common pool, then

\[
\bigl|\{u\in P_0:u\text{ is frozen by an installed block relevant to }b\}\bigr|
\leq \delta_{\rm block}|P_0|.
\]

The collision, high-line, and block contributions must have total density
strictly below one. Merely saying that every installed block has bounded
size is insufficient, because linearly many disjoint bounded blocks give
the wall above.

## GC3a -- paid pool-depletion lemma

Let \(P_0\) be a partner pool with \(|P_0|\geq\alpha n\). During a sequence
of batches, let \(c_i\) be the number of partners made permanently
unavailable by batch \(i\), and let \(w_i>0\) be paid certified excess
destroyed by that batch.

### Lemma GC3a -- PROVED

Assume

\[
c_i\leq\kappa w_i
\]

for every batch and that a nonnegative potential satisfies

\[
\Psi_{i+1}\leq\Psi_i-w_i.
\]

Then

\[
\sum_i c_i\leq\kappa\Psi_0.
\]

In particular, if

\[
\Psi_0\leq\frac{\alpha}{2\kappa}n,
\]

at least \(\alpha n/2\) partners remain throughout the process.

### Proof

Telescoping the potential inequality and using \(\Psi_i\geq0\) gives

\[
\sum_i w_i\leq\Psi_0.
\]

Therefore

\[
\sum_i c_i\leq\kappa\sum_iw_i\leq\kappa\Psi_0.
\]

Subtracting this bound from \(|P_0|\) proves the final assertion.
\(\square\)

### Density stability corollary

Suppose initially every target has at least
\((1-\delta)|P_0|\) admissible partners, and the only loss is deletion of
pool elements. If GC3a leaves at least \(|P_0|/2\) elements, then every
unchanged target has at least

\[
(1-2\delta)|P|
\]

admissible partners in the remaining pool \(P\).

Indeed, the number of initially inadmissible elements is at most
\(\delta|P_0|\leq2\delta|P|\), and deletion cannot create an inadmissible
element among those retained.

## Consequence for the track

The phrase "charged to the potential decrease" in GC3 must be instantiated
by a bound such as \(c_i\leq\kappa w_i\), and the entry value of the
scale-local potential must be \(O(n)\) with a sufficiently small constant,
or partners must be safely reusable. A global \(O(n\log n)\) syndrome
bound alone does not protect a linear pool through all scales.
