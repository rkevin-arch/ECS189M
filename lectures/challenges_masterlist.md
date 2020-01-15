## Challenge type explanation
|Type|Explanation|
|-|-|
|misc|No special server-side behavior/processing needed|
|xinetd(port)|The service runs on a port served by the xinetd container|
|sshable(ssh_password)|The service is a docker container intended to be SSH'd into. The SSH username is the same as the challenge.|
|web|The service is a docker container intended to be served via beamsplitter. The URL is {challengename}.webchal.twinpeaks.cs.ucdavis.edu, if everything goes well.|

## Status explanation
|Status|Explanation|
|-|-|
|Done|Full on 100% done|
|Tested|Tested on hadron, needs final deployment on twinpeaks
|Untested|Finished, needs testing|
|Changes needed|Mostly done, just a few changes left (i.e. write info.yml)|
|Waiting on downloadable|This challenge has a downloadable file, but I haven't implemented that feature in build.py yet|
|Waiting on beamsplitter|This challenge requires beamsplitter to work, but I haven't implemented beamsplitter integration to build.py yet|
|Needs porting over|Challenge has been done elsewhere (i.e. from a workshop), but needs to be converted over|
||I know what the challenge is going to be, but I haven't started yet|
|No idea|No idea what I'm going to put in the challenge yet. Discuss with professor and @aenygma|

## Scoring breakdown
|Category|Start time|End time|Points|Status|
|-|-|-|-|-|
|Linux and miscellaneous|Jan 6|Feb 2|1900|14/14 done|
|Webapp exploitation|Jan 25|Feb 16|1800|0/10 done|
|Binary exploitation|Feb 8|Mar 8|2600|0/14 done|
|Cryptography|Feb 24|Mar 15|1400|0/8 done|
|Final challenges|Mar 9|Mar 19|2500|0/4 done|
|TOTAL|10200|||0/50 done|
## Linux and miscellaneous
|Challenge|Points|Type|Status|
|-|-|-|-|
|introflag|50|misc|Done|
|linuxbasics|200|sshable(gusto_proofing_bully_equinox_deceiving)|Done|
|linuxadv|200|sshable(freeness_flame_revision_stylist_truth)|Done|
|loganalysis|200|sshable(amplifier_starting_unplowed_propose_aflame)|Done|
|nmap|75|xinetd(57129)|Done|
|nc|75|sshable(calamari_hefty_delegator_overrule_props)|Done|
|addition|100|xinetd(30001)|Done|
|binaryaddition|100|xinetd(30002)|Done|
|privesc1|100|sshable(tucking_bacteria_litter_cheek_scrutiny)|Done|
|privesc2|150|sshable(flier_blissful_gopher_scorn_modular)|Done|
|privesc3|100|sshable(correct_wick_blunt_democracy_rare)|Done|
|race|200|sshable(sterling_protector_overuse_spearmint_violet)|Done|
|strcmp|150|xinetd(30004)|Done|
|timingsc|200|xinetd(30003)|Done|
|TOTAL|1900||Done|

## Webapp exploitation
|Challenge|Points|Type|Status|
|-|-|-|-|
|adminme|75|web|adm|
|phpeval|100|web||
|jsprog|150|web|Note: Write function to do addition and alert(answer)|
|xss|250|web||
|csrf|250|web||
|sqli|125|web|Needs porting over|
|searchbar|175|web|Needs porting over|
|bsqli|250|web|Needs porting over|
|babylfi|125|web||
|lfirce|300|web|Needs porting over|
|TOTAL|1800||0/10 done|

## Binary exploitation
|Challenge|Points|Type|Status|
|-|-|-|-|
|strings|75|misc||
|runme|100|misc||
|ltrace|75|misc||
|xmem|125|misc||
|reveng|250|misc|Needs porting over|
|babybufov|250|xinetd(30005)|Needs porting over (4_x86_bufov_noargs)|
|toddlerbufov|250|xinetd(30006)|Needs porting over (6_x86_bufov_args_harder)|
|babyrop|300|xinetd(30007)|Needs porting over (2_x64_bufov_args)|
|ropmelikeyoumeanit|350|xinetd(30008)|Needs porting over (5_x64_ret2libc_harder_static)
|shellcode|150|xinetd(30009)||
|readme|100|xinetd(30010)|Changes needed|
|writeme|150|xinetd(30011)|Changes needed|
|tinyuaf|75|xinetd(30012)|Changes needed|
|invtracker|350|xinetd(30013)|Changes needed|
|TOTAL|2600||0/14 done|

## Cryptography
|Challenge|Points|Type|Status|
|-|-|-|-|
|caesar|50|misc||
|substitution|200|misc||
|vigenere|250|misc||
|aesdec|75|misc||
|dhke|150|xinetd(30014)||
|rsadec|125|misc||
|rsarev|200|misc||
|cbc2|350|xinetd(30016)||
|TOTAL|1400||0/8 done|

## Final challenges
|Challenge|Points|Type|Status|
|-|-|-|-|
|finalprivesc|500|sshable|No idea|
|finalwebapp|500|web|No idea|
|finalbinary|500|xinetd(30017)|No idea|
|finalcrypto|500|xinetd(30018)|No idea|
|writeup|500+partial credit|misc|Changes needed|
|TOTAL|2500||0/4 done|


