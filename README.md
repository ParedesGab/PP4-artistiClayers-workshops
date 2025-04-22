# [PP4-artistiClayers-workshops](https://artisticlayers-d41862efab95.herokuapp.com)

(Developer: Gabriela Fabiola Paredes Rojas)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ParedesGab/PP4-artistiClayers-workshops)](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/ParedesGab/PP4-artistiClayers-workshops)](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/ParedesGab/PP4-artistiClayers-workshops)](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops)

![Responsive Mockup image](documentation/website-screenshots/responsive-mockup.png)

**Welcome to ArtistiClayers!**

Ready to mold, sculpt, and bake your way to amazing creations? Welcome to your go-to spot for booking fun and inspiring polymer clay workshops in the beautiful Vienna! Explore our range of classes for all skill levels and unleash your inner artist. 

Let's get claying! 🎉

+ The site can be accessed via this [link](https://artisticlayers-d41862efab95.herokuapp.com)

---

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "I Think Therefore I Blog".

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Provide users a booking platform for polymer clay workshops in Vienna, catering to all skill levels: beginner, intermediate, and advanced. We offer a workshop designed for everyone.
- Provide workshop owners with tools to create, view and manage their own bookings. 
- Offer users an intuitive platform to explore and book our available polymer clay workshops, and the possibility of contacting us for any questions.

##### Primary User Needs
- Potential Workshop Attendees: Need an intuitive platform to explore available polymer clay workshops (beginner, intermediate, advanced), and easily book their desired sessions.
- Registered Users: Need the ability to view, create and manage (edit and/or delete) their bookings, and receive confirmation messages of their actions.

##### Business Goals
- Captivate users with inspiring polymer clay visuals showcased throughout the website to encourage workshop booking and selection.
- Create an engaging platform that empowers users to easily book and manage their polymer clay workshop experiences.
- Ensure easy booking and booking management for owners.

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- Booking workshop management (create, update, delete, and view).
- User account features (register, log in, edit/delete own bookings).
- Notification system when editing/deleting bookings.
- 404 error page for lost users.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, About, Workshops, Contact, Bookings, Sign in, Sign up, Sign out.
- **Hierarchy**:
  - Clear call-to-action buttons for display of available workshops.
  - Clear call-to-action buttons for booking creations and management (e.g., update or delete a booking).

##### User Flow
1. Registered users create a booking for a workshop → receive a confirmation message on top of the page and the booking appears now in "My bookings".
2. Booking owners update, and manage own bookings.
3. Workshop owners create, update, and manage workshop levels (i.e., beginner, intermediate and advanced).
5. Workshop owners approve or reject collaboration requests.

#### 4. Skeleton Plane
##### Wireframe Suggestions
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements
- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

**Main color scheme**

![Color Scheme](documentation/website-screenshots/coolors.png)

- The website's color scheme features a vibrant orange and a soft champagne pink as cohesive elements. This choice was deliberate to complement the colorful background images, providing a nude-toned contrast that allows the imagery to stand out prominently.

- The buttons are styled in vibrant colors to ensure that they stand out.

### Typography

- [Roboto](https://fonts.google.com/specimen/Roboto) from Google Fonts was used for the logo (i.e., ArtistiClayers).
- [bs-font-sans-serif](https://getbootstrap.com/docs/5.1/customize/css-variables/) The rest of the website's typography utilizes Bootstrap's $font-family-sans-serif variable (bs-font-sans-serif) for its primary sans-serif font stack, ensuring consistency with the Bootstrap design system.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site in the footer (social media icons).

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a User | I would like to regardless of the page I am in, I can click on the ArtistiClayers logo | so that I am taken back to the Home page. |
| As a User | I would like to easily locate the navbar across all website pages | so that I can efficiently access different sections of the website. |
| As a User | I would like to easily recognized which navbar link I clicked | so that I can efficiently see in which section of the website I am. |
| As a User | I would like to have a footer across all website pages | so that I can  see the different social media links that ArtistiClayers have. |
| As a User | I would like to click on the social media links| so that I can  efficiently access different social media links to connect and engage with ArtistiClayers social platforms. |
| As a User | I would like to find an intuitive, welcoming and enjoyable Home page | so that I can easily understand the purpose of the website and remain on it. |
| As a User | I would like to be drawn to click the button "Our Workshops" in the home page | so that I can easily have access to the list of workshops. |
| As a User | I would like to find an intuitive and user-friendly About page | so that I learn about the workshop's tutor experience and further understand the concept of ArtistiClayers. |
| As a User | I would like to see the available workshops | so that I can gather detailed information and choose the best fit for my learning needs. |
| As a User | I would like to be able to click each workshop card | so that I can be directed to a more detailed page of each workshop. |
| As a Logged in User | I would like to see and click a button to book a workshop | so that I can book my desired workshop. |
| As a Non-logged in User | I would like to see and click a button stating that to book a workshop Log in and/or Register is first required | so that I am aware I need to log in or register to book a workshop.|
| As a User | I would like to be able to submit a contact form | so that I can request a collaboration with the site owner or ask questions I might have. |
| As a User | I would like to receive a notification or message saying my contact request is pending approval | so that I understand it hasn't been posted immediately. |
| As a Site Admin | I would like to accept or reject contact/collaboration requests | so that I can manage collaboration requests|
| As a Site Admin | I would like to access the Admin panel | so that I can manage bookings, collaboration requests, user accounts and the about me page |
| As a Site Admin | I would like to access the workshops content in the Admin panel | so that I can manage them and display them with the desired content in the website. |
| As a User | I would like to register an account | so that I log in to my private account and manage my bookings or book a desired workshop |
| As a User | I would like to Sign in to my account | so that I log in to my private account and manage my bookings or book a desired workshop |
| As a Logged in User | I would like to be able to choose for my booking: one of the available workshop levels, choose the number of people participating (min 0, max 10), and choose the appointment date and appointment time | so that I can participate to one of the workshops with my desired selection. |
| As a Logged in User | I would like to receive clear and specific error messages if I make a mistake in any of the booking fields | so that I can easily identify and correct the errors to successfully complete my booking. |
| As a Logged in User | I would like to book from only three pre selected time slots | so that scheduling is simplified with a few clear choices. |
| As a Logged in User | I would like to see a "Thank you for you booking" message displayed | so that I know that my booking was successfully created. |
| As a Logged in User | I would like to see all bookings I created | so that I can visualize them and update them or delete them if desired. |
| As a Logged in User | I would like to distinguis the update from the delete button, and the past from the "today" bookings | so that I can visualize them and, if possible, update them or delete them if desired. |
| As a Site owner | I would like the booking system to prevent users from selecting appointment dates that are in the past or the current day | so that booking errors are avoided and the workshop tutor has adequate preparation time based on the number of attendees. |
| As a Site owner | I would like to not allow updates or deletions of past bookings | so that I can maintain control over the past bookings. |
| As a Site owner | I would like to not allow updates or deletions of bookings made for the current day | so that the Tutor receives timely notification of any changes with adequate advance notice.|
| As a Site owner | I would like the booking system to prevent users from selecting either 0 or more than 10 participants for workshop | so that adequate materials and proper attention can be provided to each attendee. |
| As a Logged in User | I would like to log out | so that my account is secured from unauthorized use. |
| As a Logged in User | I would like to create a booking | so that  I can participate to one of the workshops. |
| As a Logged in User | I would like to, before logging out, be presented with a confirmation message to ensur I wish to end my session | so that I can rethink whether I want to log out or maybe I clicked it by mistake.|
| As a Logged out User | I would like to see a confirmation message that I logged out, and be redirected to the Home page | so that I know the log out was succesful and that I am not redirected to an unkown website. |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. |

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| About | ![screenshot](documentation/wireframes/mobile-about.png) | ![screenshot](documentation/wireframes/tablet-about.png) | ![screenshot](documentation/wireframes/desktop-about.png) |
| Worshops list | ![screenshot](documentation/wireframes/mobile-workshops.png) | ![screenshot](documentation/wireframes/tablet-workshops.png) | ![screenshot](documentation/wireframes/desktop-workshops.png) |
| Each workshop | ![screenshot](documentation/wireframes/mobile-workshop.png) | ![screenshot](documentation/wireframes/tablet-workshop.png) | ![screenshot](documentation/wireframes/desktop-workshop.png) |
| Contact | ![screenshot](documentation/wireframes/mobile-contact.png) | ![screenshot](documentation/wireframes/tablet-contact.png) | ![screenshot](documentation/wireframes/desktop-contact.png) |
| Bookings | ![screenshot](documentation/wireframes/mobile-bookings.png) | ![screenshot](documentation/wireframes/tablet-bookings.png) | ![screenshot](documentation/wireframes/desktop-bookings.png) |
| Update Booking | ![screenshot](documentation/wireframes/mobile-edit-booking.png) | ![screenshot](documentation/wireframes/tablet-edit-booking.png) | ![screenshot](documentation/wireframes/desktop-edit-booking.png) |
| Delete Booking | ![screenshot](documentation/wireframes/mobile-delete-booking.png) | ![screenshot](documentation/wireframes/tablet-delete-booking.png) | ![screenshot](documentation/wireframes/desktop-delete-booking.png) |
| Sign in | ![screenshot](documentation/wireframes/mobile-sign-in.png) | ![screenshot](documentation/wireframes/tablet-sign-in.png) | ![screenshot](documentation/wireframes/desktop-sign-in.png) |
| Logout | ![screenshot](documentation/wireframes/mobile-logout.png) | ![screenshot](documentation/wireframes/tablet-logout.png) | ![screenshot](documentation/wireframes/desktop-logout.png) |
| Sign up | ![screenshot](documentation/wireframes/mobile-sign-up.png) | ![screenshot](documentation/wireframes/tablet-sign-up.png) | ![screenshot](documentation/wireframes/desktop-sign-up.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Blog List | The homepage displays basic information about blog posts, including image, title, author, date, and a brief excerpt. | ![screenshot](documentation/features/blog-list.png) |
| View Post | Users can view the full blog post details, including any comments. | ![screenshot](documentation/features/view-post.png) |
| Pagination | Blog posts are displayed in pages, with six posts per page. This provides better navigation for users through the post list. | ![screenshot](documentation/features/pagination.png) |
| Add Comments | Authenticated visitors can comment on blog posts; comments require approval before being published. | ![screenshot](documentation/features/add-comment.png) |
| Edit Comments | Authenticated visitors can edit their own comments. | ![screenshot](documentation/features/edit-comment.png) |
| Delete Comments | Authenticated visitors can delete their own comments. | ![screenshot](documentation/features/delete-comment.png) |
| Comment Approvals | Admins can approve or disapprove comments submitted by users before they are visible on the blog post. | ![screenshot](documentation/features/comment-approval.png) |
| Create Post | Site owners can create/publish blog posts, including setting a featured image using Cloudinary, all from the Django admin dashboard. | ![screenshot](documentation/features/create-post.png) |
| Update Post | Site owners can update/manage blog posts from the Django admin dashboard. | ![screenshot](documentation/features/update-post.png) |
| Delete Post | Site owners can delete blog posts from the Django admin dashboard. | ![screenshot](documentation/features/delete-post.png) |
| About Page | The About page displays the latest information about the site author, along with the option for visitors to send collaboration requests. | ![screenshot](documentation/features/about.png) |
| Collaboration Requests | Visitors can submit collaboration requests from the *About* page, which are later reviewed by the admin. | ![screenshot](documentation/features/collaboration.png) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/features/messages.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

- **User Profiles**: Create personalized user profiles where authenticated users can view their bookings and account information.
- **Notifications**: Implement a notification system that alerts users when their booking appointment is soon coming.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for updates, and booking confirmations.
- **Multilingual Support**: Add the ability to write and view the workshops in multiple languages, broadening the audience.
- **Custom Themes for Users**: Allow users to customize the visual theme of the site (colors, fonts, etc.) to suit their preferences.
- **Online payment implementation**: Implement secure payment using various payment methods so that users can conveniently finalize their booking and guarantee their spot without needing to handle cash or payment in person.
- **Guest booking capability**: Enable users who are not registered or logged in to book workshops by providing necessary contact and booking details, offering a quick and easy way to secure a spot without account creation.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README template |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |


## Database Design

### Data Model

![screenshot](documentation/erd.png)


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/projects) served as an Agile tool for this project. Through it, User Stories, issues, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks.

| Link | Screenshot |
| --- | --- |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/ParedesGab/PP4-artistiClayers-workshops)](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### GitHub Milestones

[GitHub Milestones ](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/projects) served as an Agile tool for this project.

![screenshot](documentation/gh-milestones.png)

### MoSCoW Prioritization

I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- |
| home | [index.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/templates/home/index.html) | [W3 home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2F) | ![screenshot](documentation/validation/html-home-index.png) |
| about | [about.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/tree/main/about/templates/about) | [W3 about](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/validation/html-about-about.png) |
| workshop list | [workshop_list.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/workshop_list.html) | [W3 workshop list](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fworkshops%2F) | ![screenshot](documentation/validation/html-workshop-workshop-list.png) |
| workshop beginner | [workshop_detail.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/workshop_detail.html) | [W3 workshop beginner](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fworkshops%2Fworkshop%2F12%2F) | ![screenshot](documentation/validation/html-workshop-workshop-detail-beginner.png) |
| workshop intermediate | [workshop_detail.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/workshop_detail.html) | [W3 workshop intermediate](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fworkshops%2Fworkshop%2F15%2F) | ![screenshot](documentation/validation/html-workshop-workshop-detail-intermediate.png) |
| workshop advanced | [workshop_detail.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/workshop_detail.html) | [W3 workshop advanced](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fworkshops%2Fworkshop%2F16%2F) | ![screenshot](documentation/validation/html-workshop-workshop-detail-advanced.png) |
| contact | [collaboration.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/templates/collaboration/collaboration.html) | [W3 contact](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/validation/html-contact.png) |
| sign in | [login.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/templates/account/login.html) | [W3 sign in](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/validation/html-login.png) |
| sign up | [signup.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/templates/account/signup.html) | [W3 sign up](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/validation/html-home-post_list.png) |
| bookings | [booking.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/booking.html) | N/A | ![screenshot](documentation/validation/html-booking.png) |
| update booking | [booking_edit.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/booking_edit.html) | N/A | ![screenshot](documentation/validation/html-booking-edit.png) |
| delete booking | [booking_delete.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/booking_delete.html) | N/A | ![screenshot](documentation/validation/html-booking-delete.png) |
| Log out | [logout.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/templates/account/logout.html) | N/A | ![screenshot](documentation/validation/html-logout.png) |
| 404 | [404.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/templates/404.html) | N/A | ![screenshot](documentation/validation/html-404.png) |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- |
| static | [style.css](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/static/css/style.css) | [CSS style Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/css-static-style.png) |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate my JS code inserted in the templates [booking.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/booking.html) and [booking_edit.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/booking_edit.html). 

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| workshop | [booking.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/booking.html) [booking_edit.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/booking_edit.html)  | N/A | ![screenshot](documentation/validation/js-script.png) | Both, booking.html and booking_edit.html templates have the same JS code.


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- |
| about | [admin.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/admin.py) | ![screenshot](documentation/validation/py-about-admin.png) |
| about | [models.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/models.py) | ![screenshot](documentation/validation/py-about-models.png) |
| about | [tests.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/main/about/tests.py) | ![screenshot](documentation/validation/py-about-tests.png) |
| about | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/urls.py) | ![screenshot](documentation/validation/py-about-urls.png) |
| about | [views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/views.py) | ![screenshot](documentation/validation/py-about-views.png) |
| artisticlayers | [settings.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/artisticlayers/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/artisticlayers/settings.py) | ![screenshot](documentation/validation/py-artisticlayers-settings.png) |
| artisticlayers | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/artisticlayers/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/main/artisticlayers/urls.py) | ![screenshot](documentation/validation/py-artisticlayers-urls.png) |
| collaboration | [admin.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/collaboration/admin.py) | ![screenshot](documentation/validation/py-collaboration-admin.png) |
| collaboration | [models.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/models.py) | ![screenshot](documentation/validation/py-collaboration-models.png) |
| collaboration | [forms.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/models.py) | ![screenshot](documentation/validation/py-collaboration-forms.png) |
| collaboration | [tests.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/main/about/tests.py) | ![screenshot](documentation/validation/py-collaboration-tests.png) |
| collaboration | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/urls.py) | ![screenshot](documentation/validation/py-collaboration-urls.png) |
| collaboration | [views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/views.py) | ![screenshot](documentation/validation/py-collaboration-views.png) |
| home | [admin.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/admin.py) | N/A | N/A |
| home | [models.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/models.py) | N/A | N/A |
| home | [tests.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/main/home/tests.py) | ![screenshot](documentation/validation/py-home-tests.png) |
| home | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) |
| home | [views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) |
| workshop | [admin.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/admin.py) | ![screenshot](documentation/validation/py-workshop-admin.png) |
| workshop | [models.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/models.py) | ![screenshot](documentation/validation/py-workshop-models.png) |
| workshop | [forms.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/forms.py) | ![screenshot](documentation/validation/py-workshop-forms.png) |
| workshop | [tests.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/main/home/tests.py) | ![screenshot](documentation/validation/py-workshop-tests.png) |
| workshop | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/urls.py) | ![screenshot](documentation/validation/py-workshop-urls.png) |
| workshop | [views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/views.py) | ![screenshot](documentation/validation/py-workshop-views.png) |
| | [manage.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | Notes (if applicable) |


## Responsiveness

- The website was checked across devices using the chrome extension [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en).

- In addition, it was manually checked in the following devices:
  - Huawei Y9 Prime 2019
  - Iphone XR
  - Iphone 15 pro
  - Samsung Galaxy S8

## Browser Compatibility

The website was tested on the following browsers:
- Google Chrome
- Firefox
- Microsof Edge


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| --- | --- | --- |
| About | ![screenshot](documentation/lighthouse/mobile-about.png) | ![screenshot](documentation/lighthouse/desktop-about.png) |
| Workshops | ![screenshot](documentation/lighthouse/mobile-workshops.png) | ![screenshot](documentation/lighthouse/desktop-workshops.png) |
| Workshop | ![screenshot](documentation/lighthouse/mobile-workshop.png) | ![screenshot](documentation/lighthouse/desktop-workshop.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| Booking | ![screenshot](documentation/lighthouse/mobile-booking.png) | ![screenshot](documentation/lighthouse/desktop-booking.png) |
| Update Booking | ![screenshot](documentation/lighthouse/mobile-update-booking.png) | ![screenshot](documentation/lighthouse/desktop-update-booking.png) |
| Delete Booking | ![screenshot](documentation/lighthouse/mobile-delete-booking.png) | ![screenshot](documentation/lighthouse/desktop-delete-booking.png) |
| Sign in | ![screenshot](documentation/lighthouse/mobile-sign-in.png) | ![screenshot](documentation/lighthouse/desktop-sign-in.png) |
| Sign up | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Log out| ![screenshot](documentation/lighthouse/mobile-logout.png) | ![screenshot](documentation/lighthouse/desktop-logout.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Blog Management | Feature is expected to allow the blog owner to create new posts with a title, featured image, and content. | Created a new post with valid title, image, and content data. | Post was created successfully and displayed correctly in the blog. | ![screenshot](documentation/defensive/create-post.png) |
| | Feature is expected to allow the blog owner to update existing posts. | Edited the content of an existing blog post. | Post was updated successfully with the new content. | ![screenshot](documentation/defensive/update-post.png) |
| | Feature is expected to allow the blog owner to delete blog posts. | Attempted to delete a blog post, confirming the action before proceeding. | Blog post was deleted successfully. | ![screenshot](documentation/defensive/delete-post.png) |
| | Feature is expected to retrieve a list of all published posts. | Accessed the blog owner dashboard to view all published posts. | All published posts were displayed in a list view. | ![screenshot](documentation/defensive/published-posts.png) |
| | Feature is expected to preview posts as drafts before publishing. | Created a draft post and previewed it. | Draft was displayed correctly in preview mode. | ![screenshot](documentation/defensive/preview-draft.png) |
| Comments Management | Feature is expected to allow the blog owner to approve or reject comments. | Approved and rejected comments from the dashboard. | Approved comments were published; rejected comments were removed. | ![screenshot](documentation/defensive/review-comments.png) |
| | Feature is expected to allow the blog owner to edit or delete comments. | Edited and deleted existing comments. | Comments were updated or removed successfully. | ![screenshot](documentation/defensive/edit-delete-comments.png) |
| User Authentication | Feature is expected to allow registered users to log in to the site. | Attempted to log in with valid and invalid credentials. | Login was successful with valid credentials; invalid credentials were rejected. | ![screenshot](documentation/defensive/login.png) |
| | Feature is expected to allow users to register for an account. | Registered a new user with unique credentials. | User account was created successfully. | ![screenshot](documentation/defensive/register.png) |
| | Feature is expected to allow users to log out securely. | Logged out and tried accessing a restricted page. | Access was denied after logout, as expected. | ![screenshot](documentation/defensive/logout.png) |
| User Comments | Feature is expected to allow registered users to leave comments on blog posts. | Logged in and added comments to a blog post. | Comments were successfully added and marked as pending approval. | ![screenshot](documentation/defensive/add-comment.png) |
| | Feature is expected to display a notification that comments are pending approval. | Added a comment and checked the notification message. | Notification was displayed as expected. | ![screenshot](documentation/defensive/pending-approval.png) |
| | Feature is expected to allow users to edit their own comments. | Edited personal comments. | Comments were updated as expected. | ![screenshot](documentation/defensive/edit-user-comments.png) |
| | Feature is expected to allow users to delete their own comments. | Deleted personal comments. | Comments were removed as expected. | ![screenshot](documentation/defensive/delete-user-comments.png) |
| Guest Features | Feature is expected to allow guest users to read blog posts without registering. | Opened blog posts as a guest user. | Blog posts were fully accessible without logging in. | ![screenshot](documentation/defensive/view-posts-guest.png) |
| | Feature is expected to display the names of other commenters on posts. | Checked the names of commenters on posts as a guest user. | Commenter names were displayed as expected. | ![screenshot](documentation/defensive/commenter-names.png) |
| | Feature is expected to block standard users from brute-forcing admin pages. | Attempted to navigate to admin-only pages by manipulating the URL (e.g., `/admin`). | Access was blocked, and a message was displayed showing denied access. | ![screenshot](documentation/defensive/brute-force.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a blog owner | I would like to create new blog posts with a title, featured image, and content | so that I can share my experiences with my audience. | ![screenshot](documentation/features/feature01.png) |
| As a blog owner | I would like to update existing blog posts | so that I can correct or add new information to my previous stories. | ![screenshot](documentation/features/feature02.png) |
| As a blog owner | I would like to delete blog posts | so that I can remove outdated or irrelevant content from my blog. | ![screenshot](documentation/features/feature03.png) |
| As a blog owner | I would like to retrieve a list of all my published blog posts | so that I can manage them from a central dashboard. | ![screenshot](documentation/features/feature04.png) |
| As a blog owner | I would like to preview a post as draft before publishing it | so that I can ensure formatting and content appear correctly. | ![screenshot](documentation/features/feature05.png) |
| As a blog owner | I would like to review comments before they are published | so that I can filter out spam or inappropriate content. | ![screenshot](documentation/features/feature06.png) |
| As a blog owner | I would like to approve or reject comments from users | so that I can maintain control over the discussion on my posts. | ![screenshot](documentation/features/feature07.png) |
| As a blog owner | I would like to view a list of all comments (both approved and pending) | so that I can manage user engagement effectively. | ![screenshot](documentation/features/feature08.png) |
| As a blog owner | I would like to edit or delete user comments | so that I can clean up or remove inappropriate responses after they've been posted. | ![screenshot](documentation/features/feature09.png) |
| As a registered user | I would like to log in to the site | so that I can leave comments on blog posts. | ![screenshot](documentation/features/feature10.png) |
| As a registered user | I would like to register for an account | so that I can become part of the community and engage with the blog. | ![screenshot](documentation/features/feature11.png) |
| As a registered user | I would like to leave a comment on a blog post | so that I can share my thoughts or ask questions about the owner's experiences. | ![screenshot](documentation/features/feature12.png) |
| As a registered user | I would like my comment to show my name and the timestamp | so that others can see who I am and when I left the comment. | ![screenshot](documentation/features/feature13.png) |
| As a registered user | I would like to receive a notification or message saying my comment is pending approval | so that I understand it hasn't been posted immediately. | ![screenshot](documentation/features/feature14.png) |
| As a registered user | I would like to edit or delete my own comments | so that I can fix mistakes or retract my statement. | ![screenshot](documentation/features/feature15.png) |
| As a guest user | I would like to read blog posts without registering | so that I can enjoy the content without needing to log in. | ![screenshot](documentation/features/feature16.png) |
| As a guest user | I would like to browse past posts | so that I can explore the blog's full content history. | ![screenshot](documentation/features/feature17.png) |
| As a guest user | I would like to register for an account | so that I can participate in the community by leaving comments on posts. | ![screenshot](documentation/features/feature18.png) |
| As a guest user | I would like to see the names of other commenters on posts | so that I can get a sense of community interaction before registering. | ![screenshot](documentation/features/feature19.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/feature20.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AParedesGab%2FPP4-artistiClayers-workshops%20label%3Abug&label=bugs)](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issues](https://img.shields.io/github/issues/ParedesGab/PP4-artistiClayers-workshops)](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues)

Any remaining open issues can be tracked [here](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| On devices smaller than 375px, the page starts to have horizontal `overflow-x` scrolling. | ![screenshot](documentation/issues/overflow.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.


## Deployment

The live deployed application can be found deployed on [Heroku](https://artisticlayers-d41862efab95.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION ParedesGab !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️

🛑 --- END --- 🛑

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION ParedesGab !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️

🛑 --- END --- 🛑

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/ParedesGab/PP4-artistiClayers-workshops.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/ParedesGab/PP4-artistiClayers-workshops)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss any differences between the local version you've developed, and the live deployment site. Generally, there shouldn't be [m]any major differences, so if you honestly cannot find any differences, feel free to use the following example:

⚠️ --- END --- ⚠️

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

⚠️ INSTRUCTIONS ⚠️

In the following sections, you need to reference where you got your content, media, and any extra help. It is common practice to use code from other repositories and tutorials (which is totally acceptable), however, it is important to be very specific about these sources to avoid potential plagiarism.

⚠️ --- END ---⚠️

### Content

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links for any borrowed code snippets, elements, and resources. Ideally, you should provide an actual link to every resource used, not just a generic link to the main site. If you've used multiple components from the same source (such as Bootstrap), then you only need to list it once, but if it's multiple Codepen samples, then you should list each example individually. If you've used AI for some assistance (such as ChatGPT or Perplexity), be sure to mention that as well. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links to any media files borrowed from elsewhere (images, videos, audio, etc.). If you're the owner (or a close acquaintance) of some/all media files, then make sure to specify this information. Let the assessors know that you have explicit rights to use the media files within your project. Ideally, you should provide an actual link to every media file used, not just a generic link to the main site, unless it's AI-generated artwork.

Looking for some media files? Here are some popular sites to use. The list of examples below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links by sending yourself (or Slackbot) the following command: `!freemedia`.

- Images
    - [Pexels](https://www.pexels.com)
    - [Unsplash](https://unsplash.com)
    - [Pixabay](https://pixabay.com)
    - [Lorem Picsum](https://picsum.photos) (placeholder images)
    - [Wallhere](https://wallhere.com) (wallpaper / backgrounds)
    - [This Person Does Not Exist](https://thispersondoesnotexist.com) (reload to get a new person)
- Audio
    - [Audio Micro](https://www.audiomicro.com/free-sound-effects)
- Video
    - [Videvo](https://www.videvo.net)
- Image Compression
    - [TinyPNG](https://tinypng.com) (for images <5MB)
    - [CompressPNG](https://compresspng.com) (for images >5MB)

A few examples have been provided below to give you some ideas on how to do your own Media credits.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [I Think Therefore I Blog](https://codeinstitute.net) | Sample images provided from the walkthrough projects |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution and acknowledgement to any supports that helped, encouraged, or supported you throughout the development stages of this project. It's always lovely to appreciate those that help us grow and improve our developer skills. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.

