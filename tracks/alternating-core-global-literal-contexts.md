# Global literal stars and realizable context extraction

AC3ad--AC3af close a phase-literal bucket once all of its other
literals agree with the current assignment.  The preceding global
chart can instead return one centre literal carrying checks with many
different residual contexts.  This note removes that gap by exploiting
the rank-three bound before any current-state claim is made.

A global literal star has residual rank at most two.  Residual contexts
on disjoint mutable block sets are simultaneously realizable, while a
failure of disjointness concentrates the star on one residual block.
After one dyadic weight regularization, bounded residual-block degree
preserves a definite fraction of the paid weight in a disjoint context
bank.  High degree refines exactly to a paid depth-two literal or many
different phase labels at one block.

## Global centre stars

Let \(V\) be a finite phase-block set, with nonempty alphabets
\(\mathcal A_x\).  A canonical check \(C=(S_C,f_C)\) has nonempty
scope \(S_C\subseteq V\), rank at most three, and one forbidden partial
assignment \(f_C\).

Fix a centre literal \((v,a)\) and define its global star

\[
\mathcal S(v,a)
=
\{C:v\in S_C,\ f_C(v)=a\}.
\]

Give its checks nonnegative weights \(w_C\).  For each star check put

\[
R_C=S_C\setminus\{v\},
\qquad
\widehat R_C
=
\{x\in R_C:|\mathcal A_x|\geq2\}.
\]

The effective residual omits rigid blocks.  Every realizable literal
on such a block is its unique phase, so rigid blocks never create a
context inconsistency and cannot be changed to block a check.

A subfamily \(\mathcal M\subseteq\mathcal S(v,a)\) is
**context-disjoint** when its nonempty effective residual scopes are
pairwise disjoint.

## AC3ag -- exact global context matching

Let \(\mathcal S^+\) be the star checks with
\(\widehat R_C\ne\varnothing\).  Choose any maximal
context-disjoint subfamily \(\mathcal M\subseteq\mathcal S^+\) and put

\[
X=\bigcup_{C\in\mathcal M}\widehat R_C.
\]

### Theorem AC3ag -- PROVED

The set \(X\) meets every effective residual scope in
\(\mathcal S^+\), and

\[
\boxed{|X|\leq2|\mathcal M|.}
\]

Moreover, all checks in \(\mathcal M\), together with every
effectively rank-one check in the star, can be activated
simultaneously by one phase assignment with \(v=a\).

Consequently, for every integer \(m\geq1\), the global star returns one
of:

1. \(m\) residual contexts which are simultaneously realizable with
   the centre literal;
2. a residual-block transversal of size at most \(2(m-1)\); or
3. an effectively rank-one centre check.

### Proof

If some effective residual scope missed \(X\), its check could be
added to the maximal context-disjoint family.  Thus \(X\) is a
transversal.  Every effective residual has size at most two, giving
the displayed bound.

Set \(v=a\).  For every \(C\in\mathcal M\), assign each mutable
\(x\in\widehat R_C\) the phase \(f_C(x)\).  The effective scopes are
disjoint, so these prescriptions never disagree.  Every omitted rigid
block has only one realizable phase and therefore already agrees with
every \(f_C\) which mentions it.  Extend the partial assignment
arbitrarily to all remaining blocks.  It agrees with every literal of
every selected check.  The same assignment activates every effectively
rank-one check because all of its residual blocks are rigid.

If \(|\mathcal M|\geq m\), retain \(m\) checks.  Otherwise its union is
the claimed transversal. \(\square\)

This is an activation statement, not yet a legal decoder state.
External hard checks and all collateral created by the simultaneous
assignment remain in the scope-complete AC3v audit.

## AC3ah -- dyadic paid context extraction

Discard zero-weight checks, reuse \(\mathcal S^+\) for the remaining
positive-weight family, and suppose it is nonempty.
Write

\[
w_{\min}=\min_{C\in\mathcal S^+}w_C,
\qquad
w_{\max}=\max_{C\in\mathcal S^+}w_C,
\]

and let \(K\) be the least positive integer satisfying

\[
w_{\max}<2^K w_{\min}.
\]

Partition the positive checks into the \(K\) dyadic strata

\[
\mathcal T_k
=
\{C:2^k w_{\min}\leq w_C<2^{k+1}w_{\min}\}.
\]

Let \(\mathcal T\) be a stratum of maximum total weight, write

\[
W_+=\sum_{C\in\mathcal S^+}w_C,
\qquad
W_\mathcal T=\sum_{C\in\mathcal T}w_C,
\]

and put \(\eta=2^k w_{\min}\) for its lower weight scale.  Then

\[
\boxed{
W_\mathcal T\geq\frac{W_+}{K},
\qquad
\eta\leq w_C<2\eta\quad(C\in\mathcal T).
}
\]

For a mutable residual block \(x\), let

\[
d_\mathcal T(x)
=
|\{C\in\mathcal T:x\in\widehat R_C\}|.
\]

### Theorem AC3ah -- PROVED

For every integer \(d\geq1\), one of the following holds:

1. a residual block has \(d_\mathcal T(x)>d\); or
2. there is a context-disjoint family
   \(\mathcal I\subseteq\mathcal T\) with
   \[
   \boxed{
   \sum_{C\in\mathcal I}w_C
   \geq
   \frac{W_\mathcal T}{2d-1}
   \geq
   \frac{W_+}{K(2d-1)}.
   }
   \]

Every family in conclusion 2 is simultaneously activatable with
\((v,a)\) by AC3ag.

### Proof

Form the intersection graph on \(\mathcal T\), joining two checks when
their effective residual scopes intersect.  If every residual-block
degree is at most \(d\), a check with residual rank at most two has at
most

\[
2(d-1)
\]

neighbours.  Greedy colouring therefore uses at most \(2d-1\)
colours.  Each colour class is context-disjoint, and the heaviest class
has at least the displayed fraction of \(W_\mathcal T\).  If the
degree cap fails, conclusion 1 holds. \(\square\)

The dyadic loss is unnecessary for equal weights.  In particular, an
unweighted hard-check star has \(K=1\).

## AC3ai -- high residual degree becomes a literal kernel or phase fan

Suppose AC3ah returns a block \(x\) with
\(d_\mathcal T(x)>d\).  For \(b\in\mathcal A_x\), define

\[
n_{x,b}
=
|\{C\in\mathcal T:x\in\widehat R_C,\ f_C(x)=b\}|
\]

and its paid depth-two load

\[
\mu_{v,a}(x,b)
=
\sum_{\substack{C\in\mathcal T\\
                  x\in\widehat R_C,\ f_C(x)=b}}
w_C.
\]

### Theorem AC3ai -- PROVED

For every integer \(e\geq1\), the high-degree block returns one of:

1. a residual phase \(b\) used by more than \(e\) checks, carrying
   \[
   \boxed{\mu_{v,a}(x,b)>e\eta;}
   \]
2. at least
   \[
   \boxed{
   \left\lfloor\frac de\right\rfloor+1
   }
   \]
   distinct residual phase literals \((x,b)\).

The complete block star itself carries weight greater than \(d\eta\).
Conditioning \((v,a)\) and a phase from conclusion 1 leaves effective
residual rank at most one.

### Proof

The phase counts partition the checks through \(x\):

\[
\sum_b n_{x,b}=d_\mathcal T(x)>d.
\]

If some count is greater than \(e\), every check in the stratum has
weight at least \(\eta\), proving conclusion 1.  Otherwise every count
is at most \(e\).  If \(L\) phases occur, then

\[
Le\geq d_\mathcal T(x)>d,
\]

so \(L>d/e\) and hence
\(L\geq\lfloor d/e\rfloor+1\).  Summing the stratum lower bound over
all checks through \(x\) also gives total block weight greater than
\(d\eta\). \(\square\)

## Combined global router

Let

\[
W_0
=
\sum_{\substack{C\in\mathcal S(v,a)\\
                 \widehat R_C=\varnothing}}w_C,
\qquad
W=W_0+W_+.
\]

If \(W_0\geq W/2\), at least half of the centre-star weight is
effectively rank one.  Otherwise \(W_+>W/2\), and AC3ah--AC3ai give,
for every \(d,e\geq1\), one of:

1. a simultaneously activatable context-disjoint bank carrying
   \[
   \boxed{
   \frac{W}{2K(2d-1)}
   }
   \]
   or more weight;
2. a paid depth-two literal class of more than \(e\) comparable-weight
   checks and load \(>e\eta\); or
3. at least \(\lfloor d/e\rfloor+1\) different phase literals at one
   residual block.

Thus global context localization no longer returns an arbitrary
mixture of residual assignments.  Its remaining outputs are exactly a
scope-complete product-state bank, a depth-two kernel ready for unary
conditioning, or a one-block phase fan for OP2/RI/BDA arithmetic
classification.  Applying AC3ad--AC3af to any installed current
context still requires the actual destroyed-weight and hard-safety
audit; this theorem does not infer those quantities from global
literal load.

`scripts/verify_ac_global_literal_contexts.py` exhausts small
nonuniform phase alphabets, including a rigid block, checks simultaneous
realizability and the matching/transversal bound, constructs every
dyadic paid stratum, verifies the \(2d-1\) weighted colouring
extraction, and checks the depth-two/phase-fan alternative at every
small threshold.
