# Payment-safe provenance of saturated hard literals

**Branch:** `research/alternating-core-chain`

AC3li--AC3lm split every saturated noncurrent phase literal into an active
current-context blocker or a latent dependency record.  The remaining local
frontier is not merely to attach an arithmetic name.  A forbidden phase,
carry, BDA, RI or protected pattern containing the noncurrent source literal
is absent from the current state and is therefore prospective geometry.  It
can be a hard obstruction, but it is not destroyed current payment.

This note gives every active or latent literal one finite provenance word and
applies the transition-relative owner registry.  It also audits fixed-registry
dependency cycles: the hard checks on their edges contribute zero payment by
themselves, while any separate current owners are counted once by exact token
identity.

## Saturated literal records

Let

\[
\omega\in\prod_{x\in V}\mathcal A_x
\]

be the current hard-feasible phase assignment.  A canonical saturated-literal
record consists of:

- a block `x`;
- a noncurrent phase `b != omega_x`;
- the least exact hard check
  \(C=(S_C,f_C)\) with `x in S_C` and `f_C(x)=b`;
- the residual mismatch set
  \[
  D_{x,b}
  =
  \{(y,f_C(y)):
    y\in S_C\setminus\{x\},\ f_C(y)\ne\omega_y\}.
  \]

Hard rank at most three gives `|D_{x,b}|<=2`.  The record is active when this
set is empty and latent otherwise.  A latent record retains its least mismatch
literal as the canonical dependency, as in AC3li.

Give every exact hard check one declared provenance kind.  The installed
registry uses the following seven coarse families:

1. canonical phase;
2. carry or arithmetic-capacity condition;
3. BDA geometry;
4. RI/OP geometry;
5. protected-bank condition;
6. mask, reverse-ticket or finite capacity condition;
7. unowned hard literal.

The exact check identifier, physical addresses, arithmetic decorations and
optional owner token are retained separately.  The seven-family list is a
registry interface, not a claim that an undeclared hard condition belongs to
one of these names.  Any additional hard-check builder must add its own
provenance kind.

## AC3ln -- every noncurrent hard pattern is prospective -- PROVED

For every saturated-literal record,

\[
\boxed{f_C\ne\omega|_{S_C}.}
\]

Consequently the forbidden pattern represented by `C` is absent from the
current phase state.  This holds for both active and latent records.

Therefore:

1. the phase/carry/BDA/RI/protected formula of `C` contributes zero certified
   destroyed payment by itself;
2. an active record is an immediate current-context hard obstruction, not a
   current certificate;
3. a latent record is an exact prospective dependency, not a deferred paid
   token;
4. payment is available only from a separate current owner satisfying AC3jw
   and the transition-relative registry AC3ke--AC3kh.

### Proof

The source literal satisfies

\[
f_C(x)=b\ne\omega_x.
\]

Thus the forbidden assignment differs from the current assignment at `x`,
regardless of its residual literals.  A current paid certificate or resource
pattern must be present in the parent state, so the target-containing pattern
cannot itself be destroyed current payment.  AC3jw gives the exact criterion
for a separate owner. QED.

This is the phase-literal analogue of AC3jv's absent blocker-cell theorem.

## Finite provenance words

Assume there are at most `q` ordered hard-check kinds, at most `K_prov`
provenance kinds and hard rank at most three.  Give an active or latent record
the word

\[
(\operatorname{kind}(C),
 \operatorname{prov}(C),
 s,i,
 \eta,
 \operatorname{route}),
\]

where:

- `s=|S_C|`;
- `i` is the source-literal position in the ordered scope;
- `eta` is the binary residual mismatch word on the other `s-1` positions;
- `route` is one of the six AC3jz owner routes:
  `PAID`, `FIXED_CURRENT`, `PROSPECTIVE`, `OCCURRENCE_FAILURE`,
  `COHERENCE_MISMATCH`, `OWNER_RESET`.

For a latent word the selected dependency position is determined by `eta` and
the fixed scope order.  Exact source/dependency addresses and owner identity
are not suppressed by this coarse word.

## AC3lo -- finite provenance-role dictionary -- PROVED

The rank/source/mismatch part has size

\[
\sum_{s=1}^{3}s2^{s-1}=17.
\]

Hence the provenance-role alphabet satisfies

\[
\boxed{
R_{\rm prov}
\le
6K_{\rm prov}q
\sum_{s=1}^{3}s2^{s-1}
=
102K_{\rm prov}q.
}
\]

For the seven installed provenance families,

\[
\boxed{R_{\rm prov}\le714q.}
\]

### Proof

For rank `s`, choose the source position in `s` ways and the mismatch subset of
the remaining positions in `2^(s-1)` ways.  Multiply the sum by the hard kind,
provenance kind and six owner-route choices. QED.

The role word is deliberately finite and local.  It does not merge exact
checks, physical literals, owners, scales or contexts needed by a recurrence
or payment theorem.

## AC3lp -- payment-safe provenance routing -- PROVED

Attach to every record and proposed transition its optional separate owner and
the exact AC3jz route.  Then the following routes are exhaustive.

1. **PAID.**  A separate owner is current, physical, coherent and actually
   destroyed or consumed by the proposed transition.  Its weight is counted by
   AC3w, once for a shared owner and additively only for private disjoint owners.
2. **FIXED_CURRENT.**  A current owner remains present.  It may protect or block
   the transition but contributes no destroyed payment to that transition.
3. **PROSPECTIVE.**  The hard pattern is physically meaningful but absent from
   the current state.  It remains in the active/latent literal router with zero
   payment.
4. **OCCURRENCE_FAILURE.**  The declared phase, carry, radial, coset or protected
   geometry is not physically realized.
5. **COHERENCE_MISMATCH.**  Physical witnesses exist but disagree on their
   scale, anchor, context or owner interpretation.
6. **OWNER_RESET.**  The transition-relative owner interpretation changes and
   is recorded as a decorated AC3ka outer edge.

In particular:

- a carry formula is paid only through a separate current carry/capacity token
  with an explicit consumption contract;
- a BDA literal is paid only through a separate occurrence-faithful current
  radial owner;
- an RI literal may determine a physical scale but is paid only through a
  separate movable or closed-bank owner satisfying the corresponding theorem;
- a protected literal is paid only when a distinct current protected/capacity
  token is consumed;
- an unowned literal remains unpaid.

### Proof

AC3ln removes payment from the forbidden pattern itself.  AC3jw gives the
separate-owner charging criterion, and AC3jz proves that the six status routes
are exhaustive.  AC3w supplies exact shared/private owner accounting. QED.

## AC3lq -- weighted role and owner localization -- PROVED

Give active and latent saturated-literal records nonnegative incidence weights
with total `W`.  Some provenance role carries weight at least

\[
\boxed{W/R_{\rm prov}.}
\]

Inside the retained role:

1. active records form a role-pure current-context hard-target family;
2. latent records push their incidence to one exact selected dependency
   literal;
3. for every threshold `Delta>0`, either one exact dependency or owner token
   receives load greater than `Delta`, or at least
   \[
   \boxed{
   \left\lceil
   \frac{W}{R_{\rm prov}\Delta}
   \right\rceil
   }
   \]
   distinct dependency or owner addresses receive positive load;
4. the owner-route label is retained throughout, so prospective incidence is
   never converted into paid weight by pigeonholing.

### Proof

Pigeonhole the total weight over the finite role alphabet.  Push every record
in the retained class to its exact dependency or owner address.  If every
address has load at most `Delta`, carrying the retained total requires the
displayed number of distinct addresses.  AC3lp preserves the payment route.
QED.

## Dependency-cycle payment audit

Let

\[
\gamma=(\ell_0,\ell_1,\ldots,\ell_{d-1},\ell_0)
\]

be one canonical latent dependency cycle in the fixed-registry graph of AC3lk.
Each edge is selected from one exact hard check.  The cycle is a static hard
registry object; it need not be an executable sequence of phase changes.

When a separate theorem realizes a transition sequence associated with
`gamma`, attach the transition-relative owner record to every used edge.  Let
`D_gamma` be the set of distinct owner tokens whose edge records are `PAID`
and which the realized sequence actually destroys or consumes.

## AC3lr -- exact dependency-cycle payment ledger -- PROVED

For every fixed-registry dependency cycle:

1. its target-containing hard-check patterns contribute zero destroyed payment;
2. the exact certified owner payment of a realized sequence is
   \[
   \boxed{w(D_\gamma),}
   \]
   with every shared owner counted once;
3. repeated use of one owner on several cycle edges does not multiply payment;
4. if `D_gamma` is empty, the cycle remains unpaid and can enter AC3lc only
   through strict bounded descent, physical impossibility or a separately proved
   capacity-one cycle ticket;
5. owner occurrence, coherence or route changes are decorated outer resets,
   not hidden progress inside the same cycle.

### Proof

Item 1 is AC3ln edge by edge.  The owners in `D_gamma` are current paid tokens
under AC3lp.  AC3w counts the weighted union of distinct paid tokens, which
proves items 2 and 3.  If the union is empty, no certified destroyed owner
exists; AC3lc lists the remaining valid cycle-progress alternatives.  AC3kh
handles route changes. QED.

## Polynomial literal-dependency decoration stock

Let `U` be the number of exact noncurrent literal addresses.  Use one formal
sink `ACTIVE` for active records.  A decorated record consists of:

- one source literal in `U`;
- one target in `U union {ACTIVE}`;
- one provenance role.

## AC3ls -- polynomial saturated-literal decoration bound -- PROVED

The ambient stock of decorated active/latent records is at most

\[
\boxed{
N_{\rm sat}
\le
R_{\rm prov}U(U+1).
}
\]

With the seven installed provenance families and a two-layer O1 registry,
`U<=2n^2`, so

\[
\boxed{
N_{\rm sat}
\le
714q(2n^2)(2n^2+1)
=
O(qn^4).
}
\]

The actual canonical dependency graph in one fixed registry still has at most
`U` edges and at most `floor(U/2)` cycles by AC3ll.  The larger display is a
safe cross-registry decoration dictionary before exact source/target
compatibility is imposed.

### Proof

Choose the source, the dependency or active sink, and the role word.  Apply
AC3lo and the O1 phase-address bound. QED.

This bounds the active/latent literal contribution to the AC3ka outer
decoration alphabet.  Denominator, owner-token identity, protected-contract
and envelope alphabets still require their own bounds.

## Consequence

The saturated-literal frontier now has a payment-safe exact dictionary.

- Active literals are current-context hard obstructions but their forbidden
  patterns are prospective.
- Latent literals are exact prospective dependency edges.
- A separate current owner may pay only through its transition-relative
  destruction contract.
- Fixed-registry dependency cycles carry no automatic payment.
- The role and literal-edge decoration stocks are polynomial under the declared
  physical O1 hard registry.

The remaining arithmetic work is edge-specific: classify which phase, carry,
BDA, RI or protected records have a separate current owner, prove its actual
transition destruction, or supply descent, impossibility or a capacity-one
cycle ticket.

## Finite check

`scripts/verify_ac_saturated_literal_provenance.py` exhausts canonical rank-at-
most-three hard checks on small phase systems, confirms that every noncurrent
hard pattern is prospective, checks the `17`, `102Kq` and `714q` role bounds,
audits the six owner routes, verifies weighted dependency/owner localization,
checks duplicate-owner accounting on dependency cycles and verifies the
polynomial decoration stock.