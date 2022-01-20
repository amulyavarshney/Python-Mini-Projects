# Smart Door alert System
### DESCRIPTION
<p>When someone knocks on the door. A sudden change in frequency is picked up by KY-038 Sound Sensor moduleand it will be reflected by a digital HIGH and send this signal to the desktop over a <a href="https://en.wikipedia.org/wiki/WebSocket">websocket</a> via Raspberry Pi module as the server and the desktop as the client. The alert will be sent as a boolean value which when true indicates that someone knocked on the door and will alert by playing a 30-second audio clip which will clearly make the user aware that someone just knocked on the door.</p>

### TASKS
<ol>
  <li>Sound (knock) to Digital Output ✅</li>
  <li>Websockets
    <ol>
      <li>Client ✅</li>    
      <li>Server ✅</li>    
    </ol>
  </li>
  <li>Socket Communication ✅</li>
  <li>Hardware Setup ✅</li>  
</ol>

### Working Prototype:
> Close up of the sound sensor (RaspPi4)
![close-up](image.jpg)
