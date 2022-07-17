from flask import Flask
from thyroid.logger import logging


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.info("testing logging functionality")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)