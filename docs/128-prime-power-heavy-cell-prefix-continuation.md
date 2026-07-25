# Heavy thin carry cells open an executable prefix continuation

CMR310--CMR317 classify the third witness of a heavy thin carry cell by its
primitive line parameter.  The non-equilateral cases are not new terminal
objects.  In the state containing the certificate, their unique closest pair
is a same-layer binary prefix star, so the complete rematching bank CMR75--CMR76
destroys it.  Only the equilateral cluster class remains outside that bank.

Let

\[
P_0=P,
\qquad
P_1=P+G(u,v),
\qquad
P_2=P+q(u,v)
\]

be one compatible same-layer candidate triple from CMR314.  Put

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
lies outside their depth-`b` prefix block.  In every saturated state containing
the triple, CMR76 assigns it to that unique layer-prefix block and every state
of the corresponding CMR75 bank destroys it.

### Proof

CMR315 gives

\[
(b,c,e)=(b,c,c).
\]

Thus `P_0,P_1` are the unique closest pair.  Their coordinate differences are
divisible by `p^b`, while the differences from `P_2` have exact valuation
`c<b`.  The third point is therefore outside the closest pair's depth-`b`
prefix block.  All three candidate cells belong to the same rematched
permutation layer.  These are exactly the hypotheses of CMR76. ∎

## 2. Non-equilateral internal routing is a deeper binary star

### Theorem CMR341 — PROVED

Assume `c>=b` and the triple is not equilateral at depth `b`.

1. If `c>b`, then `P_0,P_2` are the unique closest pair at depth `c`, and `P_1`
   lies outside their depth-`c` prefix block.
2. If `c=b<e`, then `P_1,P_2` are the unique closest pair at depth `e`, and
   `P_0` lies outside their depth-`e` prefix block.

In either case, the corresponding CMR75 bank destroys the triple.

### Proof

This is the two non-equilateral alternatives of CMR316.  In the first case the
other two pair depths equal `b<c`; in the second they equal `b<e`.  Hence the
third point lies outside the deeper closest-pair prefix block.  Apply CMR76. ∎

## 3. Heavy-cell continuation dichotomy

### Corollary CMR342 — PROVED

Let a heavy-cell population from CMR303 be realized as replacement certificates
across its candidate states.  At least one of the following holds.

1. One state contains an equilateral same-layer triple at the heavy-cell depth.
2. One state contains a binary same-layer triple and hence opens an executable
   CMR75 prefix-rematching continuation.

If the population contains no equilateral certificate, every one of its
certificates opens such a binary continuation, at either the original cell
depth or a strictly deeper depth.

### Proof

CMR314--CMR316 exhaust the parameter valuation patterns.  Apply CMR340 to the
external case and CMR341 to the two internal non-equilateral cases. ∎

## 4. Strict-depth no-return for internal binary recreations

### Corollary CMR343 — PROVED

Suppose a continuation branch repeatedly selects the deeper closest pair from
the internal non-equilateral alternative of CMR341 without expanding the
closure envelope.  Starting from depth `b`, this can occur at most

\[
\boxed{h-1-b}
\]

times before an equilateral certificate appears or the available prefix depths
are exhausted.

### Proof

Each internal non-equilateral transfer raises the unique closest-pair depth
strictly.  CMR317 bounds the number of strict increases. ∎

## 5. Revised thin-carry endpoint

The **heavy-cell** half of CMR303 is now locally executable:

- external witnesses return directly to the original binary-star prefix bank;
- internal non-equilateral witnesses open the same bank at a deeper scale;
- repeated internal depth transfer terminates;
- only equilateral certificates leave the binary bank.

The unresolved global thin-blocker task is therefore narrower.  It must charge

1. the **dispersed-cell** half of CMR303;
2. equilateral heavy-cell certificates;
3. and fine binary stars recreated after later coarse repairs.

No all-`n` theorem is claimed here.  The closest-pair ownership and prefix-block
assignment are checked in
[`scripts/verify_prime_power_heavy_cell_continuation.py`](../scripts/verify_prime_power_heavy_cell_continuation.py).
