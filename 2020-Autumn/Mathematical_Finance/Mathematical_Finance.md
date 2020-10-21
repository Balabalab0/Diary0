- # Single Period Securities Markets #
- ## 1 Model Specification ##
- **1.1 Model**
    1. Initial date $t=0$ ; terminal date $t=1$
    2. **Finite** sample space $\Omega$ $$\Omega = \{w_1,w_2,...,w_n\}$$
    3. A probability measure $P$ on $\Omega$ with $P(w_i)>0$ for all $w\in\Omega$
    4. A bank account $B = \{B_t:t=0,1\}$, in which $$B_0 = 1,B_t = 1+t$$
    5. A price process of stocks $S = \{S_t,t=0,1\}$, where $S_t = (S_1(t),...,S_N(t)), N<\infty$ and $S_N(t)$ is the time $t$ price of $n$
        
    【注意：投资者只知道$t=0$时刻股票的价格，而$t=1$时刻只受$\{w_i\}$影响】

    We call $\mathscr{M} = \{(\Omega,\mathscr{F},P),B,S\}$ is a single period securities market
- **1.2 Definitions**
    1. **Trading Strategy**: $H = (H_0,..., H_n)$, in which $H_0$ is the number of dollers invested in saving account; $H_1,...,H_n$ is the units of security $n$; $H_n$ can be positive or negative 
    2. **Value Process**: $V = \{V_t,t=0,1\}$, in which $V_t = H_0B_t + \sum_{i=1}^n H_iS_t$
    3. **Gain Process**: $G = H_0 r + \sum_{i=1}^n H_i\Delta S_n, G = V_1 - V_0$
    4. **Discounted price process**: $S^* = \{S_t^*: t=0,1\}, S_t^* = (S_1^*(t),...,S_N^*(t))$, in which $S_n^*(t) = \frac{S_n(t)}{B_t}$
    5. **Discounted value process**: $V^* = \{V_t^*,t=0,1\}$, $V_t = H_0 + \sum_{i=1}^n H_i S_i^*(t)$
    6. **Discounted gains process**: $G^* = \sum_{i=1}^N H_n\Delta S_n^*, \Delta S_n^* = S_n^*(1) - S_n^*(0), G^* = V_1^* - V_0^*$
- ## 2 Arbitrage ##
- **2.1 Dominant trading strategy**占优策略
    1. **Def** A trading strategy $\widehat{H}$ is said to be dominant if there exists another trading strategy $\widetilde{H}$, s.t. $$\widehat{V}_0 = \widetilde{V}_0,\widehat{V}_1(w_i) > \widetilde{V}_1(w_i), \forall w_i\in\Omega$$
    2. **Prop** Dominant trading strategy equivalance:
    (i) There exists a dominant trading strategy
    $\iff$ (ii) There exists a trading strategy $V_0 = 0, V_1(w_i)>0, \forall w_i\in\Omega$
    $\iff$ (iii) There exists a trading strategy $G^*(w_i)>0, \forall w_i\in\Omega$
    $\iff$ (iv) There exists a trading strategy $V_0<0, V_1(w_i)\ge 0,\forall w\in\Omega$
- **2.2 可复制、可定价**
    - 设随机变量$(X,r,u)$，若存在$H$，使得$V_1(w_i,H) = X(w_i),\forall w_i$成立，则称$H$为复制策略，称为可复制的；
    - 若$v_0(H)$不随$H$变化，则称未定权益是可定价的
    - **Linear Pricing Measure** 线性价格测度
    > If there is a linear pricing measure, that is, a non-negative vector $$\pi = (\pi(w_1),...,\pi(w_k))$$ such that for every trading strategy $H$ you have **(1.6)** $$V_0^\ast = \sum_w\pi(w)V_1^\ast(w) = \sum_w\pi(w)V_1(w)/B_1(w)$$
    【Remark1】 令$H_1 = ... = H_N = 0$，容易得到$\sum_w \pi(w) = 1$，从而$\pi$可被看成一个概率测度；
    【Remark2】 **(1.7)** 对于任意$i\in\{1,...,N\}$，令$H_n = 0 , \forall n\not= i$，容易得到$$S_n^\ast(0) = \sum_w\pi(w)S_n^\ast(1)(w) , n = 1,...,N$$ 进而：**$\pi$是一个线性价格测度$\iff$其满足上述两个Remark**
    【Remark3】 **(1.8)** 若存在线性价格测度，则$V_0$就等于各种情况下折价后的期望
    - **(1.9)** 一个市场存在线性价格测度$\iff$其不存在占优策略
    - **Law of one price** 单一价格定律
    > It's said that the law of one price holds for a securities market model if there do not exist two trading strategies, say $\widehat{H},\widetilde{H}$，such that $\widehat{V}_1(w) = \widetilde{V}_1(w)$ for all $w\in\Omega$ but $\widehat{V}_0>\widetilde{V}_0$。
    【Remark】 If the law of one price holds, then there is no ambiguity about the time $t=0$ price of any claim.
    - **(1.12)** 若一个市场不存在占优策略，则单一价格定律成立；反之则不一定成立。
    - **Arbitrage opportunity** 套利
    > An arbitrage opportunity is some trading strategy $H$ such that:
    **(a)** $V_0 = 0$,  $V_1\ge 0$, $EV_1 > 0$ （期望）
    $\iff$ **(b)** $V_0^\ast = 0 , V_1^\ast\ge 0, EV_1^\ast > 0$
    $\iff$ **(c)** $G^\ast\ge0 , EG^\ast > 0$
    - **(1.13)** 若一个市场存在占优策略，则必存在套利机会；但反过来不一定成立。
- ## 3 Risk Neutral Probability Measures ##
- **Def**
> A probability measure $Q$ on $\Omega$ is said to be a risk neutral probability measure if
(a) $Q(w) > 0, \forall w\in\Omega$
(b) $E_Q[\Delta S_n^\ast] = 0, n=1,2,...,N$
- **(1.16)** There are no arbitrage opporunities if and only if there exists a risk neutral probability measure $Q$