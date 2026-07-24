# Activated literal stars and exact phase-bucket routing

OP2k reduces every conditioned heavy-kernel pattern to a canonical
antichain star.  AC3's independent active-literal audit identifies the
same object from the alternating side: a failed one-block phase change
returns one target phase together with the checks which that phase can
activate.

For rank-at-most-three canonical checks, this object has more structure
than a generic kernel star.  Once the centre phase is fixed, every
activated check has residual rank at most two, and every residual
literal agrees with the current assignment.  The star is therefore an
ordinary transversal problem.  A maximal residual matching either gives
many disjoint blocker arms or a bounded auxiliary phase change which
blocks the entire bucket.

The second part of the note proves exact phase averaging.  All defects
destroyed by changing one variable are destroyed by every alternative
phase, while possible creations partition by their unique target
phase.  Thus a failed one-block decoder pays every target bucket; it
does not return an unweighted collection of convenient phase labels.

## Activated phase buckets

Let \(\mathcal C\) be a finite family of canonical checks.  Check \(C\)
has nonempty scope \(S_C\) and forbids one partial assignment \(f_C\).
Give checks nonnegative weights \(w_C\).

Fix a full current assignment

\[
\omega\in\prod_{x\in V}\mathcal A_x,
\]

a variable \(v\), its current phase

\[
q=\omega_v,
\]

and a target phase \(a\ne q\).  Define the **activated target bucket**

\[
\boxed{
\mathcal B_\omega(v,a)
=
\left\{
C\in\mathcal C:
v\in S_C,\ f_C(v)=a,
\omega_x=f_C(x)\ \text{for every }x\in S_C\setminus\{v\}
\right\}.
}
\]

These are exactly the checks which are currently satisfied because
\(\omega_v\ne a\) and become violated after the one-block phase change
\(v:q\mapsto a\).

For \(C\in\mathcal B_\omega(v,a)\), put

\[
R_C=S_C\setminus\{v\}.
\]

Assume the OP2g irreducible setting and rank at most three.  Then

\[
1\leq |R_C|\leq2.
\]

All forbidden residual literals are aligned:

\[
\boxed{
f_C|_{R_C}=\omega|_{R_C}.
}
\]

If the original checks form an antichain, OP2k with
\(H=\{v\}\) also says that residualization inside one target bucket is
injective and that the residual checks remain an antichain.  The
matching and transversal statements below only need alignment and the
rank bound.

## OP2l -- exact matching/transversal form of one target bucket

Let

\[
\mathcal R_\omega(v,a)=\{R_C:C\in\mathcal B_\omega(v,a)\}.
\]

A residual matching is a subfamily of pairwise disjoint scopes.
A transversal is a variable set meeting every residual scope.
Write

\[
\nu(v,a)=
\max\{|\mathcal M|:\mathcal M\subseteq\mathcal R_\omega(v,a)
\text{ is a matching}\}
\]

and

\[
\tau(v,a)=
\min\{|X|:X\cap R\ne\varnothing
\text{ for every }R\in\mathcal R_\omega(v,a)\}.
\]

The empty bucket has \(\nu=\tau=0\).

### Theorem OP2l -- PROVED

For every nonempty activated target bucket:

\[
\boxed{
\nu(v,a)\leq\tau(v,a)\leq2\nu(v,a).
}
\]

More constructively, let \(\mathcal M\) be any maximal residual matching
and put

\[
X=\bigcup_{R\in\mathcal M}R.
\]

Then \(X\) is a transversal and

\[
\boxed{
|X|\leq2|\mathcal M|.
}
\]

Change every \(x\in X\) to any phase

\[
\omega'_x\in\mathcal A_x\setminus\{\omega_x\},
\]

and change the centre to \(\omega'_v=a\), leaving every other phase
unchanged.  Every check in \(\mathcal B_\omega(v,a)\) is satisfied by
\(\omega'\).  Every phase change is an O1 row-column-preserving state
change when the variables are orbit blocks.

Consequently, for every integer \(m\geq1\), the maximal-matching
algorithm returns one of the following constructive outputs:

1. a family of \(m\) activated checks with pairwise disjoint residual
   scopes; or
2. an auxiliary set \(X\) of size at most \(2(m-1)\) whose phase
   changes block the entire target bucket.

The first output certifies that every assignment which sets \(v=a\)
and blocks the full bucket must change at least \(m\) residual variables.

### Proof

Every transversal meets each member of a maximum matching, and the
matching scopes are pairwise disjoint.  Hence \(\nu\leq\tau\).

If a residual scope \(R_C\) were disjoint from
\(X=\bigcup\mathcal M\), it could be added to \(\mathcal M\),
contradicting maximality.  Thus \(X\) is a transversal.  Every residual
scope has size at most two, so

\[
|X|
\leq
\sum_{R\in\mathcal M}|R|
\leq2|\mathcal M|.
\]

After the centre is changed to \(a\), a check
\(C\in\mathcal B_\omega(v,a)\) is violated exactly when every
\(x\in R_C\) remains at its current phase \(\omega_x=f_C(x)\).
The transversal \(X\) meets \(R_C\), and every member of \(X\) is
changed away from its current phase.  Hence every bucket check contains
a mismatch and is satisfied.

If a maximum matching has size at least \(m\), retain \(m\) members.
Otherwise any maximal matching has size at most \(m-1\), and its union
is the required auxiliary set.  Finally, pairwise disjoint residual
scopes require distinct mismatching variables in every transversal,
proving the lower bound in the first output. \(\square\)

### Exact scope of the conclusion

The theorem blocks every check activated by the original one-block
change \(v:q\mapsto a\).  Checks outside that bucket may react to the
auxiliary changes on \(X\).  They are not discarded: their exact
creation and destruction terms must be included in the next OP3 drift
audit or in a scope-complete conflict graph.  Thus conclusion 2 is a
bounded product-state candidate, not an unconditional global
improvement.

Likewise, conclusion 1 is a genuine disjoint-arm obstruction, but it
does not declare those arms separately paid.  Payment is supplied by
the phase-bucket identity below.

## OP2m -- paid matching or a deeper current-literal kernel

Retain one activated bucket and put

\[
W(v,a)
=
\sum_{C\in\mathcal B_\omega(v,a)}w_C.
\]

For a residual variable \(x\ne v\), define

\[
\mu_{v,a}(x)
=
\sum_{\substack{C\in\mathcal B_\omega(v,a)\\x\in R_C}}w_C.
\]

Because the bucket is activated at \(\omega\), every term in this sum
uses the same literal

\[
(x,\omega_x).
\]

### Theorem OP2m -- PROVED

Let \(\mathcal M\) be any maximal residual matching and
\(X=\bigcup_{R\in\mathcal M}R\).  Then

\[
\boxed{
W(v,a)
\leq
\sum_{x\in X}\mu_{v,a}(x)
\leq
2|\mathcal M|\max_x\mu_{v,a}(x).
}
\]

Consequently, at every threshold \(\Delta>0\), one of the following
holds:

1. some current residual literal \((x,\omega_x)\) extends the centre
   literal \((v,a)\) and carries paid bucket weight
   \[
   \boxed{\mu_{v,a}(x)>\Delta;}
   \]
2. the bucket contains a residual matching of size at least
   \[
   \boxed{
   \left\lceil\frac{W(v,a)}{2\Delta}\right\rceil.
   }
   \]

If all bucket weights are equal and the maximum number of bucket checks
using one residual variable is \(d\), a maximal matching retains at
least a \(1/(2d)\) fraction of the checks and of their total weight.

### Proof

OP2l shows that \(X\) meets every residual scope.  Thus every check
weight in \(W(v,a)\) occurs at least once in
\(\sum_{x\in X}\mu_{v,a}(x)\), proving the first inequality.  There are
at most \(2|\mathcal M|\) variables in \(X\), proving the second.

If no residual load exceeds \(\Delta\), the display gives

\[
|\mathcal M|
\geq
\frac{W(v,a)}{2\Delta}.
\]

Integrality yields the ceiling.  Alignment identifies a high residual
variable load with the single current phase literal
\((x,\omega_x)\), so conclusion 1 is a genuine depth-two canonical
kernel rather than an unlabelled degree concentration.

In the equal-weight case, cancel the common weight.  Then
\(\max_x\mu_{v,a}(x)=d w\), while
\(W(v,a)=|\mathcal B_\omega(v,a)|w\), giving the final assertion.
\(\square\)

OP2m is the paid version of the matching/transversal router.  It uses
no independence or negative-dependency assumption.  A low residual
literal load forces many disjoint arms; failure returns one explicitly
paid two-literal kernel whose residual rank is at most one and therefore
enters OP2g unit propagation after conditioning those two literals.

## OP3c -- exact phase-bucket averaging

Return to an arbitrary finite canonical check family with nonnegative
weights and current assignment \(\omega\).  For variable \(v\), define
the destroyed incident weight

\[
D_\omega(v)
=
\sum_{\substack{C\in\mathcal C\\
                  v\in S_C,\ \omega|_{S_C}=f_C}}
w_C.
\]

Every check in this sum is currently violated.  For
\(a\ne q=\omega_v\), define

\[
C_\omega(v,a)
=
\sum_{C\in\mathcal B_\omega(v,a)}w_C,
\qquad
E_\omega(v)
=
\sum_{a\ne q}C_\omega(v,a).
\]

### Theorem OP3c -- PROVED

For every target phase \(a\ne q\):

\[
\boxed{
\Phi(\omega^{v\leftarrow a})-\Phi(\omega)
=
C_\omega(v,a)-D_\omega(v).
}
\]

In particular, the destroyed term is independent of the target phase,
and the creation buckets are disjoint with total

\[
\boxed{
\sum_{a\ne q}C_\omega(v,a)=E_\omega(v).
}
\]

If \(h_v=|\mathcal A_v|\geq2\), some target phase satisfies

\[
\boxed{
C_\omega(v,a)
\leq
\frac{E_\omega(v)}{h_v-1}.
}
\]

Hence

\[
\boxed{
(h_v-1)D_\omega(v)>E_\omega(v)
}
\]

guarantees a strict one-block improvement.

Conversely, if no one-block phase change at \(v\) strictly improves the
potential, then every target bucket is quantitatively paid:

\[
\boxed{
C_\omega(v,a)\geq D_\omega(v)
\quad\text{for every }a\ne q,
}
\]

and therefore

\[
\boxed{
E_\omega(v)\geq(h_v-1)D_\omega(v).
}
\]

### Proof

A currently violated check containing \(v\) agrees with \(\omega\) on
every literal, so its literal at \(v\) is \(q\).  Changing \(v\) to any
\(a\ne q\) destroys it.  Thus the destroyed weight is
\(D_\omega(v)\) for every target.

A currently satisfied check is created by changing only \(v\) to \(a\)
exactly when its other literals already agree with \(\omega\) and its
literal at \(v\) is \(a\).  This is precisely membership in
\(\mathcal B_\omega(v,a)\).  A canonical check has only one target
literal at \(v\), so the target buckets are disjoint.  OP3a now gives
the drift identity and summing gives the total creation identity.

Averaging \(h_v-1\) nonnegative bucket weights gives the displayed
target.  Its creation weight is smaller than \(D_\omega(v)\) under the
strict boxed hypothesis, so its drift is negative.  If no target has
negative drift, the drift identity instead gives
\(C_\omega(v,a)\geq D_\omega(v)\) for every target; summing proves the
last assertion. \(\square\)

### Hard feasibility buckets

Let \(\mathcal H\) be a separate family of currently satisfied hard
canonical checks.  A target \(a\ne q\) is hard-safe for a one-block
change exactly when

\[
\mathcal B^\mathcal H_\omega(v,a)=\varnothing.
\]

If every target is unsafe, choosing one hard blocker from each nonempty
bucket gives exactly \(h_v-1\) blockers with distinct centre literals.
Each bucket separately has the rank-two transversal form of OP2l.

More generally, every target phase has one of two explicit records:

1. a nonempty aligned hard blocker bucket, entering OP2l; or
2. a hard-safe soft bucket with its exact drift
   \(C_\omega(v,a)-D_\omega(v)\).

Thus a failed admissible one-block decoder cannot hide feasibility and
collateral in one undifferentiated phase label.

## Combined local router

For an irreducible rank-at-most-three orbit-phase core and one current
variable \(v\):

1. Exact OP3c bucket inspection returns an improving hard-safe target
   whenever one exists.
2. Every hard-unsafe target returns an aligned rank-at-most-two blocker
   star.
3. Every hard-safe but non-improving target has soft bucket weight at
   least \(D_\omega(v)\).
4. OP2l turns each returned bucket into either a bounded auxiliary
   product state or many disjoint residual arms.
5. OP2m turns a paid bucket into either many disjoint arms or one paid
   depth-two current-literal kernel.

This is a total local phase-bucket router.  It does not yet prove OP3
termination: auxiliary phase changes can activate checks outside the
original bucket, and a large disjoint-arm family still needs geometric
expansion or a scope-complete paid selection.  What it removes is the
previously unclassified step between a failed phase flip and those two
precise outputs.

For the alternating-core interface, a large hard active-literal family
now has a canonical interpretation.  Each target literal is either
absent, admits a bounded transversal correction, or carries a disjoint
blocker family.  A failed soft flip additionally pays its whole target
bucket at the current destroyed-weight scale.  RI and BDA delegation is
still terminal only when their own structured collateral hypotheses
hold.

`scripts/verify_phase_literal_star_router.py` exhausts small aligned
rank-two residual stars, compares matching and transversal numbers,
executes the maximal-matching auxiliary state, checks the paid
literal-load inequality, and verifies every phase-bucket drift and
averaging identity against brute-force potential differences.
