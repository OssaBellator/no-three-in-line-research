# Canonical phase roles for shared certificate tokens

AC3p--AC3r solve the abstract same-token fan once its common phase
alphabet and separable private supports are identified.  This note
constructs that interface for a canonical phase-block certificate.  The
key point is that a triple meets at most three blocks: destroying the
shared certificate is recorded by a nonzero mismatch word of length at
most three, hence by at most seven states.

Exact phase values are retained only when the reopening relation or its
collateral distinguishes two assignments with the same mismatch word.
Such a failure is not left as an unspecified role; it returns one
explicit phase-sensitivity witness for the carry/denominator/quotient
classifiers.

## Canonical phase-block tokens

Let \(\mathcal B\) be a family of disjoint phase blocks.  Every block
\(B\) has a finite nonempty phase alphabet \(\mathcal A_B\), and its
states partition its candidate cells.  Thus every candidate cell
\(e\in B\) has a unique phase

\[
\operatorname{ph}_B(e)\in\mathcal A_B
\]

whose block state contains it.

A current rank-three certificate \(\pi\) is a **canonical phase-block
token** when at least one of its cells belongs to a phase block and
every nonfixed cell of \(\pi\) belongs to one of these blocks.  Let

\[
K(\pi)=
\{B\in\mathcal B:B\cap\pi\ne\varnothing\}
\]

be its block scope.  Because \(\pi\) has three cells,

\[
1\leq r=|K(\pi)|\leq3.
\]

All cells of \(\pi\) in one block have the same phase: they occur
together in the current block state.  Define their common forbidden
phase by

\[
q_\pi(B)=\operatorname{ph}_B(e),
\qquad e\in B\cap\pi.
\]

Put

\[
\mathcal A_\pi=
\prod_{B\in K(\pi)}\mathcal A_B.
\]

For \(\alpha\in\mathcal A_\pi\), define the mismatch word

\[
\beta_\pi(\alpha)
=
\bigl(
\mathbf1_{\alpha(B)\ne q_\pi(B)}
\bigr)_{B\in K(\pi)}
\in\{0,1\}^{K(\pi)}.
\]

## AC3s -- the seven-state token interface

### Theorem AC3s -- PROVED

With its fixed cells held in place, the certificate \(\pi\) is present
under a phase assignment \(\alpha\in\mathcal A_\pi\) if and only if

\[
\boxed{\alpha=q_\pi.}
\]

Consequently its exact discharging alphabet is

\[
\mathcal D_\pi=
\mathcal A_\pi\setminus\{q_\pi\}.
\]

The mismatch image

\[
\mathcal M_\pi=
\beta_\pi(\mathcal D_\pi)
\]

contains only nonzero binary words and satisfies

\[
\boxed{
|\mathcal M_\pi|
\leq
2^r-1
\leq7.
}
\]

### Proof

A block state contains a token cell exactly at that cell's unique
phase.  Since every token cell in \(B\) has phase \(q_\pi(B)\), all
token cells are simultaneously present exactly when every scope block
uses its \(q_\pi\)-phase.  Any other assignment destroys at least one
token cell.  Its mismatch word is nonzero.  There are
\(2^r-1\) nonzero binary words on an \(r\)-element scope, and
\(r\leq3\). \(\square\)

Some nonzero words may be unrealizable when a scope block has a
singleton phase domain.  Using the image \(\mathcal M_\pi\), rather
than the full binary cube, preserves that degeneracy exactly.
If \(\mathcal D_\pi=\varnothing\), the token is **phase-rigid**: no
phase state can discharge it, so it returns to the anchor-realized or
terminal dictionary rather than entering AC3p.

## Scope-complete support conflicts

Fix a same-token reopening family \(\mathcal J\).  Let \(V_j\) be the
phase-variable support of reopening \(j\), together with every variable
needed to certify its collateral, and put

\[
P_j=V_j\setminus K(\pi).
\]

Call the support-conflict graph **scope-complete at \(\pi\)** when it
joins \(j\) and \(k\) whenever:

- \(P_j\cap P_k\ne\varnothing\);
- their geometric row, column, cell, or paid-certificate supports
  overlap;
- any potential certificate or protected-bank condition can meet both
  private supports, even when its realization also uses a third
  reopening; or
- any nonadditive collateral term depends on states from both private
  supports, including a higher-order term involving further reopenings.

Hence an independent family in this graph has pairwise disjoint private
phase supports and no omitted cross-effect.  Sharing the token scope is
allowed: it is represented by one common assignment
\(\alpha\in\mathcal D_\pi\).

For \(j\in\mathcal J\), let \(\mathcal X_j\) be its finite private state
set and let

\[
R_j\subseteq\mathcal D_\pi\times\mathcal X_j
\]

be its exact legal relation.  Write

\[
E_j(\alpha)=
\{x\in\mathcal X_j:(\alpha,x)\in R_j\}.
\]

The relation is **literal-invariant** when

\[
\beta_\pi(\alpha)=\beta_\pi(\alpha')
\quad\Longrightarrow\quad
E_j(\alpha)=E_j(\alpha')
\]

for all \(\alpha,\alpha'\in\mathcal D_\pi\).  Certified private costs
\(c_j(\alpha,x)\) and a fixed common cost \(f(\alpha)\) are
literal-invariant when their values also agree on every such mismatch
fibre.

## AC3t -- literal-invariant role realization

### Theorem AC3t -- PROVED

Let \(\mathcal I\) be an independent same-token family in a
scope-complete conflict graph.  Assume:

1. \(\mathcal D_\pi\ne\varnothing\);
2. every \(R_j\), every certified \(c_j\), and \(f\) are
   literal-invariant;
3. a legal joint state closes every represented reopening; and
4. choosing a common assignment from \(\mathcal D_\pi\) discharges
   \(\pi\) once.

Then the fibre is separable phase-realized in the sense of AC3p with
common alphabet \(\mathcal M_\pi\).  In particular:

- a joint legal state exists or an equivalent infeasible core has at
  most seven reopenings;
- under persistent message history, one token fibre has at most seven
  strict phase-loss tickets; and
- the additive collateral minimum and its failure profile are exactly
  those of AC3p.1 on \(\mathcal M_\pi\).

### Proof

For every \(b\in\mathcal M_\pi\), choose one representative
\alpha_b\in\mathcal D_\pi\) with
\(\beta_\pi(\alpha_b)=b\).  Literal invariance makes

\[
\overline R_j=
\{(b,x):(\alpha_b,x)\in R_j\}
\]

independent of the representative, and the same is true of the
compressed costs.

Scope completeness and independence make the private supports \(P_j\)
pairwise disjoint and exclude every nonadditive cross-effect.  Thus a
common mismatch word and independently chosen legal private states
install jointly, close all reopenings, and discharge the shared token
once.  This is precisely the AC3p separability contract.  AC3s gives
\(|\mathcal M_\pi|\leq7\), so AC3p--AC3q give the three stated
conclusions. \(\square\)

The theorem does not infer literal invariance from support
compatibility.  Exact phase arithmetic may distinguish two assignments
inside one mismatch fibre; that case is audited next.

## AC3u -- exact-phase fallback or sensitivity witness

Let

\[
h=\max_{B\in K(\pi)}|\mathcal A_B|.
\]

### Theorem AC3u -- PROVED

Retain AC3t's joint-closing and token-discharge hypotheses.  If literal
invariance fails, the same scope-complete independent family
is separable phase-realized over the exact common alphabet
\(\mathcal D_\pi\), whose size satisfies

\[
\boxed{
|\mathcal D_\pi|
=
\prod_{B\in K(\pi)}|\mathcal A_B|-1
\leq
h^r-1
\leq
h^3-1.
}
\]

Moreover, failure of literal invariance returns at least one explicit
witness of one of the following forms:

1. phases
   \(\alpha,\alpha'\in\mathcal D_\pi\) with the same mismatch word,
   one reopening \(j\), and one private state \(x\) which belongs to
   exactly one of \(E_j(\alpha),E_j(\alpha')\);
2. such phases, a reopening \(j\), and a private state legal at both
   phases for which
   \[
   c_j(\alpha,x)\ne c_j(\alpha',x);
   \]
3. such phases for which
   \[
   f(\alpha)\ne f(\alpha').
   \]

Hence:

- if \(h^3=p^{o(1)}\), AC3p--AC3q still give a subpolynomial exact-phase
  ticket interface;
- otherwise the unresolved output is a rank-at-most-three
  phase-sensitivity witness, not an unclassified high-reuse fan.

### Proof

Use the full exact assignment \(\alpha\in\mathcal D_\pi\) as the common
phase.  Scope completeness again makes all other supports private and
all certified costs additive, so the AC3p separability contract holds.
The cardinality calculation is immediate from \(r\leq3\).

If literal invariance fails for a relation, two same-mismatch extension
sets differ; a state in their symmetric difference gives conclusion 1.
If the relations are invariant but a private cost is not, its defining
failure gives conclusion 2.  If only the fixed cost fails invariance,
conclusion 3 holds.  These exhaust the definition. \(\square\)

## Dictionary after AC3s--AC3u

For a canonical phase-block certificate token in a scope-complete
support-conflict graph, the same-token branch now has a finite audit:

1. **phase-rigid:** no phase assignment discharges the token, so it
   returns to the anchor-realized or terminal route;
2. **literal-invariant:** an absolute alphabet of at most seven, handled
   by AC3p--AC3t;
3. **small exact phase:** at most \(h^3-1=p^{o(1)}\) states, handled by
   AC3p--AC3q;
4. **large exact phase:** one explicit rank-at-most-three sensitivity
   witness for carry, denominator, quotient, or orbit classification.

A token which is not represented by canonical phase blocks remains in
the anchor-realized or terminally labelled branches of the role
dictionary.  A purported compatible fan whose private supports overlap
exposes a missing scope-conflict edge instead of entering this theorem.

Thus the remaining role frontier is narrow: classify exact phase
sensitivity on at most three block variables, and verify
scope-completeness for each concrete closure operation.

`scripts/verify_ac_canonical_roles.py` checks the rank-three mismatch
bound, exact and compressed product relations, sensitivity witnesses,
and private-support extraction on exhaustive small phase systems.
