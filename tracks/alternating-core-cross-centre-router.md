# Cross-centre hard blockers and safe-target payment

AC3ag--AC3ai route all residual contexts attached to one fixed centre
literal.  The other large-chart obstruction is many distinct target
literals at the same phase block.  At a fixed current assignment this
case is substantially more rigid than a general phase CSP.

Every hard-unsafe target has an activated blocker whose residual
literals all equal the current phases.  Selecting one blocker per
target produces an ordinary rank-two scope system.  Its targets either
have unconditional effectively rank-one blockers, disperse over
support-disjoint residual arms, or share one current residual literal.
Meanwhile, the soft creation buckets of different hard-safe targets
are disjoint, so failure of every safe phase change pays their full
aggregate weight without reuse.

## Current cross-centre buckets

Retain the canonical rank-at-most-three setup of AC3ad.  Let

\[
\omega\in\prod_{x\in V}\mathcal A_x
\]

be hard-feasible, fix a block \(v\), and write \(q=\omega_v\).  For
each target \(a\in\mathcal A_v\setminus\{q\}\), let

\[
\mathcal B^\mathcal H_\omega(v,a),
\qquad
\mathcal B^\mathcal S_\omega(v,a)
\]

be its activated hard and weighted soft buckets.

Partition the target phases into

\[
T_{\rm safe}
=
\{a:\mathcal B^\mathcal H_\omega(v,a)=\varnothing\},
\qquad
T_{\rm unsafe}
=
\{a:\mathcal B^\mathcal H_\omega(v,a)\ne\varnothing\}.
\]

Put

\[
s=|T_{\rm safe}|,
\qquad
u=|T_{\rm unsafe}|,
\qquad
s+u=|\mathcal A_v|-1.
\]

For every unsafe target \(a\), first inspect the effective residuals

\[
\widehat R_C
=
\{x\in S_C\setminus\{v\}:|\mathcal A_x|\geq2\}
\qquad
(C\in\mathcal B^\mathcal H_\omega(v,a)).
\]

Let \(U_0\subseteq T_{\rm unsafe}\) contain the targets whose hard
bucket has an empty effective residual.  Such a target cannot be
repaired by changing other phase blocks.  For each
\(a\in U_+=T_{\rm unsafe}\setminus U_0\), choose one blocker
\(C_a\) with \(\widehat R_{C_a}\ne\varnothing\).

All of its residual literals are current-aligned:

\[
\boxed{
f_{C_a}(x)=\omega_x
\quad(x\in\widehat R_{C_a}).
}
\]

## AC3aj -- cross-target blocker matching or a common residual literal

Choose any maximal subfamily
\(\mathcal M\subseteq\{C_a:a\in U_+\}\) whose effective residual
scopes are pairwise disjoint, and put

\[
X=\bigcup_{C_a\in\mathcal M}\widehat R_{C_a}.
\]

For a mutable residual block \(x\), define its target degree

\[
d(x)
=
|\{a\in U_+:x\in\widehat R_{C_a}\}|.
\]

### Theorem AC3aj -- PROVED

The set \(X\) meets every selected unsafe-target blocker and

\[
\boxed{|X|\leq2|\mathcal M|.}
\]

If \(U_+\ne\varnothing\), moreover,

\[
\boxed{
|U_+|
\leq
\sum_{x\in X}d(x)
\leq
2|\mathcal M|\max_x d(x).
}
\]

Consequently, at every integer threshold \(\Delta\geq1\), one of:

1. one current residual literal \((x,\omega_x)\) is paired with more
   than \(\Delta\) **distinct centre target phases** \(a\);
2. the unsafe targets contain at least
   \[
   \boxed{
   \left\lceil\frac{|U_+|}{2\Delta}\right\rceil
   }
   \]
   blockers with pairwise disjoint effective residual scopes; or
3. \(U_+=\varnothing\), so every unsafe target has an effectively
   rank-one hard blocker.

If fewer than half of the \(u\) unsafe targets lie in \(U_0\), the
second conclusion strengthens to

\[
\boxed{
|\mathcal M|
\geq
\left\lceil\frac{u}{4\Delta}\right\rceil
}
\]

whenever conclusion 1 fails.

### Proof

Maximality makes \(X\) a transversal of the chosen blocker scopes, and
rank at most three gives \(|X|\leq2|\mathcal M|\).  Every
\(a\in U_+\) has its chosen scope meeting \(X\), so it contributes at
least once to \(\sum_{x\in X}d(x)\).  The second inequality follows
from the size bound on \(X\).

If every target degree is at most \(\Delta\), rearranging gives the
matching bound.  Otherwise the common block \(x\) has the same
residual literal \((x,\omega_x)\) in every incident blocker, while the
centre literals \((v,a)\) are distinct by construction.  This is
conclusion 1.

Finally, \(|U_0|<u/2\) implies \(|U_+|>u/2\).  Substitute this into the
first matching bound and use integrality. \(\square\)

The blockers in conclusion 2 correspond to alternative values of the
same centre block \(v\); they are not claimed to be simultaneously
activated.  Their pairwise-disjoint residual supports are a geometric
dispersion certificate across alternative target phases.

## AC3ak -- total current-block router

Retain the soft destroyed weight

\[
D_\omega(v)
=
\sum_{\substack{C\in\mathcal S\\
                  v\in S_C,\ \omega|_{S_C}=f_C}}
w_C
\]

and creation weights

\[
C_\omega(v,a)
=
\sum_{C\in\mathcal B^\mathcal S_\omega(v,a)}w_C.
\]

### Theorem AC3ak -- PROVED

Exactly one of the following statements applies.

1. Some hard-safe target \(a\) has
   \[
   C_\omega(v,a)<D_\omega(v)
   \]
   and is an improving one-block O1 phase change.
2. No hard-safe target improves.  Then
   \[
   \boxed{
   \sum_{a\in T_{\rm safe}}C_\omega(v,a)
   \geq
   sD_\omega(v).
   }
   \]
   The target buckets in this sum are pairwise disjoint check
   families, and every individual target has the AC3af
   effectively-rank-one/depth-two/residual-matching route.

Simultaneously, the unsafe targets have the AC3aj route.  In
particular, if \(h=|\mathcal A_v|\), no safe target improves, and
\(\Delta\geq1\) is any integer, then at least one of the following
quantitative records holds:

1. \(2s\geq h-1\), and the disjoint safe-target creation mass is at
   least
   \[
   \boxed{\frac{(h-1)D_\omega(v)}2};
   \]
2. \(2u>h-1\) and at least \(\lceil u/2\rceil\) target phases have
   effectively rank-one hard blockers;
3. \(2u>h-1\), one current residual literal is paired with more than
   \(\Delta\) unsafe centre phases; or
4. \(2u>h-1\), and there are at least
   \[
   \boxed{
   \left\lceil\frac{u}{4\Delta}\right\rceil
   }
   unsafe-target blockers with pairwise disjoint effective residual
   scopes.

### Proof

AC3ad gives the exact drift

\[
\Phi(\omega^{v\leftarrow a})-\Phi(\omega)
=
C_\omega(v,a)-D_\omega(v)
\]

for every hard-safe target.  If none improves, each creation weight is
at least \(D_\omega(v)\).  Canonical checks use one unique literal at
\(v\), so soft buckets belonging to different target phases are
disjoint.  Summing proves the safe-target display, and AC3af applies
inside each bucket.

Either \(2s\geq h-1\) or \(2u>h-1\).  The former gives record 1.  In
the latter case, either \(2|U_0|\geq u\), giving record 2, or
\(|U_0|<u/2\).  Apply the strengthened AC3aj alternative to obtain
record 3 or 4. \(\square\)

## Remaining interface

AC3aj--AC3ak close the distinct hard-literal family **at the current
phase context**.  A target is improving, contributes a disjoint paid
soft bucket, has a fixed hard exclusion, or belongs to an explicit
cross-centre hard fan/matching.

The remaining arithmetic work is now attached to two concrete
objects:

1. a common current residual literal paired with many centre phases;
2. many alternative centre phases whose hard blockers have
   support-disjoint residual arms.

AC3v must still include the complete external scopes of any proposed
multi-block corrections.  OP2/RI/BDA classification must use the
actual orbit, quotient, carry, or denominator labels of these objects;
the present theorem does not call an unlabelled fan terminal.

`scripts/verify_ac_cross_centre_router.py` exhausts abstract
safe/unit/rank-one/rank-two blocker records through five target phases,
checks every threshold form of AC3aj, and enumerates canonical
rank-at-most-three hard/soft phase buckets to verify the disjoint
safe-target payment identity.
