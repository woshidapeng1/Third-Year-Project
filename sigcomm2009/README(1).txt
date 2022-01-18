=========================
== Dataset Description ==
=========================


============
Dataset
============

One-word name : sigcomm2009
Institution: Technicolor

Short: 
-------

Traces of Bluetooth encounters, opportunistic messaging, and social profiles of 76 users of MobiClique application at SIGCOMM 2009.

Longer summary:
--------------

The trace contains data collected by an opportunistic mobile social application, MobiClique. The application was used by 76 persons during SIGCOMM 2009 conference in Barcelona, Spain. The data sets include traces of Bluetooth device proximity, opportunistic message creation and dissemination, and the social profiles (friends and interests) of the participants.

Date start: 2009-08-17
Date end: 2009-08-21

Authors: Anna-Kaisa Pietilainen, Christophe Diot
Email: annakaisa.pietilainen@gmail.com
Web: http://www.thlab.net

BibTex:
-------

@inproceedings{pietilainen09mobiclique,
  author = {A-K Pietil"{a}inen and E. Oliver and J. LeBrun and G. Varghese and C. Diot},
  title = {MobiClique: Middleware for Mobile Social Networking},
  booktitle = {WOSN'09: Proceedings of ACM SIGCOMM Workshop on Online Social Networks},
  year = {2009},
  month = {August},
}

@inproceedings{pietilainen12temporal,
  author = {A-K Pietil"{a}inen and C. Diot},
  title = {Dissemination in Opportunistic Social Networks: The Role of Temporal Communities},
  booktitle = {MobiHoc'12: Proceedings of the 13th International Symposium on Mobile Ad Hoc Networking and Computing},
  year = {2012},
  month = {June},
}

Keywords: Bluetooth, DTN, social network
Measurement Purposes: User Mobility Characterization, Routing Protocol for DTNs, Social Network Analysis, Human Behavior Modeling, Opportunistic Connectivity
Network type: bluetooth, DTN, social network

Non-tech description:
---------------------

The data set was collected during at the SIGCOMM 2009 conference at Barcelona, Spain. 

Around 100 smartphones were distributed to a set of volunteers during the first two days of the conference. The participants were recruited on-site in conjunction of the conference registration. 

Each device was initialized with the social profile of the participant that included some basic information such as home city, country and affiliation. In addition, each participant was asked to log on to their Facebook profile in order to include the list of Facebook friends and interests in the social profile. The participants could edit the social profile before it was uploaded on the device and recorded in our traces. 

Each participant was instructed to keep the device with them and powered on at all times, and to use the MobiClique application for mobile social networking during the conference. The participants could also use the device as their personal mobile phone during the conference by installing their personal SIM card on it.

The final trace contains data from 76 devices that show significant activity during the experiment.

Network configuration:
---------------------

The network is a Bluetooth based opportunistic network created among the participating devices during the conference.

Each device performs a periodic Bluetooth device discovery every 120+/-10.24 seconds for a duration of 10.24s to find out about nearby devices. Upon discovering new contacts, the devices form a RFCOMM link on a preconfigured channel for data communications. Both the Bluetooth name query and service discovery are disabled.

The experimental hardware is an HTC s620 Windows Mobile smartphone. HTC s620 has a 200MHz TI processor, 64MB of RAM, 128MB of ROM and a MicroSD slot. The radio interfaces include a quad-band GSM/EDGE cellular radio, Bluetooth v1.2 and 802.11b/g. The Bluetooth radio is a class 2 device with a radio range of around 10-20 meters.

Collection:
-----------
Each device records the results of the periodic device discovery and all data communications (RFCOMM link setup and bytes send/received). In addition, the devices record details of the user's social profile and its evolution, and application level messaging. All traces are recorded constantly in text files on the device's SD memory card.

All traces are timestamped based on the device clock and reported as a relative time in seconds since the start of the experiment, 17/08/2009 08:00. The device clocks are set manually to the same reference time at the beginning of the experiment.

Sanitization:
------------

All sensitive identifiers including Facebook identifiers, social profile data and Bluetooth MAC addresses are replaced with random integer ids.

Limitations:
------------

The social profiles, in particular the list of friends and interest groups, are not necessarily complete as the participants had a possibility to remove any details they wished before the data was uploaded on the device and recorded. This option was given for privacy reasons as the application shared all profile details with all nodes.

The Bluetooth proximity data and RFCOMM data communications suffer from the known limitations of the Bluetooth technology. The device discovery process is slow and regularly misses some nearby devices and RFCOMM links (setup and transmission) fail often when there are many Bluetooth devices in range.

The timestamps among different devices are not synchronized. The clocks are set manually to the same reference time at the beginning of the experiment, but there is significant clock drift visible in the final data. The traces can be synchronized based on mutual sightings and/or data transmission traces.

Due to constantly running periodic Bluetooth device discovery and frequent data communications, the battery life of the devices was limited to about one day or less depending on other usage. Hence, the devices are active and collecting data during varying periods of time depending on how faithfully (or not) the device owner was charging the device.



============
Traceset 1
============

Name: MobiClique

Other details are identical with the dataset description.

============
Trace 1
============

Name: participants
Short description: List of participants and basic social profiles

Summary: List of participants and basic social profile including home city, country and affiliation.

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: user_id;key;value

The user_ids run from 1 to 76 (inclusive). Each user carries a single device that is identified by the same user_id. The 'key' is one of ['institute','city','country'] and the values are anonymized to simple integer ids.

Setup: 

This data was asked from the user when he joined the experiment and was also part of the users public social profile during the experiment (together with his real name that we do not disclose here for privacy reasons).

============
Trace 2
============

Name: interests1
Short description: The initial interest groups of the participants.

Summary: List of initial interest groups of the participants based on their Facebook groups and networks. The list contains also three pre-configured common groups for each participants (ids 1,2,3).

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: user_id;group_id

Setup: 

The MobiClique application adds three common interest groups for everybody (group_id=[1,2,3]). In addition, we use a simple Facebook desktop application to get the list of Facebook groups and networks for each participant to initialize his profile. While each participant logged on to their Facebook account for the initial configuration, they had the possibility to remove any details they wished before the application was run for the first time and the data was recorded in our trace file. Hence, the initial interest list does not necessarily contain the full list of Facebook groups of each participant.

============
Trace 3
============

Name: friends1
Short description: The initial friendship graph of the participants.

Summary: List of friends of the participants based on their Facebook friends.

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: user_id;friend_user_id

The trace only includes links among the participating users.

Setup: 

We use a simple Facebook desktop application to get the list of Facebook friends for each participant to initialize his profile. While each participant logged on to their Facebook account for the initial configuration, they had the possibility to remove any details they wished before the application was run for the first time and the data was recorded in our trace file. Hence, the initial friendship graph does not necessarily contain the full list of Facebook friends of each participant and the relationships may be asymmetric.

============
Trace 4
============

Name: interests2
Short description: The evolution of interest groups.

Summary: The MobiClique application lets users to discover and join existing interest groups, and create new interest groups at any time. Hence, the interest lists are changing over time.

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: user_id;group_id;timestamp

The group_ids < 1000 correspond to the initial interest groups and group_ids >= 1000 are new adhoc groups created during the experiment. The timestamp is the relative time in seconds since the start of the experiment, 17/08/2009 08:00.

Setup: 

The trace is based on the MobiClique application usage on each device.

============
Trace 5
============

Name: friends2
Short description: The evolution of the friendship graph.

Summary: Similarly to the interest groups, the MobiClique application lets users to discover and friend other MobiClique users upon opportunistic encounters with them. Hence, the friendship graph is changing over time.

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: user_id;friend_user_id;timestamp

The timestamp is the relative time in seconds since the start of the experiment, 17/08/2009 08:00.

Setup: 

The trace is based on the MobiClique application usage on each device.

============
Trace 6
============

Name: activity
Short description: The activity periods of each participant and device

Summary: A device is active when its collecting data. The inactivity periods occur due to batteries running out, at night time when the device is turned off,and due to some software problems.

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: user_id;start;end

The start and end timestamps are the relative times in seconds since the start of the experiment, 17/08/2009 08:00.

Setup: 

The trace is calculated based on the periodic device discovery logs.

============
Trace 7
============

Name: proximity
Short description: The Bluetooth device discovery logs.

Summary: The trace records all the nearby Bluetooth devices reported by the periodic Bluetooth device discoveries.

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: timestamp;user_id;seen_user_id;seen_device_major_cod;seen_device_minor_cod

The timestamp is the relative time in seconds since the start of the experiment, 17/08/2009 08:00. The user_ids below 100 are the experimental devices, user_ids >= 100 are external Bluetooth devices seen during the experiment. The device_major_cod and device_minor_cod correspond to the device's standard Bluetooth Class of Device values.

Note, that Bluetooth device discovery (and thus the trace) is asymmetric, i.e., a device A may see device B at some point in time but not the other way around.

Setup: 

Each device performs a periodic Bluetooth device discovery every 120 +/- 10.24 seconds (randomized) for 10.24 seconds. Both the Bluetooth name and service queries are disabled to speed up the discovery process.

============
Trace 8
============

Name: messages
Short description: User-generated messages

Summary: This file lists the application level messages created by the users during the experiment. MobiClique allowed messaging between friends or among members of an interest group. In addition, MobiClique contained an epidemic voting application that allowed users to give rankings (1 to 5 stars) to the talks of the conference and see the real time results on their device.

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: msg_id;src_user_id;created;type;dst

Each message has an unique msg_id (used in the message transmission traces). The messages are either unicast (type=U), multicast (type=M), or broadcast (type=B) messages.

The destination ('dst' field) for unicast messages is another user. These messages are either delivered directly to the destination upon an encounter or forwarded to the friends of the the destination.

The multicast messages are targeted to an interest group ('dst' is an interest group id). These messages are forwarded only to the members of the destination group.

The broadcast messages (empty dst) are created by an epidemic voting application. As each vote requires only few bytes of data, the application aggregates them in a single broadcast message that contains all the votes given and/or received by the device at any time. For this reason, in the transmission log we do not detail the message id for the broadcast messages.

The creation timestamp is the relative time in seconds since the start of the experiment, 17/08/2009 08:00. This is the time when the message is inserted to the MobiClique network queue, however, the actual sending takes place asynchronously upon encountering suitable target devices.

Setup: 

The trace is based on the MobiClique application usage on each device.

============
Trace 9
============

Name: transmission
Short description: Message transmission logs

Summary: The data transmission protocol logs from the sender side. Data is transmitted between two devices using Bluetooth RFCOMM protocol on a fixed channel (no service discovery required).


Date start: 2009-08-17
Date end: 2009-08-21

Format: 

csv: type;msg_id;bytes;hop_src_user_id;hop_dst_user_id;src_timestamp;status

There are three types of protocol data units: 1=handshake (exchange of user profiles at contact start), 2=unicast or multicast message, 3=broadcast message.

The handshake takes place upon every new encounter to exchange the social profiles and message Bloomfilters between the two nodes. The unicast and multicast msg_ids match the msg_id in the messages trace. The handshake and broadcast msg_ids are set to -1. 

The bytes field indicates the size of the message in bytes. The timestamp is the time at the sender and the status codes are 0 for success; 1 for failure. The timestamp is the relative time in seconds since the start of the experiment, 17/08/2009 08:00.

Setup: 

The trace is based on the MobiClique application operation on each device.



============
Trace 10
============

Name: reception
Short description: Message reception logs

Summary: The data transmission protocol logs from the receiver side. Data is transmitted between two devices using Bluetooth RFCOMM protocol on a fixed channel (no service discovery required).

Date start: 2009-08-17
Date end: 2009-08-21

Format: 

The format is identical to the transmission trace, except all the timestamps are on the receiving device's time.

Setup: 

The trace is based on the MobiClique application operation on each device.

