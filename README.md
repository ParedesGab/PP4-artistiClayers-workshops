# ArtistiClayers Workshops

(Developer: Gabriela Fabiola Paredes Rojas)

![Responsive Mockup image](documentation/website-screenshots/responsive-mockup.png)

**Welcome to the ArtistiClayers Polymer Clay Workshops!**


+ The site can be accessed via this [link](https://paredesgab.github.io/PP2-the-cosmic-match-memory-game/)

---
## Project Goals

### User Goals

+ Find a casual and fun activity to pass time or to relax.
+ Test memory skills with an enjoyable memory game. 
+ Enhance memory, concentration, and problem-solving skills.
+ Find a simple, accessible game that doesn't require downloads or setup.
+ Find a vibrant, eye-catching game that provides a visually engaging experience.

### Site Owner Goals

  + Provide a fun, relaxed and engaging User experience.
  + Create an entertaining memory game that appeals to a broad audience.
  + Create a game that helps users improve memory, focus, and cognitive abilities. 
  + Develop a unique design and thematic experience, such as the galaxy theme, to stand out from generic memory games.
  
---
## User Experience

### Target audience

+ Space enthusiasts, kids or adults.
+ Parents looking for educational and fun games for their children.
+ Children interested in games and space and galaxy themes. 
+ Students or educators that seek tools to improve cognitive abilities.
+ Casual gamers, casual web users or individuals looking for light, engaging games to pass the time.

### User expectations

+ Accessible site.
+ Understand clearly the purpose of the site.
+ Quick and easy access to content and navigation.
+ Clean and intuitive layout, overall a smooth experience.
+ Have vibrant and eye-catching content that keeps the user engaged.
+ Expect the game to work seamlessly on various devices, allowing them to enjoy it anytime, anywhere.

### User stories

+ **As a first-time user, I want to:**

  + Quickly understand how the game works.
  + Dive into the game without confusion.
  + Have a smooth, enjoyable experience without delays or glitches.
  + Easily navigate the website and find the content interesting.
  + Be drawn into the game's theme by having an engaging and visually appealing experience.
  + Know how many movements I am doing during and a summary after the game.

+ **As a returning user, I want to:**

  + See if my cognitive skills have improved by comparing the movements I made in one game versus another.
  + See a more dynamic galaxy-themed background to make the page more immersive.
  + Check if new space card-theme designs are being featured.

+ **As the site ownser, I want:**

  + To keep the users engaged and the website updated with newer themes.
  + Deliver a smooth, accessible experience.
  + Relaxed, stress-free experience: Without a timer and the possibility of losing, players can enjoy the game at their own pace, exploring and improving their memory without feeling rushed or pressured.
  + Positive reinforcement and engagement: The "no-loss" design encourages players to keep playing and improving, offering a rewarding, fun experience where they can focus on achieving personal milestones and celebrating small victories.

---
## Features 

### Game Header

![Game Header up to Tablets](documentation/website-screenshots/game-name.png)

+ It contains two titles (h1 and h2) positioned at the center of the page, and they are the first elements found across all pages.
    + Clear and easy to read.
    + It uses a futuristic Google font "Rajdhanithat" and a background style that conveys and embraces the cosmic-theme.
  
+ Therefore, the user understands directly that theme of the memory game is related to galaxy, space, universe.

+ The header position and font-size are responsive across all devices. For example, it increases in size in larger screens (**Figure below**). However, it is made smaller in all the other pages.

![Game Header Laptops and up](documentation/website-screenshots/game-name-laptops-up.png)
       
---
### Home Menu Page

![Home menu main page](documentation/website-screenshots/home-menu-main-page.png)

+ The main page of the Galaxy Memory Game, consists of the game heading and the home menu buttons. 

+ The intention was to have a simple yet impactful background that would immediately introduce the galactic theme of the Memory Game.

+ This same background is used across all pages and it allows the title and buttons to stand out.

**Home Menu Buttons**

![Home menu buttons](documentation/website-screenshots/home-menu-buttons.png)

+ The home menu buttons are present on the main page of Memory Game, and they consist on two buttons: Play Game, and Play instructions. 
  
+ They are responsive, and across all devices the home menu buttons are found positioned on top of the other (flex-direction: column).

+ The buttons will rotate slightly and change colors when hovered, creating a smooth, visually appealing interactive effect.

+ Clear and easy to read.

+ Consistent styling and easy navigation.

---
### Game Indications Page

- The user is redirected to this page when clicking to the "Play Instructions" button from the Home Menu page.

- This section provides the user with an introductory explanation of the game, shows visual representations of the game cards, and gives them an option to return to the main menu.

- This section is responsive and the images use the flex-wrap property. 

Design for mobiles:

![Game indications mobiles](documentation/website-screenshots/game-indications-mobile.png)

Design for Tablets and larger devices:

![Game indications tablets and up](documentation/website-screenshots/game-indications-tablets-up.png)

---
### Memory Board Game Page

![Memory board game card deck open](documentation/website-screenshots/memory-game-open.png)

It contains two subsections, from top to bottom:

**Subsection: Game Board**

- This section presents the memory game itself: a relaxing and fun memory-matching game designed with a space-related theme.

- Players are challenged to match 8 pairs of cards, with a total of 16 cards in the game.

- The card deck array is created by Javascript within the Game Board section. 

 - The game offers a no-pressure environment where players never lose, ensuring a calm and enjoyable experience.

 - When the game starts (or if it is restarted) the cards will be shuffled and placed face down (**Figure below**), and they have the same hover effect as the home menu buttons. 

![Memory board game card deck closed](documentation/website-screenshots/memory-game-closed.png)

**Subsection: Control Area**
 
 - This subsection displays the "Moves", "Score" and one button, the "Restart Game".

 - These elements are placed on top of the other. 

 - The Restart Game button has the same hover effects as the home menu buttons, and to encourage the user to restart the game as much as they want, the button stands out in orange. 

 - At the beginning of the game:
    - The **Moves** are set to 0, and every time the user chooses two cards, the "moves" will increase by 1.
    - The **Score** is set to 0, and every time there is a match, the player earns 100 points. When the user reaches 800 (i.e., all pairs are matched), the score will show 🎉 800! 🎉.

- The Memory Board Game page is responsive. Namely:

  -   The card grid maintains 4 columns and 4 rows across all devices, with the width and height of the cards increasing on larger screens.

  - In tablets and larger screens, the memory card deck and control are placed next to each other (flex-direction: row).

  - In mobiles: the Control Area is placed below the memory card deck. This was achieved because their container (id memory-game-container) was set to display property: flex, and flex-direction: column 

![memory board game mobiles](documentation/website-screenshots/memory-game-mobiles.png)

---
### Game Finished - Congratulations Page

![congratulations page](documentation/website-screenshots/congratulations-message.png)

- After 4 seconds, once the user has matched all the cards (score: 🎉 800! 🎉), they are redirected to a page that congratulates them on their victory.

- The congratulations message also stands out in orange.

- In addition, it displays in bold the amount of moves the user made.

- This section contains two buttons:
  - **Home Menu:** Directs you back to to the Home Menu page.
  - **Play again!:** Starts a new game. 

- The buttons use the same style as the home menu buttons. 

- With Javascript, the class smaller-name was added to the header (i.e., game name), to make the whole page more visually organized. 

---
## Features left to implement

- Implement a more dynamic galaxy-themed background (e.g., moving nebulas).

- Add a space-themed sound effect by implementing an event listener in JavaScript that triggers whenever a match occurs.

- Add animations for card flips and matches to enhance the user experience.

- Implement visual feedback (e.g., a highlight) for matched pairs.
- Allow users to navigate back to the home page directly from the memory game. Please note that for now this option was intentionally excluded to encourage players to stay on the game page longer, with the added flexibility to restart the game if they wish.

- I intentionally left out a timer to keep the game relaxed and pressure-free. However, if feedback suggests it, I’d be happy to implement it with JavaScript.

- Due to time constraints, I used onclick in all buttons of the HTML document for faster implementation. However, I recognize that mixing structure (HTML) with functionality (JS) is not best practice, as it can make the code harder to maintain and does not facilitate collaboration in team environments. After the project is graded, I plan to refactor the code by removing inline onclick attributes, and instead handling events via JavaScript by adding event listeners, ensuring better separation of concerns and improving maintainability.

---
## Design

### Color scheme

**Main color scheme**

![Main Color scheme](documentation/design/main-color-scheme.png)

- The russian violet (blue), seasalt (white) and davy's gray color where used as the main colors of the website. Their choice was inspired by the universe background image and their used keeps the website cohesive.

- The russian violet (blue) was used for the titles, button names and the paragraph within the Game indications section.

- All buttons except for the button with class btn--restart, used as box shadow the color davy's gray color. 

**Secondary color scheme**

![Secondary Color scheme](documentation/design/secondary-color-scheme.png)

- To simulate colors of the universe the hover effect used two colors as gradient: Royal purple ( #7943af) and Sapphire ( #3455af). 

- The button with the class btn--restart and the congratulatory message are styled in Sinopia orange to ensure that they stand out. This vibrant choice draws attention to the restart option, making it easy for users to replay the game, and highlights the victory message effectively, celebrating the user's success in a visually striking way.

### Typography

- "Rajdhani" and "Roboto" from Google Fonts were used as the primary and secondary font of the website, respectively. 
- The generic family name is "Sans-serif".
- For the titles (h1 and h2) letter-spacing CSS property with a value of 0.3rem was used, to add a slight space between letters in the text.

![Primary Font](documentation/design/primary-font.png)
![Secondary Font](documentation/design/secondary-font.png)

---
## Wireframes

#### Mobile

- [Mobile: Home menu page](documentation/wireframes/main-page-mobile.png)
- [Mobile: Games indications page](documentation/wireframes/game-instructions-mobile.png)
- [Mobile: Memory board game page](documentation/wireframes/memory-board-game-mobile.png)
- [Mobile: Congratulations page](documentation/wireframes/congratulations-mobile.png)

#### Tablets

- [Tablet: Home menu page](documentation/wireframes/main-page-tablet.png)
- [Tablet: Games indications page](documentation/wireframes/game-instructions-tablet.png)
- [Tablet: Memory board game page](documentation/wireframes/memory-board-game-tablet.png)
- [Tablet: Congratulations page](documentation/wireframes/congratulations-tablet.png)

#### Laptops/Desktop

- [Laptops: Home menu page](documentation/wireframes/main-page-laptops-up.png)
- [Laptops: Games indications page](documentation/wireframes/game-instructions-laptops-up.png)
- [Laptops: Memory board game page](documentation/wireframes/memory-board-game-laptops-up.png)
- [Laptops: Congratulations page](documentation/wireframes/congratulations-laptops-up.png)

---
## Technologies used
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Gitpod](https://www.gitpod.io/): the development environment to create the project files, folders and html, css and javascript codes.
- [GitHub](https://github.com/): to store the repository, bug track and see the deployed version.
- [Balsamiq](https://balsamiq.com/): to create the wireframes.
- [Google Fonts](https://fonts.google.com/): to import the Rajdhani and Roboto family fonts.
- [TinyPNG](https://tinypng.com/): to compress the images.
- [Flaticon](https://www.flaticon.com/): source of the memory card images.
- [Favicon.io](https://favicon.io/): source of the favicon images.
- [Am I responsive?](https://ui.dev/amiresponsive): to generate the responsive mockup image.
- [MDN Web Docs](https://developer.mozilla.org/en-US/): resource to check CSS properties and javascript syntax and definition descriptions.
- [Color-hex](https://www.color-hex.com/): to get the rgb color information.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools?hl=de) and its open source [Lighthouse](https://developer.chrome.com/docs/lighthouse?hl=de).
-  [W3C HTML](https://validator.w3.org/) and [W3C CSS](https://jigsaw.w3.org/css-validator/) Validation Services. 
- [JSHint](https://jshint.com/): to detect errors and potential problems in the JavaScript code.
- [WAVE](https://wave.webaim.org/): to test accessibility.
- [DeepL Write](https://www.deepl.com/en/write): to spot spelling mistakes in the text. 

---
## Testing

### Validation
- In this section, the HTML and CSS codes were checked for compliance with industry standards. This was done using the W3C Markup Validation Service for HTML and CSS respectively, using the code from both: the working environment and the the deployed version.

- The result in both reports: no errors were returned.

#### HTML Validation

![HTML Validation](documentation/validation/html-file-validator.png)

#### CSS Validator

![CSS Validation](documentation/validation/css-stylesheet-css-validator.png)

#### JSHint

![JS validation](documentation/validation/javascript-jshint-validation.png)

+ There were no errors found in the javascript code using the JS Hint Validator. 
+ There was one warning and a message of unused variables. This is documented in the "Bugs" section below.

### Accessibility 

Accessibility was tested using the Web Accessibility Evaluation Tool (WAVE report below), and no errors were reported. 

![WAVE report](documentation/wave/wave-report.png)

### LightHouse report

Lighthouse tool from Devtools was used to confirm that the website is performing well, is accessible and the colors and fonts chosen are readable.

![LightHouse report Home menu page](documentation/lighthouse/lighthouse-report-homepage.png.png)

### Responsiveness

- The website was checked across devices using the chrome extension [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en). 

- In addition, it was manually checked in the following devices:
  - Huawei Y9 Prime 2019
  - Iphone XR
  - Iphone 15 pro
  - Samsung Galaxy S8

### Manual Testing

| Feature | Action | Expected result | Tested | Passed | Observations |
| --- | --- | --- | --- | --- | --- |
| **Home Menu Page** | | | | | |
| Header | Game name display | The title is centered and positioned as the topmost element on the page and it is readable | Yes | Yes | - |- |
| Play Game! button | Click on the Play Game! button | Redirects to the Memory Board Game page | Yes | Yes | - |
| Play Instructions button | Click on the Play Instructions button | Redirects to the Game Indications page | Yes | Yes | - |
| Both Home menu buttons | Hover over them | The buttons will rotate slightly and change colors to a gradient of blue and purple | Yes | Yes | 
| Both Home menu buttons | Buttons displayed | The buttons are centered one of top of the other with a consisting style, and they are readable | Yes | Yes | 
| **Game Indications Page** | | | | | |
| Header | Game name display | The title is centered and positioned as the topmost element on the page and it is readable | Yes | Yes | - |- |
| Game indications text | Text display| The paragraph stands out, the content is justified with no spelling mistakes | Yes | Yes | - |
| Images | Images display | The images are loading correctly, they have the same style and dimensions, and are located  below the text| Yes | Yes | - |
| Home Menu button | Click on the Home Menu button | Redirects to the Home Menu page | Yes | Yes | - |
| **Memory Board Game Page** | | | | | |
| Header | Game name display | The title is centered and positioned as the topmost element on the page and it is readable | Yes | Yes | - |- |
| Game Board | Game board display | It stands out and it is centered | Yes | Yes | - |
| Memory cards | Cards display | They have identical dimensions and are arranged in a grid layout. Initially, they appear "closed" with a white background. A hover effect is applied, and the cursor changes to indicate that they are clickable.| Yes | Yes | - |
| Game logic | Game logic | The images are revealed only when clicked. Once a card is clicked, it becomes disabled and cannot be clicked again. After the user clicks two cards, they are re-enabled for further interactions. Each time the user clicks two cards, the "moves" count increases by 1. However, the "score" only increases by 100 when a match is made. The player wins once their score reaches 800 | Yes | Yes | - |
| Restart Game button | Restarts the game | It restarst the game at any time | Yes | Yes | - |
| Restart Game button | Hover over them | The button will rotate slightly and change colors to a gradient of blue and purple | Yes | Yes | - |
| **Game Finished Congratulations Page** | | | | | |
| Header | Game name display | The title is centered and positioned as the topmost element on the page and it is readable | Yes | Yes | - |- |
| Game Finished - Congratulations Page | Page displays | This page appears 4s after the player has won | Yes | Yes | - |
| Congratulations text | Text display | The paragraph stands out, the content is centered with no spelling mistakes | Yes | Yes | - |
| Home Menu button | Click on the Home Menu button | edirects to the Home Menu page | Yes | Yes | - |
| Play Again! button | Click on the Play Again! button | Redirects to the Memory Board Game page | Yes | Yes | - |
| Both buttons | Hover over them | The buttons will rotate slightly and change colors to a gradient of blue and purple | Yes | Yes | 
| Both buttons | Buttons displayed | The buttons are centered one of top of the other with a consisting style, and they are readable | Yes | Yes | 

---
## Browser compatibility

The website was tested on the following browsers:
- Google Chrome
- Firefox
- Microsof Edge

---
## Bugs
+ ### Solved bugs
  1. The W3C Markup validation detected the below error in the HTML code:
  ![bug HTML code](documentation/bugs/bug-error-html-code.png)
        - Solution: this mistake was spotted and corrected. 

  2. The W3C Markup validation detected the below warnings in the HTML code:
    ![warnings HTML code](documentation/bugs/bug-warnings-html-code.png)
      - Solution: To enhance the HTML syntax, a hidden H2 heading was added to each section without an existing heading.

  3. JSHint showed the following warning:
    ![warnings JS code](documentation/bugs/bug-warning1-jshint.png)
      - Solution: Although the original code was functioning correctly, the event listener logic was updated to avoid any potentially confusing semantics. A separate click handler function was created. This change ensures the correct card index is captured using a closure for the handleCardFlip function.

+ ### Unfixed bugs

  1. JSHint showed the following warning:

    ![warnings JS code](documentation/bugs/bug-warning2-jshint.png)
    
    - As described in the "Features left to implement" section, due to time constraints, I used onclick in all buttons of the HTML document for faster implementation. However, I recognize that mixing structure (HTML) with functionality (JS) is not best practice, as it can make the code harder to maintain and does not facilitate collaboration in team environments. After the project is graded, I plan to refactor the code by removing inline onclick attributes, and instead handling events via JavaScript by adding event listeners, ensuring better separation of concerns and improving maintainability.
  
---
## Deployment

The website has been deployed to GitHub pages following these steps:

1. In the GitHub repository for The Cosmic Match Memory Game [GitHub repository](https://github.com/ParedesGab/PP2-the-cosmic-match-memory-game), select the "Settings" tab.

2. Click on "Pages" from the field "Code and automation" (on the left), and select the below settings:
    - Source: deploy from a branch.
    - Branch: main.
    - click "Save".

3. Select the "Code" tab and refresh the page. 

4. On the right side of the page, a "Deployments" section has been activated indicating a successful deployment. 

5. The live link can be accessed [here](https://paredesgab.github.io/PP2-the-cosmic-match-memory-game/).

## Local Deployment

### Forking

To have a copy of the project in your repositories:
1. Log in or sign up to GitHub.
3. Navigate to the [project repository](https://github.com/ParedesGab/PP2-the-cosmic-match-memory-game).
4. In the top right corner, click the "Fork" button.
5. A new page titled "Create a new fork" will appear. Optionally, you can edit the repository name.
6. At the bottom of the page, click "Create fork."

### Cloning

1. Log in or sign up to GitHub.
2. Go to the [project repository](https://github.com/ParedesGab/PP2-the-cosmic-match-memory-game).
3. Click the green button "Code" and choose your preferred cloning method (for example: HTTPS, SSH, or GitHub CLI) and copy the provided url.
4. Open the terminal in your preferred code editor and change the current working directory to the one where you want the cloned directory
5. Run git clone in the terminal, paste the copied link, and press Enter.

---
## Credits 

### Content 

- The Code institute ci-full-template was used to create the GitHub repository of the Cosmic Match Memory Game website.

- [W3 Schools](https://www.w3schools.com/jsref/met_win_settimeout.asp) showed me how to use the setTimeout() method. 

- [W3 Schools](https://www.w3schools.com/jsref/prop_html_id.asp) showed me how to return the id property. 

- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius) showed me how to create elliptical corner radius used in the Control Area of the Memory Board Game section.

- I got further clarificaion on the used of Parameters vs Arguments from the from the YouTube channel [Anna McDougall](https://www.youtube.com/watch?v=5o4P8lESTF0).

- Stack Overflow solutions was also used to resolve doubts.

- Text was checked with DeepL Write for spelling mistakes. 

- I learned how to add other pages (e.g., home menu page, games indications and congratulations pages) with Javascript by reading the project of [Kristyna Wach](https://github.com/Cushione/four-seasons-memory-game) and testing it myself within my javascript code.

- Inspiration for memory game logic comes from the YouTube Channels [developedbyed](https://www.youtube.com/watch?v=-tlb4tv4mC4&t=3095s) and [Victor Talamantes](https://www.youtube.com/watch?v=c0eigGnotm0). However, I did  not relied on them and customized it my way.

- ReadMe was inspired and guided by the ReadMe documents of my mentor Iuliia Konovalova, of my previous Kamil Wojciechowski, and of the love running project. 

### Media
  
- The universe background image is from [Federico Beccari](https://unsplash.com/de/@federize?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

- All memory card images are from [Icongeek26](https://www.flaticon.com/authors/icongeek26).

## Acknowledgments

- My sincere gratitude to my mentor, Iuliia Konovalova, for her valuable feedback.  
- Thank you to Code Institute, specially to Kamil, Kristyna, and Lane for the great tips and feedback.
- Thank you to my brother Brando, Your beautiful piano music [Brando PR](https://www.youtube.com/@BrandoPR) accompanied me along this project as well.
- I am deeply grateful to Geddi and Alexis for their insightful JavaScript fundamentals guidance.
- A heartfelt thanks to my husband Johannes for "playing! (testing)
 the game more times than I can count. 