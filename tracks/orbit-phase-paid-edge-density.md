# Paid density on one rational quotient edge

OP4e and RI4b localize a certified order-two obstruction to one
quotient edge.  That localization is not yet an absorber.  Two
additional questions must be answered.

1. Does the selected implication bicycle carry certified source-factor
   payment?
2. Does one quotient edge represent many distinct rational orbits, are
   their two roots both genuinely witnessed, or does it only repeat a
   few geometric factors?

The first question cannot be answered from protected-bank weights by
logic alone.  Once factor-conservative edge payment is supplied, the
second question has an exact density/repetition/carry alternative.

## OP4i.0 -- protected-bank payment does not transfer automatically

Give the protected corrections arbitrary positive weights
\(w_1,\ldots,w_m\).  These are weights on correction centres, not on
clauses or implication occurrences.

### Proposition OP4i.0 -- PROVED

There is no positive universal lower bound on the protected-bank weight
met by an OP4d contradiction bicycle.

This remains true when every protected switch occurs in a projected
clause.

### Proof

On \(x_1,x_2\), take the four binary clauses

\[
\bigl(x_1\ne\epsilon\bigr)
\ \vee\
\bigl(x_2\ne\delta\bigr),
\qquad
(\epsilon,\delta)\in\{0,1\}^2.
\]

Every assignment to \(x_1,x_2\) falsifies the clause indexed by that
assignment, so the four-clause formula is unsatisfiable.  For every
\(i\geq3\), add the satisfiable unit clause \(x_i=1\).  Every variable
now occurs, but an implication contradiction remains entirely inside
the four clauses on \(x_1,x_2\).

Set \(w_1=w_2=1\) and let
\(\sum_{i\geq3}w_i\) tend to infinity.  The contradictory bicycle meets
corrections of total weight two while the protected-bank weight is
unbounded. \(\square\)

This is an abstract OP4a instance, not a claim that every orbit
geometry realizes the four-clause core.  It proves that OP4a--OP4d
alone cannot manufacture paid geometric incidence.  A positive paid
theorem must import a source-factor participation statement from the
current syndrome accounting.
[`orbit-phase-syndrome-payment.md`](orbit-phase-syndrome-payment.md)
provides exactly that input, with a paid off-core alternative when the
selected bicycle does not participate.

## Factor-conservative occurrence weights

Let \(\mathcal E\) be a family of certified implication occurrences on
one fixed quotient edge

\[
\boxed{(R,\{A,B\},C)}
\]

of \(Q=\mathbb F_p^\times/H\).  Give every occurrence \(e\) a
nonnegative weight \(w_e\).

The weighting is **factor-conservative** when every source factor
\(F\) has an external certified payment \(p_F\) and

\[
\boxed{
\sum_{e:\operatorname{src}(e)=F}w_e\leq p_F.
}
\]

This prevents the two implications of one binary clause, or repeated
uses of one edge in a bicycle, from creating payment by duplication.
Put

\[
W=\sum_{e\in\mathcal E}w_e.
\]

Every occurrence retains its selected OP4g normalization:

\[
(a_e,b_e,r_e,c_e,c_e^\dagger,g_e),
\]

where

\[
r_e=b_e/a_e,\qquad
c_e^\dagger=\tau_{r_e}(c_e),\qquad
F_{r_e}(c_e)=g_e.
\]

Although the quotient root \(R\) is fixed, the exact ordered channel
pair \((a_e,b_e)\) need not be fixed.

## OP4i -- density, factor reuse, or carry growth

Let \(\mathcal P\) be the set of exact ordered channel pairs represented
by \(\mathcal E\), and put

\[
P=|\mathcal P|.
\]

If the active phase state uses at most \(q_{\rm act}\) channels, then

\[
P\leq q_{\rm act}(q_{\rm act}-1).
\]

Choose a heaviest channel-pair class and call its weight \(W_0\).
Then

\[
\boxed{W_0\geq W/P.}
\]

The exact pair fixes \(a,b\) and \(r=b/a\).  Partition this class by
the exact rational fibre

\[
\mathcal O(c)
=
\bigl(\{c,\tau_r(c)\},F_r(c)\bigr).
\]

Let \(N\) be the number of represented fibres.
Call a fibre **complete** when both roots
\(c,\tau_r(c)\) occur as actual OP4g parameters, with the usual
one-root convention at a fixed point.  Let \(N_{\rm full}\) be the
number of complete fibres.

Computing \(\tau_r(c)\) is an algebraic certificate of the quotient
law.  It does not by itself witness a second geometric factor with
parameter \(\tau_r(c)\).  This completion distinction is mandatory for
RI5.

### Theorem OP4i -- PROVED

Fix an integer \(d\geq2\) and a factor-load threshold
\(\lambda>0\).  Exactly one of the following named outputs can be
returned.

1. **Complete dense rational edge.**
   \[
   \boxed{N_{\rm full}\geq d.}
   \]
   If \(A\ne B\), the complete fibres give:
   \[
   |S_A|=|S_B|=|T_C|=N_{\rm full},
   \]
   where
   \[
   S_A\subseteq A,\qquad
   S_B\subseteq B,\qquad
   T_C\subseteq C,
   \]
   and \(F_r\) maps the two source sets onto the target set in
   two-point fibres.

   If \(A=B\), they give
   \[
   |T_C|=N_{\rm full},\qquad
   |S_A|\geq2N_{\rm full}-2.
   \]

2. **One-sided orbit growth.**
   \[
   \boxed{N\geq d>N_{\rm full}.}
   \]
   Return the \(N\) distinct witnessed parameters and images, together
   with the missing companion root of every incomplete fibre.  This is
   genuine rational-orbit/image growth, but not a dense invariant core.

3. **Heavy source factor.**  When \(N<d\), one exact rational fibre and
   one of its
   at most two parameter branches retain a source factor of occurrence
   weight greater than
   \[
   \boxed{\lambda.}
   \]
   The factor identity and every duplicated implication occurrence are
   returned.

4. **Product-carry growth.**  When \(N<d\), one exact rational fibre
   and one parameter branch have weight
   \[
   \boxed{
   W_2
   \geq
   \frac{W}{2P(d-1)}.
   }
   \]
   Every source factor in the class has load at most \(\lambda\), and
   the factors represent at least
   \[
   \boxed{
   B
   \geq
   \frac{W_2}{2\lambda\Delta_p}
   \geq
   \frac{W}
   {4P(d-1)\lambda\Delta_p}
   }
   \]
   distinct same-channel product-carry signatures.

Here

\[
\Delta_p=\max_{1\leq n<p^2}\tau(n).
\]

Every output retains its exact source-factor, channel, quotient,
rational-orbit, and carry provenance.

### Proof

First suppose \(N\geq d\).  RI0 says that different
\(\tau_r\)-orbits have different images under \(F_r\).  If fewer than
\(d\) fibres have both roots witnessed, return conclusion 2 with the
exact completion deficits.

Otherwise use \(d\) complete fibres.

When \(A\ne B\), every orbit has one root in each endpoint coset.  It
therefore contributes one distinct point to \(S_A\), one to \(S_B\),
and one distinct image to \(T_C\).

When \(A=B\), every nonfixed orbit contributes two source points and a
fixed orbit contributes one.  The equation
\(\tau_r(c)=c\) is quadratic, so there are at most two fixed points.
Hence

\[
|S_A|\geq2N_{\rm full}-2.
\]

Now suppose \(N<d\).  A heaviest exact rational fibre has weight

\[
W_1\geq\frac{W_0}{N}
\geq\frac{W_0}{d-1}.
\]

Its actual OP4g parameter is one of the two fibre roots, so a heaviest
parameter branch has

\[
W_2\geq W_1/2
\geq\frac{W}{2P(d-1)}.
\]

If one source factor carries more than \(\lambda\), return conclusion
3.  Otherwise aggregate duplicated occurrences by source-factor
identity before counting geometry.

Fix the channel pair, rational fibre, parameter branch, and the
unordered same-channel product-carry signature

\[
\left\{
\kappa_a(P_x),\kappa_a(P_u)
\right\}.
\]

The parameter \(c=z/x\), transition \(g=u/x\), and channels \(a,b\)
are now fixed.  Thus the base endpoint \(x\) determines

\[
P_x,\qquad P_{gx},\qquad B_{cx},
\]

and hence determines the source factor.

For one product-carry level \(j\), SC1 gives at most
\(\Delta_p\) possible points on \(H_a\).  In an unordered two-level
signature, \(P_x\) can lie on either level, so at most
\(2\Delta_p\) distinct source factors have one fixed signature.
Each carries load at most \(\lambda\).  One signature therefore carries
at most

\[
2\lambda\Delta_p
\]

weight.  Dividing \(W_2\) by this capacity proves conclusion 4.
\(\square\)

## Density threshold for RI5

Put \(h=|H|\).  Taking

\[
d=\left\lceil\alpha h\right\rceil
\]

turns conclusion 1 into simultaneous **witnessed** density at least
\(\alpha\) in both endpoint cosets and the image coset, up to the two
fixed points in the loop case.

In particular, a threshold above \(h/2\) reaches the dense-coset regime
needed by the corrected RI1/RI5 interface.  OP4i does not assert that
such a dense partial coset is already absorbable; it supplies the exact
input on which that remaining conversion must operate.

## Interface after OP4i

The fixed-edge frontier now has four explicit gates.

1. Proposition OP4i.0 shows that protected-bank gain cannot transfer
   to one selected bicycle by 2-SAT logic alone.
   [`orbit-phase-syndrome-payment.md`](orbit-phase-syndrome-payment.md)
   proves the exact replacement: OP4l pays at least \(G/3\) on current
   rank-three source factors, then returns factor-conservative bicycle
   occurrences or a comparably paid off-core defect family.
   [`orbit-phase-defect-router.md`](orbit-phase-defect-router.md)
   routes the latter to a heavy factor, paid point star, or
   point-disjoint carry-signature growth.
2. Exact channel-pair localization costs the displayed factor \(P\);
   many channel pairs may instead be retained as a root/channel
   complexity output.
3. A complete dense exact-root fibre family enters the corrected
   rational inverse and RI5 density problem.  A large one-sided family
   returns its exact missing-companion list instead.
4. Sparse fibre support returns either one genuinely repeated source
   factor or quantified product-carry signature growth.  It cannot
   masquerade as a dense order-two absorber.

Thus RI4b's “one fixed quotient edge” conclusion is now separated from
the distinct-orbit density that absorber conversion actually needs.
Arbitrary repeated implication weight is never called rational
density.

`scripts/verify_phase_paid_edge_density.py` enumerates every really
collinear oriented two-channel factor for \(p=11\), checks the
factor/carry capacity bound in every exact template class, and exercises
the complete dense nonloop, complete dense loop, one-sided,
channel-localization, heavy-factor, carry-growth, and mixed-edge
outputs.  It also verifies the
arbitrarily-unpaid contradiction-core family through eight protected
switches.
