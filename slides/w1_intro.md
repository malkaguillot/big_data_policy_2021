# Big Data for Public Policy
## Week 1: Introduction
### [Malka Guillot](https://malkaguillot.weebly.com/)
### ETH Zürich | <a href="https://malkipp.github.io/big_data_policy_2021/">860-0033-00L</a>

---

<!-- .slide:  id="toc" class: left, inverse -->
# Table of contents

1. [Prologue](#prologue)

2. [Intro](#getting_started)

3. [Tools and resources](#tools_resources)

2. [Course outline](#course_outline)

2. [Epilogue](#hw)

Notes: my notes

---

<!-- .slide: id="prologue"  -->
# Prologue
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>


--

## How does the class work?

- Lectures: 2 hours / week
  - 1 hour theory
  - 2 * (30 min students presentations)
- Every week
  - Thursdays	12:15-14 (with a 10 minute break 13-13:10)
  - On zoom: [link](https://ethz.zoom.us/j/92433296893?pwd=a0tsSHkzU2ZhNnpiN1YxWno2MnZhdz09)
  - In person? [ML F 39](http://www.rauminfo.ethz.ch/Rauminfo/grundrissplan.gif?gebaeude=ML&geschoss=F&raumNr=39&lang=en)
  - Dates: 25.02.; 04.03.; 11.03.; 18.03.; 25.03.; 01.04.; 15.04.; 22.04.; 29.04.; 06.05.; 20.05.; 27.05.; 03.06.

--

## Online Course Materials
- Moodle:
  - Course outline with links to videos and slides
  - Course announcement and forum
  - Giving back homerwork
- [Syllabus](https://docs.google.com/document/d/1eviJuOoWUjoonxS1LvQJi1kMbmkNUulJtZ31542w100)
- [Github folder](https://github.com/MalkIPP/big_data_policy_2020) or [Github page](https://malkipp.github.io/big_data_policy_2021/)


--

## Evaluation

- Weekly homework: should be given back as [jupyter notebooks](https://jupyter.org/) in HTML format.
- Reading:
  - 1 presentation during the Semester
  - Prepare 1 question / week on the week's articles
- Take home exam
- [Alternatively] Course project

--

## Course Communication

- Course communication will be done through eDoz
- I will be available in the zoom 5 minutes early, during the mid-lecture break and after the end of lectures.

--

## How to reach me?

<i class="fa fa-send" aria-hidden="true"></i>
malka.guillot@gess.ethz.ch


<i class="fa fa-location-arrow" aria-hidden="true"></i>
IFW E 44 (Haldeneggsteig 4) <br>
8092 Zürich


<i class="fa fa-arrow-right" aria-hidden="true"></i> I will be available for 1:1 meetings after the class, just book a 15 minutes slot [here](https://calendly.com/malkaguillot/1-1-meeting-eth-class).


--

<!-- .slide: id=""-->
## Who am I?

  <div class="image-float">
    <p style="position: relative; right: 0px; top: 10;">
        <a href="images/malka_small.jpg"><img src="images/malka_small.jpg" height="200px"/></a></p>
        <a href="image2.jpg"><img src="" height="100px"/></a></p>
   <p class="fragment" data-fragment-index="4" style="position:absolute; left:40px; top:40px;">
     </div>
  <div class="content-aside">
   <p class="fragment fade-down" data-fragment-index="1">
    PhD in economics from the Paris School of Economics </p>
   <p class="fragment" data-fragment-index="2">
    Postdoc at ETH </p>
   <p class="fragment" data-fragment-index="3">
    Interested in public economics questions: inequality and taxation</p>
   <p class="fragment" data-fragment-index="4">
    Using the standard econometric toolbox + natural language processing + machine learning </p>
 </div>




--

## Who are you?

TODO: results from pre-class survey

---

<!-- .slide: id="getting_started"  -->
# Machine learning, big data an policy analysis
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>


--

## What is Big data?

--

## What is machine learning?

<img data-src="images/ml_vs_traditional_paradigm2.png"  style="height: 400px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

- **Classical computer programming**: <span style="color:blue">humans</span> input the <span style="color:blue">rules</span> and the <span style="color:blue">data</span>, and the <span style="color:green">computer</span> provides <span style="color:green">answers</span>.

- **Machine learning**: <span style="color:blue">humans</span> input the <span style="color:blue">data</span> and the <span style="color:blue">answer</span>, and the <span style="color:green">computer</span>  learns the <span style="color:green">rules</span>.

--

## The Machine learning landscape
<img data-src="images/machine_learning_landscape.jpeg"  style="height: 550px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

--

## Model-based vs. algorithmic approaches


--

## Why is it useful to policy analysis?


--

## Researcher vs. policy analysist

- The frontier can be thin
- I will sometimes be speaking from the point of view of an economist, but:
  - The model-based vs. algorithm-based problematics transfers to other social sciences
  - I try to cover a wide range of topics in the literature
  - You are welcome to propose relevant papers
- All aim at *using data to solve problems*

---

<!-- .slide: id="tools_resources" -->
# Tools and resources
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>


--

## Why Python?

- General-purpose language
  - One of the core languages of scientific computing
- Elegant syntax
- Many useful libraries:
  - Data manipulation: `Pandas`
  - Machine learning: [scikit-learn](http://scikit-learn.org/)
  - Statistics: [statsmodels](http://statsmodels.sourceforge.net/)
  - Natural Language Procession [nltk]()


--

## Using Python

| <a href=https://www.anaconda.com/products/individual>Anaconda</a>| <a href=https://jupyter.org/>Jupyter notebook</a> | Spyder</a> |
|:------:|:---:|:-----:|
|<img data-src="images/anaconda-logo.png"  style="height: 80px;" > | <img data-src="images/jupyter-logo2.png" style="height: 80px" class="center"> | <img data-src="images/spyder-logo.png" alt="" style="height: 80px">|
|a convenient all-in-one install |for homerwork|for longer code|


--

##  <i class="fa fa-arrow-right" aria-hidden="true"></i> Anaconda

<img data-src="images/anaconda-navigator.png" style="width: 1800px;"  >
See downlowding instruction and small video

--


## Course materials are on [Github](https://github.com/MalkIPP/big_data_policy_2020)

- [Git](https://git-scm.com)
  - Git is a distributed version control system.
  - Dropbox + track changes, optimized for codes
- [GitHub](https://github.com/) (≠ Git)
  - = Online hosting platform that provides an array of services built on top of the Git system.
  - Makes life easier

>Github is also great for scientific research and for collaboration on code.

--

## Why Git and Github?

<img data-src="images/phd-comics-doc.gif"  style="height: 550px; position:relative;     margin-left: auto;margin-right: auto;display: block" >

Also [git vs. Dropbox from a researcher's perspective](https://michaelstepner.com/blog/git-vs-dropbox/)


--

## How to interact with the materials?

1. **Simple** -> Just use the online GitHub interface to
   - Access the materials
   - Amend the students' presentation signing sheet
2. **Advanced**
   - Download [git](https://git-scm.com/downloads)
   - Create an account on [GitHub](https://github.com/)
   - Go through this [simple guide](https://rogerdudler.github.io/git-guide/)
   - In case it goes wrong: http://ohshitgit.com/


--

### Main textbook references
<i class="fa fa-book fa-fw" aria-hidden="true">


---

<!-- .slide: id="course_outline"-->
# Course outline
<html><div style='float:left'></div><hr color='#EB811B' size=1px width=796px></html>


--

## W1

## W2

---

<!-- .slide: id="hw"-->
# For next week

- Install [Anaconda](https://www.anaconda.com/products/individual), try out to run python in a Jupyter notebook and spyder
- Get familiarized with the basics of python's syntax
- Take a slot for a **paper presentation** by:
  - Modifying the `raw` version of the signing sheet on github [can be done directly on the platform]
  - This works as a small exercise on github!
  - You can contact me (*and are encourage to*) if you want to present a paper that is not on the list
