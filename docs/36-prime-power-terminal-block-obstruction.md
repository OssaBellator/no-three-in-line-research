# Terminal-block first-moment obstruction

CMR21 gives a full two-layer product bank, but the uniform product measure is
not by itself a no-three proof. The terminal block already has too much
internal line mass when the prime base is at least five.

Let

\[
N=p^k,
\qquad p\text{ odd},
\qquad k\ge2,
\qquad a=p^{k-1}.
\]

The terminal column block is

\[
X_*=\{0,a,2a,\ldots,(p-1)a\}.
\]

Its first-layer row set is the same set of multiples of `a`, because inversion
and multiplication by \(c_{k-1}\) permute the nonzero residues modulo `p` and
fix zero as a set. Its companion row set is a translate

\[
Z_*=\{1,1+a,\ldots,1+(p-1)a\}.
\]

Thus, within either layer, the terminal candidate block is an affine copy of
the complete `p` by `p` permutation host.

## 1. Slope-one and slope-minus-one certificate mass

### Theorem CMR23 — PROVED

Under the independent uniform terminal-block permutations in the two layers,
the expected number of selected real triples lying entirely inside the
terminal block is at least

\[
\frac{p-1}{3}.
\]

Consequently, for every odd prime base \(p\ge5\), the unrestricted CMR21
first-moment mass is greater than one before any cross-block certificate is
counted. Therefore the implication

\[
\mathbb E\Phi<1
\]

cannot prove a saturated no-three state for this uniform bank.

### Proof

Work in one layer and divide both coordinates by `a`; translating the
companion rows by `-1` does not change collinearity. Consider only lines of
slope `+1` and `-1` in the `p` by `p` integer box.

For one fixed slope, the line lengths are

\[
p,
\quad 1,1,
\quad 2,2,
\quad\ldots,
\quad p-1,p-1.
\]

Hence the number of compatible candidate triples on lines of that slope is

\[
\binom p3+2\sum_{j=1}^{p-1}\binom j3
=
\binom p3+2\binom p4.
\]

Every compatible three-cell prescription in one permutation block has
probability \(1/(p)_3\). The two slope families are disjoint on triples, so
one layer contributes at least

\[
\frac{2\left(\binom p3+2\binom p4\right)}{(p)_3}
=
\frac{p-1}{6}.
\]

The two layer permutations are independent and each contributes the same
amount. Their terminal-only expectation is therefore at least

\[
2\cdot\frac{p-1}{6}=\frac{p-1}{3}.
\]

For \(p\ge5\), this is at least `4/3`. ∎

## 2. Required correction

CMR23 does not refute the block bank. It refutes only the unconditioned
first-moment finish. A successful decoder must modify the terminal treatment
in one of the following ways:

1. restrict each terminal permutation to a local no-three family;
2. install a fixed saturated no-three pair on the terminal `p` by `p` block;
3. use a local-lemma or resampling measure that forbids terminal internal
   triples while retaining spread on external cells;
4. enlarge the terminal block and couple it to neighbouring valuation blocks
   through an absorber.

After the terminal internal triples are removed, the remaining CMR22 mass is
cross-block or mixed-block collateral. That is the correct quantity for the
next concentration theorem.

The finite check is in
[`scripts/verify_prime_power_terminal_mass.py`](../scripts/verify_prime_power_terminal_mass.py).
