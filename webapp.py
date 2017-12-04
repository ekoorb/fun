
from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    
    with open('static/county_demographics.json') as demographicsdata:
        counties = json.load(demographicsdata)
    
    reply_list = get_state_options(counties)
    
    if 'State' in request.args:
        return render_template('home.html', options = reply_list, fact = fact_function(request.args["State"]), reply_state = request.args["State"]) 
    
    return render_template('home.html' , options = reply_list)


    
def get_state_options(counties):
    states = []
    options = ""
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options
  
def fact_function(stateName):
    with open('static/county_demographics.json') as demographicsdata:
        counties = json.load(demographicsdata)
    statePopulation = 0
    for c in counties:
        if c["State"] == stateName:
            statePopulation += c["Population"]["2014 Population"]
    return statePopulation


if __name__=="__home__":
    app.run(debug=False, port=54321)

