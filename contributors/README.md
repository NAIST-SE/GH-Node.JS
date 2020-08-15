# Contributors
Contributor is the folder that contains contributor infor-mation  collected  from  the  GitHub  API.  Note  that  this information  is  not  the  same  as  the  author  information contained in the contributing.md file.

### Contributors attributes:
### User attribute:
|Attribute|Description|
|---------|-----------|
|login| Login name|
|id| Login id|
|avatar_url| Personal url for to represent yourself on the Internet|
|gravatar_id| "gravatar_id" for more information but optional|
|url| Personal account url|
|html_url| Html url|
|followers_url| List of followers url|
|following_url| List of followings url|
|gists_url| The fork or clonned url|
|starred_url| List of starred url|
|subscriptions_url| list of subscription url|
|organizations_url| Owners organizations url|
|repos_url| List of repos url|
|events_url| List of events url|
|received_events_url| List of received events url|
|type| User account type|
|site_admin| Status of site_admin (Boolean `True` or `False`)|
|contributions| The number of contrubtions done (e.g., 10)|


### Example of Contributors:
```
[
  {
    "login": "aaronthomas",
    "id": 1419558,
    "node_id": "MDQ6VXNlcjE0MTk1NTg=",
    "avatar_url": "https://avatars0.githubusercontent.com/u/1419558?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/aaronthomas",
    "html_url": "https://github.com/aaronthomas",
    "followers_url": "https://api.github.com/users/aaronthomas/followers",
    "following_url": "https://api.github.com/users/aaronthomas/following{/other_user}",
    "gists_url": "https://api.github.com/users/aaronthomas/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/aaronthomas/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/aaronthomas/subscriptions",
    "organizations_url": "https://api.github.com/users/aaronthomas/orgs",
    "repos_url": "https://api.github.com/users/aaronthomas/repos",
    "events_url": "https://api.github.com/users/aaronthomas/events{/privacy}",
    "received_events_url": "https://api.github.com/users/aaronthomas/received_events",
    "type": "User",
    "site_admin": false,
    "contributions": 10
  }
]

```
