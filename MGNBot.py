#!/usr/bin/python
import praw
import time

Noob = ('help', 'first grow', 'newbie', 'noob', 'question', 'questions');	#Newbie Questions
Noob_Info = 'Have you checked the [sidebar](https://www.reddit.com/r/microgrowery/wiki/config/sidebar) \
		It is full of all sorts of helpful Information'

Sex = ('male', 'males', 'male?', 'males?', 'female', 'females','female?', 'females?',\
		'sex', 'sex?', 'sexing', 'sexing?', 'male/female', 'male/female?');	#Sex Questions
Sex_Info = 'Sex can be determined once the plant starts to receive less than 14 hours of light per day, in the "pre-flower" stage. If your plant \
		is still in seedling or vegetative phase (>14 hours of light per day) you may see early sex indicators, but wait till pre-flower is \
		triggered to be sure.\
		Males will develop little ball-shaped pollen sacs, while females will develop pointy, teardrop-shaped growths that extrude fuzzy white \
		hairs called "pistils". Some plants may show signs of both sexes, we call these "hermaphrodites", or "hermies". \
		Here is a [Quiz](https://docs.google.com/forms/d/e/1FAIpQLSc1v779jfbU1-AmDcw0u09BCS3pIhBpnUem-8x3xiiX17TG8g/viewform?c=0&w=1) \
		to help you familiarize yourself with marijuana plant sex. The quiz was provided by Ser_NSFW'
		
Deficiency = ('whats wrong', 'yellow', 'brown', 'red', 'dying', 'dieing', 'curling', 'curling?', 'curl', 'taco', 'tacoing', 'spots', 'spot' );		#Deficiency Questions
Deficiency_Info = "Your plant(s) could be suffering from a pH imbalance, nutrient deficiency, or nutrient toxicity. To remedy, a common \
					first step is to check the pH level of the water you're giving your plant to make sure it's within the \
					appropriate range (6.2-6.8). Also consider measuring the pH of your pot's runoff to make sure your soil \
					is also within the correct pH range. Please check the [FAQ](https://www.reddit.com/r/microgrowery/wiki/faq) \
					for more detailed information, and [here](https://imgur.com/a/EwdZM) is a handy visual guide on the different \
					nutrients your marijuana plant uses, and how!"

time = int(time.time())									#sets time to when bot was first started
reddit = praw.Reddit('bot1')							#sets up bots credentials 
subreddit = reddit.subreddit('MGNBot')					#Sets subreddit

def main():
	print(time)
	
	for submission in subreddit.stream.submissions():	#Looks for New Posts
		process_submission(submission)

def should_skip(submission):
    if submission.created_utc < time:
		return(True)
    

def generate_response(submission):						#Generates a response based on the title and returns the corect reply
	
	normalized_title = submission.title.lower()			#Replaces capitol letters with lower case ones
	
	for question_phrase2 in Sex:
		if question_phrase2 in normalized_title:
			print('Replying to: {}'.format(submission.title))
			return(Sex_Info)
	
	for question_phrase1 in Deficiency:
		if question_phrase1 in normalized_title:
			print('Replying to: {}'.format(submission.title))
			return(Deficiency_Info)

	for question_phrase in Noob:
		if question_phrase in normalized_title:
			print('Replying to: {}'.format(submission.title))
			return(Noob_Info)


def process_submission(submission):
	
	if should_skip(submission):
		return
		
	response = generate_response(submission)
	
	if response:
		submission.reply(response)

	return response
	
	
if __name__ == '__main__':
    main()
