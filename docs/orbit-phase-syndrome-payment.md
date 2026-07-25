# Current-syndrome payment for protected correction banks

OP4i.0 proves that protected-bank weights do not automatically
concentrate on an arbitrary implication bicycle.  The missing positive
statement is not a logical theorem about 2-SAT.  It is an incidence
theorem between improving corrections and the current defects they
destroy.

This note gives the exact theorem available from that incidence.

1. Total correction gain has a factor-conservative payment of at least
   a \(1/r\) fraction on current violated source factors, where \(r\)
   is the maximum factor rank.
2. A capacitated Hall test decides whether all correction gain can be
   paid without exceeding current syndrome weight.
3. Hall failure returns a quantified family of current defects reused
   by several corrections.
4. For any selected implication bicycle, either its current-defect
   source factors receive a chosen fraction of the payment or the
   complementary payment survives on explicit off-bicycle current
   defects.

For the orbit-phase instance \(r=3\), so the unconditional retained
payment is at least one third of the correction gain.  This factor is
sharp.

## Gain--defect incidence

Fix one current phase assignment \(\omega\), and let
\(\mathcal I\) be improving corrections from one current protected
bank.  Correction \(i\) has gain

\[
g_i
=
\Phi(\omega)-\Phi(\rho_i)
>0.
\]

Let \(\mathcal D\) be the weighted soft factors violated by
\(\omega\).  Factor \(Q\) has weight \(w_Q>0\) and scope of size at
most \(r\).

Write

\[
i\sim Q
\]

when \(\rho_i\) destroys \(Q\).  Since \(Q\) is currently violated,
every current value on its scope equals its forbidden value.  Thus a
correction destroys \(Q\) exactly when its support meets the scope of
\(Q\).

Put

\[
D_i
=
\sum_{Q:i\sim Q}w_Q.
\]

If \(C_i\geq0\) is the collateral weight created by correction \(i\),
then OP3d gives

\[
\boxed{
g_i=D_i-C_i\leq D_i.
}
\]

Every defect meets at most \(r\) pairwise disjoint protected supports,
so

\[
\boxed{
\deg_{\mathcal I}(Q)\leq r.
}
\]

In the OP4a projection, a current defect meeting protected supports
\(i_1,\ldots,i_s\) contributes the current-zero clause

\[
\boxed{x_{i_1}\vee\cdots\vee x_{i_s}.}
\]

It is false at the all-current orientation, and switching any incident
correction satisfies it.  Therefore every paid defect below retains
an OP4a source-clause identity as well as its original geometric
factor.

## OP4l.0 -- sharp proportional source-factor payment

Define the normalized congestion

\[
\kappa
=
\max_{Q\in\mathcal D}
\sum_{i:i\sim Q}\frac{g_i}{D_i},
\qquad
K=\max\{1,\kappa\}.
\]

For every incidence \(i\sim Q\), assign

\[
\boxed{
a_{iQ}
=
\frac{g_iw_Q}{KD_i}.
}
\]

### Theorem OP4l.0 -- PROVED

The proportional charges have all of the following properties.

1. Every correction sends
   \[
   \boxed{
   \sum_{Q:i\sim Q}a_{iQ}
   =
   \frac{g_i}{K}.
   }
   \]
2. Every current defect receives at most its syndrome weight:
   \[
   \boxed{
   p_Q
   :=
   \sum_{i:i\sim Q}a_{iQ}
   \leq w_Q.
   }
   \]
3. With \(G=\sum_i g_i\), the factor-conservative payment satisfies
   \[
   \boxed{
   P:=\sum_Qp_Q
   =
   \frac GK
   \geq\frac Gr.
   }
   \]

For rank three, \(P\geq G/3\).

### Proof

Summing \(a_{iQ}\) over the neighborhood of \(i\) gives

\[
\sum_{Q:i\sim Q}a_{iQ}
=
\frac{g_i}{KD_i}
\sum_{Q:i\sim Q}w_Q
=
\frac{g_i}{K}.
\]

For a fixed defect,

\[
p_Q
=
\frac{w_Q}{K}
\sum_{i:i\sim Q}\frac{g_i}{D_i}
\leq w_Q
\]

by the definition of \(K\).

Finally, \(g_i/D_i\leq1\), and at most \(r\) corrections meet a
rank-\(r\) defect.  Hence \(\kappa\leq r\), so
\(K\leq r\).  Summing the correction row totals gives
\(P=G/K\geq G/r\). \(\square\)

The rank loss is sharp.  One rank-\(r\) current defect of weight one
can be destroyed independently by \(r\) disjoint one-variable
corrections, each of gain one.  Then \(G=r\), while a
factor-conservative payment on that sole source factor is at most one.

## OP4l.1 -- capacitated Hall payment or paid reuse

Build the payment network

\[
s\longrightarrow i\longrightarrow Q\longrightarrow t
\]

with capacities

\[
c(s,i)=g_i,
\qquad
c(i,Q)=+\infty\quad(i\sim Q),
\qquad
c(Q,t)=w_Q.
\]

For \(\mathcal J\subseteq\mathcal I\), let

\[
g(\mathcal J)=\sum_{i\in\mathcal J}g_i,
\qquad
N(\mathcal J)=\{Q:\exists i\in\mathcal J,\ i\sim Q\},
\]
\[
w(N(\mathcal J))
=
\sum_{Q\in N(\mathcal J)}w_Q.
\]

Define the Hall deficit

\[
\boxed{
\delta
=
\max_{\mathcal J\subseteq\mathcal I}
\bigl(
g(\mathcal J)-w(N(\mathcal J))
\bigr)_+.
}
\]

### Theorem OP4l.1 -- PROVED

The maximum factor-conservative payment has value

\[
\boxed{P_{\max}=G-\delta.}
\]

Consequently:

1. all gain is paid exactly when
   \[
   \boxed{
   g(\mathcal J)\leq w(N(\mathcal J))
   \quad
   \text{for every }\mathcal J\subseteq\mathcal I;
   }
   \]
2. always
   \[
   \boxed{
   P_{\max}\geq\frac GK\geq\frac Gr;
   }
   \]
3. if \(\delta>0\), a maximizing deficient set
   \(\mathcal J\) satisfies
   \[
   \boxed{
   \sum_{Q\in N(\mathcal J)}
   \bigl(m_{\mathcal J}(Q)-1\bigr)w_Q
   \geq\delta,
   }
   \]
   where
   \[
   m_{\mathcal J}(Q)
   =
   |\{i\in\mathcal J:i\sim Q\}|.
   \]
   Hence the repeated-defect family
   \[
   \mathcal R_{\mathcal J}
   =
   \{Q:m_{\mathcal J}(Q)\geq2\}
   \]
   has current syndrome weight at least
   \[
   \boxed{
   \sum_{Q\in\mathcal R_{\mathcal J}}w_Q
   \geq
   \frac{\delta}{r-1}.
   }
   \]

### Proof

Every finite cut in the displayed network is determined by the
corrections \(\mathcal J\) retained on the source side.  All their
neighboring factors must also lie on that side.  Extra factor vertices
only increase the cut, so its minimum capacity for fixed
\(\mathcal J\) is

\[
G-g(\mathcal J)+w(N(\mathcal J)).
\]

Minimizing over \(\mathcal J\) and applying max-flow/min-cut gives
\(P_{\max}=G-\delta\).  This proves the Hall criterion.  OP4l.0 is an
explicit feasible flow of value \(G/K\), proving the universal lower
bounds.

For a maximizing deficient set,

\[
\begin{aligned}
\sum_{Q\in N(\mathcal J)}
\bigl(m_{\mathcal J}(Q)-1\bigr)w_Q
&=
\sum_{i\in\mathcal J}D_i-w(N(\mathcal J))\\
&\geq
g(\mathcal J)-w(N(\mathcal J))\\
&=\delta.
\end{aligned}
\]

Only repeated factors contribute, and
\(m_{\mathcal J}(Q)-1\leq r-1\).  Dividing by \(r-1\) gives the final
bound. \(\square\)

Thus failure of full payment is not an anonymous max-flow failure.  It
returns a current-syndrome factor family whose weight is certified by
multiple correction incidences.  This is the same capacitated-Hall
mechanism that appears in the alternating-core and geometric-cleaning
tracks, now specialized to the protected-bank interface.

## OP4l.2 -- bicycle payment or off-core defect escape

Let \(\mathcal C\) be the set of source factors used by one selected
OP4d bicycle, and let \(p_Q\) be any factor-conservative payment of
total \(P>0\), for example OP4l.0 or a maximum flow from OP4l.1.

Fix \(0<\theta<1\), and put

\[
P_{\mathcal C}
=
\sum_{Q\in\mathcal C\cap\mathcal D}p_Q.
\]

### Corollary OP4l.2 -- PROVED

Exactly one of the following payment gates holds.

1. **Bicycle participation.**
   \[
   \boxed{P_{\mathcal C}\geq\theta P.}
   \]
   Distribute \(p_Q\) evenly over the selected implication
   occurrences sourced by \(Q\).  The resulting occurrence weights
   are factor-conservative and have total \(P_{\mathcal C}\), so they
   may enter OP4h and OP4i.
2. **Off-core current-defect escape.**
   \[
   \boxed{
   \sum_{Q\in\mathcal D\setminus\mathcal C}p_Q
   >(1-\theta)P.
   }
   \]
   Every returned factor is currently violated and retains its OP1a
   geometric triple, current-zero OP4a clause, channel profile, and
   OP4g carry routes.

### Proof

The two displayed payment sums partition \(P\).  In the first case, if
source factor \(Q\) occurs \(k_Q\geq1\) times in the selected bicycle,
give each such occurrence weight \(p_Q/k_Q\).  The weights sourced by
\(Q\) sum to \(p_Q\leq w_Q\), so no duplicated implication creates
payment.  If the first inequality fails, the complementary sum is
strictly greater than \((1-\theta)P\). \(\square\)

Taking the proportional payment and \(\theta=1/2\) gives an explicit
rank-three alternative:

\[
\boxed{
\text{paid bicycle weight at least }G/6
\quad\text{or}\quad
\text{paid off-core current defects of weight greater than }G/6.
}
\]

This is the strongest universal source-participation statement
available without additional geometry.  It respects OP4i.0: an
arbitrary contradiction core may receive no payment, but that failure
now returns a comparably paid current-syndrome factor family rather
than losing the correction gain.

## Exact interface after OP4l

The source-payment frontier now has a lossless gate.

1. OP4l.0 transfers at least one third of rank-three correction gain to
   current geometric source factors.
2. OP4l.1 either pays all gain or returns a Hall-deficient correction
   set with quantified repeated current-defect weight.
3. OP4l.2 either supplies the factor-conservative occurrence weights
   required by OP4i or preserves a comparable payment on explicit
   off-bicycle current defects.

[`orbit-phase-defect-router.md`](orbit-phase-defect-router.md) proves
OP4m and performs that routing.  A paid off-core or Hall-reuse family
returns one heavy current factor, a paid point-star carry family, or
quantitatively many exact signatures on point-disjoint current
defects.  [`orbit-phase-chargeback.md`](orbit-phase-chargeback.md)
proves OP4n and sends every heavy or current-recurrent paid fibre back
to an executable improving correction.  Thus no further generic
conversion from correction gain to current source-factor payment, from
paid source factors to geometric carry records, or from recurrent paid
records to decoder descent is missing.

`scripts/verify_phase_syndrome_payment.py` exhausts small rank-three
gain--defect incidence systems over a finite rational weight grid.  It
checks the proportional charges, max-flow/min-cut value, Hall
criterion, overload identity, repeated-defect bound, occurrence
deduplication, core/off-core split, and the sharp rank-three example.

`scripts/verify_phase_defect_router.py` checks the subsequent OP4m
point-star/matching and carry-capacity alternatives.

`scripts/verify_phase_chargeback.py` checks OP4n's incidence-resolved
descent and sharp rank/fibre loss.
