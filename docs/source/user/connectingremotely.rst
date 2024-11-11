Connecting while off-campus
===========================

If you are looking to connect to DMOG from off-campus you will need to use the SSH gateway (SSHGW) as a proxy/jump host.

If you have not already been given access to the SSHGW please create a ticket with the helpdesk to request this.

Set your client to use sshw.hw.ac.uk as a proxy/jump host, and to connect to it on port 44788

If you are looking to use VSCode or MobaXterm (see above) in this way, you'll need to make some adjustments:

VSCode
------

In your SSH config file, change the host DMOG section to match the following (changing the values in the [ ] to your own):

.. code-block:: bash

   Host dmog
     User [username]
     IdentityFile [PATH TO YOUR DMOG SSH PRIV KEY]
     HostName dmog.hw.ac.uk
     Port 22
     ProxyJump [username]@sshgw.hw.ac.uk:44788
     ConnectTimeout 60
     ServerAliveInterval 30
     ServerAliveCountMax 120

MobaXTerm
---------

Right-click the session on the left, then select Edit Session.

In the window that appears, change "Remote Host" from dmog.hw.ac.uk to 137.195.249.10

Then, select Network Settings, then click 'SSH gateway (jump host)'

In the new window that appears enter the following:

Gatway host: ``sshgw.hw.ac.uk``

Username: ``your HWU username``

Port: ``44788``

Click OK, then OK again. 

You should now be able to connect to DMOG via the SSHGW
