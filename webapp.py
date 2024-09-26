from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

#TODO: Add an @app.route annotation and a function that creates a response based on the user input. 
#The function should set the response variable in response.html and should render the response.html template.
    
if __name__=="__main__":
    app.run(debug=True)
