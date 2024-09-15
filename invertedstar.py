import logging
import azure.functions as func

def invertedstar(n):
    result = []
    for i in range(n, 0, -1):
        result.append((n-i) * ' ' + i * '*')
    return "\n".join(result)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        n = int(req.params.get('n'))
        if n < 1:
            raise ValueError
    except (ValueError, TypeError):
        return func.HttpResponse(
            "Please provide a valid positive integer for the number of lines. Example: ?n=5",
            status_code=400
        )

    result = invertedstar(n)
    return func.HttpResponse(result, status_code=200)