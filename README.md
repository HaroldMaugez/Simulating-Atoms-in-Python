## ⚛️ Simulating-Atoms-in-Python

I’m working on this project for an NSI-level physics assignment :

My teacher asked me to create a Python project once I finish the course material ahead of schedule.
So here’s my project: It’s inspired by a video by Kavan, who did the same project but in C++. I decided to take on this project because it will allow me to combine my physics and computer science classes into a single project.

![Original Vidéo](/images/Kavan-Video.png)

Since I’m against using AI, I’m going to document each of my steps and the sources that helped me get to this point. The goal of this project is to be concise—at least more so than my other projects—but still rewarding.

### This is the beggining of a long story : 
---

#### First Commit, initializing Pygame
For this project, I'll need a visual game engine. I could use Turtle but I choosed Pygame as it's a game engine not a geometric engine to draw some circles.
So the first step is to initialize a window. I have to check the official documentation after importing it into my IDE.

![Official Documentation](/images/PygameQuickStart.png)
##### So let's put that into one simple code

![FirstCommit](/images/InitializePygame.png)

In his video, the nexte step is to make a simple atom like evryone learned, for this he used a complexe system of calculation to make a circle. Luckly for me, I can do that with only one line in python : pygame.show.circle()

![pygame.draw.circle()](/images/DrawCircle.png)

So, I looked what parameters he used to take the same.
Then, I did a simple condition to color and resize the particule wether it's a proton, a neutron or an electron. Made the electron orbit around the proton with the same maths as him.
Puting that on a list and now I can create as many atoms as I want just with coordinates.

![A part of the actual code](/images/SimpleAtom.png)
