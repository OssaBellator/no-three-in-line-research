# Explicit p=19 no-three-in-line certificate

## Status

This note keeps AC as the sole active research focus and proves AC5nb--AC5ng. It completes the concrete `p=19`, `n=18` trajectory begun in AC5mp--AC5na. Starting from the two modular-hyperbola permutation layers, one alternating-star installation followed by a finite sequence of legal two-row switches reaches two disjoint permutation layers whose union has exactly 36 points and no real collinear triple.

This is an explicit certificate for the single board size `n=18`. It does not prove AC6, a uniform prime-minus-one theorem, or the no-three-in-line conjecture for all `n`.

## Move graph and checkpoint barriers

A state is an ordered pair `(R,B)` of disjoint permutation graphs on `[1,18]^2`. A legal move swaps the images of two rows in one layer and is admitted only when the two inserted cells avoid the opposite layer.

Let

\[
\Phi(R,B)
=
\sum_L\binom{|(R\cup B)\cap L|}{3}
\]

be the exact number of real collinear triple occurrences. For a state `v` and lower-potential target set `T`, define the switch barrier

\[
\mathcal B(v,T)
=
\min_{P:v\leadsto T}\max_{x\in P}\Phi(x).
\]

The finite exact searches below enumerate complete sublevel components, so their lower bounds are graph-theoretic exhaustion certificates rather than heuristic search failures.

## AC5nb -- exact barrier seven from five triples -- PROVED

Start at the five-triple state of AC5my. Its complete legal switch component inside

\[
\{v:\Phi(v)\le6\}
\]

contains exactly five states and none has potential below five.

The four legal switches

\[
r:(8,15),
\quad r:(13,15),
\quad b:(5,13),
\quad b:(11,13)
\]

have exact potential sequence

\[
\boxed{5,7,6,7,4.}
\]

Consequently

\[
\boxed{
\mathcal B(\Phi=5,\{\Phi<5\})=7.
}
\]

The same value is the exact barrier from this state to a zero-triple state, because the continuation below never exceeds six.

### Proof

Breadth-first enumeration of the barrier-six component gives the five-state exhaustion certificate. Direct replay verifies the four legal switches and the displayed potentials. The later certified path reaches zero without exceeding six after the four-triple checkpoint. QED.

## AC5nc -- exact barrier six from four triples to two -- PROVED

At the four-triple checkpoint, the complete component inside `Phi<=5` contains exactly 16 states and none has potential below four.

The committed 73-switch path reaches potential two and has maximum potential six. Its exact potential sequence is retained in `data/ac-p19-zero-certificate.json`.

Therefore

\[
\boxed{
\mathcal B(\Phi=4,\{\Phi<4\})=6.
}
\]

Since the later route to zero also stays below or at six,

\[
\boxed{
\mathcal B(\Phi=4,\{\Phi=0\})=6.
}
\]

### Proof

Exact sublevel breadth-first search gives the 16-state lower-barrier component. Every move in the displayed candidate path is replayed from its complete permutation tables; all remain legal and the maximum exact potential is six. QED.

## AC5nd -- exact barrier six from two triples to one -- PROVED

At the two-triple checkpoint, the complete component inside `Phi<=5` contains exactly 181 states and none has potential below two.

The 13 legal switches

\[
\begin{aligned}
&r:(2,10),\ b:(3,4),\ b:(4,14),\ b:(13,15),\ b:(2,16),\\
&b:(4,11),\ b:(1,17),\ b:(1,5),\ b:(4,15),\ b:(7,8),\\
&r:(8,14),\ b:(7,14),\ b:(7,15)
\end{aligned}
\]

have potential sequence

\[
\boxed{2,6,5,6,6,6,6,5,5,6,6,6,5,1.}
\]

Thus

\[
\boxed{
\mathcal B(\Phi=2,\{\Phi<2\})
=
\mathcal B(\Phi=2,\{\Phi=0\})
=6.
}
\]

The exact search discovered 35,290 states before finding the one-triple endpoint.

### Proof

Barrier-five component exhaustion proves the lower bound. Replay of the 13 legal switches proves the matching upper bound, and AC5ne continues from one to zero with barrier five. QED.

## AC5ne -- exact final barrier five from one triple to zero -- PROVED

The one-triple checkpoint has the unique remaining triple

\[
\{(15,13),(16,10),(17,7)\}.
\]

Its complete sublevel component sizes are:

\[
\begin{array}{c|c}
\text{barrier}&\text{component states}\\\hline
2&2\\
3&5\\
4&56.
\end{array}
\]

None of these components contains a zero-triple state.

The committed 41-switch path has potential sequence

\[
\begin{aligned}
&1,5,4,5,4,5,4,5,4,5,5,5,5,4,5,4,5,5,5,5,5,5,\\
&4,5,5,5,5,5,4,4,4,4,3,5,3,4,2,5,5,5,3,0.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal B(\Phi=1,\{\Phi=0\})=5.
}
\]

The exact barrier-five breadth-first search processed 725,607 states, discovered 930,292 distinct states, and returned the stored 41-edge predecessor path.

### Proof

Exhaustion of the barrier-four component proves every route to zero has maximum at least five. The stored predecessor path is replayed edge by edge, remains legal, never exceeds five and ends at zero. QED.

## Explicit zero-triple configuration

The final red permutation layer is

\[
\begin{aligned}
R_0=\{&(1,4),(2,15),(3,11),(4,14),(5,7),(6,3),\\
&(7,18),(8,9),(9,16),(10,2),(11,12),(12,1),\\
&(13,5),(14,8),(15,17),(16,10),(17,6),(18,13)\}.
\end{aligned}
\]

The final blue layer is

\[
\begin{aligned}
B_0=\{&(1,12),(2,7),(3,3),(4,10),(5,5),(6,15),\\
&(7,14),(8,11),(9,18),(10,9),(11,4),(12,16),\\
&(13,17),(14,2),(15,1),(16,6),(17,13),(18,8)\}.
\end{aligned}
\]

## AC5nf -- explicit 36-point no-three-in-line set on the 18 by 18 board -- PROVED

Both `R_0` and `B_0` are permutation graphs, they are disjoint, and

\[
|R_0\cup B_0|=36=2n.
\]

Every real grid line contains at most two selected cells. Equivalently,

\[
\boxed{\Phi(R_0,B_0)=0.}
\]

Thus `R_0 union B_0` is an explicit no-three-in-line configuration of the maximum conjectured size `2n` for `n=18`.

### Proof

The displayed row images in each layer are permutations of `1,...,18`, and their cells are disjoint. Exhaustive determinant evaluation on all

\[
\binom{36}{3}=7140
\]

three-point subsets finds no zero determinant. QED.

## AC5ng -- completed explicit initial-state termination manifest -- PROVED

For the explicit modular-hyperbola initial state of AC5mp, the physical manifest now contains a complete terminal trajectory:

1. one alternating-star installation lowers `Phi` from 66 to 41;
2. 11 strict switches lower 41 to 10;
3. a 247-switch loop-erased path crosses a certified barrier at most 40 and reaches five;
4. 131 further switches pass through the exact barriers of AC5nb--AC5ne and reach zero.

The raw post-installation switch path has 389 moves; loop erasure leaves 387. Including the initial AN installation, the complete recorded terminal trajectory has 390 physical operations.

Every operation preserves the two disjoint permutation layers. The terminal state satisfies the exact no-three-in-line predicate, so no exceptional payment, source, ticket, repair or reset occurrence is needed to certify termination of this particular initial state.

### Proof

AC5mt, AC5mv--AC5my and AC5nb--AC5nf verify every segment and endpoint. Concatenating the complete operation records gives the terminal manifest. QED.

## Deterministic audit

`scripts/verify_ac_explicit_p19_zero_certificate.py` reconstructs the initial modular-hyperbola seed and replays all path segments. It also exhausts the four small lower-barrier components, checks the exact component sizes, verifies every row switch and potential, and confirms that the final 36-point union has no collinear triple.

## Main AC frontier

Only AC remains active. This completes one explicit initial-state task and proves the `n=18` special case by a concrete certificate. The remaining frontiers are:

1. shorten or lower the high barrier on the 10-to-5 segment;
2. identify a uniform structural reason for the exact low-potential barriers;
3. generalize the modular-hyperbola seed and terminal path to other primes;
4. manifest the full intended AC initial-state class rather than one explicit state;
5. discharge the unresolved AC1 arithmetic, repair-layer and source predicates in the uniform argument.

AC6 and the global no-three-in-line conjecture remain open.
