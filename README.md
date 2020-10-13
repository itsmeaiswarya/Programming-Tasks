# General Skillls

## 2warm -
converting 42 in   decimal   to binary dividing 42 by 2 everytime untill to give result

& noting down the remainders in reverse orderuntill final result be zero.

  - ans: picoCTF{101010}
## Let's warm up -
converting a word starting with 0x70(hexa decimal) to ASCII using an online tool conver

ted hexadecimal to ASCII

  - ans: picoCTF{p}
## Warmed up - 
converting 0x3D(hexadecimal) to decimal 3 & D is 3 & 13(since A=10,B=11,C=12,D=13) so, 

'D' is the one's position so multiply 'D' value with 16 power 0, i.e 1 and add it to'3'

 in 10's place multiplied with 16 power 1, more clearly  (3*16)+(13*1)

  - ans: picoCTF{61}
## Bases - 
given a text convert it using bases converter using an online tool to base 64 output in

ASCII source

  - ans: picoCTF{I3arn_th3_r0p35}
## First Grep - 
finding flag in a file opened the file with pycharm and thus found the flag in the code.

  - ans: picoCTF{grep_is_good_to_find_things_eda8911c}
## Resources - 
opening link & finding file opening the resource link directing to picoctf resource page,

thus flag found.

  - ans: picoCTF{r3source_pag3_f1ag}
  
# Web Exploitation

## Insp3ct0r -
link given & we are asked to inspect it open the link, a web page appears, right click &

choose inspect. Then view the sources &  you will find 1/3 of the flag in (index) html code,

then open mycss.css & you will find 2/3 of the flag at end of program as commands in css code,

& finally open myjs.js & you will find 3/3 of the flag as command at the end in javascript.

  - ans: picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?8a7e3144}
## dont_use_client_side - 
opening super secure portal open link then in the web page right click & open 'view source page'

option & then you will see password split into 8 parts,combine them in order. Verify by entering 

it & it says verified. Thus flag found.

  - ans: picoCTF{no_clients_plz_90ff34}
## logon - 
login using a username & password, you will be directed to a page saying no flag for you, inspect

the page.Go to storage then cookies, change the assigned admin values from false to true.Now refresh

the page & receive flag.

  - ans: picoCTF{th3_c0nsp1racy_l1v3s_6f2c20e9}

# Forensic

## unzip - 
a link is given open it,extract it in winrar seen unzipped.

  - ans: picoCTF{unz1pp1ng_1s_3a5y}

# Reverse engineering 

## vault_door_training -
open the source code for training vault. Then reading the code we find the flag.

  - ans: picoCTF{w4rm1ng_Up_w1tH_jAv4_ca5ae7fcc95}
## vault_door_1 -
open the source code for the vault door it contains an array with 0 to 31 indices,

each when arranged in order we receive the flag.

  - ans: picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_9d038f}
  
# Cryptography

## the numbers -
open the numbers file and you find numbers starting from 16 after 7 places from there

there is '{' which indicates the format 'picoCTF{' , so 'p' is in 16th position of

alphabets so arrange other numbers respective to their alphabets.Also in caps.

  - ans: PICOCTF{THENUMBERSMASON}
## 13 -
using ROT13 decode the encoded string. ROT13 is were first 13 alphabets arranged in a

row with next 13 in next row below the before ones respectively.Now decode.

  - ans: picoCTF{not_too_bad_of_a_problem}
## Easy1 -
solve using vignere cipher with the help of the table given along with key and encryption.

  - ans: picoCTF{CRYPTOISFUN}
## Caesar -
solve using caesar cipher i.e move every encrypted alphabet 3 times forward & note the next

alphabet.It gives the complete flag.

  - ans: picoCTF{crossingtherubiconvrtezsxl}
## Flags -
given a file containing maritime flags which represent each letter of alphabets, decode it.

  - ans:PICOCTF{F1AG5AND5TUFF}
  

  
  
  
