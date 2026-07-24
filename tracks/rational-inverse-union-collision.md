# Collision localization for unions of subgroup cosets

RI2a gives maximal target-coset coverage in the small-index range. When
the subgroup index is larger, the individual Weil error can dominate.
The exact collision involution still gives a uniform alternative: loss
of target cosets forces many full collision pairs, and those pairs
concentrate on one pair of source cosets.

Let \(H\leq\mathbb F_p^\times\) have order \(h\), and let

\[
C=\bigcup_{i=1}^s x_iH
\]

be a union of \(s\) distinct full cosets. Put

\[
D=C\cap D_r=C\setminus\{1,r\},
\qquad
e=|C\setminus D|\leq2,
\]

and let

\[
k=N_H(F_r(D)).
\]

## RI2b -- universal half-coverage and collision mass

### Theorem RI2b -- PROVED

The image meets at least

\[
\boxed{
k\geq
\left\lceil\frac{sh-e}{2h}\right\rceil
}
\]

target \(H\)-cosets. More precisely, its full nonfixed collision-pair
count satisfies

\[
\boxed{
|\mathcal P_r(D)|
\geq
(s-k)h-e.
}
\]

### Proof

RI0 gives

\[
|F_r(D)|\geq\left\lceil\frac{|D|}{2}\right\rceil
=\left\lceil\frac{sh-e}{2}\right\rceil.
\]

The image lies in \(k\) target cosets, containing at most \(kh\) values,
which proves the first box.

RI1a gives the exact identity

\[
|\mathcal P_r(D)|=|D|-|F_r(D)|.
\]

Using \(|D|=sh-e\) and \(|F_r(D)|\leq kh\) proves the second box.
\(\square\)

Thus a loss of one target coset below the source count already forces at
least \(h-e\) full collision pairs. The bound is uniform in the subgroup
index and does not use a character-sum error term.

## RI2c -- one heavy source-coset pair

Classify a collision pair by the unordered pair of source cosets
containing its endpoints. There are at most

\[
\binom{s+1}{2}
\]

such types.

### Corollary RI2c -- PROVED

Some unordered source-coset pair \(\{x_iH,x_jH\}\), allowing \(i=j\),
contains at least

\[
\boxed{
\frac{\bigl((s-k)h-e\bigr)_+}{\binom{s+1}{2}}
}
\]

full collision pairs.

Writing their endpoints as

\[
x=x_i u,\qquad z=x_jv,\qquad u,v\in H,
\]

every one of these pairs lies on the single bilinear subgroup curve

\[
\boxed{
x_ix_j uv-r(x_i u+x_jv)+r=0.
}
\]

### Proof

Partition \(\mathcal P_r(D)\) by its unordered source-coset pair and
apply the pigeonhole principle with RI2b. The collision equation from
RI0 is

\[
(x-r)(z-r)=r(r-1).
\]

Expansion followed by the substitutions \(x=x_i u\) and \(z=x_jv\)
gives the displayed curve. \(\square\)

## Interface to the remaining RI2 problem

For every proposed threshold \(k\), RI2b--RI2c give an exact alternative:

- the image meets more than \(k\) target cosets; or
- one source-coset pair supports the displayed quantified collision
  curve.

RI2 therefore no longer needs to analyze arbitrary many-coset
recombination at once. The unresolved large-index theorem is to bound or
classify high incidence on this two-coset bilinear curve and convert its
exceptional cases to RI3--RI5.

`scripts/verify_rational_union_collision.py` exhaustively checks the
image, collision-mass, and heavy coset-pair bounds on small primes.
