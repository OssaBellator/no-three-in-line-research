# Universal diagonal-signature bypass

The common-line rectangle bank first exposes two natural local states: the
diagonal on the obstruction line and the opposite cross diagonal.  Their
homogeneous binary signature may be credit-rich, credit-poor, or locally
contradictory.  Dense cross-state conflicts may also localize to a rich line,
pencil, or fixed-anchor secant design.

The cross-block construction PP3qs does not use either natural diagonal.  It
therefore bypasses every original binary signature and every geometric witness
supported only on the original two-state family.  Under sparse unary endpoint
degree, almost all rectangles enter a safe four-state bank regardless of how
bad the original binary CSP was.

## 1. Signature-independent cross-block states

Let \(s,t\) be resource-disjoint rectangles.  Their original supports are

\[
L_s\times R_s
\qquad\text{and}\qquad
L_t\times R_t.
\]

The four cross-block states of PP3qs use only

\[
L_s\times R_t
\qquad\text{and}\qquad
L_t\times R_s.
\]

### Proposition PP3rl -- PROVED

No unit clause, binary bad box, or ternary bad box whose selected points all lie
in the two original rectangle supports directly forbids a cross-block state.

Consequently the following original two-state structures impose no logical
restriction on the new four-state supervariable:

- a credit-poor homogeneous signature;
- a three-rectangle equal-state contradiction;
- an all-cross conflict star or clique;
- a rich common cross line;
- a cross-line pencil;
- a complete fixed-anchor secant design formed from original cross cells.

#### Proof

Every point selected by a cross-block state lies outside both original supports,
by PP3qs.  A bad box is determined by the selected points in its local states.
Therefore a witness using only original-state points is absent from every
cross-block state.  New collinear triples and shadow incidences involving the
cross-block cells must be recomputed; they are exactly the multistate bad boxes
and costs of PP3qw. ∎

This is a change of local state space, not an assertion that the old witness has
vanished from the ambient geometry.

## 2. Safe pairing under sparse unary degree

### Theorem PP3rm -- PROVED

Let a linear resource-disjoint rectangle bank have size \(h\to\infty\), with no
assumption on its original binary signatures.  Suppose the non-designated unary
endpoint graph has maximum degree

\[
d=o(h).
\]

Then, after discarding \(o(h)\) rectangles, the bank may be paired into
resource-disjoint cross-block supervariables with nonempty source-safe state
sets.  Every supervariable moves both designated owners and has removal credit
at least two.

#### Proof

The pairing regularization PP3ra--PP3rc uses only the rectangle resource pairs,
the direct recapture exclusions, and the non-designated unary graph.  It does
not use the original rectangle-state signatures.  Apply PP3rc. ∎

Thus every original dense binary obstruction is bypassed in the sparse-unary
regime.

## 3. Recomputed multistate geometry

After safe pairing, delete locally impossible states and pass to a linear common
alphabet as in PP3re.  Adaptive source preparation gives \(o(K^3)\) ternary bad
boxes, and fixed-colour Ramsey homogenizes the complete pair signature.

### Theorem PP3rn -- PROVED

Under the hypotheses of PP3rm, the original rectangle bank has one of the
following outcomes.

1. A growing safe cross-block bank has an allowed constant state.  If its unary,
   binary, and residual matching costs are diffuse, it gives a strict paid
   improvement by PP3ri--PP3rj.
2. Five cross-block supervariables form a local multistate contradiction.
3. A linear number of paired blocks have no locally admissible cross-block
   state.
4. Cross-block unary or binary cost is concentrated at the two-credit-per-block
   scale.
5. The adaptive high-support ternary estimate fails.

#### Proof

Apply PP3re--PP3rk to the safe paired bank supplied by PP3rm. ∎

The theorem deliberately recomputes all geometry in the new state space; it does
not transfer satisfiability from the original rectangle states.

## 4. Elimination of the original signed frontier

### Corollary PP3ro -- PROVED

In the sparse-unary superregular recapture branch, none of the following is a
separate terminal obstruction:

- the credit-poor homogeneous Boolean signature;
- the three-rectangle Boolean contradiction;
- a dense all-cross conflict graph;
- the rich cross line or cross-line pencil extracted from that graph;
- a complete fixed-anchor secant design on original cross cells.

All five enter the same safe four-state cross-block bank and reduce to the
multistate alternatives PP3rn.

#### Proof

Use PP3rl to discard the original diagonal signature and PP3rm to install the
new safe state space.  Then apply PP3rn. ∎

These structures may still be useful for a direct geometric trade in the dense-
unary regime, but they are unnecessary when unary degree is sublinear.

## 5. Revised rectangle frontier

### Corollary PP3rp -- PROVED

For a superregular adaptively prepared common-line rectangle bank, conversion is
complete whenever:

1. the non-designated unary endpoint degree is \(o(h)\);
2. some Ramsey-homogeneous cross-block state has diffuse unary and binary cost;
3. the residual matching expected shadow is \(o(h)\).

Failure therefore requires at least one of:

- a unary endpoint resource with \(\Omega(h)\) forbidden cross-block cells;
- a linear family of locally impossible cross-block state sets;
- a five-supervariable multistate contradiction;
- unary or binary cross-block cost concentrated at the two-credit-per-block
  scale;
- residual unary or binary weighted shadow at the same scale.

The original two-state Boolean signature and its cross-conflict geometry are no
longer part of the sparse-unary frontier.