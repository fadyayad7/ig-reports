from dotenv import dotenv_values
from Instagram import Instagram

username = dotenv_values(".env").get('username')

instagram = Instagram(username)
instagram.login()

instagram.getFollowers()
instagram.getFollowing()
instagram.getNotFollowingBack()

