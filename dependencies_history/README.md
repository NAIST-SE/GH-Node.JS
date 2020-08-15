# Dependencies history
Using the dependency graph, you can see the packages your project depends on and the repositories that depend on it. In addition, you can see any vulnerabilities detected in its dependencies.

### Semantic versioning:

![Example](https://github.com/NAIST-SE/npmDependencyEcosystemDatasets/blob/master/dependencies_history/semver.png "Example of semantic virsioning")

```
    ~version "Approximately equivalent to version" See npm semver - Tilde Ranges & semver (7)
    ^version "Compatible with version" See npm semver - Caret Ranges & semver (7)
    version Must match version exactly
    >version Must be greater than version
    >=version etc
    <version
    <=version
    1.2.x 1.2.0, 1.2.1, etc., but not 1.3.0
    http://sometarballurl (this may be the URL of a tarball which will be downloaded and installed locally
    * Matches any version
    latest Obtains latest release
````

### npm dependencies history attributes:

|Attribute|Description|
|---------|-----------|
|bundledDependencies| The array of package names that will be bundled when publishing the package|
|commit_hash| The commit_hash information while performing commit|
|commit_time| The commit time information of the repository |
|commit_tz|The commit_tz is timestamp infromation|
|committer| The person information who performed commit operation|
|dependencies|The packages required by your application in production (e.g.,"git-execute":"~0.1.0").|
|devDependencies| The packages that are only needed for local development and testing (e.g.,  "mocha":"~1.19.0").|
|optionalDependencies| Optional dependencies are just that: optional. If they fail to install, Yarn will still say the install process was successful.|
|peerDependencies|Peer dependencies are a special type of dependency that would only ever come up if you were publishing your own package|



### Example of dependencies history:
```
{
  "0.1.0":{
    "bundledDependencies":null,
    "commit_hash":"3b9594b85433e0cd61d89e439289fa2fc768329d",
    "commit_time":1401044052,
    "commit_tz":-10800,
    "committer":"Alexandru Vladutu <alexandru.vladutu@gmail.com>",
    "dependencies":{
      "git-execute":"~0.1.0"
    },
    "devDependencies":{
      "mocha":"~1.19.0",
      "proxyquire":"~1.0.0",
      "should":"~3.3.2"
    },
    "optionalDependencies":null,
    "peerDependencies":null
  }
}
```
