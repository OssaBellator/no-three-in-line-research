# Anchor-link structure inside a high-load conflict witness

GC4a returns an ordered sequence of vertices carrying fresh surviving
conflict mass. For candidate triples, each high-load step has an exact
second-level dichotomy: pair concentration or a large endpoint-disjoint
star.

Let \(\mathcal H\) be a simple three-uniform hypergraph of surviving
candidate triples. For a vertex \(v\), define

\[
d(v)=|\{T\in\mathcal H:v\in T\}|,
\qquad
d(v,x)=|\{T\in\mathcal H:\{v,x\}\subseteq T\}|.
\]

## GC4b -- anchor-link dichotomy

### Lemma GC4b -- PROVED

For every integer \(\Delta\geq1\), every vertex \(v\) has one of:

1. a second vertex \(x\) with
   \[
   d(v,x)>\Delta;
   \]
2. a family \(\mathcal S_v\) of at least
   \[
   \boxed{\frac{d(v)}{2\Delta-1}}
   \]
   triples which all contain \(v\) and are pairwise disjoint outside
   \(v\).

### Proof

Form the link graph \(L_v\): its vertices are \(V(\mathcal H)\setminus
\{v\}\), and \(\{x,y\}\) is an edge when \(\{v,x,y\}\in\mathcal H\).
Its number of edges is \(d(v)\), and the degree of \(x\) is \(d(v,x)\).

If the first alternative fails, \(L_v\) has maximum degree at most
\(\Delta\). Greedily choose a link edge and delete every edge meeting it.
Each chosen edge deletes at most \(2\Delta-1\) edges, so the resulting
matching has at least \(d(v)/(2\Delta-1)\) members. The corresponding
triples form the required star.
\(\square\)

## GC4c -- weighted anchor-link dichotomy

Give the surviving triples through \(v\) arbitrary nonnegative weights
\(w(T)\), and write

\[
W_v=\sum_{T\ni v}w(T).
\]

### Lemma GC4c -- PROVED

For every integer \(\Delta\geq1\), either some pair
\(\{v,x\}\) has codegree greater than \(\Delta\), or there is a family
\(\mathcal S_v\) of triples, pairwise disjoint outside \(v\), such that

\[
\boxed{
\sum_{T\in\mathcal S_v}w(T)
\geq
\frac{W_v}{2\Delta-1}.
}
\]

### Proof

If all pair codegrees through \(v\) are at most \(\Delta\), the link
graph \(L_v\) has maximum degree at most \(\Delta\). Greedy edge
colouring uses at most \(2\Delta-1\) colours, because an edge meets at
most \(2\Delta-2\) other edges. Each colour class is a matching, and the
weights of the colour classes sum to \(W_v\). A heaviest class gives the
displayed bound. \(\square\)

## Combination with GC4a

Apply GC4b to the surviving hypergraph at each step of the GC4a peeling
order. If the current load exceeds \(\tau\), that step returns either:

- a pair of current codegree greater than \(\Delta\); or
- more than \(\tau/(2\Delta-1)\) fresh triples forming an
  endpoint-disjoint star.

The star is the exact topology needed by the alternating neutralization
bank, while high pair codegree is a lower-dimensional concentration that
can be tested for common-ratio, carry, or denominator structure.

GC4c applies directly to the normalized weights in GC4a. If those
weights have already been identified with current syndrome incidence, it
returns a genuinely paid star with the same
\(1/(2\Delta-1)\)-fractional guarantee. If they are only latent
candidate-conflict weights, the output remains latent. Thus the
low-codegree extraction no longer loses whatever weight is supplied, but
the geometric conversion from candidate weight to current paid incidence
is still required before delegation through GC1--GC3.

## GC4d -- accumulated fresh-star mass

Run GC4a on the triple-conflict family for \(k\) high-load steps at
threshold \(\tau\). At step \(i\), give each surviving triple through the
deleted anchor \(v_i\) its current weight. These step families are
disjoint because GC4a deletes a conflict at its first selected anchor.

### Corollary GC4d -- PROVED

For every integer \(\Delta\geq1\), either some one of the first \(k\)
steps contains a pair of current codegree greater than \(\Delta\), or
there are stars \(\mathcal S_1,\ldots,\mathcal S_k\) such that:

1. every \(\mathcal S_i\) is endpoint-disjoint outside \(v_i\);
2. no triple belongs to two different \(\mathcal S_i\); and
3. their total fresh weight satisfies
   \[
   \boxed{
   \sum_{i=1}^k\sum_{T\in\mathcal S_i}w(T)
   >
   \frac{k\tau}{2\Delta-1}.
   }
   \]

### Proof

At step \(i\), the current weighted load \(W_i\) at \(v_i\) exceeds
\(\tau\). If the high-pair alternative does not occur, GC4c supplies a
star of weight at least \(W_i/(2\Delta-1)\). The conflict families
charged at distinct peeling steps are disjoint, so their selected
subfamilies are also disjoint. Summing the \(k\) strict load inequalities
proves the box. \(\square\)

GC4d turns a long bounded-codegree peeling witness into a quantified
bank of fresh star objects without reusing any conflict certificate.
Their cross-star row, column, and collateral incompatibilities still
have to be regularized before simultaneous installation.

## GC4e -- weighted cross-star regularization

Put every star returned by GC4d into a conflict graph, joining two stars
whenever they cannot be installed simultaneously. The relation must
include row/column overlap, shared replacement cells, and nonadditive
cross-star collateral. Give star \(i\) its fresh weight \(W_i\), and put

\[
\Lambda_i=\sum_{j\in N[i]}W_j.
\]

### Lemma GC4e -- PROVED

For every \(K\geq1\), either:

1. some star has a weighted overload
   \[
   \boxed{\Lambda_i>K W_i};
   \]
2. a simultaneously installable star family retains at least
   \[
   \boxed{\frac1K\sum_iW_i}
   \]
   fresh weight.

Consequently, in the bounded-pair-codegree case of GC4d, the second
alternative retains more than

\[
\boxed{
\frac{k\tau}{K(2\Delta-1)}
}
\]

fresh weight after \(k\) peeling steps.

### Proof

Assign star \(i\) an independent exponential clock of rate \(W_i\), and
select it when its clock is earliest in its closed conflict
neighbourhood. The selected stars are compatible, and star \(i\) is
selected with probability \(W_i/\Lambda_i\). If the first alternative
fails, the expected selected weight is

\[
\sum_i\frac{W_i^2}{\Lambda_i}
\geq
\frac1K\sum_iW_i.
\]

Some realization has at least the expected weight. Combine this with
GC4d for the final display. \(\square\)

If the \(W_i\) are current syndrome weights, both alternatives are paid:
the overload itself identifies a star together with more than \(K W_i\)
neighbouring paid mass. For latent candidate weights the same caveat as
GC4c remains; this lemma preserves but does not create payment.

## GC4f -- certificate-labelled overload descent

Assume every cross-star conflict incident with a star \(i\) has one of
at most \(T\) certificate labels. A label records the actual reason for
incompatibility, such as a shared row, shared column, replacement cell,
anchor, or collateral type. Let \(S_\lambda(i)\) be the neighbouring
stars carrying label \(\lambda\).

### Lemma GC4f -- PROVED

If \(\Lambda_i>K W_i\) for \(K>1\), then for every \(Q\ge1\) some label
\(\lambda\) carries

\[
\boxed{
\sum_{j\in S_\lambda(i)}W_j
>
\frac{K-1}{T}W_i
}
\]

and either:

1. one star in \(S_\lambda(i)\) has restricted closed-neighbourhood load
   greater than \(Q\) times its own weight inside the induced conflict
   graph on \(S_\lambda(i)\); or
2. a simultaneously installable subfamily
   \(\mathcal I\subseteq S_\lambda(i)\) carries more than
   \[
   \boxed{
   \frac{K-1}{TQ}W_i.
   }
   \]

For every \(\theta>0\), the same label class also contains either a star
of weight greater than \(\theta W_i\), or more than
\((K-1)/(T\theta)\) stars.

### Proof

Subtract \(W_i\) from the overload and partition the remaining weight
among the at most \(T\) incident certificate labels. A heaviest class
proves the first box. Apply GC4e with parameter \(Q\) to the conflict
graph induced by that class. Its compatible-family alternative gives
the second box, while its other alternative is precisely the stated
restricted overload. If no class member is heavier than
\(\theta W_i\), the first box divided by that upper bound gives the
cardinality conclusion. \(\square\)

For paid weights, GC4f removes mixtures of incompatibility mechanisms
before delegation: one explicit certificate type now carries the
recursive obstruction. For latent weights it still does not supply the
missing syndrome-incidence payment.

## GC4g -- strict-support potential for certificate recursion

Fix the finite star family \(\mathcal S\) present at the start of one
GC4 regularization epoch.  A pure GC4f recursive descent has states

\[
(U_0,i_0),(U_1,i_1),\ldots,
\qquad i_t\in U_t\subseteq\mathcal S,
\]

and its recursive overload alternative replaces \(U_t\) by one
certificate class

\[
U_{t+1}=S_{\lambda_t}^{U_t}(i_t)
\subseteq U_t\setminus\{i_t\}.
\]

No discarded star is reintroduced inside the epoch.

### Lemma GC4g -- PROVED

The support-deficit potential

\[
\boxed{
\Gamma_{\rm supp}(U)=|\mathcal S|-|U|
}
\]

increases by at least one at every pure GC4f recursive overload step.
Consequently an epoch beginning on \(U_0\) has at most
\(|U_0|-1\) such steps and contains no recursive state cycle.

### Proof

A star is not its own conflict neighbour, so every incident
certificate class omits the current centre.  Hence

\[
|U_{t+1}|\leq |U_t|-1
\]

and the displayed potential increases by at least one.  It is bounded
above by \(|\mathcal S|-1\) on a nonempty recursive state.  Strictly
nested supports cannot revisit a previous state. \(\square\)

Thus label-pure overload descent itself terminates without any geometric
assumption.  Any later return to a discarded star must enlarge the
support and is a separate reuse event.  Such a reopening still needs
current syndrome payment or a bounded reuse ticket; likewise GC4g does
not repair the latent-weight caveat in GC4c--GC4f.

## GC4h -- combined descent/reopening potential

Let \(n=|\mathcal S|\), and suppose one paid regularization component
has at most \(R\) support-reuse tickets.  Record a nonempty active star
support \(U\subseteq\mathcal S\) and the number \(t\) of tickets already
used.  Every nonterminal transition must either strictly shrink \(U\)
without a ticket, or consume at least one ticket before replacing \(U\)
by an arbitrary nonempty support.

### Lemma GC4h -- PROVED

The scalar potential

\[
\boxed{
\Gamma_{\rm reopen}(U,t)
=
nt+n-|U|
}
\]

increases by at least one on every such transition and is at most
\(nR+n-1\).  Hence the component has at most

\[
\boxed{
nR+n-\Gamma_{\rm reopen}(U_0,t_0)
}
\]

further transition-or-terminal calls from \((U_0,t_0)\).

### Proof

A strict shrink raises \(n-|U|\) by at least one.  A ticket raises the
first term by at least \(n\), while an arbitrary support replacement can
lower \(n-|U|\) by at most \(n-1\).  Both transition types therefore
increase the potential.  The bound follows from
\(0\leq t\leq R\) and \(1\leq|U|\leq n\). \(\square\)

Thus a GC4f recursion may restart at full support after a paid
reopening without resetting the termination argument.  Once current
syndrome incidence bounds the total number of reopenings, GC4g--GC4h
give an explicit finite regularization depth.  They still do not turn
latent candidate weight into that payment.

## GC4i -- capacitated Hall certificate for paid star reopenings

Fix the reopening events \(\mathcal J\) in a finite regularization
prefix.  Let \(\mathcal P\) be a set of atomic current-syndrome
incidences, certified destroyed triples, or other nonreusable paid
resources.  Give \(\pi\in\mathcal P\) integer capacity \(c_\pi\geq0\).
For each reopening \(j\), let \(A_j\subseteq\mathcal P\) be the nonempty
set of resources whose incidence actually meets the reopened star
support and is therefore eligible to pay for \(j\).

### Lemma GC4i -- PROVED

A capacity-respecting payment

\[
\chi(j)\in A_j,
\qquad
|\chi^{-1}(\pi)|\leq c_\pi,
\]

exists if and only if every \(\mathcal X\subseteq\mathcal J\) obeys

\[
\boxed{
|\mathcal X|
\leq
\sum_{\pi\in\bigcup_{j\in\mathcal X}A_j}c_\pi.
}
\]

If this condition holds for every finite prefix, then there are at most

\[
R=\sum_{\pi\in\mathcal P}c_\pi
\]

reopenings in the whole component.  GC4h consequently gives the scalar
ceiling \( |\mathcal S|R+|\mathcal S|-1\).  If the condition fails, it
returns a subfamily \(\mathcal X\) whose eligible current-incidence
capacity is strictly smaller than the number of star reopenings it must
support.

### Proof

Clone each resource \(\pi\) into \(c_\pi\) distinguishable tokens and
join reopening \(j\) to every token belonging to a resource in \(A_j\).
Hall's marriage theorem matches all reopenings precisely when every
subfamily sees at least as many tokens as events.  Its token
neighbourhood has the cardinality in the boxed sum, proving the
equivalence.  Applying the inequality to all events bounds their number
by \(R\).  An infinite component would have a prefix with \(R+1\)
reopenings, which is impossible.  GC4h then applies with its ticket
counter equal to the reopening count. \(\square\)

GC4i sharpens the latent-to-paid frontier.  A geometric proof need not
guess a compatible greedy charge order: it may prove the boxed
neighbourhood inequality directly.  Conversely, failure exposes a
specific cluster of star reopenings with too small a current-syndrome
neighbourhood; that cluster, rather than the entire mixed conflict
system, must be converted to an absorber or an alternating-core
delegation.

`scripts/verify_gc_anchor_link.py` exhaustively checks the matching bound
and weighted \(2\Delta-1\)-colour partition for every simple graph on at
most six link vertices, together with strict-support recursion through
every maximal-depth order on at most seven stars and every ticketed
support replacement through six stars and three tickets.  It also
compares the capacitated Hall test with direct paid-token assignment on
small reopening systems.
