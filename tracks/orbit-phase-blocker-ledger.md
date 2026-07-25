# State-qualified ledger for rank-three blockers

OP4j turns every switch-disjoint rank-three matching into canonical
product-carry records.  This note integrates those records into the
state-qualified ledger of OP3k.

The integration needs a separate role tag.  An OP3j factor-fan
signature belongs to an improving correction centre, whereas an OP4j
signature belongs to a blocker factor.  Equal arithmetic tuples in the
two roles do not represent the same event and are never identified.

No syndrome payment is manufactured here.  The unweighted theorem is
an exact finite-growth statement.  Its weighted refinement applies
only when the rank-three source factors already carry certified
external weights.

## Canonical blocker tokens

Fix one bounded-channel seed.  Let \(\Sigma_3\) be the finite set of
canonical OP4j records

\[
\sigma_3(F)
=
\bigl(
\operatorname{profile}(F),
\operatorname{product\mbox{-}carry}(F)
\bigr)
\]

represented by its real rank-three source factors.  The profile is
part of the record; equal numerical carry levels in different channel
profiles are different signatures.

For a phase snapshot \(\omega\), the corresponding blocker token is

\[
\boxed{
(\omega,\mathsf{rank3},\sigma_3(F)).
}
\]

Maintain a persistent ledger

\[
\mathcal L_3
\subseteq
\Omega\times\{\mathsf{rank3}\}\times\Sigma_3.
\]

For one OP4f matching \(M\) at \(\omega\), write

\[
M_\sigma
=
\{F\in M:\sigma_3(F)=\sigma\},
\qquad
b_\sigma=|M_\sigma|.
\]

Let

\[
\Delta_p=\max_{1\leq n<p^2}\tau(n).
\]

### Lemma OP4k.0 -- PROVED

Every signature fibre in one matching satisfies

\[
\boxed{b_\sigma\leq\Delta_p.}
\]

Consequently, if \(M\) has size \(\nu\) and represents \(R\) distinct
canonical blocker signatures, then

\[
\boxed{
R\geq\left\lceil\frac{\nu}{\Delta_p}\right\rceil.
}
\]

### Proof

The profile and signature fix the two endpoint product-carry levels
used in the canonical OP4j route.  OP4j.0 makes the selected endpoint
pairs disjoint.  Each level contains at most \(\Delta_p\) points by
SC1, so an endpoint-disjoint family contains at most \(\Delta_p\)
pairs.  Summing \(b_\sigma\leq\Delta_p\) over the \(R\) represented
records gives \(\nu\leq R\Delta_p\). \(\square\)

Notice that retaining the exact profile removes the \(T_q\)
pigeonhole loss from this ledger count.  OP4j still supplies the
stronger conclusion inside one selected profile when that form is
needed by an arithmetic endpoint.

## OP4k -- growth or current recurrent blocker fibre

At the current snapshot, put

\[
K_\omega
=
\left|
\{\sigma:(\omega,\mathsf{rank3},\sigma)\in\mathcal L_3\}
\right|.
\]

### Theorem OP4k -- PROVED

For an OP4f matching \(M\) of size \(\nu>0\), exactly one of the
following ledger actions is available.

1. **Blocker-ledger growth.**  At least one represented token is new.
   Insert every new represented token.  The number inserted is at
   least
   \[
   \boxed{
   \max\left\{
   1,\,
   \left\lceil\frac{\nu}{\Delta_p}\right\rceil-K_\omega
   \right\}.
   }
   \]
2. **Current recurrent fibre.**  Every represented token is already
   in the ledger.  One old signature \(\sigma\) has
   \[
   \boxed{
   \left\lceil\frac{\nu}{K_\omega}\right\rceil
   \leq b_\sigma\leq\Delta_p.
   }
   \]
   The returned fibre retains its source factors, three protected
   supports, forbidden orientations, channel profile, and all OP4g
   carry routes.

The second case is impossible when \(K_\omega=0\).

### Proof

Let \(S\) be the set of signatures represented by \(M\).
OP4k.0 gives

\[
|S|\geq\left\lceil\frac{\nu}{\Delta_p}\right\rceil.
\]

At most \(K_\omega\) members of \(S\) were already present at
\(\omega\).  Thus, if \(S\) contains a new record, then

\[
|S\setminus\mathcal L_3(\omega)|
\geq
\max\left\{
1,\,
\left\lceil\frac{\nu}{\Delta_p}\right\rceil-K_\omega
\right\}.
\]

If it contains no new record, then \(S\) is a nonempty subset of the
\(K_\omega\) old records.  Pigeonholing the \(\nu\) matching factors
over \(S\) gives

\[
\max_{\sigma\in S}b_\sigma
\geq
\left\lceil\frac{\nu}{|S|}\right\rceil
\geq
\left\lceil\frac{\nu}{K_\omega}\right\rceil.
\]

The upper bound is OP4k.0.  All provenance is copied from the OP4j
records. \(\square\)

## Weighted capacity gate

Suppose the source factors have externally certified weights
\(p_F\geq0\).  Put

\[
W=\sum_{F\in M}p_F.
\]

### Corollary OP4k.1 -- PROVED

For every \(\lambda>0\), at least one of the following holds.

1. Some source factor has \(p_F>\lambda\).
2. OP4k inserts a new blocker token.
3. Every token is old, and a current recurrent fibre has weight at
   least
   \[
   \boxed{\frac{W}{K_\omega}}
   \]
   while containing at most \(\Delta_p\) factors.  In this case
   \[
   \boxed{
   W\leq\lambda\Delta_p K_\omega.
   }
   \]

In particular,

\[
\boxed{
W>\lambda\Delta_p K_\omega
}
\]

forces a heavy source factor or blocker-ledger growth.

### Proof

Return conclusion 1 if it occurs.  Otherwise every signature fibre
contains at most \(\Delta_p\) factors of weight at most \(\lambda\),
so it has weight at most \(\lambda\Delta_p\).

If OP4k grows the ledger, return conclusion 2.  Otherwise the
represented signatures form a nonempty subset of the \(K_\omega\)
old records.  Their weights sum to \(W\), so the heaviest has weight at
least \(W/K_\omega\).  Summing the per-fibre capacity over at most
\(K_\omega\) fibres gives the final upper bound. \(\square\)

The qualification “externally certified” is essential.  OP4a clause
logic and OP4f matching size do not attach current-syndrome weight to a
source factor.

## Combined state ledger

Let \(\Sigma_{\rm fan}\) be the OP3k correction-centre signature
universe.  Use the disjoint role-tagged universe

\[
\boxed{
\Sigma_{\rm all}
=
\bigl(\{\mathsf{fan}\}\times\Sigma_{\rm fan}\bigr)
\;\dot\cup\;
\bigl(\{\mathsf{rank3}\}\times\Sigma_3\bigr).
}
\]

The persistent state ledger is

\[
\mathcal L_{\rm all}
\subseteq
\Omega\times\Sigma_{\rm all}.
\]

### Corollary OP4k.2 -- PROVED

Across decoder rounds there are at most

\[
\boxed{
|\Omega|
\bigl(
|\Sigma_{\rm fan}|+|\Sigma_3|
\bigr)
}
\]

strict ledger-growth rounds.  A no-growth OP3j fan return remains the
current paid high-reuse correction class of OP3k.  A no-growth OP4j
matching return is the current recurrent blocker fibre of OP4k.
Neither return combines objects from different phase snapshots or
different geometric roles.

### Proof

The displayed disjoint union is the finite token universe.  Every
growth round inserts a previously absent token.  The two no-growth
statements are OP3k and OP4k applied only to objects generated at the
current snapshot. \(\square\)

Put

\[
B_{\rm all}
=
|\Omega|
\bigl(
|\Sigma_{\rm fan}|+|\Sigma_3|
\bigr).
\]

### Corollary OP4k.3 -- PROVED

Suppose every nonterminal combined decoder round either:

1. decreases the integer syndrome potential \(\Phi\) by at least one;
2. leaves \(\Phi\) fixed and inserts a new role-tagged state token; or
3. leaves \(\Phi\) fixed with no new token and exits immediately to
   the current OP3k recurrent-correction interface or the current OP4k
   recurrent-blocker interface.

Before zero syndrome or one of those named exits, the decoder has at
most

\[
\boxed{
(B_{\rm all}+1)\Phi_0
+B_{\rm all}-|\mathcal L_{{\rm all},0}|
}
\]

nonterminal rounds.

### Proof

Apply OP3b with

\[
\Xi=|\mathcal L_{\rm all}|.
\]

It lies between zero and \(B_{\rm all}\).  A token insertion strictly
increases \(\Xi\); a syndrome step strictly decreases \(\Phi\); and a
no-growth recurrence exits instead of continuing.  The OP3b rank
gives the displayed bound. \(\square\)

## Exact interface after OP4k

The former “rank-three ledger integration” obligation is now closed.

1. A large OP4f matching inserts quantitatively many state-qualified
   blocker signatures unless all of its signatures are already
   current-old.
2. A current-old return is localized to one exact profile/signature
   fibre containing at most \(\Delta_p\) point-disjoint factors.
3. With external source-factor weights, excessive recurrent mass
   forces either one heavy factor or a new token.
4. The fan and blocker ledgers share a finite state space but remain
   role-disjoint.

What remains arithmetic is the treatment of the bounded recurrent
blocker fibre, the OP4m heavy-factor/recurrent-defect outputs, RI5
conversion, action-kernel, and wide-CSP frontiers.  OP4k does not
claim that a recurrent blocker fibre is itself absorbable.

`scripts/verify_phase_blocker_ledger.py` exhausts abstract fibre
occupancies up to the divisor cap, checks the growth and recurrence
bounds for every old-token subset, and exercises new-token, recurrent,
heavy-factor, weighted-capacity, snapshot-separation, and role-tag
outputs on real \(p=11\) rank-three matchings.  It also exhausts the
combined finite-descent rank on small syndrome and ledger capacities.
