![Game view](https://cdn.discordapp.com/attachments/617778489374015488/691311834652737606/unknown.png)

# README

## The game: notaviralgame

This game was made for the [Trijam#62](https://itch.io/jam/trijam-62) game jam which theme was *Viral Infection*. We didn’t want the COVID19 interpretation of it so we figured we’d do a game revolving around a computer viral infection. 

And so we started our first ever game jam. The plan was to have computer nodes spread around the screen that would form a net. The idea was that the player would be a hacker trying to create their botnet.

For this the gameplay goes as follow:

- the players clicks on a node to infect it
- the more infected neighbors there are the greatest the chance to succeed the infection!
- if the infection fails the link between the two nodes has a chance to blacklist the attacking node (this should have blacklisted it also for links that had proxies but we ended up running out of time)
- the goal of the game is to infect as many nodes as possible

This was a really simple idea in our heads when we set out to do it. However neither of us had any experience with game jams and now realize we spent more time on polishing some unessential aspects than actually implementing gameplay. This taught us a lot and we both had a lot of fun doing it!



We hope you’ll have fun playing the game!

*NB: there is no actual game to speak of, just circles to click*



## Installation

At this time we do not offer pre-built binaries for the game. If you wish to play it you will need to make sure you have:

- python (>=3.7)
- pygame (2.0.0.dev6)

For this I recommend installing python and then run `python -m pip install -r requirements.txt`. This should take care of everything. Then you simply need to get into the `src` folder and run `main.py`. (ex: `python main.py`).



The source can be found on [Github](https://github.com/s0lst1ce/notaviralgame)

## Credits

This game was entirely made by [Kadir Aksoy](https://github.com/kadir014) and [I (s0lst1ce)](https://github.com/s0lst1ce/).

The music was kindly provided by [Kubbi](https://www.youtube.com/user/KUBBIkthxbai/featured).
