# Physical-cause concentration inside weighted source-hole stars

**Branch:** `research/superregular-resampling`

SRR2ao--SRR2ar show that large exceptional endpoint weight concentrates on one weighted source-hole star. This note resolves that star into one finite physical cause.

Fix a threshold endpoint set `S`. Every occurrence-faithful hole incidence `(a,b)` with `b in S cap H(a)` carries endpoint weight `lambda_b` and one least cause from an ordered dictionary

\[
\mathcal C=\{c_1,\ldots,c_K\}.
\]

The dictionary may contain line, blocker, boundary, owner, protected-event, host, context and occurrence causes.

## SRR2as -- exact source-cause partition -- PROVED

For source `a` and cause `c_j`, define

\[
M_{a,j}
=
\sum_{\substack{b\in S\cap H(a)\\
\text{least cause}(a,b)=c_j}}
\lambda_b.
\]

Then

\[
\boxed{
\mathcal M_S
=
\sum_{a\in A}\sum_{j=1}^K M_{a,j}.
}
\]

### Proof

Every weighted hole incidence has exactly one source and exactly one least cause. Therefore the source-cause buckets partition the occurrence-faithful incidence multiset. QED.

## SRR2at -- one heavy labeled source star -- PROVED

There exist `a in A` and `j in {1,...,K}` such that

\[
\boxed{
M_{a,j}
\ge
\frac{\mathcal M_S}{|A|K}.
}
\]

Equivalently, one source and one physical cause carry a `1/(|A|K)` fraction of the complete weighted hole mass.

### Proof

Pigeonhole the identity from SRR2as over the `|A|K` buckets. QED.

## SRR2au -- exceptional-budget labeled dichotomy -- PROVED

Fix a multiplicity threshold `tau` and exceptional endpoint-weight budget `Lambda`. One of the following holds:

1. the exceptional endpoint weight is at most `Lambda`;
2. one source-cause bucket has weight greater than
   \[
   \boxed{
   \frac{(\tau+1)\Lambda}{|A|K}.
   }
   \]

### Proof

If branch 1 fails, SRR2ao gives `mathcal M_S>(tau+1)Lambda`. Apply SRR2at. QED.

## SRR2av -- complete labeled trimmed-flow router -- PROVED

For one low-cost threshold set and one chosen `tau`, one exact continuation holds:

1. trim the high-multiplicity endpoints, retain the SRR2al Hall-deficiency bound and charge their weight by SRR2ao;
2. one source and one least line/blocker/boundary/owner/protected/context cause carry weight at least `mathcal M_S/(|A|K)`;
3. one source-cause refinement, occurrence alias or endpoint weight record is not fixed;
4. or one retained Hall cut realizes the residual deficiency bound.

Thus the exceptional endpoint branch is reduced to a finite labeled source-local obstruction, suitable for direct current payment, owner concentration or a cause-specific capacity ticket.

## Corrected SRR3 frontier

Remaining work is to bound the actual weighted hole mass or pay the finitely labeled source-cause stars produced above. No diffuse exceptional-weight branch remains.

## Finite check

`scripts/verify_srr_labeled_hole_star_payment.py` enumerates small weighted incidence systems, verifies the source-cause partition and checks the `1/(|A|K)` and exceptional-budget concentration bounds.