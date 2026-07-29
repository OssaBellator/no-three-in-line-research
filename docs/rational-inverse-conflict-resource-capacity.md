# Resource-capacity payment for labeled RI conflict classes

**Branch:** `research/rational-inverse-expansion`

RI5bz--RI5cc reduce failure of a requested physical RI bank to one quantitatively heavy conflict class. This note converts that class into either a stock of resource-disjoint records or one high-multiplicity physical resource.

Let `C` be one returned conflict class, with nonnegative record weights `w(c)` and total weight

\[
Q=\sum_{c\in C}w(c).
\]

Each record carries one least payment resource `r(c)` from a fixed physical resource set. A resource may be a line cell, blocker, owner occurrence, protected cell, certificate or exterior slot.

## RI5cd -- exact resource partition -- PROVED

For each resource `r`, put

\[
C_r=\{c\in C:r(c)=r\}.
\]

Then the nonempty `C_r` partition `C`, and

\[
\boxed{Q=\sum_r w(C_r).}
\]

### Proof

Every conflict record has exactly one least payment resource. Hence it belongs to exactly one fibre. Summing over the fibres gives the identity. QED.

## RI5ce -- bounded-multiplicity representative stock -- PROVED

Suppose every resource fibre contains at most `mu` records, with `mu>=1`. Choose one maximum-weight record `c_r` from every nonempty fibre. Then the selected records have pairwise distinct payment resources and

\[
\boxed{
\sum_r w(c_r)\ge \frac{Q}{\mu}.
}
\]

### Proof

For each fibre, `w(C_r)<=mu w(c_r)`. Sum this inequality over resources and use RI5cd. Distinct fibres give distinct resources. QED.

## RI5cf -- payment efficiency or resource-star alternative -- PROVED

Fix `mu>=1`. Exactly one of the following holds:

1. one physical resource supports more than `mu` conflict records;
2. there is a resource-disjoint representative stock of weight at least `Q/mu`.

If every selected record pays at least `rho w(c)` through its own resource, then branch 2 realizes total payment at least

\[
\boxed{\rho Q/\mu.}
\]

### Proof

If no fibre exceeds `mu`, apply RI5ce. Resource-disjointness prevents reuse of any capacity-one resource. Sum the assumed per-record payment. QED.

## RI5cg -- complete conflict-resource router -- PROVED UNDER THE RESOURCE CONTRACT

For a requested `q`-component bank, finite conflict-label dictionary of size `K`, optional sublabel dictionary of size `R`, and resource threshold `mu`, one exact continuation holds:

1. a physical RI bank of size at least `q` exists;
2. one resource occurs in more than `mu` records of one heavy conflict class;
3. one resource-disjoint stock has weight at least
   \[
   \boxed{
   \frac{W}{(q-1)(K+1)R\mu}
   }
   \]
   with `R=1` when no sublabel refinement is used;
4. that stock pays with the efficiency declared in RI5cf;
5. or one conflict record lacks a fixed label, sublabel, resource, occurrence, owner or weight field.

### Proof

RI5ca--RI5cb give a conflict class of weight at least `W/((q-1)(K+1)R)`. Apply RI5cf to that class. QED.

## Corrected RI6 frontier

The graph failure branch now yields either a high-multiplicity physical resource or a capacity-one resource-disjoint stock with an explicit retained fraction. Remaining work is to prove useful resource multiplicity and payment-efficiency bounds for the actual conflict labels, together with repeated-coset correlations, blocker repair and replenishable-source recurrence.

## Finite check

`scripts/verify_ri_conflict_resource_capacity.py` enumerates finite weighted resource fibres, verifies the maximum-representative bound and checks the composed RI fraction.