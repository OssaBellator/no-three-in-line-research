# Complete switching flow for every one-bridge state

PX117 resolves the five frozen rows of a one-bridge nonlinear core.  PX124
resolves the four active bridge-support rows under every rank-at-most-two
condition.  The affine exterior admits a simpler direct flow, completing the
PX100-scale switching theorem for the whole one-bridge family.

Let \(p\equiv1\pmod4\) be prime, choose \(i^2=-1\), and let

\[
F(x)=ix+b.
\]

Construct a one-bridge state \(G\) from adjacent parent squares and one PX108
bridge.  Put

\[
W=\{x:G(x)\ne F(x)\}.
\]

Then \(|W|=9\).

## 1. Direct affine-exterior flow

Fix a target row

\[
x\notin W
\]

and target edge

\[
e=(x,G(x))=(x,F(x)).
\]

Let \(F_0\subseteq\operatorname{graph}(G)\) be a compatible partial matching of
size at most two.

Choose an affine-square block \(R\) from the \(F\)-root design satisfying

\[
x\in R,
\qquad
R\cap W=\varnothing,
\]

and avoiding every conditioned row.  Since \(G=F\) on \(R\), the PX98 root
trade on \(R\) is available.

## Theorem PX126 -- PROVED

There are at least

\[
\boxed{p-34}
\]

admissible choices of \(R\).  Every resulting endpoint:

1. is strong complete;
2. contains \(F_0\);
3. omits the target edge \(e\);
4. is joined to \(G\) by one PX98 trade.

Distinct supports give distinct endpoints.

### Proof

There are exactly \(p-1\) affine squares through \(x\).  For each of the nine
rows of \(W\), exactly three blocks contain the pair with \(x\), so at most
\(27\) blocks through \(x\) meet the nonlinear core.  The at most two
conditioned rows exclude at most six further blocks.  Hence at least

\[
p-1-27-6=p-34
\]

remain.

The trade support avoids both the changed core and every conditioned row, so it
preserves \(F_0\), while containing \(x\) and changing its image. \(\square\)

## Theorem PX127 -- PROVED

Fix \((F_0,e)\).  One endpoint of the PX126 bank has fewer than

\[
\boxed{2^{60}}
\]

one-bridge predecessors and support labels.  Thus the unit path bank has source
outflow at least \(p-34\) and absolute terminal congestion.

### Proof

An endpoint differs from \(F\) on the nine-row bridge core and the disjoint
four-row final square, hence on at most thirteen rows.  If it were within
thirteen rows of two affine maps, those maps would agree on at least

\[
p-26
\]

rows.  For \(p\ge29\), this is more than one, so the affine root \(F\) is
unique.

Relative to this root, all source and final data live on at most thirteen rows.
The final support is one four-subset, the bridge core is one nine-subset, and
the parent/bridge orientation has only boundedly many labels.  Encoding all
subsets and labels uses fewer than sixty bits, giving the stated bound.
\(\square\)

Again the numerical constant is intentionally crude.

## 2. Complete one-bridge flow theorem

### Theorem PX128 -- PROVED

Let \(p\equiv1\pmod4\) be prime with \(p\ge149\).  Let \(G\) be any one-bridge
state obtained from an affine strong complete mapping by two adjacent root
squares and one PX108 bridge.

For every partial matching \(F_0\subseteq\operatorname{graph}(G)\) of size at
most two and every compatible edge

\[
e\in\operatorname{graph}(G)\setminus F_0,
\]

there is a PX98 path flow from mappings containing \(F_0\cup\{e\}\) to mappings
containing \(F_0\) but not \(e\), with

\[
\boxed{L\ge p-142}
\]

and

\[
\boxed{U\le2^{700}}.
\]

The paths have length at most \((p-1)/2+1\).

### Proof

Classify the row of \(e\).

1. **Affine exterior.** Apply PX126--PX127.  Here
   \[
   L\ge p-34,
   \qquad
   U<2^{60}.
   \]
2. **Frozen bridge core \(W\setminus U\).** Apply PX117--PX118.  Here
   \[
   L\ge p-55,
   \qquad
   U<2^{26}.
   \]
3. **Active bridge support \(U\).** Apply PX124--PX125.  Here
   \[
   L\ge p-142,
   \qquad
   U<2^{700}.
   \]

The last case dominates both constants and the path-length bound. \(\square\)

PX128 is the first nontrivial infinite switching family for which the complete
rank-zero, rank-one, and rank-two PX100 source-flow requirement is proved.

## 3. What PX128 does and does not finish

PX128 does not yet prove rank-three spread on all strong complete mappings.  It
covers one explicit nonlinear shell family, not every source in a candidate
measure.  Its significance is that every apparent obstruction inside that
family has now been removed:

- the one-step shell reversal bottleneck;
- the five frozen bridge rows;
- the active bridge support;
- intersecting rank-two restoration squares;
- the affine exterior;
- arbitrary rank-at-most-two conditions.

The next route is to construct a probability measure or layered switching flow
supported on affine roots, one-shell states, and one-bridge states, and check
whether PX103, PX115, and PX128 can be balanced to give the conditional edge
ratios in PX100.  PX101 still requires later layers to rewrite almost all rows,
but the first nonlinear expansion stage is now complete.

## 4. Verification

Run

```bash
python scripts/verify_product_complete_one_bridge_flow.py
```

The verifier checks the affine-exterior bank at primes \(37,53,149\), combines
its bounds with the frozen- and active-core verifiers, and checks the case
partition for every row of representative one-bridge states.
