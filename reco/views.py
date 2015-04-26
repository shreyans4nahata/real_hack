from django.shortcuts import render
from googleplaces import GooglePlaces, types, lang
import requests
import json
from pymongo import MongoClient
from django.http import HttpResponse
from bson import json_util


YOUR_API_KEY = 'AIzaSyA40WUFjvGbWn81giJaH9xsXiDvmqz0BCw'
google_places = GooglePlaces(YOUR_API_KEY)
def gog(request):
    locat=request.GET.get('places','')
    keyw=request.GET.get('keyw','')
    lat=request.GET.get('lat','')
    lon=request.GET.get('lon','')
    r=request.GET.get('radius','')
    if r is None    :
        r=20000
    if keyw == '':
        keyw = "Flats for rent"
    #locat = raw_input("Enter Location: ")
    lat_lng={'lat': (lat) ,"lng": (lon) }
    #keyw = raw_input()
    # You may prefer to use the text_search API, instead.
    #query_result = google_places.nearby_search( location="Bangalore", keyword= "hotels",  
       # types=[types.TYPE_ATM],radius=200000
       # )   
    query_result = google_places.nearby_search( lat_lng=lat_lng, keyword= keyw,  
    	types=[],radius=str(r).strip("'")
    	)

    if query_result.has_attributions:
        print query_result.html_attributions
    l={}
    i=0
    for place in query_result.places:
    # Returned places from a query are place summaries.
        print place.name
        #print place.geo_location
    #print place.place_id
        place.get_details()
    # The following method has ypesto make a further API call.
        l[i]=place.details
        i+=1
    '''#print place.geometry.location.lat
    #print place.geometry.location.lng
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    #print place.details
    #if "u'rating'" in place.details:
        print place.rating # A dict matching the JSON response from Google.
    #if "u'address_components'" in place.details:
        print place.formatted_address # A dict matching the JSON response from Google.
        if "u'rating'" in place.details:
            print place.details[u'rating'] # A dict matching the JSON response from Google.
        if "u'rating'" in place.details:
:            print place.details[u'rating'] # A dict matching the JSON response from Google.
        if "u'rating'" in place.details:
            print place.details[u'rating'] # A dict matching the JSON response from Google.

        print place.local_phone_number'''
    #st = json.load(l)
    return HttpResponse(json.dumps(l), content_type="application/json")
#    print place.international_phone_number
#    print place.website
#    print place.url

    # Getting place photos
'''
for photo in place.photos:
        # 'maxheight' or 'maxwidth' is required
            photo.get(maxheight=500, maxwidth=500)
        # MIME-type, e.g. 'image/jpeg'
            photo.mimetype
        # Image URL
            print photo.url
        # Original filename (optional)
            photo.filename
        # Raw image data
            photo.data
    #return
'''
def fb(request): 


    ACCESS_TOKEN = 'CAACEdEose0cBAMSQsejdaLPgoTqvrUsgPQFt2Eb8eBQArfVk612CIT6ReKRr68SergBTWZAbBU8vDZA5q2yApz7UNedWjRah0T4YBZA7muwSZBPlUDpLzl3kq7gGEW1fKCszeFuuZBzCNVirB1AyZABcTCl8UATpPQxtI0NAVepZAXp6fXmeIHZBpaCdDIx7hCoK0NhSyNBm71geA2kdjZAmZC'

    base_url = 'https://graph.facebook.com/me'

    fields = 'id,name'

    url = '%s?fields=%s&access_token=%s' % \
        (base_url, fields, ACCESS_TOKEN,)


#print(url)


    content = requests.get(url).json()


    print json.dumps(content, indent=1)
# Adding and deleting a place
def mongo(request):
    c = MongoClient()
    db1 = c.data_house
    collection = db1.posts
    lat=request.GET.get('lat','')
    lon=request.GET.get('lon','')
    places=request.GET.get('place',"")
    k={}
    i=0
    #print db1.data_house.find({"result.locality_url_name":places})
    if lat == '' :
        d = db1.data_house.find({"result.locality_url_name":"kandivali-east"})
        l = list(d)
        #print l
        
    #n=len(l)
    #print n
    #for i in xrange(n):
    #    k[i] = l[i]
    return HttpResponse(json.dumps(l,default=json_util.default),content_type='application/json')

        
    #places=request.GET.get('places','')
    #if lat == "" || lon == '':
    #    db1.data_house.find()

'''
try:
    added_place = google_places.add_place(name='Mom and Pop local store',
            lat_lng={'lat': 51.501984, 'lng': -0.141792},
            accuracy=100,
            types=types.TYPE_HOME_GOODS_STORE,
            language=lang.ENGLISH_GREAT_BRITAIN)
    print added_place.place_id # The Google Places identifier - Important!
    print added_place.id

    # Delete the place that you've just added.
    google_places.delete_place(added_place.place_id)
except GooglePlacesError as error_detail:
    # You've passed in parameter values that the Places API doesn't like..
    print error_detail'''

# Create your views here.
