# Big Data for Public Policy
## Statistical Learning [Part 1]
### [Malka Guillot](https://malkaguillot.weebly.com/)
### ETH Zürich | <a href="https://malkipp.github.io/big_data_policy_2021/">860-0033-00L</a>

---

<!-- .slide: id="prologue"  -->
# Prologue
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## References

- <i class="fa fa-book fa-fw" aria-hidden="true"></i> [JWHT](https://static1.squarespace.com/static/5ff2adbe3fe4fe33db902812/t/601cc86d7f828c4792e0bcae/1612499080032/ISLR+Seventh+Printing.pdf) chap 1. & 2.1
-  Kleinberg, Ludwig, Mullainathan, and Obermeyer (2015), ["Prediction Policy Problems."](https://www.aeaweb.org/articles?id=10.1257/aer.p20151023) American Economic Review, 105 (5), pp. 491-95.
- Mullainathan and Spiess (2017), ["Machine Learning: An Applied Econometric Approach"]((https://pubs.aeaweb.org/doi/pdfplus/10.1257/jep.31.2.87)), Journal of Economic Perspectives, 31 (2), pp. 87-106,

--

## Context
### Today
- What is statistical learning?
- Statistics in social science – causality.
- Statistics in machine learning – prediction.
- Accuracy v. interpretability.

### Next week
- Model accuracy.
- The bias-variance tradeoff.
- Classification

--

<!-- .slide:  id="toc" class: left, inverse -->
## Table of contents

1. [What is statistical learning?](#what)

3. [Why estimate $f(X)$?](#why)

3. [How do we estimate $f(X)$?](#how)

3. [Machine Learning: an overview](#ml)

3. [Conclusion](#conclusion)

Notes: my notes

---

<!-- .slide: id="what"  -->
# What is statistical learning?
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

note:
https://raw.githubusercontent.com/ljanastas/Princeton_WWS586A-Machine-Learning-Policy-Analysis/master/Lectures/Stat_Learning/WWS586a-02-21-18.pdf
https://teaching.parisschoolofeconomics.eu/docs/SHAREDmachinelearning/Part1.pdf


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

## Statistical model

Concretely, finding $f(.)$ s.t. `$$ Y=f(X)+\epsilon$$`

  - $f(X)$ is an unknown function of a matrix of predictors $X= (X_1,···,X_p)$,
  - $Y$: a scalar outcome variable
  - an error term $\epsilon$ with mean zero.
  - While $X$ and $Y$ are known, $f(·)$ is unknown.

<bcolor>Goal of statistical learning</bcolor>: to utilize a set of approaches to estimate the “best” $f(·)$ for the problem at hand.

--

### Example: income as a function of education

<div class="r-stack"><img data-src="images/jwht-fig2-2.png" style="height: 400px;" > </div>

Notes:
- The **red dots** are the *observed values* of income and years of education for 30 individuals.
- The **blue curve** represents the *true underlying relationship* between in come and years of education, which is generally unknown (but is known in this case because the data were simulated).
- The **black lines** represent the *error* associated with each observation. Overall, these errors have approximately mean zero.

---
<!-- .slide: id="why"  -->
# Why estimate $f(X)$?
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Prediction

- Predict $Y$ by $\hat Y =\hat f (X)$
- When do we care about "pure prediction"?
  - $X$ readily available but $Y$ is not
- $\hat f$ can be a **block box**:
  - the only concern is accuracy of the prediction

Notes:
- $\hat f = $ our estimate for $f$
- $\hat Y$ =resulting prediction for $Y$

--

## Inference

- Understanding the way that $Y$ is affected as $X_1,...,X_p$ change
  - Which predictors are associated with the response?
  - What is the relationship between the response and each predictor?

$\Rightarrow \hat f$ is cannot be a **black box** anymore

Notes:

Add a question: using examples, identify whether the questions relate to prediction or inference paradigm

--

## Approach in social science

- Objective: Understanding the way that $Y$ is affected as $X_1,...,X_p$ change
- The goal not necessarily to make predictions for $Y$
- Often linear function to estimate $Y$: $ f(X)=\sum_{i=1}^p \beta_i x_i$
- Assume  $ \epsilon \sim  N(0, \sigma^2)$
- Parameters $\beta$ are estimated by minimizing the sum of squared errors

$$ Y= \sum_{i=1}^p \beta_i x_i + \epsilon $$

Notes:
Assume that the error term is normally distributed with a zero mean :

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
- (We want to estimate unbiased coefficients)

--

## Approach in machine learning: prediction
$$ \hat Y = \hat f(X) $$
- Objectives:
  - find the “best” $f(·)$ and the “best” set of $X$’s which give the best predictions,$\hat Y$
  - **Accuracy**: find the function that <bcolor>minimize the difference between *predicted* and *observed* values</bcolor>
  - (We want to minimize prediction error)

Note:  Machine learning is primarily concerned with prediction


--

## Reducible and irreducible error
$\hat f(X)=\hat Y$ estimated function

$f(X)+\epsilon =\hat Y$ true function

- <bcolor>Reducible error</bcolor>: $\hat f$ is used to estimate f, but not perfect
  $\rightarrow$ accuracy can be improved by adding more features
- <bcolor>Irreducible error</bcolor>: $\epsilon$ = all other features that can be used to predict $f$ $\rightarrow$ unobserved $\rightarrow$ irreducible

--

## Reducible and irreducible error
$$\begin{align}
E(Y-\hat Y)^2 &= E[f(X)+\epsilon - \hat f (X)]^2 \\\\
      &= \underbrace{[f(X) - \hat f(X)]^2}_{Reducible} +  \overbrace{Var(\epsilon)}^{Irreducible} \\
\end{align}$$

$\Rightarrow$ **Objective**: estimating $f$ with the aim of minimizing the reducible error

Notes:
where $E(Y−\hat Y)^2$ represents the average, or expected value, of the squared expected value difference between the predicted and actual value of $Y$,and $Var(\epsilon)$ represents the variance associated with the error term.

We focus on estimating $f$ with the aim of minimizing the reducible error.
The irreducible error will always provide an upper bound on the accuracy of our prediction for $Y$. This bound is almost always unknown in practice.

---

<!-- .slide: id="how"  -->
# How do we estimate $f$?
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Context
We use observations to "teach" our ML algorithm to predict outcomes

- <bcolor>Training data</bcolor>: $ \\{ (x_1,y_1), (x_2,y_2), \dots, (x_n,y_n)\\} $
where $x_i=(x_{i1}, x_{i2}, \dots, x_{ip})^T$
- Goal: use the training data to estimate the unknown function $f$
- 2 types of SL methods: <bcolor>parameteric vs. nonparametric</bcolor>

--

### Parametric methods
**Model-based approaches**, 2 steps:

1. Specify a <bcolor>*parametric* (functional) form</bcolor> for $f(X)$, e.g. linear:
   $$ f(X) = \beta_0+\beta_1X_1+\cdots+\beta_pX_p$$
   (Parametric means that the function depends on a finitenumber of parameters, here $p+1$).

2. <bcolor>Training</bcolor>: Estimate the parameters by OLS and predict $Y$ by
   $$ \hat Y = \hat f(X)=\hat \beta_0+\hat \beta_1X_1+\cdots+\hat \beta_pX_p$$

Notes:
 - Parametric methods involve a two-step model-based approach.
 1. make an assumption about the functional form
 2. use the training data to fit or train the model
 $\Rightarrow$ reduces the problem of estimating $f$ down to one of estimating a set of parameters

--

### True function

<div class="r-stack"><img data-src="images/jwht-fig2-3.png" style="height: 400px;" > </div>

Notes:
The plot displays income as a function of years of education and seniority.
- The **blue surface** represents the true underlying relationship between income and years of education and seniority, which is known since the data are simulated.
- The **red dots** indicate the observed values of these quantities for30individuals

--

### Linear estimate

<div class="r-stack"><img data-src="images/jwht-fig2-4.png" style="height: 400px;" > </div>

Notes:
the true $f$ has some curvature that is not captured in the linear fit

--

### Parametric methods -- issues
Misspecification of $f(X)$

1. Rigid models (e.g. strictly linear) may not fit the data well
2. More flexible models require more parameter estimation $\rightarrow$ **overfitting**

Note:

--

### Non-parametric methods
- **No assumptions** about the functional form of $f$

- Estimates a function only **based on the data itself**.

- **Disadvantage**: very large number of observations is required to obtain an accurate estimate of $f$

--

### “Smooth” nonlinear estimate

<div class="r-stack"><img data-src="images/jwht-fig2-5.png" style="height: 400px;" > </div>

Notes:
The approach attempts to produce an estimate for $f$ that is as close as possible to the observed data, subject to the fit being smooth

--

### Rough nonlinear estimate with perfect fit $\Rightarrow$ overfit

<div class="r-stack"><img data-src="images/jwht-fig2-6.png" style="height: 400px;" > </div>

Notes:
But if we allow for a rougher fit, =>  zero errors on the training data.
= Example of OVERFITTING

--

## Recap: parametric vs. non-parametric approaches

<div style="position:relative;  text-align: center;" >
  <a href="https://app.sli.do/event/tevwuniu" target="_blank">
    <div style="position:absolute;  z-index:500;height:245px;width:100%;"></div>
    <iframe src="https://app.sli.do/event/tevwuniu/embed/polls/6285f58c-7406-45fe-a424-cc3ba1fdf010" width="300" height="500"></iframe>
  </a>
</div>

--

## Accuracy and interpretability tradeoffs

- <bcolor>More accurate</bcolor> models often require estimating <bcolor>more parameters</bcolor> and/or having more flexible models

- Models that are better at prediction generally are <bcolor>less interpretable</bcolor>.

- For inference, we care about interpretability.

$\rightarrow$ More on this next week!

---

<!-- .slide: id="ml"  -->
# Machine Learning: overview and examples
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Supervised vs. unsupervised learning
- <bcolor>Supervised learning</bcolor>: estimating functions with known observation and outcome data.
  - We observe data on $Y$ and $X$ and want to learn the mapping $\hat Y=\hat f(X)$
  - **Classification** when $\hat Y$ discrete; **regression** when $\hat Y$ continuous

- <bcolor>Unsupervised learning</bcolor>: estimating functions without the aid of outcome data.
  - We only observe $X$ and want to learn something about its structure
  - Clustering: Partition data into homogeneous groups based on X
  - Dimensionality reduction (e.g. PCA)

--

## The Machine learning landscape
<img data-src="images/machine_learning_landscape.jpeg"  style="height: 550px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

--

## Examples: Studies using ML for p rediction
<div style="font-size:80%;">
<ul>
  <li><a href "https://onlinelibrary.wiley.com/doi/full/10.1111/ecin.12364">Glaeser, Kominers, Luca, and Naik (2016)</a> use images from Google Street View to measure block-level income in New York City and Boston</li>
  <li><a href "http://science.sciencemag.org/content/353/6301/790"> Jean et al. (2016)</a> train a neural net to predict local economic outcomes from satellite data in African countries</li>
  <li><a href "https://www.aeaweb.org/articles?id=10.1257/aer.101.3.288"> Chandler, Levitt, and List (2011)</a> predict shootings among high-risk youth so that mentoring interventions can be appropriately targeted</li>
  <li><a href "https://academic.oup.com/qje/article-abstract/133/1/237/4095198?redirectedFrom=fulltext"> Kleinberg, Lakkaraju, Leskovec, Ludwig, and Mullainathan (2018)</a> predict the crime probability of defendants released from investigative custody to improve judge decisions</li>
  <li><a href "https://aclanthology.info/pdf/D/D13/D13-1150.pdf"> Kang, Kuznetsova, Luca, and Choi (2013)</a> use restaurant reviews on Yelp.com to predict the outcome of hygiene inspections</li>
  <li><a href "http://doc.rero.ch/record/308901/files/WP_SES_494.pdf">Huber and Imhof (2018) </a> use machine learning to detect bid-rigging cartels in Switzerland</li>
  <li><a href "https://homes.cs.washington.edu/~nasmith/papers/kogan+levin+routledge+sagi+smith.naacl09.pdf)">Kogan, Levin, Routledge, Sagi, and Smith (2009) </a> predict volatility of firms from market-risk disclosure texts (annual 10-K forms)</li>
  </ul>
</div>

--

## The Machine learning workflow

1. Look at the big picture.
2. Get the data.
3. Discover and visualize the data to gain insights.
4. Prepare the data for Machine Learning algorithms.
5. Select a model and train it.
6. Fine-tune your model.
7. Present your solution.8. Launch, monitor, and maintain your system

<i class="fa fa-book fa-fw" aria-hidden="true"></i>
Aurelien Geron, *Hands-on machine learning with Scikit-Learn & TensorFlow*, Chapter 2

---

<!-- .slide: id="conclusion"  -->
# Conclusion:
## Econometrics vs. Machine Learning
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
