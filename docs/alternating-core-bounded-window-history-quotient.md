# Bounded-window quotient for path-dependent phase memory

**Branch:** `research/alternating-core-chain`

AC3se--AC3si close physically bounded scalar-affine memory whenever all payment-relevant future
behavior is Markov in the current decorated state and memory value.  A remaining natural exception is
bounded-delay path dependence: legality or the next update may inspect the last few phase events even
when it does not inspect the full history.

This note includes that retained suffix explicitly.  A fixed finite event alphabet and fixed window
length give one finite transducer state.  Every recurrence is again a short exact state cycle.  Only an
unbounded retained log, a changing event alphabet or a genuinely omitted history field remains outside
the quotient.

## Window model

Fix one epoch.  Let:

- `X` be the finite decorated physical phase-state set;
- `L<=h<=U` be a bounded integer memory range, with `R=U-L`;
- `Sigma` be a finite event-signature alphabet of size `s>=1`;
- `w>=0` be the maximum retained history length.

A live history window is a word

`eta in W_(<=w)=union_(j=0)^w Sigma^j`.

Its exact stock is

`Q_w=sum_(j=0)^w s^j`.

After an event `sigma`, update the window by appending `sigma` and retaining only the last `w`
symbols.  Denote this deterministic shift by

`eta' = sh_w(eta,sigma)`.

Assume the **bounded-window Markov contract**:

1. the next event signature is one of the fixed symbols in `Sigma`;
2. legality, the next physical state, the next memory value and terminal classification depend only
   on `(x,h,eta)` and the proposed event;
3. every ticket or payment balance that affects future legality is included in `x`, `h` or `eta`;
4. older history is never inspected directly;
5. changing `Sigma`, `w` or any transition law is an outer reset.

The update of `h` may be affine or non-affine.  Boundedness and finite-window dependence, not linearity,
are the hypotheses here.

## AC3sj -- exact suffix reconstruction -- PROVED

For every finite event history `v`, its live window is exactly the suffix of `v` of length
`min{w,|v|}`.

Consequently two histories with the same current `(x,h)` and the same last at most `w` event signatures
have identical future legal moves, successors and terminal classification.

### Proof

The shift rule appends each new symbol and deletes every symbol lying more than `w` positions behind
the current end.  Induction on the history length therefore leaves precisely the declared suffix.
The second statement is item 2 of the bounded-window Markov contract applied to equal live states.
QED.

The theorem does not identify histories whose older prefixes affect an omitted ticket or payment
balance.  Such a balance must be included in the decorated state.

## AC3sk -- finite augmented state stock -- PROVED

The complete live-state stock is at most

`N_win=|X|*(R+1)*Q_w`

with

`Q_w=sum_(j=0)^w s^j`.

This bound is independent of the total history length and of the number of times an event signature
has appeared before the retained window.

### Proof

There are `|X|` physical decorations, `R+1` integer memory values and `Q_w` retained suffixes.  AC3sj
removes every older event from the future-relevant state. QED.

For `w=0`, `Q_w=1` and this reduces to the exact-state stock in AC3sf.

## AC3sl -- canonical bounded-window return word -- PROVED

Every internal history containing at least `N_win` transitions repeats one exact augmented state
`(x,h,eta)`.  Choosing the least ending time at which a repetition occurs gives a simple directed
cycle of length at most `N_win`.

If the cycle event word is `v`, then

`sh_w(eta,v)=eta`.

Moreover, when `|v|>=w>0`, the returned window is forced by the cycle word:

`eta=suffix_w(v)`.

### Proof

The history visits `N_win+1` states, so AC3sk and pigeonhole give a repeat.  At the least ending repeat,
no interior state is repeated, hence the segment is a simple cycle and has length at most the state
stock.

Its event word carries the initial window to the final window, which is the same exact state, giving
the shift identity.  If `|v|>=w`, all symbols of the initial window have been shifted out, so the final
window consists exactly of the final `w` symbols of `v`. QED.

When `|v|<w`, the return identity is a finite periodic-overlap condition between `eta` and `v`; no
unbounded prefix information is required.

## AC3sm -- finite decorated return-address stock -- PROVED

The number of nonempty event words of length at most `N_win` is at most

`C_win=sum_(ell=1)^(N_win) s^ell`.

Every canonical simple recurrence has one address consisting of its initial augmented state and event
word.  Hence the complete state-cycle ticket stock is at most

`N_win*C_win`.

### Proof

There are at most `s^ell` event words of length `ell`, and AC3sl bounds a canonical simple cycle by
`N_win`.  Multiply the resulting word stock by the possible initial augmented states. QED.

Illegal words and words failing the exact return condition only reduce the true stock.

## AC3sn -- bounded-window history router -- PROVED UNDER THE WINDOW-CYCLE CONTRACT

Assume every canonical simple augmented-state return is one of:

1. quotient-stuttering and erasable;
2. strictly descending in a declared well-founded rank;
3. charged to one finite ticket of its exact state-cycle address;
4. impossible under the physical phase contract;
5. or an outer reset.

Then one fixed bounded-window epoch has no infinite nonterminal internal history.  After completed
simple cycles are erased or paid, every residual cycle-free segment has fewer than `N_win`
transitions.

### Proof

The augmented state graph is finite by AC3sk.  An infinite path in it repeats states infinitely often,
and AC3sl extracts a canonical simple cycle at every least-ending repeat.  Each extraction erases,
descends, spends a finite ticket or exits the epoch.  None can occur infinitely often under the stated
contract.  A path with no repeated augmented state visits fewer than `N_win+1` states. QED.

## Corrected AC4 phase-memory frontier

Fixed-delay path dependence is no longer a genuinely unbounded history obstruction.  A finite event
alphabet and retained window of length `w` enlarge the exact state stock only by

`Q_w=sum_(j=0)^w |Sigma|^j`.

The remaining path-memory frontier is:

- an unbounded retained event log or window length;
- a changing or physically unbounded event-signature alphabet;
- ticket, payment, owner or capacity fields omitted from the augmented state;
- unticketed simple augmented-state cycles;
- unbounded numerical memory without a common rank;
- and changes of transition law not declared as outer resets.

Fresh or recreated weighted capacity, nonadditive outputs, unpaid loss and the other AC4 interfaces
remain unchanged.

## Finite check

`scripts/verify_ac_bounded_window_history_quotient.py` exhausts small alphabets, windows and event
words, then samples finite decorated transducers.  It checks exact suffix reconstruction, the
`sum_(j=0)^w s^j` window stock, return-window identities, least-ending simple-cycle extraction and the
cycle-free path bound.