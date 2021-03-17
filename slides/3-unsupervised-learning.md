
# Big Data for Public Policy

## Unsupervised Learning
### [Malka Guillot](https://malkaguillot.weebly.com/)
### ETH Zürich | <a href="https://malkipp.github.io/big_data_policy_2021/">860-0033-00L</a>

---

# <i class="fas fa-video"></i> Turn on recording

---


<!-- .slide:  id="toc" class: left, inverse -->
## Table of Contents

1. [Prologue](#prologue)
1. [Dimension Reduction](#pca)
2. [Clustering Methods](#cluster)

Notes:
- **PCA** looks to find a low-dimensional representation of the observations that explain a good fraction of the variance;
- **Clustering** looks to find homogeneous subgroups among the observations.

---

<!-- .slide: id="prologue"  -->
# Prologue
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

--

### Last Week
- Regression analysis (continuous outcome)
- First ML project!

### Today
- Unsupervised learning

Reference:
- [JWHT](), chap 6.3, 10

### Next Week
- Classification (binary outcome)

--

## Unsupervised Learning

-   So far, supervised learning methods such as   regression

-   Unlike for supervised learning, there is no known goal

    -   No labeled data,

    -   Not a prediction exercise

-   The algorithm **discovers** patterns in the data

-   We (human) **interpret** the results

    -   More subjective than supervised learning

-   Hard to assess the results

---

## Setting

-   Features $X_1, X_2, ... X_p $ measured on $n$ observations, but no associated labeled variable $Y$

-   **Dimensionality reduction** methods are needed
  - ML pbs often involve thousands of features.
  - Especially in the case of **text data**,
  - Not just for computational tractability, but also to help find a good solution.

-   Can be use as a **descriptive tool**
  -   Can we extract information from the data and visualize it?
  -   Can we discover subgroups among the variables or among the observations?

Notes:
- **exploratory data analysis** : correlations for 2 features
  s\rightarrow$ ${n \choose 2}$ (n choose 2) such scatterplots

find a low-dimensional representation of the data that captures as much of the information as possible.

Dimensionality reduction reduces the number of dimensions (also called features and attributes) of a dataset.

It is used to remove redundancy and help both data scientists and machines extract useful patterns.

--

## Examples
-   Dimension reduction for pre-processing

-   Costumer segmentation in marketing


---

<!-- .slide: id="pca"-->
# Dimensionality Reduction
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>


--

<img data-src="images/ml-book/dim-1.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

--

## Principal Component Analysis (PCA)

-   Popular **dimension reduction** technique.

-   Identifies the axis that accounts for the **largest amount of variance** in the data.

-   Finds a second axis, orthogonal to the first, that accounts for the  largest amount of the remaining variance, and so on

-   The unit vector defining the $i^{th}$ axis is called the $i^{th}$ principal component.

Notes:
- History: old techniques from the 40s - mainly used in psychology
- It finds a low-dimensional representation of a data set that contains as much as possible of the variation

--

## Objectives

-   Summarize a large set of feature variables with a smaller number of representative variables
  - collectively explain most of the  variability in the original dataset

-   Find a **low-dimensional representation** of the data that captures as much of the information possible

-   If we can obtain a 2-dimensional representation, then we can plot the observations in 2D.


--

## Principal Components

-   What we are after

-   Each of the dimensions found by the PCA is a linear combination of the $p$ features.

-   The <bcolor>First Principal Component</bcolor> of a set of features  $X_1, X_2, ..., X_p$
    - $=$ the normalized linear combination of the features: $$Z_1= \phi_{11}X_1+\phi_{21}X_2+.... +\phi_{p1}X_p$$ that has the largest variance

-   Normalized means that $\sum_{j=1}^p\phi^2_{j1}=1$

-   $\phi_1 =(\phi_{11}, \phi_{21}, ... \phi_{p1})\,^T $ is the <bcolor>loading vector</bcolor> of the first principal component

Notes:
- the $\phi_{ij}$ are the *loadings*
- Loading vectors constraint to have a $L2$ norm of 1
  - otherwise setting these elements to be arbitrarily large in absolute value could result in an arbitrarily large variance

--

## Computing the First Principal Component
-   We solve:

    $\max_{\phi_{11}, \phi_{21},..., \phi_{p1}}  \underbrace{\frac{1}{n}\sum_{i=1}^n ( \sum_{j=1}^p  \phi_{j1} x_{ij})^2}_{\textrm{Sample variance of }Z_1}$

     $\textrm{   subject to} \sum_{j=1}^p \phi_{j1}^2=1$

-   Re-writen :

    $$\nonumber
    \max_{\phi_{11}, \phi_{21},..., \phi_{p1}}   \frac{1}{n}\sum_{i=1}^n z_{i1}^2   \text{   subject to} \sum_{j=1}^p \phi_{j1}^2=1$$

  - as $\frac{1}{n} \sum_{i=1}^n x_{ij}=0$ (mean zero property)

Notes:
- PCA: low-dimensional representation of a data set that contains as much as possible of the variation
- look for the linear combination that have the highest Variance, subject to the constraint
- **Mean 0**: we are only interested in variance, we assume that each of the variables in $X$ has been centered to have mean 0

--

## Computing the First Principal Component

-   Using eigen decomposition (outside the scope of the class)

-   $z_{11}, ..., z_{n1}$ are the *scores *of the first principal component

-   Solved using Singular Value Decomposition (SVD) [a standard linear algebra tool]

--

## Finding the second principal component $Z_2$

-  $Z_2$ is the linear combination of $X_1, X_2, ..., X_p$:
  $$Z_2= \phi_{12}X_1+\phi_{22}X_2+.... +\phi_{p2}X_p$$

- With maximal variance out of all linear combinations that are uncorrelated with $Z1$

- $Z_2$ uncorrelated with $Z_1$ $\Leftrightarrow$ $\phi _2$ is orthgonal to $\phi_1$

Notes:
- After the first principal component $Z1$ of the features has been determined, we can find the second principal component $Z2$.
- Once we have computed the principal components, we can plot them against each other in order to produce low-dimensional views of the data.
- For instance, we can plot the score vector $Z_1$ against $Z_2$,$Z_1$ against $Z_3$ ...
- Geometrically, this amounts to projecting the original data down onto the subspace spanned by $\phi_1,phi_2$,and $phi_3$,and plotting the projected points

--


## Illustration in 3D, projected on a 2D space
![image](images/pca_eg.png)

*Left:* simulated data in 3 dimensions\
*Right:* projection on the first 2 principal components (plan
represented on the left)

Notes:
- 90 observations simulated in 3D
- *Left*: the first two principal component directions span the plane that best fits the data.
  - It minimizes the sum of squared distances from each point to the plane.
- *Right*: the 1st two PC score vectors give the coordinates of the projection of the 90 observations onto the plane.
    - The variance in the plane is maximized

--

## Alternative Interpretation
- The $M$ principal component score vectors + $M$ principal component loading vectors:
    - can give a good approximation to the data when $M$ is **sufficiently large**.

- When $M= min(n−1,p)$, then the representation is exact

Notes:
- **previously**:
  - We described the principal component loading vectors as the directions in feature space along which the data vary the most, and the principal component scores as projections along these directions
- However, an **alternative interpretation** for principal components can also be useful: principal components provide low-dimensional linear surfaces that are closest to the observations

--

## Pre-processing the variables
-   Variables should

    -   be centered to have mean zero

    -   have the same variance 1

-   the results obtained depend on whether the variables have been  individually scaled

-   Step done by default in python

Notes:

--

## Proportion of the Variance Explained (PVE)

How much of the information in a given data set is lost by projecting the observations onto the first few PC?

$\rightarrow$ plot the proportion of the variance explained by each PC

$$PVE_m=\frac{\text{Variance exeplained by the m}^{th} \text{component}}{\text{Total variance}}$$

Notes:
- Previous 3D figure: the orange, green, and cyan observations that are near each other in 3D space remain nearby in the 2D representation
- But how much is lost with the projection?


--


## PVE
<img data-src="images/jwht-fig10-4.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

Notes:  
- *Left*: proportion of variance explained by each of the four principal components in
- *Right*: the cumulative proportion of variance explained by the four principal components


--

## Choosing the number of dimensions

There is no criteria for deciding how many principal components are required, but some rules of thumb:

-   Choose the smallest number of PC required to explain a **sizable amount** of the variation  in the data

-   For dimensionality reduction

    -   Explaining 95% of the variance is a good objective

-   For data visualization:

    -   Focus on a small number of axis that you can interpret

    -   Do not interpret the components explaining less than 10%


---

<!-- .slide: id="cluster"-->
# Clustering Methods

<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>

Notes:
Clustering refers to a very broad set of techniques for finding subgroups, or clustering clusters, in a data set.

--

## Objective
When performing clustering, the aim is to group data into subsets so that:

-   the objects grouped in each subset are similar, close to one
    another, <bcolor>homogeneous</bcolor>

-   and [different]() from  the objects in other groups.

$\Rightarrow$ find some structure in the data.

Notes:
- Objective = partition data into distinct groups so that the observations within each group are quite similar to each other, while observations in different groups are quite different from each other
- What does homoenenous or different mean?

--

## 2 possibilities

We can

-  <bcolor>Cluster observations</bcolor> on the basis of the features in order to identify subgroups among the observations,

- or we can <bcolor> cluster features</bcolor> on the basis of the observations in order to discover subgroups among the features

Equivalent: simply <bcolor>transpose</bcolor> the data matrix

--

## K-means clustering
**Partitioning** the data into a pre-specified number ($k$) of clusters

The partitioning corresponds to an **optimization problem** which consists in:

-   partitioning the data into $k$ clusters of equal variance

-   so that it minimizes the within-cluster sum-of-squares
    [**inertia**]: $$\sum_{i=0}^k \min_{\mu_j}(||x_i-\mu_j||^2)$$

-   Each cluster is represented by the **central vector** or centroïd
    $\mu_j$

Notes:
- Objective = **Partitioning** the data into $K$ disjoint clusters, setting the desired value of $K$, based on the $p$ variables.


--

## K-means clustering


<img data-src="images/blobs_diagram.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block" >
Simulated data

Notes:

--

## K-means clustering


<img data-src="images/blobs_diagram_4clusters.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block">

4 clusters and their centroïds

--

## K-means clustering


<img data-src="images/blobs_diagram_6clusters.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

6 clusters


--

## K-means clustering


<img data-src="images/voronoi_diagram.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block" >
Decision boundaries for 4 clusters

--

## K-means algorithm

1.  <bcolor>Randomly assign a number</bcolor> ($1$ to $k$) to each of the
    observations. $=$ initial cluster assignments

2.  <bcolor>Iterate until the cluster assignments stop changing</bcolor>:

    1.  For each of the $k$ clusters,
        - compute the cluster **centroid**.
        - The $k^{th}$ cluster centroid is the vector of the $p$ feature means  for the observations in the $k^{th}$ cluster.

    2.  Assign each observation to the cluster whose centroid is closest
        - where **closest** is defined using Euclidean distance

$\rightarrow$ The algorithm aims to choose <bcolor>centroids that minimise the inertia</bcolor> (=within-cluster sum-of-squares criterion)

Notes:
- Need for an algorithm: $k^n$ possibilities for partionning in k groups for n observations

--

## K-means algorithm: example

<img data-src="images/jwht-fig10-6.png"  style="height: 550px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

Notes:
1. the observations are shown.
2. [Top center] Step 1of the algorithm, each observation is randomly assigned to a cluster.
3. Step 2(a): The cluster centroids are computed.
4. Step 2(b): each observation is assigned to the nearest centroid.
5. Step 2(a) is once again performed, leading to new cluster centroids.
6. the results obtained after ten iterations.


--

## Finding the optimal number of clusters

-   Most of the time, the number of clusters does not stand out from
    looking at the data

-   Why not picking the model with the lowest inertia?

-   Because inertia decreases with the number of clusters

-   Rule of thumb: choose the number of clusters at the “elbow”

--

<img data-src="images/inertia_vs_k_diagram.png"  style="height: 350px; position:relative;     margin-left: auto;margin-right: auto;display: block" >


--

## Finding the optimal number of clusters

-   Can pick the optimal number of clusters with the **silhouette score**:
  $$\frac{b_i-a_i}{max(a_i, b_i)}$$

    -   $a_i$ mean distance to members of $i$’s cluster

    -   $b_i$ mean distance to members of $i$’s second-closest cluster

<img data-src="images/silhouette_score_vs_k_diagram.png"  style="height: 280px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

--

## Other Clustering Algorithms

-   **DBSCAN **defines clusters as continuous regions of high density

    -   Works well if all the clusters are dense enough and if they are
        very well separated by low-density regions

    -   Detects and excludes outliers automatically

-   Agglomerative **hierarchical clustering** makes nested clusters:

    -   we do not know in advance how many clusters we want

    -   tree-like visual representation of the observations, called a dendrogram,

    -   show at once the clusterings obtained for each possible number of clusters, from $1$ to $n$.


--


# Turn off recording <i class="fas fa-video"></i>
