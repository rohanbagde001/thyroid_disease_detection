from flask import Flask
from thyroid.logger import logging
from thyroid.exception import ThyroidException
import sys



app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        thyroid = ThyroidException(e, sys)
        logging.info(thyroid.error_message)
        logging.info("testing logging functionality")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)