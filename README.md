# GW2HelpingHands
This is the code for https://gw2helpinghand.appspot.com/

I used jinja for page routing and javascript to do processing of data within the webpage. 

There are scripts that run on Google App Engine that pull data from the Guild Wars 2 API and store the data in Google Datastore. The script is scheduled to run every minute so that the data is as fresh as possible without overloading the Guild Wars 2 API. The last updated time is listed on the website in case the Guild Wars 2 API is down or there is a problem establishing a connection, the user will know that the data is old.
