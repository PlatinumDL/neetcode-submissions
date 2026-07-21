class Twitter:

    def __init__(self):
        self.tweets = {} #User Id to tweets [] heapified #At most 10 largest
        self.follows = {} #User Id to follows []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        if self.tweets.get(userId) == None:
            self.tweets[userId] = [(self.time,tweetId)]
        else:
            self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        #Retrieve everybody the user follows
        followsPeople = self.follows.get(userId, [])
        userTweets = self.tweets.get(userId,[])
        newArr = []
        newArr.extend(userTweets)

        #For each person the user follows, retrieve their list and extend it onto the list. Now, i have an array containing ALL the tweets that user follows
        for following in followsPeople:
            followingTweets = self.tweets.get(following,[])
            newArr.extend(followingTweets)

        heapq.heapify(newArr)
        
        outputArr = []
        #Get top 10 and append to output arr
        counter = 0
        while newArr and counter < 10:
            time, tweetId = heapq.heappop(newArr)
            outputArr.append(tweetId)
            counter += 1

        return outputArr

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return #Cant follow urself lol

        #If already followed, return
        if self.follows.get(followerId) is None:
            self.follows[followerId] = [followeeId]
        else:
            followerArr = self.follows.get(followerId,[])
            if followeeId in followerArr:
                return
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        followerArr = self.follows.get(followerId,[])
        if followeeId in followerArr:
            self.follows.get(followerId).remove(followeeId) #Remove followeeId


