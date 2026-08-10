#Integer
likes = int(input("enter number of likes: " ))
followers = int(input("enter number of followers: "))
number_of_posts = int(input("enter number of posts: "))

#string
username = input("enter username: ")
post_title = input("enter post title: ")
description = input("enter description: ")

#list
posts = input("enter post names: ").split()

#tuple
width = int(input("enter width: "))
height = int(input("enter height: "))
dimensions = (width ,height)

#dictionary
user_profile = {

    "username" = username,
    "followers" = followers,
    "posts" = number_of_posts,
}

#set
interests = int(input("enter interests: ").split())

#output
print("\n pintrest user details: ")
print("username: " ,username)
print("post title: ",post title)
print("Description:", description)
print("followers: ", followers)
print("Number of Posts:", number_of_posts)
print("Posts:", posts)
print("Image Dimensions:", dimensions)
print("User Profile:", user_profile)
print("Interests:", interests)
