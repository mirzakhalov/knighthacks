
class Analyzer():

    def __init__(self, essay):
        self.paper = ""
        with open(essay, 'r') as text:
            self.paper = text.read().replace('/n', '') # save the file as string into "self.essay"
    def data_structures(self):
            counter = 0
            glitch = 0
            ids = []
            username = []
            visibility = []
            birthday = []
            gender = []
            location = []
            status = []
            joined = []
            job = []
            language = []
            blogTraffic = []
            posts = []
            myComments = []
            userComments = []
            photos = []
            friends = []
            following = []
            followers = []
            points = []
            lastOnline = []
            for i in range(len(self.paper)):
                if((self.paper[i] == "|" and (len(ids) == len(lastOnline))) or (glitch == 1)):
                    ids.append(self.paper[counter:i])
                    glitch = 0
                    counter = i + 1
                elif(self.paper[i] == "|" and (len(username) == len(lastOnline))):
                    username.append(self.paper[counter:i])
                    counter = i + 1
                elif(self.paper[i] == "|" and (len(visibility) == len(lastOnline))):
                    visibility.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(birthday) == len(lastOnline))):
                    birthday.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(gender) == len(lastOnline))):
                    gender.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(location) == len(lastOnline))):
                    location.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(status) == len(lastOnline))):
                    status.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(joined) == len(lastOnline))):
                    joined.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(job) == len(lastOnline))):
                    job.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(language) == len(lastOnline))):
                    language.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(blogTraffic) == len(lastOnline))):
                    blogTraffic.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(posts) == len(lastOnline))):
                    posts.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(myComments) == len(lastOnline))):
                    myComments.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(userComments) == len(lastOnline))):
                    userComments.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(photos) == len(lastOnline))):
                    photos.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(friends) == len(lastOnline))):
                    friends.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(following) == len(lastOnline))):
                    following.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(followers) == len(lastOnline))):
                    followers.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|" and (len(points) == len(lastOnline))):
                    points.append(self.paper[counter:i])
                    counter = i + 1;
                elif(self.paper[i] == "|"):
                    lastOnline.append(self.paper[counter:i])
                    glitch = 1
                    counter = i + 1;
            return  {"ids": ids, "username": username, "visibility": visibility, "birthday": birthday, "gender": gender, "location": location, "status": status, "joined": joined, "job": job, "language": language, "blogTraffic": blogTraffic, "posts": posts, "myComments": myComments, "userComments": userComments, 
                    "photos": photos, "friends": friends, "following": following, "followers": followers, "points": points, "lastOnline": lastOnline}


                  
        