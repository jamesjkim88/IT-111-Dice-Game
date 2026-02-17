# Dice Game (Flask)

## Description

This project is a web-based Dice Game built using Python and Flask.  
The game follows simplified Craps rules and demonstrates input validation, conditional logic, and control flow.

## How the Game Works

- The game starts at Turn 1.
- On the first roll:
  - Rolling 2, 3, or 12 → You lose.
  - Rolling 7 or 11 → You win.
  - Any other number → That number becomes the "point".
- On later turns:
  - Rolling 7 → You lose.
  - Rolling the point number → You win.
  - Any other number → Continue playing.

Each roll must be between 2 and 12.

## Technologies Used

- Python 3
- Flask

## Project Structure
