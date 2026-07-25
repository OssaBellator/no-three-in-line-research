# Correction to the PX166 mixed old-edge codegree count

The statement and parameter condition of PX166 are unchanged.  One displayed
intermediate bound in `docs/92-mixed-shape-stars-and-exact-triangle-completion.md`
implicitly assumed that a fixed old edge always determines the row bucket.  In
the two-old-role sector, all fixed edges can occupy the nondistinguished old
role, so one must allow a sum over the bucket label.

This note supplies the corrected count.

Fix \(j'\) old graph edges occupying \(k\) of the \(q\) labelled occurrences in
one mixed repeated-shape conflict.  Conditional on the affine shape:

- a touched occurrence containing \(c\in\{1,2\}\) fixed old edges has
  \(O(p^{2-c})\) choices;
- an untouched occurrence in a specified bucket has \(O(p^3/B)\) choices.

Thus the touched occurrences contribute

\[
O(p^{2k-j'}),
\]

and the untouched occurrences contribute

\[
O\left((p^3/B)^{q-k}ight).
\]

There are \(O(p^3)\) shapes.  In the worst case the fixed old edges do not
determine the bucket, so summing over its \(B\) choices gives the one-row
codegree bound

\[
oxed{
C_qrac{p^{3q-k-j'+3}}{B^{q-k-1}}.
}
\]

This deliberately ignores the additional saving from fixing the completion
row.

Comparing with the required threshold

\[
p^{3q-j'-arepsilon}
\]

reduces the check to

\[
oxed{
B^{q-k-1}\ge p^{3-k+arepsilon}.
}
\]

Only \(k=1,2,3\) are nontrivial.  Since \(B=p^eta\), they require

\[
eta(q-2)\ge2+arepsilon,\qquad
eta(q-3)\ge1+arepsilon,\qquad
eta(q-4)\gearepsilon.
\]

All three follow from the original PX166 hypotheses

\[
0<eta<1,\qquad
eta(q-1)>3+2arepsilon.
\]

Indeed, subtracting respectively \(eta,2eta,3eta\) from the latter
inequality leaves strictly more than the three required right-hand sides.

Therefore PX166, PX167, and their later uses remain valid.  This correction
replaces only the old-edge codegree display and its comparison in the original
proof.
