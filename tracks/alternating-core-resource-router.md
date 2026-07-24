# Anchor-realized resource stars

AC3j routes the second-order collision load of a minimal Hall core to
either a same-token fan or many distinct charging tokens in one role at
one reopening.  Distinct tokens need not be distinct current
certificates, and an abstract role need not identify an anchor.  This
note records the exact additional interface under which the
resource-star alternative becomes paid secant geometry.

## Anchor-realized roles

Fix a reopening \(j\) and one of its geometric roles \(\lambda\).  Call
the role **anchor-realized** when there is a current cell \(v=v(j,\lambda)\)
such that every underlying current certificate resource selected in
this role is a distinct rank-three certificate

\[
C=\{v,x_C,y_C\}.
\]

Distinct certificates have distinct unordered outside pairs
\(\{x_C,y_C\}\).  Each certificate also has its corresponding
neutralization object, and the full support-conflict graph on those
objects includes:

- overlap of outside endpoints, rows, columns, or replacement cells;
- overlap of paid certificates;
- every pair whose joint installation creates nonadditive collateral;
- every protected-bank or opposite-layer incompatibility.

The role is **terminally labelled** instead when its label already
places it in a carry-growth, bounded-denominator, rational-quotient, or
finite exceptional-state interface.  A shared-token role may instead
be **separable phase-realized** in the sense of AC3p; AC3s--AC3u prove
this interface for scope-complete canonical phase-block tokens, up to
one explicit exact-phase sensitivity witness.  The remaining geometric
work must route the actual role dictionary to one of these three forms;
the results below close the combinatorics of the anchor-realized form.

## AC3k -- four-way routing of an anchor-realized Hall output

Retain the notation of AC3j.  Let

\[
\kappa=\kappa(j),
\qquad
s=\left\lfloor\sqrt{\frac{\kappa}{T}}\right\rfloor,
\]

and suppose \(s\geq1\).  Assume every underlying certificate resource
has token capacity at most \(\rho\geq1\).

Condition on the resource-star alternative of AC3j selecting an
anchor-realized role.  If it selects a terminally labelled role instead,
that label leaves through its stated carry/BDA/RI/finite interface and
the theorem below is not needed.

For an anchor-realized resource family \(\mathcal F_v\), put

\[
d(v,x)
=
\bigl|
\{C\in\mathcal F_v:x\in C\setminus\{v\}\}
\bigr|.
\]

### Theorem AC3k -- PROVED

For every integer pair-codegree threshold \(\Delta\geq1\) and support
threshold \(\Gamma\geq0\), at least one of the following holds.

1. **Shared-token fan.**  One capacity token is used in the same role
   as at \(j\) by more than \(s\) other reopenings.
2. **High anchor-pair codegree.**  One anchor \(x\ne v\) belongs with
   \(v\) to more than \(\Delta\) distinct current certificates.
3. **Support-conflict overload.**  One neutralization object conflicts
   with more than \(\Gamma\) other members of an endpoint-disjoint
   anchor star.
4. **Paid compatible anchor star.**  There is a family of distinct
   current certificates which:

   - all contain \(v\);
   - are pairwise disjoint outside \(v\);
   - have pairwise support-compatible neutralization objects; and
   - have cardinality at least
     \[
     \boxed{
     \left\lceil
     \frac{1}{\Gamma+1}
     \left\lceil
     \frac{\lceil s/\rho\rceil}{2\Delta-1}
     \right\rceil
     \right\rceil.
     }
     \]

Thus, whenever the fourth quantity is at least seven and the selected
objects satisfy both the AN2 layer/channel interface and the AN3
central-cell/intermediate-state contract, they form a valid finite input
for the AN3 neutralization bank.

### Proof

Apply AC3j with threshold \(D=s\).  Its first outcome is conclusion 1.
Otherwise one role at \(j\) contains at least \(s\) distinct colliding
capacity tokens.  Since one underlying resource supplies at most
\(\rho\) copies, these tokens represent at least

\[
n=\lceil s/\rho\rceil
\]

distinct current certificate resources.  Restrict to any \(n\) of
them.  By the anchor-realization hypothesis they form a rank-three
certificate family through \(v\).

Apply AC1c with threshold \(\Delta\).  Either conclusion 2 holds, or
there is an endpoint-disjoint anchor star of size at least

\[
M=
\left\lceil
\frac{n}{2\Delta-1}
\right\rceil.
\]

On its full support-conflict graph, conclusion 3 holds if the maximum
degree exceeds \(\Gamma\).  Otherwise a greedy proper colouring uses at
most \(\Gamma+1\) colours.  A largest colour class has size at least
\(\lceil M/(\Gamma+1)\rceil\) and is the family in conclusion 4.
\(\square\)

The theorem does not claim that a large compatible family is
automatically improving.  It supplies the exact paid, endpoint-disjoint
topology required by AN3; AN4 must still compare its destroyed
incidence with fixed and normalized collateral.

## AC3l -- weighted compatible extraction

Now give every distinct certificate \(C\in\mathcal F_v\) a nonnegative
current destroyed-incidence weight \(w(C)\), and put

\[
W=\sum_{C\in\mathcal F_v}w(C).
\]

Discard zero-weight certificates.  For an endpoint-disjoint anchor
star \(\mathcal S\), let its full conflict graph be as above and define
the closed-neighbourhood paid load

\[
L_{\mathcal S}(C)
=
\sum_{C'\in N_{\mathcal S}[C]}w(C').
\]

### Corollary AC3l -- PROVED

For every \(\Delta\geq1\) and real \(K\geq1\), at least one of the
following holds.

1. some anchor pair has unweighted codegree greater than \(\Delta\);
2. some certificate \(C\) in an endpoint-disjoint anchor star satisfies
   \[
   \boxed{
   L_{\mathcal S}(C)>K\,w(C);
   }
   \]
3. there is an endpoint-disjoint, support-compatible family
   \(\mathcal I\) with
   \[
   \boxed{
   \sum_{C\in\mathcal I}w(C)
   \geq
   \frac{W}{(2\Delta-1)K}.
   }
   \]

In outcome 2, when conflict edges carry the finite AC2d arithmetic
label set, AC2d localizes the paid overload to one such label.  In
outcome 3, if every selected neutralization object has collateral at
most \(\eta w(C)\), with all nonadditive effects in the conflict graph,
their joint collateral is at most

\[
\eta\sum_{C\in\mathcal I}w(C).
\]

Hence \(\eta<1\) gives a strict improving state.

### Proof

If outcome 1 fails, AC1d gives an endpoint-disjoint anchor star
\(\mathcal S\) of paid weight at least \(W/(2\Delta-1)\).  Apply AC2c
with parameter \(K\) to its full weighted conflict graph.  Its overload
alternative is outcome 2.  Otherwise it returns a compatible family
carrying at least \(1/K\) of the weight of \(\mathcal S\), which proves
outcome 3.  The collateral assertion is AC2a.
\(\square\)

## Interface after AC3k--AC3l

For an anchor-realized role, the Hall obstruction now has only four
explicit exits:

1. a shared-token fan entering AC3p--AC3r when its role is separable
   phase-realized, and otherwise returning to the finite role
   dictionary;
2. a high anchor-pair codegree entering the endpoint-rematching bank
   AC3m--AC3n;
3. a quantitatively paid labelled support overload handled recursively
   by AC2d and the AC3d--AC3e potential; or
4. an endpoint-disjoint compatible paid star entering AN3--AN4.

Terminally labelled non-anchor roles already leave through the
carry/BDA/RI interfaces by definition.  The remaining arithmetic
frontier is therefore to prove the finite role dictionary and classify
the explicit shared-token phase-collateral profile.  AC3p--AC3r remove
generic fan feasibility and, under persistent message history, give at
most one strict-loss ticket per common phase; a message reset is an
AC3e reopening and is paid separately.  The high anchor-pair output is
executable by
[`alternating-core-pair-core-bank.md`](alternating-core-pair-core-bank.md):
codegree greater than \(12\) gives seven third endpoints in one
permutation layer, while codegree at most \(12\) costs only the absolute
anchor-link factor \(23\).  No further abstract compatibility
extraction is missing.

For canonical phase-block tokens, AC3s--AC3u make the role alternative
finite and checkable: at most seven literal mismatch states, at most
\(h^3-1\) exact states, or one rank-at-most-three phase-sensitivity
witness.  What remains is to verify the scope-complete conflict graph
for the concrete closure moves and pass the witness to the existing
carry/BDA/RI classifiers.

`scripts/verify_ac_resource_router.py` exhausts all simple anchor-link
graphs through six outside endpoints, checks the exact nested colouring
bound, and verifies the weighted AC1d--AC2c composition on every small
support-conflict graph produced by the extraction.
