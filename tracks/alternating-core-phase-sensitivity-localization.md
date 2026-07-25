# One-block phase sensitivity and behavioral compression

AC3u reduces a non-literal shared-token role to two exact phase
assignments with the same mismatch word and one legality or collateral
discrepancy.  Those assignments may differ on as many as three token
blocks, and the raw exact alphabet can have size \(h^3-1\).

This note sharpens both conclusions.  Every same-mismatch fibre is a
connected Hamming product, so any discrepancy already occurs across
one phase-block flip.  Moreover, exact phase values which no reopening,
private cost, or common cost can distinguish are identified in a
canonical behavioral quotient.  AC3p needs only the quotient alphabet,
not the raw phase alphabet.

The result is an exact audit interface for the existing carry,
denominator, quotient, and orbit labels.  A proposed arithmetic chart
either determines all behavior and supplies a bounded common alphabet,
or it returns two phases with the same arithmetic label and one explicit
one-block discrepancy.  The latter is a genuine missing arithmetic
invariant; it is not hidden inside a multi-block witness.

## Exact behavior records

Retain the canonical token notation of AC3s--AC3u.  Its block scope is

\[
K(\pi)=\{B_1,\ldots,B_r\},
\qquad
1\leq r\leq3,
\]

with phase alphabets \(\mathcal A_i\), forbidden values \(q_i\), exact
product alphabet

\[
\mathcal A_\pi=\prod_{i=1}^r\mathcal A_i,
\]

and discharge alphabet

\[
\mathcal D_\pi
=
\mathcal A_\pi\setminus\{q\},
\qquad
q=(q_1,\ldots,q_r).
\]

Assume \(\mathcal D_\pi\ne\varnothing\).  The empty case is the
phase-rigid branch already returned by AC3s.

For each reopening \(j\), private state \(x\in\mathcal X_j\), and
discharging phase \(\alpha\), combine legality and private collateral
into

\[
g_{j,x}(\alpha)
=
\begin{cases}
\bot,
  &(\alpha,x)\notin R_j,\\
c_j(\alpha,x),
  &(\alpha,x)\in R_j.
\end{cases}
\]

The symbol \(\bot\) is distinct from every numerical cost.  Define the
complete observable behavior record

\[
\boxed{
\mathfrak b(\alpha)
=
\left(
f(\alpha),
\bigl(g_{j,x}(\alpha)\bigr)_{
  j\in\mathcal J,\ x\in\mathcal X_j
}
\right).
}
\]

Equality of these records is exactly simultaneous equality of the
common cost, every legal extension set, and every legal private cost.
Thus the literal-invariance hypothesis of AC3t says precisely that
\(\mathfrak b\) is constant on every mismatch fibre.

## AC3y -- one-block derivative audit

For a nonzero mismatch word
\(b\in\mathcal M_\pi\), put

\[
\mathcal F_b
=
\{\alpha\in\mathcal D_\pi:
\beta_\pi(\alpha)=b\}.
\]

Join two assignments in \(\mathcal F_b\) when they differ in exactly
one block coordinate.  In a coordinate with \(b_i=0\), the value is
fixed at \(q_i\).  In a coordinate with \(b_i=1\), the value ranges
over

\[
\mathcal A_i^\times
=
\mathcal A_i\setminus\{q_i\}.
\]

Hence this fibre graph is the Cartesian product of complete graphs on
the nonempty sets \(\mathcal A_i^\times\) for which \(b_i=1\).

### Theorem AC3y -- PROVED

The following are equivalent:

1. the role relations, private costs, and common cost are
   literal-invariant;
2. for every nonzero mismatch word \(b\), the behavior record
   \(\mathfrak b\) is equal at the endpoints of every one-coordinate
   edge of \(\mathcal F_b\).

If literal invariance fails, there are phases
\(\alpha,\alpha'\in\mathcal D_\pi\) such that:

\[
\boxed{
\beta_\pi(\alpha)=\beta_\pi(\alpha'),
\qquad
|\{i:\alpha_i\ne\alpha_i'\}|=1,
\qquad
\mathfrak b(\alpha)\ne\mathfrak b(\alpha').
}
\]

The differing record coordinate gives exactly one of:

1. a private state which is legal at exactly one endpoint;
2. a private state legal at both endpoints with unequal private costs;
3. unequal common costs.

Thus every AC3u sensitivity witness can be replaced by an explicit
one-block phase flip which keeps the shared token discharged.

### Proof

Each \(\mathcal F_b\) is a Cartesian product of nonempty complete
graphs and is therefore connected.  If all one-coordinate edge
differences vanish, \(\mathfrak b\) is constant along every path and
hence throughout each fibre.  This is literal invariance.  The converse
is immediate because the endpoints of an edge have the same mismatch
word.

If literal invariance fails, choose two assignments in one fibre with
different behavior records.  Connect them by changing their differing
coordinates one at a time.  Every intermediate assignment has the same
mismatch word, and hence still discharges the token.  Some edge on this
path has different behavior records.  Those endpoints differ in one
block.

If the common-cost coordinate differs, conclusion 3 holds.  Otherwise
some \(g_{j,x}\) differs.  One value is \(\bot\) and the other is not,
giving conclusion 1, or both are numerical and unequal, giving
conclusion 2. \(\square\)

### Weighted localization

Suppose a finite multiset of AC3u sensitivity witnesses carries total
current weight \(W\).  For each witness, retain one scalar record
coordinate \(f\) or \(g_{j,x}\) which differs at its endpoints.  On the
coordinate-by-coordinate path used in the proof, select the first edge
on which that same record coordinate changes, classify the selected
edge afresh by the three cases above, and charge the witness weight to
that edge.  Reclassification is necessary because a private-cost
discrepancy may pass through an intermediate illegal phase, or vice
versa.

There are at most \(3r\leq9\) coarse labels consisting of:

- the unique flipped block; and
- the discrepancy kind.

Consequently one coarse label carries weight at least

\[
\boxed{
\frac{W}{3r}\geq\frac W9.
}
\]

If the witnesses first arise from the \(T\) structural conflict labels
of AC3x, one combined structural/block/kind label carries at least

\[
\boxed{\frac{W}{9T}}
\]

of the original weight.  This is a paid one-block derivative family,
not an unweighted choice of a convenient phase pair.

## Coordinate observational equivalence

Raw phase names may contain distinctions which no closure operation can
observe.  For block \(i\), declare the forbidden value \(q_i\) to be a
singleton class.  For nonforbidden values
\(u,v\in\mathcal A_i^\times\), define

\[
u\equiv_i v
\]

when, for every context

\[
\gamma\in\prod_{\ell\ne i}\mathcal A_\ell,
\]

the two discharging assignments obtained by inserting \(u\) and \(v\)
in coordinate \(i\) have equal behavior records.  This is equality of
two context-indexed functions, so \(\equiv_i\) is an equivalence
relation.

Let

\[
\mathcal Q_i=\mathcal A_i/{\equiv_i},
\qquad
k_i=|\mathcal Q_i|,
\]

where the forbidden singleton remains distinguished.  Write

\[
\overline{\mathcal D}_\pi
=
\left(\prod_{i=1}^r\mathcal Q_i\right)
\setminus
\{([q_1],\ldots,[q_r])\}.
\]

Every non-all-forbidden tuple of classes has a discharging
representative, so

\[
\boxed{
|\overline{\mathcal D}_\pi|
=
\prod_{i=1}^r k_i-1.
}
\]

## AC3z -- coarsest coordinatewise behavioral alphabet

### Theorem AC3z -- PROVED

The complete behavior record \(\mathfrak b\) factors through the
coordinate quotient map

\[
\mathcal D_\pi\longrightarrow
\overline{\mathcal D}_\pi.
\]

This quotient is coarsest among coordinatewise quotients which keep
each forbidden phase distinct and determine \(\mathfrak b\): if maps

\[
\psi_i:\mathcal A_i\longrightarrow\mathcal P_i
\]

have those properties, then

\[
\psi_i(u)=\psi_i(v)
\quad\Longrightarrow\quad
u\equiv_i v,
\]

and therefore

\[
|\psi_i(\mathcal A_i)|\geq k_i.
\]

Consequently every scope-complete independent fan is separable
phase-realized over the behavioral alphabet
\(\overline{\mathcal D}_\pi\), and AC3p--AC3q apply with

\[
\boxed{
a_{\rm eff}
=
\prod_{i=1}^r k_i-1
\leq
\prod_{i=1}^r|\mathcal A_i|-1
\leq h^3-1.
}
\]

More precisely:

1. literal invariance holds if and only if
   \[
   \boxed{k_i\leq2\quad\text{for every }i;}
   \]
   the two possible classes are the forbidden value and all
   nonforbidden values;
2. if \(k_i\leq\kappa\) for every block, then
   \[
   \boxed{a_{\rm eff}\leq\kappa^r-1\leq\kappa^3-1;}
   \]
3. some block satisfies
   \[
   \boxed{
   k_i\geq(a_{\rm eff}+1)^{1/r}
   \geq(a_{\rm eff}+1)^{1/3};
   }
   \]
   its \(k_i-1\) nonforbidden classes are pairwise observationally
   distinct, and every pair of such classes has a context exposing a
   one-block legality or cost discrepancy.

Hence a large raw phase alphabet is harmless when its observable
quotient is small.  A large effective alphabet returns one block with
large observational rank rather than an arbitrary rank-three
dependence.

### Proof

Suppose \(\alpha,\alpha'\in\mathcal D_\pi\) have the same tuple of
coordinate classes.  A forbidden value is equivalent only to itself,
so the two assignments have the same mismatch word.  Change their
differing coordinates one at a time.  At each step the old and new
values are \(\equiv_i\)-equivalent in the current context, so the
behavior record does not change.  Every intermediate assignment has
the same nonzero mismatch word.  Thus
\(\mathfrak b(\alpha)=\mathfrak b(\alpha')\), proving factorization.

The descended record defines every relation and cost independently of
the representative.  AC3v supplies joint legality and exact additive
collateral on a primal-independent fan, so this quotient is a valid
AC3p common alphabet.  Its cardinality gives the displayed bounds.

For minimality, suppose
\(\psi_i(u)=\psi_i(v)\) for two nonforbidden phases.  Fix any context
on the remaining coordinates.  The two full assignments have the same
product \(\psi\)-label, so factorization through that product makes
their behavior records equal.  Since this holds in every context,
\(u\equiv_i v\).  Forbidden phases are singleton classes under both
quotients.  Every \(\psi_i\)-fibre therefore lies inside one
\(\equiv_i\)-class, proving the cardinality inequality.

Literal invariance implies that all nonforbidden values of one
coordinate are equivalent in every context, hence \(k_i\leq2\).
Conversely, if every block has only its forbidden class and at most one
nonforbidden class, the quotient tuple is exactly the mismatch word, so
factorization makes the behavior literal-invariant.

The second assertion follows by multiplying the coordinate bounds.  For
the third, the geometric mean is at most the largest \(k_i\).  Two
distinct nonforbidden equivalence classes represent unequal
context-indexed behavior functions, so some context distinguishes any
chosen pair.  The resulting assignments differ in only block \(i\) and
have the same mismatch word. \(\square\)

## Arithmetic-chart audit

For every block \(i\), let

\[
\chi_i:\mathcal A_i\longrightarrow\Lambda_i
\]

be any proposed arithmetic chart, with the forbidden value's label
used by no nonforbidden phase.  A chart may record any tuple of the
already exposed data which is determined by that block phase:

- product, cross, or aligned carry signatures;
- reduced denominator and wrap-index residues;
- rational wrap center;
- quotient/coset or orbit label; and
- bounded channel and endpoint-role data.

Put \(\ell_i=|\chi_i(\mathcal A_i)|\).

### Corollary AC3z.1 -- PROVED

Exactly one of the following audit outcomes holds.

1. **Chart-complete.**  For every block and all phases,
   \[
   \chi_i(u)=\chi_i(v)
   \quad\Longrightarrow\quad
   u\equiv_i v.
   \]
   Then all behavior factors through the product arithmetic chart, and
   AC3p--AC3q apply with at most
   \[
   \boxed{\prod_{i=1}^r\ell_i-1}
   \]
   common states.
2. **Same-label derivative.**  Some block has nonforbidden phases
   \(u,v\) with the same arithmetic label but
   \(u\not\equiv_i v\).  The definition returns a fixed context on the
   other at most two blocks and an explicit one-block legality, private
   cost, or common-cost discrepancy.

### Proof

If outcome 1 holds, every product-chart fibre lies inside one product
of observational equivalence classes.  AC3z makes the behavior
constant on that fibre, so it descends to the product chart.  The
forbidden labels are distinguished, giving at most the displayed
number of discharging chart tuples.

If outcome 1 fails, its defining phases have the same chart label but
belong to different observational classes.  By the definition of
\(\equiv_i\), some context gives unequal behavior records.  AC3y's
record-coordinate classification gives the stated discrepancy.
\(\square\)

### Corollary AC3z.2 -- persistent observational refinements

Consider a sequential token--role fibre in which new reopening
relations or certified costs are appended to the behavior record and
old record coordinates are retained.  Let \(k_i(t)\) be the number of
coordinate observational classes after time \(t\).  Then

\[
\boxed{
\Xi_{\rm obs}(t)=\sum_{i=1}^r k_i(t)
}
\]

is integer-valued and nondecreasing.  Every strict change of the
behavioral quotient increases \(\Xi_{\rm obs}\) by at least one, and

\[
\boxed{
\Xi_{\rm obs}(t)
\leq
\sum_{i=1}^r|\mathcal A_i|.
}
\]

If one persistent arithmetic chart is complete for every appended
record and has \(\ell_i\) labels on block \(i\), then

\[
\boxed{
\Xi_{\rm obs}(t)\leq\sum_i\ell_i.
}
\]

Hence a \(p^{o(1)}\)-sized complete chart supplies a subpolynomial
strict-refinement ticket budget.  The first appended record for which
the chart is not complete returns the same-label one-block derivative
of AC3z.1 rather than silently resetting the quotient.

Equivalently, one may use a persistent complete product chart as the
fixed AC3q common alphabet from the outset, obtaining at most
\(\prod_i\ell_i-1\) strict phase losses without changing alphabets.

Removing or replacing an old behavior coordinate is not an append-only
refinement.  It is a genuine history reset and must use the separately
paid AC3e reopening interface, exactly as a common-message enlargement
does in AC3q.

#### Proof

Appending record coordinates can distinguish phases which were
previously equivalent, but it cannot identify phases whose retained
records were already different.  Each coordinate partition therefore
refines monotonically.  A proper refinement of a finite partition
strictly increases its number of classes, proving monotonicity and the
raw alphabet bound.  Under a complete chart, every chart fibre lies
inside one observational class, so the coarsest-quotient property gives
\(k_i(t)\leq\ell_i\).  If this containment first fails, AC3z.1 gives
the stated derivative. \(\square\)

This corollary does not assert that the existing arithmetic charts are
already complete for every closure move.  It makes that remaining
claim checkable: prove chart completeness with
\(\prod_i\ell_i=p^{o(1)}\), or classify one same-label one-block
derivative.  Multi-block phase sensitivity and irrelevant raw phase
multiplicity are no longer part of the frontier.

[`alternating-core-orbit-literal-charts.md`](alternating-core-orbit-literal-charts.md)
performs this audit for canonical O1/OP1a checks.  AC3aa constructs the
exact chart from active phase literals, AC3ab proves the sharp
\(h\)-label lower bound when all O1 cells are observable, and AC3ac
keeps hard behavior exact while bounding every light one-block
collateral derivative by \(2\tau\).

[`alternating-core-literal-star-router.md`](alternating-core-literal-star-router.md)
then handles every literal already localized to the current phase
context.  AC3ad computes exact drift and hard safety, while
AC3ae--AC3af reduce a nonimproving rank-three bucket to fixed
collateral, a paid depth-two literal, or a quantitatively large
residual-disjoint bank.

[`alternating-core-global-literal-contexts.md`](alternating-core-global-literal-contexts.md)
closes the varying-context mixture at one fixed centre by AC3ag--AC3ai.
Thus only cross-centre hard-literal expansion and arithmetic
classification of the paid context bank, depth-two kernel, or
residual-block phase fan remain.

`scripts/verify_ac_phase_sensitivity.py` exhausts Boolean behavior
records on small phase products, checks the Hamming-edge criterion,
constructs the coordinate observational quotient, audits coarse and
exact charts, verifies persistent quotient refinement, and checks the
weighted \(1/(3r)\) localization.
