# A transposition decoder for background-rainbow collisions

PX191--PX192 identify the two-replacement/one-background collateral \(T_2\) with
repeated colours in a family of proper anchor colourings. This chapter gives a
complete transposition decoder for that collision potential.

The conclusion has the same form as the original rectangle decoder:

- either one executable transposition lowers \(T_2\); or
- one off-matching cell has a large anchor-colour shadow.

That shadow in turn contains either a loaded line or a clean endpoint-disjoint
star, reconnecting the second-generation obstruction to the first-generation
neutralization geometry.

Let \(G\subseteq R\times C\) be a balanced bipartite graph of order \(s\). Its
forbidden-position complement has row and column degree at most two. Let

\[
M=\{e_i=(r_i,c_i):i\in[s]\}
\]

be one perfect matching of \(G\), and let \(Z\) be the fixed background point
set.

For every \(z\in Z\), use the proper anchor colouring \(\chi_z\) from PX191.
Define the collision potential

\[
\Phi_Z(M)
=
\sum_{z\in Z}
\sum_\gamma
\binom{|\{e\in M:\chi_z(e)=\gamma\}|}{2}.
\]

By PX192, this is exactly \(T_2(M;Z)\).

## 1. Executable transpositions

For two matching rows \(i\ne j\), the transposition replaces

\[
(r_i,c_i),
\qquad
(r_j,c_j)
\]

by

\[
(r_i,c_j),
\qquad
(r_j,c_i).
\]

It is executable when both cross edges lie in \(G\).

Since every row and column has at most two forbidden positions, for a fixed
row \(i\), at most four choices of \(j\) make the transposition nonexecutable:

- at most two because \((r_i,c_j)\) is forbidden;
- at most two because \((r_j,c_i)\) is forbidden.

## Theorem PX193 -- PROVED

Every current anchor-colour collision in \(M\) is destroyed by at least

\[
\boxed{2(s-6)}
\]

executable transpositions.

### Proof

Fix a collision consisting of \(e_i,e_j\) with

\[
\chi_z(e_i)=\chi_z(e_j)
\]

for one anchor \(z\).

Swap \(i\) with a row \(b\notin\{i,j\}\). Among the \(s-2\) choices, at most four
are nonexecutable, leaving at least \(s-6\).

The old edge \(e_j\) remains. Neither inserted cross edge can retain its colour:

- \((r_i,c_b)\) lies in the same source row as \(e_i\), and properness gives at
  most one edge of the old colour in that row;
- \((r_b,c_i)\) lies in the same target column as \(e_i\), and properness gives
  at most one edge of the old colour in that column.

Thus the collision with \(e_j\) is destroyed. Repeating the argument with
\(j\) as the moved endpoint gives another \(s-6\) distinct swaps. \(\square\)

## 2. Creation shadows

For an allowed off-matching edge \(f\in E(G)\setminus M\), define its selected
anchor shadow

\[
\lambda_M(f)
=
\#\{(z,e)\in Z\times M:
 e\text{ compatible with }f,
 \chi_z(e)=\chi_z(f)\}.
\]

Equivalently, \(\lambda_M(f)\) counts triples consisting of \(f\), one selected
matching edge, and one background anchor.

Put

\[
\mathcal S_1(M)
=
\sum_{f\in E(G)\setminus M}\lambda_M(f).
\]

For one executable transposition, let its two cross edges be \(f,f'\). Define

\[
\mathcal S_2(M)
=
\sum_{\text{executable swaps }\{i,j\}}
\#\{z\in Z:\chi_z(f)=\chi_z(f')\}.
\]

The first sum overcounts every new collision using one inserted edge and one
unchanged matching edge. The second counts every collision using both inserted
edges.

## Theorem PX194 -- PROVED

For \(s\ge7\), summing over all executable transpositions gives

\[
\boxed{
\sum_{\omega}
\bigl(\Phi_Z(M^\omega)-\Phi_Z(M)\bigr)
\le
\mathcal S_1(M)+\mathcal S_2(M)
-2(s-6)\Phi_Z(M).
}
\]

Consequently, if

\[
2(s-6)\Phi_Z(M)
>
\mathcal S_1(M)+\mathcal S_2(M),
\]

some executable transposition strictly lowers the two-background collision
potential.

### Proof

PX193 supplies the destroyed-collision incidences. Across the transposition
bank, every off-matching edge occurs in at most one executable swap, so all
one-inserted creations are bounded by \(\mathcal S_1\). The two-inserted
creations are exactly bounded by \(\mathcal S_2\). Sum the exact potential
changes. \(\square\)

## 3. Local shadow form

Define

\[
\Lambda(M)
=
\max_{f\in E(G)\setminus M}\lambda_M(f)
\]

and let

\[
L_Z
=
\max_{f,f'\text{ compatible}}
\#\{z\in Z:z,f,f'\text{ collinear}\}.
\]

There are at most \(s(s-1)\) off-matching edges, so

\[
\mathcal S_1(M)
\le
s(s-1)\Lambda(M).
\]

Every cross pair lies on one scalar line and has at most \(L_Z\) background
completions. Therefore

\[
\mathcal S_2(M)
\le
L_Z\binom{s}{2}.
\]

## Corollary PX195 -- PROVED

A transposition-local minimum with \(\Phi_Z(M)>0\) satisfies

\[
\boxed{
2(s-6)\Phi_Z(M)
\le
s(s-1)\Lambda(M)
+
L_Z\binom{s}{2}.
}
\]

Equivalently,

\[
\boxed{
\Lambda(M)
\ge
\frac{2(s-6)\Phi_Z(M)-L_Z\binom{s}{2}}{s(s-1)}.
}
\]

Thus a collision mass substantially larger than \(L_Zs\) forces one
candidate cell with anchor shadow of order \(\Phi_Z(M)/s\).

## 4. Shadow extraction returns to clean stars and loaded lines

Fix an off-matching cell \(f\) attaining \(\Lambda(M)\). Form the bipartite
incidence graph

\[
\mathcal B_f
\subseteq
Z\times M
\]

with edge \(ze\) when \(z,f,e\) are collinear. It has exactly
\(\Lambda(M)\) edges.

The degree of one selected matching edge \(e\) is at most \(L_Z\), because all
its neighboring anchors lie on the one line \(fe\).

For one anchor \(z\), all neighboring matching cells lie on the line \(fz\).
Hence:

- if some anchor degree is large, the line \(fz\) is a loaded selected line;
- if every selected line has occupancy at most \(K\), then every anchor degree
  is at most \(K\).

A bipartite graph of maximum degrees \(L_Z\) and \(K\) has a matching of size at
least

\[
\frac{|E(\mathcal B_f)|}{L_Z+K}.
\]

## Corollary PX195a -- PROVED

For every heavy shadow cell \(f\), either:

1. one line through \(f\) contains more than \(K\) selected/background points,
   giving a loaded-line outcome; or
2. there is an endpoint-disjoint clean star through \(f\) of size at least

   \[
   \boxed{
   \frac{\Lambda(M)}{L_Z+K}.
   }
   \]

### Proof

In the bounded-degree case, greedily extract a matching from
\(\mathcal B_f\). Each chosen incidence removes at most \(L_Z+K-1\) other
incidences. The selected incidences have distinct anchors and distinct matching
cells, and every corresponding pair is collinear with the common outside point
\(f\). \(\square\)

In the complementary regime used by PX78, one may take \(K=12\). If the whole
selected state also has line occupancy at most twelve, then \(L_Z\le12\), and
the extracted clean star has size at least \(\Lambda(M)/24\).

## 5. Consequence for the repair recursion

The second-generation \(T_2\) obstruction is now decoded into the same two
geometric outcomes already handled at first generation.

1. Run executable transpositions inside the thinned rematching block until
   \(T_2\) decreases or reaches a local minimum.
2. At a local minimum, PX195 produces a heavy off-matching shadow unless the
   collision mass is already \(O(L_Zs)\).
3. PX195a converts the heavy shadow into a loaded line or clean star.
4. Apply the corresponding neutralization bank again, now centred on the new
   outside cell \(f\).

What remains is a termination theorem for this recursion. A successful
potential must charge the reduction in \(T_2\) against the size of the newly
extracted star/line so that repeated generations cannot cycle.

The obstruction is no longer an unstructured fixed-rank certificate mass: it
has an exact decoder back to executable geometry.

## Verification

Run

```bash
python scripts/verify_product_background_rainbow_decoder.py
```

The verifier constructs random degree-two-forbidden rematching graphs and
background-anchor colourings, checks the aggregate transposition inequality,
and verifies the local-minimum shadow bound through order eleven.
