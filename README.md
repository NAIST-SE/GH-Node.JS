# Title: The Node.js Dependency Ecosystem in GitHub:Social, Technical, and Documentation Aspects
### Authors: Bodin Chinthanet∗, Syful Islam∗, Raula Gaikovina Kula∗, Christoph Treude†,Takashi Ishio∗, Hideaki Hata∗, Kenichi Matsumoto

### Abstract: 
Acquired by the largest social coding platform GitHub in 2020, the Node.js Package Manager (i.e., npm) archive repository serves as a critical part of the JavaScript community, and helps support one of the largest developer ecosystems in the world.
Like other software artifacts, the ecosystem now contains rich information that covers many different aspects of software development.
To enable the research community to mine and analyze the diverse data related to Node.js, we built the Node.js dependency ecosystem (i.e., npmDE), an open dataset that contains a curated snapshot of npm packages and their clients. 
Moreover, we have included related data dumps from GitHub and the npmJS registry. 
In addition, \npmDE~provides access to issues, pull requests and related vulnerability data.
The dataset can be explored from various aspects, including: (i) \textit{Social}, since it includes all developer information related to the packages and their clients, (ii) \textit{Technical},  since it includes source code and maintenance activities such as issues, pull requests and vulnerability information, and (iii) \textit{Documentation}, since it features README files, code of conduct, and licensing information. 
Our vision is that researchers will use \npmDE~to investigate their questions with a validated snapshot of npm packages and their clients.

## Dataset structure

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
