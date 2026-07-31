"""
api.py
---------------------------------------
REST API for PhishGuard AI
"""


from src.predict import predict_url
from flask import Flask,request,jsonify
from src.predict import predict_url

app = Flask(__name__)


# ---------------------------------------------------
# Home
# ---------------------------------------------------

@app.route("/api", methods=["GET"])
def apihome():

    return jsonify({

        "application": "PhishGuard AI",

        "version": "1.0.0",

        "status": "running"

    })


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@app.route("/api/health", methods=["GET"])
def apihealth():

    return jsonify({

        "status": "healthy"

    })


# ---------------------------------------------------
# Predict
# ---------------------------------------------------

@app.route("/api/predict", methods=["POST"])
def apipredict():

    data = request.get_json()

    if data is None:

        return jsonify({

            "success": False,

            "message": "JSON body is required."

        }), 400

    url = data.get("url", "").strip()

    if url == "":

        return jsonify({

            "success": False,

            "message": "URL is required."

        }), 400

    try:

        result = predict_url(url)

        return jsonify({

            "success": True,

            "data": result

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500


# ---------------------------------------------------
# Batch Prediction
# ---------------------------------------------------

@app.route("/api/predict/batch", methods=["POST"])
def apibatch_predict():

    data = request.get_json()

    urls = data.get("urls")

    if not urls:

        return jsonify({

            "success": False,

            "message": "URLs list is required."

        }), 400

    results = []

    for url in urls:

        try:

            results.append(

                predict_url(url)

            )

        except Exception:

            results.append({

                "url": url,

                "prediction": "Error",

                "probability": None

            })

    return jsonify({

        "success": True,

        "total": len(results),

        "results": results

    })


# ---------------------------------------------------
# Run
# ---------------------------------------------------

# if __name__ == "__main__":

    # app.run(

    #     host="0.0.0.0",

    #     port=8000,

    #     debug=True

    # )