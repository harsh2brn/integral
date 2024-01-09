import azure.functions as func
import logging
import math
import json
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="numericalintegralservice/0/3.14159")
def numericalintegralservice(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    iterations = [10, 100, 1000, 10000, 100000, 1000000]
    results = []
    upper = 3.141519
    lower = 0

    for N in iterations:
        delta_x = (upper - lower) / N
        result = 0.0

        for i in range(N):
            x_i = lower + i * delta_x
            result += abs(math.sin(x_i)) * delta_x

        results.append({"N": N, "result": result})

    return func.HttpResponse(json.dumps(results), mimetype="application/json", status_code=200)