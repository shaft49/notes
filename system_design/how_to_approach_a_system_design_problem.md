- [Tutorial Link](https://towardsdatascience.com/system-design-101-b8f15162ef7c)

## Step 1: Requirements Clarification

We need to clarify the goal of the system. Focus on the main featires that you are trying to design. Divide requirements into two categories.

- Functional Requirement
  - What would be system input and what is the output it should be cleared in these requirements.
- Non functional requirement
  - Performance, modifiability, availability, scalability, reliability, etc. are important quality requirements in system design. These `ilities` are what we need to analyze for a system and determine if our system is designed properly

## Step 2: Estimation of Important Parts

- One of the important points of the system design is to know about the scale of the system.
- Another important estimation is about storage.
- Network bandwidth usage is also an important factor. In the case of distributed systems, bandwidth usage management is crucial. For example, if you want to efficiently handle file transfer, you may need to divide a file into chunks.
  ![](https://miro.medium.com/max/1400/1*apFPTrQrwlPR8DX7Gr-lOw.jpeg)
  <center>Fig: Transfer only the updated chunk only</center>

## Step 3: Data Flow

- We need to define the system’s data model and how data will flow between different system components.
- Database system selection is part of this section. NoSQL or SQL database selection is a common scenario.

## Step 4: High-level Component design

- Try to draw a block diagram representing the core components of our system in 5–6 parts. It can be more if the system is too big.

- The File Processing Server will manage the file processing Workflow. Metadata Server will take care of the info of file, chunk size, and user information. The Notification server will let the client application know about updating files to all the other devices the client is logged in. Cloud Storage will keep the file stored.
  ![](https://miro.medium.com/max/2000/1*a8pNOY6V7FETtF2waFhfaw.jpeg)
  <center> Fig: High Level Design of Google Drive </center>

## Step 5: Detailed design

- In this step, we can analyze different approaches to solve a problem, their pros and cons, and explain why we prefer one approach over the other. Tradeoff analysis is an important part of this section.

![](https://miro.medium.com/max/2000/1*K1M2D2oC6MhoDhWXARRsGA.jpeg)

<center> Fig: System Design of Google Drive </center>

## Step 6: Identify bottlenecks and resolve them

- Now, we have a detailed design of the system. We have to find the bottlenecks of the system and find different ways to mitigate them. (Data duplication, backup server)
