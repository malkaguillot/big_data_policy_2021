# Big Data for Public Policy
## Regressions
### [Malka Guillot](https://malkaguillot.weebly.com/)
### ETH Zürich | <a href="https://malkipp.github.io/big_data_policy_2021/">860-0033-00L</a>

---

# <i class="fas fa-video"></i> Turn on recording

---


<!-- .slide:  id="toc" class: left, inverse -->
## Table of Contents

1. [Prologue](#prologue)
2. [Linear Regression](#linear)
2. [Regularized Regression](#linear)
2. [Final Toughts](#final)

---

<!-- .slide: id="prologue"  -->
# Prologue
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>
<!--  
Things to clarify:
  - what is on the moodle & what is on the GitHub
    - github: things that go public
    - moodle: private documents
    - Also: notebooks depend on images => need for the github folder
    - you can print the html slides yourselves to pdf: by using print on your browser
  - Post class discussion on the course projects
  - You cannot view the notebooks as slides unless you install more options, but why would you?


-->

--

## Coming Back on the Homework

Notes:

- gradient descent
- Reading for next week
- Announce the group project discussion at the end

--

### Last Week
- Model accuracy

### Today
- Regression analysis (continuous outcome)
- Our first ML project!


Reference:
- [JWHT](https://static1.squarespace.com/static/5ff2adbe3fe4fe33db902812/t/601cc86d7f828c4792e0bcae/1612499080032/ISLR+Seventh+Printing.pdf), chap 3, 6.2
- Geron, chapter 2


### Next Week
- Classification (binary outcome)

---

# Linear Regression as a Predictive Model
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Linear Regression

$$Y=\beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p + \epsilon $$

$=$ one of the simplest algorithms for doing supervised learning

A good starting point before studying more complex learning methods

Notes:
Interpretation of $\beta_j$ = the average effect on $Y$ of a unit increase in $X_j$ holding all other predictors fixed

--

## Estimation by Ordinary Least Squares

$RSS=\textrm{Residual sum of squares}=\sum_{i=1}^n (y_i - \hat y_i)^2$

Minimizing RSS gives a <bcolor>closed form solution</bcolor> for the  $\hat \beta_1,\cdots \hat \beta_p$

Most ML models <bcolor>do not</bcolor> have a a colsed form solution

--

<img data-src="images/jwht-fig3-4.png"  style="height: 400px; position:relative;     margin-left: auto;margin-right: auto;display: block" >


--

## Extensions of the Linear Model

Going further model's assumptions:

- the <bcolor>additive</bcolor>: the effect of changes in a predictor $X_j$ on the response $Y$ is independent of the values of the other predictors

-  <bcolor>linearity</bcolor>: the change in the response $Y$ due to a one-unit change in $X_j$ is constant

--

### Interactions
- Adding interacted variable can help
- Should respect the <bcolor>hierarchy principle</bcolor>:
  - if an interaction is included, the model should always include the main effects as well

Notes:
- Even if the p-value associated with their coef is not significant
- Interactions are hard to interpret without main effects in the model

--

### Non Linearity
- Include transformed versions of the predictors in the model


$\Rightarrow$ Including polynomials in $X$ may provide a better fit

--

## Linear Models: pros and cons
- [Pros]():
  - Interpretability
  - Good predictive performance
  - Accuracy measures for
      - coefficient estimates (standard errors and confidence intervals)
      - the model

- [Cons]():
  - When $p>n$
  - Tend to over-fit training data.
  - Cannot handle multicollinearity.

--

## Generalization of the Linear Models
- <bcolor>Classification problems</bcolor>: logistic regression, support vector machines

- <bcolor>Non-linearity</bcolor>: nearest neighbor methods

- <bcolor>Interactions</bcolor>: Tree-based methods, random forests and boosting

- <bcolor>Regularized fitting</bcolor>: ridge regression and lasso

Notes:
In much of the rest of the class, we discuss methods that expand the scope of linear models and how they are fit:

---

<!-- .slide: id="regularized"  -->
# Regularized Regressions
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Why Regularization?

- Solution against <bcolor>over-fitting</bcolor>

-  Allow High-Dimensional Predictors
  - $p>>n$: OLS no longer has a unique solution
  - $x_i$ "high-dimensional" i.e. very many regressors
    - pixels on a picture

Notes:
Corollary of regularization:
- Prediction Accuracy:especially when $p > n$, to control the variance

--

## Adding a Regularization Term to the Loss Function $L(.)$

`$$ \hat \beta =arg min_\beta \frac{1}{n} \sum_{i=1}^n L(h(x_i, \beta), y_i) +\lambda R(\beta) $$`

- $R(\beta)$ = <bcolor> regularization  function </bcolor>
  - $R(\beta)=\sum_{i=1}^n p(\beta_i)$ for $p(.)$ the penalty function

- $\lambda$ is a <bcolor>hyperparameter</bcolor> where higher values increase regularization


--

## Different Penalty Functions $p()$
- <bcolor>Ridge (L2)</bcolor>: $p(\beta_j)=\beta_j^2$

- <bcolor>LASSO (L1)</bcolor>: $p(\beta_j)=|\beta_j|$

- <bcolor>Elastic Net</bcolor>: $p(\beta_j)=\alpha |\beta_j| + (1-\alpha) \beta_j^2$

- <bcolor>Subset selection</bcolor>: $p(\beta_j)=1\\{\beta_j\neq 0\\}$

Notes:
- **Ridge**: shrinks coefficients toward zero and helps select between collinear predictors.
- **Lasso** automatically performs feature selection and outputs a sparse model.


--

## How to Solve Without a Closed-form Solution? Gradient Descent
<img data-src="images/gradient-descent.jpeg"  style="height: 400px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

Gradient descent measures the local gradient of the error function, and then steps in that direction.

$\rightarrow$ Minimum in 0

Notes:
- Gradient Descent is a first-order iterative optimization algorithm for finding the local minimum of a differentiable function
  - because it uses the first-order derivative of the loss function to find minima
- Initialize the parameters(weights and bias) randomly.
- In each iteration we move a step in direction of steepest descent
- The size of each step is determined by a parameter which is called Learning Rate

--

## Stochastic Gradient Descent

1. Picks a <bcolor>random instance</bcolor> in the training set

2. Computes the gradient only for that single instance

- [**Pro**](): SGD is much faster to train,

- [**Cons**](): bounces around even after it is close to the minimum.

$\rightarrow$ Compromise: <bcolor>mini-batch gradient descent</bcolor>, selects a sample of rows (a “mini-batch”) for gradient compute

Notes:
- Instead of just randomly sampling one point at each step (SGD), the **“mini-batch”** gradient descent samples a small number of points.
- Mini-batch tries to strike a balance between the goodness of gradient descent and speed of SGD.


--

## Varients of Gradient Descent
<img data-src="images/gradient-descent-details.png"  style="height: 400px; position:relative;     margin-left: auto;margin-right: auto;display: block" >




--

## Ridge Regression

$min_{\beta} \sum_{i=1}^n (y_i - \hat y_i)^2 + \lambda \sum_{j=1}^p \beta_j^2 $

Where
- $\lambda > 0$ = penalty parameter
- covariates can be high-dimensionnal $p>>N$

Trade-off, from the minimization of the sum of
1. RSS
2. shrinkage penalty: decreases with $\beta_j$

$\rightarrow$ relative importance given by $\lambda$

Notes:
- The tuning parameter $\lambda$ serves to control the relative impact of these two terms on the regression coefficient estimates.
- When $\lambda=0$, the penalty term has no effect, and ridge regression will produce the least squares estimates
- when $\lambda \rightarrow \infty$ : penalty grows and coefficient estimates approach zero

--

## Ridge Regression: shrinkage to $0$
<img data-src="images/jwht-fig6-4.png"  style="height: 400px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

Notes:
Next: Why Does Ridge Regression Improve Over Least Squares?

--

## Ridge: Variance-Bias Trade-Off
<img data-src="images/jwht-fig6-5.png"  style="height: 400px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

Squared bias (black), variance (green), [test] MSE (red)

Notes:
- As $\lambda$ increases, the flexibility of the ridge regression fit decreases, leading to decreased variance but increased bias
- Up to 10, the variance decreases rapidly, with very little increase in bias
- Beyond this point, the decrease in variance due to increasing $\lambda$ slows, and the shrinkage on the coefficients causes them to be significantly underestimated
- Recall that the test MSE (purple), is a function of the variance plus the squared bias.

--

## Ridge vs. Linear Models

- when outcome and predictors are close to having a linear relationship, the OLS will have low bias but potentially high variance
  - small change in the training data $\rightarrow$ large change in the estimates
  - worse with $p$ close tp $n$
  - if $p>n$, OLS do not have a unique solution

$\rightarrow$ ridge regression works best in situations where the least squares estimates have high variance

--

## LASSO
Overcome an important drawback of Ridge (all $p$ predictors are included in the final model)

LASSO proposes a method to build a model which just <bcolor>includes the most important predictors</bcolor>.

Better for interpretability than Ridge!

Notes:
Ridge: the penalty shinks coefficients toward $0$ but not exactly to $0$

This may not be a problem for prediction accuracy, but it can create a challenge in model interpretation when $p$ is quite large

--

## Lasso Coefficients
<img data-src="images/jwht-fig6-6.png"  style="height: 400px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

Notes:
- When $\lambda=0$: the lasso simply gives the least squares fit
- when $\lambda$ becomes sufficiently large, the lasso gives the null model in which all coefficient estimates equal 0.
- in between these two extremes, the ridge regression and lasso models are quite different from each other

--

## Lasso: Variance-Bias Trade-Off
<img data-src="images/jwht-fig6-8.png"  style="height: 400px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

Squared bias (black), variance (green), [test] MSE (red)

--

## Constrained Regression
The minimization problem can be written as follow:

`$$ \sum_{i=1}^n(y_i-x_i'\beta)^2 \textrm{ s.t. } \sum_{j=1}^p p(\beta_j) \leq s,$$`

Where
- Ridge: $\sum_{j=1}^p \beta_j^2 <s $
$\rightarrow$ equation of a <bcolor>circle</bcolor>
- Lasso: $\sum_{j=1}^p |\beta_j| <s $
$\rightarrow$ equation of a <bcolor>diamond</bcolor>

Notes:
- Lasso:  we try to find the set of coefficient estimates that lead to the smallest RSS, subject to the constraint that there is a budgets for how large $\sum_{j=1}^p |\beta_j|$ can be.
- if $s$ is extremely large, it is not very restrictive and the least square solution falls within the budget

--

## Constraint Regions
| Lasso | Ridge|
|:------:|:---:|
|<img data-src="images/jwht-fig6-7lasso.png"  style="height: 350px;" > | <img data-src="images/jwht-fig6-7ridge.png" style="height: 350px" class="center"> |


Notes:
- Why is it that the lasso, unlike ridge regression, results in coefficient estimates that are exactly equal to zero?
- diamonds & circle represent the ridge & lasso constraint regions
- the red ellipses are the contours of the RSS (for different levels of RSS): regions centered around $\beta$ of constant value of RSS
- $\hat \beta$ is the least square estimate
- the lasso constraint has corners at each of the axes, and so the ellipse will often intersect the constraint region at an axis $\rightarrow$ When this occurs, one of the coefficients will equal zero.

--

## Elastic Net = Lasso + Ridge
$$ MSE(\beta)+\lambda_1 \sum_{j=1}^p |\beta_j| +\lambda_2 \sum_{j=1}^p \beta_j^2$$

$\lambda_1$, $\lambda_2$ $=$ strength of L1 (Lasso) penalty and L2 (Ridge) penalty

--

## Selecting Elastic Net Hyperparameters

- Elastic net <bcolor>hyperparameters</bcolor> should be selected to optimize out-of-sample fit (measured by mean squared error or MSE).

- <bcolor>“Grid search”</bcolor>
  - scans over the hyperparameter space ($\lambda_1 \geq 0, \lambda_2\geq 0$),
  - computes out-of-sample MSE for all pairs $(\lambda_1, \lambda_2)$ ,
  - selects the MSE-minimizing model.

--

## Evaluating Regression Models: $R^2$
MSE is good for comparing regression models, but the units depend on the outcome variable and therefore are not interpretable

Better to use $R^2$ in the test set, which has same ranking as MSE but it <bcolor>more interpretable</bcolor>.

Notes:
$R^2$ proportion of the variance in the dependent variable that is predictable from the independent variable(s)

---

<!-- .slide: id="final"  -->
# Final Toughts
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Selecting the Tuning Parameter By Cross-Validation
1. Choose a <bcolor>grid</bcolor> of $\lambda$ values
2. Compute the <bcolor>CV error</bcolor> for each lambda
3. Select the tuning parameter value for which the CV error is smallest
4. <bcolor>Re-fit</bcolor> the model using all available observation and the best $\lambda$


--

## Data Prep for Machine Learning
- See Geron Chapter 2 for [pandas]() and [sklearn]() syntax:
  - imputing missing values.
  - feature <bcolor>scaling</bcolor> (coefficient size depends on the scaling)
  - <bcolor>encoding</bcolor> categorical variables.

- Best practice
  - <bcolor>reproducible</bcolor> data pipeline
  - <bcolor>standardize</bcolor> coefficients

--

## Other Supervised Machine Learning Methods
- Forward Selection,
- Backward Selection
- Trees and Forests
- Neural Networks
- Boosting
- Ensemble Methods

--

> “Essentially, all models are wrong, but some are useful”
-- George Box

---


# Turn off recording <i class="fas fa-video"></i>
