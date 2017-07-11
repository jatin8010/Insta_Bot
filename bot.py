import requests ,urllib


APP_ACCESS_TOKEN = '5688449444.909a40a.5ffe8de011994ffba98b210c34b0ac5f'
# api access token for username = mriu.test.08

# use username = mriu.test.08

BASE_URL = 'https://api.instagram.com/v1/'
# base url used for instagram.com

def self_info():
# self information defined
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'
#retrieval of self information

def get_user_id(insta_username):
# defining user id
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

# retrieval of user id using username
def get_user_info(insta_username):
#defining user information
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'
# retrieving the information of user by username

def get_own_post():
#defining own post
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    print own_media
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
         image_name = own_media['data'][0]['id'] + '.jpeg'
         image_url = own_media['data'][0]['images']['standard_resolution']['url']
         urllib.urlretrieve(image_url, image_name)
         print 'Your image has been downloaded!'
        else:
           print 'Post does not exist!'
    else:
     print 'Status code other than 200 received!'

# infomation about the downloading of image of own

def get_user_post(insta_username):
#defining user post
     user_id = get_user_id(insta_username)
     if user_id == None:
        print 'User does not exist!'
        exit()
     request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
     print 'GET request url : %s' % (request_url)
     user_media = requests.get(request_url).json()

     if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
     else:
        print 'Status code other than 200 received!'
# information about the downloading of image of user by username

def get_post_id(insta_username):
# defining post id
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
# invalid username gives USER DOES NOT EXIST
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()
#getting post id by username

def like_a_post(insta_username):
# defining like_a_post function
    media_id = get_post_id(insta_username)
# media id is specific and different key assigned to every image
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'
# hitting like on post by usernam

def post_a_comment(insta_username):
#defining post_a_comment
    media_id = get_post_id(insta_username)
    print media_id
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"
# commenting on a post

def geo_fencing(insta_username):
# defining geo_fencing
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    Id = user_media['data'][0]['location']['id']
    Name = user_media['data'][0]['location']['name']
    Longitude = user_media['data'][0]['location']['longitude']
    Latitude = user_media['data'][0]['location']['latitude']
    request_url = (BASE_URL + 'locations/%s/media/recent?access_token=%s') % (Id, APP_ACCESS_TOKEN)
    print "Request url:%s" % (request_url)
    access_media = requests.get(request_url).json()
    print access_media
    i = 0
    k = 0
    length =0
    if access_media['meta']['code'] == 200:
        if len(access_media['data']):

            insta_tag = access_media['data'][0]['tags']
            if len(insta_tag) > 0:
                for x in range(0, insta_tag.__len__()):
                    if insta_tag[x] == 'flood':
                        print 'Flood Region'
                    elif insta_tag[x] == 'earthquake':
                        print 'Earthquake Region'
                    else:
                        print 'Not matched'
            else:
                print 'No hash tag'
                exit()
        else:
            print "No image found of calamity"
            i -= 0
    else:
        print "No media found in the mentioned location"
# gives the regional discription  about a particular region shown in an image
# tells the location of region on globe

def start_bot():
# starting the bot
    while True:
        print '\n'
        print 'Hey! Welcome to Insta_Bot!'
        print 'Here are your menu options:'
        print "1.Get your own details\n"
        print "2.Get details of another user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get the recent post of a user by username\n"
        print "5.Like the recent post of a user\n"
        print "6.Comment on the recent post of a user\n"
        print "7.For geo fencing\n"
        print "9.Exit"
# various print functions
        choice=raw_input("Enter you choice: ")
        if choice=="1":
            self_info()
        elif choice=="2":
            insta_username = raw_input("Enter the username: ")
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "5":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice == "6":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
        elif choice == "7":
            insta_username = raw_input("Enter the username of the user: ")
            geo_fencing(insta_username)
        elif choice=="9":
            exit()
        else:
            print "incorrect choice"
# select the above mentioned choices to perform the desired task
start_bot()



