import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class Visualize():

    def __init__(self, data):
        self.pd_username = pd.DataFrame(data["username"], columns = ["Name"])
        self.pd_visibility = pd.DataFrame(data["visibility"], columns = ["Visibility"])
        self.pd_birthday = pd.DataFrame(data["birthday"], columns = ["Birthday"])
        self.pd_gender = pd.DataFrame(data["gender"], columns = ["Gender"]).replace("nan", "Not Specified").astype(str)
        self.pd_location = pd.DataFrame(data["location"], columns = ["Location"]).replace("nan", "").astype(str)
        self.pd_status = pd.DataFrame(data["status"], columns = ["Status"])
        self.pd_joined = pd.DataFrame(data["joined"], columns = ["Joined"])
        self.pd_job = pd.DataFrame(data["job"], columns = ["Job"])
        self.pd_language = pd.DataFrame(data["language"], columns = ["Language"])
        self.pd_blogTraffic = pd.DataFrame(data["blogTraffic"], columns = ["BlogTraffic"])
        self.pd_posts = (pd.DataFrame(data["posts"], columns = ["Posts"])).replace("nan", 0).astype(int)
        self.pd_myComments = pd.DataFrame(data["myComments"], columns = ["MyComments"])
        self.pd_userComments = pd.DataFrame(data["userComments"], columns = ["UserComments"])
        self.pd_photos = pd.DataFrame(data["photos"], columns = ["Photos"]).replace("nan", 0).astype(int)
        self.pd_friends = pd.DataFrame(data["friends"], columns = ["Friends"]).replace("nan", 0).astype(int)
        self.pd_following = pd.DataFrame(data["following"], columns = ["Following"]).replace("nan", 0).astype(int)
        self.pd_followers = pd.DataFrame(data["followers"], columns = ["Followers"]).replace("nan", 0).astype(int)
        self.pd_points = pd.DataFrame(data["points"], columns = ["Points"]).replace("nan", 0).astype(int)
        self.pd_lastOnline = pd.DataFrame(data["lastOnline"], columns = ["LastOnline"])
        self.pd_data = self.pd_username.join(self.pd_visibility)
        self.pd_data = self.pd_data.join(self.pd_birthday)
        self.pd_data = self.pd_data.join(self.pd_gender)
        self.pd_data = self.pd_data.join(self.pd_location)
        self.pd_data = self.pd_data.join(self.pd_status)
        self.pd_data = self.pd_data.join(self.pd_job)
        self.pd_data = self.pd_data.join(self.pd_language)
        self.pd_data = self.pd_data.join(self.pd_blogTraffic)
        self.pd_data = self.pd_data.join(self.pd_posts)
        self.pd_data = self.pd_data.join(self.pd_myComments)
        self.pd_data = self.pd_data.join(self.pd_userComments)
        self.pd_data = self.pd_data.join(self.pd_photos)
        self.pd_data = self.pd_data.join(self.pd_friends)
        self.pd_data = self.pd_data.join(self.pd_following)
        self.pd_data = self.pd_data.join(self.pd_followers)
        self.pd_data = self.pd_data.join(self.pd_points)
        self.pd_data = self.pd_data.join(self.pd_lastOnline)
        
             
    def genderStats(self):
        males = len(self.pd_data.loc[self.pd_data["Gender"].str.contains("Male", na=False)])
        females = len(self.pd_data.loc[self.pd_data["Gender"].str.contains("Female", na=False)])
        notSpecified = len(self.pd_data.loc[self.pd_data["Gender"].str.contains("Not Specified", na=False)])
        return males, females, notSpecified
        
    def genderVSposts(self):
        male_posts = 0
        female_posts = 0
        notspecified_posts = 0
        for i in range(26811):
            if(self.pd_data["Gender"][i] == "Male"):
                male_posts = male_posts + self.pd_data["Posts"][i]
            elif(self.pd_data["Gender"][i] == "Female"):
                female_posts = female_posts + self.pd_data["Posts"][i]
            elif(self.pd_data["Gender"][i] == "Not Specified"):
                notspecified_posts = notspecified_posts + self.pd_data["Posts"][i]
        return male_posts, female_posts, notspecified_posts

    def location(self):
        #print self.pd_data["Location"].value_counts()
        location = self.pd_data["Location"].str.lower()
        writer = pd.ExcelWriter('output.xlsx')
        location.value_counts().to_excel(writer,'Sheet1')
        writer.save()
    
    def pointsVSlocation(self):
        points_sorted = self.pd_data["Points"].sort_values(ascending = False)
        places = []

    def jobVSposts(self):
        job_lower = self.pd_data["Job"].str.lower()
        print job_lower.value_counts() 
    
           
