# MS4_breadit

## Table of Contents
- [MS4_breadit](#ms4-breadit)
  * [A forum for bakers and bread enthusiasts](#a-forum-for-bakers-and-bread-enthusiasts)
  * [Project Goals](#project-goals)
  * [User Goals](#user-goals)
  * [Site Owner Goals](#site-owner-goals)
  * [User Stories](#user-stories)
    + [Epic 1: Basic functions](#epic-1--basic-functions)
    + [Epic 2: Easy to use](#epic-2--easy-to-use)
    + [Epic 3: Authentication and permission](#epic-3--authentication-and-permission)
    + [Epic 4: Admin](#epic-4--admin)
  * [Design Choices](#design-choices)
    + [Color palette](#color-palette)
    + [Wireframes](#wireframes)
  * [Structure](#structure)
    + [Code directories](#code-directories)
    + [Database](#database)
    + [Data Models](#data-models)
    + [Data Model scheme](#data-model-scheme)
  * [Features](#features)
    + [Navbar](#navbar)
    + [Home Page](#home-page)
    + [User log in and sign up](#user-log-in-and-sign-up)
    + [Post Detail page](#post-detail-page)
    + [Leaving Comments](#leaving-comments)
    + [Add Post](#add-post)
    + [Edit and delete posts](#edit-and-delete-posts)
    + [Admin and staff access](#admin-and-staff-access)
    + [Features still to implement](#features-still-to-implement)
  * [Technologies used](#technologies-used)
    + [Languages](#languages)
    + [Other technologies](#other-technologies)
  * [Testing](#testing)
    + [HTML](#html)
    + [CSS](#css)
    + [Python](#python)
    + [JavaScript](#javascript)
    + [LIGHTHOUSE](#lighthouse)
    + [Devices](#devices)
  * [Bugs](#bugs)
  * [Deployment](#deployment)
    + [Creating the Github repository and cloning it](#creating-the-github-repository-and-cloning-it)
    + [Deploying to Heroku](#deploying-to-heroku)
  * [Credits](#credits)
    + [Tutorials and other resources](#tutorials-and-other-resources)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## A forum for bakers and bread enthusiasts


## Project Goals
The goals for this project are:

- Creating a forum where users can talk and discuss about baking
- Users can sign up and log in to take advantage of the main features
- Users can create, update and delete their posts. They can also engage with posts of other users by liking them and commenting.

My own goals for this project are:
- Creating a user-friendly and simple application
- Improving my skills of web development, especially regarding frameworks(Django), back-end development and python.

## User Goals
- Find information or recipes about baking
- Discuss bakery-related things with other users
- Share recipes, pictures or advice with other users

## Site Owner Goals
- Keep the site friendly and secure by having access to the admin panel, where it's possible to delete posts, comments and users should it be necessary.

## User Stories

### Epic 1: Basic functions
1. As a user I want to see all the breadit posts on the main page so that I can scroll through them.
2. As a user I want to click on a post that seems interesting to me so that I can see more details.
3. As a user I want to see likes, user and number of comments of a post without first having to click on it so that I can decide which posts are most relevant to me.
### Epic 2: Easy to use
4. As a user I want to get redirected to the sign in/sign up page if I click on any links or buttons that require me to be logged in so that I can sign in or sign up easily.
5. As a user I want to get feedback from the site on the actions I have performed so that I can see whether my action was carried out correctly or not.
6. As a user I want to be able to get back to the home page in one click so that I can navigate the site easily.
### Epic 3: Authentication and permission
7. As a user I want to sign up and log in so that I can perform actions reserved for registered users.
8. As a registered user I want to be able to log out so that I have more security.
9. As a registered user I want to be able to create posts so that I can share my recipes, tutorials or advice with other users.
10. As a registered user I want to like posts so that I can express my preferences for certain posts.
11. As a registered user I want to leave comments under posts so that I can discuss topics with other users.
13. As a registered user I want to be able to edit my posts so that I can correct mistakes easily if they happen.
14. As a registered user I want to be able to remove my posts so that I can delete them if I don't like them anymore.
### Epic 4: Admin
15. As a site admin I want to be able to access the admin page so that I can monitor posts and comments and remove them if they are inappropriate.

## Design Choices
My goal was to create a simple site with a clean look. I have opted for two warm primary colors, to create a welcoming atmosphere. The brown and gold colors should remind of the colors of bread (crust and inside).

### Color palette
![html-validator](https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/color-palette.png)

### Wireframes
I used balsamiq for the wireframes. The final wireframe is a bit different from the first version, as i made some changes while creating the project, in accordance with Agile principles.
<details>
<summary>Wireframes for mobile</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/wireframes/Mobile_wireframe.png' alt='mobile wireframe'>
</details>

<details>
<summary>Wireframes for tablet</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/wireframes/Tablet_wireframe.png' alt='tablet wireframe'>
</details>

<details>
<summary>Wireframes for desktop</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/wireframes/Desktop_wireframe.png' alt='desktop wireframe'>
</details>

## Structure
### Code directories
Breadit was created with the Django framework, so it is divided into apps:
- breadit is the main app, where settings.py can be found
- The other two apps are accounts and forum. Forum is the core part of the app.

Other directories:
- static: This is where the custom CSS and JavaScript files for this project are stored.
- templates: This is where all the templates (html files) are stored, as is usual with Django.
- docs: in this directory I stored all the images and screenshots needed for this Readme file.

### Database
This website relies heavily on a databse. I used postgreSQL as database both for development and for the deployed version.

### Data Models
Data Models are a central part of this project. There are three data models I used:

- User: This is a built-in data model that comes with Django. It is used for authentication and authorisation.
- Post: This is my own data model, used for all the posts you see on my site.
- Comment: This is another data model I created. I drew a lot of inspiration for this model from CodeInstitute's Django walkthrough project, which has a similar model.

### Data Model scheme
<img src="https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/wireframes/database-schema.png" alt="database schema">

This scheme was made with Lucidchart.

## Features 

### Navbar

The navbar is sticky and thus offers a quick and easy way to return to the Homepage, wherever the user is in the page.
For users that are logged out, it will display the option to sign up or log in, and for users who are already logged in it will display their username (so they know that they are logged in) and if they are a superuser or staff member they will see a link to the admin panel.

<details>
<summary>Navbar when not logged in</summary>
<img src='breadit/docs/features/navbar-loggedout.png' alt='Navbar screenshot'>
</details>
<details>
<summary>Navbar when logged in (user has admin or staff privilege)</summary>
<img src='breadit/docs/features/navbar-loggedin.png' alt='Navbar screenshot'>
</details>

User stories covered:
- 6. As a user I want to be able to get back to the home page in one click so that I can navigate the site easily.

### Home Page

The home page is the central part of Breadit: this is where all the posts are displayed (the latest posts are displayed on top) and where the user can see more information about them.
From here the user can scroll through the posts and click on the ones they like. Information about the posts is visible from the home page, like the user who created the post, publication date, number of likes and number of comments.
The user can also decide to add their own post to the site, but they need to be logged in to do that.
<details>
<summary>Home page</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/homepage.png' alt='home page screenshot'>
</details>

User stories covered:
- 1. As a user I want to see all the breadit posts on the main page so that I can scroll through them.
- 3. As a user I want to see likes, user and number of comments of a post without first having to click on it so that I can decide which posts are most relevant to me.
- 8. As a registered user I want to be able to log out so that I have more security.

### User log in and sign up
These are the forms used to sign the user up or log them in. If an anonymous user tries to access a forbidden view, they will be redirected to the login page.
<details>
<summary>Log in</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/login.png' alt='log in screenshot'>
</details>

<details>
<summary>Sign up</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/signup.png' alt='sign up screenshot'>
</details>

User stories covered:
- 4. As a user I want to get redirected to the sign in/sign up page if I click on any links or buttons that require me to be logged in so that I can sign in or sign up easily.
- 7. As a user I want to sign up and log in so that I can perform actions reserved for registered users.


### Post Detail page
This is where the users can see more details about a post. The full lenght of the post text can be seen here, and the comments and likes as well. The user can also like a post if they are signed in.
<details>
<summary>Post detail</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/post-detail1.png' alt='post detail screenshot'>
</details>

User stories covered:
- 10. As a registered user I want to like posts so that I can express my preferences for certain posts.
- 13. As a registered user I want to be able to edit my posts so that I can correct mistakes easily if they happen.
- 14. As a registered user I want to be able to remove my posts so that I can delete them if I don't like them anymore.

### Leaving Comments
This is where registered users can leave a comment.
<details>
<summary>Comments</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/post-detail2.png' alt='comment screenshot'>
</details>

User stories covered:
- 11. As a registered user I want to leave comments under posts so that I can discuss topics with other users.

### Add Post
This is where registered users can create their own post. They can add an image but don't have to, but it's mandatory to fill both the title and the content fields.
<details>
<summary>Add Post</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/createpost.png' alt='add post screenshot'>
</details>
<details>
<summary>Add Post alert for wrong media file</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/createpost-alert.png' alt='media file alert screenshot'>
</details>

User stories covered:
- 9. As a registered user I want to be able to create posts so that I can share my recipes, tutorials or advice with other users.
- 5. As a user I want to get feedback from the site on the actions I have performed so that I can see whether my action was carried out correctly or not.

### Edit and delete posts
Registered users can also delete or edit their own posts. An attempt to modify or delete the post of a different user through url modification will raise a 403 error.
<details>
<summary>Edit Post</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/update-post.png' alt='Edit Post screenshot'>
</details>
<details>
<summary>Delete Post</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/post-delete.png' alt='delete Post screenshot'>
</details>

User stories covered:
- 14. As a registered user I want to be able to remove my posts so that I can delete them if I don't like them anymore.
- 13. As a registered user I want to be able to edit my posts so that I can correct mistakes easily if they happen.

### Admin and staff access
Users that have superuser or staff privileges can access the admin panel from their navbar. From there, they can delete users, posts and comments if necessary.
<details>
<summary>Admin Panel</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/admin.png' alt='admin panel screenshot'>
</details>

User stories covered:
- 15. As a site admin I want to be able to access the admin page so that I can monitor posts and comments and remove them if they are inappropriate.

### Features still to implement
- A user profile where users can edit their information\
- A search bar to search for posts or comments
- A chat for users

## Technologies used
The primary technology used here was the Django framework
### Languages
- HTML5 for building the web pages
- CSS3 for styling the web pages (although I used mainly Bootstrap 5)
- JavaScript for validating the media input field 
- Python 3 for the backend programming and database manipulation

### Other technologies
Apart from the programming languages, I have used the following:

- [Heroku](https://www.heroku.com/) for deploying and hosting my site.
- [Git](https://git-scm.com/) and [GitHub](https://github.com/) for version control and storage of my code 
- [Cloudinary](https://cloudinary.com/) for hosting the image files
- [postgreSQL](https://www.postgresql.org/) as a database
- [Balsamiq Wireframes](https://balsamiq.com/) for creating my wireframes
- [Lucidchart](https://www.lucidchart.com/pages/de) for creating the data schema for my models
- [Font Awesome](https://fontawesome.com/) - All icons are from Font Awesome
- [Google Fonts](https://fonts.google.com/) - I used the Roboto and Open Sans fonts from Google Fonts
- [VSCode](https://code.visualstudio.com/) - The code editor where I wrote all my code.

## Testing

### HTML
No errors were returned when passing through the official [W3C validator](https://validator.w3.org/).
Please see the screenshots for HTML here: [HTML validation](https://github.com/Damianjacob/MS4_breadit/tree/main/breadit/docs/validation/html-validation) .

### CSS
No errors were found when passing through the [Jigsaw validator](https://jigsaw.w3.org/css-validator/).
<img src="https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/validation/css-validation/css-validation.png">

### Python
All my Python documents passed through the PEP8 validator without any errors. The result was the following for all of them.
<img src="https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/validation/css-validation/css-validation.png">

### JavaScript
My JavaScript file passed through the JSHint validation without any errors.
<img src="https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/validation/javascript-validation/javascript-validation.png">

### LIGHTHOUSE
All of the pages in this site have achieved a total score of at least 89 in Google Lighthouse (for performance, accessibility, SEO and best practices.)
You can see the results [here](https://github.com/Damianjacob/MS4_breadit/tree/main/breadit/docs/validation/performance).

### Devices
The testing was done on a Mac Mini and iPhone. I tested Google Chrome and Safari, and the site was functional and responsive for all devices (I used the list of devices available in the web inspector).

## Bugs

- "ModuleNotFoundError: _tkinter" while trying to load the page in Heroku.
Fix: One of the Python files had automatically imported a module called "turtle" which contains tkinter. Deleted turtle import.

- Duplicate Keys: duplicate slugs for some new posts.
Fix: used the "uuid" python module and the post title for slugs.

- Media file validation accepts any file extension or accepts no file extension (breadit.js)
Fix: "for" loops in JavaScript return the index of an array element, not its value. Adapted the function accordingly.

- Login template not found.
Fix: Moved login.html template into the "registration" folder, as prescribed by django.

- Server Error (500) with DEBUG=False
This has been a consistent error on both my local development environment and on Heroku.
some of the troubleshootings have included:
- running "collectstatic" on Heroku
- Hosting static files on cloudinary
- Installing whitenoise
- Downloading all django files into staticfiles directory, as suggestion from Tutor

None of this has worked. I have tried to troubleshoot with a Tutor who gave me some very helpful tips, but while the solution worked on Gitpod it did not work for me. I still got a Server error both locally and on Heroku. I feel really out of my depth with this error and I feel like I have tried everything. I have taken the decision to submit my project with DEBUG=True, knowing that this should never happen, but I wanted to show a functioning site.

## Deployment

### Creating the Github repository and cloning it
- Go to Github to your profile
- Go to repositories and click on "New"
- Choose a name and the settings you prefer, then click on "create repository"
- Go to the repository
- Click on "code", and copy the HTTPS address
- In VSCode, click on "Clone Git repository"
- Paste the address of your repository and press enter. 

### Deploying to Heroku
- Create account at Heroku
- Create new app, give it a name and select your region
- Go to Settings
- Under Config Vars add your secret data (for example environment variables like API keys)
- Add Heroku Postgres Add-on
- In the deployment tab, select the preferred deployment method (I chose Github)
- Connect your app to your GitHub repository
- Enable automatic deploys
- For any issues it's useful to consult the build log in the activity tab
- Before going public, it's very important to set DEBUG to false in the django settings.py file.


## Credits
I would like to thank my Mentor Mo Shami for his guidance and the team of Tutors of Code Institute for nudging me in the right direction when I was panicking because my code for uploading an image was not working as intended. I would also like to thank the people who created the teaching material at Code Institute, I often referred back to it while making this project and it helped me a lot.

### Tutorials and other resources
During the researches I did, I found a lot of very helpful material. Some of the resources I used are the following:

- Slugs in django: https://learndjango.com/tutorials/django-slug-tutorial
- The answer to why "post.user" and "user.username" did not result as equal in my templates: https://stackoverflow.com/questions/60955686/the-if-equal-not-working-in-django-template
- How to display a message for DeleteView: https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
- Tutorial for adding a sign up view: https://learndjango.com/tutorials/django-signup-tutorial

I have used the [Django Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) and read the Django documentation extensively during the creation of this project.


