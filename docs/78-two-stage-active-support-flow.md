# Unconditional two-stage flow for active bridge-support edges

PX119 gives a linear marker flow for an active bridge-support edge except when
two conditioned restoration squares overlap.  This chapter removes that
exception by preserving the conditioned source values before the second affine
completion, rather than restoring them afterwards.

The cost is only a larger fixed marker region.  The resulting flow works under
every rank-at-most-two condition.

Let \(p\equiv1\pmod4\) be prime with \(p\ge149\).  Retain the one-bridge notation:

- \(F(x)=ix+b\), with \(i^2=-1\);
- parent centre \(c\) and adjacent parent blocks \(S,T\in\mathcal P_c\);
- first opposite root
  \[
  L_c(x)=-ix+b+2ic;
  \]
- bridge support \(U\), with centre \(d\) in the \(L_c\)-design;
- second affine root
  \[
  K(x)=ix+b+2ic-2id;
  \]
- bridge source \(G\).

Thus

\[
G=
\begin{cases}
K,&\text{on }U,\\
L_c,&\text{on }(S\cup T\cup\{c\})\setminus U,\\
F,&\text{elsewhere}.
\end{cases}
\]

Fix a target row \(x\in U\), the active source edge

\[
e=(x,K(x)),
\]

and a compatible partial matching \(F_0\subseteq\operatorname{graph}(G)\) of
size at most two.

## 1. First-stage source markers

For every conditioned row \(y\) in the affine exterior

\[
y\notin S\cup T\cup\{c\},
\]

let \(E_y\in\mathcal P_c\) be the unique parent near-class block containing
\(y\).  Merge repeated blocks and call the resulting family \(\mathcal E\).
It has size at most two.

Starting from \(G\), apply the commuting \(F\)-root trades on every block of

\[
\mathcal P_c\setminus
\bigl(\{S,T\}\cup\mathcal E\bigr).
\]

Call the result \(H_1\).

### Lemma PX122 -- PROVED

The map \(H_1\) is strong complete and has the form

\[
H_1=
\begin{cases}
K,&\text{on }U,\\
F,&\text{on every block in }\mathcal E,\\
L_c,&\text{everywhere else except possibly the common centre }c.
\end{cases}
\]

Every conditioned source edge in the affine exterior is preserved.

### Proof

All toggled blocks are disjoint members of \(\mathcal P_c\), and they are
disjoint from \(S,T,U\).  PX106 therefore allows the trades to be applied in
any order.  Completing the whole class would give \(L_c\); omitting the blocks
in \(\mathcal E\) leaves their original \(F\)-values.  The bridge support is
untouched and retains \(K\). \(\square\)

## 2. Second-stage protection

Let \(\mathcal P_d\) be the \(L_c\) near-parallel class containing \(U\).  Form
a protected block family \(\mathcal D\) as follows.

1. Include \(U\).
2. Include every block of \(\mathcal P_d\) which meets a member of
   \(\mathcal E\).
3. For every conditioned row in the frozen parent core
   \[
   (S\cup T\cup\{c\})\setminus U,
   \]
   include its unique block of \(\mathcal P_d\).
4. Add one further deterministic marker block \(M\in\mathcal P_d\) not already
   included.

Each member of \(\mathcal E\) has four rows and therefore meets at most four
blocks of the partition \(\mathcal P_d\).  Hence

\[
\boxed{|\mathcal D|\le12.}
\]

The class has \((p-1)/4\ge37\) blocks, so the extra marker always exists.

Starting from \(H_1\), apply the \(L_c\)-root trade on every block of

\[
\mathcal P_d\setminus\mathcal D.
\]

Call the result \(H_2\).

## Theorem PX123 -- PROVED

The map \(H_2\) is strong complete, contains \(F_0\cup\{e\}\), and agrees with
\(K\) outside a set \(Z\) of at most forty-five rows.

More precisely:

- the rows where \(H_2\ne K\) lie in the at most eleven protected class blocks
  \(\mathcal D\setminus\{U\}\), together with possibly the omitted centre
  \(d\);
- every conditioned exterior row retains its \(F\)-value;
- every conditioned frozen-core row retains its \(L_c\)-value;
- every conditioned row in \(U\), and the target row \(x\), retain their
  \(K\)-values.

### Proof

Relative to \(L_c\), the map \(H_1\) differs only on the pairwise disjoint
supports \(U\) and the blocks of \(\mathcal E\).  A block of
\(\mathcal P_d\setminus\mathcal D\) is disjoint from all these supports, so
\(H_1=L_c\) on it and the \(L_c\)-root trade is available.  The toggled blocks
are pairwise disjoint, hence the resulting map is strong complete.

Every unprotected class block is changed from \(L_c\) to \(K\).  The block
\(U\) already has \(K\)-values.  Thus disagreement with \(K\) is confined to
\(\mathcal D\setminus\{U\}\), containing at most \(44\) rows, and possibly the
class centre \(d\), which no block moves.

An exterior condition lies in one of the first-stage marker blocks
\(E_y\).  Every second-stage block meeting \(E_y\) is protected, so its
\(F\)-value survives.  A frozen-core condition has its own protected
\(\mathcal P_d\)-block and retains \(L_c\).  Conditions and the target in
\(U\) retain \(K\). \(\square\)

A useful exact identity is

\[
U-(d-c)(1-C_4)=S\cup T\cup\{c\}.
\]

It implies that no exterior source marker can force a restoration square
through the target row; this is the target-disjointness observed in PX119.

## 3. Final target trade

Choose a block \(R\) of the \(K\)-root affine-square design satisfying

\[
x\in R,
\qquad
R\cap Z=\varnothing,
\]

and avoiding every conditioned row.  Since \(H_2=K\) on \(R\), its root trade
is available.

## Theorem PX124 -- PROVED

There are at least

\[
\boxed{p-142}
\]

admissible choices of \(R\).  Each endpoint \(H_R\):

1. is a strong complete mapping;
2. contains every edge of \(F_0\);
3. omits the target edge \(e\);
4. is joined to the bridge source by a PX98 path of length at most
   \((p-1)/2+1\).

Distinct final supports give distinct endpoints.

### Proof

There are \(p-1\) \(K\)-root squares through \(x\).  The bad set \(Z\) has at
most \(45\) rows, and each pair consisting of \(x\) and one bad row belongs to
three design blocks.  Hence at most \(135\) blocks through \(x\) meet \(Z\).
At most two conditioned rows exclude at most six more blocks.  Therefore at
least

\[
p-1-135-6=p-142
\]

choices remain.

The root trade on one such block changes the value at \(x\) and is disjoint
from every bad or conditioned row, so it preserves \(F_0\).  The two completion
stages use at most \((p-1)/2\) commuting trades in total. \(\square\)

## 4. Absolute terminal congestion

Every endpoint differs from the global affine root \(K\) on at most

\[
45+4=49
\]

rows.

### Theorem PX125 -- PROVED

Fix \((F_0,e)\).  One endpoint of the PX124 bank arises from at most

\[
\boxed{2^{700}}
\]

source paths.  Thus the unit-weight bank has

\[
L\ge p-142,
\qquad
U\le2^{700}.
\]

### Proof

For \(p\ge149\), two affine maps each within Hamming distance \(49\) of one
endpoint agree on at least \(p-98>1\) rows and therefore are equal.  Hence the
global root \(K\) is uniquely determined.

The extra marker \(M\) is a complete four-row \(K\)-root trade and records the
centre \(d\).  The target row \(x\) then determines the unique block \(U\) of
\(\mathcal P_d\) containing it.  There are only four bridge orientations for
recovering the parent centre and the source roots.

All remaining support data involve at most thirteen labelled four-row sets in
a universe of at most forty-nine affected rows.  A crude encoding which lists
each support as an arbitrary four-subset, followed by its role label and bridge
orientation, uses fewer than \(700\) binary choices.  Therefore the number of
source-path decompositions is below \(2^{700}\). \(\square\)

No attempt is made to optimize this constant; only independence from \(p\)
matters for PX100.

## 5. Completion of the one-bridge active sector

PX124 removes the restoration-overlap exception in PX121.  Every active
bridge-support edge now has the required linear-outflow, constant-congestion
path bank under every rank-at-most-two condition.

Together with PX117, all nine nonlinear-core edges of a one-bridge state are
resolved.  The affine-exterior sector still has the one-step source count
PX110; a corresponding marker flow with constant reverse congestion is the
last step needed for a full one-bridge PX100 theorem.

## 6. Verification

Run

```bash
python scripts/verify_product_two_stage_active_flow.py
```

The verifier exhausts representative condition types at primes
\(149,157,173\), checks both completion stages exactly, verifies all source
conditions and every final target trade, and reproduces the \(p-142\) bound.
