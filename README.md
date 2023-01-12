# Hangman

Welcome to Hangman, a simple game based on a childhood classic. In this game the user can play against the computer to guess the correct letters from a random word. However they must race to complete the word before running out of lives.
In this game the user can play as many times as they want, with a list of over 50+ possible words to keep it interesting.

### Link to deployed program: --- ADD ---

--- example screenshot? ---

---

## User Expectations / Stories

- As a user I want to be able to play a game of Hangman
- As a user I want to be able to see clearly what letters I have already guessed
- As a user I want to be able to play the game as many times as I want
- As a user I want to a variety of words to guess from to keep the game interesting

---

## Existing Features:


---

## Future Features:

- An option to be able to choose difficulty

- An option to be able to play against a friend. Have them choose the word for you and vise versa.

---

## Technologies:

- Python was the main technology I used for this project. All the game code is written in Python.
- I used [Github](https://github.com/) along with a Python template to create my repository and [Gitpod](https://www.gitpod.io/) for writting the code.

---

## Testing:

--- screenshots ---

## Validator Testing:

- I tested my code using JSHint and it found no errors

--add image--

---

## Bugs

- I had a bug where the legs of the hangman diagram were made of slashes like so: / \ . However the program saw the backslash as something that shouldn't be displayed for some reason. This resulted in him always having one leg and offset the bottom of the stand onto to right end of the next line. Basically it ruined the final stage of the diagram and I had to rework it by making the legs L's instead. This seemed to fix the issue as the program no longer recognised the punctuation as a kind of command or syntax for something else.

---

## Deployment:

### Gitpod

---text here ---

### Github and Github Pages

--- text here ---

### Heroku

- I deployed my site using Heroku.

---

## Credits:

- Line 55-63 of the run.py file takes heavey inspiration from a YouTube tutorial by a channel called 'Kite'. I had a lot of trouble and spent a lot of time trying to figure ouut how to write this part of the code.
- I knew I wanted the correct letters to replace the underscores in the word when guessed but I was'nt sure how to do this. I knew that I would need the program to iterate through the individual letters of the word
and see if they matched to the users guess. What I didn't know until watching this tutorial was that I could use the '.join' method to the add that letter in if it did match.
- Link to the video: https://www.youtube.com/watch?v=m4nEnsavl6w&t=510s&ab_channel=Kite (specifically at 4:40)

---

---

---

## CI info
* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.