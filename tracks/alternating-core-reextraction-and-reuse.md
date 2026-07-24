# Compatible re-extraction and an exact no-recycling criterion

This note proves two finite combinatorial interfaces used between AC1 and
AC4.  It does not supply the geometric conflict-degree or signature-reuse
bounds; it identifies exactly which bounds are sufficient.

## AC2a -- weighted compatible re-extraction

Let \(\mathcal O\) be a finite family of candidate structural objects
returned by AC1.  Give \(o\in\mathcal O\) a paid destroyed-incidence
weight \(w(o)\geq0\).  Join two objects in a conflict graph whenever they
cannot be installed simultaneously.  The conflict relation must include:

- overlap of active rows, columns, or replacement cells;
- overlap of paid certificates, so destroyed weight is not double-counted;
- any pair whose simultaneous installation creates a cross-object
  certificate or violates a protected bank contract.

### Lemma AC2a -- PROVED

If the conflict graph has maximum degree at most \(\Delta\), then it
contains a compatible family \(\mathcal I\) satisfying

\[
\boxed{
\sum_{o\in\mathcal I}w(o)
\geq
\frac1{\Delta+1}
\sum_{o\in\mathcal O}w(o).
}
\]

If every selected object has collateral at most
\(\eta w(o)\), and all nonadditive cross-object collateral was included
in the conflict relation, their simultaneous installation has total
collateral at most

\[
\eta\sum_{o\in\mathcal I}w(o).
\]

### Proof

A graph of maximum degree \(\Delta\) has a greedy proper colouring with at
most \(\Delta+1\) colours.  The colour classes are compatible.  One
colour class has at least a \(1/(\Delta+1)\) fraction of the total vertex
weight.  On a compatible colour class, paid certificate sets are disjoint
and all forbidden cross-effects have been excluded, so destroyed weight
and the assumed per-object collateral bounds add.
\(\square\)

Thus the constant-factor part of AC2 is complete once AC1's arithmetic
labels give a conflict graph of bounded degree.  A bound on ordinary
support overlap alone is not enough: certificate overlap and cross-object
creation must also be edges.

## AC2b -- composed paid-star re-extraction

Suppose the heavy-anchor family entering AC1d has total paid weight
\(W_v\), every anchor pair has codegree at most \(\Delta\), and the full
AC2a incompatibility graph on the resulting certificate objects has
maximum degree at most \(\Gamma\).

### Corollary AC2b -- PROVED

There is a simultaneously installable endpoint-disjoint star
\(\mathcal I\) with

\[
\boxed{
\sum_{C\in\mathcal I}w(C)
\geq
\frac{W_v}{(2\Delta-1)(\Gamma+1)}.
}
\]

If every object has collateral at most \(\eta w(C)\), with all
nonadditive effects represented in the incompatibility graph, the joint
collateral of \(\mathcal I\) is at most
\(\eta\sum_{C\in\mathcal I}w(C)\).

### Proof

AC1d first returns an endpoint-disjoint star of weight at least
\(W_v/(2\Delta-1)\). Restrict the full incompatibility graph to that
star; its maximum degree is still at most \(\Gamma\). AC2a retains at
least a \(1/(\Gamma+1)\) fraction of its weight and gives the collateral
assertion. \(\square\)

This completes the AC1-to-AC2 transition whenever the arithmetic labels
give both bounded pair codegree and bounded full incompatibility degree.
The unresolved route is now exactly a high pair codegree or a
high-incompatibility-degree return carrying current paid mass.

## AC2c -- weighted incompatibility return

The maximum-degree hypothesis in AC2a can be replaced by a condition
which measures the actual paid mass around each object. Discard
zero-weight objects and define the closed-neighbourhood load

\[
L(o)=\sum_{o'\in N[o]}w(o').
\]

### Lemma AC2c -- PROVED

For every real \(K\geq1\), one of the following holds:

1. some object \(o\) has a paid overloaded neighbourhood
   \[
   \boxed{L(o)>K\,w(o);}
   \]
2. there is a compatible family \(\mathcal I\) with
   \[
   \boxed{
   \sum_{o\in\mathcal I}w(o)
   \geq
   \frac1K\sum_{o\in\mathcal O}w(o).
   }
   \]

### Proof

Give every object \(o\) an independent exponential clock of rate
\(w(o)\), and select \(o\) when its clock is the earliest in \(N[o]\).
Adjacent objects cannot both be selected. The exponential-race identity
gives

\[
\Pr(o\text{ is selected})=\frac{w(o)}{L(o)}.
\]

Hence the expected selected weight is

\[
\sum_o\frac{w(o)^2}{L(o)}.
\]

If the first alternative fails, every summand is at least \(w(o)/K\).
The expectation is therefore at least the second boxed quantity, so some
realization has at least that weight. \(\square\)

This makes the high-incompatibility alternative paid without using
unweighted degree. To finish the route, the geometry must classify an
object whose full conflict neighbourhood carries \(K\) times its own
current incidence, or show that such neighbourhood loads are uniformly
bounded.

## AC2d -- labelled overload descent

Suppose every conflict edge incident with an object \(o\) carries one of
at most \(T\) arithmetic labels. These labels may record the pair-rank,
carry, quotient-ratio, wrap-center, or channel certificate responsible
for the incompatibility. For a label \(\lambda\), let

\[
S_\lambda(o)
=
\{v\in N(o):ov\text{ has label }\lambda\}.
\]

### Lemma AC2d -- PROVED

Assume \(L(o)>K w(o)\), where \(K>1\). For every \(Q\ge1\), some label
\(\lambda\) satisfies

\[
\boxed{
\sum_{v\in S_\lambda(o)}w(v)
>
\frac{K-1}{T}w(o)
}
\]

and one of the following holds inside the conflict graph induced by
\(S_\lambda(o)\):

1. some \(v\in S_\lambda(o)\) has restricted closed-neighbourhood load
   greater than \(Qw(v)\); or
2. a compatible family \(\mathcal I\subseteq S_\lambda(o)\) has
   \[
   \boxed{
   \sum_{v\in\mathcal I}w(v)
   >
   \frac{K-1}{TQ}w(o).
   }
   \]

Moreover, for every \(\theta>0\), either that label class contains one
object of weight greater than \(\theta w(o)\), or

\[
\boxed{
|S_\lambda(o)|
>
\frac{K-1}{T\theta}.
}
\]

### Proof

The overload inequality gives

\[
\sum_{v\in N(o)}w(v)>(K-1)w(o).
\]

Partition this sum among at most \(T\) labels and choose a heaviest
part. This proves the first box. Apply AC2c with parameter \(Q\) to the
induced weighted conflict graph on that label class. Its two alternatives
give the restricted overload or a compatible family carrying at least
\(1/Q\) of the class weight, which proves the second box.

Finally, if every member of the class has weight at most
\(\theta w(o)\), its cardinality times \(\theta w(o)\) is at least its
total weight. Combining this with the strict first box proves the last
display. \(\square\)

Thus a paid high-conflict return can be narrowed to one arithmetic
certificate label before recursion. It then produces an installable paid
bank, a single heavier object, a broad same-label star, or a deeper
overload wholly inside that label. AC2d does not classify the resulting
label; it removes arbitrary mixtures of labels from that remaining
classification problem.

## AC3b -- ticketed signature potential

Let \(\Sigma\) be the finite signature universe from AC3a.  Give every
signature \(\sigma\) a nonnegative integer reuse budget \(R_\sigma\).
A closure state records an exposed set \(E\subseteq\Sigma\) and counters

\[
0\leq c_\sigma\leq R_\sigma.
\]

Assume every nonterminal transition does at least one of:

1. expose a signature outside \(E\); or
2. increment \(c_\sigma\) for a previously exposed signature without
   exceeding \(R_\sigma\).

### Lemma AC3b -- PROVED

The integer potential

\[
\boxed{
\Xi_{\rm ticket}
=|E|+\sum_{\sigma\in\Sigma}c_\sigma
}
\]

strictly increases at every nonterminal transition and satisfies

\[
0\leq\Xi_{\rm ticket}
\leq
|\Sigma|+\sum_{\sigma\in\Sigma}R_\sigma.
\]

Consequently the closure makes at most

\[
|\Sigma|+\sum_\sigma R_\sigma-\Xi_{\rm ticket}(s_0)+1
\]

oracle calls before termination.

### Proof

Exposure is permanent, so the first kind of transition increases
\(|E|\).  The second increases one counter.  All terms are nonnegative
and the displayed capacities give the upper bound.  Apply the bounded
integer-growth argument of AC4a.
\(\square\)

The substantive geometric assertion in AC3 is now the construction of
the tickets: an old signature must consume a charge attached to current
syndrome incidence, an original certificate, or a finite exceptional
state, and the corresponding \(R_\sigma\) must be \(p^{o(1)}\).

## AC3c -- exact unticketed cycle obstruction

Collapse closure states which have the same exposed-signature data, and
let \(Q\) be the finite directed graph of transitions carrying only old
signatures and consuming no ticket.

### Lemma AC3c -- PROVED

There is an integer potential strictly increasing on every edge of \(Q\)
if and only if \(Q\) is acyclic.

### Proof

A directed cycle is incompatible with strict increase: summing the
inequalities around the cycle would make a value strictly smaller than
itself.  Conversely, if \(Q\) is acyclic, assign each vertex the maximum
length of a directed path ending there.  Every edge extends such a path
by one, so the assigned integer strictly increases.
\(\square\)

Therefore a repeated-signature cycle cannot be repaired by choosing
different coefficients in the same potential.  AC3 must break every such
cycle by a paid bank, BDA/RI delegation, terminal improvement, or a
finite consumable ticket.  This is an exact audit criterion for the
remaining no-recycling proof.

## AC3d -- strict-support potential for labelled recursion

Fix a finite object universe \(\mathcal O\).  A **pure AC2d descent
epoch** is a sequence of recursive overload states

\[
(U_0,o_0),(U_1,o_1),\ldots,
\qquad o_t\in U_t\subseteq\mathcal O,
\]

in which the recursive alternative at time \(t\) chooses a certificate
label \(\lambda_t\) and replaces the current universe by

\[
U_{t+1}=S_{\lambda_t}^{U_t}(o_t)
\subseteq U_t\setminus\{o_t\}.
\]

The next centre \(o_{t+1}\) is the restricted-overload object supplied
inside that induced label class.  No discarded object is reintroduced
during a pure epoch.

### Lemma AC3d -- PROVED

The integer support potential

\[
\boxed{
\Xi_{\rm supp}(U)=|\mathcal O|-|U|
}
\]

strictly increases at every recursive AC2d overload descent.  A pure
epoch beginning with \(U_0\) therefore contains at most
\(|U_0|-1\) recursive descents and cannot contain a directed state
cycle.

### Proof

Every conflict-neighbour class excludes its centre, so

\[
|U_{t+1}|
\leq |U_t|-1.
\]

Consequently

\[
\Xi_{\rm supp}(U_{t+1})
\geq
\Xi_{\rm supp}(U_t)+1.
\]

The potential is bounded above by \(|\mathcal O|-1\) on a nonempty
recursive state.  This gives the length bound.  Strict containment also
precludes returning to an earlier universe, hence precludes a directed
state cycle. \(\square\)

Thus the recursive overload alternative created by AC2d is not one of
the unticketed cycles left abstract in AC3c.  To revisit an object
discarded from \(U_t\), a later operation must enlarge the support; that
is a support-reuse event rather than an induced-label recursion and must
consume an AC3b ticket or terminate through a paid bank or BDA/RI
delegation.  AC3d does not bound those reopenings, but isolates them as
the only possible source of recycling after labelled overload descent.

## AC3e -- combined descent/reopening potential

Let \(n=|\mathcal O|\), and suppose a closure component has a total
budget of \(R\) support-reuse tickets.  A nonterminal support transition
from \((U,t)\), where \(U\ne\varnothing\) and \(0\leq t\leq R\), is
required to be one of:

1. an unticketed labelled descent \(U'\subsetneq U\), with \(t'=t\);
2. a ticketed transition to any nonempty \(U'\subseteq\mathcal O\),
   with \(t'\geq t+1\).

The second case includes every reopening or other failure of strict
support descent.

### Lemma AC3e -- PROVED

The integer potential

\[
\boxed{
\Xi_{\rm reopen}(U,t)
=
nt+n-|U|
}
\]

increases by at least one on every nonterminal transition and satisfies

\[
0\leq\Xi_{\rm reopen}\leq nR+n-1.
\]

Consequently, from state \((U_0,t_0)\), the component makes at most

\[
\boxed{
nR+n-\Xi_{\rm reopen}(U_0,t_0)
}
\]

further transition-or-terminal oracle calls.

### Proof

On an unticketed descent, \(t\) is fixed and \(|U|\) drops by at least
one, so the potential rises by at least one.

On a ticketed transition, the ticket term rises by at least \(n\).
Changing between two nonempty supports can decrease the support-deficit
term \(n-|U|\) by at most \(n-1\).  The net increase is therefore at
least one.  The displayed range follows from \(t\leq R\) and
\(1\leq|U|\leq n\).  Apply the bounded integer-growth argument of AC4a.
\(\square\)

AC3e combines AC3b and AC3d without a lexicographic reset: a ticket may
reopen the entire object universe, yet its coefficient pays for the
largest possible loss of support deficit.  Thus, once current syndrome
incidence supplies a finite total ticket budget \(R\), labelled overload
recursion and all paid reopenings terminate under one explicit scalar
potential.  Constructing that syndrome-paid budget remains the geometric
part of AC3.

## AC3f -- capacitated Hall certificate for paid reopenings

Let \(\mathcal J\) be the reopening events in a finite closure prefix and
let \(\mathcal P\) be a finite set of atomic paid resources.  A resource
\(\pi\in\mathcal P\) has an integer capacity \(c_\pi\geq0\).  Each
reopening \(j\in\mathcal J\) has a nonempty eligibility set
\(A_j\subseteq\mathcal P\), consisting of the current syndrome
incidences, original certificates, or exceptional-state tokens which
may legitimately pay for that reopening.

### Lemma AC3f -- PROVED

There is a charge map

\[
\chi:\mathcal J\longrightarrow\mathcal P,
\qquad
\chi(j)\in A_j,
\qquad
|\chi^{-1}(\pi)|\leq c_\pi,
\]

if and only if every subfamily \(\mathcal X\subseteq\mathcal J\)
satisfies the capacitated Hall inequalities

\[
\boxed{
|\mathcal X|
\leq
\sum_{\pi\in\bigcup_{j\in\mathcal X}A_j}c_\pi.
}
\]

Consequently, if these inequalities hold for every finite prefix of a
closure trajectory, then the total number of reopenings is at most

\[
\boxed{
R=\sum_{\pi\in\mathcal P}c_\pi.
}
\]

With \(n=|\mathcal O|\), AC3e then bounds the entire mixture of labelled
descents and reopenings by the potential ceiling \(nR+n-1\).  If every
atomic paid resource has capacity at most \(\rho\), then
\(R\leq\rho|\mathcal P|\).

### Proof

Replace each resource \(\pi\) by \(c_\pi\) distinguishable copies and
join reopening \(j\) to every copy of every resource in \(A_j\).
Ordinary Hall's marriage theorem gives a matching covering
\(\mathcal J\) exactly when every subfamily has at least its cardinality
many neighbouring copies.  The number of copies in the neighbourhood
of \(\mathcal X\) is precisely the sum in the boxed inequality.  A
covering matching is the required charge map, and conversely every
charge map chooses distinct copies.

Taking \(\mathcal X=\mathcal J\) gives
\(|\mathcal J|\leq R\).  If an infinite trajectory existed, its first
\(R+1\) reopenings would form a finite prefix contradicting that bound.
The AC3e conclusion follows by using the reopening count as its ticket
counter. \(\square\)

Thus AC3 no longer needs an ad hoc greedy ticket assignment.  Its exact
remaining payment obligation is to prove the boxed neighbourhood
capacity inequality for the geometric eligibility relation.  Failure is
equally informative: Hall returns a specific reopening subfamily whose
entire eligible current-incidence neighbourhood has insufficient
capacity, and that deficient family is the object to classify or
delegate to BDA/RI.

## AC3g -- bounded-overlap payment criterion

Replace every resource \(\pi\) by its \(c_\pi\) capacity tokens, as in
AC3f.  A reopening is adjacent to all tokens belonging to its eligible
resources.  Suppose:

1. every reopening is adjacent to at least \(L\) tokens;
2. every token is adjacent to at most \(\Delta\) reopenings.

### Lemma AC3g -- PROVED

For every reopening subfamily \(\mathcal X\),

\[
\boxed{
|N(\mathcal X)|
\geq
\frac L\Delta|\mathcal X|.
}
\]

In particular, \(L\geq\Delta\) implies all capacitated Hall inequalities
from AC3f and hence supplies a valid paid ticket assignment.

More sharply, assume only the first condition.  If Hall fails, then
there is a deficient reopening family \(\mathcal X\) and one paid
resource token which is eligible for more than \(L\) events of
\(\mathcal X\).  Thus one of the following exact alternatives holds:

1. all token reuse degrees are at most \(L\), and every reopening can be
   paid within capacity;
2. one current syndrome incidence or certificate resource is eligible
   for more than \(L\) reopenings in a Hall-deficient component.

### Proof

Count eligibility edges between \(\mathcal X\) and its token
neighbourhood.  The reopening degree condition gives at least
\(L|\mathcal X|\) edges, while the token degree condition gives at most
\(\Delta|N(\mathcal X)|\).  This proves the first box, and
\(L\geq\Delta\) gives Hall.

If Hall fails, choose \(\mathcal X\) with
\(|N(\mathcal X)|<|\mathcal X|\).  The same edge count, without an
upper-degree assumption, shows that the average degree of a token in
\(N(\mathcal X)\) is greater than

\[
\frac{L|\mathcal X|}{|N(\mathcal X)|}>L.
\]

Some token therefore has degree greater than \(L\) inside the deficient
family. \(\square\)

AC3g turns the Hall interface into a local geometric audit.  It is
enough to prove that every reopening meets \(L\) units of current paid
incidence and that no such unit can support more than \(L\) reopenings.
Failure is already a concentrated reuse obstruction at one incidence,
which can be passed to the anchor, carry, denominator, or rational
classification machinery.

## AC3h -- labelled fan inside a high-reuse incidence

Assume the second alternative of AC3g.  Thus a paid resource token
\(\pi\) is eligible for a reopening family
\(\mathcal Y\) with

\[
|\mathcal Y|=d>L.
\]

Give every eligibility pair \((j,\pi)\), \(j\in\mathcal Y\), one of at
most \(T\) geometric labels.  A label may record the role of \(\pi\) in
the reopened object: anchor, endpoint, carry channel, denominator chart,
or rational-return type.  On each label class put the full support
conflict graph for the corresponding reopenings.

### Lemma AC3h -- PROVED

Some label \(\lambda\) has a class
\(\mathcal Y_\lambda\) satisfying

\[
\boxed{
|\mathcal Y_\lambda|\geq\left\lceil\frac dT\right\rceil
>\frac LT.
}
\]

For every integer \(\Gamma\geq0\), that same-label class has one of the
following two outcomes:

1. one reopening conflicts with more than \(\Gamma\) other members of
   \(\mathcal Y_\lambda\); or
2. there is a pairwise support-compatible subfamily
   \(\mathcal I\subseteq\mathcal Y_\lambda\) with
   \[
   \boxed{
   |\mathcal I|
   \geq
   \left\lceil
   \frac{|\mathcal Y_\lambda|}{\Gamma+1}
   \right\rceil,
   \qquad
   |\mathcal I|>\frac{L}{T(\Gamma+1)}.
   }
   \]

### Proof

Pigeonhole the \(d\) eligibility pairs among at most \(T\) labels.  This
gives the first box, including its strict inequality because \(d>L\).

If the first outcome fails, the conflict graph induced by
\(\mathcal Y_\lambda\) has maximum degree at most \(\Gamma\).  A greedy
proper colouring uses at most \(\Gamma+1\) colours.  Its largest colour
class is support-compatible and has the size in the second box.  The
strict lower bound follows from
\(|\mathcal Y_\lambda|>L/T\). \(\square\)

The members of \(\mathcal I\) still share the same capacity token, so
AC3h does **not** declare them separately paid.  Its role is
classification: every Hall failure now yields either a second-order
support-conflict overload or a broad compatible fan with one fixed paid
incidence and one fixed arithmetic label.  The geometric no-reuse
theorem may therefore work inside a single token--label fibre rather
than an arbitrary deficient bipartite graph.

[`alternating-core-shared-token-phase.md`](alternating-core-shared-token-phase.md)
proves AC3p--AC3r for every such fibre whose role is separable through
one bounded common phase. Its complete feasibility message is an
intersection \(M\) of phase subsets. The same \(M\) is witnessed by at
most \(|\mathcal A|-|M|\) reopenings, strict message loss occurs at most
\(|\mathcal A|\) times, and a message-redundant reopening receives no
new ticket. A nonempty message yields one joint product state and an
exact additive collateral audit; an empty message has a bounded
exceptional core. The remaining geometric obligation is to prove that
the actual role dictionary is phase-realized, anchor-realized, or
terminally labelled.

`scripts/verify_ac_reextraction.py` exhaustively checks the weighted
colouring bound through six objects, the directed-cycle criterion through
four quotient states, a finite ticket trace, and every strict-support
maximal-depth descent order through seven objects.  It also enumerates
all descent and ticketed-reopening transitions through six objects and
three tickets, and compares the capacitated Hall inequalities with direct
charge assignment on small eligibility systems.  The same enumeration
checks the bounded-overlap expansion and its high-reuse deficient
alternative, together with the same-label fan/conflict dichotomy.
