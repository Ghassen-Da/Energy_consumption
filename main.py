from flask import Flask, request
from service import DB
app = Flask(__name__)

@app.route('/')
def hello_enexflow():
    return 'Welcome To Enexflow API!'

@app.route("/consommation")
def get_consommation_between_dates():
    db= DB() #Instantiate the DB with the Singleton pattern
    args = request.args # request query arguments
    starting_date = args.get('start')
    ending_date = args.get('end')   
    return db.get_consommation_between_dates(starting_date, ending_date)


if __name__ == '__main__':
    app.run(host='0.0.0.0')