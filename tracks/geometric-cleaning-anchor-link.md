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

`scripts/verify_gc_anchor_link.py` exhaustively checks the matching bound
and weighted \(2\Delta-1\)-colour partition for every simple graph on at
most six link vertices.
