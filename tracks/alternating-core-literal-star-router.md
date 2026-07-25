# Current-context literal-star routing

AC3aa--AC3ac isolate large hard phase-literal families and paid heavy
soft literals as the remaining canonical O1 chart obstruction.  A
literal name alone is not yet a repair object: the other literals of
its checks must match one current context before changing that phase
can activate them.

This note performs the exact routing after such a context has been
localized.  It includes rank-one checks explicitly.  Every
context-active target is either hard-forbidden, improves immediately,
or carries collateral at the current destroyed-weight scale.  A
rank-at-most-three target bucket then reduces to a rank-at-most-two
matching/transversal problem.

## Current target buckets

Let \(V\) be a finite phase-block set.  Block \(v\) has alphabet
\(\mathcal A_v\), and let

\[
\omega\in\prod_{v\in V}\mathcal A_v
\]

be the current assignment.  A canonical check
\(C=(S_C,f_C)\) forbids exactly the partial assignment \(f_C\).
Let \(\mathcal H\) be a hard-check family and assume that \(\omega\)
violates none of its members.  Let \(\mathcal S\) be a weighted
soft-check family, with \(w_C\geq0\), and put

\[
\Phi(\alpha)
=
\sum_{C\in\mathcal S}
w_C\mathbf 1_{\{\alpha|_{S_C}=f_C\}}.
\]

Fix a block \(v\), write \(q=\omega_v\), and take \(a\ne q\).
For either check family \(\mathcal C\), define its activated target
bucket

\[
\boxed{
\mathcal B^\mathcal C_\omega(v,a)
=
\left\{
C\in\mathcal C:
v\in S_C,\ f_C(v)=a,
\omega_x=f_C(x)\ (x\in S_C\setminus\{v\})
\right\}.
}
\]

These are exactly the checks which become violated when only \(v\)
changes from \(q\) to \(a\).  Their residual scopes are

\[
R_C=S_C\setminus\{v\}.
\]

Every residual literal is current-aligned:

\[
\boxed{f_C|_{R_C}=\omega|_{R_C}.}
\]

Only blocks which actually have an alternative phase can block such a
check.  Define the **effective residual**

\[
\widehat R_C
=
\{x\in R_C:|\mathcal A_x|\geq2\}.
\]

When the original rank is at most three,
\(|\widehat R_C|\leq|R_C|\leq2\).  An empty effective residual is an
unavoidable target check: it is literally rank one, or all of its
other phase blocks are rigid.  If every phase block under discussion
has at least two phases, then \(\widehat R_C=R_C\).

## AC3ad -- exact hard/soft phase-bucket audit

Define the current soft weight destroyed by changing \(v\):

\[
D_\omega(v)
=
\sum_{\substack{C\in\mathcal S\\
                  v\in S_C,
                  \omega|_{S_C}=f_C}}
w_C.
\]

For \(a\ne q\), put

\[
C_\omega(v,a)
=
\sum_{C\in\mathcal B^\mathcal S_\omega(v,a)}w_C,
\qquad
E_\omega(v)
=
\sum_{a\ne q}C_\omega(v,a).
\]

### Theorem AC3ad -- PROVED

For every target phase \(a\ne q\):

\[
\boxed{
\Phi(\omega^{v\leftarrow a})-\Phi(\omega)
=
C_\omega(v,a)-D_\omega(v).
}
\]

The creation buckets are disjoint over \(a\), so

\[
\boxed{
\sum_{a\ne q}C_\omega(v,a)=E_\omega(v).
}
\]

Moreover:

1. the target is hard-safe for the one-block change exactly when
   \[
   \boxed{\mathcal B^\mathcal H_\omega(v,a)=\varnothing;}
   \]
2. a hard-safe target with
   \(C_\omega(v,a)<D_\omega(v)\) is an immediately improving
   row-column-preserving O1 phase change;
3. if no hard-safe target improves, every hard-safe target satisfies
   \[
   \boxed{C_\omega(v,a)\geq D_\omega(v);}
   \]
4. without hard constraints, some target has
   \(C_\omega(v,a)\leq E_\omega(v)/(|\mathcal A_v|-1)\), and hence
   \[
   \boxed{
   (|\mathcal A_v|-1)D_\omega(v)>E_\omega(v)
   }
   \]
   guarantees an improving phase.

### Proof

A currently violated soft check containing \(v\) has
\(f_C(v)=q\), so every alternative phase destroys it.  A currently
satisfied check is created by the one-block change precisely when it
belongs to the displayed target bucket.  This proves the drift
identity.

Every canonical check uses only one forbidden literal at \(v\), so the
target buckets are disjoint and their weights sum to \(E_\omega(v)\).
The same characterization without weights proves the hard-safety
claim.  The next two assertions follow from the drift identity, and
averaging the \(|\mathcal A_v|-1\) creation buckets proves the final
assertion. \(\square\)

This theorem uses actual current potential, not latent literal count.
A hard or heavy literal which is not activated in the localized
context is not assigned payment by this result.

## AC3ae -- rank-two residual transversal

Fix one activated hard or soft bucket.  First split off its empty
effective residuals.  A hard empty effective residual makes the target
unconditionally hard-forbidden inside the phase bank.  A soft empty
effective residual is unavoidable collateral once \(v=a\).

Let \(\mathcal R^+\) be the multiset of nonempty effective residual
scopes.
Thus every member has size one or two.  Let \(\mathcal M\) be any
maximal pairwise-disjoint subfamily and put

\[
X=\bigcup_{R\in\mathcal M}R.
\]

### Theorem AC3ae -- PROVED

The set \(X\) meets every member of \(\mathcal R^+\), and

\[
\boxed{|X|\leq2|\mathcal M|.}
\]

Changing \(v\) to \(a\) and every \(x\in X\) to any noncurrent phase
blocks every check with nonempty effective residual in the original
target bucket.

Consequently, at every integer \(m\geq1\), the bucket returns one of:

1. \(m\) checks with pairwise-disjoint nonempty residual scopes;
2. a set of at most \(2(m-1)\) auxiliary blocks which blocks every
   nonunit bucket check; or
3. an empty effective residual, retained as a hard target exclusion or
   fixed soft collateral.

### Proof

If a residual scope missed \(X\), it could be added to the maximal
matching.  Thus \(X\) is a transversal.  Each matching member has size
at most two, proving the cardinality bound.

Every residual literal equals the current phase.  Every element of
\(X\) is mutable by definition.  After changing it away from its
current phase, every effective residual scope contains a mismatch, so
its parent check is satisfied even though \(v=a\).  If
\(|\mathcal M|\geq m\), retain \(m\) members; otherwise the displayed
size bound is at most \(2(m-1)\).  Empty effective residuals have no
mutable auxiliary literal and give conclusion 3. \(\square\)

The auxiliary assignment blocks this bucket exactly.  AC3v must still
include every outside factor and feasibility scope touched by the
auxiliary changes before the state is called globally legal or
improving.

## AC3af -- paid residual matching or depth-two kernel

For a weighted soft target bucket, let

\[
W_0
=
\sum_{\substack{C\in\mathcal B^\mathcal S_\omega(v,a)\\
                 \widehat R_C=\varnothing}}
w_C,
\qquad
W_+
=
\sum_{\substack{C\in\mathcal B^\mathcal S_\omega(v,a)\\
                 \widehat R_C\ne\varnothing}}
w_C.
\]

For a mutable \(x\ne v\), define its aligned residual-literal load

\[
\mu_{v,a}(x)
=
\sum_{\substack{C\in\mathcal B^\mathcal S_\omega(v,a)\\
                 x\in\widehat R_C}}
w_C.
\]

### Theorem AC3af -- PROVED

For the maximal matching and transversal \(X\) of AC3ae,

\[
\boxed{
W_+
\leq
\sum_{x\in X}\mu_{v,a}(x)
\leq
2|\mathcal M|\max_x\mu_{v,a}(x).
}
\]

At every threshold \(\Delta>0\), one of the following holds:

1. some current residual literal \((x,\omega_x)\), together with
   centre literal \((v,a)\), carries
   \[
   \boxed{\mu_{v,a}(x)>\Delta;}
   \]
2. the bucket contains a residual matching of size at least
   \[
   \boxed{
   \left\lceil\frac{W_+}{2\Delta}\right\rceil;
   }
   \]
3. \(W_+ =0\), so all target collateral is the explicit effectively
   rank-one amount \(W_0\).

If the target is hard-safe and nonimproving, then

\[
W_0+W_+
=
C_\omega(v,a)
\geq
D_\omega(v).
\]

Therefore it has the sharper paid alternative:

1. effectively rank-one target collateral
   \[
   \boxed{W_0\geq D_\omega(v)/2;}
   \]
2. one depth-two current-literal kernel of load \(>\Delta\); or
3. a residual matching of size at least
   \[
   \boxed{
   \left\lceil\frac{D_\omega(v)}{4\Delta}\right\rceil.
   }
\]

### Proof

The transversal \(X\) meets every nonempty residual scope.  Hence each
check weight in \(W_+\) occurs at least once in the sum of literal
loads over \(X\).  There are at most \(2|\mathcal M|\) terms, proving
the first display.  If every load is at most \(\Delta\), rearrangement
gives the matching bound; otherwise conclusion 1 holds.

For a hard-safe nonimproving target, AC3ad gives
\(W_0+W_+\geq D_\omega(v)\).  Either
\(W_0\geq D_\omega(v)/2\), or
\(W_+\geq D_\omega(v)/2\).  Apply the first part to the latter case:
if no load exceeds \(\Delta\), the matching size is at least
\[
\left\lceil
\frac{D_\omega(v)/2}{2\Delta}
\right\rceil
=
\left\lceil\frac{D_\omega(v)}{4\Delta}\right\rceil.
\]
\(\square\)

## Interface to the canonical role frontier

AC3ad--AC3af turn every **current-context-localized** O1 literal into
one of the following exact outputs:

1. an improving one-block O1 phase;
2. an effectively rank-one hard exclusion or paid collateral term;
3. a bounded auxiliary transversal candidate;
4. a paid depth-two current-literal kernel; or
5. a quantitatively large residual-disjoint blocker family.

The last two outputs enter AC3v--AC3x and the existing
anchor/carry/BDA/RI role dictionary.  They are not generic “many
literals.”

[`alternating-core-global-literal-contexts.md`](alternating-core-global-literal-contexts.md)
handles the complementary case in which one fixed centre literal has
large global weight spread across different contexts.  AC3ag--AC3ai
return effectively rank-one mass, a paid simultaneously activatable
context bank, a depth-two literal, or a one-block phase fan.

What remains arithmetic is cross-centre expansion for many distinct
hard literals and scope-complete collateral control or structured
classification of those last three global outputs.  No payment is
inferred from a phase label which is inactive at the current context.

`scripts/verify_ac_literal_star_router.py` exhausts small rank-at-most
three canonical check systems, compares every phase-bucket drift with
brute force, checks hard safety and effectively rank-one targets,
including rigid auxiliary alphabets, exhausts
rank-one/rank-two residual hypergraphs through four auxiliary blocks,
and verifies the weighted matching, \(D/2\), and
\(D/(4\Delta)\) alternatives.
