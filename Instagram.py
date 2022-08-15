import instaloader

class Instagram:

    def __init__(self, username):
        self.username = username
        self.loader = instaloader.Instaloader()
        self.loader.load_session_from_file(self.username)
        self.profile = instaloader.Profile.from_username(self.loader.context,self.username)
        open('followers.txt', 'w').close()
        open('following.txt', 'w').close()
        open('not_following_back.txt', 'w').close()


    def login(self):
        return self.loader.load_session_from_file(self.username)

    def getFollowers(self):
        for followers in self.profile.get_followers():
            with open("followers.txt","a+") as f:
                f.write(followers.username+'\n')
        
        print("Writing followers...")


    def getFollowing(self):
        for followees in self.profile.get_followees():
            with open("following.txt","a+") as f:
                f.write(followees.username+'\n')

        print("Writing followees...")

    def getNotFollowingBack(self):
        followers = [follower.username for follower in self.profile.get_followers()]
        following = [followee.username for followee in self.profile.get_followees()]
        notFollowingBack = [nfb for nfb in following if nfb not in followers]

        for nfb in notFollowingBack:
            with open("not_following_back.txt","a+") as f:
                f.write(nfb+'\n')

        print("Writing not following back...")
            

        
        
        



