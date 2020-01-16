# Final linux
Our agents have captured a developer working in a criminal organization, and have fetched these files from his laptop. See if you can compromise the organization using it.
(give id_rsa file and known_hosts file pointing to finallinux@twinpeaks.cs.ucdavis.edu)
Once you're in, you are john@workstation. Have a note explaining the workstation is connected to the mainframe and their most important plans are stored there.
Look around, find admin@workstation's password in their home folder, escalate to admin (1/3)
Found a directory with a note explaining it is mounted on the mainframe as well, where you can submit jobs that will be run via cron
Execute a nc reverse shell on the mainframe, grab a shell there as admin (2/3)
Once you are admin@mainframe, you can run sudo as mastermind@mainframe, but only for the cp command. you can then cp /bin/bash with a suid bit (--preserve=all), then run it and get the flag. (3/3)

# Final webapp


# Final binary
Oh no! The criminal organization got their hands on a missile and are ready to launch it! Find a way to disable it quickly!
xinetd, run the program "main" (binary not distributed). It has a menu with several options.
One of the options is view changelogs, which prints out 
