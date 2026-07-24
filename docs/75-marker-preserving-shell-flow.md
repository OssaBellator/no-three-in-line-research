# Marker-preserving global flow out of the affine first shell

PX105 shows that a one-trade descendant has only one one-step move touching its
original four-row support.  PX108 supplies three direct two-step bridge paths
for each support row, but this is still below the \(\Omega(p)\) source scale
required by PX100.

The quartic near-resolution PX106 gives a global escape.  Complete almost the
entire near-parallel class to the opposite affine root, while leaving a bounded
number of marker blocks untoggled.  The markers preserve conditioned edges and
record the original centre.  A final opposite-root square then changes the
target edge in linearly many ways with constant reverse multiplicity.

Let \(p\equiv1\pmod4\) be prime, \(p\ge53\), choose \(i^2=-1\), and let

\[
F(x)=ix+b.
\]

Fix a centre \(c\) and one block

\[
S\in\mathcal P_c
\]

from the PX106 near-parallel class.  Let \(G_S\) be the one-trade descendant of
\(F\) on \(S\).  Put

\[
L_c(x)=-ix+b+2ic.
\]

Then \(G_S=L_c\) on \(S\), \(G_S=F\) off \(S\), and

\[
F(c)=L_c(c).
\]

Fix a target row \(x\in S\) and the source edge

\[
e=(x,G_S(x))=(x,L_c(x)).
\]

Let \(F_0\) be any partial matching of size at most two, compatible with \(e\),
and contained in \(G_S\).

## 1. Marker selection

For every conditioned row \(y\notin S\cup\{c\}\), let \(B_y\in\mathcal P_c\)
be the unique near-parallel block containing \(y\).  Leave every distinct
\(B_y\) untoggled.  Also choose one additional marker block

\[
M\in\mathcal P_c
\]

which is different from \(S\) and all the forced blocks \(B_y\).  Choose \(M\)
by any fixed deterministic ordering of the class.

Let \(\mathcal M\) be the resulting marker family.  Since \(|F_0|\le2\),

\[
\boxed{1\le|\mathcal M|\le3.}
\]

Starting from \(G_S\), apply the commuting root-square trades on every block of

\[
\mathcal P_c\setminus(\{S\}\cup\mathcal M).
\]

Call the resulting map \(H_0\).

### Lemma PX113 -- PROVED

The map \(H_0\) is strong complete and satisfies:

1. \(H_0=L_c\) outside the marker blocks;
2. \(H_0=F\) on every marker block;
3. \(F_0\subseteq\operatorname{graph}(H_0)\);
4. \(e\in\operatorname{graph}(H_0)\).

### Proof

PX106a allows every subfamily of one near-parallel class to be toggled
independently.  Toggling the complete class would give \(L_c\).  The blocks in
\(\mathcal M\) are precisely those omitted from that completion, so they retain
\(F\), while \(S\) already had the \(L_c\)-values in the source.

A conditioned row in \(S\) retains its source value because \(S\) is untouched.
The centre \(c\) is omitted by every class block and has the same value under
\(F\) and \(L_c\).  Every other conditioned row lies in its forced marker block
and retains its source value \(F(y)\).  Finally \(x\in S\), so its value remains
\(L_c(x)\). \(\square\)

## 2. Linear final-exit bank

Let \(\mathcal B_{-i}\) denote the affine-square design belonging to the
opposite root \(L_c\).  Choose a block \(R\in\mathcal B_{-i}\) satisfying:

1. \(x\in R\);
2. \(R\) is disjoint from every marker block in \(\mathcal M\);
3. \(R\) avoids the rows of \(F_0\);
4. \(R\ne S\).

Since \(H_0=L_c\) on \(R\), the opposite-root PX98 trade on \(R\) is available.
Let \(H_R\) be the resulting endpoint.

## Theorem PX114 -- PROVED

For every source datum \((G_S,F_0,e)\) above, there are at least

\[
\boxed{p-44}
\]

admissible choices of \(R\).  Every endpoint \(H_R\):

1. is a strong complete mapping;
2. contains every edge of \(F_0\);
3. does not contain \(e\);
4. is connected to \(G_S\) by a PX98 path of length at most
   \((p-1)/4+1\).

Distinct choices of \(R\) give distinct endpoints.

### Proof

There are exactly \(p-1\) opposite-root affine squares through \(x\).  One
marker block has four rows, and each pair consisting of \(x\) and one marker
row lies in exactly three blocks by PX104.  Thus one marker excludes at most
\(12\) blocks through \(x\).  Since \(|\mathcal M|\le3\), all markers exclude at
most \(36\).

Each of the at most two conditioned rows excludes at most three further blocks
through \(x\), giving at most six.  Excluding \(S\) removes one more.  Therefore
at least

\[
p-1-36-6-1=p-44
\]

choices remain.

The final trade is supported away from the marker blocks and conditioned rows,
so it preserves \(F_0\).  It contains \(x\), hence changes \(L_c(x)=G_S(x)\)
and removes \(e\).  Every step is a PX98 trade, and the near-parallel toggles
commute.  Different supports \(R\) change different four-row sets relative to
\(H_0\), so the endpoints are distinct. \(\square\)

## 3. Constant reverse multiplicity

The terminal mappings have bounded structural complexity relative to one
affine root.  Namely,

\[
\{y:H_R(y)\ne L_c(y)\}
\]

is the disjoint union of at most three marker blocks and the final block \(R\),
so it has at most sixteen rows.

### Theorem PX115 -- PROVED

Fix \((F_0,e)\).  For \(p\ge53\), one endpoint mapping can arise from at most

\[
\boxed{2^{20}}
\]

marker-preserving shell paths of Theorem PX114.

Consequently the unit-weight path bank has source outflow at least \(p-44\) and
terminal congestion bounded by an absolute constant.

### Proof

Suppose an endpoint \(H\) has one representation from the construction.  It
agrees with the opposite affine root \(L_c\) outside at most sixteen rows.  If
it also agreed outside sixteen rows with another affine map \(L'\), then
\(L_c\) and \(L'\) would agree on at least

\[
p-32\ge21
\]

rows.  Distinct affine maps agree on at most one row, so \(L_c=L'\).  Thus the
opposite affine root is uniquely determined by \(H\).

The changed row set relative to this root has size at most sixteen.  Every
candidate representation partitions a subset of this set into at most four
four-row affine-square blocks and labels one block as the final support.  The
number of set partitions and labels is smaller than \(2^{16}\cdot16<2^{20}\).
Once those blocks are specified, their common marker centre gives \(c\), the
source root \(F\) is determined by \(L_c\) and \(c\), and \(S\) is the unique
block of \(\mathcal P_c\) containing the target row \(x\).  Hence every
candidate decomposition gives at most one source path. \(\square\)

The constant is deliberately crude.  Its independence of \(p\) is the point.

## 4. Switching-flow consequence

PX114--PX115 meet the exact scale required by PX100 for every one-trade shell
source, under every rank-at-most-two conditioning:

\[
L\ge p-44,
\qquad
U\le2^{20}.
\]

This does not yet prove the full PX100 hypothesis, because mappings in deeper
nonlinear layers also require outgoing flows.  It removes the affine-shell
exception completely: neither conditioned centre edges nor conditioned
co-support edges can trap the flow.

The remaining problem begins after the source differs from every affine root on
more than one square block.  PX109 and PX112 give the first two exact nonlinear
shells; the next target is a marker-preserving flow for a general bounded-size
nonlinear core.

## 5. Verification

Run

```bash
python scripts/verify_product_marker_preserving_shell_flow.py
```

The verifier constructs the bank at primes \(53,61,73\), checks representative
rank-zero, rank-one, and rank-two conditioning patterns, verifies every endpoint
is strong complete and preserves the conditions, and confirms the \(p-44\)
exit bound.
