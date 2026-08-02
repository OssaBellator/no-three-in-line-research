# Physical atlas of the p=31 five-triple core

## Status

This AC-only note proves AC5oa for the five-triple endpoint of AC5ny. It enumerates the complete current certificate core and every legal one-switch repair attempt.

## Core lines

The five exact triples lie on primitive line equations `Ax+By=C` with records

\[
(3,-1,-14),\quad(1,-6,-117),\quad(1,-1,3),\quad(1,4,106),\quad(1,3,90).
\]

Four triples are vertex-disjoint. The remaining two share exactly the red point `(27,24)`. No other selected point lies in two current triples.

## AC5oa -- complete immediate repair atlas -- PROVED

The state has exactly

\[
\boxed{812}
\]

legal two-row switches. Their successor-potential distribution is

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrr}
\Phi'&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20&21&22&23\\\hline
\#&1&8&5&30&48&65&86&118&126&110&87&62&27&25&7&4&2&1.
\end{array}
\]

In particular, no one-switch improvement exists.

The number of current triples destroyed by one legal switch has distribution

\[
\begin{array}{c|rrrr}
\text{destroyed}&0&1&2&3\\\hline
\#&475&281&53&3.
\end{array}
\]

The unique least-potential neighbour is produced by

\[
\boxed{r:(3,27)}
\]

and has potential six. It destroys three current triples and creates four new triples.

### Proof

Enumerate all two-row swaps in both permutation layers and retain exactly those whose inserted cells avoid the opposite layer. Recompute all real collinear triples on each successor. The resulting 812 records give the displayed distributions and unique minimum. QED.

## Consequence

The five-triple state is not merely a local minimum in scalar potential. Its best immediate repair must temporarily replace a three-certificate subcore by a four-certificate family. Any uniform repair theorem must therefore retain certificate identity and a minimax or bank rank, rather than use raw triple count as a strict local potential.

## Audit

Run:

```text
python scripts/verify_ac_p31_five_triple_core.py
```

The machine-readable atlas is `data/ac-p31-five-triple-core.json`.
