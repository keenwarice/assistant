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
