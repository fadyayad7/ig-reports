following = []
with open('following.txt') as following:
    following = following.readlines()

followers = []
with open('followers.txt') as followers:
    followers = followers.readlines()

notFollowingBack = [nfb for nfb in following if nfb not in followers]

for nfb in notFollowingBack:
    with open("not_following_back.txt","a+") as f:
        f.write(nfb+'\n')

print("Writing not following back...")