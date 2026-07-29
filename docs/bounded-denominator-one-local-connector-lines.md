# Connector-line classification for off-diagonal one-local channels

**Branch:** `research/bounded-denominator-absorbers`

BDA5bo--BDA5bq reduce the balanced-floor off-diagonal work to fifteen unordered channel templates.  Six of those templates compare two distinct one-local channels from

\[
\mathcal W_1=\{A,B,C,D\}.
\]

This note closes their exact cross-role overlap geometry.

Fix distinct channel vectors `z,z'` from `{z_A,z_B,z_C,z_D}`, distinct role parameters `u,v`, and the local cells

\[
U=P+uz,
\qquad
V=P+vz'.
\]

A context-pair address is an unordered pair `{X,Y}` of distinct fixed cells.

## BDA5br -- common context pairs lie on one connector -- PROVED

Suppose both triples

\[
\{U,X,Y\},
\qquad
\{V,X,Y\}
\]

are collinear.

1. If `U!=V`, then all four cells lie on the unique connector line
   \[
   \boxed{L_{z,z'}(u,v)=\operatorname{line}(P+uz,P+vz').}
   \]
   In particular, `X,Y in L_{z,z'}(u,v)`.
2. If `U=V`, then
   \[
   \boxed{uz=vz'}
   \]
   is an exact local-cell collision profile.

Conversely, in the noncollision case, every distinct context pair on the connector line completes both one-local triples.

### Proof

The first collinearity places `U,X,Y` on the context line through `X,Y`; the second places `V` on the same line.  If `U` and `V` are distinct, that line is uniquely their connector.  If they coincide, subtract `P` to obtain the collision identity.  The converse is immediate. QED.

## BDA5bs -- exact weighted overlap decomposition -- PROVED

Let `E_u,E_v` be weighted multisets of context-pair addresses for the two role sides.  Aggregate aliases first.  For each address `e`, write its two weights as `w_u(e),w_v(e)` and put

\[
O=\sum_e\min\{w_u(e),w_v(e)\}.
\]

Then both families split losslessly into:

1. common overlap of weight `O`;
2. role-`u` exclusive residual of weight `W_u-O`;
3. role-`v` exclusive residual of weight `W_v-O`.

Outside the local-cell collision profile, every address contributing to `O` lies on the single connector line `L_{z,z'}(u,v)`.

### Proof

At each address remove the common amount `min(w_u,w_v)` from both sides.  The residuals are nonnegative and have disjoint address support.  Sum over addresses and apply BDA5br to every common address. QED.

## BDA5bt -- six-template weighted router -- PROVED

Assume each selected role-side family has weight at least `Q`.  For any `0<theta<1`, one of the following holds:

1. the exact collision profile `uz=vz'` occurs;
2. connector-line overlap has weight at least `theta Q`;
3. both exclusive residuals have weight greater than `(1-theta)Q`.

At `theta=1/2`, every off-diagonal one-local template yields a collision, one connector-line family of weight at least `Q/2`, or two address-disjoint role families each of weight greater than `Q/2`.

There are exactly

\[
\boxed{\binom42=6}
\]

unordered one-local templates, so the unresolved off-diagonal BDA geometry is reduced from fifteen templates to the nine templates involving `CD` or `AB`, together with payment/realization of the connector or exclusive outputs above.

### Proof

If the collision does not occur, use BDA5bs.  If `O<theta Q`, then `W_u-O>=(1-theta)Q` and similarly for `v`, with strict inequality when the overlap inequality is strict.  The template count is the number of unordered pairs from four one-local channels. QED.

## Finite check

`scripts/verify_bda_one_local_connector_lines.py` exhausts small decoder parameters and context cells, checks the connector-line equivalence, the exact overlap decomposition, and the weighted `theta=1/2` router for all six unordered one-local channel templates.
