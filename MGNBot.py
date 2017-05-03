#!/usr/bin/python
import praw
import time

Noob = ('help', 'first grow', 'newbie', 'noob', 'question', 'questions');	#Newbie Questions
Noob_Info = 'Have you checked the [sidebar](https://www.reddit.com/r/microgrowery/wiki/config/sidebar) \
			It is full of all sorts of helpful Information'

Sex = ('male', 'males', 'male?', 'males?', 'female', 'females','female?', 'females?',\
		'sex', 'sex?', 'sexing', 'sexing?', 'male/female', 'male/female?');	#Sex questions
Sex_Info = 'Sex can be determined once the plant starts to receive less than 14 hours of light per day, in the "pre-flower" stage. If your plant \
		is still in seedling or vegetative phase (>14 hours of light per day) you may see early sex indicators, but wait till pre-flower is \
		triggered to be sure.\
		Males will develop little ball-shaped pollen sacs, while females will develop pointy, teardrop-shaped growths that extrude fuzzy white \
		hairs called "pistils". Some plants may show signs of both sexes, we call these "hermaphrodites", or "hermies". \
		Here is a [Quiz](https://docs.google.com/forms/d/e/1FAIpQLSc1v779jfbU1-AmDcw0u09BCS3pIhBpnUem-8x3xiiX17TG8g/viewform?c=0&w=1) \
		to help you familiarize yourself with marijuana plant sex. The quiz was provided by Ser_NSFW'
		
Deficiency = ('whats wrong', 'yellow', 'brown', 'red', 'dying', 'dieing', 'curling', 'curling?', 'curl', 'taco', 'tacoing', 'spots', 'spot' );
Deficiency_Info = "Your plant(s) could be suffering from a pH imbalance, nutrient deficiency, or nutrient toxicity. To remedy, a common \
					first step is to check the pH level of the water you're giving your plant to make sure it's within the \
					appropriate range (6.2-6.8). Also consider measuring the pH of your pot's runoff to make sure your soil \
					is also within the correct pH range. Please check the [FAQ](https://www.reddit.com/r/microgrowery/wiki/faq) \
					for more detailed information, and [here](https://imgur.com/a/EwdZM) is a handy visual guide on the different \
					nutrients your marijuana plant uses, and how!"
					
Harvest = ('harvest?', 'chop?', 'is it time', 'is it time?');
Harvest_Info = "If you are wondering if it is time to harvest please make sure you are supplying pictures of your tricomes as that is the only way for us \
				to help you. If you are wondering how this is achieved there are several ways. 1. Using a Jewlers Loupe. 2. Getting a handheld microscope \
				or a USB Microscope (They have them for your computers and sometimes even your Cell Phone). and 3. you can make a simple DIY macro lens \
				for your phone using this handy [guide](https://www.reddit.com/r/microgrowery/comments/yutpq/diy_how_to_make_macro_pictures_of_your_trees_with/) \
				posted by siimR"

time = int(time.time())								#sets time to when bot was first started
reddit = praw.Reddit('bot1')							#sets up bots credentials 
subreddit = reddit.subreddit('MGNBot')						#Sets subreddit

def main():
	print(time)
	
	for submission in subreddit.stream.submissions():			#Looks for New Posts
		process_submission(submission)

def should_skip(submission):
    if submission.created_utc < time:						#checks the post time to the initial start time of the script
		return(True)
    

def generate_response(submission):						#Generates a response based on the title and returns the corect reply if a match is found
	
	normalized_title = submission.title.lower()				#Replaces capitol letters with lower case ones
	
	for question_phrase3 in Sex:
		if question_phrase3 in normalized_title:
			print('Replying to: {}'.format(submission.title))
			return(Sex_Info)
	
	for question_phrase2 in Deficiency:
		if question_phrase2 in normalized_title:
			print('Replying to: {}'.format(submission.title))
			return(Deficiency_Info)
			
	for question_phrase1 in Harvest:
		if question_phrase1 in normalized_title:
			print('Replying to: {}'.format(submission.title))
			return(Harvest_Info)

	for question_phrase in Noob:
		if question_phrase in normalized_title:
			print('Replying to: {}'.format(submission.title))
			return(Noob_Info)


def process_submission(submission):
	
	if should_skip(submission):							#checks to see if the post should be skipped
		return
		
	response = generate_response(submission)					#determins if the post requires a response
	
	if response:
		submission.reply(response)						#if a response is required a post is made with the correct info supplied by generate_response

	return response
	
	
if __name__ == '__main__':
    main()										#calls the main script and starts everything off
