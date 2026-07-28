# Holonomy-aware physical residual product

**Branch:** `research/orbit-phase-expansion`

OP4ad--OP4ah compress source-coset cycle shifts to component holonomies, while OP4ai--OP4am give a complete finite quotient for bounded blocker fibres and action kernels.  This note combines the two interfaces.  Nonzero holonomy supplies an exact finite quotient orbit before any physical recurrence can occur; at the first quotient return, the remaining recurrence is purely physical and exposes the bounded restoration gate.

The holonomy statements are imported under the normalized source-coset contract.  A changed subgroup, component decomposition, physical dictionary or action kernel is an outer reset.

## Simultaneous component holonomy

Suppose the residual has cycle components indexed by `j=1,...,c`.  Component `j` has shift group `Z/h_j Z` and holonomy `omega_j`.  Define

\[
o_j=
\begin{cases}
1,&\omega_j=0,\\
h_j/\gcd(h_j,\omega_j),&\omega_j\ne0,
\end{cases}
\]

and put

\[
L_\Omega=\operatorname{lcm}(o_1,\ldots,o_c),
\]

with `L_Omega=1` when there is no cycle component.

## OP4an -- exact simultaneous holonomy order -- PROVED

After `r` traversals of the same normalized component word, every quotient cycle coordinate returns exactly when

\[
r\equiv0\pmod{o_j}
\]

for every `j`.  The least positive simultaneous return time is

\[
\boxed{L_\Omega.}
\]

### Proof

Component `j` has displacement `r omega_j` after `r` traversals, so it returns exactly when `h_j` divides `r omega_j`, equivalently when `o_j` divides `r`.  The least positive integer divisible by every `o_j` is their least common multiple. QED.

## OP4ao -- product state stock -- PROVED

Let `K_phys` be the complete finite physical blocker/action/boundary state stock supplied by OP4ai.  For one fixed normalized component type and holonomy vector, the combined quotient--physical state stock is at most

\[
\boxed{K_{\rm phys}L_\Omega.}
\]

### Proof

Choose one of the `L_Omega` quotient orbit positions and one of the `K_phys` complete physical states.  Compatibility constraints only reduce the ambient product. QED.

The exact individual arc shifts need not be reintroduced unless ownership or legality depends on them; in that case they remain part of `K_phys`.

## OP4ap -- no complete recurrence before quotient return -- PROVED

If `1<=r<L_Omega`, the state after `r` repetitions cannot equal the initial complete quotient--physical state.

### Proof

By minimality of `L_Omega`, at least one component has `r omega_j != 0 mod h_j`.  Its quotient coordinate differs from the initial coordinate, irrespective of the physical state. QED.

Thus nonzero simultaneous holonomy supplies a strict finite phase clock rather than an unstructured recurrent blocker fibre.

## OP4aq -- first quotient return exposes a physical restoration gate -- PROVED UNDER THE COMPLETE-PHYSICAL-STATE CONTRACT

At repetition `L_Omega`, all normalized quotient cycle coordinates return.  If the complete physical state also returns and the combined cycle is nonconstant, then OP4ak supplies a canonical first blocker, variable, factor or boundary restoration gate.

For a zero-holonomy vector, `L_Omega=1`, so the same physical restoration conclusion applies after one traversal.

### Proof

OP4an gives exact quotient return at `L_Omega`.  The remaining coordinates are precisely the complete finite physical state of OP4ai.  A nonconstant exact return in that finite product uses the canonical hierarchy of OP4ak. QED.

## OP4ar -- holonomy-aware bounded residual router -- PROVED UNDER THE NORMALIZED-HOLONOMY CONTRACT

Every bounded source-coset residual cycle has one continuation:

1. a nonzero holonomy vector advances through a finite exact quotient orbit of length `L_Omega`;
2. before that orbit closes, exact recurrence is impossible by OP4ap;
3. at the first quotient return, nonconstant physical recurrence exposes the canonical restoration gate of OP4aq;
4. the selected gate gives syndrome payment, completion/rank/carry descent, simultaneous repair, physical impossibility or a capacity-one restoration ticket;
5. a coherent fixed-edge class invokes the existing bank;
6. or the subgroup, component type, holonomy, physical dictionary, owner, action kernel, context or legality interpretation changes, giving an explicit reset.

Consequently bounded rank-three blocker fibres with nonzero holonomy are controlled by an exact finite phase clock, while zero-holonomy fibres reduce immediately to physical restoration.  Remaining OP5 work is arithmetic payment of the resulting exact fixed component classes and genuinely wide or dynamic action CSPs.

### Proof

Apply OP4an--OP4ap to the quotient orbit and OP4aq at its first return.  The declared physical continuations are those of OP4al--OP4am.  Contract changes are returned rather than silently identified. QED.

## Finite check

`scripts/verify_op_holonomy_physical_product.py` enumerates simultaneous holonomy vectors for small component groups, verifies the least-common-multiple return law, checks absence of earlier quotient return and audits the product-state count.