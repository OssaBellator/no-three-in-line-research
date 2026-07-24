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

## Combination with GC4a

Apply GC4b to the surviving hypergraph at each step of the GC4a peeling
order. If the current load exceeds \(\tau\), that step returns either:

- a pair of current codegree greater than \(\Delta\); or
- more than \(\tau/(2\Delta-1)\) fresh triples forming an
  endpoint-disjoint star.

The star is the exact topology needed by the alternating neutralization
bank, while high pair codegree is a lower-dimensional concentration that
can be tested for common-ratio, carry, or denominator structure.

This is still a candidate-only statement. To complete GC4, the selected
triples must carry current syndrome incidence, or the geometry must prove
that the concentrated pair/star blocks enough admissible candidates to be
charged through GC1--GC3. Latent triples are not relabelled as paid by this
lemma.

`scripts/verify_gc_anchor_link.py` exhaustively checks the link matching
bound for every simple graph on at most six link vertices.
