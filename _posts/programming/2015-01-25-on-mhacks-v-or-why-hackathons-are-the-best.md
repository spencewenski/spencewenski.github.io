---
layout: post
title: "On MHacks V (or, why hackathons are the best)"
categories:
- programming
tags:
- hackathons
- mhacks
- programming
- writing_201
---

If you're like me, you already know why MHacks is the best. But for everyone else, let me explain:

<!--more-->

MHacks is like being a kid in a candy shop for 36 hours straight, with no adults to tell you what to do. MHacks is like being at an amusement park where everything is free and the are no lines (except for food, I guess; the like for food is always long...). Anyway, MHacks is like a 36 hour programming competition where bleeding edge, high-tech products are everywhere, and everyone there is better than you at something, and you just want to talk to everyone you see. See? It's the best.

Here's a rundown of my experience at this semester's MHacks:

It started at the opening ceremonies with a speech from the creator of the Magic Bus system and the ride sharing app Sidecar. He talked about how everyone in the room has the chance to make an impact and effect change; you know, the usual inspirational jargon. Then the hacking commenced!! I met a couple guys from Purdue, brainstormed some ideas, and started working on our favourite: an app that finds the warmest path between two points.

So for the next 36 hours (minus a few for sleep), we worked on our app. We gathered the data we would need for the demo, whipped up an Express api, [transformed an existing implementation of Dijkstra's algorithm](https://github.com/andrewhayward/dijkstra) into a Node module, hacked together a front-end using [Mapbox](https://www.mapbox.com) and some custom controllers, and voilà, we had our app. The only thing left to do was find a place to host it. Since Microsoft was there promoting their [Azure](http://azure.microsoft.com/en-us/) service, we went with that (and aside from a couple issues with the way our git repo was set up, it was actually pretty painless). For anyone interested in more detail, the code is hosted on my [GitHub](https://github.com/spencewenski/mhacksv).

![Strol screenshot]({{ site.url }}/assets/strol_screenshot.png)

At the end of the 36 hours, the judges deliberated, chose the top ten finalists, and those ten teams demonstrated their projects at Rackham. During set up and other delays, there were rap battles, [Rue whistles](http://youtu.be/CCu_-bIdHtc) throughout the audience, and probably the worst rendition of "Let it go" I've ever heard (and since it was performed impromptu by a bunch of engineers, I'm not surprised). Anyway, here are the top ten projects:



	
  * [A Tango Vision](http://challengepost.com/software/a-tango-vision) - an motley of technologies combined to create a 3D projector

	
  * [Skipchat](http://challengepost.com/software/skipchat) - a P2P messaging protocol; basically the messages are transferred between phones by Bluetooth until the message reaches its intended recipient (my personal favourite)

	
  * [Drum-teacher](http://challengepost.com/software/drum-teacher) - (aka drum hero) an augmented reality app/game uses a headset to overlay a beat/pattern onto a real life drumset

	
  * [Haptic Feedback Suit](http://challengepost.com/software/haptic-feedback-suit) - a suit that simulates physical interactions with a virtual reality

	
  * [Draw Anything](http://challengepost.com/software/draw-anything) - a drawing app that takes any images and shows you the steps required to draw that image

	
  * [Left 4 Virtual Reality](http://challengepost.com/software/left-4-virtual-reality) - Left 4 Dead on a VR headset and physical (nerf) gun controls

	
  * [DataWave](http://challengepost.com/software/datawave) - Internet of FM radio

	
  * [Mixtape](http://challengepost.com/software/mixtape-enbmh) - basically just an audio looper, not really sure why this was in the top ten

	
  * [Erudite](http://challengepost.com/software/erudite-okay-glass-make-me-smarter) - Google Glass app that listens to your conversation and searches Wikipedia for words you might want to know more about

	
  * I forget the name of the last one, but the team developed a way to reverse engineer iPhone apps and inject new visuals


And here are some of my personal favourites, some of which won prizes, others of which did not but were still cool:

	
  * [FuzzBeed](http://challengepost.com/software/fuzzbeed) - procedurally generated BuzzFeed articles; basically just random articles that follow the format of the basic BuzzFeed listicle

	
  * [Portal](http://challengepost.com/software/portal) - an innovative new way to use tabs, in which the tab is displayed as a pop-up in the current page instead of as a new tab

	
  * [HueMonitor](http://challengepost.com/software/huemonitor) - samples pixels on your screen uses the pixels' colour to change the colour of two external LED lights, creating a cool ambiance

	
  * [Twilix](http://challengepost.com/software/twilix) - allows system admins to control their servers via SMS


To check out the rest of the projects, visit the [MHacks V page on ChallengPost](http://mhacksv.challengepost.com/).

So yeah, it was a great time. Getting to spend the weekend working on a random project with other brilliant engineers, surrounded by even more brilliant engineers, is basically the dream. I loved every minute of it and I can't wait for MHacks VI.
