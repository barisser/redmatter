##Node Lifecycle

###Responding to Requests
####Requests for Neighbors
      - Expected JSON
        "neighborhash": string
####Requests for Data
      - Expected JSON
        "filehash": string

        Returns
        "data": string, "nexthash": string, "neighbor": string
        Gives data and next hash, as well as nearest known neighbor to that hash, if applicable.

        OR
        "neighbor": "some_hash_here", state: "known" || "unknown"

        If no data present, gives nearest known neighbor.  If unknown, returns random neighbor.

  - Requests for Directions to Neighbors with Data

####Monitoring the Network
  - Determine if Files are Hosted:
    - With the necessary redundancy
    - By the Neighbors who are expected to be hosting certain files

###Threats
  - Sybil Attacks
      Huge numbers of false nodes reporting false data
  - Spamming Attack
      There must be some cost to adding data
  - Baiting
      It must not be rational to constantly offer hosting, receive bitcoins, and then turn off.

###Solutions
  - Money flows as an informational signal
    - Send bitcoins to honest nodes
  - Nodes are ranked by trustworthiness
    - Being Trustworthy is either
     - Being upvoted by other nodes (scaling with their trustworthiness)
     - Sending bitcoins to other honest nodes

##Guarding
Each node is a 'guardian'.  It tells you where to go to find the next file/neighbor.  But it also reports on its knowledge about the trustworthiness of others.  This means
      - did they host the files they said they would host over the requisite amount of time
      - are they consistently lying / how much do i agree with them on everything.
      

##Hosting
Each node may host files: a tuneable amount of data of course.

##The ask-for-hosting cycle
- start with a file, convert it deterministically to the right hash
- send out "who should host this?" request.  Request reverberates until nodes who cant find nearest neighbors offer to host.  Originator gets a list of nodes who should host.  List will be too long.  Originator picks short list based on minimizing distance between node hashes and the file's hash.
- 
