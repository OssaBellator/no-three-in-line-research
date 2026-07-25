# Homogeneous-signature paid capacity

PP3pi produces a growing rectangle subbank on which every ordered variable pair
has the same binary signature

\[
 \Sigma\subseteq\{0,1\}^2.
\]

The preferred cross state is state one.  This chapter classifies every valid
state sequence for a homogeneous signature and computes the maximum number of
credit-preserving cross states it can contain.

## 1. Ordered homogeneous constraints

Let the variables be ordered

\[
 1<2<\cdots<h.
\]

A state sequence

\[
 x=(x_1,\ldots,x_h)\in\{0,1\}^h
\]

is valid exactly when

\[
 (x_s,x_t)\notin\Sigma
 \qquad(s<t).
\]

### Proposition PP3qd -- PROVED

The four possible forbidden ordered pairs have the following exact effects.

1. If \((0,0)\in\Sigma\), every valid sequence contains at most one zero.
2. If \((1,1)\in\Sigma\), every valid sequence contains at most one one.
3. If \((0,1)\in\Sigma\), no zero may occur before a one.  Every valid sequence
   is of the form
   
   \[
   1\cdots10\cdots0
   \]
   
   after ignoring any additional restrictions.
4. If \((1,0)\in\Sigma\), no one may occur before a zero.  Every valid sequence
   is of the form
   
   \[
   0\cdots01\cdots1
   \]
   
   after ignoring any additional restrictions.

#### Proof

Each statement is the direct translation of the corresponding forbidden pair
condition for ordered indices \(s<t\). ∎

This completely classifies homogeneous binary formulas because the signature is
just a subset of the four ordered pairs.

## 2. Cross-state capacity

Define

\[
 \alpha_1(\Sigma,h)
 =
 \max\left\{
 |\{s:x_s=1\}|:
 x\text{ is valid}
 \right\},
\]

with value \(-\infty\) when no valid sequence exists.

### Theorem PP3qe -- PROVED

For every homogeneous signature and every \(h\ge3\):

1. If \((1,1)\notin\Sigma\), then the all-one sequence is valid and
   
   \[
   \alpha_1(\Sigma,h)=h.
   \]
2. If \((1,1)\in\Sigma\), then
   
   \[
   \alpha_1(\Sigma,h)\le1.
   \]
3. If both diagonal pairs belong to the signature,
   
   \[
   (0,0),(1,1)\in\Sigma,
   \]
   then no valid sequence exists for \(h\ge3\).
4. If
   
   \[
   (0,0)\notin\Sigma,
   \qquad
   (1,1)\in\Sigma,
   \]
   
   then the all-zero sequence is valid, but every valid sequence preserves at
   most one cross-oriented rectangle.

#### Proof

If \((1,1)\) is allowed, every ordered pair in the all-one sequence is allowed,
proving the first statement.  If it is forbidden, PP3qd gives at most one one.
If both diagonal pairs are forbidden, a length-three binary sequence contains
two equal states by pigeonhole, so it is invalid.  The final statement combines
the allowed all-zero sequence with the at-most-one-one bound. ∎

The cross pairs \((0,1)\) and \((1,0)\) may determine where the unique one can
occur, but they cannot increase its number.

## 3. Designated-credit consequence

Use the common-line recapture rectangles and the credit inheritance PP3pn.
Every cross-oriented variable protects one distinct designated credit unit from
direct recapture.  A line-oriented state has no such guaranteed protection.

### Corollary PP3qf -- PROVED

Let \(H\) be a homogeneous ternary-free rectangle subbank of size \(h\to\infty\).

1. If \((1,1)\notin\Sigma\), there is a geometrically valid all-cross assignment
   protecting at least \(h\) designated credit units before residual collateral.
2. If \((1,1)\in\Sigma\), every geometrically valid assignment protects at most
   one designated unit by the cross-orientation mechanism.
3. If both diagonal pairs are forbidden, the homogeneous subbank is already a
   three-variable geometric contradiction.

#### Proof

Apply PP3qe and then PP3pn to every state-one variable. ∎

Thus the paid meaning of the signature is sharper than satisfiability alone.
The only homogeneous signatures capable of preserving a growing designated
credit are those allowing the pair \((1,1)\).

## 4. Exact paid-signature endpoint

### Corollary PP3qg -- PROVED

After ternary thinning and signature Ramsey regularisation, exactly one of the
following holds on a growing subbank.

1. **Credit-rich signature:** \((1,1)\notin\Sigma\).  The all-cross assignment is
   geometrically valid, directly protects one designated unit per rectangle,
   and succeeds whenever its residual insertion cost is below that linear
   credit.
2. **Credit-poor but satisfiable signature:**
   
   \[
   (0,0)\notin\Sigma,
   \qquad
   (1,1)\in\Sigma.
   \]
   
   The all-line assignment is valid, but every valid assignment has at most one
   cross-oriented rectangle.  A new geometric trade, not a different Boolean
   assignment on the same bank, is required to preserve linear credit.
3. **Local contradiction:** both diagonal pairs are forbidden, so three
   rectangles form an unsatisfiable core.

The arbitrary sixteen-signature CSP has therefore been reduced to one useful
orientation, one explicitly credit-poor orientation class, or a constant-size
contradiction.