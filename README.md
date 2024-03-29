# Hangman

### Welcome to Hangman, a simple childhood classic. The user must guess the correct letters from a random word, one letter at a time. Each incorrect guess builds a stage of the hangman. If the entire hangman is completed before you guess the word it's game over! So choose your letters wisely. The user can play as many times as they want, with a list of over 50+ possible words available. This project being my first ever Python based project was extremely fun to make so I hope you enjoy!

![Screenshot of finished program when opened](./docs/finished.jpg)

### Link to deployed app on Heroku: https://hangman-project.herokuapp.com/

---

## User Expectations / Stories

- As a user I want to be able to play a game of Hangman
- As a user I want to be able to see clearly what letters I have already guessed
- As a user I want to be able to play the game as many times as I want
- As a user I want a variety of words to guess from to keep the game interesting

---

## Existing Features:

- Firstly there is a welcome message to user. Then they are asked if they want to play the game.

- Upon answering no the user is told how they can start the game again if they change their mind.

- If they answer yes, the game begins and an empty word is diplayed along with the base stage of the hangman.

- The user can then enter a letter of their choice, pressing enter to submit the letter. From here there are four possible outcomes:

    1. The letter is not in the word. The letter is added to the 'Letters guessed:' list for the user to see. They are notified with a print statement that the letter is not in the word, and one stage of hangman is added and displayed.

    2. The letter is in the word. The letter is added to the 'Letters guessed:' list for the user to see. They are notified with a print statement that the letter was correct, and it is added into the word.

    3. The letter is already guessed. Reguardless of if it's in the word or not, if the letter is in the 'Letters guessed:' list they will be notified with a print statement that they already guessed that letter.

    4. The user input is invalid. The user must enter one single letter, or they will be told their answer was invalid and asked again for an input. Letters are not case sensitive.

- At the end of each of these the user is asked again for an input until the word or hangman are complete.

- If the hangman is complete they are told that have run out guesses, and it's game over. The word is then revealed to them so they can see what it was.

- If the word is complete they are congratulated on their win.

- After either of these outcomes the user is asked again if they would like to play, and the cycle continues.

---

## Future Features:

- An option to be able to choose the difficulty setting would make the game more suitable for different age ranges. For example children could choose to play on an easier setting that chooses from a list of shorter, more common words.

- An option to be able to play against a friend would make to game more interactive. If there was a two player option the players could take it in turns to choose the word for each other. There could even be a score system where each are awarded a point for correctly guessing a word, and the first to five points wins.

---

## Flowchart:

- I created this flow chart using an app called Goodnotes which I constantly keep beside me to record everything I do. The flowchart is a super useful way of planning a project and makes it a lot easier to plan out what functions you need to perform which tasks.

![Image of my flowchart showing stages of game](./docs/fc.jpg)

## Technologies:

- Python was the main coding language I used for this project. All the game code is written in Python.
- I used [Github](https://github.com/) and [Gitpod](https://www.gitpod.io/) for making this projected.
- I used [Heroku](https://www.heroku.com) to deploy my project.

---

## Testing:


- When the program is opened the user will see the welcome message and play question:

![Screenshot of the welcome message and question](./docs/hmwelcome.jpg)

- When the user answers the question there are multiple different outcomes:

The user answer is invalid. This could mean that they typed anything that is not 'y', 'Y', 'n' or 'N'. This includes punctuation, empty space, numbers, other letters or multiple of the above.

![Screenshot of invalid answers](./docs/invalid1.jpg)

- If the user answers 'n' or 'N' for no they will see the message telling them to click 'Run Program' if they change their mind, and the program ends.

![Screenshot of the program ending after user enters lower case n](./docs/n.jpg)

![Screenshot of the program ending after user enters upper case n](./docs/N2.jpg)

- If the user answers 'y' or 'Y' for yes, they will see the message "Great, lets play!" and the game begins.

![Screenshot of the program ending after user enters lower case y](./docs/y.jpg)

![Screenshot of the program ending after user enters upper case y](./docs/Y2.jpg)

- After the game begins the user can enter a second input to guess the letters from the word. Here are the different possible outcomes:

The user answer is invalid. This means they entered anything other than a single letter in lower or upper case. Again this could be punctuation, empty space, numbers, multiple letters or several of the above.

![Screenshot of invalid answers](./docs/invalid2.jpg)

The user answer was incorrect. Then they will see their guess added to the letters guessed list and a hangman stage added. In this case it's the first stage which is the head.

![Screenshot of incorrect answer](./docs/incorrect.jpg)

The user answer was correct. They will see a message telling them their guess was correct. Then they will see their guess added to the word and the letters guessed list.

![Screenshot of correct answer](./docs/correct1.jpg)

The user answer was already guessed, whether it was correct or not. Again this can be in lower or upper case. They will see the already guessed messaged and be asked for another input.

Examples of already guessed correct and incorrect letters in upper or lower case:

![Screenshot of users answer already guessed](./docs/guessed3.jpg)

- The user can continue to guess until either the hangman or the word is complete. If the hangman is complete, the user has lost and they are told that they ran out of guesses. They can see what the word actually was, before the play question from the begining is asked again. The steps are then repeated.

![Screenshot of user loosing the game](./docs/loose1.jpg)

- If the word is complete and the user has won, they are congratulated. The play question from the begining is asked again and the steps are repeated.

![Screenshot of user winning the game](./docs/win.jpg)

---

## Validator Testing:

- I tested my code using [Python Syntax Checker PEP8](https://www.pythonchecker.com) and found one indentation error which I quickly fixed resulting in no errors.

Validation of run.py file:

![Screenshot of run.py file showing 0 erros](./docs/codecheck1.jpg)

Validation of hangman.py file:

![Screenshot of hangamn.py file showing 0 erros](./docs/codecheck2.jpg)

Validation of words.py file:

![Screenshot of words.py file showing 0 erros](./docs/codecheck3.jpg)

- I tested my program using [Lighthouse](https://www.pythonchecker.com) from Google Chromes Dev Tools and it had a good score.

![Screenshot of lighthouse score](./docs/hangmanlighthouse.jpg)

---

## Bugs

- BUG: The user could guess the same incorrect answer again and again. 

- SOLUTION:  The guess was returned if it was valid before it was checked to see if it was on the list of guessed letters. All I had to do was switch the lines of code around inside the while loop. So after the 'if' statement I put 'user_input in letters guessed' followed by the print statement. Then after the 'elif' statement I put the code to check if the users guess was valid. Therefore it would check if the guess was already guessed before returning it to the play_game() function to be checked if it's in the word or not.

- OUTCOME: **Fixed**

Before fix:

![Screenshot of code before bug fix](./docs/bug1.jpg)

After fix:

![Screenshot of code after bug fix ](./docs/bug2.jpg)

- BUG: I currently have bug where the gaps between the underscores do not show up. It is **only on the deployed version** on Heroku.

- SOLUTION: I've spent a long time trying to fix this with help from a professional tutor and a mentor. After an hour of us trying different things this is still unfixed. We tried adding spaces but then they were counted as part of the word resulting in more issues. 

- OUTCOME: **UNFIXED** The game is still playable but the word is harder to see without the gaps. 

![Screenshot of bug](./docs/nospace.jpg)

---

## Deployment:

### Gitpod

- Typing 'python3 -m http.server' into the Gitpod terminal and clicking open browser on the pop up window allows you to view the site in a browser as if it were live.
- Alternatively you can type 'python3 run.py' into the terminal to run the game there.
- The browser can be refreshed to see any changes made, providing you quick save changes with ctrl+s. Sometimes you need to press ctrl, shift and R at the same time for changes to be updated.
- To save changes type 'git add .' into the terminal
- Next type 'git commit -m "_"' followed by your message describing what you changed inside the double quotes.
- Lastly type'git push' and this will push your code along with all the saved changes ready for use. This should be done at the end of every coding session or whenever you want an already deployed site to be updated.


### Github and Github Pages

- To deploy my site I first went to Github and found my project repository on the left hand side and clicked it.
- I then clicked on 'Settings' and then the 'Pages' option on the left.   
- Here I changed the branch from 'none' to 'main'.
- Finally I clicked save and after a short while a link to my deployed site is displayed on screen.
- It can take a few minutes, but if nothing happens I find that typing anything in the 'Custom domain' input box and pressing enter can cause the page to produce the link.
- I made sure to click on the link to check that it worked.
- Note that for this project deployed site on Github only displays the readme.md file, and it's Heroku where the actual game is runnable.

Link to deployed Github site: https://madeleinewalder.github.io/Hangman/

### Heroku

- I deployed my site using Heroku once I had made an account with them and linked it to my Github account. The steps were as follows:
- Click on 'New' and then 'Create new app'.
- Name the app. I named mine 'hangman-project'.
- Select the region. I selected Europe as that's my region.
- Click 'Create App'.
- Next go to the 'Settings' tab to create any Config Var's you need.
- For mine the key was 'PORT' and the value was 8000.
- Next scroll down to 'Buildpacks' to add any buildpacks you need.
- To do this click 'Add buildpack' and select the one you need. I needed two, the first was Python and the second was node.js in that order, making sure to click 'Save changes' after each.
- Click 'Save'.
- Go to the 'Deploy' tab.
- Select 'Github', search for your repository and click 'Connect'.
- Click on 'Automatic Deploy' to enable the app to be updated every time new code is pushed to Github.
- Then click 'Manual Deploy' to deploy to app. This can take a minute. When it's done click 'View' to see your deployed app and save the link.

Link to deployed app on Heroku: https://hangman-project.herokuapp.com/

---

## Credits:

- Line 77-83 of the run.py file takes heavey inspiration from a YouTube tutorial by a channel called 'Kite'. I had a lot of trouble and spent a lot of time trying to figure out how to write this part of the code.
I knew I wanted the correct letters to replace the underscores in the word when guessed but I wasn't sure how to do this. I knew that I would need the code to iterate through the individual letters of the word
and see if they matched to the users guess. From Kite's code I learnt the 'enumerate' keyword which could be used to do exactly that. I also learnt that I could use the '.join' method to add the correct letter in.

![Screenshot of credited code](./docs/kite.jpg)

Link to the video: https://www.youtube.com/watch?v=m4nEnsavl6w&t=510s&ab_channel=Kite (See 4:40).

- The hangman I used in my game was designed by Chris Horton. After trying to make my own I was having problems with the legs. I was using slashes like so: '/ \' but there was a bug with the program recognising the backslash as code and not displaying it. I changed them to two L's instead but then it looked confusing as they are also letters and could be mistaken for guessed answers. I then searched for a hangman diagram I could use instead and found this one https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c which was much better.

---