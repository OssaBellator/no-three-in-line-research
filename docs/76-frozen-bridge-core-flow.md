# Marker flow for the frozen part of one bridge core

PX112 shows that a bridge state has a nine-row nonlinear core

\[
W=S\cup T\cup\{c\}
\]

and that five rows

\[
W\setminus U
\]

are untouched by every one-step trade.  This chapter gives a global
condition-preserving flow for those five frozen edges.

Let \(p\equiv1\pmod4\) be prime with \(p\ge61\).  Use an affine root

\[
F(x)=ix+b,
\qquad i^2=-1,
\]

and one near-parallel class \(\mathcal P_c\).  Let \(S,T\in\mathcal P_c\) be
adjacent parent blocks, and apply their root trades followed by one bridge on
support \(U\).  Call the resulting source mapping \(G\).

Put

\[
L_c(x)=-ix+b+2ic.
\]

Before the bridge, the two parent blocks and their omitted centre all have the
\(L_c\)-values.  The bridge is exactly the \(L_c\)-root trade on \(U\).
Consequently:

- \(G=L_c\) on \(W\setminus U\);
- \(G\) is the one-square \(L_c\)-descendant on \(U\);
- \(G=F\) outside \(W\).

Fix a target row

\[
x\in W\setminus U
\]

and its source edge

\[
e=(x,G(x))=(x,L_c(x)).
\]

Let \(F_0\) be any partial matching of size at most two, compatible with \(e\),
and contained in \(G\).

## 1. Completion and restoration

Perform the following path.

1. Reverse the bridge on \(U\).  The state returns to the two-parent packing.
2. Toggle every block of
   \[
   \mathcal P_c\setminus\{S,T\}.
   \]
   The state becomes the global opposite affine root \(L_c\).
3. Apply the \(L_c\)-root trade on \(U\).  This restores every source edge on
   the active bridge support.
4. For each conditioned row \(y\notin W\), apply the unique block
   \(B_y\in\mathcal P_c\) containing \(y\).  This changes \(L_c\) back to \(F\)
   on that block and restores the source condition at \(y\).
5. Choose one additional deterministic marker block
   \[
   M\in\mathcal P_c\setminus\bigl(\{S,T\}\cup\{B_y\}\bigr)
   \]
   and apply its \(L_c\)-root trade.

The supports in steps 3--5 are pairwise disjoint: \(U\subseteq S\cup T\cup\{c\}\),
while all \(B_y\) and \(M\) are other blocks of the near-parallel class.

Call the resulting map \(H_0\).

### Lemma PX116 -- PROVED

The map \(H_0\) is strong complete, contains \(F_0\cup\{e\}\), and differs from
\(L_c\) on a union of at most four pairwise disjoint affine-square blocks.

### Proof

Every step is an available PX98 trade.  Completion to \(L_c\) is PX106.  The
trade on \(U\) restores all source bridge values on \(U\).  A conditioned row
inside \(W\setminus U\) already has its source value \(L_c(y)\).  A conditioned
row in \(U\), including the centre \(c\), is restored by the \(U\)-trade.  A
conditioned row outside \(W\) lies in its unique restoration block \(B_y\), on
which the \(L_c\)-trade recovers \(F\).  The target row lies in
\(W\setminus U\), so it retains \(L_c(x)\).

There is one support \(U\), at most two forced restoration blocks, and one extra
marker.  They are disjoint, proving the structural assertion. \(\square\)

## 2. Final target exits

Choose an affine-square block \(R\) of the \(L_c\)-root design satisfying:

1. \(x\in R\);
2. \(R\) is disjoint from all restoration and marker supports used in
   PX116;
3. \(R\) avoids every conditioned row.

Then \(H_0=L_c\) on \(R\), so the root trade on \(R\) is available.  Let
\(H_R\) be the endpoint.

## Theorem PX117 -- PROVED

There are at least

\[
\boxed{p-55}
\]

admissible final supports \(R\).  Every endpoint \(H_R\):

1. is strong complete;
2. contains \(F_0\);
3. omits the target edge \(e\);
4. is connected to \(G\) by a PX98 path of length at most
   \((p-1)/4+4\).

Distinct choices of \(R\) give distinct endpoints.

### Proof

The \(L_c\)-design has \(p-1\) blocks through \(x\).  The at most four disjoint
supports in PX116 contain at most sixteen rows.  By the pair multiplicity three
of PX104, at most

\[
3\cdot16=48
\]

blocks through \(x\) meet their union.  The at most two conditioned rows exclude
at most six more blocks.  Hence at least

\[
p-1-48-6=p-55
\]

remain.

On one such support, the final trade preserves every restoration block and every
conditioned row.  It contains \(x\), so it changes \(L_c(x)=G(x)\) and removes
\(e\).  The path-length bound counts one bridge reversal, \((p-1)/4-2\)
near-class completion moves, at most four restorations/markers, and the final
trade.  Distinct final supports produce distinct changed row sets relative to
\(H_0\). \(\square\)

## 3. Constant terminal congestion

Every endpoint differs from the uniquely determined affine map \(L_c\) on at
most five disjoint four-row blocks, hence on at most twenty rows.

### Theorem PX118 -- PROVED

Fix \((F_0,e)\).  For \(p\ge61\), one endpoint can arise from fewer than

\[
\boxed{2^{26}}
\]

paths of Theorem PX117.

Thus the unit path bank has source outflow at least \(p-55\) and absolute
terminal congestion.

### Proof

Two affine maps which are each at Hamming distance at most twenty from the same
endpoint agree on at least

\[
p-40\ge21
\]

rows, and therefore are equal.  Hence \(L_c\) is unique.

Relative to \(L_c\), the changed set has at most twenty rows and is partitioned
into at most five four-row affine-square supports, one labelled as the final
support.  The number of possible support partitions and labels is less than

\[
2^{20}\cdot32=2^{25},
\]

and allowing the bridge orientation gives the stated \(2^{26}\) bound.  Once a
candidate decomposition is fixed, the parent centre \(c\), root \(F\), parent
blocks, bridge support, restorations, and deterministic marker are all fixed.
\(\square\)

The constants are crude but independent of \(p\).

## 4. Revised bridge-core boundary

PX117 resolves every altered edge outside the active four-row bridge support
\(U\), under arbitrary rank-at-most-two conditioning.  Together with PX110 it
also resolves every affine-exterior edge.

The only unresolved edges of the one-bridge state are now the four source edges
on \(U\).  Those form an exact one-square shell relative to \(L_c\), but outside
\(U\) the source uses both \(L_c\) and \(F\).  A final theorem must combine the
PX115 shell flow with restoration of at most two exterior source edges.

## 5. Verification

Run

```bash
python scripts/verify_product_frozen_bridge_core_flow.py
```

The verifier constructs representative flows at primes \(61,73,89\), covers
conditioned rows in every one of the three source regions \(U\),
\(W\setminus U\), and the affine exterior, and checks the \(p-55\) exit bound.
