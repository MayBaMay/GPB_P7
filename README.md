# GrandPy Bot

This project was created for the [OpenClassRoom's Python developer course](https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python) (Project 7/13)).<br/>
It is a Flask application integrating a back-end part based on Python 3.7 and a front-end part developed with HTML5, CSS3 and JavaScript.


## Ask GrandPy about a location and if he knows the place, he will give you:
* the adress and a map showing the place location.<br/>
  The application is using Google map API
* and a story about the place or a place nearby<br/>
  The application is using Media Wiki API

You can test this project online on https://gpbotp7.herokuapp.com/<br/>
__NB__: Google API keys might be deactivated in the future.

### Program on GitHub :
Clone this repository, create your environment with Python 3.7 and install requirements.<br/>

You will need two [Google map's API keys](https://cloud.google.com/maps-platform/?hl=fr&utm_source=google&utm_medium=cpc&utm_campaign=FY18-Q2-global-demandgen-paidsearchonnetworkhouseads-cs-maps_contactsal_saf&utm_content=text-ad-none-none-DEV_c-CRE_321592199697-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+Google+Maps+API+EXA-KWID_43700039907225900-kwd-1952727095-userloc_20874&utm_term=KW_google%20map%20api-ST_google+map+api&gclid=Cj0KCQiArozwBRDOARIsAHo2s7sxYc1IeDzv4cuo3ZEUQPd08BclHplMC17n_CuQuv1b8KV9JBH8wiwaAkvtEALw_wcB).<br/>
 One for geolocation (**GOOGLE_GEO_K**) and the other used with javascript to get the map from the geolocation (**GOOGLE_JS_K**). <br/>
 <br/>
Create a file **.env** containing the following script :

```
FLASK_ENV=development
DEBUG=True
GOOGLE_GEO_K="YOUR_GEO_API_KEY"
GOOGLE_JS_K="YOUR_JS_API_KEY"
```

Then, you can run the program in a development mode from your terminal `python run.py` and open your web browser to the localhost address http://localhost:5000/.<br/>

Have fun!
