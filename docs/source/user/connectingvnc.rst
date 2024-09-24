Connecting to DMOG using VNC
============================

Before following the process below, this guide assumes you have an account on the cluster. 
If that is not the case, you can request one by contacting ISHelp@hw.ac.uk

You will first need to connect to DMOG via SSH as you normally would.

There are a few desktop environments available to use, you can see these with the following command:

.. code-block:: bash
  
   flight desktop avail

You should see an output similar to this:

.. code-block:: bash
  
   ┌───────┬────────────────────────────────────────────────────────────────────────────────────────────── ───────────┐
   │ Name  │ Summary                                                                                                  │
   ├───────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────┤
   │ gnome │ GNOME v3, a free and open-source desktop environment for Unix-like operating systems.                    │
   │       │  > https://www.gnome.org/                                                                                |
   │ kde   │ KDE Plasma Desktop (KDE 4). Plasma is KDE's desktop environment. Simple by default, powerful when needed.│
   │       │  > https://kde.org/                                                                                      │
   │ xfce  │ Xfce is a lightweight desktop environment for UNIX-like operating systems. It aims to be fast.           │
   │       │ user friendly.                                                                                           │
   │       │  > https://xfce.org/                                                                                     │
   └───────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────┘

To start a session with your chosen desktop environment:

.. code-block:: bash

   flight desktop start gnome

You should see an output similar to this:

.. code-block:: bash

   == Session details ==
      Name:
      Identity: dda965c2-500d-4469-9eee-e51da4b26104
      Type: gnome
      Host IP: 137.195.249.10
      Hostname: login1
      Port: 5903
      Display: :3
      Password: GhoddOv4
      Geometry: 1024x768

   This desktop session is not directly accessible from outside of your
   cluster as it is running on a machine that only provides internal
   cluster access.  In order to access your desktop session you will need
   to perform port forwarding using 'ssh'.

   Refer to 'flight desktop show dda965c2' for more details.

On the last line, run the command shown. In my example this would be

.. code-block:: bash

   flight desktop show dda965c2

This will print the same information again, but with some key info added. Specifically, this will show the command you will need to use to connect to the VNC session:

.. code-block:: bash

   This desktop session is not directly accessible from outside of your
   cluster as it is running on a machine that only provides internal
   cluster access.  In order to access your desktop session you will need
   to perform port forwarding using 'ssh':

   ssh -L 5903:137.195.249.10:5903 gp27@dmog.hw.ac.uk

(please note that this command assumes you are connecting to DMOG from on-campus or via the VPN. If you can't connect to DMOG using just simple 'ssh dmog.hw.ac.uk' the above command won't work.

Run this command on your local machine. Then switch over to your VNC client and connect to, in my example, localhost:5903. You will be prompted to enter a password, enter the password shown on DMOG.
   
