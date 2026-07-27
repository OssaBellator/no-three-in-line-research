# Bounded-state quotient for affine phase memory

**Branch:** `research/alternating-core-chain`

AC3rz--AC3sd remove chronological order from a mixed-centre affine family modulo the gcd of
its pair-swap defects.  The remaining ledger still records an unbounded count vector and one of
finitely many exact lifts.  In a physically bounded epoch, however, neither field is an independent
state variable when future legality depends only on the current decorated phase state and current
memory value.

This note makes that quotient explicit.  The bounded mixed-centre branch becomes one finite directed
state graph.  Every recurrent history contains a short exact affine return word, and the count ledger
is retained only as an optional proof annotation rather than as payment-relevant state.

## State-Markov contract

Fix one affine epoch.  Let `X` be the finite set of decorated physical phase states and let

`L<=h<=U`

be the physical integer memory range.  Put

`R=U-L`.

Let `Lambda={1,...,s}` be the fixed affine address alphabet.  Address `lambda` has update

`h -> A_lambda*h+B_lambda`

and a declared phase update on `X`.

Assume the **state-Markov contract**:

1. legality of an address depends only on the current pair `(x,h)` and the address;
2. the resulting next state depends only on the same data;
3. terminal classification and payment-relevant continuation data depend only on `(x,h)`;
4. the accumulated count vector, residue affine map and chronological order-lift label are not
   separately inspected by future transitions;
5. changing any of these rules is an outer reset.

The theorem does not erase a genuinely history-sensitive field.  Such a field violates item 3 or 4
and remains an explicit AC4 residual.

## AC3se -- count ledgers are historical annotations -- PROVED

Under the state-Markov contract, two histories ending at the same exact pair

`(x,h)`

have identical legal next-address sets, identical next-state maps and identical terminal
classification.

Consequently the accumulated affine count vector, the residue map modulo the pair-defect gcd and the
exact chronological lift may be removed from the live state representation.

### Proof

Every legal and terminal query is, by contract, a function of `(x,h)` and the proposed next address.
Therefore equal current pairs give equal answers and equal successors.  The historical ledgers may
still be stored as proof certificates, but they do not distinguish future behavior. QED.

This is a quotient-faithfulness statement.  It does not say that two histories have used the same
tickets; any ticket balance that affects future legality must be included in `X`.

## AC3sf -- exact bounded affine state stock -- PROVED

The number of live exact states is at most

`N_aff=|X|*(R+1)`.

This bound is independent of:

- the affine address count vector;
- the pair-defect gcd `g`;
- the number of chronological orderings of one count vector;
- and the absolute number of completed phase cycles before the current state.

### Proof

There are `|X|` choices for the decorated physical phase state and exactly `R+1` integer values in
`[L,U]`.  AC3se removes every other history-only field. QED.

The finer `floor(R/g)+1` lift bound from AC3sc remains valid inside one count ledger, but the complete
state stock is already bounded by `N_aff`.

## AC3sg -- canonical simple affine return word -- PROVED

Every internal history containing at least `N_aff` transitions has a repeated exact state.  Choose
the least ending time at which a state repeats and the unique earlier occurrence of that state.
The intervening segment is a simple directed cycle of length at most

`N_aff`.

Let its affine word be `w`, with exact map

`F_w(h)=A(w)h+B(w)`.

If the repeated state has memory value `h_0`, then

`(A(w)-1)h_0+B(w)=0`.

Hence:

1. if `A(w)=1`, then `B(w)=0`, so the return word is an exact identity translation at `h_0`;
2. if `A(w)!=1`, then the return value is the unique rational fixed point

   `h_0=B(w)/(1-A(w))`.

### Proof

A history with `N_aff` transitions visits `N_aff+1` states, so AC3sf and pigeonhole give a repeated
state.  The least-ending choice has no repeated interior state and therefore is a simple cycle.  Its
length is at most the total state stock.  Exact return gives

`A(w)h_0+B(w)=h_0`,

which rearranges to the displayed equation and the two cases. QED.

The fixed-point formula is an exact return test, not an assertion that every rational fixed point is
physically legal.

## AC3sh -- finite simple-cycle address dictionary -- PROVED

Let `s=|Lambda|`.  The number of possible nonempty affine address words of length at most `N_aff` is
at most

`C_aff=sum_(ell=1)^(N_aff) s^ell`.

Every canonical recurrent simple cycle from AC3sg has one address in this finite dictionary.

If a cycle ticket also records its initial exact state, the complete state-cycle ticket stock is at
most

`N_aff*C_aff`.

### Proof

For each length `ell`, there are at most `s^ell` address words.  AC3sg bounds the length of a
canonical simple return by `N_aff`.  Multiplying by the possible initial states gives the decorated
ticket stock. QED.

Many words are illegal or fail the return equation, so the displayed stock is safe rather than
sharp.

## AC3si -- bounded affine epoch router -- PROVED UNDER THE STATE-CYCLE CONTRACT

Assume every canonical simple return from AC3sg is one of:

1. quotient-stuttering and erasable;
2. strictly descending in a declared well-founded rank;
3. charged to a finite ticket of its exact state-cycle address;
4. impossible under the physical phase contract;
5. or an outer reset.

Then one bounded affine epoch has no infinite nonterminal internal history.

More precisely, after removing or paying all completed simple cycles, every residual cycle-free
segment has fewer than `N_aff` transitions.

### Proof

An infinite history in the finite exact state graph must contain infinitely many repeated states.
AC3sg extracts a canonical simple cycle whenever a repeat first occurs.  Each extraction erases the
cycle, decreases a rank, spends a finite ticket or exits the epoch.  None can happen infinitely often
inside one fixed contract.  A segment with no repeated state visits at most `N_aff` states and
therefore has fewer than `N_aff` transitions. QED.

## Corrected AC4 phase-memory frontier

For physically bounded scalar-affine memory, the mixed-centre count ledger and exact lift are no
longer separate recurrence obstructions.  Under the state-Markov contract they quotient to the
finite exact state `(x,h)`, and every recurrence is one short exact affine return word.

The remaining affine frontier is now:

- unbounded physical memory without a common rank;
- ticket-sensitive or payment-sensitive history fields omitted from `X`;
- unticketed simple state cycles;
- genuinely nonlinear or non-Markov path memory;
- and changes of law not declared as outer resets.

Fresh or recreated weighted capacity, nonadditive outputs, unpaid loss and the other AC4 interfaces
remain unchanged.

## Finite check

`scripts/verify_ac_bounded_affine_state_quotient.py` exhausts small decorated memory intervals and
small integer-affine address families, then samples legal histories.  It checks the exact
`|X|(R+1)` stock, state-Markov continuation equality, least-ending simple-cycle extraction, the
affine return equation, the identity-translation case and the cycle-free path bound.
