# Title: The Node.js Dependency Ecosystem in GitHub:Social, Technical, and Documentation Aspects
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3986016.svg)](https://doi.org/10.5281/zenodo.3986016)

This is the API documentation for GH-Node.js dataset and paper **The Node.js Dependency Ecosystem in GitHub:Social, Technical, and Documentation Aspects**.

### Abstract: 
Acquired   by   the   largest   social   coding   platform GitHub in 2020, the Node.js Package Manager (i.e., npm) archive repository serves as a critical part of the JavaScript community, and  helps  support  one  of  the  largest  developer  ecosystems  in the  world.  Like  other  software  artifacts,  the  ecosystem  nowcontains  rich  information  that  covers  many  different  aspects of  software  development.  To  enable  the  research  community to  mine  and  analyze  the  diverse  data  related  to  Node.js,  we built  the  Node.js  dependency  ecosystem  (i.e.,  GH-Node.js),  an open  dataset  that  contains  a  curated  snapshot  of  npm  packages and their applications. Moreover, we have included related data dumps  from  GitHub  and  the  npmJS  registry.  In  addition,  GH-Node.js   provides   access   to   issues,   pull   requests   and   related vulnerability  data.  The  dataset  can  be  explored  from  various aspects,   including:   (i) Social,   since   it   includes   all   developer information  related  to  the  packages  and  their  applications,  (ii) Technical, since it includes source code and maintenance activities such  as  issues,  pull  requests  and  vulnerability  information,  and (iii) Documentation,  since  it  features  README  files,  code  of conduct, and licensing information. Our vision is that researchers will use GH-Node.js to investigate their questions with a validated snapshot  of  npm  packages  and  their  applications.

### Dataset structure

```
📁 /
├─ 📁 repositories 
├─ 📁 repositories_info
├─ 📁 dependencies_history
├─ 📁 issues
├─ 📁 pull_requests
├─ 📁 contributors
└─ 📁 security_advisories
```

### Contents:
  1. [repositories](https://tinyurl.com/yynovv2w): is the folder that contains the git repositories.
  2. [repositories_info](https://tinyurl.com/yy2jf64y): is the folder that contains the basic information of a git repository. 
  3. [dependencies_history](https://tinyurl.com/y5pf2xr6): is the folder that contains the information related to the dependency changes over time for the package.
  4. [issues](https://tinyurl.com/y2s3ok3w): is the folder that contains the issues for the package.
  5. [pull_requests](https://tinyurl.com/y4wwdsv4): is the folder that contains all the changes information collected from the GitHub API.
  6. [contributors](https://tinyurl.com/y5za6ols): is the folder that contains contributor information collected from the GitHub API.
  7. [security_advisories](https://tinyurl.com/y3h3uy6k): is the folder that contains security advisories that taken from the GitHub Security Advisory database.
  
 ### How to run:
  1. Download the dataset from: [link]( https://zenodo.org/record/3986016)
  2. Extract the files.
  3. Clone this repository into your userhome folder in the system
  ```git clone https://github.com/NAIST-SE/GH-Node.JS.git```
  3. Open `Jupyter Notebook`.
  4. Run the **[example_query_1.ipynb](https://github.com/NAIST-SE/GH-Node.JS/blob/master/example_query_1.ipynb)** and **[example_query_2.ipynb](https://github.com/NAIST-SE/GH-Node.JS/blob/master/example_query_2.ipynb)** on the dataset.


### Authors:
  1. [Bodin Chinthanet](https://bchinthanet.com/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  2. [Syful Islam](https://syful-is.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  3. [Raula Gaikovina Kula](https://raux.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  4. [Christoph Treude](http://ctreude.ca/), University of Adelaide, Adelaide, Australia.
  5. [Takashi Ishio](https://takashi-ishio.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  6. [Hideaki Hata](https://hideakihata.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  7. [Kenichi Matsumoto](http://isw3.naist.jp/Contents/Research/cs-05-en.html), Nara Institute of Science and Technology (NAIST), Nara, Japan.
