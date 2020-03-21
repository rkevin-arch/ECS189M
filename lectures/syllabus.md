# ECS189M: Hands-On Cybersecurity

Welcome to ECS189M! Here, we will learn about the basics of computer security, how to find vulnerabilities, how they can be exploited, and how to fix them and defend against attacks. This course will be heavily focused on hands-on exercises.

We will be covering four subjects in cybersecurity: the Linux operating system, webapp exploitation, binary exploitation and cryptography. 

**CRN**: [REDACTED]. Remember to select 4 units for this course.

**Prerequisites**: At least one lower division ECS course or equivalent, to make sure you can program in at least one language comfortably. ECS50 (x86/x86_64 assembly) is not required, but will help. ECS153 (Computer Security) is also not required.

**Lectures**: Mondays, Wednesdays and Fridays, 1:10PM-2:00PM, in Cruess Hall 107. Mondays and Wednesdays will be main lecture days, and Fridays serve to either cover material that didn't get covered earlier in the week or for extended office hours. Discussions will be used as extended office hours, and won't be mandatory.

## Instructor info
Instructor: @rkevin-arch

Co-instructor / TA / Friend: @aenygma

Instructor of record / Advisor: Prof. Matt Bishop

Office Hours:
- Mondays 7PM-8PM in Cruess 107
- Tuesday 3PM-5PM in Kemper 53
- Wednesday 2PM-4PM in Kemper 53
- Thursdays 3PM-5PM in Kemper lobby
- Fridays 1PM-2PM in Cruess 107 (if we don't have class)
- Or by appointment.
- Or if you see me in the Kemper lobby at any time.

Feel free to email me (@rkevin-arch) at any time, and put [ECS189M] in the subject so I know it's important. I should get back to you within 24 hours, and if I don't, just keep bugging me until I respond.

#### Office hours during Finals

Office hours during finals week will be completely online, from 1-5PM, every day Monday to Thursday, and 3-10PM on Friday.

The preferred way to contact me during office hours is via Discord. I have created [a temporary guild](https://discord.gg/TJgkeeg) to host office hours in, and you may join the voice chat and ask your question. I may ask you to share your screen to help you debug, and Discord provides a convenient option to do so.

If you don't want to register on Discord, you may also use Zoom to contact me, Just send me an invite via email and I'll hop in. Note that I might not check my email every second, so maybe coordinate a time with me in advance. I'll definitely try to check it every 30 minutes during office hours, though.

Finally, if all of the above doesn't work for you, keep in mind that [Piazza](https://piazza.com/class/k5xdzuh03l7664) is still a thing if you just need regular help.

## Grading
There will be no quizzes, midterms or finals for this class. Your grade will be solely determined by a Capture-the-flag "competition" that will run during the quarter.

There are 51 solvable challenges and 10000 available points throughout the quarter. You can also earn 500 points as "extra credit" by submitting a writeup before 10PM, Friday, Mar 20th, detailing how you attempted to solve the final 4 challenges (If you failed to solve any / all of those 4 challenges, I can also award you extra credit based on how far you got in the writeup).

The grade cutoffs are as follows. Considering the class average is now an A-, and more than 80% of people have at least a B, we are not going to change the cutoffs.

Max|A+|A|A-|B+|B|B-|C+|C|C-|D+|D|F
-|-|-|-|-|-|-|-|-|-|-|-|-
10500|7000|6500|6000|5500|5000|4500|4000|3500|3000|2500|2000|0

## Capture the Flag
If you haven't heard of capture-the-flag competitions, they are a type of computer security competition. You solve challenges that test your skills (breaking into a vulnerable service, cracking a cipher, etc.) and you get a "flag" at the end, which proves you have succeeded in breaking into the system. You the submit the flag for points. If you are still unsure, [here's](https://youtu.be/8ev9ZX9J45A) a short video so you can decide if the class is for you or not.

The CTF portal is [here](https://twinpeaks.cs.ucdavis.edu/) (https://twinpeaks.cs.ucdavis.edu/). Details of all challenges and flag submission will all be done through this portal. When you register, please use your UC Davis email address so we can match your score to yourself (or let me know which email you used). All flags will look like `ECS{SOME_STUFF_IN_HERE}`. As a freebie, the flag for the "introflag" challenge is `ECS{W3LC0M3_0E08436ACF7DA35A9D508E7A3BF8690A}`.

In this class, we will have 51 challenges in total. The challenges will only be available during the times listed below. _There won't be extensions_, so start early!

|Category|Available from (00:00AM)|Available until (11:59PM)|Total possible points|# challenges|
|-|-|-|-|-|
|Linux and miscellaneous|Jan 6|Feb 2|1900|14|
|Webapp exploitation|Jan 26|Feb 17|1700|10|
|Binary exploitation|Feb 9|Mar 9|2650|14|
|Cryptography|Feb 24|Mar 15|1450|8|
|Final challenges|Mar 9|Mar 20 (10:00PM)|2300+500|5|
|TOTAL|||10000+500|51|

## Final challenges
The final challenges will be available from `00:00AM, Monday, Mar 9th` to `10:00PM, Friday, Mar 20th`. There will be 4 final challenges, worth 550 points each. In addition, there is also a feedback form available between `10:00PM, Friday, Mar 20th` to `11:59PM, Saturday, Mar 21th`. If you fill out the feedback form, you will also get 100 points.

Each of the 4 final challenges test you on the 4 parts we covered in class: Linux privilege escalation, webapp exploitation, binary exploitation and cryptography. Each challenge is split up into three parts. If you finish all three parts, you should get the flag. If you can only finish one or two parts, you can get 175 or 350 points of partial credit, respectively. You need to explain how you got to the part you're on in your [writeup](#writeup). Each part will be marked by an explicit message saying you're 1/3 or 2/3 of the way there, so if you see the message, you are eligible for the partial credit.

## Writeup
There will be an optional writeup due `10:00PM, Friday, Mar 20th`. In the writeup you are supposed to detail what you have tried and how far you got for _each_ of the final challenges. You can earn 500 extra credit points in addition to the partial credit of the final challenges. Note that if you submit to Canvas early I can give you a preliminary grade and you can make further changes before the deadline.

There is no official grading rubric, but I ask that you explain every step you did, including anything you tried that didn't work. (Learning from failures is important, so please include them!) Supplement everything with screenshots, and include the source code of any exploit you have (functional or not), or any script you have used. You don't have to follow a formal format like a lab report, as long as everything is clear to someone who hasn't looked at the challenges yet.

You can use whatever format is the most convenient for you (Word/Google docs, markdown, LaTeX, etc). Handwriting is discouraged since I require you to send screenshots and your exploit code.

Here are some examples of writeups. I just found them on [CTFTime](https://ctftime.org), which is a great website to find CTFs. All of these challenges are harder than the ones we have in class, so it's not required for you to understand any of this. Just look at how people explain what they're doing and try to emulate that in your writeup. If your writeup goes through around the same amount of detail, you should get full points.
1. [Web challenge from BSidesSF](https://medium.com/@ctfgudai/bsides-san-francisco-recipes-204-points-e1cd93fe9ef)
2. [Some crypto challenges from HackTM CTF Quals](https://www.0xkasper.com/articles/hacktm-ctf-2020-qualifiers-write-up)
3. [Binary exploitation challenge from Pwny Racing](https://rkevin.dev/blog/pwny-racing-community-challenge-7-writeup/) (no need to be this verbose)

By the way, if you fail to solve any part of any final challenge (unlikely, but _just_ in case), and don't have enough to write about, including your attempts, you are allowed to pick 4 challenges you have solved during the CTF. Try to pick the hardest ones in your opinion so you have more to write about.

Your writeup should be graded within 24 hours of your submission, and your final grade should be available shortly after Saturday midnight.

## Academic Integrity

The UC Davis Code of Academic Conduct, available [here](http://sja.ucdavis.edu/files/cac.pdf), applies to this class. Please make sure you follow the rules for the course.

You are encouraged to help one another by talking about how you are doing the challenges. You can work together, but each of you should write your own exploit. **DO NOT SHARE FLAGS WITH OTHERS.** If you do, you will receive an F in the course. You shouldn't share exploits with each other either, unless you _both_ have solved the challenge already and want to learn from each other's exploits. If you finished a challenge, you may help others debug their exploits, but you may not give them your exploit until they solved it as well.

As a legal disclaimer, we allow you to attack anything under `twinpeaks.cs.ucdavis.edu`, except for the scoreboard (this site). All denial-of-service attacks are disallowed. For HTTP(S) websites, do not attack anything that's not under `*.webchal.twinpeaks.cs.ucdavis.edu`. Anything not running on `twinpeaks.cs.ucdavis.edu` is out of scope. You shouldn’t be able to get root-level access when solving any challenge. If you do, please let me know ASAP and please don’t abuse this privilege.

## Lecture schedule

These are subject to change, depending on how ahead/behind of the material we are. The challenges listed mean you can solve them after the lecture. If a challenge is not listed here, that means you'll have to do your own research to figure out how to attack it!

Date | Content | Links | Challenges |
-|-|-|-
M 1/6|Syllabus + what are CTFs|[slides](https://drive.google.com/open?id=16TJfjI6n0hByiVrPtJwkGCLFKQ0dd3tEJmVFCWJA40w)|introflag|
W 1/8|Basic Bash commands|[slides](https://drive.google.com/open?id=1Q-iHpHYpjuwPWloh5HhlmVfATsdnYqMG1D5V188Bu6Y)|linuxbasics|
M 1/13|Advanced bash techniques and basic log analysis|[slides](https://drive.google.com/open?id=1kO4vhXI8FLo_jDnXe-wTgAG-CGo6YSy0FPYdzk0B3Ec)|linuxadv, loganalysis|
W 1/15|TCP Ports and talking to remote servers|[slides](https://drive.google.com/open?id=1tHcXE7iu699sTLic64TuwrO_COLfn2gRVVhgrVF3z78)|nmap, nc, addition, binaryaddition|
M 1/20|HOLIDAY, NO CLASS|-||
W 1/22|Linux system enumeration and privilege escalation|[slides](https://drive.google.com/open?id=1OMB08gdXmcqJfHXruFzPAcfuiZmeSKom0WKl-QGcNWs)|privesc1, privesc2, privesc3|
M 1/27|HTTP packets, headers, cookies, Javascript, PHP|[slides](https://drive.google.com/open?id=1HU1YeI1yG7HX__oHh_p0bV5_FsNIXWNMYMv4QWlDdto)|adminme, phpeval, jsprog|
W 1/29|Local File Inclusion and Log Poisoning|[slides](https://drive.google.com/open?id=1zHkZL1MkPBcjnlRz8vV3Gr3-w3B21ScdUmT1yb7kbYc)|babylfi, lfirce|
M 2/3|Cross Site Scripting and Cross Site Request Forgery|[slides](https://drive.google.com/open?id=1RWVEP9s3z8WQtHQ_gFBP02JATMzDk4M3GypVxztvDmc)|xss, csrf|
W 2/5|SQL injection|[slides](https://drive.google.com/open?id=1XtkmZYxEc_rpm2Iyhp3ORIodN-NVZ1I74z9_vKTPHBQ)|sqli, searchbar, bsqli|
M 2/10|x86 and x86_64 Assembly refresher|[slides](https://drive.google.com/open?id=1SiYFYhXvQbZXesYpPT7q89xkkdvFndSROcS-6L7Ffr8)||
W 2/12|Using GDB to examine programs|[slides](https://drive.google.com/open?id=1LDld49fp6yp5qV5CCgVC258MroIyseVkoYcQBpiFpFU) |stringy, runme, trace, xmem, reveng|
M 2/17|HOLIDAY, NO CLASS|-||
W 2/19|Calling conventions and stack buffer overflows|[slides](https://drive.google.com/open?id=1bDUIh-OXVa_meFnk33ZzjxsnvEHMNOhASwULAyecn-k), [binaries](/calling_conventions.zip)|babybufov, toddlerbufov|
M 2/24|No lecture|-||
W 2/26|Return Oriented Programming|[slides](https://drive.google.com/open?id=1asV0zvNlPZa4zmTUwo_6cjetGllklCNmE7enlD1uQRE)|babyrop, ropmelikeyoumeanit|
M 3/2|Classic ciphers|[slides](https://drive.google.com/open?id=1ug5uiBlox2tNlf5c76F0AEaDx6l5cpiww2kQX_Xjsyk)|caesar, substitution, vigenere|
W 3/4|Diffie-Hellman key exchange and RSA encryption|[slides](https://drive.google.com/open?id=1EO27BFdUHw6NKCPFe0vLVF2mfE-W4VlZhSiCreqwuMU)|dhke, rsadec, rsarev|
M 3/9|Signatures, certificates and cryptographic hash functions|[slides](https://drive.google.com/open?id=1n5xxbkWfDfgtYai9MxZLt-VFt1JUWARqh61vIBm-g0U)|signing|
W 3/11|No lecture, extended office hours|-||
