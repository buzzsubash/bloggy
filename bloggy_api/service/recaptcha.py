from urllib import request

from bloggy import settings


def recaptcha_verify(recaptchaResponse):
    data = {
        'secret': settings.GOOGLE_RECAPTHCA_SECRET_KEY,
        'response': recaptchaResponse
    }

    req = request.Request(settings.GOOGLE_RECAPTHCA_TOKEN_VERIFY_URL, data=data)
    response = request.urlopen(req)
    if response.status == 200:
        result = response.json()
        print("Recaptcha verification:" + str(result))
        return True
    return False