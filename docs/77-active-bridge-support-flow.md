# Flow for the active bridge support and the restoration-overlap exception

PX117 resolves the five frozen rows of a one-bridge nonlinear core.  This
chapter treats target edges on the active bridge support itself.

The construction uses two successive near-resolution completions.  The first
turns the bridge source into a one-square shell relative to an opposite affine
root.  The second turns that shell into a new global affine root.  Conditioned
source edges are then restored by at most two uniquely decoded root-square
trades.

Let \(p\equiv1\pmod4\) be prime with \(p\ge53\).  Retain the notation of PX116:

- \(F(x)=ix+b\);
- parent centre \(c\);
- adjacent parent blocks \(S,T\in\mathcal P_c\);
- bridge support \(U\);
- bridge source \(G\);
- first opposite root
  \[
  L_c(x)=-ix+b+2ic.
  \]

Let \(d\) be the centre of the affine square \(U\) in the \(L_c\)-design.  The
bridge is the \(L_c\)-root trade on \(U\).  Hence on \(U\), the source agrees
with the second affine root

\[
K(x)=ix+\beta,
\qquad
\beta=b+2ic-2id.
\]

Fix a target row \(x\in U\) and source edge

\[
e=(x,G(x))=(x,K(x)).
\]

Let \(F_0\) be any partial matching of size at most two, compatible with \(e\),
and contained in \(G\).

## 1. Two-stage affine completion

Starting from \(G\):

1. toggle every block of
   \[
   \mathcal P_c\setminus\{S,T\};
   \]
   the resulting map is the one-square \(L_c\)-descendant on \(U\);
2. in the \(L_c\) near-parallel class \(\mathcal P_d\) containing \(U\), toggle
   every block except \(U\) and one deterministic marker block \(M\).

The marker \(M\) will be chosen after the restoration supports below are known.
The resulting prefinal map equals \(K\) outside \(M\), while it retains the
\(L_c\)-values on \(M\).  The target edge remains \(e=K(x)\).

## 2. Unique restoration squares

For a conditioned row \(y\), no restoration is needed when \(y\in U\), because
the global root \(K\) already has the source value there.

For \(y\notin U\), let \(C_y\) be the unique affine-square support in the
\(K\)-root design whose root trade changes \(K(y)\) to the source value \(G(y)\).
Existence and uniqueness are PX106b.

There are two explicit forms.

### Parent-core rows

If

\[
y\in(S\cup T\cup\{c\})\setminus U,
\]

then \(G(y)=L_c(y)\), and \(C_y\) is the unique block of the near-parallel
class \(\mathcal P_d\) containing \(y\).  Two such restoration supports are
either equal or disjoint.

### Affine-exterior rows

If \(y\notin S\cup T\cup\{c\}\), then \(G(y)=F(y)\).  Put

\[
A=(d-c)(1-C_4).
\]

Then

\[
\boxed{C_y=y+A.}
\]

Indeed, \(K\) and \(F\) have the same slope \(i\), and their intercept
difference is

\[
b-\beta=2i(d-c).
\]

The unique-edge decoder gives restoration-square centre

\[
y+\frac{F(y)-K(y)}{2i}=y+d-c
\]

and radius \(c-d\), which is exactly the displayed translate.

Merge equal restoration supports.  Call the resulting family \(\mathcal C\).
It has size at most two.

## Theorem PX119 -- PROVED

Suppose the distinct supports in \(\mathcal C\) are pairwise disjoint.  Then
one may choose the marker \(M\in\mathcal P_d\) so that

\[
M\ne U
\]

and \(M\) is disjoint from every support in \(\mathcal C\).

After the two affine completions, there are at least

\[
\boxed{p-43}
\]

blocks \(R\) of the \(K\)-root design satisfying:

1. \(x\in R\);
2. \(R\) is disjoint from \(M\) and every support in \(\mathcal C\);
3. \(R\) avoids every conditioned row.

For every such \(R\), apply the \(K\)-root trade on \(R\), followed by the
root trades on the supports in \(\mathcal C\).  The endpoint is strong complete,
contains \(F_0\), and omits \(e\).

### Proof

The class \(\mathcal P_d\) partitions all rows except \(d\).  Each restoration
support has four rows and therefore meets at most four blocks of this class.
At most eight class blocks are excluded by \(\mathcal C\), and \(U\) excludes
one more.  Since \((p-1)/4\ge13\), an admissible marker exists.

There are \(p-1\) \(K\)-root squares through \(x\).  The marker and at most two
restoration supports contain at most twelve rows, excluding at most

\[
3\cdot12=36
\]

blocks through \(x\).  The at most two conditioned rows exclude at most six
more.  Hence at least

\[
p-1-36-6=p-43
\]

choices remain.

Before the final operations, the map equals \(K\) away from \(M\).  The chosen
supports \(R\) and \(\mathcal C\) are pairwise disjoint and avoid \(M\), so all
of their root trades are available and commute.  The trade on \(R\) changes the
target edge.  A restoration trade gives the prescribed source value at its
conditioned row.  If a restoration support contains \(x\), it cannot restore
\(e\): by PX106b, the unique \(K\)-square which maps \(K(x)\) to \(G(x)=K(x)\)
does not exist, while every nontrivial root trade changes that value.  Thus the
target remains absent. \(\square\)

## Theorem PX120 -- PROVED

Fix \((F_0,e)\).  Under the hypotheses of PX119, one endpoint arises from at
most

\[
\boxed{2^{22}}
\]

paths of the construction.

Thus the active-support path bank has source outflow at least \(p-43\) and
absolute terminal congestion whenever the restoration supports are pairwise
disjoint.

### Proof

The endpoint differs from the global affine root \(K\) on at most four disjoint
four-row blocks: the marker, final support, and at most two restorations.  Hence
it differs on at most sixteen rows.  As in PX115, \(K\) is the unique affine
map within distance sixteen for \(p\ge53\).

The changed set has at most \(2^{16}\) candidate support partitions and fewer
than \(64\) choices of labels and bridge orientation.  Once these data are
fixed, the centres \(d,c\), roots \(K,L_c,F\), parent blocks, bridge support,
marker, and restorations are fixed.  The product is below \(2^{22}\).
\(\square\)

## 3. Exact exceptional-pair geometry

The disjointness hypothesis can fail only for a constant-degree set of
rank-two conditions.

### Theorem PX121 -- PROVED

For a fixed conditioned row, there are at most \(32\) second rows whose distinct
restoration support intersects its restoration support.

More precisely:

1. two parent-core restoration supports are equal or disjoint;
2. for two affine-exterior rows \(y,z\),
   \[
   C_y\cap C_z\ne\varnothing
   \quad\Longrightarrow\quad
   z-y\in A-A,
   \]
   giving at most \(|A-A|-1\le15\) nonzero differences;
3. for one parent-core support \(B\in\mathcal P_d\) and one exterior row \(y\),
   \[
   C_y\cap B\ne\varnothing
   \quad\Longrightarrow\quad
   y\in B-A,
   \]
   giving at most sixteen exterior rows.

Thus the unresolved rank-two conditioning graph has maximum degree at most
\(32\).

### Proof

The first statement is the partition property of \(\mathcal P_d\).  The second
uses \(C_y=y+A\): an intersection gives

\[
y+a=z+a'
\]

for some \(a,a'\in A\), hence \(z-y=a-a'\).  The third follows similarly from
\(y+a\in B\).  The crude union of the two possible exception types is at most
\(15+16<32\). \(\square\)

## 4. Revised one-bridge boundary

PX117 resolves every frozen bridge-core edge.  PX119 resolves every active
bridge-support edge except when two conditioned rows have distinct,
non-disjoint restoration squares.  PX121 shows that this is a bounded-degree
rank-two exception, not a growing geometric sector.

The next exact target is a two-restoration composite trade for those intersecting
support pairs.  Proving it would complete the PX100-scale flow for every edge
of every one-bridge state.

## 5. Verification

Run

```bash
python scripts/verify_product_active_bridge_support_flow.py
```

The verifier constructs the two-stage completion at primes \(53,61,73\), checks
all one-condition cases and every disjoint two-restoration case, reproduces the
\(p-43\) exit bound, and verifies the translate formulas and degree-32 exception
bound.
