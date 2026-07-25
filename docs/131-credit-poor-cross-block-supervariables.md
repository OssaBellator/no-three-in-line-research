# Credit-poor cross-block supervariables

PP3qg identifies the exact credit-poor homogeneous signature: state pair
\((1,1)\) is forbidden, while the all-line state is geometrically valid but
directly recaptures the designated owner credits.  This is a limitation of the
two original rectangle diagonals, not of the four endpoint resources.

Pair two resource-disjoint rectangles and use only the cross-block cells mapping
the columns of each rectangle to the rows of the other.  These states avoid both
original rectangle diagonals and give a four-state equal-margin supervariable.

## 1. Four cross-block perfect matchings

Let rectangle \(s\) use left resources

\[
 L_s=\{x_s^0,x_s^1\}
\]

and right resources

\[
 R_s=\{y_s^0,y_s^1\}.
\]

Let rectangle \(t\) have disjoint resource pairs \(L_t,R_t\).

A **cross-block state** is the union of:

- one perfect matching from \(L_s\) to \(R_t\);
- one perfect matching from \(L_t\) to \(R_s\).

### Proposition PP3qs -- PROVED

The paired resource block has exactly

\[
 2!\,2!=4
\]

cross-block states.  Every state is a perfect matching on

\[
 L_s\cup L_t
 \quad\text{and}\quad
 R_s\cup R_t.
\]

No selected cell belongs to either original rectangle support

\[
 L_s\times R_s
 \quad\text{or}\quad
 L_t\times R_t.
\]

#### Proof

Choose either of the two bijections \(L_s\to R_t\) and independently either of
the two bijections \(L_t\to R_s\).  Their union covers every one of the four left
and four right resources exactly once.  Every chosen cell lies in one of the two
off-diagonal resource blocks. ∎

Thus the common obstruction line and the original line-state recapture cells are
both left behind.

## 2. Guaranteed designated-credit preservation

Each original rectangle has one distinguished owner column, coming from the
removed endpoint \(r_s\) or \(r_t\), and one unchanged designated blocker endpoint
\(s_s\) or \(s_t\).  Direct recapture of owner \(s\)'s credit occurs only when the
new cell in its owner column lies on the nonaxis line

\[
 \overline{z_ss_s}.
\]

### Proposition PP3qt -- PROVED

Among the four cross-block states, at least one directly preserves both
designated owner credit units.

#### Proof

The owner column of rectangle \(s\) is matched to one of the two rows in \(R_t\).
Because the designated recapture line is nonhorizontal, it meets those two rows
in at most one cell in that fixed owner column.  Therefore at least one of the
two row choices does not directly recapture owner \(s\)'s credit.  Once that row
is chosen, the other column of \(L_s\) is forced to the remaining row of \(R_t\).

The same argument independently chooses a nonrecapturing image for the owner
column of rectangle \(t\) inside \(R_s\).  Combining the two forced bijections
gives one of the four cross-block states and protects both designated units. ∎

The state may still create unrelated unary or binary shadow; that is paid
collateral rather than direct loss of the two designated credits.

## 3. Exact source-safe cross-block host

Delete from the two cross blocks every cell that is unavailable because of:

- collision with the fixed configuration;
- a secant through two fixed points;
- direct designated recapture for either owner;
- any other unary restriction imposed before the multistate selection.

Let

\[
 H_{s\to t}\subseteq L_s\times R_t,
 \qquad
 H_{t\to s}\subseteq L_t\times R_s
\]

be the two resulting \(2\)-by-\(2\) bipartite graphs.

### Proposition PP3qu -- PROVED

A source-safe credit-preserving cross-block state exists if and only if both
\(H_{s\to t}\) and \(H_{t\to s}\) contain perfect matchings.

Failure in either direction is an exact \(2\)-by-\(2\) Hall obstruction.

#### Proof

A cross-block state is exactly one perfect matching in each direction, and the
two directions use disjoint resources.  Hence the choices are independent and
exist precisely when both small hosts are matchable.  Hall's theorem is exact on
each host. ∎

For a \(2\)-by-\(2\) host, failure means one left vertex is isolated or both left
vertices have the same singleton neighbourhood; the transposed statement is
equivalent.

## 4. Linear bank of four-state supervariables

Let a credit-poor homogeneous rectangle subbank have size \(h\to\infty\).
Pair its variables arbitrarily, discarding at most one rectangle.

### Theorem PP3qv -- PROVED

The paired bank contains

\[
 \left\lfloor\frac h2\right\rfloor
\]

resource-disjoint supervariables.  Every supervariable has at most four
cross-block states and at least one credit-preserving state before source-safety
pruning.  If both \(2\)-by-\(2\) safe hosts are matchable, its nonempty safe state
set consists entirely of equal-margin perfect matchings and every state moves
both distinguished owner endpoints.

#### Proof

Original rectangle supports are resource-disjoint, so disjoint rectangle pairs
remain resource-disjoint.  Apply PP3qs--PP3qu to each pair.  Every cross-block
cell maps a column of one rectangle to a row resource of the other rectangle,
which is disjoint from the original owner row; hence both owner endpoints move.
All states use every local left and right resource once. ∎

The designated owner removal credit of a safe supervariable is therefore at
least two.

## 5. Exact multistate geometry and cost

Fix a source-valid residual matching and retain, for every paired block, its
nonempty set of safe cross-block states.

### Corollary PP3qw -- PROVED

The paired bank is an equal-margin finite-state system of the type PP3bh.

- Every collinear triple gives an exact bad box involving at most three
  supervariables.
- Exact controller-shadow insertion cost is a pseudo-Boolean finite-state cost
  involving at most two supervariables.
- Every assignment preserves all endpoint row and column margins.

#### Proof

Distinct supervariable supports are resource-disjoint and every local state is a
perfect matching on the same four-by-four resource block.  Apply PP3bh--PP3bi.
A triple meets at most three supports, while a blocker pair uses at most two
selected supports. ∎

Thus the credit-poor Boolean clique has been converted into a four-state
multistate bank with two units of designated credit per variable.

## 6. Paid multistate completion interface

### Corollary PP3qx -- PROVED

Suppose a linear fraction of the paired blocks have nonempty safe state sets.  A
strict source-admissible improvement follows from either of the standard
multistate criteria:

1. the product-state bad-box probability plus normalized expected insertion cost
   is below one;
2. the variable bad-box mass satisfies a local-lemma criterion and the
   conditioned expected insertion cost is below the two-per-block removal
   credit.

#### Proof

Saturation and exact bad boxes are PP3qw.  Apply PP3bj or PP3bk together with the
same integer-plus-normalized-cost argument as PP3oy.  The removal credit lower
bound is PP3qv. ∎

## 7. Revised credit-poor endpoint

### Corollary PP3qy -- PROVED

A credit-poor homogeneous two-state rectangle signature is not terminal.  After
pairing rectangles, at least one of the following holds.

1. A linear four-state cross-block bank survives source-safe pruning and meets a
   paid multistate selection criterion.
2. A linear number of rectangle pairs contain an exact \(2\)-by-\(2\) unary Hall
   obstruction in one cross direction.
3. Safe cross-block states exist, but their rank-at-most-three bad-box mass or
   unary/binary insertion cost is concentrated at the two-credit-per-block
   scale.

The remaining credit-poor problem is therefore a finite cross-block host
obstruction or a multistate geometric/cost concentration.  The original
pairwise-incompatible Boolean signature has been bypassed.