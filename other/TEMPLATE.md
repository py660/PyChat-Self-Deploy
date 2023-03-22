# HTML BLOCK TEMPLATES
### User / Chatroom Card
```html
<li class="active"> <!-- active class is optional -->
<div class="d-flex bd-highlight">
<div class="img_cont">
<img src="https://js-game.python660.repl.co/dynamic/view.php?1" class="rounded-circle user_img">
<span class="online_icon"></span> <!-- Optional "offline" class -->
</div>
<!-- User/Chatroom Info Section -->
    <div class="user_info">
    <span>Khalid</span>
    <p>Kalid is online</p>
    </div>
</div>
</li>
```
---
### User / Chatroom Title Section
```html
<div class="d-flex bd-highlight">
<div class="img_cont">
<img src="https://js-game.python660.repl.co/dynamic/view.php?6" class="rounded-circle user_img">
<span class="online_icon"></span> <!-- Optional "offline" class -->
</div>
<div class="user_info">
<span>Chat with Khalid</span>
<p>1767 Messages</p>
</div>
<!--div class="video_cam">
<span><i class="fas fa-video"></i></span>
<span><i class="fas fa-phone"></i></span>
</div-->
</div>
```
---
### This User Message
```html
<div class="d-flex justify-content-end mb-4">
<div class="msg_cotainer_send">
Hi Khalid i am good tnx how about you?
<span class="msg_time_send">8:55 AM, Today</span>
</div>
<div class="img_cont_msg">
<img src="https://js-game.python660.repl.co/dynamic/view.php?8" class="rounded-circle user_img_msg">
</div>
</div>
```
---
### Other User Message
```html

<div class="d-flex justify-content-start mb-4">
<div class="img_cont_msg">
<img src="https://js-game.python660.repl.co/dynamic/view.php?7" class="rounded-circle user_img_msg">
</div>
<div class="msg_cotainer">
Hi, how are you samim?
<span class="msg_time">8:40 AM, Today</span>
</div>
</div>
```