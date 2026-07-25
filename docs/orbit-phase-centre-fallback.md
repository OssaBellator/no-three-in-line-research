# Current-centre descent fallback

The structured outputs of OP3j--OP4k were retained in order to obtain
stronger arithmetic information: simultaneous completions, classified
absorbers, or monotone carry-signature growth.  That extra structure is
not needed to execute one of the correction centres which generated the
output.

This distinction matters for the bounded recurrent rank-three fibre.
OP4k correctly says that its source factors need not carry
current-syndrome payment.  Nevertheless, the three switches incident
with each matching factor are current improving corrections from the
protected bank.  The fibre is unpaid on the **source-factor side**, not
on the **correction-centre side**.

Everything below is snapshot-local.  A correction is executed before
the phase assignment changes; historical centres are never revived
from a ledger token.

## Retained centre weights

Fix a current hard-legal phase assignment \(\omega\).  Let
\(\rho_i\), \(i\in\mathcal I\), be distinct individually hard-legal
corrections produced at \(\omega\).  By OP3d, their exact gains are

\[
g_i
=
\Phi(\omega)-\Phi(\rho_i)
>0.
\]

Attach a retained centre weight \(w_i\) satisfying

\[
\boxed{0<w_i\leq g_i.}
\]

The two uses needed here satisfy this condition exactly.

1. An OP3j wide or action-kernel class retains its original weights,
   so \(w_i=g_i\).
2. In a fixed OP3k signature class, centre \(i\) contributes
   \[
   w_i=\frac{g_i}{|\mathcal S_i|}\leq g_i.
   \]
   OP3l restricts these positive split weights without altering the
   underlying corrections.

## OP4o -- one-centre descent

### Theorem OP4o.0 -- PROVED

For every nonempty current subfamily
\(\mathcal J\subseteq\mathcal I\), put

\[
n=|\mathcal J|,
\qquad
W_{\mathcal J}=\sum_{i\in\mathcal J}w_i.
\]

There is an \(i\in\mathcal J\) such that executing \(\rho_i\):

1. is hard-legal;
2. preserves every active row and column; and
3. has exact potential decrease satisfying
   \[
   \boxed{
   \Phi(\omega)-\Phi(\rho_i)
   =g_i
   \geq w_i
   \geq\frac{W_{\mathcal J}}{n}
   >0.
   }
   \]

### Proof

Choose \(i\) with maximum \(w_i\) in \(\mathcal J\).  Averaging gives
\(w_i\geq W_{\mathcal J}/n\), and the retained-weight condition gives
\(g_i\geq w_i\).  Individual hard legality and the exact potential
identity are OP3d.  Every correction changes only O1 orbit phases, so
O1 preserves the active row and column sets. \(\square\)

The conclusion is sharp: if all \(w_i=g_i=c\), its guaranteed decrease
is exactly \(W_{\mathcal J}/n=c\).

When \(\Phi\) is the integer syndrome potential used by OP3b, the
strict decrease is at least one and is a type-1 OP3b round.  For
arbitrary positive real factor weights it is still strict; since the
phase-state space is finite, a sequence which always executes the
returned current correction cannot repeat a state.  This observation
does not supply the missing total oracle at a positive local minimum.

## Paid OP3j classes

Let \(N_{\rm wide}\) be the number of centres in the wide class of
OP3j conclusion 2.  That class has original gain
\(G_{\rm wide}>G/4\), so OP4o.0 gives a current correction with

\[
\boxed{
g_i\geq\frac{G_{\rm wide}}{N_{\rm wide}}
>\frac{G}{4N_{\rm wide}}.
}
\]

Likewise, if \(N_{\rm act}\) centres form the paid action-literal
kernel class of OP3j conclusion 3, then

\[
\boxed{
g_i\geq\frac{G_{\rm act}}{N_{\rm act}}
>\frac{G}{12N_{\rm act}}.
}
\]

Thus a wide action CSP or repeated action-literal kernel is not a
decoder stall.  Its unresolved status concerns a stronger batched
completion or absorber classification.

The same statement applies to any positive-weight subset selected by
the high-reuse output of OP3l.  If its \(k\) current centres have
total retained split weight \(W\), one of them decreases \(\Phi\) by
at least \(W/k\).

## Source-unpaid rank-three fibres

Take an OP4f switch-disjoint matching fibre \(M_\sigma\) returned by
OP4k at \(\omega\), and put

\[
b=|M_\sigma|.
\]

Each factor meets exactly three protected switches, and
switch-disjointness makes the union \(K(M_\sigma)\) contain exactly
\(3b\) distinct current correction centres.  Retain on those centres
their positive OP3k--OP3l split weights and put

\[
W_K=\sum_{i\in K(M_\sigma)}w_i.
\]

### Corollary OP4o.1 -- PROVED

The current recurrent blocker fibre has an executable correction with

\[
\boxed{
g_i\geq\frac{W_K}{3b}
\geq\frac{W_K}{3\Delta_p}
>0.
}
\]

### Proof

Apply OP4o.0 to the \(3b\) incident centres.  OP4k.0 gives
\(b\leq\Delta_p\). \(\square\)

This corollary does not assign \(W_K\) to the source factors.  It uses
the centre weights only, so it neither assumes nor manufactures the
OP4l factor-conservative payment that OP4k deliberately omits.

The same fallback applies before the matching route.  A rank-two
implication bicycle, a bounded switch kernel, or any other nonempty
protected-bank subinstance touches a finite set \(K\) of current
centres.  With \(W_K=\sum_{i\in K}w_i\), one incident centre gives
descent at least \(W_K/|K|\).

## Decoder consequence and remaining boundary

Add the following current-centre rule to the structured decoder.

1. Ledger growth may be recorded without changing \(\omega\).
2. On a no-growth current return, either use its stronger arithmetic
   endpoint or immediately execute the OP4o centre.
3. After any phase change, discard every remaining centre and rebuild
   all corrections at the new snapshot.

Consequently, source-unpaid OP4k fibres, paid action-literal classes,
and paid wide classes cannot recur as zero-progress decoder rounds.
For the integer syndrome potential they rejoin OP3b descent; otherwise
they give strict descent in the finite phase space.

The result does **not** prove that these structured families are
absorbers, that a whole protected bank has a satisfying noncurrent
orientation, or that OP2 supplies an improving correction at every
positive-syndrome state.  The remaining arithmetic work is therefore
more precisely separated into:

1. RI5 row-column-preserving conversion of a complete dense fixed
   quotient edge;
2. simultaneous absorber or completion structure for the rank-three,
   action-kernel, and wide-CSP outputs when that stronger interface is
   required; and
3. the upstream total-oracle theorem which must produce a current
   improving correction, ledger growth, or a classified terminal
   exception at every positive-syndrome state.

`scripts/verify_phase_centre_fallback.py` exhausts small exact rational
gain/weight families and every nonempty subfamily, checks OP3k split
weights, paid OP3j class bounds, and switch-disjoint blocker fibres,
and verifies sharp equal-weight examples.
