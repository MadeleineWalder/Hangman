# Hangman

Welcome to Hangman! A simple game based on a childhood classic written using python. In this game the user can play against the computer to guess a random word before they run out of lives.

---

### Link to deployed program: --- ADD ---

--- example screenshot? ---

## User Expectations / Stories

---

## Existing Features:

---

## Technologies:

---

## Testing:

--- screenshots ---

## Validator Testing:

- I tested my code using JSHint and it found no errors

--add image--

---

## Deployment:

### Gitpod

---text here ---

### Github and Github Pages

--- text here ---

### Heroku

--- text here ---

## Credits:

- Line 55-63 of the run.py file takes heavey inspiration from a YouTube tutorial by a channel called 'Kite'. I had a lot of trouble and spent a lot of time trying to figure ouut how to write this part of the code.
- I knew I wanted the correct letters to replace the underscores in the word when guessed but I was'nt sure how to do this. I knew that I would need the program to iterate through the individual letters of the word
and see if they matched to the users guess. What I didn't know until watching this tutorial was that I could use the '.join' method to the add that letter in if it did match.

--- add link ---

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