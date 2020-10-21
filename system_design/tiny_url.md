# Design a Tiny URL System

Think about these 3 things straight away

- API

  - How the user will interact with the system

    > create_tiny_url(long_url) -> tiny_ur(unique)

    > get_long_url(tiny_url) -> long_url

- Application Layer
- Persistence Layer
  - Where and How you would store the long/tiny url

## Q&A to ask to design the system

### What are the characters can we use to generate to tiny url to get an assumption about the length of our tiny url?

> a-z A-Z 0-9 => 62 in total

If our tiny url is 7 characters long then we can have 62^7 = 3.5 trillion

### How many new tiny we need to generate in seconds? Or it could be no of active users, from there you get an assumption of no of new tiny urls in seconds?

> Lets say 1000 new urls per second, then it would take 112 years to get all the unique tiny urls of lenght 7 or shorter

### Can a user set the tiny url?

### How to generate the tiny url?

- Generate random tiny url and check against DB. DB Schema will have a key, value pair where key is tiny url and value is longer url. Not a great solution.

  - Time consuming, parallel processing of multiple request can invalidate one or more tiny url.
  - Two same long url will have different tiny url, which means more memory heavy.

- Pick first 43 bits of MD5. first 43 bits cause, it takes 43 bits to generate all numbers upto 3.5 trillion. MD5 is a hashing function which generates 128 bit long hash, out of those you take a 43 bit then you'll use that for tiny url.

  - Same problem as above problem, need to check the authenicity of generated tiny url.
  - But this time two same long url will have same tiny url.

- Counter Based Approach
  - Single Host Approach: Only one host responsible for returning the tiny url.
    - Single point of failure, single point of bottleneck.
    - Sequential, which is time consuming.
  - All Host internally tries to maintain the counter
    - Divide the 3.5 trillion possiblities into range. You can divide in any ration, depending on the requirements. So now, every host will have its own unique range and maintain the counter on its own.
    - If a host terminates then we're only loosing a certain range of tiny urls, our service will still be up and running.
    - Scalable
    - To make it more secure, add some randomness.

### Is there any expiration period?

## How to scale?

- Get request must be faster than create request. For that you can use caching. Another way is CDN (Content Delivery Network). CDN is location specific server to make the request faster, it allows to get responses without going to the main server.

### This is simple design that I've made in miro

- [tiny url design in miro](https://miro.com/app/board/o9J_kiTa6Xw=/)
