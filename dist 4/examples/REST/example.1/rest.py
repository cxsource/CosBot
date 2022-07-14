import cloudscraper
import base64

class REST():

    # ------------------------------------------------------------------------------- #

    def __init__(self):
        self.restURL = 'https://helheim.io.project-z.eu'

        self.session = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'mobile': False,
                'platform': 'windows'
            }
        )

    # ------------------------------------------------------------------------------- #

    def auth(self, key):
        response = self.session.post(
            f'{self.restURL}/rest/authenticate',
            json={'key': key}
        ).json()

        if response['error']:
            print(response['errorMsg'])
            exit()

        return response

    # ------------------------------------------------------------------------------- #

    def solveCT(self, userAgent, domain, challenge):
        response = self.session.post(
            f'{self.restURL}/rest/kasada/ct',
            json={
                'User-Agent': userAgent,
                'domain': domain,
                'challenge': challenge
            }
        ).json()

        if response['error']:
            print(response['errorMsg'])
            exit()

        return base64.b64decode(response['payload'])

    # ------------------------------------------------------------------------------- #

    def solveCD(self, domain):
        response = self.session.post(
            f'{self.restURL}/rest/kasada/cd',
            json={'domain': domain}
        ).json()

        if response['error']:
            print(response['errorMsg'])
            exit()

        return response['payload']

# ------------------------------------------------------------------------------- #
