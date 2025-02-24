# Azure VM with Sentinel - Personal SIEM/Home SOC

After some hands-on work through various learning paths, virtual internships and to satisfy my own insatiable curiosity, I built out my own test SIEM with a custom rule, set to detect succesful logins via RDP (which was intentionally left open for testing purposes). Thanks to the free $200 credit for new Azure accounts, this project even worked out to be the best kind of cheap... Free! 


## Creating the VM

The first step after getting started on Azure was, of course, to create a relatively simple Windows 10 Pro VM. I created an aptly named resource group and proceeded to aptly name the VM itself, then changed the default region (which was inexplicably set to South Africa) to the much more geographically convenient East US. Not pictured, but in the Networking tab I ensured we had open access to RDP via port 3389 - incredibly irresponsible under most circumstances, but perfect for our current purpose.

[Azure VM Creation](Azure VM Creation.png)

## Sentinel/Log Analytics Workspace & Set Up 

Next up was setting up Sentinel itself. I continued with my apt naming trend.

[Sentinel Creation](Azure Sentinel Creation.png)

After this, I installed the Windows Security Events Data Connector via the Content Hub. We need this Data Connector because although our VM is likely logging events as it should, we want to be able to pull them from the endpoint and view them in our new Sentinel SIEM.

[Sentinel WinAMA](Azure WinSecEvents AMA.png)

Once that's installed, we want to set up the Data Collection Rule. (Azure really loves some Personal Pronouns!) That ended up looking something like this, with me selecting the only available VM on the Resources tab.

[Sentinel DCR](Azure Data Collection Rule AMA.png)

We wait a few minutes (and grab the Uber Eats order, inhale some slices of pizza, crack open an energy drink...) at this point, and then verify that logs are being collected upon our return - success!

[Logs Collected](Azure Log Received DCR.png)

Now that we're receiving logs from our VM, we want to create a useful detection rule. Since an RDP access alert is probably the single most ubiquitous, obvious and important rule imaginable and we've configured a vulnerability to it, we set up the following - keeping in mind that we don't want to see system accounts and only want to see successful sign-ins.

[Rule Logic](Rule Logic Full 2.png)

We create a new, high severity scheduled rule with that logic, setting it to alert us if incidents are greater than 0 (meaning any and all), and to run it every 5 minutes with that same 5 minutes of data. Sentinel also has beta ATT&CK integration, so we categorize it as [TA0001 - Initial Access](https://attack.mitre.org/tactics/TA0001/).

## Testing it out!

Now we get to check our work! I RDP into the VM and sign-in with the previously created administrator credentials. I hang around for a bit, then turn the VM off and wait 5 minutes before checking our SIEM Incidents...

[Incident Logged](Azure Incident Logged.png)

Aha! I caught myself red-handed! So it looks like everything worked out, and the test run was successful - I'll now return to the real world, and immediately cut off RDP exposure for my VM.

[RDP DENY](Azure RDP 3389 Deny.png)

A quick switch from 'Allow' to 'Deny' in the port rules should do the trick. With that, we wrap up this very basic but very useful experiment! This is just the tip of the iceberg, and I'll definitely be back to do more with this setup in the near future - I'll probably have it on a separate page linked from the index. Thanks for reading!


