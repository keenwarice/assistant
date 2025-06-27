---
title: "Sirius | AI voice assistant"
author: "rice"
description: "An AI voice assistant that doesn't spy on you"
created_at: "2025-06-23"
---

# June 23rd: first steps for audio!!
**8:46 PM:**<br/>
got audio to work yippie!<br/>
[the audio](https://github.com/keenwarice/assistant/blob/0080e99633b3a5e2bb6d95e8da195b1a5354822f/journal_attatchments/recording_JUN23_845.wav)<br/>
 <br/>
**9:07 PM:**<br/>
YESSIR, got STT to work finally<br/>
![image of an expert coder's STT working](https://raw.githubusercontent.com/keenwarice/assistant/7fa26025a701c7c745ecd39e5ff69e68ebdc80c4/journal_attatchments/Screenshot%202025-06-23.png)<br/>
 <br/>
 
# June 24th: WAKE WORD DETECTION & PROMPT PROCESSING
**4:30-5:11 PM:**<br/>
ITS NOT WORKINGGGGGGGGGGG<br/>
so basically im trying to use vosk to listen constantly (don't worry I wont log it so you don't get spied on) and trying to get partial phrases to detect the wake word but idk whats happening<br/>
for some reason its not working the second time the wake word is said<br/>
normal function:<br/>
![normal function of code](https://raw.githubusercontent.com/keenwarice/assistant/ecab1a540b3ae39889de5407377b2cf8636f79cf/journal_attatchments/2025-06-24%20normal%20function.png)<br/>
second time saying it:<br/>
![image of perfectly fine code not doing what its supposed to](https://raw.githubusercontent.com/keenwarice/assistant/ecab1a540b3ae39889de5407377b2cf8636f79cf/journal_attatchments/2025-06-24%20odd%20function.png)<br/>
 <br/>
**5:31 PM:**<br/>
i fixed it. all i needed to do was reset last_detected, questioning my own intelligence<br/>
wish me luck on working on the AI and voice recognition<br/>
 <br/>
**7:20 PM:**<br/>
I GOT IT TO WORK!<br/>
i have gotten the script to record a single phrase after the wake word is said, identify it with vosk, and send the file & phrase over to the main Python file!!!!<br/>
next step: add voice recognition and assistant response<br/>
![image of the code actually working for once](https://raw.githubusercontent.com/keenwarice/assistant/3edba28b8b5f6bfd07f1cfa1da635a1c2241bb1b/journal_attatchments/2025-06-24%20itworks.png)<br/>
 <br/>
 **8:50 PM:**<br/>
just got voice recognition to work! i used resemblyzer and volunteered my sister to train the recognizer as well. it works for both of us and recognizes our separate voices. i obviously censored the names, but you can see the separate names.<br/>
![image of my voice recognition working](https://raw.githubusercontent.com/keenwarice/assistant/0c31c0ed3d48e6770e63093f9106580b24bd613c/journal_attatchments/2025-06-24%20voice%20recognition.png)<br/>
 <br/>
 **10:11 PM:**<br/>
 after a short break, i uploaded all of the voice recognition code and made simple code to easily add voices.<br/>
  <br/>
 # June 25th: AI & INTERNET
 **7:40 PM:**<br/>
 ive worked on the AI integration for the entire afternoon, and i got it mostly to work. i let the AI search the web for results, but i think the AI is too stupid to understand my instructions, and is doing the opposite of WHAT I TELL IT. im thinking of switching from llama to zephyr.<br/>
![idiot AI making something up](https://raw.githubusercontent.com/keenwarice/assistant/fb73bbfa011226d33a13b523efeb9c45266323e6/journal_attatchments/2025-06-25%20ai%20dumb.png)<br/>
 <br/>
 **8:12 PM:**<br/>
 there may be an issue. i was testing to see if my raspberry pi 5 was capable of running the AI (it was 4.1 gb), but when i tried downloading it weird colors started appearing on screen so i immediatley stopped it.<br/>
 i think it was about to crash but i thought maybe enabling adding more swap memory would help, so i overrode the limit and gave myself 2 gb over the max (4gb) of swap memory. hope i dont break the rpi. wish me luck. might have cooked the pi<br/>
 ![image of rpi on life support
](https://raw.githubusercontent.com/keenwarice/assistant/fb73bbfa011226d33a13b523efeb9c45266323e6/journal_attatchments/2025-06-25%20rpi%20problem.png)<br/>
**8:25 PM:**<br/>
there may be another issue.<br/>
the pi wont run ai anymore even small models. i might have to find another solution but this might force me to find another computer or run it on an old home computer...<br/>
ill hopefully find a solution soon<br/>
 <br/>
**10:06 PM:**<br/>
![the ai is not cooperating I am not very happy](https://raw.githubusercontent.com/keenwarice/assistant/fee34853c2f8868a24439e337a412058b1b70a41/journal_attatchments/2025-06-25%20ahhh.png)<br/>
<br/>
# June 26th: big fixes with AI<br/>
**7:53 PM:**<br/>
YEAAAAAAH IT WORKED!!!!! i fixed the system prompt and made it have the capability to search the internet.<br/>
![ai searching the internet](https://raw.githubusercontent.com/keenwarice/assistant/8be3238b016c7275dc3d4c1c47b9f7a3c1e25419/journal_attatchments/2025-06-26%20ai%20search.png)<br/>
and yes that was accurate<br/>
![real stock price](https://raw.githubusercontent.com/keenwarice/assistant/8be3238b016c7275dc3d4c1c47b9f7a3c1e25419/journal_attatchments/2025-06-26%20real%20stock%20price.png)<br/>
 <br/>
**8:01 PM:**<br/>
okay, maybe the AI is still not smart...<br/>
![bruh image](https://raw.githubusercontent.com/keenwarice/assistant/8be3238b016c7275dc3d4c1c47b9f7a3c1e25419/journal_attatchments/2025-06-26%20chicken.png)<br/>
 <br/>
# June 27th: TTS & small updates<br/>
**3:42 PM:**<br/>
updated the code with changes i made last night, minor changes like clearing up system prompt and fixing a problem where if the wake word is said accidentally, it would keep listening for a question forever. planning on adding TTS today<br/>


