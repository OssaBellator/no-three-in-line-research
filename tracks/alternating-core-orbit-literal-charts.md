# Canonical orbit-literal charts and the sharp compression boundary

AC3z reduces the remaining phase-role problem to a concrete question:
which phase values can the active legality and collateral records
distinguish?  The O1 orbit construction and OP1a answer this question at
the level of individual triples.  Every realizable triple is one
canonical forbidden partial assignment on at most three orbit blocks.

This note converts that representation into an exact chart.  The chart
isolates only phase literals actually mentioned by the active checks;
all other phases have identical canonical-check behavior.  A second,
weighted chart isolates every hard literal and every heavy soft literal,
while merging the remaining soft phases with a sharp one-block error
bound.

There is also an unavoidable lower bound.  If the behavior record asks
for every cell of an O1 block, then it distinguishes every exact phase.
The modular-hyperbola channel is itself injective in the phase, so it
has \(h\), not \(O(1)\), values on an order-\(h\) orbit.  Thus neither
OP1a nor a channel label proves uniform compression.  Compression is
available precisely when the active observable literal support is
small, or when the light residual is explicitly paid.

## Canonical hard and soft checks

Let \(V\) be a finite set of phase blocks.  Block \(v\) has finite
alphabet \(\mathcal A_v\) and distinguished current phase \(q_v\).
A **canonical check**

\[
C=(S_C,f_C)
\]

has a nonempty scope \(S_C\subseteq V\) and one forbidden partial
assignment

\[
f_C\in\prod_{v\in S_C}\mathcal A_v.
\]

An assignment \(\alpha\in\prod_v\mathcal A_v\) violates \(C\) exactly
when

\[
\alpha|_{S_C}=f_C.
\]

Separate the active checks into:

- a hard family \(\mathcal H\), whose full violation vector determines
  the relevant feasibility relations; and
- a soft family \(\mathcal S\), with weights \(w_C\geq0\), whose
  weighted violation sums determine the relevant private and common
  collateral.

Several collateral coordinates may be handled by tagging each soft
check with its record coordinate.  All statements below then apply to
each tagged subfamily, or simultaneously after summing their
nonnegative weights.

For any check family \(\mathcal C\), define its literal support at
block \(v\) by

\[
L_v(\mathcal C)
=
\{f_C(v):C\in\mathcal C,\ v\in S_C\}.
\]

The full active support is

\[
L_v=L_v(\mathcal H\cup\mathcal S).
\]

## AC3aa -- the exact active-literal chart

For every block \(v\), define

\[
\chi_v^{\rm lit}(a)
=
\begin{cases}
\mathtt{current},&a=q_v,\\
\mathtt{lit}(a),&a\in L_v\setminus\{q_v\},\\
\mathtt{other},&a\notin L_v\cup\{q_v\}.
\end{cases}
\]

The last label is omitted when its fibre is empty.  In particular,

\[
\boxed{
|\chi_v^{\rm lit}(\mathcal A_v)|
\leq
|L_v\setminus\{q_v\}|+2.
}
\]

### Theorem AC3aa -- PROVED

The complete hard and soft violation vector factors through the product
chart

\[
\chi^{\rm lit}
=
\prod_{v\in V}\chi_v^{\rm lit}.
\]

Consequently every feasibility relation and every collateral record
which is a function of that vector also factors through the chart.
For a rank-\(r\) token role on \(K(\pi)\), the number of discharging
chart states is at most

\[
\boxed{
\prod_{v\in K(\pi)}
\bigl(|L_v\setminus\{q_v\}|+2\bigr)-1.
}
\]

The coordinate observational quotient of AC3z is no larger than this
chart.  In particular, if \(r\leq3\) and every active literal support
has size \(p^{o(1)}\), then AC3p--AC3q have a \(p^{o(1)}\) exact common
alphabet even when the raw orbit orders are polynomial in \(p\).

### Proof

Suppose two assignments \(\alpha,\alpha'\) have the same product chart.
Fix \(C\in\mathcal H\cup\mathcal S\) and \(v\in S_C\).

If \(f_C(v)=q_v\), equality of chart labels gives

\[
\alpha_v=q_v
\quad\Longleftrightarrow\quad
\alpha'_v=q_v.
\]

If \(f_C(v)\ne q_v\), then \(f_C(v)\in L_v\setminus\{q_v\}\) and is a
singleton chart fibre.  Hence

\[
\alpha_v=f_C(v)
\quad\Longleftrightarrow\quad
\alpha'_v=f_C(v).
\]

Taking the conjunction over \(v\in S_C\) shows that \(\alpha\) violates
\(C\) if and only if \(\alpha'\) does.  This holds for every hard and
soft check, proving factorization of the entire violation vector and
therefore of every function of that vector.

The label bound is immediate from the definition.  The all-current
chart tuple is the only tuple which may fail to discharge the common
token, so removing it gives the displayed product bound.  Since this
chart determines the complete behavior record, the coarsest property
of AC3z bounds the coordinate observational quotient by the same
labels. \(\square\)

### Orbit-phase specialization

For an O1 orbit block \(B\), use

\[
\mathcal A_B=\mathbb Z/h_B\mathbb Z.
\]

OP1a proves that every realizable geometric triple is one canonical
check on at most three such blocks.  Every phase state also preserves
the active row and column sets.  Therefore AC3aa applies without a
modular-to-real relaxation:

- hard triple exclusions contribute their exact phase literals;
- weighted triple collateral contributes its exact phase literals; and
- row-column legality contributes no phase distinction inside the O1
  bank.

Thus the relevant size is the number of phase literals used by the
active real triples, not the total number \(h_B\) of orbit phases.
Arbitrary additional feasibility or cost factors must either be
written as canonical checks and added to \(L_B\), or remain outside
this theorem.  They cannot be silently treated as phase-invariant.

## AC3ab -- exact phase information can really be necessary

Retain one O1 block of order \(h\), with phase states
\(A_{B,t}\), \(t\in\mathbb Z/h\mathbb Z\).  For a candidate cell
\(e\) in the block, define its membership probe

\[
P_e(t)=\mathbf 1_{\{e\in A_{B,t}\}}.
\]

### Theorem AC3ab -- PROVED

Any block chart which determines every membership probe \(P_e\) has at
least \(h\) labels.  Equivalently, if all cell probes occur in the
behavior record, then the AC3z coordinate observational quotient has
exactly \(h\) classes.

Moreover, if the block is generated by
\(K=\langle\lambda\rangle\leq\mathbb F_p^\times\) of order \(h\) on
the layer \(xy=a\), its phase-\(t\) modular channel

\[
c_t=a\lambda^{-t}
\]

is injective in \(t\in\mathbb Z/h\mathbb Z\).  Hence the exact channel
chart also has \(h\) labels.

### Proof

The O1 states partition the block's candidate cells.  For distinct
phases \(s,t\), choose any \(e\in A_{B,t}\).  Then

\[
P_e(t)=1,
\qquad
P_e(s)=0.
\]

Thus the vector of all membership probes separates every pair of
phases, and any chart determining that vector must be injective.  The
observational quotient is coarsest among complete charts, so it also
has \(h\) classes.

For the channel assertion, \(c_s=c_t\) implies

\[
\lambda^{t-s}=1.
\]

Since \(\lambda\) has order \(h\), this gives \(s=t\) in
\(\mathbb Z/h\mathbb Z\). \(\square\)

AC3ab rules out a tempting shortcut: a constant-length record is not a
bounded-range record.  Exact phase, exact channel, and the product carry
decoration from OP1a may each take \(h\) or more numerical values.
When \(h=p^{o(1)}\), the exact chart is already sufficient.  When \(h\)
is large, a proof must restrict the observable literal support, pay a
light residual, or use new arithmetic expansion.  Merely renaming the
phase by its channel does not compress it.

## AC3ac -- hard-exact, heavy-soft compression

The exact chart can still be large because many positive-weight soft
checks mention different phases.  Those literals can be separated by
their total possible influence.

For \(C\in\mathcal S\), retain \(w_C\geq0\), and put

\[
\Phi(\alpha)
=
\sum_{C\in\mathcal S}
w_C\mathbf 1_{\{\alpha|_{S_C}=f_C\}}.
\]

Define the soft load of one phase literal by

\[
\lambda(v,a)
=
\sum_{\substack{C\in\mathcal S\\
                  v\in S_C,\ f_C(v)=a}}
w_C.
\]

Let

\[
W=\sum_{C\in\mathcal S}w_C,
\qquad
\rho=\max_{C\in\mathcal S}|S_C|.
\]

Assume \(\mathcal S\ne\varnothing\); when it is empty, all conclusions
hold with zero residual and no heavy literals.

For a threshold \(\tau>0\), call \((v,a)\) heavy when
\(\lambda(v,a)\geq\tau\).  Define \(\chi_v^\tau\) by giving singleton
labels to:

1. the current phase \(q_v\);
2. every noncurrent hard literal in
   \(L_v(\mathcal H)\); and
3. every remaining noncurrent heavy soft literal.

All other noncurrent phases receive one \(\mathtt{light}\) label.

### Theorem AC3ac -- PROVED

The threshold chart has the following properties.

1. **Hard exactness.**  The full hard-check violation vector factors
   through \(\prod_v\chi_v^\tau\).
2. **One-block light bound.**  If distinct phases \(a,b\) have the same
   block-chart label, then for every fixed context \(\gamma\) on the
   other blocks,
   \[
   \boxed{
   |\Phi(a,\gamma)-\Phi(b,\gamma)|
   \leq
   \lambda(v,a)+\lambda(v,b)
   <2\tau.
   }
   \]
3. **Product-fibre bound.**  If two assignments in the same product
   chart fibre differ in \(d\) coordinates, then they have identical
   hard behavior and
   \[
   \boxed{
   |\Phi(\alpha)-\Phi(\alpha')|<2d\tau.
   }
   \]
   For an AC3 token scope, \(d\leq3\), so the error is less than
   \(6\tau\).
4. **Heavy-literal budget.**
   \[
   \boxed{
   \sum_{v,a}\lambda(v,a)
   =
   \sum_{C\in\mathcal S}|S_C|w_C
   \leq
   \rho W,
   }
   \]
   and consequently the total number of heavy phase literals is at
   most
   \[
   \boxed{\rho W/\tau.}
   \]

Thus the chart is exactly safe for feasibility.  It is exactly safe for
collateral after reserving the displayed \(2d\tau\) residual in the
paid comparison.  It is not an exact AC3p collateral chart unless that
residual is retained or the full soft literal support is isolated as in
AC3aa.

### Proof

The proof of AC3aa using only \(C\in\mathcal H\) proves hard exactness.
If distinct \(a,b\) have the same chart label, they must both lie in the
light fibre.  Neither is a hard literal, and

\[
\lambda(v,a)<\tau,
\qquad
\lambda(v,b)<\tau.
\]

Fix a context \(\gamma\).  A soft check not containing \(v\) is
unchanged.  A soft check containing \(v\) can change from violated to
satisfied only when its literal at \(v\) is \(a\), and can change in the
opposite direction only when its literal is \(b\).  Even if every such
check's remaining literals match \(\gamma\), the total absolute change
is at most

\[
\lambda(v,a)+\lambda(v,b)<2\tau.
\]

For two assignments in one product fibre, change their differing
coordinates one at a time.  Each step remains inside one coordinate
chart fibre, so hard behavior is unchanged and the preceding bound
applies.  The triangle inequality gives the product-fibre bound.

Finally, double-count weighted check--literal incidences:

\[
\sum_{v,a}\lambda(v,a)
=
\sum_{C\in\mathcal S}|S_C|w_C.
\]

Every check has rank at most \(\rho\), and every heavy literal
contributes at least \(\tau\) to the left side.  This proves both budget
claims. \(\square\)

The one-block constant is sharp: one context can activate every check
carrying literal \(a\) and every check carrying literal \(b\), with the
two families changing in opposite directions.  No independence or
negative-dependency assertion is used.

## Resulting arithmetic router

For a canonical O1 phase role, choose a threshold \(\tau\) at the scale
which the current paid token can absorb.  AC3aa--AC3ac give the following
exhaustive audit.

1. If the full active hard-and-soft literal supports are
   \(p^{o(1)}\), use the exact AC3aa chart in AC3p--AC3q.
2. If the hard supports and the heavy-soft kernel are
   \(p^{o(1)}\), use the AC3ac chart and place the \(<2d\tau\) light
   residual explicitly in the collateral comparison.
3. Otherwise return one of two concrete obstructions:
   - many distinct hard phase literals, which is a genuine OP2
     arithmetic-expansion problem; or
   - a large heavy-literal kernel, carrying the explicit load
     \(\lambda(v,a)\geq\tau\).

This router also explains the independent structured interfaces.

- An order-\(h\) O1 block already supplies the explicit subgroup
  \(K=\langle\lambda\rangle\) and its cosets.  A large exact chart may
  therefore be passed to the rational-inverse branch as a labelled
  subgroup-coset component.  It becomes an absorber only after that
  branch's paid-edge and collateral inequalities are verified.
- A fixed reduced-denominator chart may be appended to
  \(\chi_v^{\rm lit}\) or \(\chi_v^\tau\).  The BDA valuation/CRT data
  determine the residue profile, but they do not by themselves erase
  different active hard literals or unbounded radial lifts.  The BDA
  absorber is terminal only under its explicit local-cleanliness and
  paid-collateral hypotheses.

Accordingly, this note does not upgrade AC4.  It closes the formal chart
construction for canonical orbit checks and identifies the remaining
frontier without conflating three different issues:

- exact active-literal complexity;
- quantitatively light collateral sensitivity; and
- arithmetic expansion of a large hard-literal family.

`scripts/verify_ac_orbit_literal_charts.py` exhausts small canonical
check systems, verifies exact chart factorization and the observational
quotient bound, enumerates the hard/heavy/light inequalities, and checks
the O1 phase/channel lower bound on small prime fields.
