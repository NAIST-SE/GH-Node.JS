# Repositories information
Repositories_info is  the  folder  that  contains  the  basic information of a git repository
Information repositories are created to store project information in a centralized public location to provide easy access for community members.

### Repository attributes:
|Attribute|Description|
|---------|-----------|
|github_url| the url of the repository|
|is_npm_package| Flag to ensure the type of repository (e.g., Boolean `True` or `False`)|
|npm_info| The information of the repository|
|description| The description of the repository|
|homepage| The home page of the repository|
|name| The name of the repository|
|readmeFilename| The readMe file of the repository|
|repository| The git url of the repository|
|time| The time tracking of the repository|
|version| The current version of the repository|
|versions| The version history of the repository|
|owner| The owner name of the repository|
|repo_name| The name of the repository|




### Example of repositories information:
```
{
  "github_url":"https://github.com/Ahineya/jsdv",
  "is_npm_package":true,
  "npm_info":{
    "_cached":true,
    "_contentLength":3382,
    "_from":".",
    "_id":"jsdv@0.0.2-7",
    "_npmUser":"ahineya <deadswallow@gmail.com>",
    "_npmVersion":"1.3.24",
    "_rev":"1-738673dad47d2df6cce1cca6416c8d2d",
    "author":"Pavel Evsegneev <deadswallow@gmail.com> (http://github.com/Ahineya/)",
    "bugs":{
      "url":"https://github.com/Ahineya/jsdv/issues"
    },
    "description":"JavaScript forms validator. Created for html attributes validation declarations",
    "dist":{
      "shasum":"c66132121bbbce36b89da08e759f8b71a5709698",
      "tarball":"https://registry.npmjs.org/jsdv/-/jsdv-0.0.2-7.tgz"
    },
    "dist-tags":{
      "latest":"0.0.2-7"
    },
    "homepage":"http://github.com/Ahineya/jsdv",
    "keywords":[
      "validation",
      "forms"
    ],
    "main":"./js/validator.js",
    "maintainers":[
      "ahineya <deadswallow@gmail.com>"
    ],
    "name":"jsdv",
    "readmeFilename":"README.md",
    "repository":{
      "type":"git",
      "url":"https://github.com/Ahineya/jsdv.git"
    },
    "time":{
      "0.0.2-5":"2014-05-29T08:07:40.518Z",
      "0.0.2-6":"2014-05-29T08:18:15.026Z",
      "0.0.2-7":"2014-05-29T09:38:04.691Z",
      "created":"2014-05-29T08:07:40.518Z",
      "modified":"2014-05-29T09:38:04.691Z"
    },
    "version":"0.0.2-7",
    "versions":[
      "0.0.2-5",
      "0.0.2-6",
      "0.0.2-7"
    ]
  },
  "owner":"Ahineya",
  "repo_name":"jsdv"
}
```
