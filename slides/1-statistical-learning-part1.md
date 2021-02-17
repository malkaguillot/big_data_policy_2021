# Big Data for Public Policy
## Statistical Learning [Part 1]
### [Malka Guillot](https://malkaguillot.weebly.com/)
### ETH Zürich | <a href="https://malkipp.github.io/big_data_policy_2021/">860-0033-00L</a>

---

<!-- .slide:  id="toc" class: left, inverse -->
## Table of contents

3. [What is statistical learning?](#)

3. [Inference vs. predictions](#)

2. [Epilogue](#hw)

Notes: my notes

---

<!-- .slide: id="prologue"  -->
## Prologue

### Today
- What is statistical learning?
- Statistics in social science – causality.
- Statistics in machine learning – prediction.

### Next week
- Estimating $f$.
- Accuracy v. interpretability.
- Model accuracy.
- The bias-variance tradeoff.
- Classification

---

<!-- .slide: id="causality_vs_prediction"  -->
# What is statistical learning?
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

note:
https://raw.githubusercontent.com/ljanastas/Princeton_WWS586A-Machine-Learning-Policy-Analysis/master/Lectures/Stat_Learning/WWS586a-02-21-18.pdf

--

## Setting

- Input variables `$\mathcal{X}$`
  - AKA features, independent variables, predictors
- Output variables `$\mathcal{Y}$`
  - AKA dependent variables, outcomes, etc.

--

## Statistical learning theory

  `$$ f: \mathcal{X} \rightarrow \mathcal{Y}$$`

  `$$ \mathcal{X}\in \mathbb{R}^{n \times p} ,  \mathcal{Y}\in \mathbb{R}^{p}  $$`

  > SL= approaches for finding a function that accurately maps the inputs `$\mathcal{X}$` to outputs `$\mathcal{Y}$`


--

## Statistical learning theory

Concretely, finding $f(.)$ s.t. `$$ Y=f(X)+\epsilon$$`

  - $f(X)$ is an unknown function of a matrix of predictors $X= (X_1,···,X_p)$,
  - an outcome $Y$
  - an error term $\epsilon$ with mean zero.
  - While $X$ and $Y$ are known, $f(·)$ is unknown.

<bcolor>Goal of statistical learning</bcolor>: to utilize a set of approaches to estimate the “best” $f(·)$ for the problem at hand.


---

# Inference vs. prediction
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Approach in social science

Objective:
- Understanding the way that $Y$ is affected as $X_1,...,X_p$ change
- The goal not necessarily to make predictions for $Y$


--

## Statistical learning theory


- Social science:
  - often choose a linear function to estimate $Y$ $ f(X)=\sum_{i=1}^p \beta_i x_i$
  - assume that the error term is normally distributed with a zero mean : $ \epsilon \sim  N(0, \sigma^2)$
  - Parameters $\beta$ are estimated by minimizing the sum of squared errors

  $$ Y= \sum_{i=1}^p \beta_i x_i + \epsilon $$

--

## Approach in social science: causality
$$ Y= \beta_0 + \beta_1 T + \sum_{i=1}^{p-1} \beta_i x_i + \epsilon $$

- Interested in the values of one or two parameters and whether they are **causal** or not.
- Framework to interpret statistical causality: <bcolor>Rubin (1974)</bcolor>
- $\beta_1$ measures the extent to which $\Delta X_t$ will affect $\Delta Y_{t+1}$

--

## Approach in social science: causality

- Causal inference requires that $T \perp \epsilon $ or $T|X \perp \epsilon $

$\rightarrow$ can be achieved through randomization of $T$

- This implies that we are not really all that interested in choosing an optimal $f(.)$


--

## Approach in machine learning: prediction
$$ \hat Y = \hat f(X) $$
- Objectives:
  - find the “best” $f(·)$ and the “best” set of $X$’s which give the best predictions,$\hat Y$
  - find the function that <bcolor>minimize the difference between the predicted values and the observed values</bcolor>

Note:  Machine learning is primarily concerned with prediction


--

## Reducible and irreducible error
$\hat f(X)=\hat Y$ estimated function

$f(X)+\epsilon =\hat Y$ true function

- Reducible error: $\hat f$ is used to estimate f, but not perfect
  $\rightarrow$ accuracy can be improved by adding more features
- Irreducible error: $\epsilon$ = all other features that can be used to predict $f$ $\rightarrow$ unobserved $\rightarrow$ irreducible

--

## Reducible and irreducible error
$E(Y_\hat Y)^2 = E[f(X)+\epsilon - \hat f (X)]^2$


---

## Estimating $f$

--

## Assessing model accuracy


---

<!-- .slide: id="getting_started"  -->
# Econometrics vs. Machine Learning
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

---

<!-- .slide: id="getting_started"  -->
# Econometrics vs. Machine Learning
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Econometrics vs. Machine Learning (1)

- **Common objective**: to build a predictive model, for a variable of interest, using explanatory variables (or features)
- **Different cultures**:
  - *E*: probabilistic models designed to describe economic phenomena
  - *ML*: algorithms capable of learning from their mistakes

<cite><i class="fa fa-book fa-fw" aria-hidden="true"> </i> Charpentier A., Flachaire, E. & Ly, A. (2018). [Econometrics and Machine Learning](https://www.insee.fr/en/statistiques/fichier/3706234/505-506_Charpentier-Flachaire-Ly-EN.pdf). *Economics and Statistics*, 505-506, 147–169.</cite>

--

##  Econometrics vs.  Machine Learning (2)

<img data-src="images/ml_vs_traditional_paradigm2.png"  style="height: 300px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

- **Classical computer programming**: <span style="color:blue">humans</span> input the <span style="color:blue">rules</span> and the <span style="color:blue">data</span>, and the <span style="color:green">computer</span> provides <span style="color:green">answers</span>.

- **Machine learning**: <span style="color:blue">humans</span> input the <span style="color:blue">data</span> and the <span style="color:blue">answer</span>, and the <span style="color:green">computer</span>  learns the <span style="color:green">rules</span>.

--

## The Machine learning landscape
<img data-src="images/machine_learning_landscape.jpeg"  style="height: 550px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

--

## Model-based vs. algorithmic approaches



--

## Researcher vs. policy analysist

- <!-- .element: class="fragment" data-fragment-index="1" -->
   The frontier can be thin
-  <!-- .element: class="fragment" data-fragment-index="2" -->
   I will sometimes be speaking from the point of view of an economist, but:
  - <!-- .element: class="fragment" data-fragment-index="3" -->
    The model-based vs. algorithm-based problematics transfers to other social sciences
  - <!-- .element: class="fragment" data-fragment-index="4" -->
    I try to cover a wide range of topics in the literature
  - <!-- .element: class="fragment" data-fragment-index="5" -->  You are welcome to propose relevant papers
- <!-- .element: class="fragment" data-fragment-index="6" -->
  All aim at *using data to solve problems*

---

<!-- .slide: id="hw"-->
## For next week

- Homework
