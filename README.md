# GrandPy Bot

## Ask GrandPy about a location and if he knows the place, he will give you:
* the adress and a map showing the place location.<br/>
  The application is using Google map API
* and a story about the place or a place nearby<br/>
  The application is using Media Wiki API

The project is available online on https://gpbotp7.herokuapp.com/<br/>
__NB__: Google API might be deactivated in the future.

## Programm on GitHub :
If you clone this repository, make sure your environnement contains all requirements.<br/>
You will find them in the file requirement.txt

Use your [Google map's API keys](https://cloud.google.com/maps-platform/?hl=fr&utm_source=google&utm_medium=cpc&utm_campaign=FY18-Q2-global-demandgen-paidsearchonnetworkhouseads-cs-maps_contactsal_saf&utm_content=text-ad-none-none-DEV_c-CRE_321592199697-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+Google+Maps+API+EXA-KWID_43700039907225900-kwd-1952727095-userloc_20874&utm_term=KW_google%20map%20api-ST_google+map+api&gclid=Cj0KCQiArozwBRDOARIsAHo2s7sxYc1IeDzv4cuo3ZEUQPd08BclHplMC17n_CuQuv1b8KV9JBH8wiwaAkvtEALw_wcB) in the **config.py** file. You will need two keys. One for geolocation (**GOOGLE_GEO_KEY**) and the other used with javascript to get the map from the geolocation (**GOOGLE_JS_KEY**).<br/>

Then you can run the programm from your terminal: `python run.py`, open you're web browser and go to the localhost adress http://localhost:5000/.
