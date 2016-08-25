# up_in_time
It is a django-powered web app which can create reminders or alarms just by a single click.

## Installation
* Just clone the git repo.
* OPen the terminal and cd into the folder 
* Run ```./manage.py runserver```
* Visit [here](http://127.0.0.1:8000/alarm/) (If you haven't changed the default port - 8000)

##Still To-Do:

* Obviously, give it some *better* looks.
* Add an alert message when user tries to close the alarm tab or as soon as the user clicks on setting alarm, we can display a danger box on this page.
* Add a message input and display it on tha alarm screen. Again JS should communicate with HTTP GET request or you can write the message in a database.
* optimize the code - Use django's template system
* Design GUI and choose colors.
* Look for a way by which webbrowser.open("alarm set") which opens tab only in the default browser can open it in the same browser perhaps by manipulating HTTP_USER_AGENT.
* ~~Embed music in pop up so that there is actually an alarm~~
* ~~Seperate the Javascript and HTML in pop-up.~~
* Add customization to alarm screen- Figure out a way to give input directlty from HTTP to JS
* ~~Make and add a favicon~~
* Add contact us, about_us page.
	
### Far away:
* Add functionality like sending automatic emails and messages(look up twillio) at the given time.
* Make the website responsive.
* Add the facility for the users to add custom Youtube videos or uploaded Audios or audio links to be served as alarm.

##Features

* Works even if you have changed the window.
* If you have switched into fullscreen, then also the alarm pop up is shown.

## Dependencies

* python
* django v1.9.8
* Make sure that pop ups are allowed in your browser.

### Happy Time Saving

