

# Big Data for Public Policy

## Classification
### [Malka Guillot](https://malkaguillot.weebly.com/)
### ETH Zürich | <a href="https://malkipp.github.io/big_data_policy_2021/">860-0033-00L</a>

---

# <i class="fas fa-video"></i> Turn on recording

---


<!-- .slide:  id="toc" class: left, inverse -->
## Table of Contents

1. [Prologue](#prologue)
1. [Introduction](#introduction)
2. [Performance Measures](#performance)
2. [Binary Classifier](#binary)
2. [Multi-class Model](#multi)
2. [Wrap up](#wrap)

Notes:

---

<!-- .slide: id="prologue"  -->
# Prologue
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

### Last Week
- Regression analysis (continuous outcome)
- Unsupervised learning

### Today
- Classification (binary outcome)

Reference:
- [JWHT](https://static1.squarespace.com/static/5ff2adbe3fe4fe33db902812/t/6009dd9fa7bc363aa822d2c7/1611259312432/ISLR+Seventh+Printing.pdf): chap 2.2.3, 4

### Next Week
- Text data [Elliott Ash ]

---

<!-- .slide: id="intro"-->
# Introduction
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Classification Framework

-   Response/target variable $y$ is **qualitative** (or
    **categorical**):

    -   2 categories $\rightarrow$ binary classification

    -   More than 2 categories $\rightarrow$ multi-class classification

-   Features $X$:

    -   can be high-dimensional

-   We want to assign a class to a **quantitative response**

    $\rightarrow$ probability to belong to the class

-   **Classifier**: An algorithm that maps the input data to a specific
    category.

-   Performance measures specific to classification

--

## Application examples

-   In business:

    -   Loan default prediction

    -   Type of costumer

-   In public economics:

    -   Tax evasion prediction

-   In political sciences:

    -   political affiliation of author of texts

-   In medical sciences:

    -   Diagnostic diseases, drug choice

-   Other:

    -   email filtering, speech recognition...

--


## Predicting corruption based on public finance account>

**Ash, Galetta and Giommoni (2020) A Machine Learning Approach to Analyzing Corruption in Local Public Finances.**

-   Predict corruption from budget accounts in Brazilian municipalities that have been audited for corruption

    -   train set: Using an innovative anticorruption program: **audit
        lotteries**

    -   Features: local public finance data

    -   Gradient boosting algorithm: Test-set accuracy of 75%, much better than guessing (58%) and predictions from OLS (59%)

-   Used to evaluate the dynamic (and spillover) effects of audits

$\rightarrow$  inputs to policy decisions about corruption

--

## Predicting corruption based on public finance account

<img data-src="images/REG_PLOT_FTTF.png"  style="height: 350px; position:relative;background-color:white;   margin-left: auto;margin-right: auto;display: block" >

Notes. Binscatter diagram of average true corruption (vertical axis) against binned predicted corruption (horizontal axis).

--

## Applying to Full Dataset

Take model trained on audited municipality-terms and predict probability of corruption in all municipalities and all years

[fig:map] Actual Prediction

--

## Why not fitting a linear regression?

-   **Technically possible** to fit a linear model using a categorical
    response variable but it implies

    -   an **ordering** on the outcome

    -   a **scale** in the class difference

$\rightarrow$  If the response variable was coded differently, the results could be
    completely different

-   Less problematic if the response variable is **binary**

    -   The result of the model would be stable

    -   But prediction may lie outside of $[0, 1]$: hard to interpret
        them in terms of probabilities

Notes:

--

## Example

-   We predict $y$, the **occupation of individuals**:
  $$y = \\{
    \\begin{array}{cc}
      0 & \textrm{ if blue-collar} \\\\
      1 & \textrm{ if white-collar}
    \\end{array}
    $$
-   based on their characteristics $X$ (gender, wage, contract duration,
    experience, age...)

<img data-src="images/logistic-vs-linear.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >


--

## Linear Regression vs Binary Classifier

-   We model the probability of belonging to a category
    $$P(y=1 \mid X)$$

-   We can rely on this probability to assign a class to the
    observation.

    -   For example, we can assign the class yes for all observations
        where $P(y = 1 | x) > 0.5 $

    -   But we can also select a different **threshold**.


---

<!-- .slide: id="performance"  -->
# Performance measures
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>


--

## Confusion Matrix

- For comparing the predictions of the fitted model to the actual classes.

- After applying a classifier to a data set with known labels *Yes* and *No*:

<table>
<thead>
  <tr>
    <th></th>
    <th></th>
    <th colspan="2">Predicted class</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td></td>
    <td>no</td>
    <td>yes</td>
  </tr>
  <tr>
    <td rowspan="2">True class</td>
    <td>no</td>
    <td style="color:#90EE90;">TN</td>
    <td style="color:orange;">FP</td>
  </tr>
  <tr>
    <td>yes</td>
    <td style="color:yellow;">FN</td>
    <td style="color:green;">TP</td>
  </tr>
</tbody>
</table>


--

## Precision and Recall

-   <bcolor>Precision</bcolor>

    -   accuracy of positive predictions.

    -   $  \frac{{\color{green}{\text{True Positives}}}}{{\color{green}{\text{True Positives}}} +  {\color{orange}{\text{False Positives}}}}$

    -   decreases with false positives.

-   <bcolor>Recall</bcolor>

    -   true positive rate.

    -   $  \frac{{\color{green}{\text{True Positives}}}}{{\color{green}{\text{True Positives}}} +  {\color{yellow}{\text{False Negatives}}}}$

    -   decreases with false negatives.


--

## F1 Score

-   The $F_{1}$ score provides a single combined metric it is the **harmonic mean** of precision and recall

    $$\begin{aligned}
    F_{1} &= \frac{2}{\frac{1}{\text{precision}}+\frac{1}{\text{recall}}}
    = 2\times\frac{\text{precision}\times\text{recall}}{\text{precision}+\text{recall}} \\\\
    &=  \frac{\text{Total Positives}}{\text{Total Positives}+\frac{1}{2}(\text{False Negatives}+\text{False Positives})}
    \end{aligned}$$

-   The harmonic mean gives **more weight to low values**.

-   The F1 score values precision and recall **symmetrically**.

--

## The Precision/Recall Trade-off

- $F_1$ favors classifiers with similar precision and recall,
- but sometimes you want **asymmetry**:

1.   <bcolor>low recall + high precision is better</bcolor>

    -   e.g. **deciding “guilty” in court**, you might prefer a model that
    -   lets many actual-guilty go free (high false negatives
        $\leftrightarrow$ low recall)...
    -   ... but has very few actual-innocent put in jail (low false
        positives $\leftrightarrow$ high precision

2.   <bcolor>high recall + low precision is better</bcolor>

--

## The Precision/Recall Trade-off
- $F_1$ favors classifiers with similar precision and recall,
- but sometimes you want **asymmetry**:

1.   <bcolor>low recall + high precision is better</bcolor>
2.   <bcolor>high recall + low precision is better</bcolor>

    -   e.g classifier to **detect bombs during flight screening**, you
        might prefer a model that:
    -   has many false alarms (low precision)...
    -   ... to minimize the number of misses (high recall).


--

## ROC Curve and AUC

-   Plots *true positive rate* (recall) against the *false positive rate* ($\frac{FP}{FP + TN}$):

<img data-src="images/roc-curve.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

Notes:
- ROC= "receiver operating characteristics"
- The ROC curve is a popular graphic for simultaneously displaying the ROC curve 2 types of errors for classification problems at various threshold settings
- It tells how much the model is capable of distinguishing between classes.
- An ideal ROC curve will hug the top left corner, so the larger area under the (ROC) curve the AUC the better the classifier

--

## ROC Curve and AUC

-   The area under the ROC curve (AUC) is a popular metric ranging between:

    -   0.5

        -   **random classification**
        -   ROC curve $=$ first diagonal

    -   and 1

        -   **perfect classification**
        -   $=$ area of the square

    -   better classifier $\rightarrow$ ROC curve toward the top-left
        corner

-   Good measure for model comparison


---

<!-- .slide: id="binary"  -->
# Binary Classifier
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

- Logistic Regressions
- K-Nearest Neighbors
- Support Vector Machine


--

## Logistic Regression


-   Like OLS, logistic “regression” computes a weighted sum of the input features to predict the output.

    -   But it transforms the sum using the **logistic function**.
        $$\hat{p}=\Pr(Y_{i}=1)=\sigma(\theta'x)$$ where
        $\sigma(\cdot)$ is the sigmoid function
        $$\sigma(a)=\frac{1}{1+\exp(-a)}$$

--

## Logistic Regression

  <img data-src="images/ml-book/sigmoid.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

-   Prediction:
  $$\hat{y} = \\{
     \\begin{array}{cc}
       0 & \textrm{ if } \hat{p}<.5 \\\\
       1 & \textrm{ if } \hat{p}\geq.5
   \\end{array}
  $$

--

## Logistic Regression Cost Function

-   The cost function to minimize is
<img data-src="images/log-reg-cost-function.png"  style="height: 130px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

  -   this does not have a closed form solution

  -   but it is convex, so gradient descent will find the global
      minimum.

-   Just like linear models, logistic can be regulared with L1 or L2
    penalties, e.g.:
    $$J_{2}(\theta)=J(\theta)+\alpha_{2}\frac{1}{2}\sum_{i=1}^{n}\theta_{i}^{2}$$


--

## Naive Bayes Classifier

-   Relies on the observed conditional probabilities (and the Bayes theorem)

-   For a 2-class problem for a given observation $X=x_0$:

    -   Predict class 1 if $P(Y=1| X=x_0) \geq  0.5 $

    -   Predict class 0 if $P(Y=1| X=x_0) < 0.5$

-   Relies on the independence assumption

Notes:
- It is possible to show that the test error rate is minimized, on average, by a very simple classifier
  - assigns each observation to the most likely class, given its predictor values.
  - we should simply assign a test observation with predictor vectorx0to the class $j$ for which the proba is the largest
- Based on the conditional probabilities


--

## Naive Bayes Classifier
<img data-src="images/jwht-fig2-13.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

Notes:
- simulated data set consisting of 100observations in each of two groups, indicated in blue and in orange.
- The purple dashed line represents the Bayes decision boundary.
- The orange background grid indicates the region in which a test observation will be assigned to the orange class, and
- the blue background grid indicates the region in which a test observation will be assigned to the blue class.

--

## K-Nearest Neighbors

-   With real data, we do not know the conditional distribution of Y  given X.

-   computing the Bayes classifier is not possible.

-   The K-nearest neighbors (KNN) classifier estimates the conditional distribution of Y given X.

-   Approximate Bayes decision rule in a subset of data around the testing point

-   **Non-parametric method** often successful in classification situations where the **decision boundary is very irregular**

Notes:
- the Bayes classifier serves as an unattainable gold standard against which to compare other methods


--

## K-Nearest Neighbors

For $K$ and a test observation $x_0$
1. KNN classifier first identifies the $K$ points in the training data that are closest to $x_0$ (i.e $N_0$)
2. estimates the conditional probability for class $j$ as the fraction of points in $N_0$ whose response values equal $j$:

$$ P(Y=j|X=x_O) = \frac{1}{K}\sum_{i \in N_O} I (y_i=j)$$

3. applies Bayes rule and classifies the test observationx0tothe class with the largest probability


--

## KNN: illustration

<img data-src="images/jwht-fig2-14.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

- Assume $K=3$
- Left: small training data set consisting of 6 blue and 6 orange observations
- Right: KNN approach at of the possible values for $X_1$ and $X_2$, and  corresponding KNN decision boundary

Notes:
- goal is to make a prediction for the point labeled by the black cross
1. KNN finds the 3 observations that are closest to the cross
2. neighborhood is 1/3 orange & 2/3 blue $\rightarrow$ the cross belongs to the blue class


--

## KNN: illustration

<img data-src="images/jwht-fig2-15.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

- black curve: KNN decision boundary
- dashed line: Bayes decision boundary

Notes:
- KNN can often produce classifiers that are surprisingly close to the optimal Bayes classifier

--

## KNN: choice of $K$

<img data-src="images/jwht-fig2-17.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

- $K=1$,the KNN training error rate is $0$, but the test error rate may be quite high

Notes:
- with more flexible classification methods, the training error rate will decline but the test error rate may not

--

## Support Vector Machine

-   Context: developed in the mid-1990s

-   A generalization of the early logistic regression (1930s)

-   One of the best “out of the box” classifiers

-   Core idea: hyperplane that separates the data as well as possible,   while allowing some violations to this separation

Notes:
- an approach for classification that was developed in the computer science community in the 1990s
-

--

### Support Vector Machine: context and concepts

-   [Pieces of the puzzle]():

    1.  A <bcolor>maximal margin classifier</bcolor>: requires that classes be
        separable by a linear boundary.

    2.  A <bcolor>support vector classifier</bcolor>: extension of the maximal margin classifier.

    3.  <bcolor>Support vector machine</bcolor>: further extension to accommodate  non-linear class boundaries.

-   For binary classification, can be extended to multiple classes

Notes:
- People often loosely refer to the **maximal margin classifier**, the **support vector classifier**, and the support vector machine as **“support vector machines”**.

--

## Classification and Hyperplane

A perfectly separating linear hyperplan for a binary outcome<img data-src="images/svm1.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

There are an infinity of such separating hyperplan\
$\rightarrow$ we need to choose one

Notes:
- If a separating hyperplane exists, we can use it to construct a very natural classifier:
    - a test observation is assigned a class depending on which side of the hyperplane it is located
- but then if there exists 1 separating hyperplan, there exist an infinity

--

## Maximum Margin

Maximum margin classifier for a perfectly separable binary
outcome variable  <img data-src="images/svm2.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

<bcolor>Criterium for optimal choice</bcolor>: the separating hyperplane for which the margin is the farthest from the observations\
i.e., to select the <bcolor>maximal margin hyperplane</bcolor>

Notes:
- **Methodo**:  
  - compute the (perpendicular) distance from each training observation to a given separating hyperplane;
  - the smallest such distance is the minimal distance from the observations to the hyperplane $=$ the *margin*
- We can then classify a test observation based on which side of the maximal margin hyperplane it lies.
- This is known as the maximal margin classifier.
- On the figure:
  - 3 training observations are equidistant from the max maring hyperplane = **support vector**


--

## Support Vector

<bcolor>Support vector</bcolor> = the 3 observations from the training set that are
equidistant from the maximal margin hyperplane

$\rightarrow$ they “support” the maximal margin hyperplane (if they
move, the the maximal margin hyperplane also moves)

--

## Overcoming the perfectly separable hyperplan assumption

 We allow some number of observations to violate the rules so that they can lie on the wrong side of the margin boundaries.

$\rightarrow$ find a hyperplane that almost separates the classes

The <bcolor>support vector classifier</bcolor> generalizes the maximum margin classifier to the non-separable case.

--

## Support Vector Classifiers

Maximal margin classifier (left) and support vector classifier
(right) <img data-src="images/svm3.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

Notes:
- **pb** of Maximal margin hyperplan: only perfect classification, by essence overfits the training dataset
- **Advantages** of SVC (vs MMH):
  - Greater robustness to individual observations
  - Better classification of most of the training observations

--

## Support Vector Classifiers: Details

- A <bcolor>tuning parameter</bcolor> $C$ determines the severity of the violation ot the margin that the model tolerates
  - chosen by cross Validation
  - controls the bias-variance trade-off

- $C$ small $\rightarrow$ narrow margins, rarely violated
- $C$ large $\rightarrow$ wide margins, allow more violation
  - More bias classifier, but lower variance

--

## Shortcomings of the linearity assumption:
<img data-src="images/jwht-fig9-8.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

Notes:
- **Left**:The observations fall into two classes, with a non-linear boundary between them.
- **Right**:The support vector classifier seeks a linear boundary, and consequently performs very poorly


--

## Overcoming the linearity assumption:
### Support vector machines

-  *Idea 1*: (polynomial) transformation of the features + `StandardScaler` + `LinearSVC`.

- *Idea 2*:  convert a linear classifier into a classifier that produced <bcolor>non-linear decision boundaries</bcolor>.
$\rightarrow$  using a <bcolor>Kernel</bcolor> such as:

    - Gaussian RBF kernel
    - Polynomial kernel

-   **We do not open the kernel box**.

    -   Just think as them as a way to construct non-linear hyperplans
    -   Try out different kernel and distance specification

Notes:
- The kernel approach is computationally efficient
- A kernel is a function that quantifies the similarity of 2 observations.

--

## Support vector machines
<img data-src="images/jwht-fig9-9.png"  style="height: 350px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

- *Left*: polynomial kernel of degree 3;
- *Right*: radial kernel


---

<!-- .slide: id="multi"  -->
# Multi-Class Models
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

### Multi-Class Models

-   Many interesting machine learning problems involve multiple
    un-ordered categories:

    -   categorizing a case by area of law

    -   predicting the political party of a speaker in a proportional representation system

-   Some classifier handle multi-class natively

-   Others are strictly binary (SVM)

--

## 2 approaches for N classes

-   One-versus-the-rest (OvR)

    -   each classifier compares a class to all the other classes

    -   select the class whose classifier outputs the highest score

    -   train N classifiers (1 by class) on the whole data

    $\rightarrow$   preferred solution

-   One-versus-the-one (OvO)

    -   each classifier compares a pair of class

    -   train $\frac{N(N-1)}{2}$ classifiers on two classes each time

    $\rightarrow$  good if training takes time on a large dataset

--

## Multi-Class Confusion Matrix
<img data-src="images/confusion-matrix.png"  style="height: 270px; position:relative;     margin-left: auto;margin-right: auto;display: block" >
- More generally, can have a confusion matrix $M$ with items $M_{ij}$ (row $i$, column $j$).

--

## Multi-Class Performance Metrics

Confusion matrix $M$ with items $M_{ij}$ (row $i$, column $j$).

$$\text{Precision for xk}=\frac{\text{True Positives for k}}{\text{T. Positives for k}+\text{F. Positives for k}}=\frac{M_{kk}}{\sum_{j}M_{kj}}$$
$$\text{Recall for xk}=\frac{\text{True Positives for k}}{\text{T. Positives for k + F. Negatives for k}}=\frac{M_{kk}}{\sum_{i}M_{ik}}$$

$$\begin{aligned}
F_{1}(k)=2\times\frac{\text{precision(k)}\times\text{recall(k)}}{\text{precision(k)}+\text{recall(k)}}\end{aligned}$$

--

## Metrics for whole model

-   Macro-averaging:

    -   average of the per-class precision, recall, and F1, e.g.
        $$F_{1}=\frac{1}{n}\sum_{k=1}^{n}F_{1}(k)$$

    -   treats all classes equally

-   Micro-averaging:

    -   Compute model-level sums for true positives, false positives,
        and false negatives; compute precision/recall from model sums.


--

## Metrics for whole model
$$\text{Precision}=\frac{\text{True Positives}}{\text{True Positives + False Positives}}$$
$$\text{Recall}=\frac{\text{True Positives}}{\text{True Positives + False Negatives}}$$

$$\begin{aligned}
  F_{1}=2\times\frac{\text{precision}\times\text{recall}}{\text{precision}+\text{recall}}
\end{aligned}$$

-   favors bigger classes

- “Weighted”: same as macro averaging, but classes are weighted by  number of true instances in data.

--

## Multinomial Logistic Regression

-   Logistic can be generalized to multiple classes.

    -   When given an instance $x_{i}$, multinomial logistic computes a score $s_{k}(x_{i})$ for each class $k$, $$s_{k}(x_{i})=\theta_{k}'x_{i}$$

    -   If there are $n$ features and $K$ output classes, there is a
        $K\times n$ parameter matrix $\Theta$, where the parameters for
        each class are stored as rows.

-   Using the scores, probabilities for each class are computed using
    the softmax function
$$\hat p_{k}(x_{i})=\Pr(Y_{i}=k)=\frac{\exp(s_{k}(x_{i}))}{\sum_{j=1}^{K}\exp(s_{j}(x_{i}))}
=\frac{e^{\theta_{k}x_{i}}}{\sum_{j=1}^{K}e^{\theta_{j}x_{i}}}    $$


-   And the prediction $Y_{i}\in\{1,...,K\}$ is determined by the highest-probability category.

--

## Multinomial Logistic Cost Function

-   The binary cost function generalizes to the cross entropy

<img data-src="images/multi-logit-cost-function.png"  style="height: 110px; position:relative;background-color:white;     margin-left: auto;margin-right: auto;display: block" >

-   again, this is convex, so gradient descent will find the global minimum.

---

<!-- .slide: id="wrap"  -->
# Wrap-up
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

## Types of Classification Algorithms

-   Linear Classifiers

    -   Logistic regression

    -   Naive Bayes classifier

-   Support vector machines

-   Kernel estimation

    -   k-nearest neighbor

-   Decision trees [week 7]

    -   Random forests


---

# Turn off recording <i class="fas fa-video"></i>
