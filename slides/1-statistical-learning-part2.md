# Big Data for Public Policy
## Statistical Learning [Part 2]
### [Malka Guillot](https://malkaguillot.weebly.com/)
### ETH Zürich | <a href="https://malkipp.github.io/big_data_policy_2021/">860-0033-00L</a>

---

# Turn on recording

---


<!-- .slide:  id="toc" class: left, inverse -->
## Table of contents

1. [Prologue](#prologue)

2. [Model accuracy](#accuracy)

3. [The Bias-Variance Trade Off](#bias_variance)

3. [How to choose training and test set?](#train_test)

Notes: my notes

---

<!-- .slide: id="prologue"  -->
# Prologue
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Coming back on the homework
- Most challenging homework
- Great spirit on the forum!
- Organizing an intro to python session (voluntary participation)

--

## By now you should have:

- Installed Anaconda, with Jupyter-notebook and Spyder
- (Installed Git)
- Created a GitHub account
- Joined the Moodle class
- Registered for a presentation

--

### Last week
- What is statistical learning?
- Statistics in social science – causality.
- Statistics in machine learning – prediction.
- Accuracy v. interpretability.

### Today
- [Model accuracy](#accuracy)
- The bias-variance tradeoff.
- Classification

Reference: [JWHT](https://static1.squarespace.com/static/5ff2adbe3fe4fe33db902812/t/601cc86d7f828c4792e0bcae/1612499080032/ISLR+Seventh+Printing.pdf), chap 2.2 & 5.1

---

<!-- .slide: id="accuracy"-->
# Model Accuracy
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

Notes:
In order to evaluate the performance of a statistical learning method on a given data set, we need some way to measure how well its predictions actually match the observed data

--

## Mean Squared Error (MSE)

`$$MSE= \frac{1}{n} \sum_{i=1}^n (y_i - \hat f(x_i))^2$$`

- **Regression setting**: the <bcolor>mean squared error</bcolor> is a metric of how well a model fits the data.

- But it’s <bcolor>in-sample</bcolor>.  

- What we are really interested in is the <bcolor>out-of-sample</bcolor> fit!

Notes:

MSE will be small if the predicted responses are very close to the true responses,and will be large if for some of the observations, the predicted and true responses differ substantially

--

## Measuring fit (1)

- We would like $(y_0 - \hat f(x_0))^2$ to be small for some $(y_0, x_0)$, not in our training sample $\{(x_i, y_i)\}_{i=1}^n$.

- Assume we had a large set of observations $(y_0, x_0)$ (a test sample),

- then we would like a low
  $$ Ave(y_0 - \hat f(x_0))^2$$

- i.e a low average squared prediction error (test MSE)

--

## Measuring fit (2)

To estimate model fit we need to partition the data:

1. <bcolor>Training set</bcolor>: data used to **fit** the model
  - <bcolor>Training MSE</bcolor>: how well our model fits the training data.
2. <bcolor>Test set</bcolor>: data used to **test the fit**
  - <bcolor>Test MSE</bcolor>: how well our model fits new data

We are most concerned in <bcolor>minimizing test MSE</bcolor>

--

## Training MSE, test MSE and model flexibility

<img data-src="images/jwht-fig2-9.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block" >
Red (grey) curve is test (train) MSE

Increasing model flexibility tends to <bcolor>decrease</bcolor> training MSE but will eventually <bcolor>increase</bcolor> test MSE

Notes:

- Left:Data simulated from $f$, shown in black.
- Three estimates of $f$ are shown:
    - the linear regression line (orange curve),
    - and two smoothing splinefits (blue and green curves).
- Right:Training MSE (grey curve), test MSE (red curve), and minimum possible test MSE over all methods (dashed line).
- Squares represent the training and test MSEs for the three fits shown in the left-hand panel.

- we observe a monotone decrease in the training MSE and a U-shape in the test MSE

--

## Overfitting

- As model flexibility increases, training MSE will decrease, but the test MSE may not.

- When a given method yields a small training MSE but a large test MSE, we are said to be **overfitting** the data.

- (We almost always expect the training MSE to be smaller than the test MSE)

- Estimating test MSE is important, but requires training data...


---

<!-- .slide: id="bias_variance"  -->
# The Bias-Variance Trade-Off
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>


Notes:
The U-shape observed in the test MSE curves (Figures2.9  –2.11  ) turns out to be the result of two competing properties of statistical learning methods.

--

## Decomposing the expected (test) MSE

$$ E(y_0 - \hat f(x_0))^2 = Var(\hat f(x_0)) + [Bias(\hat f(x_0))]^2 + Var(\epsilon)$$

3 components:
1. $ Var(\hat f(x_0))=$ Variance of the predictions
   - how much would $\hat f$ change if we applied it to a different data set
2. $[Bias(\hat f(x_0))]^2=$ Bias of the predictions
   - how well does the model fit the data?
3. $Var(\epsilon)=$ variance of the error term

Notes:

-  notation $E(y_0 - \hat f(x_0))^2 $ defines the expected test MSE, and refers expected test MSE to the average test MSE that we would obtain if we repeatedly estimated $f$ using a large number of training sets, and tested each at $x_0$
- to minimize E, need to minimize both variance and bias
- the expected test MSE can never lie below $Var(\hat f(x_0))$, the irreducible error

- more flexible methods, the variance will increase and the bias will decrease

--

## The bias-variance tradeoff

<img data-src="images/jwht-fig2-9-11.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

- less flexibility $\rightarrow$ high bias and low variance

- more flexibility $\rightarrow$ low bias and high variance

Models that are too flexible or expressive or complex overfit!!

Notes:
- Simple models give consistent results across test sets (low variance) but don’t predict well. (high bias).
- Very flexible (complex) models give inconsistent results across test sets (high variance), but do well at prediction(low bias).

--

## Accuracy in Classifications

$$ \textrm{(training) error rate}=\frac{1}{n}\sum_{i=1}^n 1(y_i\neq \hat y_i)$$

$$ \textrm{(test) error rate}=Ave(1(y_0\neq \hat y_0))$$

- MSE in the context of regression (continuous predictor).

- Modifications in the setting in which we’re interested in prediction classes

- We are essentially interested in what % of classifications are correct.

- For cross-validation we could also use the estimated test error rate


---

<!-- .slide: id="train_test"-->
# How to choose training and test set?
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

Notes:
In real life situation, it is generally not possible to explicitly compute the test MSE, bias, or variance for a statistical learning method

They involve repeatedly drawing samples from a training set and refitting a model of interest on each sample in order to obtain additional information about the fitted model

--

## Resamling methods

Estimate the test error rate by

<bcolor>holding out</bcolor> a subset of the training observations from the fitting process,

$+$ then <bcolor>applying</bcolor> the statistical learning method to those held out observations

--

## Validation set approach
- Randomly divide labeled data <bcolor>randomly</bcolor> into two parts: training and test (validation) sets.

<div class="r-stack"><img src="https://docs.splunk.com/images/thumb/3/3b/TrainTest.png/550px-TrainTest.png
" style="height: 400px;" > </div>

--

## Two concerns
- Arbitrariness of split
- Only use parts of the data for estimation

  $\rightarrow$ we tend to overestimate test MSE because our estimate of $f(x)$ is less precise

--

## Leave-One-Out Cross-Validation (LOOC)

- Fit on $n−1$ training observations, and a prediction the Last
- Iterate $n$ times
- Assess the average model fit across each test set.

Estimate for the test MSE:
`$$ CV_n=\sum_{i=1}^n MSE_i$$`

--

## Leave-One-Out Cross-Validation (LOOC)
<div class="r-stack"><img data-src="images/jwht-fig5.3.png" style="height: 400px;" > </div>

- less bias than the validation set approach
- always yield the same results
- potentially too expensive to implement

Notes:
- less bias because tends not to overestimate the test error rate as much as the validation set approach does


--

## $k$-fold Cross-validation
- Leave-One-Out Cross-Validation with $k=1$
- Randomly dividing the data into the set of observations into $k$ groups
- 1st fold is treated as a validation set, and the method is fit on the remaining $k−1$ folds
- Iterate $k$ times


Estimate for the test MSE:
`$$ CV_k=\sum_{i=1}^k MSE_i$$`


--

## $k$-fold Cross-validation
<div class="r-stack"><img data-src="images/jwht-fig5.5.png" style="height: 400px;" > </div>

$\Rightarrow$ Arguably the contribution to econom(etr)ics: Cross-validation (to estimate test MSE)!

--

##  Bias-Variance Trade-Off $f$-Fold Cross-Validation
Bias
- **validation set approach** can lead to overestimates of the test error rate
- **1-fold validation**: almost unbiased estimates of the test error
- **k-fold validation** is in between

Variance
- **1-fold validation**: higher variance
- **k-fold validation**: lower variance

$k=5$ or $k=10$ is a good benchmark


---

# Turn off recording
