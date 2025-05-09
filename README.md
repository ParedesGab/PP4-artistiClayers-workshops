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


## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Provide users a booking platform for polymer clay workshops in Vienna, catering to all skill levels: beginner, intermediate, and advanced. We offer a workshop designed for everyone.
- Provide users who have booked workshops with the functionality to create, view, and manage their own bookings.
- Offer users an intuitive platform to explore and book our available polymer clay workshops, and the possibility of contacting us for any questions.

##### Primary User Needs
- Potential Workshop Attendees: Need an intuitive platform to explore available polymer clay workshops (beginner, intermediate, advanced), and easily book their desired sessions.
- Registered Users: Need the ability to view, create and manage (edit and/or delete) their bookings, and receive confirmation messages of their actions.

##### Business Goals
- Captivate users with inspiring polymer clay visuals showcased throughout the website to encourage workshop booking and selection.
- Create an engaging platform that empowers users to easily book and manage their polymer clay workshop experiences.
- Ensure easy booking and booking management for both registered users and the site owner.

#### 2. Scope Plane
##### Features
- A full list of [Existing-features](#existing-features) can be viewed in detail below.

##### Content Requirements
- Booking workshop management (create, update, delete, and view).
- Contact request management by Site owner.
- User account features (sign up, sign in, log out, create a booking, view/edit/delete own bookings).
- Notification system when editing/deleting bookings.
- 404 error page for lost users.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, About, Workshops, Contact, Bookings, Sign in, Sign up, Logout.
- **Hierarchy**:
  - Clear call-to-action buttons for display of available workshops when creating a booking.
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

- The website's color scheme features a vibrant orange and a soft champagne pink as cohesive elements. This choice was deliberate to complement the colorful background images found across all pages, providing a nude-toned contrast that allows the polymer clay imagery to stand out prominently.

- The buttons are styled in vibrant colors to ensure that they stand out.

### Typography

- [Roboto](https://fonts.google.com/specimen/Roboto) from Google Fonts, was used for the logo (i.e., ArtistiClayers).
- [bs-font-sans-serif](https://getbootstrap.com/docs/5.1/customize/css-variables/) The rest of the website's typography utilizes Bootstrap's $font-family-sans-serif variable (bs-font-sans-serif) for its primary sans-serif font stack, ensuring consistency with the Bootstrap design system.
- [Font Awesome](https://fontawesome.com) Icons were used throughout the site, including social media icons in the footer and a hamburger icon in the mobile navbar.

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a User | I would like to regardless of the page I am in, I can click on the ArtistiClayers logo | so that I am taken back to the Home page. |
| As a User | I would like to easily locate the navbar across all website pages | so that I can efficiently access different sections of the website. |
| As a User | I would like to easily recognized which navbar link I clicked | so that I can efficiently see in which section of the website I am. |
| As a User | I would like to have a footer across all website pages | so that I can  see the different social media links that ArtistiClayers have. |
| As a User | I would like to click on the social media links| so that I can  efficiently access different social media links to connect and engage with ArtistiClayers social platforms. |
| As a User | I would like to find an intuitive, welcoming and enjoyable Home page | so that I can easily understand the purpose of the website and want to remain on it and explore further. |
| As a User | I would like to be drawn to click the button "Our Workshops" in the home page | so that I can easily have access to the list of workshops. |
| As a User | I would like to find an intuitive and user-friendly About page | so that I learn about the workshop's tutor experience and further understand the concept of ArtistiClayers. |
| As a User | I would like to see the available workshops | so that I can gather detailed information and choose the best fit for my learning needs. |
| As a User | I would like to be able to click each workshop card | so that I can be directed to a more detailed page of each workshop. |
| As a Logged in User | I would like to see and click a button to book a workshop | so that I can book my desired workshop. |
| As a Non-logged in User | I would like to see and click a button stating that to book a workshop Log in and/or Register is first required | so that I am aware I need to log in or register to book a workshop.|
| As a User | I would like to be able to submit a contact form | so that I can request a collaboration with the site owner or ask questions I might have. |
| As a User | I would like to receive a notification or message saying my contact request is pending approval | so that I understand it hasn't been read immediately. |
| As a Site Admin | I would like to accept or reject contact/collaboration requests | so that I can manage collaboration requests|
| As a Site Admin | I would like to access the Admin panel | so that I can manage bookings, collaboration requests, user accounts and the about me page |
| As a Site Admin | I would like to access the workshops content in the Admin panel | so that I can manage them and display them with the desired content in the website. |
| As a User | I would like to register an account | so that I log in to my private account and manage my bookings or book a desired workshop |
| As a User | I would like to Sign in to my account | so that I log in to my private account and manage my bookings or book a desired workshop |
| As a Logged in User | I would like to create a booking | so that  I can participate to one of the workshops. |
| As a Logged in User | I would like to be able to choose for my booking: one of the available workshop levels, choose the number of people participating (min 0, max 10), and choose the appointment date and appointment time | so that I can participate to one of the workshops with my desired selection. |
| As a Logged in User | I would like to receive clear and specific error messages if I make a mistake in any of the booking fields | so that I can easily identify and correct the errors to successfully complete my booking. |
| As a Logged in User | I would like to book from only three pre selected time slots | so that scheduling is simplified with a few clear choices. |
| As a Logged in User | I would like to see a "Thank you for you booking" message displayed | so that I know that my booking was successfully created. |
| As a Logged in User | I would like to see all bookings I created | so that I can visualize them and update them or delete them if desired. |
| As a Logged in User | I would like to distinguish the update from the delete button, and the past from the "today" bookings | so that I can visualize them and, if possible, update them or delete them if desired. |
| As a Site owner | I would like the booking system to prevent users from selecting appointment dates that are in the past or the current day | so that booking errors are avoided and the workshop tutor has adequate preparation time based on the number of attendees. |
| As a Site owner | I would like to not allow updates or deletions of past bookings (workshops that already took place) | so that I can maintain control over the past bookings. |
| As a Site owner | I would like to not allow updates or deletions of bookings made for the current day | so that the Tutor receives timely notification of any changes with adequate advance notice.|
| As a Site owner | I would like the booking system to prevent users from selecting either 0 or more than 10 participants for workshop | so that adequate materials and proper attention can be provided to each attendee. |
| As a Logged in User | I would like to log out | so that my account is secured from unauthorized use. |
| As a Logged in User | I would like to, before logging out, be presented with a confirmation message to ensure I wish to end my session | so that I can reconsider whether it was accidental or my intended action was to log out. |
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
| Logo | Logo located at the top center of every page. Clicking it always redirects users to the homepage. | ![screenshot](documentation/features/website-logo.png) |
| Navbar | Below the ArtistiClayers logo, a top-center navbar appears on tablets and larger devices, present across all pages. Its links feature a hover effect: orange to indicate the current page and a highlight to show they're clickable.| ![screenshot](documentation/features/website-navigation-bar.png) |
| Navbar | On mobile devices, the responsive navigation bar transforms into a Font Awesome hamburger menu located on the right. | ![screenshot](documentation/features/website-navigation-bar-burgermenu-close.png) |
| Navbar | When clicked, the hamburger menu reveals a drop-down with the navigation links displayed in the center of the page, and a different color (orange) indicates in which page the user is on. | ![screenshot](documentation/features/website-navbar-burgermenu-open.png) |
| Footer | Footer located at the bottom across all pages. Social media links have a hover effect and when clicked a new tab opens with the selected social media platform. | ![screenshot](documentation/features/website-footer.png) |
| Home Page | Vibrant homepage that communicates the website's purpose: unleash your artistic creativity through our offered polymer clay workshops. The background image showcases the potential of polymer clay, while the toucans add a fun, colorful, and eye-catching element. The homepage also features a prominent, vibrant orange button that directs users to our available workshops, revealing an intense purple hover effect for contrast and surprise. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/website-homepage.png) |
| Home Page | The homepage is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-homepage-mobiles.png) |
| Home Page | The homepage is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-homepage-tablets.png) |
| Home Page | When the user logs in or registers, they receive a welcome message. | ![screenshot](documentation/features/website-homepage-message.png) |
| About Page | The About page introduces the tutor with a text and image and highlights the experience and tutor's passion for polymer clay, also inviting the User to explore its colorful world and workshops for all skill levels. The banner image on the About page displays a variety of polymer clay creations, allowing users to see firsthand the material's colorful versatility and limitless potential. The screenshot ilustrates responsiveness in laptops and larger devices.| ![screenshot](documentation/features/website-about.png) |
| About Page | The About page is is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-about-mobiles.png) |
| About Page | The About page is is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-about-tablets.png) |
| Workshops Page | The Workshops displays basic information about the polymer clay workshops, including image, workshop level/name, amd a brief excerpt. Users can see them whether they are logged in or not. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/website-workshops.png) |
| Workshops Page | The Workshops page is is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-workshops-mobiles.png) |
| Workshops Page | The Workshops page is is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-workshops-tablets.png) |
| Workshop Page: Beginners | In the Beginners Workshop page, users can find comprehensive details about this workshop level (title, description, image of an example creation, price, location) and a button to book. If not logged in, users are prompted to register or log in; otherwise, the button says "Book Workshop". The banner image is the same as the About page for style cohesion and it is again a reminder of a variety of polymer clay creations, allowing users to see firsthand the material's colorful versatility and limitless potential. This section is accessible to all Users, and its responsive design on larger devices is shown in the screenshot. | ![screenshot](documentation/features/website-workshop-beginner.png) ![screenshot](documentation/features/website-workshop-beginner-loggedin.png) |
| Workshop Page: Beginners  | The Beginners Workshops page is is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-workshop-beginner-mobiles.png) |
| Workshop Page: Beginners  | The Beginners Workshops page is is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-workshop-beginner-tablets.png) |
| Workshop Page: Intermediate | In the Intermediate Workshops page, users can find comprehensive details about this workshop level (title, description, image of an example creation, price, location) and a button to book. If not logged in, users are prompted to register or log in; otherwise, the button says "Book Workshop". The banner image is the same as the About page for style cohesion and it is again a reminder of a variety of polymer clay creations, allowing users to see firsthand the material's colorful versatility and limitless potential. This section is accessible to all Users, and its responsive design on larger devices is shown in the screenshot.  | ![screenshot](documentation/features/website-workshop-intermediate.png) |
| Workshop Page: Intermediate  | The Intermediate Workshops page is is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-workshop-intermediate-mobiles.png) |
| Workshop Page: Intermediate  | The Intermediate Workshops page is is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-workshop-intermediate-tablets.png) |
| Workshop Page: Advanced | In the Advanced Workshop page, users can find comprehensive details about this workshop level (title, description, image of an example creation, price, location) and a button to book. If not logged in, users are prompted to register or log in; otherwise, the button says "Book Workshop". The banner image is the same as the About page for style cohesion and it is again a reminder of a variety of polymer clay creations, allowing users to see firsthand the material's colorful versatility and limitless potential. This section is accessible to all Users, and its responsive design on larger devices is shown in the screenshot. | ![screenshot](documentation/features/website-workshop-advanced.png) |
| Workshop Page: Advanced  | The Advanced Workshops page is is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-workshop-advanced-mobiles.png) |
| Workshop Page: Advanced  | The Workshops page is is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-workshop-advanced-tablets.png) |
| Contact Page | The contact page allows all users (registered or not) to send collaboration requests, which are then reviewed by the administrator. The screenshot shows its responsiveness on larger devices. | ![screenshot](documentation/features/website-contact.png) |
| Contact Page | The contact page is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-contact-mobile.png) |
| Contact Page | The contact page is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-contact-tablets.png) |
| Contact Page | All fields need to be filled out in order to submit the contact form. | ![screenshot](documentation/features/website-contact-all-fields.png) |
| Contact Page | Upon submitting the correct contact information, the User receives a confirmation message that their contact request has been received and they will be contacted within 2 working days. | ![screenshot](documentation/features/website-contact-message.png) |
| Sign up Page | Authentication is handled by allauth, allowing users to register accounts. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/website-signup.png) |
| Sign up Page | The Sign up page is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-signup-mobile.png) |
| Sign up Page | The Sign up page is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-signup-tablets.png) |
| Sign in Page | Authentication is handled by allauth, allowing users to log in to their existing accounts. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/website-login.png) |
| Sign in Page | Authentication is handled by allauth, if username and/or password are incorrect, the user receives the message tha "The username and/or password you specified are not correct." | ![screenshot](documentation/features/website-login-incorrect-credentials.png) |
| Sign in Page | The Sign in page is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-signin-mobiles.png) |
| Sign in Page | The Sign in page is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-signin-tablets.png) |
| Logout Page | Authentication is handled by allauth, allowing users to log out of their accounts. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/website-logout.png) |
| Logout Page  | When the user logs out, they receive a goodbye message. | ![screenshot](documentation/features/website-logout-message.png) |
| Logout Page  | The Logout page is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-logout-mobiles.png) |
| Logout Page  | The Logout page is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-logout-tablets.png) |
| Bookings Page | On the booking page, users first encounter a form for creating new bookings, distinguished by a background image. Below this, they can find a list of all their bookings. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/website-bookings.png) |
| Bookings Page | Logged-in users can book a workshop level by specifying the number of participants (0-10), selecting a date, and choosing one of three available times. All fields are mandatory. | ![screenshot](documentation/features/website-create-booking.png) |
| Bookings Page | Upon submitting the correct booking information, the User receives a confirmation message of their booking, and the booking appears in the "My Bookings" section | ![screenshot](documentation/features/website-new-booking.png) |
| Bookings Page | "My Bookings" displays booking information in a table, allowing users to update or delete upcoming bookings. These buttons are visually distinct for easy recognition. Today's and past bookings are also visually distinct for easy identification but they cannot be updated or deleted. | ![screenshot](documentation/features/website-my-bookings.png) |
| Bookings Page | If user has not made abooking yet the "My Bookings" section shows a message "Time to book a workshop! See our availability above ✨" | ![screenshot](documentation/features/website-no-bookings.png) |
| Bookings Page  | The Bookings page is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-bookings-mobiles.png) |
| Bookings Page  | The Bookings page is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-bookings-tablets.png) |
| Update Bookings Page | Logged-in users can update their bookings via the "Update booking" button or return to their booking list using the "My Bookings" button. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/website-update-booking.png) |
| Update Bookings Page | Upon updating the booking, the User receives a confirmation message of their update booking, and the updated booking appears in the "My Bookings" section | ![screenshot](documentation/features/website-updated-booking.png) |
| Update Bookings Page   | The Update Bookings page  is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-update-booking-mobiles.png) |
| Update Bookings Page   | The Update Bookings page is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-update-booking-tablets.png) |
| Delete Bookings Page | Logged-in users can delete their bookings via the "Yes" button or return to their booking list using the "No" button. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/website-delete-booking.png) |
| Delete Bookings Page  | After deleting a booking, the user receives a confirmation message, and the deleted booking is removed from the "My Bookings" section. | ![screenshot](documentation/features/website-deleted-booking.png) |
| Delete Bookings Page   | The Delete Bookings page  is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/website-delete-booking-mobiles.png) |
| Delete Bookings Page   | The Delete Bookings page is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/website-delete-booking-tablets.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's feel but that it is yet distinctive, and it has a "Take me to Homepage" button. The screenshot ilustrates responsiveness in laptops and larger devices. | ![screenshot](documentation/features/404.png) |
| 404 | The 404 page  is also responsive for mobiles as demonstrated in this screenshot. | ![screenshot](documentation/features/404-mobiles.png) |
| 404 | The 404 page is also responsive for tablets as demonstrated in this screenshot. | ![screenshot](documentation/features/404-tablets.png) |
| Admin page | Site owners can create/publish the About content, including setting a profile image using Cloudinary, all from the Django admin dashboard. | ![screenshot](documentation/features/admin-create-about.png) |
| Admin page | Site owners can see contact requests, open them and mark them as read | ![screenshot](documentation/features/admin-contact-requests.png) |
| Admin page | Site owners have the ability to view, manage and set to public all workshops | ![screenshot](documentation/features/admin-workshops.png) |
| Admin page | Site owners can create, publish and manage workshop levels (beginner, intermediate, advanced) that users can then select when booking. | ![screenshot](documentation/features/admin-level.png) |
| Admin page | Site owners can can create, publish and manage the Workshops content, including setting a workshop image using Cloudinary, all from the Django admin dashboard. | ![screenshot](documentation/features/admin-workshop.png) |
| Admin page | Site owners have the ability to view and manage all user bookings. | ![screenshot](documentation/features/admin-bookings.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |


### Future Features

- **User Profiles**: Create personalized user profiles where authenticated users can view their bookings and account information.
- **Notifications**: Implement a notification system that alerts users when their booking appointment is soon coming.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for workshop updates, and booking confirmations.
- **Multilingual Support**: Add the ability to write and view the workshops in German and Spanish too, broadening the audience.
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

I have used [Smartdraw](https://www.smartdraw.com/) to draw the ERD of my project.

![screenshot](documentation/erd.png)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    ABOUT {
        int id PK
        string title
        string image
        text description
    }

    CONTACTREQUEST {
        int id PK
        string first_name
        string last_name
        string email
        text message
        boolean read
    }

    LEVEL {
        int id PK
        string name
    }

    WORKSHOP {
        int id PK
        string name
        text description
        text excerpt
        string image
        boolean is_public
        int level_id FK
    }

    BOOKING {
        int id PK
        datetime date_booked
        date appointment_date
        string appointment_time
        int participants
        boolean approved
        int booked_by_id FK
        int workshop_id FK
    }

    USER {
        int id PK
        string username
        string email
        string first_name
        string last_name
    }

    LEVEL ||--o{ WORKSHOP : has
    WORKSHOP ||--o{ BOOKING : "is booked in"
    USER ||--o{ BOOKING : "makes"
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVNtu4jAQ_RXLzxSVBEzIW8tmL6Jqulx2pVWkyCTTYJHYke10YSn_vg4ECKFVaZ6cOWfmnPGMvMGRiAG7GOQXRhNJs4Aj893d-7Mp2ux_yo9xjViMnkankNKS8QRpplO4iLKMJrWohpVGMahIslwzwffINqgOQ_9xejecjr2fM29ype4zk0qHnGaX4il9D4GMsrRhKwOlzszOhUiBciSBxg2jD94v7-E6fyf9Y_ZvfzyafPefPlvg_Rs8IrCKQOb6ozkcWmMqzIt5yqJzIym8QBoaO19HDev3vj_68fjtA-cx1aBZBrtDaMSWEJ-jiOa5MJkZcB2WgQvHdUJZ61wwp1KziOWUa3XZlsmV4qWuWebsfYTzdb2zA_hXyKVaiPzNrmcTb3zdsAoF8pqN-_TyNlbv9fXmRmxOm-SiBVWN7ao4h5G5KMBMVbdgWghwrbk3uBldgipJuIUzkMZ_bB6I3S0EWC_AOMMlL6ZyWdK2hkcLLSZrHmFXywJauMjL2VZPCnafaapM1EwNuxu8wu6g27ZtYvV6NiHdbqfvtPAau4S0HeIQYvct0h10bgfbFv4nhClw23Z6fTLo2lbfsTsWcaxdtT87cC8pRZEsjlKJLF1XCPAY5FAUXGO3Q3rb_6YteeU)


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/projects) served as an Agile tool for this project. Through it, User Stories, issues, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks.
The remaining five open issues are currently in the Backlog.

| Link | Screenshot | Notes |
| --- | --- | --- |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/ParedesGab/PP4-artistiClayers-workshops)](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) | The remaining five open issues are currently in the Backlog. |

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
| about | [about.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/templates/about/about.html) | [W3 about](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/validation/html-about-about.png) |
| workshop list | [workshop_list.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/workshop_list.html) | [W3 workshop list](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fworkshops%2F) | ![screenshot](documentation/validation/html-workshop-workshop-list.png) |
| workshop beginner | [workshop_detail.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/workshop_detail.html) | [W3 workshop beginner](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fworkshops%2Fworkshop%2F12%2F) | ![screenshot](documentation/validation/html-workshop-workshop-detail-beginner.png) |
| workshop intermediate | [workshop_detail.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/workshop_detail.html) | [W3 workshop intermediate](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fworkshops%2Fworkshop%2F15%2F) | ![screenshot](documentation/validation/html-workshop-workshop-detail-intermediate.png) |
| workshop advanced | [workshop_detail.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/templates/workshop/workshop_detail.html) | [W3 workshop advanced](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fworkshops%2Fworkshop%2F16%2F) | ![screenshot](documentation/validation/html-workshop-workshop-detail-advanced.png) |
| contact | [collaboration.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/templates/collaboration/collaboration.html) | [W3 contact](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/validation/html-contact.png) |
| sign in | [login.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/templates/account/login.html) | [W3 sign in](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/validation/html-login.png) |
| sign up (see section: [Known-issues](#known-issues)) | [signup.html](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/templates/account/signup.html) | [W3 sign up](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartisticlayers-d41862efab95.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/validation/html-register.png) |
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
| about | [tests_views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/test_views.py) | ![screenshot](documentation/validation/py-about-tests.png) |
| about | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/urls.py) | ![screenshot](documentation/validation/py-about-urls.png) |
| about | [views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/about/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/about/views.py) | ![screenshot](documentation/validation/py-about-views.png) |
| artisticlayers | [settings.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/artisticlayers/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/artisticlayers/settings.py) | ![screenshot](documentation/validation/py-artisticlayers-settings.png) |
| artisticlayers | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/artisticlayers/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/main/artisticlayers/urls.py) | ![screenshot](documentation/validation/py-artisticlayers-urls.png) |
| collaboration | [admin.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/collaboration/admin.py) | ![screenshot](documentation/validation/py-collaboration-admin.png) |
| collaboration | [models.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/collaboration/models.py) | ![screenshot](documentation/validation/py-collaboration-models.png) |
| collaboration | [forms.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/collaboration/forms.py) | ![screenshot](documentation/validation/py-collaboration-forms.png) |
| collaboration | [tests_forms.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/collaboration/test_forms.py) | ![screenshot](documentation/validation/py-collaboration-tests.png) |
| collaboration | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/collaboration/urls.py) | ![screenshot](documentation/validation/py-collaboration-urls.png) |
| collaboration | [views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/collaboration/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/collaboration/views.py) | ![screenshot](documentation/validation/py-collaboration-views.png) |
| home | [admin.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/admin.py) | N/A | N/A |
| home | [models.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/models.py) | N/A | N/A |
| home | [tests.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/tests.py) | | |
| home | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) |
| home | [views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) |
| workshop | [admin.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/admin.py) | ![screenshot](documentation/validation/py-workshop-admin.png) |
| workshop | [models.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/models.py) | ![screenshot](documentation/validation/py-workshop-models.png) |
| workshop | [forms.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/forms.py) | ![screenshot](documentation/validation/py-workshop-forms.png) |
| workshop | [test_forms.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/test_forms.py) | ![screenshot](documentation/validation/py-workshop-test-forms.png) |
| workshop | [test_views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/test_views.py) | ![screenshot](documentation/validation/py-workshop-test-views.png) |
| workshop | [urls.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/urls.py) | ![screenshot](documentation/validation/py-workshop-urls.png) |
| workshop | [views.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/workshop/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/workshop/views.py) | ![screenshot](documentation/validation/py-workshop-views.png) |
| | [manage.py](https://github.com/ParedesGab/PP4-artistiClayers-workshops/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ParedesGab/PP4-artistiClayers-workshops/refs/heads/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | Notes (if applicable) |


## Responsiveness

- The website was checked across devices using the chrome extension [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en).

- Responsiveness screenshot examples can be found in section [Existing-features](#existing-features)

- In addition, it was manually checked in the following devices:
  - Huawei Y9 Prime 2019
  - Iphone XR
  - Iphone 15 pro
  - Samsung Galaxy S8

## Browser Compatibility

The website was tested on the following browsers:

| Browser | Screenshot example |
| --- | --- |
| Google Chrome | All screenshots from section [Existing-features](#existing-features) | 
| Firefox | ![screenshot](documentation/browser-compatibility/firefox.png) | 
| Microsof Edge | ![screenshot](documentation/browser-compatibility/microsoft-edge.png) | 


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| About | ![screenshot](documentation/lighthouse/mobile-about.png) | ![screenshot](documentation/lighthouse/desktop-about.png) |
| Workshops (see section: [Known-issues](#known-issues)) | ![screenshot](documentation/lighthouse/mobile-workshops.png) | ![screenshot](documentation/lighthouse/desktop-workshops.png) |
| Workshop (see section: [Known-issues](#known-issues)) | ![screenshot](documentation/lighthouse/mobile-workshop.png) | ![screenshot](documentation/lighthouse/desktop-workshop.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| Booking | ![screenshot](documentation/lighthouse/mobile-booking.png) | ![screenshot](documentation/lighthouse/desktop-booking.png) |
| Update Booking | ![screenshot](documentation/lighthouse/mobile-update-booking.png) | ![screenshot](documentation/lighthouse/desktop-update-booking.png) |
| Delete Booking | ![screenshot](documentation/lighthouse/mobile-delete-booking.png) | ![screenshot](documentation/lighthouse/desktop-delete-booking.png) |
| Sign in | ![screenshot](documentation/lighthouse/mobile-signin.png) | ![screenshot](documentation/lighthouse/desktop-signin.png) |
| Sign up | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Log out| ![screenshot](documentation/lighthouse/mobile-logout.png) | ![screenshot](documentation/lighthouse/desktop-logout.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

| Page | Expectation | Test | Result | Passed |
| --- | --- | --- | --- | --- |
| About | The title of the About information should be a string with a maximum length. | Attempted to create/edit the About information with a title exceeding 200 characters | The form in the admin interface prevented saving, displaying a validation error for the title field | Yes |
| About | The image field should handle various image file types | Created/edited the About information by uploading different valid image file types (.webp .jpg, .png, etc.). | The image was uploaded successfully and displayed on the About page | Yes |
| About | TThe image field should handle the default placeholder. | Ensured no image was uploaded during creation/edit | The About page displayed the 'placeholder' image as defined in the model | Yes |
| About | The description field should handle various text inputs, including special characters and HTML (due to Summernote). | Created/edited the About information. | The description was saved and rendered correctly on the About page, preserving the special characters and HTML formatting | Yes |
| Contact | Administrators can accept or reject (Delete) a collaboration request. | As an admin, attempted to accept a pending collaboration request and then attempted to reject another pending collaboration request. | The Admin accepts or rejects a contact request | Yes |
| Contact | Administrators can makr collaboration requests as read or not read | Create a collaboration request | The Admin sees in the admin panel which collaboration requests have not been read and which have | Yes |
| Contact | Users should be able to submit the contact form only if all required fields are filled. | Attempted to submit the contact form leaving one or more required fields blank. | The form validation prevented submission and indicated which fields needed to be filled out still | Yes |
| Contact | Users should receive a clear notification upon successful submission of the contact form, indicating they will receive a response. | Successfully filled out all required fields in the contact form and submitted it. | Upon successful submission, the user was presented with a confirmation message | Yes |
| Contact | If a user makes an error during contact form submission, their already filled-out information in other valid fields should be preserved. | Filled out several fields in the contact form correctly, then intentionally made an error in one required field and attempted to submit. After the validation error, navigated back to the form. | The correctly filled-out values in the other fields of the contact form remained populated after the failed submission due to the validation error, preventing the user from having to re-enter all their information. | Yes |
| Bookings | All fields are required to create a booking | Attempted to submit a booking form empty fields | The form validation prevented this selection and indicated the empty field that was missing | Yes |
| Bookings | When creating a booking, the 'appointment_date' field should prevent users from selecting a date in the past | Attempted to submit a booking form with a date prior to the current date.| The form validation prevented this selection as it greys out all dates in the past | Yes |
| Bookings | When creating a booking, the 'appointment_date' field should prevent users from selecting the today's date | Attempted to submit a booking form with the today's date | The form validation prevented this selection as it greys out all same-day dates | Yes |
| Bookings | When creating a booking, the 'participants' field should only accept positive integers within the specified range (i.e, 1-10).| Attempted to submit a booking form with 0 participants and more than 10 participants| The form validation prevented these selections as the participants field can only take from 1 to 10 people | Yes |
| Bookings | Authenticated users should be associated only with their bookings and automatically. | Logged in as a user and submitted a booking form. | The new booking is displayed correctly| Yes |
| Bookings | Authenticated users should be associated with their bookings automatically. | Logged in as a user and submitted a booking form. | The new booking is displayed correctly and automatically | Yes |
| Bookings | If all fields are correctly selected clicking the "Book your Spot" button should create a booking | Clicking the "Book your Spot" button | A message appears indicating that the booking was successfuly created, and the newly created booking is now displayed in "My bookings"  | Yes |
| Bookings | clicking the "Book your Spot" button should create a booking | Clicking the "Book your Spot" button | A message appears indicating that the booking was successfuly created, and the newly created booking is now displayed in "My bookings"  | Yes |
| Bookings | Users can view all their bookings. Upcoming bookings allow updating or deletion, while same-day and past bookings are non-editable/deletable. | Attempted to update/delete a same-day booking and a past booking. | The application prevented modification/deletion of same-day and past bookings but allowed it for upcoming ones. | Yes |
| Bookings/id/update | Only the user who created a booking or the Admin should be allowed to edit it. | Logged in as one user, created a booking. Then logged in as a different user and attempted to access the edit URL for the first user's booking. | The system identified the second user as someone other than the booking owner. Consequently, they were sent back to their personal list of bookings and received the message: "You do not have permission to edit this booking" | Yes |
| Bookings/id/update | When trying to update a booking, the 'appointment_date' field should prevent users from selecting a date in the past. | Attempted to submit a booking form with a date prior to the current date.| The form validation prevented this selection as it greys out all dates in the past | Yes |
| Bookings/id/update | When trying to update a booking, the 'appointment_date' field should prevent users from selecting the today's date | Attempted to submit a booking form with the today's date | The form validation prevented this selection as it greys out all same-day dates | Yes |
| Bookings/id/update | When trying to update a booking, the 'participants' field should only accept positive integers within the specified range (i.e, 1-10).| Attempted to submit a booking form with 0 participants and more than 10 participants| The form validation prevented these selections as the participants field can only take from 1 to 10 people | Yes |
| Bookings/id/update | When trying to update a booking, clicking the "Update Booking" button should update teh booking correctly | Clicking the "Update Booking" button | A message appeares indicating that the the booking was successfuly updated , and the updated booking is now displayed in "My bookings"  | Yes |
| Bookings/id/update | If a booking update is not desired clicking the "My Bookings" button should redirect the user to the 'Bookings' page | Clicking the "My Bookings" button | User is redirected to 'Bookings' page  | Yes |
| Bookings/id/delete | Before user deletes a booking a clear question confirming whether they want to delete it or not should be presented | User clicked the "Delete Booking" button | Before deleting the booking, the user is presented with the question prompting them to confirm if they want to proceed or not with the deletion.  | Yes |
| Bookings/id/delete | Only the user who created a booking or the Admin should be allowed to delete a booking | Logged in as one user, created a booking. Then logged in as a different user and attempted to access the delete URL for the first user's booking. | The system identified the second user as someone other than the booking owner. Consequently, they were sent back to their personal list of bookings and received the message: "You do not have permission to edit this booking"   | Yes |
| Bookings/id/delete | When trying to delete a booking, clicking the "Yes" button should update erase it correctly | Clicking the "Yes" button | A message appeares indicating that the the booking was deleted, and the deleted booking is no longer displayed in "My bookings"  | Yes |
| Bookings/id/delete | When trying to delete a booking, clicking the "No" button should prevent the booking from being deleted, and redirect the user to the 'Bookings' page | Clicking the "No" button | User is redirected to the 'Bookings' page and the booking is still displayed in "My bookings"  | Yes |
| Workshops | Administrators can create, delete, or update a workshop. | As an admin, attempted to create a new workshop, delete an existing workshop, and update the details of a workshop. | The admin interface allowed creating, deleting, updateing a workshop, when trying to delete a dialog equiring explicit confirmation to proceed is presented.  | Yes |
| Sign in | Feature is expected to allow registered users to log in to the site. | Attempted to log in with valid and invalid credentials. | Login was successful with valid credentials; invalid credentials were rejected. | Yes |
| Sign up | Feature is expected to allow users to register for an account. | Registered a new user with unique credentials. | User account was created successfully. | Yes |
| Log out | Feature is expected to allow users to log out securely. | Logged out and tried accessing a restricted page. | Access was denied after logout, as expected. | Yes |
| | Feature is expected to block standard users from brute-forcing admin pages. | Attempted to navigate to admin-only pages by manipulating the URL (e.g., `/admin`). | Access was blocked, and a message was displayed showing denied access. | Yes |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | Yes |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a User | I would like to regardless of the page I am in, I can click on the ArtistiClayers logo | so that I am taken back to the Home page. | ![screenshot](documentation/features/website-logo.png) |
| As a User | I would like to easily locate the navbar across all website pages | so that I can efficiently access different sections of the website. | ![screenshot](documentation/features/website-navigation-bar.png) |
| As a User | I would like to easily recognized which navbar link I clicked | so that I can efficiently see in which section of the website I am. | ![screenshot](documentation/features/website-navigation-bar.png) |
| As a User | I would like to have a footer across all website pages | so that I can  see the different social media links that ArtistiClayers have. | ![screenshot](documentation/features/website-footer.png) |
| As a User | I would like to click on the social media links| so that I can  efficiently access different social media links to connect and engage with ArtistiClayers social platforms. | ![screenshot](documentation/features/website-footer.png) |
| As a User | I would like to find an intuitive, welcoming and enjoyable Home page | so that I can easily understand the purpose of the website and want to remain on it and explore further. | ![screenshot](documentation/features/website-homepage.png) |
| As a User | I would like to be drawn to click the button "Our Workshops" in the home page | so that I can easily have access to the list of workshops. | ![screenshot](documentation/features/website-homepage.png) |
| As a User | I would like to find an intuitive and user-friendly About page | so that I learn about the workshop's tutor experience and further understand the concept of ArtistiClayers. | ![screenshot](documentation/features/website-about.png) |
| As a User | I would like to see the available workshops | so that I can gather detailed information and choose the best fit for my learning needs. | ![screenshot](documentation/features/website-workshops-tablets.png) |
| As a User | I would like to be able to click each workshop card | so that I can be directed to a more detailed page of each workshop (example of one workshop in the screenshot)| ![screenshot](documentation/features/website-workshop-beginner.png) |
| As a Logged in User | I would like to see and click a button to book a workshop | so that I can book my desired workshop. | ![screenshot](documentation/features/website-workshop-beginner-loggedin.png) |
| As a Non-logged in User | I would like to see and click a button stating that to book a workshop Log in and/or Register is first required | so that I am aware I need to log in or register to book a workshop.| ![screenshot](documentation/features/website-workshop-beginner.png) |
| As a User | I would like to be able to submit a contact form | so that I can request a collaboration with the site owner or ask questions I might have. | ![screenshot](documentation/features/website-contact.png) |
| As a User | I would like to receive a notification or message saying my contact request is pending approval | so that I understand it hasn't been read immediately. | ![screenshot](documentation/features/website-contact-message.png) |
| As a Site Admin | I would like to accept or reject contact/collaboration requests | so that I can manage collaboration requests | ![screenshot](documentation/features/admin-contact-requests.png) |
| As a Site Admin | I would like to access the Admin panel | so that I can manage bookings, collaboration requests, user accounts and the about me page (example of the bookings administration in the screenshot) | ![screenshot](documentation/features/admin-bookings.png) |
| As a Site Admin | I would like to access the workshops content in the Admin panel | so that I can manage them and display them with the desired content in the website. | ![screenshot](documentation/features/admin-workshop.png) |
| As a User | I would like to register an account | so that I log in to my private account and manage my bookings or book a desired workshop | ![screenshot](documentation/features/website-signup.png) |
| As a User | I would like to Sign in to my account | so that I log in to my private account and manage my bookings or book a desired workshop | ![screenshot](documentation/features/website-login.png) |
| As a Logged in User | I would like to create a booking | so that  I can participate to one of the workshops. | ![screenshot](documentation/features/website-create-booking.png) |
| As a Logged in User | I would like to be able to choose for my booking: one of the available workshop levels, choose the number of people participating (min 0, max 10), and choose the appointment date and appointment time | so that I can participate to one of the workshops with my desired selection. | ![screenshot](documentation/features/website-create-booking.png) |
| As a Logged in User | I would like to receive clear and specific error messages if I make a mistake in any of the booking fields | so that I can easily identify and correct the errors to successfully complete my booking. | ![screenshot](documentation/features/website-booking-error.png) |
| As a Logged in User | I would like to book from only three pre selected time slots | so that scheduling is simplified with a few clear choices. | ![screenshot](documentation/features/website-booking-times.png) |
| As a Logged in User | I would like to see a "Thank you for you booking" message displayed | so that I know that my booking was successfully created. | ![screenshot](documentation/features/website-navigation-bar.png) |
| As a Logged in User | I would like to see all bookings I created | so that I can visualize them and update them or delete them if desired. | ![screenshot](documentation/features/website-bookings.png) |
| As a Logged in User | I would like to distinguish the update from the delete button, and the past from the "today" bookings | so that I can visualize them and, if possible, update them or delete them if desired. | ![screenshot](documentation/features/website-bookings.png) |
| As a Site owner | I would like the booking system to prevent users from selecting appointment dates that are in the past or the current day | so that booking errors are avoided and the workshop tutor has adequate preparation time based on the number of attendees. | ![screenshot](documentation/features/website-past-bookings-not-allowed.png) |
| As a Site owner | I would like to not allow updates or deletions of past bookings (workshops that already took place) | so that I can maintain control over the past bookings. | ![screenshot](documentation/features/website-my-bookings.png)  |
| As a Site owner | I would like to not allow updates or deletions of bookings made for the current day | so that the Tutor receives timely notification of any changes with adequate advance notice. | ![screenshot](documentation/features/website-my-bookings.png) |
| As a Site owner | I would like the booking system to prevent users from selecting either 0 or more than 10 participants for workshop | so that adequate materials and proper attention can be provided to each attendee. | ![screenshot](documentation/features/website-from1-10-participants.png) |
| As a Logged in User | I would like to log out | so that my account is secured from unauthorized use. | ![screenshot](documentation/features/website-logout.png) |
| As a Logged in User | I would like to, before logging out, be presented with a confirmation message to ensure I wish to end my session | so that I can reconsider whether it was accidental or my intended action was to log out. | ![screenshot](documentation/features/website-logout.png) |
| As a Logged out User | I would like to see a confirmation message that I logged out, and be redirected to the Home page | so that I know the log out was succesful and that I am not redirected to an unkown website. | ![screenshot](documentation/features/website-logout-message.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. |![screenshot](documentation/features/404.png)  |


## Automated Testing

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

Below are the results from the full coverage report on my application that I've tested:

- Automated testing was implemented for:
    - Collaboration app (form) | ![screenshot](documentation/automation/testing-collaboration-form.png)
    - Woskshop app (views and booking form) | ![screenshot](documentation/automation/testing-workshop-forms-and-views.png)
    - About app (views) | ![screenshot](documentation/automation//testing-about-views.png)


#### Unit Test Issues

## Bugs

### Fixed Bugs

1. FieldError in the  Django admin interface:
  ![bug fielderror](documentation/bugs/admin-error-1.png)
  ![bug fielderror ](documentation/bugs/admin-error-2.png)
        - Solution: To search within fields of related models I needed to use the double underscore (__) notation. This error was spotted and corrected.

2. TypeError in the Django admin interface for the model Workshop:
  ![bug typerror](documentation/bugs/type_error1.png)
  ![bug typerror](documentation/bugs/type_error2.png)
        - Solution:  The __str__ method expected an string but I was returning an integer (self_level_id). The error was corrected by using self.name instead.

3. In the workshop_list template, I used an ID attribute within a for loop.
This resulted in the same ID being assigned to multiple elements, violating the HTML requirement for unique IDs and causing an error reported by the W3C HTML validator.
  ![bug duplicated id](documentation/bugs/duplicated-id.png)
        - Solution: This was spotted and the id was erased.

4. When performing the Automated testings, I got the error that the cloud_name of cloudinary was missing.
![Bug cloudinary ](documentation/bugs/bug-cloudinary.png)
    - Solution: Code institute Tutor support could not pinpoint amy errors to my cloudinary settings, and mentioned that "the CLOUDINARY_URL is printed when running the tests, the models, views, templates and tests are all set up as in the walkthrough, the package versions are also the same". However, this error disappeared when I added my cloud_name to settings.py.

5. The lighthouse report threw the error of "Does not use HTTPs":
![Bug lighthouse](documentation/bugs/bug-lighthouse-about.png)
    - Solution: This was corrected by adding in settings.py -> cloudinary.config(secure=True)

### Unfixed Bugs

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

### Known Issues


- On devices smaller than 375px, the page starts to have horizontal `overflow-x` scrolling. 
- When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. 
- Validation errors on "signup.html" coming from the Django Allauth package. 
- Lighthouse reported as an error "Uses third-party cookies" but these are new Chrome policies and cannot be removed that at the moment 


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


#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/ParedesGab/PP4-artistiClayers-workshops).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

- [The Code institute ci-full-template](https://github.com/Code-Institute-Org/ci-full-template) was used to create the GitHub repository of the ArtistiClayers Workshops.

- [Markdown Builder](https://markdown.2bn.dev) helped generating Markdown files.

- [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project was used as guidance and inspiration.

- [Bootstrap](https://getbootstrap.com) was used for responsive front-end framework.

- [Cloudinary API](https://cloudinary.com) was used as Cloud storage for static/media files.

- [Whitenoise](https://whitenoise.readthedocs.io) was used as the static file service.

- [ChatGPT](https://chatgpt.com) helped with code logic and explanations.

- [CSS-Tricks](https://css-tricks.com/a-complete-guide-to-calc-in-css/) showed me how to use the CSS calc function.

- [W3 Schools](https://www.w3schools.com/css/css3_mediaqueries_ex.asp) showed me the concept of max-width media queries.

- The base.html code from [I Think Therefore I Blog](https://codeinstitute.net) was used as template for my base.html.

- Despite significant customization, the HTML structure for update, delete and the bookings display derived from the html structure of the project [DjangoDogGroomers](https://github.com/petermcloughlin/DjangoDogGroomers) from Peter Mcloughlin.

- Stack Overflow solutions was also used to resolve doubts.

- Website text was checked with DeepL Write for spelling mistakes. 


### Media

- Images

| Source | Notes |
| --- | --- |
| Website images | All website images belong to the developer Gabriela F. Paredes Rojas |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

- My sincere gratitude to my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for all his support throughout the development of this project.
- I would like to thank my cohort [Kristyna Wach](https://github.com/Cushione) for the great tips, feedback and always positive energy.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- A heartfelt thank you to my husband Johannes for keeping me fueled with snacks and coffee during long work sessions.

