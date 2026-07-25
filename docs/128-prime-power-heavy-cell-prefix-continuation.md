# Heavy thin carry cells open an executable prefix continuation

CMR310--CMR317 classify the third witness of a heavy thin carry cell by its
primitive line parameter.  In the state containing any such certificate, all
three points lie in one same-layer prefix geometry.  Binary cases are assigned
by their unique closest pair; equilateral cases lie wholly in one common prefix
block.  The complete rematching bank CMR75 moves every old point of the assigned
block and destroys the certificate in every bank state.

Let

\[
P_0=P,
\qquad
P_1=P+G(u,v),
\qquad
P_2=P+q(u,v)
\]

be one compatible same-layer candidate triple from CMR314. Put

\[
b=v_p(G),
\qquad
c=v_p(q),
\qquad
e=v_p(q-G).
\]

## 1. External routing is the original binary star

### Theorem CMR340 — PROVED

If `c<b`, then `P_0,P_1` are the unique closest pair at depth `b`, while `P_2`
lies outside their depth-`b` prefix block. In every saturated state containing
the triple, CMR76 assigns it to that unique layer-prefix block and every state
of the corresponding CMR75 bank destroys it.

### Proof

CMR315 gives

\[
(b,c,e)=(b,c,c).
\]

Thus `P_0,P_1` are the unique closest pair. Their coordinate differences are
divisible by `p^b`, while the differences from `P_2` have exact valuation
`c<b`. The third point is therefore outside the closest pair's depth-`b`
prefix block. All three candidate cells belong to the same rematched
permutation layer. These are exactly the hypotheses of CMR76. ∎

## 2. Internal routing is equilateral or a deeper binary star

### Theorem CMR341 — PROVED

Assume `c>=b`.

1. If `c>b`, then `P_0,P_2` are the unique closest pair at depth `c`, and `P_1`
   lies outside their depth-`c` prefix block.
2. If `c=b<e`, then `P_1,P_2` are the unique closest pair at depth `e`, and
   `P_0` lies outside their depth-`e` prefix block.
3. If `c=e=b`, all three points lie in one depth-`b` prefix block and occupy
   three distinct children of that block.

In all three cases, a CMR75 prefix-rematching bank destroys the triple.

### Proof

The first two alternatives are the non-equilateral cases of CMR316. The other
two pair depths are smaller than the unique closest-pair depth, so the third
point lies outside the deeper closest-pair prefix block. Apply CMR76.

In the equilateral case, every pairwise coordinate difference is divisible by
`p^b`, so all three points have the same depth-`b` prefix. Each pair has exact
valuation `b`, so the three points occupy distinct children. The unique common
layer-prefix block contains all three old cells. CMR75 moves every old point of
that block, hence removes the original triple. ∎

## 3. Every heavy cell opens a prefix continuation

### Corollary CMR342 — PROVED

Every certificate in a heavy-cell population from CMR303 opens an executable
CMR75 prefix-rematching continuation in the candidate state containing it.
The assigned block is

- the original depth-`b` Hall block in the external or equilateral case; or
- the strictly deeper closest-pair block in the internal non-equilateral case.

### Proof

Apply CMR340 and CMR341 to the exhaustive valuation alternatives of
CMR314--CMR316. ∎

## 4. Strict-depth no-return for internal binary recreations

### Corollary CMR343 — PROVED

Suppose a continuation branch repeatedly selects the deeper closest pair from
the internal non-equilateral alternative of CMR341 without expanding the
closure envelope. Starting from depth `b`, this can occur at most

\[
\boxed{h-1-b}
\]

times before an equilateral certificate appears or the available prefix depths
are exhausted.

### Proof

Each internal non-equilateral transfer raises the unique closest-pair depth
strictly. CMR317 bounds the number of strict increases. ∎

## 5. Revised thin-carry endpoint

The **heavy-cell** half of CMR303 is now completely executable at the local
level:

- external witnesses return directly to the original binary-star prefix bank;
- internal non-equilateral witnesses open the same bank at a deeper scale;
- equilateral witnesses open the bank on their common prefix block;
- repeated internal depth transfer terminates.

The unresolved global thin-blocker task is therefore narrower. It must charge

1. the **dispersed-cell** half of CMR303; and
2. fine stars recreated after later coarse repairs.

No all-`n` theorem is claimed here. The closest-pair ownership, equilateral
prefix assignment, and strict-depth bound are checked in
[`scripts/verify_prime_power_heavy_cell_continuation.py`](../scripts/verify_prime_power_heavy_cell_continuation.py).
