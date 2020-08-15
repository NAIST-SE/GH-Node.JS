# Pull Request

Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.

### Pull Request attributes:

|Attribute|Description|
|---------|-----------|
|url| `url` of the pull request|
|id| `id` of the pull request|
|node_id| `node_id` of the pull request|
|html_url| `html` link of the pull request|
|diff_url|`diff` operation `link` of the pull request|
|patch_url| `patch` link of the pull request|
|issue_url| `issue` link of the pull request|
|number| The pull request number|
|state| The current state of pull request (e.g. `open` or `close`)
|locked| The locking status of the pull request (e.g., Boolean `True` or `False`)
|title| The `title` of the pull request|
|body| Body of the pull request|
|created_at| Date of creating the pull request|
|updated_at| Date of updating the pull request|
|closed_at| Date of closing the pull request|
|merged_at| Date of merging the pull request|
|merge_commit_sha| The SHA of the test merge commit|
|assignee| The person who assign|
|assignees| The list of people who assigned|
|requested_reviewers| The list of requested reviewers|
|requested_teams| The requested_teams|
|labels| Labels of the pull request|
|milestone| The milestone of the pull request|
|draft| The draft of the pull request|
|commits_url| The `url` of the commits|
|review_comments_url| The `url` of the review_comments|
|review_comment_url| Each `url` of the review_comment|
|comments_url| The comments url of the pull request|
|statuses_url| The status url of the pull request|


### User attribute:

|Attribute|Description|
|---------|-----------|
|login| Login name|
|id| Login id|
|avatar_url| Personal url for to represent yourself on the Internet|
|url| Personal account url|
|html_url| Html url|
|followers_url| List of followers url|
|following_url| List of followings url|
|gists_url||
|starred_url| List of starred url|
|subscriptions_url| list of subscription url|
|organizations_url| Owners organizations url|
|repos_url| List of repos url|
|events_url| List of events url|
|received_events_url| List of received events url|
|type| User account type|
|site_admin| Status of site_admin (Boolean `True` or `False`)|

Example of github pull request:
```
{
  "url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls/18",
  "id": 62350233,
  "node_id": "MDExOlB1bGxSZXF1ZXN0NjIzNTAyMzM=",
  "html_url": "https://github.com/lourenzo/gulp-jshint-xml-file-reporter/pull/18",
  "diff_url": "https://github.com/lourenzo/gulp-jshint-xml-file-reporter/pull/18.diff",
  "patch_url": "https://github.com/lourenzo/gulp-jshint-xml-file-reporter/pull/18.patch",
  "issue_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/18",
  "number": 18,
  "state": "open",
  "locked": false,
  "title": "Use JSHint's severity levels in checkstyle XML output",
  "user": {
    "login": "jorisvddonk",
    "id": 266543,
    "node_id": "MDQ6VXNlcjI2NjU0Mw==",
    "avatar_url": "https://avatars2.githubusercontent.com/u/266543?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/jorisvddonk",
    "html_url": "https://github.com/jorisvddonk",
    "followers_url": "https://api.github.com/users/jorisvddonk/followers",
    "following_url": "https://api.github.com/users/jorisvddonk/following{/other_user}",
    "gists_url": "https://api.github.com/users/jorisvddonk/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/jorisvddonk/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/jorisvddonk/subscriptions",
    "organizations_url": "https://api.github.com/users/jorisvddonk/orgs",
    "repos_url": "https://api.github.com/users/jorisvddonk/repos",
    "events_url": "https://api.github.com/users/jorisvddonk/events{/privacy}",
    "received_events_url": "https://api.github.com/users/jorisvddonk/received_events",
    "type": "User",
    "site_admin": false
  },
  "body": "JSHint uses severity levels in its reporting. Three severity levels are used: `error`, `warning` and `info`. Errors reported in checkstyle XMLs also have a severity property. Checkstyle supports four severities: `error`, `warning`, `info` and `ignore`.\n\nCurrently, gulp-jshint-xml-file-reporter's checkstyle reporter assigns the `error` severity to each issue JSHint finds, regardless of the severity of the actual issue as reported by JSHint itself. This isn't very useful, and prevents advanced use cases of the reporter in combination with a CI solution. This PR solves this.\n\nTests have been updated and verified, as well.\n",
  "created_at": "2016-03-10T07:35:19Z",
  "updated_at": "2016-05-03T14:52:12Z",
  "closed_at": null,
  "merged_at": null,
  "merge_commit_sha": "8bdc0a19c1fabc8e741870d778865dde981c971d",
  "assignee": null,
  "assignees": [
    
  ],
  "requested_reviewers": [
    
  ],
  "requested_teams": [
    
  ],
  "labels": [
    
  ],
  "milestone": null,
  "draft": false,
  "commits_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls/18/commits",
  "review_comments_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls/18/comments",
  "review_comment_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls/comments{/number}",
  "comments_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/18/comments",
  "statuses_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/statuses/ec5a04bcfe4c966462386be275592a8782b9476a",
  "head": {
    "label": "jorisvddonk:master",
    "ref": "master",
    "sha": "ec5a04bcfe4c966462386be275592a8782b9476a",
    "user": {
      "login": "jorisvddonk",
      "id": 266543,
      "node_id": "MDQ6VXNlcjI2NjU0Mw==",
      "avatar_url": "https://avatars2.githubusercontent.com/u/266543?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/jorisvddonk",
      "html_url": "https://github.com/jorisvddonk",
      "followers_url": "https://api.github.com/users/jorisvddonk/followers",
      "following_url": "https://api.github.com/users/jorisvddonk/following{/other_user}",
      "gists_url": "https://api.github.com/users/jorisvddonk/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/jorisvddonk/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/jorisvddonk/subscriptions",
      "organizations_url": "https://api.github.com/users/jorisvddonk/orgs",
      "repos_url": "https://api.github.com/users/jorisvddonk/repos",
      "events_url": "https://api.github.com/users/jorisvddonk/events{/privacy}",
      "received_events_url": "https://api.github.com/users/jorisvddonk/received_events",
      "type": "User",
      "site_admin": false
    },
    "repo": {
      "id": 53490967,
      "node_id": "MDEwOlJlcG9zaXRvcnk1MzQ5MDk2Nw==",
      "name": "gulp-jshint-xml-file-reporter",
      "full_name": "jorisvddonk/gulp-jshint-xml-file-reporter",
      "private": false,
      "owner": {
        "login": "jorisvddonk",
        "id": 266543,
        "node_id": "MDQ6VXNlcjI2NjU0Mw==",
        "avatar_url": "https://avatars2.githubusercontent.com/u/266543?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/jorisvddonk",
        "html_url": "https://github.com/jorisvddonk",
        "followers_url": "https://api.github.com/users/jorisvddonk/followers",
        "following_url": "https://api.github.com/users/jorisvddonk/following{/other_user}",
        "gists_url": "https://api.github.com/users/jorisvddonk/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/jorisvddonk/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/jorisvddonk/subscriptions",
        "organizations_url": "https://api.github.com/users/jorisvddonk/orgs",
        "repos_url": "https://api.github.com/users/jorisvddonk/repos",
        "events_url": "https://api.github.com/users/jorisvddonk/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jorisvddonk/received_events",
        "type": "User",
        "site_admin": false
      },
      "html_url": "https://github.com/jorisvddonk/gulp-jshint-xml-file-reporter",
      "description": "A JSHint reporter to be used by gulp-jshint that will provide a jslint.xml that can be used by CI tools as jenkins",
      "fork": true,
      "url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter",
      "forks_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/forks",
      "keys_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/keys{/key_id}",
      "collaborators_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/collaborators{/collaborator}",
      "teams_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/teams",
      "hooks_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/hooks",
      "issue_events_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/issues/events{/number}",
      "events_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/events",
      "assignees_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/assignees{/user}",
      "branches_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/branches{/branch}",
      "tags_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/tags",
      "blobs_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/git/blobs{/sha}",
      "git_tags_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/git/tags{/sha}",
      "git_refs_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/git/refs{/sha}",
      "trees_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/git/trees{/sha}",
      "statuses_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/statuses/{sha}",
      "languages_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/languages",
      "stargazers_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/stargazers",
      "contributors_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/contributors",
      "subscribers_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/subscribers",
      "subscription_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/subscription",
      "commits_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/commits{/sha}",
      "git_commits_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/git/commits{/sha}",
      "comments_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/comments{/number}",
      "issue_comment_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/issues/comments{/number}",
      "contents_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/contents/{+path}",
      "compare_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/compare/{base}...{head}",
      "merges_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/merges",
      "archive_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/{archive_format}{/ref}",
      "downloads_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/downloads",
      "issues_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/issues{/number}",
      "pulls_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/pulls{/number}",
      "milestones_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/notifications{?since,all,participating}",
      "labels_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/labels{/name}",
      "releases_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/releases{/id}",
      "deployments_url": "https://api.github.com/repos/jorisvddonk/gulp-jshint-xml-file-reporter/deployments",
      "created_at": "2016-03-09T11:00:04Z",
      "updated_at": "2016-03-09T11:00:05Z",
      "pushed_at": "2016-03-10T07:27:03Z",
      "git_url": "git://github.com/jorisvddonk/gulp-jshint-xml-file-reporter.git",
      "ssh_url": "git@github.com:jorisvddonk/gulp-jshint-xml-file-reporter.git",
      "clone_url": "https://github.com/jorisvddonk/gulp-jshint-xml-file-reporter.git",
      "svn_url": "https://github.com/jorisvddonk/gulp-jshint-xml-file-reporter",
      "homepage": "",
      "size": 44,
      "stargazers_count": 0,
      "watchers_count": 0,
      "language": "JavaScript",
      "has_issues": false,
      "has_projects": true,
      "has_downloads": true,
      "has_wiki": true,
      "has_pages": false,
      "forks_count": 0,
      "mirror_url": null,
      "archived": false,
      "disabled": false,
      "open_issues_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "spdx_id": "MIT",
        "url": "https://api.github.com/licenses/mit",
        "node_id": "MDc6TGljZW5zZTEz"
      },
      "forks": 0,
      "open_issues": 0,
      "watchers": 0,
      "default_branch": "master"
    }
  },
  "base": {
    "label": "lourenzo:master",
    "ref": "master",
    "sha": "ab94e8cd0979ff974fc5ef4f2162a9a2f4c15889",
    "user": {
      "login": "lourenzo",
      "id": 81989,
      "node_id": "MDQ6VXNlcjgxOTg5",
      "avatar_url": "https://avatars3.githubusercontent.com/u/81989?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/lourenzo",
      "html_url": "https://github.com/lourenzo",
      "followers_url": "https://api.github.com/users/lourenzo/followers",
      "following_url": "https://api.github.com/users/lourenzo/following{/other_user}",
      "gists_url": "https://api.github.com/users/lourenzo/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/lourenzo/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/lourenzo/subscriptions",
      "organizations_url": "https://api.github.com/users/lourenzo/orgs",
      "repos_url": "https://api.github.com/users/lourenzo/repos",
      "events_url": "https://api.github.com/users/lourenzo/events{/privacy}",
      "received_events_url": "https://api.github.com/users/lourenzo/received_events",
      "type": "User",
      "site_admin": false
    },
    "repo": {
      "id": 27784702,
      "node_id": "MDEwOlJlcG9zaXRvcnkyNzc4NDcwMg==",
      "name": "gulp-jshint-xml-file-reporter",
      "full_name": "lourenzo/gulp-jshint-xml-file-reporter",
      "private": false,
      "owner": {
        "login": "lourenzo",
        "id": 81989,
        "node_id": "MDQ6VXNlcjgxOTg5",
        "avatar_url": "https://avatars3.githubusercontent.com/u/81989?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/lourenzo",
        "html_url": "https://github.com/lourenzo",
        "followers_url": "https://api.github.com/users/lourenzo/followers",
        "following_url": "https://api.github.com/users/lourenzo/following{/other_user}",
        "gists_url": "https://api.github.com/users/lourenzo/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/lourenzo/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/lourenzo/subscriptions",
        "organizations_url": "https://api.github.com/users/lourenzo/orgs",
        "repos_url": "https://api.github.com/users/lourenzo/repos",
        "events_url": "https://api.github.com/users/lourenzo/events{/privacy}",
        "received_events_url": "https://api.github.com/users/lourenzo/received_events",
        "type": "User",
        "site_admin": false
      },
      "html_url": "https://github.com/lourenzo/gulp-jshint-xml-file-reporter",
      "description": "A JSHint reporter to be used by gulp-jshint that will provide a jslint.xml that can be used by CI tools as jenkins",
      "fork": false,
      "url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter",
      "forks_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/forks",
      "keys_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/keys{/key_id}",
      "collaborators_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/collaborators{/collaborator}",
      "teams_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/teams",
      "hooks_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/hooks",
      "issue_events_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/events{/number}",
      "events_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/events",
      "assignees_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/assignees{/user}",
      "branches_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/branches{/branch}",
      "tags_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/tags",
      "blobs_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/git/blobs{/sha}",
      "git_tags_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/git/tags{/sha}",
      "git_refs_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/git/refs{/sha}",
      "trees_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/git/trees{/sha}",
      "statuses_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/statuses/{sha}",
      "languages_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/languages",
      "stargazers_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/stargazers",
      "contributors_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/contributors",
      "subscribers_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/subscribers",
      "subscription_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/subscription",
      "commits_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/commits{/sha}",
      "git_commits_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/git/commits{/sha}",
      "comments_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/comments{/number}",
      "issue_comment_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/comments{/number}",
      "contents_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/contents/{+path}",
      "compare_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/compare/{base}...{head}",
      "merges_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/merges",
      "archive_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/{archive_format}{/ref}",
      "downloads_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/downloads",
      "issues_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues{/number}",
      "pulls_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls{/number}",
      "milestones_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/notifications{?since,all,participating}",
      "labels_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/labels{/name}",
      "releases_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/releases{/id}",
      "deployments_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/deployments",
      "created_at": "2014-12-09T20:05:50Z",
      "updated_at": "2017-08-27T09:36:54Z",
      "pushed_at": "2017-07-26T14:00:39Z",
      "git_url": "git://github.com/lourenzo/gulp-jshint-xml-file-reporter.git",
      "ssh_url": "git@github.com:lourenzo/gulp-jshint-xml-file-reporter.git",
      "clone_url": "https://github.com/lourenzo/gulp-jshint-xml-file-reporter.git",
      "svn_url": "https://github.com/lourenzo/gulp-jshint-xml-file-reporter",
      "homepage": "",
      "size": 386,
      "stargazers_count": 4,
      "watchers_count": 4,
      "language": "JavaScript",
      "has_issues": true,
      "has_projects": true,
      "has_downloads": true,
      "has_wiki": true,
      "has_pages": false,
      "forks_count": 6,
      "mirror_url": null,
      "archived": false,
      "disabled": false,
      "open_issues_count": 4,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "spdx_id": "MIT",
        "url": "https://api.github.com/licenses/mit",
        "node_id": "MDc6TGljZW5zZTEz"
      },
      "forks": 6,
      "open_issues": 4,
      "watchers": 4,
      "default_branch": "master"
    }
  },
  "_links": {
    "self": {
      "href": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls/18"
    },
    "html": {
      "href": "https://github.com/lourenzo/gulp-jshint-xml-file-reporter/pull/18"
    },
    "issue": {
      "href": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/18"
    },
    "comments": {
      "href": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/18/comments"
    },
    "review_comments": {
      "href": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls/18/comments"
    },
    "review_comment": {
      "href": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls/comments{/number}"
    },
    "commits": {
      "href": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/pulls/18/commits"
    },
    "statuses": {
      "href": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/statuses/ec5a04bcfe4c966462386be275592a8782b9476a"
    }
  },
  "author_association": "NONE",
  "active_lock_reason": null
}
```
