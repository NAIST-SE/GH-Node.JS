**Issues:** 
Issues are a great way to keep track of tasks, enhancements, and bugs for a project. They’re kind of like email—except they can be shared and discussed with the rest of your team. Most software projects have a bug tracker of some kind. GitHub’s tracker is called Issues, and has its own section in every repository.

**Issue attributes:**

|Attribute|Description|
|---------|-----------|
|url| Link of issue in the repository|
|repository_url| Link of the respository|
|labels_url| Link of the labels|
|comments_url| Link of comments|
|events_urls| Link of the events|
|id| Id of the issue|
|node_id| Id of the node|
|number| Issue number of the repository|
|Title| Title of the issue|

**User attribute:**
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

**Lables attributes:**
|Attribute|Description|
|---------|-----------|
|id| Id of the label|
|node_id| `node_id` of the label|
|url|Lable url|
|name| Label of the issue (e.g., bug)|
|color| Color of the label|
|default| Status of Label (Boolean True or False)|
|description|Description of the label|


**Assignee attributes:**
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


**Assignees attributes:**
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


**Issue status attributes:**
|Attribute|Description|
|---------|-----------|
|State| Current state of the issue (e.g., `open` or `closed`)|
|locked| Issue fixing status (e.g., `True` or `False`)|
|milestone| milestone of the issue|
|comments| Comments on the issue|
|created_at| Date of creation of the issue|
|updated_at| Date of updating the issue|
|closed_at| Date of closing the issue|.
|author_association| Name of author who is associated with the issue|
|active_lock_reason| Reason of the active lock of the issue|
|body| Description of the issue|
|performed_via_github_app| Way of reporting the issue|































Example of github issue:
```
{
    "url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/19",
    "repository_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter",
    "labels_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/19/labels{/name}",
    "comments_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/19/comments",
    "events_url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/issues/19/events",
    "html_url": "https://github.com/lourenzo/gulp-jshint-xml-file-reporter/issues/19",
    "id": 174786546,
    "node_id": "MDU6SXNzdWUxNzQ3ODY1NDY=",
    "number": 19,
    "title": "if the target folder is not existing, the file can't be written",
    "user": {
      "login": "dabperceptive",
      "id": 8057034,
      "node_id": "MDQ6VXNlcjgwNTcwMzQ=",
      "avatar_url": "https://avatars2.githubusercontent.com/u/8057034?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/dabperceptive",
      "html_url": "https://github.com/dabperceptive",
      "followers_url": "https://api.github.com/users/dabperceptive/followers",
      "following_url": "https://api.github.com/users/dabperceptive/following{/other_user}",
      "gists_url": "https://api.github.com/users/dabperceptive/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/dabperceptive/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/dabperceptive/subscriptions",
      "organizations_url": "https://api.github.com/users/dabperceptive/orgs",
      "repos_url": "https://api.github.com/users/dabperceptive/repos",
      "events_url": "https://api.github.com/users/dabperceptive/events{/privacy}",
      "received_events_url": "https://api.github.com/users/dabperceptive/received_events",
      "type": "User",
      "site_admin": false
    },
    "labels": [
      {
        "id": 155891260,
        "node_id": "MDU6TGFiZWwxNTU4OTEyNjA=",
        "url": "https://api.github.com/repos/lourenzo/gulp-jshint-xml-file-reporter/labels/bug",
        "name": "bug",
        "color": "fc2929",
        "default": true,
        "description": null
      }
    ],
    "state": "open",
    "locked": false,
    "assignee": {
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
    "assignees": [
      {
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
      }
    ],
    "milestone": null,
    "comments": 0,
    "created_at": "2016-09-02T15:29:13Z",
    "updated_at": "2016-09-09T10:32:52Z",
    "closed_at": null,
    "author_association": "NONE",
    "active_lock_reason": null,
    "body": "If you have a clean task on your output folder, which removes all content and subfolders and then jshint is the first task which is running, then it can't write the output file because of a missing folder structure.\n\nWorkaround:\n\n```\ngulp.task('prepareStylecheck', function () {\n    //just create the output folder because of a reporter bug\n    return gulp.src(PATH_IN_SRC)\n        .pipe(gulp.dest(PATH_OUT_TESTRESULT));\n});\n\ngulp.task('stylecheck', ['prepareStylecheck'], function () {\n    return gulp.src(FILES_SRC)\n        .pipe(jshint())\n        .pipe(jshint.reporter('jshint-stylish'))\n        .pipe(jshint.reporter(jshintXMLReporter))\n        .on('end', jshintXMLReporter.writeFile({\n            format: 'checkstyle',\n            filePath: PATH_OUT_TESTRESULT + 'checkstyle.xml'\n        }));\n});\n```\n",
    "performed_via_github_app": null
  }
```
