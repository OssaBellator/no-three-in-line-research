# Weighted cross-centre residual dispersion

**Branch:** `research/alternating-core-chain`

AC3aj--AC3ak return blockers attached to **different alternative values of one centre block**. Those blockers are not simultaneously activated. Pairwise-disjoint residual scopes are therefore a geometric dispersion certificate, not by themselves an installable repair batch.

This note corrects the earlier over-strong interpretation of AC3al and gives the next valid weighted routers.

## Weighted target records

Let \(\mathcal A\) be a finite family of alternative centre targets. Each target \(a\in\mathcal A\) has:

- a nonnegative current weight \(w(a)\);
- one chosen current-aligned hard blocker;
- an effective residual scope \(S(a)\) satisfying
  \[
  1\le |S(a)|\le2.
  \]

Put

\[
W=\sum_{a\in\mathcal A}w(a).
\]

No conclusion below treats the weights as independent payments or claims that distinct target phases can be executed together.

## AC3al — weighted residual-dispersion dichotomy — PROVED

For every integer \(\Delta\ge1\), one of the following holds:

1. some current residual block belongs to more than \(\Delta\) chosen blocker scopes; or
2. there is a subfamily \(\mathcal M\subseteq\mathcal A\) whose residual scopes are pairwise disjoint and whose weight satisfies
   \[
   \boxed{
   \sum_{a\in\mathcal M}w(a)
   \ge
   \frac{W}{2\Delta-1}.
   }
   \]

### Proof

Assume the first outcome fails. Form the intersection graph on \(\mathcal A\), joining two targets when their chosen residual scopes meet. A scope has at most two blocks, and each block occurs in at most \(\Delta\) scopes. Hence every vertex has degree at most

\[
2(\Delta-1).
\]

Greedy colouring uses at most \(2\Delta-1\) colours. Each colour class has pairwise-disjoint residual scopes. A heaviest colour class carries at least the displayed fraction of \(W\). \(\square\)

The family \(\mathcal M\) is a weighted dispersion certificate across alternative target phases. It becomes an actual bank only after a separate multi-target construction specifies compatible centre actions.

## AC3am — finite-label common-residual router — PROVED

Suppose instead that every blocker in a weighted family \(\mathcal F_x\) contains one fixed current residual literal \((x,\omega_x)\). Each blocker carries one of at most \(K\) arithmetic role labels and has effective residual rank one or two.

For a rank-two blocker, write \(y(a)\) for its unique secondary residual block. Put

\[
W_x=\sum_{a\in\mathcal F_x}w(a).
\]

Then one label-and-rank class \(\mathcal C\) has weight at least

\[
\boxed{
W(\mathcal C)\ge\frac{W_x}{2K}.
}
\]

Moreover, exactly one of the following applies.

1. **Rank-one fixed exclusion.** Every blocker in \(\mathcal C\) consists only of the common current literal. Thus one arithmetic role contains a fixed-exclusion target family of weight at least \(W_x/(2K)\).
2. **Repeated residual pair.** For a chosen integer \(\rho\ge1\), some secondary block \(y\) occurs in more than \(\rho\) blockers of \(\mathcal C\). Hence the same current residual pair \((x,y)\), with one arithmetic role label, is paired with more than \(\rho\) distinct centre targets.
3. **Secondary dispersion.** The class contains a subfamily \(\mathcal D\) with pairwise-distinct secondary blocks and
   \[
   \boxed{
   \sum_{a\in\mathcal D}w(a)
   \ge
   \frac{W(\mathcal C)}{\rho}
   \ge
   \frac{W_x}{2K\rho}.
   }
   \]

### Proof

Partition \(\mathcal F_x\) by its at most \(K\) arithmetic labels and by residual rank. There are at most \(2K\) classes, proving the first display.

If the heaviest class has rank one, outcome 1 holds. Otherwise all its blockers have one secondary block. If one secondary block has multiplicity greater than \(\rho\), outcome 2 holds. If every multiplicity is at most \(\rho\), choose the heaviest blocker for each represented secondary block. The chosen blockers have pairwise-distinct secondary blocks, and each chosen weight pays for at most \(\rho\) members of its secondary-block class. Their total weight is therefore at least \(W(\mathcal C)/\rho\). \(\square\)

## Frontier after AC3al--AC3am

The cross-centre output is now quantitatively localized without conflating alternative target phases:

- bounded residual degree gives a large residual-disjoint target family;
- a common residual literal localizes to one finite arithmetic role;
- that role is rank one, repeats one exact residual pair, or disperses over distinct secondary blocks.

The remaining step is arithmetic. The selected role must be identified as an orbit, carry, quotient, or denominator configuration, after which OP2, RI, BDA, or a genuinely multi-target alternating construction must supply the executable transition.

## Finite check

`scripts/verify_ac_cross_centre_weighted_router.py` exhausts small positive-weight residual-scope systems. It verifies the weighted \(1/(2\Delta-1)\) dispersion bound, the \(1/(2K)\) label-and-rank localization, and the repeated-pair versus \(1/\rho\) secondary-dispersion alternative.