# Historical line stars and fixed-pair rematching

**Branch:** `research/alternating-core-chain`

AC3gt--AC3hk reduce the remaining historical pivot outputs to current
certificate families with one fixed centre, one real line or one fixed context
cell.  This note closes their purely combinatorial geometry.  A weighted
line-star either has a context-disjoint endpoint matching, or one fixed pair
carries a labelled overlap overload.  A context-disjoint matching supports a
direct current-anchor rematching bank; a fixed-pair overload feeds the existing
AC3m--AC3n pair-core bank or collapses to one heavy current certificate.

No alternative target states are combined.  Every executable bank below is
built inside one fixed current two-layer state.

## Weighted line-star graph

Fix one current cell `z` and a weighted family of distinct current collinear
triples

\[
\mathcal F=\{\{z,x_C,y_C\}:C\in\mathcal F\}.
\]

The two outside cells of a certificate form an edge

\[
e_C=\{x_C,y_C\}
\]

in a simple graph `G_z`.  Exact duplicate certificates are aggregated before
forming the graph.  Put

\[
W=\sum_{C\in\mathcal F}w(C).
\]

For an edge `e`, let `N[e]` be its closed neighbourhood in the line graph and
put

\[
L(e)=\sum_{e'\in N[e]}w(e').
\]

For an outside cell `x`, put

\[
\mu(x)=\sum_{C:x\in e_C}w(C).
\]

## AC3hl -- weighted matching or fixed-pair overload -- PROVED

For every real `K>=1`, exactly one of the following can be selected.

1. **Fixed-pair overload.**  Some edge `e={x,y}` satisfies

   \[
   \boxed{L(e)>K w(e).}
   \]

   One endpoint `v in {x,y}` then satisfies

   \[
   \boxed{\mu(v)>\frac K2w(e).}
   \]

   Thus the current pair `{z,v}` supports a same-role certificate family of
   total weight greater than `K w(e)/2`.

2. **Endpoint-disjoint matching.**  There is a subfamily
   `M subseteq F` whose outside pairs are pairwise disjoint and whose total
   weight satisfies

   \[
   \boxed{w(\mathcal M)\ge W/K.}
   \]

### Proof

If the first alternative fails, greedily choose any remaining positive-weight
edge and delete its closed line-graph neighbourhood.  Each chosen edge of
weight `w(e)` deletes weight at most `K w(e)`.  The chosen edges form a
matching, and summing the deletion inequalities gives `w(M)>=W/K`.

For an overloaded edge `e={x,y}`, every edge in `N[e]` contains `x` or `y`.
Therefore

\[
L(e)\le \mu(x)+\mu(y),
\]

so one endpoint has load greater than `K w(e)/2`. QED.

## AC3hm -- fixed-pair overload closure -- PROVED

Fix the endpoint `v` returned by AC3hl and let

\[
d=d(z,v)
\]

be the number of distinct current certificates containing the pair `{z,v}`.
Write `M=\mu(v)`.

Exactly one of the following holds.

1. `d>12`, and AC3o returns either:
   - an executable AC3m pair-core bank carrying certified payment at least
     \[
     \boxed{M/2,}
     \]
     or
   - one current certificate of weight at least
     \[
     \boxed{M/12.}
     \]
2. `d<=12`, and one current certificate containing `{z,v}` has weight at
   least
   \[
   \boxed{M/12.}
   \]

Consequently every fixed-pair overload yields an executable pair-core bank or
one individually heavy current certificate.  In terms of the overloaded
centre edge from AC3hl, these scales are respectively greater than

\[
\boxed{K w(e)/4}
\qquad\hbox{or}\qquad
\boxed{K w(e)/24}.
\]

### Proof

When `d>12`, apply the weighted statement of AC3o to the pair-core family.
When `d<=12`, weighted pigeonhole gives a member of weight at least `M/d`,
hence at least `M/12`.  Substitute `M>K w(e)/2`. QED.

## Current-anchor rematching

Now assume `M subseteq F` is endpoint-disjoint outside `z`.  Give each endpoint
incidence the weight of its certificate.  The total incidence weight is
`2w(M)`.  One of the two permutation layers carries incidence weight at least
`w(M)`.  Let `M_ell` be the certificates with at least one outside endpoint in
that layer.  Since one certificate contributes at most twice its weight to the
chosen layer,

\[
\boxed{w(\mathcal M_\ell)\ge w(\mathcal M)/2.}
\]

Choose one outside endpoint `q_C` in the fixed layer for every
`C in M_ell`.  Endpoint-disjointness makes the chosen cells distinct; being in
one permutation layer makes their rows and columns distinct.

Let their columns and rows be `C={c_1,...,c_t}` and `R={r_1,...,r_t}`.  In the
block `C x R`, forbid the original diagonal and every cell occupied by the
opposite permutation layer.  Every block row and column contains at most two
forbidden cells.

## AC3hn -- direct current-anchor rematching bank -- PROVED

If `t>=7`, the AN1 family `Omega(F)` is nonempty.  Every allowed rematching:

1. preserves both permutation layers and their disjointness;
2. moves every selected endpoint `q_C`;
3. destroys every selected exact certificate
   \[
   \{z,x_C,y_C\};
   \]
4. has the AN1 cylinder bound
   \[
   \Pr(Q\subseteq M_\pi)\le \frac{128}{(t)_r}
   \]
   for every compatible nonforbidden rank-`r` partial matching.

The selected certificates are distinct current resources, so their full total
weight is valid certified payment.

### Proof

AN1 gives a perfect matching avoiding the two forbidden matchings.  Rematching
inside the selected layer preserves its row and column sets, while the
opposite-layer forbidden cells preserve layer disjointness.  The forbidden
diagonal removes every selected endpoint from its old physical cell.  Hence
each exact old certificate loses one of its cells and is destroyed.  The
cylinder estimate is AN1. QED.

## AC3ho -- weighted historical-line router -- PROVED

Apply AC3hl to a historical line-star of total weight `W`.

- In the fixed-pair-overload branch, AC3hm gives a pair-core bank or one heavy
  current certificate.
- In the matching branch, `w(M)>=W/K`.  After the layer-incidence selection,
  `w(M_ell)>=W/(2K)`.
  - If `|M_ell|>=7`, AC3hn gives a direct current-anchor bank with certified
    payment at least
    \[
    \boxed{W/(2K).}
    \]
  - If `|M_ell|<=6`, one current certificate has weight at least
    \[
    \boxed{W/(12K).}
    \]

Thus a historical line-saturated or fixed-context star never remains an
unstructured family.  It yields one of:

1. an executable pair-core bank;
2. an executable current-anchor rematching bank;
3. one individually heavy current certificate;
4. one explicit AC3fr support/protected overload arising from the complete
   envelope of either bank.

All line, axis, current/new-rank, source, channel, closure, blocker, carry, RI
and denominator labels remain attached.

### Proof

Only the layer-incidence calculation remains.  The selected matching has
total endpoint-incidence weight `2w(M)`.  One layer carries at least `w(M)`.
Each represented certificate contributes at most twice its own weight, so the
represented certificate weight is at least `w(M)/2`.  If fewer than seven
certificates are represented, one has at least one sixth of that weight.
Otherwise AC3hn applies. QED.

## AC3hp -- failed current-anchor bank returns a realized rank -- PROVED

Let a direct current-anchor bank from AC3hn destroy certified weight `D`.
Choose uniformly from its finite allowed rematchings.  Relative to the parent
state, let `E_r` be the exact expected weight of genuinely created union
triples of created-cell rank `r=1,2,3`.

Then

\[
\mathbb E[\text{created collateral}]=E_1+E_2+E_3.
\]

If `D>E_1+E_2+E_3`, one rematching state improves.  If no state improves, one
rank satisfies

\[
\boxed{E_r\ge D/3.}
\]

AC3gk realizes that rank in one legal rematching state without weight loss.
For every `K'>=1`, AC3gi--AC3gj then return an explicit overload, a pivot bank
with payment at least

\[
\boxed{D/(3K'),}
\]

or a next-generation rank of expected weight at least

\[
\boxed{D/(9K').}
\]

In the AC3ho matching branch, `D>=W/(2K)`, so these become

\[
\boxed{W/(6KK')}
\qquad\hbox{and}\qquad
\boxed{W/(18KK')}.
\]

### Proof

Every local state destroys the same distinct selected certificates, so
destroyed payment is exactly additive.  Created triples partition by
created-cell rank.  Failure of strict improvement makes their expected total
at least `D`; pigeonhole gives `D/3`.  Apply AC3gk--AC3gj. QED.

## Consequence

The remaining full-line and old-axis historical profiles are now reduced to
the already finite executable interfaces:

- pair-core rematching;
- current-anchor rematching;
- one heavy current certificate and its union-safe pivot;
- explicit labelled envelope overloads;
- or a realized next created-cell rank.

The arithmetic frontier is correspondingly narrower: only the retained label
of a heavy certificate, pair-core return, or failed rematching rank remains to
be routed through carry, BDA, RI or the finite transition graph.  No raw
fixed-pair or line-star topology remains.

## Finite check

`scripts/verify_ac_historical_line_router.py` exhausts small weighted simple
graphs, every closed-neighbourhood router threshold, fixed-pair degree and
weight alternatives, endpoint-layer incidence selections, normalized
seven-endpoint rematching blocks, exact destruction of selected certificates,
rank pigeonholes and all displayed composition constants.
