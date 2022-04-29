"""Task 1"""
# import random
# import string
#
# from flask import Flask, request, jsonify
#
# from http import HTTPStatus
#
# from webargs import validate, fields
# from webargs.flaskparser import use_kwargs
#
# app = Flask(__name__)
#
#
# @app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
# @app.errorhandler(HTTPStatus.BAD_REQUEST)
# def error_handling(error):
#     headers = error.data.get("headers", None)
#     messages = error.data.get("messages", ["Invalid request."])
#
#     if headers:
#         return jsonify(
#             {
#                 'errors': messages
#             },
#             error.code,
#             headers
#         )
#     else:
#         return jsonify(
#             {
#                 'errors': messages
#             },
#             error.code,
#         )
#
#
# @app.route("/generate-password")
# @use_kwargs(
#     {
#         "length": fields.Int(
#             missing=10,
#             validate=[validate.Range(min=10, max=25)]
#         ),
#     },
#     location="query"
# )
# def generate_password(length):
#     return "".join(
#         random.choices(
#             string.ascii_lowercase + string.ascii_uppercase,
#             k=length
#         )
#     )
#
# app.run(port=5001, debug=True)

"""Task 2"""
# import csv
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/calculate-average")
# def calculate_average():
#     with open('hw.csv', 'r', newline='') as f:
#         Reader = csv.DictReader(f, delimiter=',')
#         data_height = []
#         data_weight = []
#         for line in Reader:
#             data_height.append(line[' Height(Inches)'])
#             data_weight.append(line[' Weight(Pounds)'])
#             data_height = [float(h) for h in data_height]
#             data_weight = [float(w) for w in data_weight]
#     return f'Average height: {sum(data_height)/len(data_height)} Inches; Average weight: {sum(data_weight)/len(data_weight)} Pounds'
#
#
# app.run(port=5001, debug=True)


"""Task 2 (Pandas)"""
import pandas as pd

from flask import Flask

app = Flask(__name__)

@app.route("/calculate-average")
def calculate_average():
    df = pd.read_csv('hw.csv')
    res_mean_height = df[" Height(Inches)"].mean()
    res_mean_weight = df[" Weight(Pounds)"].mean()
    return f'Average height: {res_mean_height} Inches; Average weight: {res_mean_weight} Pounds'

app.run(port=5001, debug=True)


