# NewsPaperProject
My very first educational Django project (spring 2023)
<hr>

### Techs and languages:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<hr>

### Installation:

- clone the repository:<br>`git clone https://github.com/OneHandedPirate/NewsPaperProject.git`
- cd to the project folder:<br>`cd NewsPaperProject`
- create and activate virtual environment:<br>`virtualenv venv`<br>`source venv/bin/activate`
- install all dependencies:<br>`pip install -r requirements.txt`
- create `.env` file with the following variables:
    + `DJANGO_SK` - DJANGO Secret Key;
    + `EMAIL_HOST_USER` - email (used to send emails to users); 
    + `EMAIL_HOST_PASSWORD` - email app password; 
    + `EMAIL_HOST` - SMTP address;
    + `EMAIL_PORT` - SMTP port;
    + `EMAIL_USE_TLS` - boolean; 
    + `EMAIL_USE_SSL` - boolean;

### Description:
NewsPaperProject is a simple website built using Django, where authenticated users can write articles on any topic. Users can also comment on and rate articles written by other users. Additionally, users have the ability to subscribe to specific categories of articles. 

### Features:

- <b>Registration</b>:<br>When registering one can choose to become author. Authors can write the Articles and News as well as create new categories. Non-author users can become author any moment.
- <b>Social Authentication</b>:<br>Users can log in using their Google account.
- <b>Search</b>:<br>Users can search for posts using author/post title/publish date.
- <b>Subscription to category</b>:<br>Authenticated users can subscribe categories. When new post is published all subscribed users are notified viw email. Subscription to category is implemented via AJAX-requests (without reloading the page)
- <b>Add comments</b>:<br>Authenticated users can add comments to posts. Comment authors can also delete them. Implemented via AJAX-requests. 
- <b>Post edition/deletion</b>:<br>Authors can edit or delete their own posts.
- <b>Voting</b>:<br>Authenticated users can vote on posts (but  not their authors). Implemented via AJAX-requests.
- <b>Feedback</b>:<br>Authenticated users can send feedback via Contact Us form. Feedback is sent to your email (EMAIL_HOST_USER).

### Screenshots:

- Sign up page.
![sign up.png](screenshots%2Fsign%20up.png)


- Login page with Google auth button.
![login.png](screenshots%2Flogin.png)


- Main page with the list of posts. The categories subscribed by the current user are dark.
![main_page.png](screenshots%2Fmain_page.png)


- Post details page. Edit and delete buttons are visible only for author of the post.
![detail_view.png](screenshots%2Fdetail_view.png)


- Add comment modal window.
![create_comment.png](screenshots%2Fcreate_comment.png)


- Comment on the post page. Delete button is visible only for author of the comment.
![comment.png](screenshots%2Fcomment.png)


- Post delete confirmation.
![postdelete_confirmation.png](screenshots%2Fpostdelete_confirmation.png)


- Add post page. The add post and add category menu navbar items are visible only for authors.
![add_post.png](screenshots%2Fadd_post.png)


- Add category modal window.
![add_category.png](screenshots%2Fadd_category.png)


- Feedback form.
![Feedback_form.png](screenshots%2FFeedback_form.png)