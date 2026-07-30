# Exact p=31 switch-tail extension from six triples to four

## Status

This note keeps AC as the sole active research track and proves AC5nx--AC5ob. It extends the explicit `p=31`, `n=30` trajectory of AC5nt--AC5nw from six real collinear-triple occurrences to four.

All paths use legal two-row switches in one of two disjoint permutation layers. The new results are exact finite switch-graph statements for the displayed physical states. They do not yet provide a zero-triple configuration on the `30 by 30` board.

## AC5nx -- exact barrier ten from six triples to five -- PROVED

Let `v_6` be the six-triple state of AC5nv. Its complete components at barriers `6,7,8,9` contain respectively

\[
1,\quad 9,\quad 33,\quad 860
\]

states, and none contains a state of potential below six.

The 26-switch path stored in `data/ac-p31-exact-tail-extension.json` has exact potential word

\[
6,7,7,8,10,10,10,9,9,10,7,9,10,8,10,10,9,10,10,9,9,8,10,9,8,8,5.
\]

Therefore

\[
\boxed{\mathcal B(v_6)=10}.
\]

The exact barrier-ten search processed 65,864 accepted states and discovered 75,944 sublevel states before returning the path.

### Proof

The lower bound is the complete barrier-nine component exhaustion from AC5nv. Direct replay proves every stored switch is legal and the maximum potential is ten. The endpoint has potential five. QED.

## AC5ny -- exact barrier ten from five triples to four -- PROVED

At the resulting five-triple state `v_5`, the complete lower components at barriers `6,7,8,9` have sizes

\[
2,\quad18,\quad68,\quad501.
\]

None contains a state of potential below five.

The stored 32-switch path has exact potential word

\[
5,7,10,10,9,10,9,10,9,10,10,9,10,10,10,9,10,10,8,10,8,10,10,10,10,9,10,7,10,10,10,8,4.
\]

Hence

\[
\boxed{\mathcal B(v_5)=10}.
\]

The exact barrier-ten search processed 182,765 accepted states and discovered 223,691 sublevel states before returning the path.

### Proof

Complete barrier-nine enumeration proves the lower bound. Replay of the displayed switch word proves a barrier-ten upper path ending at potential four. QED.

## AC5nz -- cumulative explicit p=31 trajectory to four triples -- PROVED

The AC5nt path uses 154 switches from the strongest AN successor at potential 75 to `v_6`. Appending AC5nx and AC5ny gives

\[
\boxed{154+26+32=212}
\]

legal switches from potential 75 to potential four.

The four remaining triples are exactly

\[
\begin{aligned}
&\{(2,15)_r,(6,18)_r,(22,30)_r\},\\
&\{(4,9)_r,(10,13)_r,(22,21)_b\},\\
&\{(21,5)_r,(26,3)_r,(11,9)_b\},\\
&\{(1,12)_b,(4,18)_b,(9,28)_b\}.
\end{aligned}
\]

Thus the endpoint retains a complete occurrence-faithful four-certificate core rather than an anonymous potential value.

## AC5oa -- exact lower barrier at the four-triple checkpoint -- PROVED

Let `v_4` be the endpoint of AC5ny. Its complete sublevel components have sizes

\[
\begin{array}{c|ccccc}
\text{barrier}&5&6&7&8&9\\\hline
\text{states}&2&10&29&286&2033.
\end{array}
\]

None contains a state of potential below four. Consequently

\[
\boxed{\mathcal B(v_4)\ge10}.
\]

This lower bound is exact finite enumeration, not a failed heuristic search.

## AC5ob -- fail-closed barrier-ten continuation -- PROVED

A resumable exact breadth-first traversal of the barrier-ten component above `v_4` has been constructed. At the committed checkpoint it had

- processed states: `293,150`;
- accepted barrier-ten states: `338,944`;
- active queue states: `45,794`;
- state below four found: no.

The traversal was incomplete at that checkpoint. Therefore no claim is made that barrier ten is impossible, and no lower bound beyond AC5oa is inferred from the partial search.

Every accepted state retains its exact predecessor and switch address, so a future lower endpoint yields a replayable path immediately. Completion without such an endpoint would prove the barrier exceeds ten.

## Deterministic audit

Compile and run:

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_exact_tail_extension.cpp -o verify_p31_tail
./verify_p31_tail
```

The verifier reconstructs the six-triple state, replays all 58 new switches, recomputes every stored potential, and independently enumerates the complete lower components at the five- and four-triple checkpoints.

Expected ledger:

- six-to-five switches: `26`;
- six-to-five maximum potential: `10`;
- five-to-four switches: `32`;
- five-to-four maximum potential: `10`;
- five-checkpoint lower components: `2,18,68,501`;
- four-checkpoint lower components: `2,10,29,286,2033`;
- extension switches: `58`;
- cumulative switches from the AN successor: `212`;
- final potential: `4`.

## Remaining AC frontier

1. Complete the exact barrier-ten component above `v_4` or extract its first three-triple path.
2. Continue the exact minimax tail through three, two, one and zero triples.
3. Classify the four current certificate lines by carry, denominator, owner and repair-source fields.
4. Compare the `p=31` low-potential barriers with the completed `p=19` path and extract a uniform local repair template.
5. Extend the seed and terminal-manifest construction beyond the currently tested primes.

AC6 and the general no-three-in-line conjecture remain open.
