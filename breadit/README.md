# MS4_breadit

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
15. As a registered user I want to be able to edit my own comments so that I can correct mistakes easily.
### Epic 4: Admin
16. As a site admin I want to be able to access the admin page so that I can monitor posts and comments and remove them if they are inappropriate.

## Design Choices
My goal was to create a simple site with a clean look. I have opted for two warm primary colors, to create a welcoming atmosphere. The brown and gold colors should remind of the colors of bread (crust and inside).

### Color palette
![html-validator](https://github.com/Damianjacob/MS4_breadit/blob/main/docs/features/color-palette.png)

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

<details>
<summary>Navbar when not logged in</summary>
<img src='breadit/docs/features/navbar-loggedout.png' alt='Navbar screenshot'>
</details>
<details>
<summary>Navbar when logged in (user has admin or staff privilege)</summary>
<img src='breadit/docs/features/navbar-loggedin.png' alt='Navbar screenshot'>
</details>

User stories covered:

### Home Page

User stories covered:

### User log in and sign up

User stories covered:

### Post Detail page

User stories covered:

### Leaving Comments

User stories covered:

### Add Post

User stories covered:

### Edit and delete posts

User stories covered:

### Admin and staff access

User stories covered:






### Existing features
<!-- Work in progress -->
<!-- optional: features left to implement -->

## Technologies used

Hosting: Heroku
Version Control: Git, GitHub
Languages: Python
For hosting media files: Cloudinary
Database: PostgreSQL

## Testing

### HTML
No errors were returned when passing through the official W3C validator

<!-- ![html-validator](https://github.com/Damianjacob/CI_MS1_Music_Pro/blob/master/assets/images/readme-images/htmlchecker-about-us.png)   -->

### CSS
No errors were found when passing through the official (Jigsaw) validator
<!-- ![css-validator](https://github.com/Damianjacob/CI_MS1_Music_Pro/blob/master/assets/images/readme-images/cssvalidator-about-us.png)   -->

### ACCESSIBILITY
<!-- There is one error because of an empty form label on index.html, however i need that label to stay empty for my responsive nav bar to show correctly as a hamburger menu.  The same goes for the instruments.html page in the buy modal: there are empty labels because i used icons from font awesome for those labels. -->

### LIGHTHOUSE
All of the pages in this site have achieved a score over 90 in performance, accessibility, best practices and SEO.

<!-- ![lighthouse](https://github.com/Damianjacob/CI_MS1_Music_Pro/blob/master/assets/images/readme-images/index.html-performance.png)   -->

### Fixed errors


## Bugs

## Deployment

The site was deployed to Heroku by connecting it go my GitHub repository and enabling automatic deploys.
The steps I followed to deploy the site on Heroku can be found here: https://devcenter.heroku.com/articles/getting-started-with-python#set-up.


## Credits

### Tutorials and other resources

Slugs in django: https://learndjango.com/tutorials/django-slug-tutorial
post.user and user.username not being equal: https://stackoverflow.com/questions/60955686/the-if-equal-not-working-in-django-template

How to display a message for DeleteView: https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown

Tutorial for adding a sign up view: https://learndjango.com/tutorials/django-signup-tutorial

I have used the Django Tutorial and Django documentation extensively during the creation of this project.

### Content

### Media

