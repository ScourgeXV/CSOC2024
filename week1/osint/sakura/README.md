TryHackMe Sakura Room



1. Tip Off

Background - The OSINT Dojo recently found themselves the victim of a cyber attack. It seems that there is no major damage, and there does not appear to be any other significant indicators of compromise on any of our systems. However during forensic analysis our admins found an image left behind by the cybercriminals. Perhaps it contains some clues that could allow us to determine who the attackers were? 

Instructions - Images can contain a treasure trove of information, both on the surface as well as embedded within the file itself. You might find information such as when a photo was created, what software was used, author and copyright information, as well as other metadata significant to an investigation. In order to answer the following question, you will need to thoroughly analyze the image found by the OSINT Dojo administrators in order to obtain basic information on the attacker.

Solution - We are given an svg image file. Upon looking the xml code of the image we can see that the image is being exported to the home diretory of a user named SakuraSnowAngelAiko. Therefore the username is SakuraSnowAngelAiko.

Ussername - SakuraSnowAngelAiko



2. Reconnaissance

Background - It appears that our attacker made a fatal mistake in their operational security. They seem to have reused their username across other social media platforms as well. This should make it far easier for us to gather additional information on them by locating their other social media accounts.

Instructions - Most digital platforms have some sort of username field. Many people become attached to their usernames, and may therefore use it across a number of platforms, making it easy to find other accounts owned by the same person when the username is unique enough. This can be especially helpful on platforms such as on job hunting sites where a user is more likely to provide real information about themselves, such as their full name or location information.
A quick search on a reputable search engine can help find matching usernames on other platforms, and there are also a large number of specialty tools that exist for that very same purpose. Keep in mind, that sometimes a platform will not show up in either the search engine results or in the specialized username searches due to false negatives. In some cases you need to manually check the site yourself to be 100% positive if the account exists or not. In order to answer the following questions, use the attacker's username found in Task 2 to expand the OSINT investigation onto other platforms in order to gather additional identifying information on the attacker. Be wary of any false positives!

Solution - Upon searching the username we found above (SakuraSnowAngelAiko) on Google we found a account on few websites like X, Github, Linkedin etc. Upon looking the twitter profile we can see him introducing himself as Aiko Abe. On looking to the github profile we found a repo named PGP having a PGP public key. When this public key is decoded using base64 se get some weird text but in between we can see an email id. Thus we get the Email id as SakuraSnowAngel83@protonmail.com

Email - SakuraSnowAngel83@protonmail.com

Real Name - Aiko Abe 



3. Unveil 

Background - It seems the cybercriminal is aware that we are on to them. As we were investigating into their Github account we observed indicators that the account owner had already begun editing and deleting information in order to throw us off their trail. It is likely that they were removing this information because it contained some sort of data that would add to our investigation. Perhaps there is a way to retrieve the original information that they provided? 

Instructions - On some platforms, the edited or removed content may be unrecoverable unless the page was cached or archived on another platform. However, other platforms may possess built-in functionality to view the history of edits, deletions, or insertions. When available this audit history allows investigators to locate information that was once included, possibly by mistake or oversight, and then removed by the user. Such content is often quite valuable in the course of an investigation. In order to answer the below questions, you will need to perform a deeper dive into the attacker's Github account for any additional information that may have been altered or removed. You will then utilize this information to trace some of the attacker's cryptocurrency transactions.

Solution - In the github profile of cybercriminal we can see a repository named ETH. Inside this repository we can see miningscript folder having an ethwallet but it is not the actual id. However we can checkout the previous commit and see the actual ethwallet of the person. This gives us the cryptocurrency that is Ethereum, and cryptocurrency wallet address. Now we see his transactions using the website etherscan. This tells his minninng pool as Ethereum on the given date and his other excahnge cryptocurrency as Tether

Cryptocurrency - Ethereum

Wallet ID - 0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef

Mining pool on January 23, 2021 UTC - Ethermine

Other Cryptocurrency exchanged - Tether



4. Taunt 

Background - Just as we thought, the cybercriminal is fully aware that we are gathering information about them after their attack. They were even so brazen as to message the OSINT Dojo on Twitter and taunt us for our efforts. The Twitter account which they used appears to use a different username than what we were previously tracking, maybe there is some additional information we can locate to get an idea of where they are heading to next?

Instruction - Although many users share their username across different platforms, it isn't uncommon for users to also have alternative accounts that they keep entirely separate, such as for investigations, trolling, or just as a way to separate their personal and public lives. These alternative accounts might contain information not seen in their other accounts, and should also be investigated thoroughly. In order to answer the following questions, you will need to view the screenshot of the message sent by the attacker to the OSINT Dojo on Twitter and use it to locate additional information on the attacker's Twitter account. You will then need to follow the leads from the Twitter account to the Dark Web and other platforms in order to discover additional information.

Solution - We already found the twitter account on google. Inside the twitter account we can see a screenshot of website where all the wifi passwords are saved. On searching this screenshot we get the website in the deep web. Hence we get the URL. On this site we get the list of passwords. From this we take the Home WiFi and search BSSID of this name. On searching we get a website wigle and we enter the name in it to get the BSSID. 

Twitter - SakuraLoverAiko

URL - http://deepv2w7p33xa4pwxzwi2ps4j62gfxpyp44ezjbmpttxz3owlsp4ljid.onion

BSSID - 84:AF:EC:34:FC:F8



5. Homebound 

Background - Based on their tweets, it appears our cybercriminal is indeed heading home as they claimed. Their Twitter account seems to have plenty of photos which should allow us to piece together their route back home. If we follow the trail of breadcrumbs they left behind, we should be able to track their movements from one location to the next back all the way to their final destination. Once we can identify their final stops, we can identify which law enforcement organization we should forward our findings to.

Instructions - In OSINT, there is oftentimes no "smoking gun" that points to a clear and definitive answer. Instead, an OSINT analyst must learn to synthesize multiple pieces of intelligence in order to make a conclusion of what is likely, unlikely, or possible. By leveraging all available data, an analyst can make more informed decisions and perhaps even minimize the size of data gaps. In order to answer the following questions, use the information collected from the attacker's Twitter account, as well as information obtained from previous parts of the investigation to track the attacker back to the place they call home.

Solution - We can see the image of sakura tree in twitter. In the background of thsi image we can see Washington Monument. Thus we need to search for airport nearest to Washington Monument which is Ronald Reagan Washington Airport. Next we are given an image of layover airport. When we search this image using Google lens we can easily see many news articles in English as well as in Japanese about Sakura lounge in Haneda Airport in Tokyo. On opening the Google maps we can easily locate Japan and the lake in th mainland that is Lake Inawashiro. We already know the home city of this person because in WiFi password list we have city passsword which mentions about Hirosaki city.

Airport - DCA

Layover - HND

Lake - Lake Inawashiro

City - Hirosaki

