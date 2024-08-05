<h1>Mac Address Changer</h1>


<h2>Description</h2>
This Python script is designed to change the MAC address of a specified network interface on a Linux system. It validates the provided MAC address and interface name, ensuring they are correctly formatted and exist on the system. The script includes enhanced error handling and requires root privileges to execute the necessary system commands. By using the ip command, it brings down the interface, changes its MAC address, and then brings the interface back up.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>Kali Linux</b>

<h2>Program walk-through:</h2>

<p align="center">
You first have to enter the interface you want to change the Mac address on: <br/>
<img src="https://imgur.com/cqfv6VQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
You now have to enter the Mac address you want the interface to change to:  <br/>
<img src="https://imgur.com/31obVRy.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sample output of a succesful Mac address change:  <br/>
<img src="https://imgur.com/zmN6CVe.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sample output of invalid inputs:  <br/>
<img src="https://imgur.com/jvO1aTi.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sample output of failed mac address change:  <br/>
<img src="https://imgur.com/pZE17uQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
