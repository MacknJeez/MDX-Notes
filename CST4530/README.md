# A summary of all the lectures 
## Lecture 1: Fundamentals of Security

The CIA Triad,
NIST Definition of Computer Security,
Computer Security Challenges,
Security Concepts & Relationships,
X.800,
Security Design Decision,
Attack Surface,
Conflict between security and ease of use,
Dimensions of Computer Security,
Design decisions.

## Lecture 2: Understanding Frameworks

Difference between a reference model and an implementation model,
A Security Reference Framework is about the functions needed to do CIA,
A Security Implementation Framework depends on what you are trying to protect,
The Firesmith Framework - gold standard,
Identification and Authentication,
User authentication,
Attacks on passwords,
Using salt to enhance password hashing,
Single Sign-on,
Multifactor Authentication,
Something you are,
Something you have,
Something you know,
Biometric authentication.

## Lecture 3-4: Access Control

Access Control components,
Subject, Object, Access Right, Reference Monitor,
Access Control Matrix,
Access Control List (ACL),
Capabilities,
Access Control on OS,
Reference Monitor, Kernel, and TCB,
Linux Security,
Concepts of groups and protection domains,
Supports the concept of a security kernel,
Read, Write, Execute,
Access Control Types,
DAC, MAC, RBAC, ABAC,
Key Principle of Least Privilege,
Identity and Credential Management,
The rise and rise of virtualization.


## Lectures 5 - Capabilities

Definition of capability,
Capabilities provide AAA,
Basic Capability Types,
Hardware and Software,
Hardware uses,
Capability Register and Segment Capability,
Software capabilities are digital tokens,
Uses a particular format,
Problems with Capabilities,
Casual tampering and revocation,
HASH and RANDOM Fields of the new capability format,
SYS_FIELD,
Application of Capabilities to Hospital Environment.


## Lectures 6 & 7: Unix Security

Keep patches up-to-date,
Apply Basic OS hardening principles,
Linux Hardening,
Check specific programs that make the system vulnerable: e.g. The X Window System,
Disabling Accounts and Services,
Effective Password Policies,
File Security based on RWE bits,
Linux DAC Model,
Subject/Object/Kernel,
Linux DAC – file based,
Users/Group/Owner,
SUID, GUID, Sticky Bit,
Umask,
Rootkits: the intruder tries to become root,
Detecting Rootkits,
Iptables.


## Lecture 8: Windows Security

Security Account Manager (SAM),
Security Identifiers,
Identifies principals and groups,
Hardening Principles for Windows,
Device Protection,
Threat Resistance,
Identity Protection,
Information Protection,
Breach detection investigation and response,
Kernel protection,
Memory Protection,
Windows Firewall,
Browser Protection Mechanisms,
Windows Browser Protection.


## Lecture 9: Security Mechanisms for DE

Applied Security,
RADIUS,
NAT,
Firewalls,
SSL,
TLS,
IPSec,
VPNs.


## Lecture 10: Security Models: Part 1

The BLP Model,
No read up,
No write down,
Prevents data from leaking through the bottom,
Carla and Dirk Example,
Sometimes, you may need to temporarily change someone’s role.,
Limitations of BLP,
Difficult to downgrade objects,
Does not stop covert channels.

## Lecture 11: Security Models: Part 2

The BIBA model,
No Write Up,
No Read Down,
This approach protects high-quality data,
Clark-Wilson Model,
Concerned about data integrity,
Objects or data can only be changed by programs, not users,
Chinese Wall Model,
Prevents conflict of interest issues,
Must prevent attackers from attacking lower layers of the framework.


## Lecture 13: Database Security

What is an RDBMS,
Properties of a Database,
Atomicity, consistency, isolation, durability (ACID),
Database Design Goals (functionality),
SQL, Data Integrity, Transactions, ACID,
SQLI – injection attack using SQL,
In-band, inferential, out-of-band,
Database Security Options,
Access Control, Privilege Management,
Encryption and Auditing.


## Lecture 14: Software Security

Need for Software Security,
Common Faults in Software,
Web Application Security Issues,
Memory Security Issues,
Prevention Methods,
Validating Input, Compiler Options, Output encoding, Access Control,
Use of software capabilities,
Use of Scope and SRPC.


## Lecture 15: Transport Level and Internet Security

Encryption,
MIME,
DKIM, SPF, and DMARC,
SSL/TLS,
IPSec,
New Cloud Storage Framework,
Application to mHealth,
Advanced Digital Platforms (ADIMEP).


## Lecture 16: Transport Level and Internet Security

Physical Security Threats,
Environmental, Technical, Man-made,
Environmental Threats,
Tornadoes, Hurricanes, Floods, Earthquakes, Lightning,
Impacts of Temperature, Humidity and Dust,
Technical Threats,
Electrical Power and EMI,
Man-made and Physical Threats,
Unauthorized access, theft, vandalism and misuse.


## Lecture 17: Blockchain - Part 1

Blockchain is about blocks and chains,
Provides immutability of blocks,
Non-repudiation of transactions,
Blockchain needs a P2P network,
Need to decide which node should next add a block to the chain,
PoW, PoS, DPoS,
Miners get coins for their work,
Blockchain Framework Layers,
Consensus, Mining, Propagation, Semantic and Application.


## Lecture 18: Blockchain – Part 2

Application of Blockchain,
Finance, legal, healthcare,
Cryptocurrency,
Replacing the financial system,
Bitcoin, Ethereum, Dogecoin, etc,
Digital Wallets,
Crypto-Exchanges,
Non-Fungible Tokens,
Might be the killer app for Blockchain.


## Lecture 19: New Security Frameworks: Part 1

Perimeter Defence,
Uses NAT, SSL/TLS, IPSec, VPN,
Issues of this approach,
Evolved rather than designed,
Protects data; not users,
Puts filters in data path – affects performance,
Y-Comm Architecture,
Security designed from the start,
Targeted Security Models,
Connection TSM,
Ring-based TSM,
Vertical Handover TSM.


## Lecture 20: New Security Frameworks: Part 2

Zero Trust Networks,
Every device, user, and network flow must be authenticated,
Uses a control plane as well as a data plane,
Only enforcement is in the data path; everything else is done in the control plane,
Zero Trust Threat Model: tighter than the Internet Threat Model,
New concepts,
Network Agent, Trust Engine,
Zero Trust Authorization System.


## Lecture 21: Cybersecurity and Society

Data Hierarchy,
Data, Information, Knowledge, Decision Making,
Relationships between different security frameworks,
Threats,
Cybercrime, cyber harassment, cyberbullying, cyber surveillance,
Understanding Cyber Targets,
Anatomy of an attack,
Risk Analysis and Management,
Recovery Plan.
