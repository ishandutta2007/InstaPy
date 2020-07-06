""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


photo_comments = [
    "Nice shot! @{}",
    "I love your profile! @{}",
    "Your feed is an inspiration :thumbsup:",
    "Just incredible :open_mouth:",
    "What camera did you use @{}?",
    "Love your posts @{}",
    "Looks awesome @{}",
    "Getting inspired by you @{}",
    ":raised_hands: Yes!",
    "I can feel your passion @{} :muscle:",
]

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy()

with smart_run(session):
    # general settings
    session.comments = photo_comments
    session.join_pods(topic="sports", engagement_mode="normal")
