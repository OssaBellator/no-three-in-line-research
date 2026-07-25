# Forced cross-child certificates have finite ancestry and paid escape

CMR677--CMR683 close one fixed child-routing product except when a mixed atom is
made entirely of child-essential edges.  Such an atom occurs in every product
state.  This chapter records its terminality, finite owner-labelled stock, and
escape payment along the strict factor-recursion path.

Work on one selected factor-recursion path after routing-change episodes have
been charged by CMR671--CMR676.  At a fixed stage, let

\[
\mathcal P
=
\prod_{a\in A}\operatorname{PM}(H_a)
\]

be the current child product, and let `T` be a compatible collinear triple whose
edges are essential in their respective child hosts.

## 1. Forced child certificates are product-terminal

### Theorem CMR684 — PROVED

Every state of `\mathcal P` contains `T`.  In particular:

1. varying any proper subcollection of child matchings cannot remove `T`;
2. recursing inside one child factor while the other factors and routing owner
   remain fixed cannot produce a globally candidate-conflict-free state;
3. before a clean continuation is possible, at least one edge of `T` must cease
   to be forced or the routing owner must change.

### Proof

Every local edge of `T` is essential in its child host, hence belongs to every
local perfect matching.  Their union therefore contains the complete triple in
every product state.  The three conclusions are immediate. ∎

Thus strict child recursion is available only in the mixed-clean branch of
CMR681, not as a way to ignore a forced mixed certificate.

## 2. Canonical forced-certificate signatures

At one normalised stage, define the signature

\[
\Sigma_T
=
(
\text{factor owner},
\text{factor envelope},
\text{routing skeleton},
\text{child hosts},
T
).
\]

The physical edges of `T` retain their absolute parent-grid coordinates.

### Theorem CMR685 — PROVED

At a stage whose factor side is `m`, the number of possible physical forced
triples is at most

\[
\boxed{
N_{\mathrm{tri}}(m)
\le
\binom{m^2}{3}.
}
\]

The same physical triple under a different factor, envelope, routing, or host
stage receives a different owner signature; within one fixed owner it is charged
only once.

### Proof

The factor host has at most `m^2` physical edges.  A certificate is a three-edge
subset of that universe.  The signature convention supplies the ownership
statement. ∎

Compatibility and collinearity only reduce the count.

## 3. Polynomial stage stock along one strict descent path

At side `m`, CMR653 uses at most

\[
m^2+m+1
\]

normalised pure-factor contraction/deletion stages.  Before entering a strict
child, CMR680 uses at most `m^2` mixed-atom deletions.

### Theorem CMR686 — PROVED

After routing-change episodes are charged separately, the number of static
normalised owner stages on one strict factor-descent path starting at side `d`
is at most

\[
\boxed{
N_{\mathrm{stage}}(d)
\le
\sum_{m=1}^{d}(2m^2+m+1)
}
\]

and hence

\[
\boxed{
N_{\mathrm{stage}}(d)
\le
\frac{d(d+1)(2d+1)}{3}
+
\frac{d(d+1)}{2}
+d.
}
\]

The total owner-labelled forced-certificate stock on the path is therefore at
most

\[
\boxed{
N_{\mathrm{cert}}(d)
\le
N_{\mathrm{stage}}(d)
\binom{d^2}{3}.
}
\]

### Proof

CMR653 supplies the first stage bound and CMR680 the second.  Every child
continuation has strictly smaller positive factor side by CMR683, so a selected
path visits each integer side at most once.  Sum the bounds over `m=1,...,d`.
Every visited stage has at most `binom(d^2,3)` possible physical triples, giving
the coarse uniform certificate bound. ∎

The envelope depth also strictly increases at every child continuation, so the
same path has at most `h` strict prefix descents inside a parent of side `p^h`.

## 4. Finite certificate history or exact recurrence

### Theorem CMR687 — PROVED

For every integer `\lambda\ge2`, a history of `J` forced-child certificate
episodes along one selected descent path satisfies at least one of:

1. **Exact signature recurrence.**  One owner-labelled signature `\Sigma_T`
   occurs in at least `\lambda` episodes.
2. **Finite forced-certificate history.**
   \[
   \boxed{
   J
   \le
   (\lambda-1)N_{\mathrm{cert}}(d).
   }
   \]

### Proof

There are at most `N_{\mathrm{cert}}(d)` signatures by CMR686.  If none occurs
`\lambda` times, every signature occurs at most `\lambda-1` times. ∎

Thus repeated forced triples cannot migrate anonymously between child owners.

## 5. Escape from a fixed signature is already paid

Fix one recurrent signature `\Sigma_T` at a stage of side `m`.

### Theorem CMR688 — PROVED

Any later matchable state with the same outer selector owner which avoids `T`
reaches at least one of:

1. deletion or absence of a certificate edge;
2. a change of the child-routing skeleton;
3. loss of essentiality of a certificate edge, supported on a genuinely new
   factor edge in every affected alternating-cycle component.

### Proof

This is the forced-product escape trichotomy CMR645, applied to the child
product.  Routing change is paid by CMR671--CMR676, and factor essentiality loss
has the entering-edge support of CMR643--CMR644. ∎

No internal variation inside the unchanged child hosts can escape the
certificate.

## 6. Repeated escape has finite witness stock or recurrence

Assign every escape the canonical witness order from CMR646: a deleted
certificate edge, then a routing symmetric-difference edge, then a new factor
edge on the first affected alternating component.

### Theorem CMR689 — PROVED

At a fixed owner stage of side `m`, there are at most

\[
\boxed{3m^2}
\]

possible physical escape witnesses.  For every integer `\mu\ge2`, `K` escapes
from the recurrent certificate satisfy at least one of:

1. one exact owner-labelled witness edge occurs in at least `\mu` escapes;
2. \[
   \boxed{K\le3(\mu-1)m^2.}
   \]

A recurrent witness enters the existing deletion, routing-edge,
reintroduction, full-token, or entering-edge recreation ledger according to its
type.

### Proof

The witness stock and recurrence bound are CMR646.  The routing and token
splices are CMR647--CMR648 and CMR671--CMR675. ∎

## 7. Forced-child ancestry endpoint

### Corollary CMR690 — PROVED

Every continuation of a recurrent child-routing product reaches at least one of
the following endpoints.

1. finite mixed-atom deletion followed by a globally clean product state;
2. strict recursion into one pure-dirty child factor with smaller envelope and
   side;
3. finite owner-labelled forced-certificate stock;
4. one exact recurrent forced certificate;
5. certificate-edge deletion, routing-change payment, or a recurrent/new
   entering edge supporting essentiality loss.

In particular, the forced-certificate branch introduces no anonymous or
unpriced child-recursion loop.

### Proof

Use CMR681--CMR683 for the first two branches, CMR686--CMR687 for finite stock or
recurrence, and CMR688--CMR689 for escape from a recurrent signature. ∎

The remaining prime-power frontier is no longer the fixed child product.  It is
to aggregate the resulting strictly descending child path and recurrent escape
witnesses with the inherited target-load potential, protected reserve, and
closure-envelope budget, and then transfer the endpoint to the prime-field and
arbitrary-side routes.

No all-`n` theorem is claimed.  Stage-stock arithmetic, certificate recurrence,
and forced-product terminality are checked in
[`scripts/verify_prime_power_forced_child_ancestry.py`](../scripts/verify_prime_power_forced_child_ancestry.py).
