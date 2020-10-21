- # 定义 #

1. **半群Semi-Group/幺半群Monoid-Group/群Group**
2. **Abel群/有限群Finite Group/无限群Infinite Group**
3. **子群**
4. **中心化子Centralizer/中心Center** 
> Given an element g in a Group G, we define $$C_G(g) = \{a\in G | ag = ga\}$$ $$C_G(S) = \{a\in G | ag = ga \forall g\in S\}$$ $$C(G) = C_G(G)$$
5.  **生成元/生成子群**
> Given $S\subseteq G$, we define $$<S> = \text{the smallest subgroup containing } S$$
6. **循环群**：$G = <a>$
7. **群和元素的阶数Order** 
8. **置换群Permutation Group**
9. **轮换Cycle/对换Transportation**
10. **sign of a permutation/奇置换/偶置换**
11. **交错群Alternating Group**
12. **左陪集/右陪集Coset**
13. **正规子群Normal Subgroup**
14. **共轭子群Conjugation Subgroup**
15. **商群Quotient Group**
16. **正规化子Normalizer**
> $H\le G$, we define $N_G(H)\triangleq \{g\in G, g^{-1}Hg = H\}$. Now, $H\lhd N_G(H)$
17. **换位子群**
> $G$ a group, $[G,G]\triangleq<aba^{-1}b^{-1} , a\in G, b\in G>$
18. **单群Simple**
19. **共轭等价Conjugation**
> $h\sim h' \iff \exist g\in G, h = gh'g^{-1}$
20. **Cycle Type**
> $\forall\sigma\in S_n, \sigma = \prod_{i=1}^n \sigma_i, \sigma_i\cap\sigma_j = \empty$；且$n_i = |\sigma_i|$满足$n_i\le n_j $若$i\le j$；则$(n_1,n_2,...,n_m)$则被称为$\sigma$的Cycle type.
21. **群同态Group Homomorphism**
22. **群同构Group Isomorphism**
23. **核Kernel/象Image**

- # 例子 #

1. $(\mathbb{Z}/\mathbb{Q}/\mathbb{R}/\mathbb{C}, +)$为Abel群
2. $(\mathbb{Q}-\{0\}/\mathbb{R}-\{0\}/\mathbb{C}-\{0\}, \times) $为Abel群
3. $\mathbb{Z}-\{0\}$为幺半群
4. $(M_n(\mathbb{C}),+)$为Abel群（$n$阶矩阵全体在加法作用下的群）
5. $(GL_n(\mathbb{C}),\times)$为非Abel群（$n$阶非异阵全体在乘法作用下的群）
6. 二面体群 $$D_{n} := \{1,a,a^2,...,a^{n-1},b,ba,ba^2,...,ba^{n-1}\} $$  $$ = <a,b | a^n= 1, b^2 = 1, ab = ba^{-1}>$$ 为非Abel群（$n\ge 3$时）
7. $$SL_2(\mathbb{Z}):= \{A\in M_2(\mathbb{Z}),\det(A) = 1\}$$ $$ = <a,b | a= \left( \begin{matrix} 1 & 0 \\ 1 & 1 \end{matrix}\right), b = a= \left( \begin{matrix} 1 & 1 \\ 0 & 1 \end{matrix}\right)>$$
8. 设$G = (\mathbb{Z},+)$，则$H = \{\text{偶数全体}\}\le G$，而$H’ = \{\text{奇数全体}\}\not\le G$；$H = \{\text{能被3整除的数}\}\le G$，而$H’ = \{a | a\equiv 1\mod 3\}\not\le G$
9. 设$G = GL_n(\mathbb{C})$，则$H = O_n(\mathbb{C}):= \{A\in GL_n(\mathbb{C}) | A\cdot A^T = I_n\}\le G$
10. 设$G = GL_n(\mathbb{C})$，则$C(G) = \{aI_n | a\in \mathbb{C}-\{0\}\}$
11. $G = (\mathbb{Z},+) = <1>$为循环群
12. $G = \mathbb{Z}/n\mathbb{Z} = \{[0],[1],...,[n-1]\} = <[1]>$为循环群
13. $S_3$是最小的非Abel群
14. $|G| = 4$时，$G = \{e,a,a^2,a^3\}$循环群或$G = \{e,a,b,ab\} = \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$
15. 【Subgroup of $S_n$】
(1) $$A_n\le S_n$$ (2) $$D_n\le S_n, (n\ge 3)$$ $n =1,2$时$D_n\not\le G$
16. {Odd permutation}即是$A_n$的左陪集，又是其右陪集，从而$A_n\lhd S_n$
17. $G = GL_n(\mathbb{C}), H = SL_n(\mathbb{C})$，则$H\lhd G, G/H = (\mathbb{C}-\{0\}, \times)$
18. $G = (\mathbb{Z}, +), H = n\mathbb{Z}$，则$H\lhd G , G/H = \mathbb{Z}/n\mathbb{Z}$
19. $G = (\mathbb{Q}, +), H = \mathbb{Z}$，则$H\lhd G, G/H = \mathbb{Q}/\mathbb{Z}$  **(Torsion Group)**
20. $[GL_n(\mathbb{C}),GL_n(\mathbb{C})] = SL_n(\mathbb{C})$
21. $G\triangleq \mathbb{Z}/p\mathbb{Z}$，p为素数，则$G$是一个Abel群，也是单群
22. $$\det: GL_n(\mathbb{C})\to \mathbb{C}^\ast = \mathbb{C} - \{0\}$$ $$A\mapsto\det(A)$$ is a Homomorphism; $\ker(f) = SL_n(\mathbb{C}) ; Im(f) = \mathbb{C}^\ast$
23. $$sgn: S_n\to\mathbb{Z}/2\mathbb{Z}$$ $$\sigma\mapsto sgn(\sigma)$$ is a Homomorphism ; $\ker(f) = A_n ; Im(f) = \mathbb{Z}/2\mathbb{Z}$
24. $$trace: M_n(\mathbb{C},+)\to(\mathbb{C},+)$$ $$M\mapsto tr(M)$$ is a Homomorphism
25. $GL_n(\mathbb{C})/SL_n(\mathbb{C})\triangleq\mathbb{C}^\ast$
26. $\mathbb{C}/\mathbb{Z}\triangleq\mathbb{C}^\ast$
27. $\mathbb{C}'(\mathbb{R})/\mathbb{R}\triangleq \{\text{Integrable function}\}$

- # 性质/结论 #

- ## 1. 群的基本概念 ##

1.1 	对于幺半群来说，幺元、逆元唯一，且消去律成立
1.2 	$H\le G \iff \forall a,b\in H, ab^{-1}\in H$
1.3 	$\forall i\in\Lambda, H_i\le G \Longrightarrow \cap_{i\in\Lambda} H_i\le G$
1.4 	若$C_G(g) = G$，那么$g\in C(G)$
1.5 	$C_G(S) = \cap_{g\in S} C_G(g)$
1.6 	$C_G(g)\le G, C_G(S)\le G, C(G)\lhd G$
1.7 	$C(G)$是一个Abel群
1.8 	$<S> = \{a_1^{n_1}a_2^{n_2}...a_k^{n_k}, a_i\in S, n_i = \pm 1\}$
1.9 	$ord(g) = 1\iff g=e$
1.10 	设$G$是一个有限群，$a,b\in G$，则$ab,ba$有相同的阶数
1.11 	设群$G$中的每个元素$a$满足$a^{-1} = a$，则$G$是一个Abel群。
1.12 	设$H$是群$G$的一个子群，它包含在$G$的每一个非平凡子群中，则$H$包含在$G$的中心中。
1.13  	设$H$是有限群$G$的一个非空子集。若$ab\in H$对任意$a,b\in H$成立，则$H\le G$。

- ## 2. 循环群 ##

2.1 	若$G$是一个循环群，则$G$只能是$\mathbb{Z}$和$\mathbb{Z}/n\mathbb{Z}$其中之一
2.2 	循环群的子群皆为循环群
2.3 	循环群皆为Abel群
2.4 	对于群$G, g\in G$，若$g^n = e$，则有$ord(g) | n$
2.5 	若$G$是一个$p$阶有限群，$p$为素数，则$G$必是一个循环群，且$G\cong \mathbb{Z}/p\mathbb{Z}$
2.6 	$|S_n| = n!$
2.7 	$S_n$由二阶轮换生成
2.8 	若$|G| = p^2$，$p$为素数，则$$G\cong\mathbb{Z}/p^2\mathbb{Z}$$ or $$G\cong\mathbb{Z}/p\mathbb{Z}\times\mathbb{Z}/p\mathbb{Z}$$ 从而$G$是一个Abel群
2.9 	设$\sigma_1,\sigma_2\in S_n$，则$sgn(\sigma_1)\cdot sgn(\sigma_2) = sgn(\sigma_1\sigma_2)$

- ## 3. 陪集 ##

3.1 	$|aH| = |Ha| = |H|$
3.2 	$aH = bH\iff ab^{-1}\in H$
3.3 	$aH = bH \iff aH\cap bH\not=\emptyset$
3.4 	$g\in G, |G|<+\infty$, then $g^{|G|} = e$

- ## 4. 正规子群 ##

4.1 	$bH = Hb,  \forall b\in G \iff (aH)(bH) = (ab)H,  \forall a,b\in G$
4.2 	若$G$是Abel群，$H\le G$，则$H\lhd G$
4.3 	$H\le G, [G:H] = 2$，则$H\lhd G$
4.4 	$[G,G] = \{e\} \iff G $ 是Abel群
4.5 	$[G,G]\lhd G$
4.6 	$G/[G,G]$是Abel群
4.7 	$|G| = 2\cdot p$，p为素数，则$G$不是单群
> （由Cauchy's Theorem）

4.8 	若$G$为单群，则$C(G) = \{e\}$，当$G\not=\mathbb{Z}/p\mathbb{Z}$时；
$[G,G] = G$，当$G\not=\mathbb{Z}/p\mathbb{Z}$时。
4.9 	第一个非Abel单群为$A_5$
4.10 	若$H$不是正规子群，则$[G:N_G(H)] = \# \text{ of distinct conjugation groups of } H$
4.11 	$|[h]| = [G:C_G(h)] = [G:N_G(h)]$
4.12 	$|G| = p^n$, p为素数，则$G$不为单群
> （用Class Equation）

4.13 	$H\le G$，则$\forall h\in H,[h]\subseteq H \iff H\lhd G$

- ## 5. 交错群 ##

5.1 	$\forall\sigma\in S_n$ a $d-$cycle, $d = (a_1,...,a_d), \forall \tau\in S_n$, we have $$\tau\sigma\tau^{-1} = \tau(a_1,...,a_d)\tau^{-1} = (\tau(a_1),...,\tau(a_d))$$
5.2 	$\sigma$ is conjugate to $\sigma' \iff \sigma,\sigma'$有相同的Cycle type.
5.3 	$A_n$由3阶轮换生成
5.4 	若$N\lhd A_n$，则$N$要么不含3-阶轮换，要么含所有的3-阶轮换
5.5 	若$N\lhd A_n ,n\ge 5, N\not=\{1\}$，那么$N$必包含一个3-阶轮换

- ## 6. 群同态 ##

6.1 	$\ker(f)\le G, Im(f)\le H$
6.2 	If $f$ is a bijection, then $f$ is an isomorphism

- # 定理 #

1. **(Lagrange Theorem)**
> Assume $H\le G, |G|<+\infty$, then $|G| = [G:H]\cdot|H|$, we call $[G:H]$ the **index of $H$ in $G$**
2. **(Extension of Lagrange Theorem)**
> Assume $K\le H\le G$, then $[G:K] = [G:H]\cdot[H:K]$
3. **(Cauchy's Theorem)**
> Suppose $|G|<+\infty, p||G|$ is a **prime** factor, then $\exist H\le G, s.t. |H| = p$
4. **(Class Equation)**
> If $|G|<+\infty$, then $$|G| = \sum_{h\in G/\sim}|[h]|$$ $$ = |C(G)| + \sum_{h\in G/\sim, h\not\in C(G)}|[h]|$$ $$= |C(G)| + \sum_{h\in G/\sim, |[h]|>1}|[h]|$$
5. 
> 对于 $n\ge 5, A_n$是一个非Abel单群。
6. **（同态基本定理）**
> $f:G\to H$ is a group homomorphism, then we have : 
	(1) $\ker(f)\lhd G$
	(2) $G/\ker(f) \triangleq Im(f)$

- # 题目 #

1. **（群的单边定义）**：设$G$是一个满足下面两个条件的半群：
	（1）存在一个$e\in G$，使$ea =a $对任何$a\in G$成立
	（2）对任何$a\in G$，存在$b\in G$使$ba = e$成立
> Hint：计算$a\cdot a^{-1} = (a^{-1})^{-1}\cdot a^{-1}\cdot a\cdot a^{-1}$
