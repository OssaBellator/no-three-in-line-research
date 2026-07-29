# Resource-capacity routing for labeled source-hole stars

**Branch:** `research/superregular-resampling`

SRR2as--SRR2av reduce excessive low-cost hole mass to one source and one physical cause. This note extracts an independently payable resource stock inside that labeled star.

Fix a returned source-cause star `C`, consisting of endpoint records `b` with weights `lambda_b`, and write

\[
Q_C=\sum_{b\in C}\lambda_b.
\]

Assign every endpoint record one least physical payment resource `r(b)`. Resources may be blocker occurrences, protected cells, line certificates, owners, boundary slots or context records.

## SRR2aw -- exact star-resource partition -- PROVED

For each resource `r`, let

\[
C_r=\{b\in C:r(b)=r\}.
\]

The nonempty fibres partition `C`, and

\[
\boxed{Q_C=\sum_r\sum_{b\in C_r}\lambda_b.}
\]

### Proof

Every endpoint record has exactly one least resource, hence belongs to exactly one fibre. QED.

## SRR2ax -- distinct-resource endpoint stock -- PROVED

Suppose every resource fibre contains at most `mu` endpoint records. Choose a maximum-weight endpoint `b_r` from every nonempty fibre. Then the chosen endpoints use pairwise distinct resources and

\[
\boxed{
\sum_r\lambda_{b_r}\ge \frac{Q_C}{\mu}.
}
\]

### Proof

For each fibre, its total weight is at most `mu` times its maximum endpoint weight. Sum over resources. QED.

## SRR2ay -- star payment or resource overload -- PROVED

For every `mu>=1`, one exact alternative holds:

1. one payment resource occurs in more than `mu` endpoint records of the labeled source star;
2. a distinct-resource endpoint stock has weight at least `Q_C/mu`.

If every selected endpoint realizes payment at least `rho lambda_b`, branch 2 realizes total payment at least

\[
\boxed{\rho Q_C/\mu.}
\]

### Proof

If no resource fibre is overloaded, apply SRR2ax. Distinct resources make capacity-one charging valid. QED.

## SRR2az -- complete labeled-star capacity router -- PROVED UNDER THE RESOURCE CONTRACT

Let the complete weighted threshold hole mass be `mathcal M_S`, let the cause dictionary have size `K`, and choose resource multiplicity threshold `mu`. One exact continuation holds:

1. trimmed low-cost flow succeeds with the previous Hall-deficiency and exceptional-weight bounds;
2. one source-cause star contains a resource used more than `mu` times;
3. one distinct-resource endpoint stock has weight at least
   \[
   \boxed{
   \frac{\mathcal M_S}{|A|K\mu}
   }
   \]
   and may be paid independently;
4. if exceptional endpoint weight exceeds `Lambda` at threshold `tau`, the selected stock has weight greater than
   \[
   \boxed{
   \frac{(\tau+1)\Lambda}{|A|K\mu};
   }
   \]
5. or one cause, resource, occurrence, conditioning or endpoint-weight record is not fixed.

### Proof

SRR2at gives a source-cause star of weight at least `mathcal M_S/(|A|K)`, and SRR2au gives the exceptional-budget form. Apply SRR2ay. QED.

## Corrected SRR3 frontier

A heavy labeled source-hole star now yields either one overloaded physical resource or a distinct-resource endpoint stock with an explicit retained fraction. Remaining work is to prove actual resource multiplicity and per-resource payment efficiencies for bounded-cycle switching menus, or pay the overloaded resource directly.

## Finite check

`scripts/verify_srr_source_star_resource_capacity.py` enumerates weighted source-star resource fibres and checks the representative-stock and composed concentration bounds.