# Carry dispersion from rank-three matchings

OP4f separates the rank-three protected-bank frontier into:

1. a large matching of width-three source factors; or
2. a bounded switch kernel whose conditioned residuals are OP4d
   implication instances.

The matching side already has enough disjointness for a direct
arithmetic conclusion.  No local-lemma or generic codegree hypothesis
is needed.

## From switch-disjointness to point-disjointness

Recall that the O1 candidate universe is a family of disjoint orbit
blocks.  Every candidate cell belongs to one block and has one phase in
that block.

A width-three OP4a clause comes from a real collinear factor meeting
three protected correction supports, once in each support.  The
protected supports \(E_i\) are pairwise disjoint sets of block
variables.

### Lemma OP4j.0 -- PROVED

The source factors in an OP4f hypergraph matching are pairwise
point-disjoint.

### Proof

Two matching hyperedges share no protected support.  Each width-three
source factor uses one block variable from each of its three support
vertices.  Since all protected supports are pairwise disjoint, the two
factor scopes share no block variable.

The O1 blocks themselves have disjoint candidate-cell sets.  Therefore
two block-disjoint factor scopes cannot contain the same geometric
point. \(\square\)

This conclusion is stronger than merely saying that the Boolean
clauses use different switch names.

## Canonical channel profile

Let \(\mathcal C_{\rm act}\) be the active hyperbola-channel set and put

\[
q=|\mathcal C_{\rm act}|.
\]

All points have nonzero coordinates.  Three distinct collinear points
cannot lie on one modular hyperbola, since a line meets \(xy=a\) in at
most two affine points.  Thus every source factor has one of two
profiles.

1. **Profile \(2+1\).**  Two endpoints lie on \(H_a\) and the singleton
   point lies on \(H_b\), where \(a\ne b\).  Choose the singleton as
   anchor and retain the unordered product-carry signature
   \[
   \boxed{
   \{\kappa_a(P),\kappa_a(Q)\}.
   }
   \]
   The exact profile is the ordered channel pair \((a,b)\).
2. **Profile \(1+1+1\).**  The points lie on three different channels.
   Order the channel labels, choose the least as the canonical anchor,
   and retain the ordered product-carry signature of the other two
   points, including their channel labels.

There are at most

\[
\boxed{
T_q=q(q-1)+\binom q3
}
\]

exact canonical profiles.

The profile choice is only a deterministic way to select one of the
three OP4g carry routes.  It does not discard the other routes.

## OP4j -- rank-three carry router

Let \(M\) be an OP4f matching of \(\nu\) width-three factors, all at one
current phase snapshot.  Put

\[
\Delta_p=\max_{1\leq n<p^2}\tau(n).
\]

### Theorem OP4j -- PROVED

The matching contains one exact channel-profile class \(M_0\) with

\[
\boxed{
|M_0|\geq\frac{\nu}{T_q}.
}
\]

If \(B\) is the number of product-carry signatures represented by that
class, then

\[
\boxed{
B\geq\frac{|M_0|}{\Delta_p}
\geq\frac{\nu}{T_q\Delta_p}.
}
\]

More generally, give the factors certified nonnegative weights of
total \(W\).  For any \(\lambda>0\), exactly one of the following
outputs can be returned.

1. One rank-three source factor has weight greater than
   \[
   \boxed{\lambda}.
   \]
2. One exact channel profile has weight at least \(W/T_q\) and
   represents at least
   \[
   \boxed{
   \frac{W}{T_q\lambda\Delta_p}
   }
   distinct product-carry signatures.

Every signature retains its source factor, its three protected
supports, its forbidden orientations, its channel profile, and its
three OP4g carry routes.

### Proof

Pigeonhole the \(\nu\) factors over the at most \(T_q\) profiles to get
\(M_0\).

Fix one product-carry signature in \(M_0\).  In a mixed-channel route,
the two selected endpoints lie in two fixed product-carry levels.  In
a same-channel route, they lie in the union of the two levels in the
unordered signature.  Every level has at most \(\Delta_p\) points by
SC1.

By OP4j.0, the selected endpoint pairs are pairwise endpoint-disjoint.
For two different levels, an endpoint-disjoint family has size at most
the smaller level size, hence at most \(\Delta_p\).  When the levels
agree, every factor uses two distinct points of that one level, giving
the same bound.  Thus one signature supports at most \(\Delta_p\)
matching factors.  Dividing \(|M_0|\) by this capacity proves the count
statement.

For the weighted statement, first return any factor heavier than
\(\lambda\).  Otherwise every factor has weight at most \(\lambda\).
Pigeonholing weight gives a profile of weight at least \(W/T_q\), and
one signature in that profile carries at most
\(\lambda\Delta_p\).  Dividing gives the displayed signature count.
\(\square\)

## Exact interface after OP4j

OP4f's large-matching branch is no longer an anonymous
“rank-three dispersion” obligation.

1. A large matching gives quantified state-current product-carry
   signature growth through OP4j.
2. A weighted matching either exposes one heavy source factor or gives
   the same growth with an explicit payment bound.  As in OP4i, the
   weights must be certified externally; clause logic does not create
   syndrome payment.
3. A small matching still gives OP4f's kernel of size
   \(3\nu\).  Exact conditioning returns the OP4d--OP4i rank-two
   interfaces.

The remaining integration task is to admit these rank-three
source-factor signatures into the state-qualified ledger, or to route a
recurrent signature class to the existing factor-fan/carry machinery.
No new rank-three local-lemma estimate is required.

`scripts/verify_phase_rank_three_router.py` enumerates all 4,448 real
non-single-channel triples in the nonzero \(p=11\) grid.  It verifies
the canonical profile/signature record in 1,466 classes, checks the
two-level divisor capacity, and exercises three-channel, two-channel,
mixed-profile, weighted carry-growth, and heavy-factor matching
outputs.
