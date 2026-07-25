# High-pair endpoint rematching

AC3k leaves a high anchor-pair codegree as one possible output of an
anchor-realized Hall obstruction.  No quotient or carry classification
is needed before this output becomes executable.  A pair contained in
many current rank-three certificates has many distinct third endpoints;
one permutation layer contains at least half of them.  Rematching those
endpoints is an AN1 bank which destroys the whole selected pair core.

Throughout this note the current state is

\[
S=S^{\rm red}\mathbin{\dot\cup}S^{\rm blue}
\subseteq [n]\times[n],
\]

where each colour is a permutation graph and the two graphs are
disjoint.  Let \(\Phi(S)\) be the number of unordered real-collinear
triples in \(S\).

## Pair cores

Fix distinct current cells \(u,v\in S\), let \(\ell(u,v)\) be their
real line, and put

\[
Y(u,v)=
\bigl(S\cap\ell(u,v)\bigr)\setminus\{u,v\}.
\]

Every \(y\in Y(u,v)\) gives the distinct current certificate
\(\{u,v,y\}\).  Conversely, every current rank-three certificate
containing \(\{u,v\}\) has this form.  Hence its pair codegree is

\[
d(u,v)=|Y(u,v)|.
\]

Partition \(Y(u,v)\) by colour and choose a larger part \(A\).  Write

\[
t=|A|\geq\left\lceil\frac{d(u,v)}2\right\rceil.
\]

The points of \(A\) have distinct columns
\(C=\{c_1,\ldots,c_t\}\) and distinct rows
\(R=\{r_1,\ldots,r_t\}\).  Index them as
\(a_i=(c_i,r_i)\).

In the block \(C\times R\), forbid:

1. every original diagonal cell \((c_i,r_i)\); and
2. every cell occupied by the opposite permutation layer.

Call the resulting forbidden set \(F\).  The first class is a perfect
matching.  The second is a restriction of another matching.  Therefore
every block row and block column contains at most two forbidden cells.
Let

\[
\Omega(F)=
\{\pi\in S_t:(c_i,r_{\pi(i)})\notin F
 \text{ for every }i\}.
\]

For \(\pi\in\Omega(F)\), put

\[
M_\pi=\{(c_i,r_{\pi(i)}):1\leq i\leq t\},
\qquad
S_\pi=(S\setminus A)\cup M_\pi.
\]

## AC3m -- the high-pair bank

### Theorem AC3m -- PROVED

If \(t\geq7\), then \(\Omega(F)\) is nonempty and every
\(\pi\in\Omega(F)\) has all of the following properties.

1. \(S_\pi\) is again the disjoint union of two permutation graphs.
2. Every selected endpoint leaves its original cell.
3. All \(t\) original pair-core certificates
   \[
   \{u,v,a_i\},
   \qquad 1\leq i\leq t,
   \]
   are destroyed.
4. If \(\pi\) is uniform on \(\Omega(F)\), every compatible
   nonforbidden partial matching \(Q\) of rank \(r\) satisfies
   \[
   \boxed{
   \Pr(Q\subseteq M_\pi)\leq\frac{128}{(t)_r}.
   }
   \]

### Proof

The row and column degree of \(F\) is at most two, so AN1 applies and
gives nonemptiness and the displayed cylinder bound.

Rematching \(C\) to \(R\) preserves the selected colour's row and
column sets.  A point of the same colour outside \(A\) uses neither a
column in \(C\) nor a row in \(R\), while the second forbidden matching
excludes every collision with the opposite colour.  Thus the new state
is again a disjoint union of two permutation graphs.

The forbidden diagonal excludes every old cell \(a_i\).  Consequently
the exact current certificate \(\{u,v,a_i\}\) is absent from
\(S_\pi\).  This proves the remaining assertions. \(\square\)

The conclusion concerns the destruction of exact old certificates.
A replacement cell may create another triple on \(\ell(u,v)\), or a
triple on a different line.  Those events are collateral and are
counted next; they are not silently declared absent.

## AC3n -- exact collateral return

Put

\[
X=S\setminus A
\]

and let \(\mathcal B=(C\times R)\setminus F\).  For \(r=1,2,3\), let
\(T_r^{\rm pair}\) be the number of real-collinear triple certificates
consisting of exactly:

- \(r\) mutually compatible cells of \(\mathcal B\), and
- \(3-r\) cells of \(X\).

Compatibility means that the block cells use distinct columns and
distinct rows.  Define

\[
D_{\rm pair}=\Phi(S)-\Phi(X).
\]

Every selected pair-core certificate meets \(A\), so

\[
\boxed{D_{\rm pair}\geq t.}
\]

### Theorem AC3n -- PROVED

For uniform \(\pi\in\Omega(F)\),

\[
\boxed{
\mathbb E\bigl[\Phi(S_\pi)-\Phi(X)\bigr]
\leq
128\left(
\frac{T_1^{\rm pair}}t+
\frac{T_2^{\rm pair}}{t(t-1)}+
\frac{T_3^{\rm pair}}{t(t-1)(t-2)}
\right).
}
\]

Consequently, if

\[
\boxed{
D_{\rm pair}>
128\left(
\frac{T_1^{\rm pair}}t+
\frac{T_2^{\rm pair}}{t(t-1)}+
\frac{T_3^{\rm pair}}{t(t-1)(t-2)}
\right),
}
\]

then some pair-core state strictly lowers \(\Phi\).

If every state fails to lower \(\Phi\), then one rank
\(r\in\{1,2,3\}\) satisfies

\[
\boxed{
\frac{T_r^{\rm pair}}{(t)_r}
\geq
\frac{D_{\rm pair}}{384}
\geq
\frac{t}{384}.
}
\]

After any partition of that rank into \(L_0\) first-stage arithmetic
labels, one labelled family has normalized size at least

\[
\boxed{\frac{D_{\rm pair}}{384L_0}.}
\]

### Proof

A new triple containing \(r\) replacement cells occurs only if its
rank-\(r\) compatible partial matching lies in \(M_\pi\).  AC3m bounds
that probability by \(128/(t)_r\).  Summing over all potential
certificates proves the expectation bound.

Since

\[
\Phi(S_\pi)-\Phi(S)
=
-D_{\rm pair}
+\bigl(\Phi(S_\pi)-\Phi(X)\bigr),
\]

the strict inequality makes the expected change negative.  Some state
therefore improves.

If every state is non-improving, the expectation is at least
\(D_{\rm pair}\).  One of the three nonnegative normalized terms is at
least \(D_{\rm pair}/(3\cdot128)\).  Pigeonholing its first-stage labels
gives the final assertion. \(\square\)

Thus a failed high-pair bank returns exactly to AC1's normalized
second-order input.  AC3n is an executable transition, not a
termination theorem: the no-recycling potential must still prevent
the same normalized family from reopening indefinitely.

## AC3o -- the constant-threshold router

The threshold in AC3k can now be fixed absolutely.

### Corollary AC3o -- PROVED

Apply AC3k with

\[
\boxed{\Delta=12.}
\]

Then its high-pair alternative has codegree at least \(13\), so one
colour class of third endpoints has size at least seven and AC3m--AC3n
apply.  If the high-pair alternative does not occur, the anchor-link
loss is the absolute constant

\[
\boxed{2\Delta-1=23.}
\]

More explicitly, with the AC3k notation

\[
s=\left\lfloor\sqrt{\frac{\kappa}{T}}\right\rfloor
\]

and resource capacity cap \(\rho\), for every support threshold
\(\Gamma\geq0\) one obtains at least one of:

1. a shared-token same-role fan of more than \(s\) reopenings;
2. an executable pair-core bank on at least seven same-layer
   endpoints;
3. a support-conflict overload of degree greater than \(\Gamma\); or
4. a support-compatible endpoint-disjoint paid star of size at least
   \[
   \boxed{
   \left\lceil
   \frac1{\Gamma+1}
   \left\lceil
   \frac{\lceil s/\rho\rceil}{23}
   \right\rceil
   \right\rceil.
   }
   \]

For nonnegative weights \(w_y\) on the \(d(u,v)>12\) pair-core
certificates, put \(W=\sum_yw_y\).  Either one colour class has at least
seven endpoints and weight at least \(W/2\), so the bank carries that
paid subfamily, or one of at most six certificates in a weight-heaviest
colour class has

\[
\boxed{w_y\geq W/12.}
\]

The weighted statement uses only additivity of the stated certificate
weights; any larger destroyed-incidence weights must satisfy the usual
AC2 no-double-counting contract before being called joint payment.

### Proof

An integer codegree greater than \(12\) is at least \(13\).  Pigeonholing
its third endpoints between two permutation layers gives at least
\(\lceil13/2\rceil=7\) endpoints in one layer.  This is AC3m's input.
The bounded alternative substitutes \(\Delta=12\) into AC3k.

For the weighted assertion, choose a colour class carrying at least
\(W/2\).  If it has at least seven endpoints, use it as \(A\).  If it
has at most six, its heaviest certificate has weight at least
\((W/2)/6=W/12\). \(\square\)

## Channel-supported sanity check

If the current state is contained in \(q\) modular-hyperbola channels,
the high-pair bank is unnecessary: every real line meets each channel
in at most two points, so

\[
\boxed{d(u,v)\leq2q-2.}
\]

For a state contained in those channels together with an exceptional
off-channel set \(E\), disjoint from their union, let
\(a=|\{u,v\}\cap\bigcup_cH_c|\).  At most \(2q-a\) third endpoints lie
in the channels.  Therefore

\[
\boxed{
|Y(u,v)\cap E|
\geq
\max\{0,d(u,v)-(2q-a)\}.
}
\]

This separates the initial channel-supported state from high pair cores
created inside active rematching blocks.  AC3m handles the latter
without requiring the exceptional cells themselves to lie on a
bounded number of algebraic channels.

`scripts/verify_ac_pair_core_bank.py` checks the rematching mechanics on
a seven-endpoint diagonal pair core, enumerates every allowed state,
verifies exact cylinder probabilities and the collateral certificate
sum, and checks the channel pair-codegree bound for small primes.
