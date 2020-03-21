The quarter is now over, so the challenges are no longer there. I'll look into hosting them myself, but that might take a while. In the meantime, don't be surprised if the ports are closed. This is here more for documentation purposes.

Some of the following URLS no longer apply (like the ones to start webapp challenges). For those URLs, they will lead to `about:blank` instead, and Github won't even render them as links.

There are some challenges with attachments, namely the ones involving binary challenges or the ones I decide to release the source code for (like timingsc or authtoken). You can find those files in the `challenges` folder.

# Linux and miscellaneous

## introflag

Read the syllabus!

## linuxbasics

Test your linux basics! SSH into `linuxbasics@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`. Play around with the system and answer the following questions:

1. What's your current working directory?
2. Search the man pages. What command would you use to generate random permutations?
3. On what day was /home/user/myfile.txt modified? Use the date format 2019-12-31
4. How big is /home/user/myfile.txt, in kilobytes? Round to the nearest whole number.
5. What user owns the file /home/user/myfile.txt?
6. What's the 3-digit octal permissions of the file /home/user/myfile.txt? (e.g 777)
7. What is the user id of 'admin'?
8. There's a user 'john' on the system. Can he write to /home/user/myfile.txt?
9. Can the 'admin' user execute /home/user/myfile.txt?
10. Which user on the system, except for you, root, admin and john, can execute /home/user/myfile.txt?
11. /home/user/myfile.txt looks like a txt file, but it actually isn't. What kind of file is it?
12. Change the ownership and permissions of /home/user/chme, so that you have full read-write-execute permissions, jade and rose can read the file only, and john cannot read write or execute the file.

Once you have figured out the answer to a question, run `answer x` to answer question number x.

## linuxadv

Time for some more advanced topics! SSH into `linuxadv@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`. Play around with the system and do the following tasks. Once you're ready, run `answer x` to try to do the xth task.

1. Try backgrounding this process and foregrounding it again.
2. What's my PID?
3. Send me a SIGUSR1 signal.
4. Redirect my standard input to be the contents of /home/user/in.txt
5. Redirect my standard error into /dev/null.
6. Cat out the contents of /home/user/in.txt, grep for the lines that contain the lowercase letter 'a', and pipe the result into me.
7. Run `. spawner` to solve this challenge. I've just spawned 5 background jobs. Find the correct one to foreground!

## loganalysis

You have some big log files, time to get some useful data out of them! SSH into `loganalysis@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`. Play around with the system and answer the following questions:

1. How many lines are in access.log?
2. Using access.log, which IP tried to find information about Siemens?
3. Using access.log, how many requests claim to be from a Windows 10 machine?
4. Using access.log, how many unique IP made requests to the server?
5. Using access.log, which IP made the most requests to the webserver?
6. Using auth.log, which IP appeared the most amount of times in the file?
7. Find the right "flag" in flags.txt. The flag should look like `ECS{START_TAIL}`, where `START` only contains uppercase letters, numbers and underscores. `TAIL` is 32 characters long and only contains numbers and the upper case letters A-F. There should be no characters before or after the flag.

Once you have figured out the answer to a question, run `answer x` to answer question number x.

## nmap

There's a port on `twinpeaks.cs.ucdavis.edu`, between `50000` and `60000`. Find it and examine the server version.

## nc

Practice how to use netcat to connect to and listen on ports.
SSH into `nc@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`.
Use `nc` to connect to `localhost` port `12345` and follow the instructions. Your goal is to get a shell as `admin` and read `/home/admin/flag`.

## addition

John's homework is due soon! Help him do his homework! Connect to `twinpeaks.cs.ucdavis.edu` port `30001`.

## binaryaddition

John's in trouble yet again! Help him do his homework! Connect to `twinpeaks.cs.ucdavis.edu` port `30002`.

## privesc1

Find a way to escalate privileges from `user` to `admin`! SSH into `privesc1@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`. Your goal is to read `/home/admin/flag`.

## privesc2

Find a way to escalate privileges from `user` to `admin`! SSH into `privesc2@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`. Your goal is to read `/home/admin/flag`.

## privesc3

Find a way to escalate privileges from `user` to `admin`! SSH into `privesc3@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`. Your goal is to read `/home/admin/flag`.

## race

A simple race condition. SSH into `race@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`. Your goal is to read the `flag` file in your home directory.

NOTE: I won't be talking about how to solve this in class. Click [here](https://en.wikipedia.org/wiki/TOCTOU) for a hint, or ask me in office hours.

## strcmp

Figure out my password of 20 lowercase letters. Connect to `twinpeaks.cs.ucdavis.edu` port `30004`.

NOTE: I won't be talking about how to solve this in class. Click [here](https://linux.die.net/man/3/strcmp) or [here](https://en.wikipedia.org/wiki/Binary_search_algorithm) for a hint, or ask me in office hours.

## timingsc

A side channel timing attack. Connect to `twinpeaks.cs.ucdavis.edu` port `30003`. The code being run on the server side is provided below.

NOTE: Code for `server.py` updated to include a hint. Please redownload it.

NOTE: I won't be talking about how to solve this in class. Click [here](https://en.wikipedia.org/wiki/Timing_attack) for a hint, or ask me in office hours.

# Webapp exploitation

## adminme

Try and become administrator on this web application. I heard the developers have no idea how cookies work...

Click [here](about:blank) to start the challenge.

## phpeval

Write some PHP code! Once you gain code execution, explore the system a bit to find how to get the flag.

Click [here](about:blank) to start the challenge.

## jsprog

Write some Javascript code!

Click [here](about:blank) to start the challenge.

## xss

Basic Cross-Site Scripting (XSS) challenge. The cookie monster is monitoring the page. Steal their cookies!

Click [here](about:blank) to start the challenge.

## csrf

Basic Cross-Site Request Forgery (CSRF) challenge. Try to trick the admin and grab the flag!

Click [here](about:blank) to start the challenge.

## sqli

SQL injection time! Break into the login page.

Click [here](about:blank) to start the challenge.

## searchbar

Another SQL injection challenge. See if you can grab the flag from the database.

Click [here](about:blank) to start the challenge.

## bsqli

Blind SQL injection. Find the `admin`'s password!

Click [here](about:blank) to start the challenge. For a hint, maybe consult the `strcmp` challenge?

*NOTE:* If you're using a programming language (like python) to solve the challenge, please also include the cookie `beamsplitter_bsqli` in your browser along with it. You can see the cookie in the Chrome developer tools.

## babylfi

Local File Inclusion! See what you can gather from the system.

Click [here](about:blank) to start the challenge. The stuff you learned from privilege escalation might help you identify important files on the system.

## lfirce

Can you take LFI vulnerabilities one step further and gain code execution? Your goal is to execute `/getflag`.

Click [here](about:blank) to start the challenge.

*NOTE:* If you're using curl to solve the challenge, please also include the cookie `beamsplitter_lfirce` in your browser along with it. You can see the cookie in the Chrome developer tools.

# Binary exploitation

## stringy

The flag is hidden in this program somewhere! Use a bit of GDB magic to find it!

## runme

The flag is hidden in this program somewhere! Use a bit of GDB magic to find it!

Hint: You don't have to reverse engineer too much for this challenge. If you're doing calculations or writing a program to automate stuff, there's an easier solution using GDB!

## trace

The flag is hidden in this program somewhere! Use a bit of GDB magic to find it!

Hint: You don't have to reverse engineer too much for this challenge. If you're doing calculations or writing a program to automate stuff, there's an easier solution using GDB!

## xmem

The flag is hidden in this program somewhere! Use a bit of GDB magic to find it!

Hint: You don't have to reverse engineer too much for this challenge. If you're doing calculations or writing a program to automate stuff, there's an easier solution using GDB!

## reveng

The flag is hidden in this program somewhere! You need to reverse engineer the program and figure out the flag!

## babybufov

Basic buffer overflow challenge! Can you trick the program into running the `target` function?

Connect to `twinpeaks.cs.ucdavis.edu` port `30005`.

*NOTE:* For consistent stack values, ALWAYS run the program using `./noaslr ./babybufov`, including in GDB!

## toddlerbufov

Can you trick the program into running the `target` function, with the right arguments that you want?

Connect to `twinpeaks.cs.ucdavis.edu` port `30006`.

*NOTE:* For consistent stack values, ALWAYS run the program using `./noaslr ./toddlerbufov`, including in GDB!

## babyrop

Time to do what you did earlier, but for 64-bit!

Connect to `twinpeaks.cs.ucdavis.edu` port `30007`.

*NOTE:* For consistent stack values, ALWAYS run the program using `./noaslr ./babyrop`, including in GDB!

*NOTE:* You can use ROPgadget in your solution, but you may NOT use the automatic ROPchain generator in ROPgadget to solve this challenge. In addition to getting the flag, you MUST also send me your exploit and a short explanation of how you solved it. This is to prevent you from using the generator and solving the challenge without understanding it.

## ropmelikeyoumeanit

Gain code execution.

Connect to `twinpeaks.cs.ucdavis.edu` port `30008`.

NOTE: For consistent stack values, run the program using `./noaslr ./ropmelikeyoumeanit`, including in GDB!

NOTE: You can use ROPgadget in your solution, but you may NOT use the automatic ROPchain generator in ROPgadget to solve this challenge. In addition to getting the flag, you MUST also send me your exploit and a short explanation of how you solved it. This is to prevent you from using the generator and solving the challenge without understanding it.

## shellcode

Write some shellcode!

Connect to `twinpeaks.cs.ucdavis.edu` port `30009`.

*Note:* I won't be talking about shellcoding in class. For more information, check out [Wikipedia](https://en.wikipedia.org/wiki/Shellcode). I also find [this online assembler](https://defuse.ca/online-x86-assembler.htm) useful when I'm writing custom shellcode, although you might not need it.

## guessme

Good luck guessing my secure random number!

Connect to `twinpeaks.cs.ucdavis.edu` port `30010`.

*Note:* I won't be talking about format string exploits in class. For more information, check out [Wikipedia](https://en.wikipedia.org/wiki/Uncontrolled_format_string).

## writeme

Try to change the `is_admin` variable.

Connect to `twinpeaks.cs.ucdavis.edu` port `30011`.

*Note:* I won't be talking about format string exploits in class. For more information, check out [Wikipedia](https://en.wikipedia.org/wiki/Uncontrolled_format_string).

## tinyuaf

A very small use-after-free challenge.

Connect to `twinpeaks.cs.ucdavis.edu` port `30012`.

*Note:* I won't be talking about use-after-free exploits, or anything heap related, in this course. If you're interested, you can read more about what a use-after-free is on [Wikipedia](https://en.wikipedia.org/wiki/Use_after_free), and [this YouTube video](https://youtu.be/ZHghwsTRyzQ) does a good job describing how it can be exploited.

Also, credit goes to [REDACTED] for developing this challenge!

## invtracker

Hack the inventory.

Connect to `twinpeaks.cs.ucdavis.edu` port `30013`.

*Note:* I won't be talking about use-after-free exploits, or anything heap related, in this course. You definitely need to understand use-after-free attacks for this challenge. Maybe check out the tinyuaf challenge first?

# Cryptography

## caesar

KIY{IR4551I_54R4J_4784J3J26779G0I8G68I63I5I19GJ1GI}

## substitution

I have a random substitution cipher applied to a file. Use some frequency analysis techniques to figure out the flag! Instructions on where to find the flag is in the first line of the plaintext.

## vigenere

The file is encrypted using a Vigenere cipher. Try to decrypt the file by guessing the key length and using frequency analysis. The instructions to get the flag is in the first line of the plaintext, similar to the substitution challenge.
Note: When encrypting the plaintext message, I'm ignoring nonalphabetic characters. As an example, if the key is "abc" and the plaintext is "hello world", I will match the key and plaintext as follows:

```
 PLAIN: hello world
   KEY: abcab cabca
CIPHER: hfnlp yosnd
```

## dhke

Pull off a Diffie-Hellman Key Exchange with the remote server using a plaintext protocol.

Connect to `twinpeaks.cs.ucdavis.edu` port `30014`.

## rsadec

I have a flag encrypted using an RSA public key. Here are the private key parameters.  and decrypt the flag.

Parameters:

N=`110267671414738970494525501170307930840512851744241760638602399682444271873453535741035734821975670983360359201501684238585962166901673721852027897764663364749008245038627577994373892745642468116144486422265242154930345472341761251401253398446958103175884730471353065769704142998448991521839595209975595991171`

p=`10620902203942110854782327308724124692152613609978162586044269224109610633179921111166522399215372792253474150369356436550953177866845014631090388398269007`

q=`10382137910450906133180463149192381475813941743104549056738098639376418806110725741879527046001514352813053329422714004528192986028060989196380147714733453`

e=`65537`

d=`78190323420140522709638663508957537910192917684031968207228446801692939904224067518461520494481794740966516819692483176458593371992227004621930214457778581725782854988217576940472487043648963799864293522067456094141075466803580056459381619186371345218888714204185098117889941610744968642615923804678756327745`

Ciphertext: `64171892671552669650359659097510303639095063899650328433874975581971710734592386612832097271678708850386299303484379587672600632994504984383014999506043075344157894649357802908461923685062167235503423692336794213532512243602361726121149758658149485954406473542634914664099945539530104467498960596261337361265`.

## rsarev

I have a RSA public key and a flag encrypted with it. Break the public key and decrypt the message. I heard that the key was generated using some shady generator that makes the two factors of N really close together.

Parameters:

N=`146745185726391139084096400279522914769034126910073992862537045006016968215020160588729425809027406529611283457391889656385480713622114674277628794458614336989450024119799162816931452269029631188507324650456425294283543581426990826256363156528336586201326849342518616158569900901184077743109203464951387585033`

e=`65537`

Ciphertext: `67499320416655058717301853648231936230077400733894242839882643282793194309912879223492728018278152327579605481088174283925221722887194350231255550369181054787763363223704783908006430560611053616648087787093258624987016758154959865246579709752028813105780605183910542830973628031842631849043652422444685655761`.

NOTE: For this challenge, if you're using a math library in Python, beware of floating point errors in `math`! Maybe check out the `decimal` library if you need to have higher precision.

## signing

I have made a signing algorithm based on RSA. Only one of the flags is signed by my private key. Can you find it?

To sign the key, I hashed the flag using SHA512, considered that as a big endian number and "decrypt" that number using my private key. The file is formatted like `FLAG signature_as_an_integer`. My N=`134159471276694609335468529984540213462174754066059581026665621949207962173095844364763109362700617771721453680389641691697424878717642030497684288785660499819910598840752820834085248385539154091771263251605651212407938795951114371523037452959409432753089566683862292804038755207477695524402887809448868860543`, and e=`65537`.

## authtoken

The developer of this application thinks they're being clever by using custom tokens to enhance security. Prove them wrong.

Connect to `twinpeaks.cs.ucdavis.edu` port `30015`.

# Final challenges

## finalprivesc

Our operatives have captured a member of the notorious criminal organiation, Redshift. We have extracted some credentials that's used by him to access one of Redshift's servers. Dig around and see what information you can find.

SSH into `finalprivesc@twinpeaks.cs.ucdavis.edu`, with password `REDACTED`.

## finalwebapp

Using the information you found via privilege escalation, you have found Redshift's internal webapp used for tracking their criminal activities. See if you can exploit it and see what their plans are.

Click [here](about:blank) to start the challenge.

## finalbinary

Oh no! How the heck do they have a missile armed and ready?! Quick, put a stop to this ASAP! They have exposed their missile control interface. Hack your way in and disable the missile!

Connect to `twinpeaks.cs.ucdavis.edu` port `30016`.

*NOTE:* The binary is not provided. This is intentional, and you need to leak the binary yourself as part of the challenge. Also, the binary is not being run with `noaslr`, but that shouldn't affect your exploit.

## finalcrypto

Phew, that was close! Redshift's plans are in shambles. However, we still don't know who's behind it all. We have found the following cryptic note which is used by Redshift to recruit people for their operations. Find the breadcrumbs and figure out who's the mastermind behind everything.

## thankyou

Thank you for taking ECS189M this quarter. I really hope you have learned something, and if you find this interesting, maybe consider going a bit deeper into computer security.

Also, thanks for bearing with me through this experimental course. I know the class is much harder than most other CS courses, the challenges might cause technical difficulties and a ton of frustration (especially the noaslr stuff), and my lectures are more like ramblethons, so thanks for staying here till the very end.

If you have time, please fill out this [feedback form](about:blank) so I know what went well and what didn't. You will get the flag for this challenge at the end of the feedback form.

Finally, I will make the source for all challenges public on [Github](https://github.com/rkevin-arch/ECS189M). The challenges for the class will be open source shortly after the quarter ends, and you're free to take a look at how everything works under the hood, or adapt it for your own purposes. The solutions won't be public, and I ask that you refrain from posting solutions publicly, in case we reuse the challenges in future ECS153 courses. If you're interested in learning the solution for a challenge, send me an email and I can explain more.

Thank you for a fantastic quarter, and I wish you good luck in your future careers.

-- rkevin
