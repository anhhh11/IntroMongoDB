__author__ = 'anhhh11'
# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import unittest
import json
import requests

class TestReadJson(unittest.TestCase):
    def setUp(self):
        self.BASE_URL = "http://musicbrainz.org/ws/2/"
        self.ARTIST_URL = self.BASE_URL + "artist/"

        self.query_type = {  "simple": {},
                        "atr": {"inc": "aliases+tags+ratings"},
                        "aliases": {"inc": "aliases"},
                        "releases": {"inc": "releases"}}


    def query_site(self,url, params, uid="", fmt="json"):
        params["fmt"] = fmt
        r = requests.get(url + uid, params=params)
        print "requesting", r.url

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            r.raise_for_status()


    def query_by_name(self,url, params, name):
        params["query"] = "artist:" + name
        print params
        return self.query_site(url, params)


    def pretty_print(self,data, indent=4):
        if type(data) == dict:
            print json.dumps(data, indent=indent, sort_keys=True)
        else:
            print data


    def ig_test_main(self):
        results = self.query_by_name(self.ARTIST_URL, self.query_type["simple"], "Nirvana")
        self.pretty_print(results)

        artist_id = results["artist"][1]["id"]
        print "\nARTIST:"
        self.pretty_print(results["artist"][1])

        artist_data = self.query_site(self.ARTIST_URL, self.query_type["releases"], artist_id)
        releases = artist_data["releases"]
        print "\nONE RELEASE:"
        self.pretty_print(releases[0], indent=2)
        release_titles = [r["title"] for r in releases]

        print "\nALL TITLES:"
        for t in release_titles:
            print t
    def test_exploring_json(self):
        #Use JSONView Chrome to overview structure
        q1 = self.query_by_name(self.ARTIST_URL, self.query_type["simple"], "FIRST AID KIT")
        q1_count = 0
        for artist in q1["artist"]:
            if artist["score"] == "100":
                q1_count += 1
        print q1_count

        q2 = self.query_by_name(self.ARTIST_URL, self.query_type["simple"], "Queen")
        begin_area = q2["artist"][0]["begin-area"]["name"]
        print "Q2: Begin area for Queen"
        print begin_area


        q3 = self.query_by_name(self.ARTIST_URL, self.query_type["simple"], "Beatles")
        aliases = q3["artist"][0]["aliases"]
        for a in aliases:
            if a["locale"] == "es":
                alias = a["name"]
        print alias


        q4 = self.query_by_name(self.ARTIST_URL, self.query_type["simple"], "Nirvana")
        disam = q4["artist"][0]["disambiguation"]
        print "Q4: Disambiguation Nirvana"
        print disam


        q5 = self.query_by_name(self.ARTIST_URL, self.query_type["simple"], "One Direction")
        begin_date = q5["artist"][0]["life-span"]["begin"]
        print "Q5: One Direction begin"
        print begin_date
