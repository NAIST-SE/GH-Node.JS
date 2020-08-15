# Title: The Node.js Dependency Ecosystem in GitHub:Social, Technical, and Documentation Aspects
### Authors: Bodin Chinthanet∗, Syful Islam∗, Raula Gaikovina Kula∗, Christoph Treude†,Takashi Ishio∗, Hideaki Hata∗, Kenichi Matsumoto*

### Abstract: 
Acquired   by   the   largest   social   coding   platformGitHub in 2020, the Node.js Package Manager (i.e., npm) archiverepository serves as a critical part of the JavaScript community,and helps support one of the largest developer ecosystems in theworld. Like other software artifacts, the ecosystem now containsrich  information  that  covers  many  different  aspects  of  softwaredevelopment.  To  enable  the  research  community  to  mine  andanalyze the diverse data related to Node.js, we built the Node.jsdependency  ecosystem  (i.e.,  GH-Node.js),  an  open  dataset  thatcontains  a  curated  snapshot  of  npm  packages  and  their  clients.Moreover,  we  have  included  related  data  dumps  from  GitHuband the npmJS registry. In addition, GH-Node.js provides accessto issues, pull requests and related vulnerability data. The datasetcan be explored from various aspects, including: (i)Social, sinceit includes all developer information related to the packages andtheir clients, (ii)Technical, since it includes source code and main-tenance  activities  such  as  issues,  pull  requests  and  vulnerabilityinformation, and (iii)Documentation, since it features READMEfiles,  code  of  conduct,  and  licensing  information.  Our  vision  isthat researchers will use GH-Node.js to investigate their questionswith  a  validated  snapshot  of  npm  packages  and  their  clients

## Dataset structure

```
📁 /
├─ 📁 repositories  [libraries.io](https://zenodo.org/record/1196312/files/Libraries.io-open-data-1.2.0.tar.gz)
├─ 📁 repositories_info
├─ 📁 dependencies_history
├─ 📁 issues
├─ 📁 pull_requests
├─ 📁 contributors
└─ 📁 security_advisories
```
