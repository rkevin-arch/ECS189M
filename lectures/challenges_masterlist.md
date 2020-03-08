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
|Webapp exploitation|Jan 26|Feb 17|1700|10/10 done|
|Binary exploitation|Feb 9|Mar 9|2650|14/14 done|
|Cryptography|Feb 24|Mar 15|1450|8/8 done|
|Final challenges|Mar 9|Mar 19|2300+500|3/5 done|
|TOTAL|10500|||49/51 done|
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
|adminme|75|web|Done|
|phpeval|100|web|Done|
|jsprog|125|web|Done|
|xss|200|web|Done|
|csrf|200|web|Done|
|sqli|125|web|Done|
|searchbar|225|web|Done|
|bsqli|250|web|Done|
|babylfi|100|web|Done|
|lfirce|300|web|Done|
|TOTAL|1700||10/10 done|

## Binary exploitation
|Challenge|Points|Type|Status|
|-|-|-|-|
|stringy|75|misc|Done|
|runme|100|misc|Done|
|trace|100|misc|Done|
|xmem|125|misc|Done|
|reveng|250|misc|Done|
|babybufov|250|xinetd(30005)|Done|
|toddlerbufov|250|xinetd(30006)|Done|
|babyrop|300|xinetd(30007)|Done|
|ropmelikeyoumeanit|350|xinetd(30008)|Done|
|shellcode|150|xinetd(30009)|Done|
|guess|100|xinetd(30010)|Done|
|writeme|150|xinetd(30011)|Done|
|tinyuaf|100|xinetd(30012)|Done|
|invtracker|350|xinetd(30013)|Done|
|TOTAL|2650||14/14 done|

## Cryptography
|Challenge|Points|Type|Status|
|-|-|-|-|
|caesar|75|misc|Done|
|substitution|275|misc|Done|
|vigenere|250|misc|Done|
|dhke|200|xinetd(30014)|Done|
|rsadec|125|misc|Done|
|rsarev|200|misc|Done|
|signing|175|misc|Done|
|tokenize|150|xinetd(30015)|Done|
|TOTAL|1450||8/8 done|

## Final challenges
|Challenge|Points|Type|Status|
|-|-|-|-|
|finalprivesc|550|sshable|Done|
|finalwebapp|550|web|Working on|
|finalbinary|550|xinetd(30016)|Done|
|finalcrypto|550|xinetd(30017)|Done|
|thankyou|100|misc|Working on feedback form|
|writeup|500+partial credit|misc|Working on rubric|
|TOTAL|2300||3/5 done|
