# Charge-back descent from paid current factors

OP4l constructs factor-conservative payment on current violated source
factors.  Crucially, that payment is incidence-resolved: every paid
unit records the improving correction from which it came.

This note uses that provenance to close the paid-defect recurrence
loop.  A bounded family of paid rank-three factors always returns one
current improving correction with a quantitative share of its payment.
The correction can be executed immediately, preserving rows and
columns and strictly decreasing the syndrome potential.

The statement is snapshot-local.  Charges and corrections from
different phase assignments are never combined.

## Incidence-resolved payment

Fix a current phase snapshot \(\omega\).  Let \(\mathcal I\) be a
family of individually hard-legal improving corrections, with

\[
g_i
=
\Phi(\omega)-\Phi(\rho_i)
>0.
\]

Let \(\mathcal F\) be current violated factors of rank at most \(r\).
An incidence-resolved payment is a family

\[
a_{iF}\geq0
\]

such that:

1. \(a_{iF}>0\) only when correction \(i\) destroys \(F\);
2. every correction respects its gain budget,
   \[
   \boxed{
   \sum_{F\in\mathcal F}a_{iF}\leq g_i;
   }
   \]
3. the paid load of \(F\) is
   \[
   p_F=\sum_i a_{iF}.
   \]

OP4l.0 has row sum \(g_i/K\leq g_i\).  A flow from OP4l.1 has row sum
at most the source capacity \(g_i\).  Restricting to a bicycle, point
star, matching, or signature fibre preserves the row inequalities.

Because the protected supports are disjoint and \(F\) has rank at most
\(r\), at most \(r\) corrections can have \(a_{iF}>0\).

## OP4n -- paid fibre forces executable descent

Let \(\mathcal S\subseteq\mathcal F\) contain \(b\geq1\) factors and
have total payment

\[
W
=
\sum_{F\in\mathcal S}p_F
>0.
\]

### Theorem OP4n -- PROVED

Some correction \(i\) incident to \(\mathcal S\) satisfies

\[
\boxed{
g_i
\geq
\max_{F\in\mathcal S}a_{iF}
\geq
\frac{W}{rb}.
}
\]

Executing \(\rho_i\) is row-column preserving, remains hard-legal, and
has exact drift

\[
\boxed{
\Phi(\rho_i)-\Phi(\omega)
=-g_i
\leq
-\frac{W}{rb}.
}
\]

### Proof

The payment \(W\) is the sum of the charges \(a_{iF}\) with
\(F\in\mathcal S\).  Every one of the \(b\) factors has at most \(r\)
incident corrections, so there are at most \(rb\) nonzero summands.
One summand is at least \(W/(rb)\).

Its correction row has total charge at most \(g_i\), so
\(g_i\geq a_{iF}\).  The correction was audited at the current
snapshot by OP3d; hence it is hard-legal, preserves the active row and
column sets, and decreases the potential by exactly \(g_i\).
\(\square\)

The factor \(r\) and fibre size \(b\) are jointly sharp for incidence
accounting.  Take \(b\) factors, give each one \(r\) private incident
corrections, and put unit charge and unit gain on every incidence.
Then \(W=rb\), while every correction has gain one.

## Consequences for the paid arithmetic outputs

### Corollary OP4n.1 -- heavy factor descent

If one current factor has payment \(p_F>\mu\), then some incident
correction gives

\[
\boxed{
g_i>\frac{\mu}{r}.
}
\]

For the orbit-phase rank \(r=3\), the potential drops by more than
\(\mu/3\).

### Corollary OP4n.2 -- recurrent defect-signature descent

Let one current-old OP4m signature fibre have total actual payment
\(W>0\).

1. For a point-disjoint exact profile/signature fibre,
   \(b\leq\Delta_p\), so an executable correction has
   \[
   \boxed{
   g_i\geq\frac{W}{r\Delta_p}.
   }
   \]
2. For an OP1d endpoint-disjoint point-star signature fibre,
   \(b\leq\Delta_p^\star\), so an executable correction has
   \[
   \boxed{
   g_i\geq\frac{W}{r\Delta_p^\star}.
   }
   \]

Thus a role-tagged paid-defect signature may grow the state ledger on
first exposure, but a current recurrent fibre cannot stall the
decoder.

### Corollary OP4n.3 -- occurrence deduplication is reversible

Suppose OP4l.2 distributes factor load \(p_F\) over repeated
implication occurrences sourced by \(F\).  Reaggregate those
occurrence weights by source-factor identity before charge-back.  The
sum returns exactly \(p_F\), and the original incidence charges
\(a_{iF}\) still satisfy the correction row budgets.

Therefore any OP4i heavy-source-factor output supported on current
paid factors also has the direct descent fallback of OP4n.1.

## Decoder consequence

Extend the role-tagged state ledger as in OP4m.  A paid current-defect
round now has the following exact outcomes.

1. OP4m returns a heavy factor, and OP4n.1 decreases \(\Phi\).
2. OP4m returns a star or matching signature outside the ledger, so
   the ledger strictly grows.
3. Every returned signature is current-old.  Choose any nonempty
   returned fibre and apply OP4n.2 to decrease \(\Phi\).

Hence paid off-core and Hall-reuse defect families require no terminal
delegation.  Before they decrease the syndrome, they can cause only
finitely many role-tagged signature insertions.  With the extended
token capacity \(B_{\rm ext}\) from OP4m, OP3b gives the usual bound

\[
\boxed{
(B_{\rm ext}+1)\Phi_0
+B_{\rm ext}-|\mathcal L_0|.
}
\]

This closes the paid-defect part of the orbit-phase decoder.
[`orbit-phase-centre-fallback.md`](orbit-phase-centre-fallback.md)
gives the complementary OP4o correction-side rule: even a
source-unpaid protected-blocker fibre, paid action-literal class, or
paid wide class contains a current executable improving centre.  That
rule prevents decoder stalling but does not classify those outputs,
or complete RI5 dense edges, as absorbers.

`scripts/verify_phase_chargeback.py` exhausts small nonnegative
rank-three charge matrices and every nonempty factor fibre.  It checks
row budgets, the \(W/(rb)\) descent bound, restriction and occurrence
reaggregation, proportional OP4l payment, recurrent divisor-capacity
bounds, and the sharp family for every \(1\leq r\leq3\).
