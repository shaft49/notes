# System Design

## **ABCD** of System Design

- **ASK** Good Questions to build MVP
  - What feasures to work on
  - How much to scale
- Don't use **BUZZWORDS**
- **CLEAR** and organized thinking
- **DRIVE** discussion with 80:20 rule, 80% of the time you'll talk and rest of the time the interviewer will talk.

## Proceed in this order in an interview

1. Features
1. Define API
1. Availability
1. Latency Performance
1. Scalability
1. Durability: Data is stored securely in a database.
1. Class Diagram: for LLD
1. Security & Privacy: Depends on the Question
1. Cost Effective: Discuss Pros & Cons with other solution

## Knowledge you need to know before you appear in a system design interview

> You should learn more, probably in details. Here are only a summary is given.

- **Vertical vs Horizontal Scaling**: Add more resource to existing host vs add more host

- **CAP Theorem**: You can only achieve two out of three. And partition tolerance is a must as you drop network package. RDBMS choose consistency over availabilty. NoSQL prefer availabilty.

  - Consistency: Read will have most recent write
  - Availability: Request will get response, might be most recent write or might not
  - Partition Tolerance: Between two nodes you could be dropping package

- ACID vs BASE:ACID is used in RDBMS while BASE is used in NoSQL database.
  - Atomicity: A operation will not in half complete state
  - Consistency: DB will consistent after a operation
  - Isolation: Paraller operation on database
  - Durabilty: Will store data incase of any hazard
  ***
  - Basicly Available: system does guarantee availability
  - Soft State: system may change over time, even without input. This is because of the eventual consistency model.
  - Eventual Consistency: system will become consistent over time, given that the system doesn't receive input during that time.
- **Partitioning or Sharding the data**: Sharde or partition millions of data to store efficiently.

  - Consistent Hashing: Techniques for sharding

- **Optimistic vs Pessimistic Locking**: Lock resources to complete a transaction. Varies when the locking is happening.
- **Strong vs Eventual Consistency**: Strong is used in RDBMS, while eventual is used in NoSQL
- **RDBMS vs NoSQL**
  - Types of NoSQL:
    - Key Value Pair
    - Wide Column
    - Document Based: XML, JSON
    - Graph Based
- **Caching**: Speed up the read time
  - Two types of caching:
    - Every Nodes does its own caching
    - Distributed Caching: Cached Data is shared between nodes
- **Data Center / Racks / Hosts**: Need to know latency time for internal DC/racks/host communication. Whate happens if an internal dc/racks/host goes down.
- **CPU / Memory / Harddrive / Network Bandwith**: Keep in mind these are Limited resources.
- **Random vs Sequential Read & Write on Disk**: Random is slow, Sequential is fast.
- **HTTP vs HTTP2 vs Web Sockets**
- **TCP / IP Model**: Four layers in tcp/ip models.
- **IPv4 vs IPv6**: IPv4 has 32 bit address, while ipv6 has 128 bit address.
- **TCP vs UDP**: TCP is reliable connection while UDP is unreliable connection but fast.
- **DNS Lookup**: Domain Name Server, when you hit a url in browser, the request goes to DNS and it look for the url'r ip address ans returns response.
- **HTTPS vs TLS**: iF TLS is used with HTTP then it preety becomes HTTPS
- **Public Key Infrastructure and Certificate Authority**: When you hit a url in https you'll get a public key as response and certificate wuthority will tell you whether it comes from the intended site or not.
- **Symmetric vs Asymmetric Encryption**: Asymmetric is more computationally expensive than symmetric
- **Load Balancer**: Sits infront of a service (server) and distribute the client request to nodes.
- **CDNs and Edge**: Stream something from a Content Delivery Network close to you rather than a Data Center. Edge is you do processing close to the client.
- **Bloom Filters and Count Min Sketch (Data Structures)**: Bloom Filter is a DS which decides whether an element is member of a set or not. Count Min Sketch Take care of frequency of events.
- **Paxos** Consensus over Distributed Systems
  - leader election of a distributed systems
- **Design Patterns and OOP**
- **Virtual Machines and Containers**
- **Publisher Subscriber over a Queue**: Publisher publishes a message in queue and subscriber receives a message in queue.
- **Map Reduce**: Distributed and parallel processing of data. Important for big data field.
- **Multi Threading / Concurrency / Locks / CAS**

---

## Knowledge about tools

- **Cassandra**: Wide Column, highly scalable database. it uses consistent hashing to sharde your data.
- **MongoDB/CouchBase**: Provide ACID properties and best for json format.
- **MySQL**: Master/Slave Architecture
- **Memcached**: Distributed Cache,key value storage
- **Redis**: Distributed Cache,key value storage but also does lot of other things, more availabity and data replication.
- **Zookeeper**: Centralized configure management tool, scale very well for reads but does not scale very well for writes.
- **Kafka**: Fault Tolerant highly available queue used in publisher subscriber or streaming applications.
- **NGINX**: A single instance can handle thousand of clients.
- **HAProxy**
- **Solr and Elastic Search**: Highly available, scalable, fault tolerant search platfor. Provide full text search.
- **BlobStore**: Amazon S3 is a example of blobstore.
- **Docker**: Software platform providing containers inside which you can develop and run your distributed applications.
  - Kubernetes, Mesus are tools to manage and coordinate this container
- **Hadoop, Spark**: Hadoop use map reduce. Spark is faster version Hadoop.
  - HDFS: Java based fault tolerant system. Hadoop depends on HDFS

## The Plan

### 1. Basics

- [x] [Jackson Gabbard Intro to Architecture and System Design Interview](https://www.youtube.com/watch?v=ZgdS0EUmn70)
  - Talks about what to expect in a system interview.
  - Don't have any specific correct answer for system design. Interviewer will not provide all the information. You need to break down the problem by asking questions.
  - Get start with the parts that you're more familiar with then move onto the remaining parts and describe your assumptions.
  - Don't get scared or intimidated about how crazy these problems sound. Turn the big crazy numbers into a reasonable numbers. Suppose there are 500m active users of an app but that doesn't mean all of them uses the app at the same time. Convert it into a rough numbers of concurrent users which might be 50k or less. 50k is preety reasoanble number.
  - Challenge of the interview is refine, refine and refine to go broad and dive deep .
  - Try to help the interviewer to help you. Keep yourself engaged.
  - If you're not in a company who builds system for millions of users then learn the details of architecture of those who does.
  - If you get rejected it means you were at least at the front door of that place. just keep going

### 2. See Videos on Real Life Examples

- [Tushar Roy Youtube](https://www.youtube.com/playlist?list=PLrmLmBdmIlps7GJJWW9I7N0P0rB0C3eY2)

  - Talks about `TinyURL`, `messenger`, `TypeAhead`, `Distributed Database`

- [Gaurav Sen System Design](https://www.youtube.com/watch?v=xpDnVSmNFX0&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX)

- [Success in Tech Youtube](https://www.youtube.com/playlist?list=PLA8lYuzFlBqAy6dkZHj5VxUAaqr4vwrka)

### 3.

- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Grokking System Design](https://www.educative.io/courses/grokking-the-system-design-interview)
- [Systems Expert](algoexpert.io/systems/product)
- [Grokking System Design - Drive Link](https://drive.google.com/drive/folders/1Ui2Bm_eyiF3-IUO2kA2qXIKFqMLPDHaN?fbclid=IwAR2jGy50-muxjZjj-AUzgU3qNLzmCk25UIc_J_3_lgZBVnWLrXcgkM4wEfU)
- [Grokking System Design Youtube](https://www.youtube.com/playlist?list=PLkQkbY7JNJuC99VDJcpQdww-4aT3QhdJv)
- [System Design Course](https://www.hiredintech.com/courses/system-design?fbclid=IwAR27ic3qIpHC3yYC6iUqaZHy8xDKZIVczcDNbQqG7VS3njMhC4L4Dh6CYs4)
- [InterviewBit System Design Section](https://www.interviewbit.com/courses/system-design/topics/storage-scalability/?fbclid=IwAR24P7SxWbu3WPaucgRADITWxOtrsYpqO3eE8PMkkUeIHPVoaR1WxWuw4Gg)
- [High Scalabilty Website](http://highscalability.com/)
- [CS75 Scalability Slides]()
- [Drawing Tools](https://sketchboard.me/)

## Examples

- [Distributed Systesm for Stream Processing](https://www.youtube.com/watch?v=y3gQDXn4x7o&feature=share&fbclid=IwAR3bQLdrPHzgoIByyhlUsKSAjWJDu3IW8Xb0IFts-zr5IzetQYbwkxMoxjY)
- [Instagram](https://www.youtube.com/watch?v=hnpzNAPiC0E&fbclid=IwAR3BNu4ad6beluW2sfpKFHLNq5nSNPgGYN4zoZ5veumKN60iUog57p9f-dk)
- [Facebook Live Videos](https://www.youtube.com/watch?v=IO4teCbHvZw)
- [Netflix Push Message](https://www.youtube.com/watch?v=6w6E_B55p0E)
- [Dropbox](https://www.youtube.com/watch?v=PE4gwstWhmc&fbclid=IwAR1G1HM_snUl9jPH1etB9t5-9OjU_QY4Cg9mgFP6kQYleqvMSQJysFQcH3M)
