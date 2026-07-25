# Controller-defect Ore scores

The direct global endpoint PP3gl is stated in terms of degrees of the refined
compatibility graphs \(J_i^{\rm ctrl}(\gamma)\).  This chapter bounds those
degrees explicitly by controller-cell defect counts and same-slot anchor counts.
It supplies a bridge from the dynamic excess-shadow potential to complementary
degree.

The resulting criterion is deterministic.  It does not assume that movement and
refill defects are uniformly distributed, and it retains the advantage of the
Ore endpoint: a bad movement label may be compensated by high average refill
degree.

## 1. Defect data

Fix a macro pool \(E_i\) of size \(R\), with movement and refill label sets both
of size \(T\).  Put

\[
 a_i(A)=R-|C_{i,A}^{\rm ctrl}|,
 \qquad
 b_i(B)=R-|D_{i,B}^{\rm ctrl}|.
\]

Thus \(a_i(A)\) and \(b_i(B)\) count controller edges whose movement or refill
cell is unsafe for that label.

For the same-slot anchor set, put

\[
 u_i(A,B)=|U_{i,A,B}^{\rm ctrl}|.
\]

Define the aggregate masses

\[
 A_i=\sum_A a_i(A),
 \qquad
 B_i=\sum_B b_i(B),
\]

and the anchor row and column masses

\[
 U_i(A)=\sum_B u_i(A,B),
 \qquad
 V_i(B)=\sum_A u_i(A,B).
\]

All quantities are counted with multiplicity in the label variables.  This is
intentional: degree bounds require row- and column-local mass rather than only the
number of distinct geometric witnesses.

## 2. Domain union bound

### Proposition PP3lx -- PROVED

For every macro and label pair,

\[
 \boxed{
 |H_{i,A,B}^{\rm ctrl}|
 \ge
 R-a_i(A)-b_i(B)-u_i(A,B).
 }
\]

Consequently, if

\[
 (A,B)\notin J_i^{\rm ctrl}(\gamma),
\]

then

\[
 \boxed{
 a_i(A)+b_i(B)+u_i(A,B)>(1-\gamma)R.
 }
\]

#### Proof

The complement of

\[
 C_{i,A}^{\rm ctrl}\cap D_{i,B}^{\rm ctrl}
 \setminus U_{i,A,B}^{\rm ctrl}
\]

inside \(E_i\) is contained in the union of the movement defect set, the refill
defect set, and the same-slot anchor set.  Apply the union bound.  If the right
side were at least \(\gamma R\), the pair would be an edge of the refined graph. ∎

The estimate permits overlaps among the three defect classes; those overlaps only
make the true domain larger.

## 3. Row and column nondegree bounds

For a movement label \(A\), let

\[
 \overline d_i(A)
 =
 T-\deg_{J_i^{\rm ctrl}}(A)
\]

be its refill nondegree.  For a refill label \(B\), let

\[
 \overline e_i(B)
 =
 T-|\{A:(A,B)\in J_i^{\rm ctrl}\}|.
\]

### Theorem PP3ly -- PROVED

If

\[
 a_i(A)<(1-\gamma)R,
\]

then

\[
 \boxed{
 \overline d_i(A)
 \le
 \frac{B_i+U_i(A)}{(1-\gamma)R-a_i(A)}.
 }
\]

Similarly, if

\[
 b_i(B)<(1-\gamma)R,
\]

then

\[
 \boxed{
 \overline e_i(B)
 \le
 \frac{A_i+V_i(B)}{(1-\gamma)R-b_i(B)}.
 }
\]

The right sides may be truncated at \(T\).

#### Proof

Let \(N\) be the set of refill labels missing from movement label \(A\).  Sum the
nonedge certificate PP3lx over \(B\in N\):

\[
 |N|(1-\gamma)R
 <
 |N|a_i(A)
 +
 \sum_{B\in N}b_i(B)
 +
 \sum_{B\in N}u_i(A,B).
\]

The last two sums are at most \(B_i\) and \(U_i(A)\).  Rearrange.  The column
statement is the transposed argument. ∎

These inequalities are deterministic Markov bounds with the heavy endpoint
defect retained in the denominator.

## 4. Complementary defect scores

Define

\[
 \rho_i(A)
 =
 \min\left\{
 T,
 \frac{B_i+U_i(A)}{(1-\gamma)R-a_i(A)}
 \right\},
\]

with \(\rho_i(A)=T\) when the denominator is nonpositive.  Define the average
refill score

\[
 \kappa(B)
 =
 \frac1M
 \sum_{j=1}^M
 \min\left\{
 T,
 \frac{A_j+V_j(B)}{(1-\gamma)R-b_j(B)}
 \right\},
\]

again using the value \(T\) when a denominator is nonpositive.

### Theorem PP3lz -- PROVED

Let \(h>0\).  Suppose every incompatible triple

\[
 (i,A,B),
 \qquad
 (A,B)\notin J_i^{\rm ctrl}(\gamma),
\]

satisfies

\[
 \boxed{
 \rho_i(A)+\kappa(B)
 \le
 T-h.
 }
\]

If also

\[
 T\exp\left(-\frac{h^2}{32T}\right)<1,
\]

then a balanced ownership and global refill matching exist.  Hence the complete
prime-gap-scale patch follows from PP3hq.

#### Proof

Theorem PP3ly gives

\[
 \deg_{J_i^{\rm ctrl}}(A)
 \ge
 T-\rho_i(A).
\]

For the average refill degree of PP3gl,

\[
 q_B
 =
 \frac1M\sum_j
 \bigl(T-\overline e_j(B)\bigr)
 \ge
 T-\kappa(B).
\]

Therefore every incompatible triple satisfies

\[
 \deg_{J_i^{\rm ctrl}}(A)+q_B
 \ge
 2T-\rho_i(A)-\kappa(B)
 \ge
 T+h.
\]

Apply PP3gl and then PP3hq. ∎

Taking \(h=8\sqrt{T\log T}\) gives the explicit asymptotic form.

## 5. Localized failure certificate

### Corollary PP3ma -- PROVED

If the actual complementary-degree hypothesis PP3gl fails, then there is an
incompatible triple \((i,A,B)\) satisfying

\[
 \boxed{
 \rho_i(A)+\kappa(B)>T-h.
 }
\]

Thus every direct-allocation failure contains at least one of the following
features.

1. A movement label with
   \[
   a_i(A)\ge(1-\gamma)R.
   \]
2. A refill label in some macro with
   \[
   b_j(B)\ge(1-\gamma)R.
   \]
3. Large macro-total movement or refill cell-defect mass \(A_j\) or \(B_i\).
4. Large same-slot anchor row mass \(U_i(A)\) or average column mass
   \(M^{-1}\sum_jV_j(B)\).
5. Two moderate defect scores whose complementary sum exceeds \(T-h\).

#### Proof

If PP3gl fails, some incompatible triple has

\[
 \deg_{J_i^{\rm ctrl}}(A)+q_B<T+h.
\]

The lower bounds in the proof of PP3lz force

\[
 2T-\rho_i(A)-\kappa(B)<T+h.
\]

Rearrange.  Expanding the score definitions gives the listed alternatives. ∎

This is sharper than a global edge-count failure: it identifies one movement
label and one refill label whose geometric defect budgets are complementary.

## 6. Relation to the excess-shadow potential

Let \(\Xi_i\) be the contribution to the dynamic potential PP3kw from movement
and refill candidate cells using the coordinate sets of pool \(i\).

### Proposition PP3mb -- PROVED

One has

\[
 \boxed{
 A_i+B_i\le\Xi_i.
 }
\]

#### Proof

Every movement defect counted by \(a_i(A)\) is a candidate cell with at least one
noncontroller blocker pair.  By PP3kv it contributes at least one unit to
\(b_S(z)-1\).  The same holds for every refill defect.  The movement and refill
candidate-cell universes are disjoint, so summing gives the inequality. ∎

Consequently, diffuse small excess shadow controls the macro-total terms in the
Ore scores.  What remains capable of defeating direct allocation is now explicit:
label concentration in \(a_i(A)\) or \(b_i(B)\), same-slot anchor concentration,
or a complementary pair of moderately large normalized scores.

This provides a direct target for pool-compatible trades: lowering \(\Xi_i\) is
useful not only because it reduces bad-cell density, but because it improves the
actual degree lower bounds required by the global label matching.