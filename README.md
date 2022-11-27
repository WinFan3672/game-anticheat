# Python Game Anticheat
A game anticheat for Python games. 
# What Is It
In a lot of IDEs that support Python, most notably IDLE [the default, in-built one], exiting the game would enter the shell rather than exiting. 
As a result, one could modify a variable and then call a subroutine and jump back into the game. 

This anti-cheat rectifies that. It uses a range of techniques to prevent people from getting to the terminal in the first place, and even nuking it by the time they reach it, so that they cannot jump back into the game, since the game would be gone. 

# How To Use

- Clone this repo.
- Edit anticheat.py to include your game. There is a single comment that says "put game under here."
- That's it. If you have issues with it, make sure you put the game in the right place.
## Exiting The Game
Instead of doing `quit()` or `exit()` as you usually do, use `raise ExitError` instead. It will instantly close a CMD window, and nuke an IDE window. 
# I found a way to bypass it!
Let me know at `winfan3672@gmail.com` ASAP or create an issue.
# I want to contribute!
Leave a pull request or issue. I'll look into it.
