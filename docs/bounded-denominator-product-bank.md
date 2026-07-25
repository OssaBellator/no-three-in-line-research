# Exact product-bank collateral criterion

BDA2a supplies a collision-free permutation bank on one chamber block,
and BDA3a extracts compatible blocks when labelled conflict mass is
linear. The product of those local banks has an exact global collateral
formula, including triples that meet several blocks.

Let \(B_1,\ldots,B_s\) be row-, column-, and support-disjoint selected
blocks. Block \(i\) has size \(t_i\geq7\) and a probability measure
\(\mu_i\) satisfying the BDA2a cylinder bound

\[
\Pr_{\mu_i}(Q\subseteq M_i)
\leq
\frac{128}{(t_i)_{|Q|}}
\]

for every compatible local prescription \(Q\) of rank one, two, or three.
Put \(\kappa_i(0)=1\) and

\[
\kappa_i(r)=\frac{128}{(t_i)_r}\qquad(1\leq r\leq3).
\]

Choose the local states independently.

Let \(\mathcal T\) be the full family of possible new certificates,
including cross-block certificates. For \(T\in\mathcal T\), let
\(r_i(T)\) be the number of prescribed replacement cells of \(T\) in
block \(i\). Since a certificate is a triple,
\(\sum_i r_i(T)\leq3\).

## BDA3b -- product-bank improvement criterion

### Theorem BDA3b -- PROVED

Suppose the selected old cells deterministically destroy distinct paid
certificates of total weight \(W\). Let \(F\) be fixed collateral not
depending on the local bank choices, and give every possible new
certificate \(T\) weight \(w(T)\geq0\). Define

\[
\mathcal C=
\sum_{T\in\mathcal T}
w(T)\prod_{i=1}^s\kappa_i(r_i(T)).
\]

Then the expected potential drift of the independent product bank is at
most

\[
\boxed{F-W+\mathcal C.}
\]

In particular, if

\[
\boxed{W>F+\mathcal C,}
\]

some joint row-column-preserving state strictly lowers the weighted triple
potential.

### Proof

Each paid old certificate counted in \(W\) contains a selected old cell
and is absent from every replacement state. Distinctness prevents double
counting its destroyed weight.

For a possible new certificate \(T\), occurrence requires its local
prescription in every block it meets. Independence gives

\[
\Pr(T\text{ occurs})
=
\prod_i
\Pr_{\mu_i}(Q_i(T)\subseteq M_i)
\leq
\prod_i\kappa_i(r_i(T)).
\]

This includes certificates meeting two or three distinct blocks; no
cross term is discarded. Linearity of expectation gives expected created
weight at most \(\mathcal C\). Adding fixed collateral and subtracting
the deterministically destroyed weight proves the drift bound. If the
bound is negative, at least one product state has negative drift.
\(\square\)

## Interface to BDA3

BDA3b completes the probabilistic product-state step once the
\(q\)-stripe arithmetic bounds the explicit normalized sum
\(\mathcal C\). Together with BDA3a, the remaining alternatives are now:

1. linear total labelled conflict mass, followed by a compatible block
   family and the displayed product-bank test;
2. paid mass concentrated on high-conflict blocks, which must be
   classified as a \(q\)-periodic template;
3. failure of the inequality because a quantified family of cross-block
   certificates carries at least \(W-F\), which itself is the structured
   high-collateral output to classify.

The theorem does not replace the arithmetic estimate with independence:
independence is used only after blocks are compatible, and every
cross-block candidate is present in \(\mathcal C\).

`scripts/verify_bda_product_bank.py` checks product cylinder probabilities
and exact expected collateral for two exhaustive local permutation banks.
