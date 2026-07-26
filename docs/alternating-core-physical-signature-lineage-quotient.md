# Finite physical-signature quotients for symbolically unbounded owner lineages

**Branch:** `research/alternating-core-chain`

AC3ou--AC3oy treat a finite occurrence-lineage graph.  A registry may nevertheless
manufacture arbitrarily many symbolic aliases for the same bounded physical owner.
That symbolic infinity is harmless only when identity, currentness and continuation
factor through one finite reconstructed physical signature.

This note gives the exact quotient.  Every certified alias path projects to a finite
signature path and has one canonical first false-to-true quotient edge.  Quotient
capacity must be shared by all aliases.  Symbolic names which do not project to a
registered continuation edge remain owner replacement rather than recreation.

## Physical signature quotient

Let `V_tilde` be a possibly unbounded set of symbolic owner occurrences.  Let

`Sigma`

be a finite set of reconstructed physical owner signatures and let

`sigma:V_tilde->Sigma`

be the canonical signature map.  A signature retains the physical owner kind,
bounded support, arithmetic decoration, registry role and every multiplicity field
which affects payment.

Assume currentness factors through signatures:

`h_tilde(v)=h_Sigma(sigma(v))`.

Every certified symbolic continuation edge `v->v'` has one exact continuation kind
`kappa` and projects to a declared directed signature edge

`(sigma(v),sigma(v'),kappa)`.

Write `D_Sigma` for the resulting finite directed signature graph.

## AC3oz -- quotient-faithful identity wall -- PROVED

A symbolic occurrence change is a same-owner continuation in the quotient exactly
when its registry witness projects to a declared edge of `D_Sigma` with the recorded
continuation kind.

If no such projected edge is registered, the target occurrence is owner replacement
or new-owner creation.  Equality of symbolic names or equality of physical support
alone does not authorize reuse of old-owner payment.

### Proof

The quotient contract defines continuation by the reconstructed signature edge and
its kind.  A registered projected edge is therefore sufficient.  Without it there
is no occurrence-faithful datum joining the two owner states; support equality may
join different capacities, phases or registry roles. QED.

## AC3pa -- every quotient-faithful return has a canonical signature boundary -- PROVED

Let

`v_0,v_1,...,v_m`

be a certified symbolic lineage path with `h_tilde(v_0)=0` and
`h_tilde(v_m)=1`.  Its projected signature path has one unique first index `j` such
that

`h_Sigma(sigma(v_(j-1)))=0`

and

`h_Sigma(sigma(v_j))=1`.

The exact projected edge, together with its continuation kind, is the canonical
physical-signature recreation gate.

### Proof

Currentness factors through `sigma`, so the projected truth word begins with zero
and ends with one.  Choose the least index with value one.  Minimality gives zero
immediately before it and uniqueness of the index. QED.

Different alias paths may share the same quotient gate.  They must therefore share
its capacity rather than receiving separate alias tickets.

## AC3pb -- finite and polynomial quotient-gate stock -- PROVED

Let `S=|Sigma|`, let `K_sig` be the number of continuation kinds and let
`d_sig` be the maximum outdegree in the kind-decorated signature graph.  The exact
gate stock satisfies

`E_sig <= |E(D_Sigma)| <= K_sig*S*d_sig`

and the safe complete-pair bound

`E_sig <= K_sig*floor(S^2/4)`

for false-to-true gates.

If signatures satisfy the AC3lt bounded-support contract, then

`S <= N_own`

and hence the safe stock is at most

`K_sig*floor(N_own^2/4)`.

### Proof

Every canonical gate is a declared kind-decorated edge from a false signature to a
true signature.  Count legal edges, or count at most `d_sig` targets for each source
and kind.  The complete false/true product is maximized by a balanced partition.
AC3lt bounds the reconstructed physical signature universe. QED.

Thus an unbounded symbolic namespace does not enlarge the recurrence alphabet when
all payment-relevant data factor through bounded physical signatures.

## AC3pc -- shared quotient capacities bound all alias returns -- PROVED

Give each exact signature gate `a` an integer capacity `c_sig(a)`.  Every symbolic
alias return charged to `a` consumes one unit of this common capacity, and no unit is
restored inside the quotient epoch.

Then the number of charged symbolic recreation episodes is at most

`C_sig=sum_a c_sig(a)`.

For a weighted family of symbolic returns of total weight `W`, one exact signature
gate carries weight at least

`W/E_sig`.

### Proof

AC3pa maps every symbolic return to one quotient gate.  All aliases using that gate
consume the same stock, so the total number of charges is bounded by the initial
capacity sum.  Weighted pigeonhole over the finite gate set gives the localization
statement. QED.

Alias-specific capacities would be invalid here: arbitrarily many fresh names could
otherwise recreate an arbitrarily large ticket stock over one physical owner.

## AC3pd -- closure under the physical-signature quotient -- PROVED UNDER THE SIGNATURE-QUOTIENT CONTRACT

Inside one quotient epoch assume:

1. every symbolic occurrence has a canonical payment-complete signature in `Sigma`;
2. currentness and certified continuation factor through `sigma` and `D_Sigma`;
3. multiplicity affecting payment is included in the signature or represented by a
   finite additive capacity vector;
4. every false-to-true signature gate is impossible, terminal/improving, strictly
   descending, or consumes finite unrestorable shared quotient capacity;
5. leaving the reconstructed signature universe is recorded as a higher outer reset.

Then symbolically unbounded alias creation cannot sustain an infinite nonterminal
same-owner recreation history inside the quotient epoch.

### Proof

AC3pa gives every certified return one finite quotient gate.  AC3pb gives a finite
gate stock.  Route 4 and the other closing routes bound or eliminate each gate;
route 5 exits the epoch.  Alias creation produces no new gate or capacity because
AC3pc aggregates all aliases at the physical signature.  Recreation-free segments
are bounded by AC3nz. QED.

## Corrected AC4 owner frontier

Symbolically unbounded occurrence registries are no longer automatically an
obstruction.  They close whenever they are aliases of a finite payment-complete
physical signature quotient.

The remaining owner frontier is now genuinely physical:

- unbounded support, arithmetic decoration or payment-relevant multiplicity;
- continuation/currentness which does not factor through reconstructed signatures;
- quotient capacities which can themselves be recreated;
- nonadditive owner resources and unresolved availability, conflict, reverse and
  arithmetic macro-cycle interactions.

## Finite check

`scripts/verify_ac_physical_signature_lineage_quotient.py` exhausts small finite
signature graphs with arbitrarily repeated aliases.  It checks projection-faithful
identity, the canonical first signature boundary, legal-edge/product/outdegree
bounds, weighted localization and shared-capacity accounting across aliases.