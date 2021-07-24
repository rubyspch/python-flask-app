from flask import Flask,render_template, request, json
import pandas as pd
import pickle
import geopandas as gpd 
from shapely.geometry import Point, Polygon

matrix = pd.read_csv('datasets/multiplier.csv', delimiter=',')
nbh = gpd.read_file('datasets/frontend_neighbourhoods.geojson')
rfr = 'models/randomforestregressor.sav'
model = pickle.load(open(rfr, 'rb'))

def get_multiplier(lat, lon):
    # look up address to get latitude, longitude
    # try:
    # convert input latitude to matrix latitude
    if (lat > 52.29) & (lat < 52.2956):
        lat = 52.29
    if (lat > 52.2956) & (lat < 52.3012):
        lat = 52.2956
    if (lat > 52.3012) & (lat < 52.3068):
        lat = 52.3012
    if (lat > 52.3068) & (lat < 52.3124):
        lat = 52.3068
    if (lat > 52.3124) & (lat < 52.318):
        lat = 52.3124
    if (lat > 52.318) & (lat < 52.3236):
        lat = 52.318
    if (lat > 52.3236) & (lat < 52.3292):
        lat = 52.3236
    if (lat > 52.3292) & (lat < 52.3348):
        lat = 52.3292
    if (lat > 52.3348) & (lat < 52.3404):
        lat = 52.3348
    if (lat > 52.3404) & (lat < 52.346):
        lat = 52.3404
    if (lat > 52.346) & (lat < 52.3516):
        lat = 52.346
    if (lat > 52.3516) & (lat < 52.3572):
        lat = 52.3516
    if (lat > 52.3572) & (lat < 52.3628):
        lat = 52.3572
    if (lat > 52.3628) & (lat < 52.3684):
        lat = 52.3628
    if (lat > 52.3684) & (lat < 52.374):
        lat = 52.3684
    if (lat > 52.374) & (lat < 52.3796):
        lat = 52.374
    if (lat > 52.3796) & (lat < 52.3852):
        lat = 52.3796
    if (lat > 52.3852) & (lat < 52.3908):
        lat = 52.3852
    if (lat > 52.3908) & (lat < 52.3964):
        lat = 52.3908
    if (lat > 52.3964) & (lat < 52.402):
        lat = 52.3964
    if (lat > 52.402) & (lat < 52.4076):
        lat = 52.402
    if (lat > 52.4076) & (lat < 52.4132):
        lat = 52.4076
    if (lat > 52.4132) & (lat < 52.4188):
        lat = 52.4132
    if (lat > 52.4188) & (lat < 52.4244):
        lat = 52.4188
    if (lat > 52.4244) & (lat < 52.43):
        lat = 52.4244
    # convert input longitude to matrix longitude
    if (lon > 4.76) & (lon < 4.7708):
        lon = 4.76
    if (lon > 4.7708) & (lon < 4.7816):
        lon = 4.7708
    if (lon > 4.7816) & (lon < 4.7924):
        lon = 4.7816
    if (lon > 4.7924) & (lon < 4.8032):
        lon = 4.7924
    if (lon > 4.8032) & (lon < 4.814):
        lon = 4.8032
    if (lon > 4.814) & (lon < 4.8248):
        lon = 4.814
    if (lon > 4.8248) & (lon < 4.8356):
        lon = 4.8248
    if (lon > 4.8356) & (lon < 4.8464):
        lon = 4.8356
    if (lon > 4.8464) & (lon < 4.8572):
        lon = 4.8464
    if (lon > 4.8572) & (lon < 4.868):
        lon = 4.8572
    if (lon > 4.868) & (lon < 4.8788):
        lon = 4.868
    if (lon > 4.8788) & (lon < 4.8896):
        lon = 4.8788
    if (lon > 4.8896) & (lon < 4.9004):
        lon = 4.8896
    if (lon > 4.9004) & (lon < 4.9112):
        lon = 4.9004
    if (lon > 4.9112) & (lon < 4.922):
        lon = 4.9112
    if (lon > 4.922) & (lon < 4.9328):
        lon = 4.922
    if (lon > 4.9328) & (lon < 4.9436):
        lon = 4.9328
    if (lon > 4.9436) & (lon < 4.9544):
        lon = 4.9436
    if (lon > 4.9544) & (lon < 4.9652):
        lon = 4.9544
    if (lon > 4.9652) & (lon < 4.976):
        lon = 4.9652
    if (lon > 4.976) & (lon < 4.9868):
        lon = 4.976
    if (lon > 4.9868) & (lon < 4.9976):
        lon = 4.9868
    if (lon > 4.9976) & (lon < 5.0084):
        lon = 4.9976
    if (lon > 5.0084) & (lon < 5.0192):
        lon = 5.0084
    if (lon > 5.0192) & (lon < 5.03):
        lon = 5.0192

    # set location multiplier
    multiplier = matrix.loc[matrix['Lat'] == lat, str(lon)]
    multiplier = multiplier.min()
    return float(multiplier)
    # except:
    #     print("Address not found")
    #     multiplier = 1
    #     return multiplier

def get_neighbourhood(lat, lon):
    # based on that we get latitude, longitude
    # try:
    pnt = Point(lon, lat)
    # set polygons to be able to crosscheck
    poly1 = nbh.loc[nbh.neighbourhood==1,'geometry'].values[0]
    poly2 = nbh.loc[nbh.neighbourhood==2,'geometry'].values[0]
    poly3 = nbh.loc[nbh.neighbourhood==3,'geometry'].values[0]
    poly4 = nbh.loc[nbh.neighbourhood==4,'geometry'].values[0]
    poly5 = nbh.loc[nbh.neighbourhood==5,'geometry'].values[0]
    poly6 = nbh.loc[nbh.neighbourhood==6,'geometry'].values[0]
    poly7 = nbh.loc[nbh.neighbourhood==7,'geometry'].values[0]
    poly8 = nbh.loc[nbh.neighbourhood==8,'geometry'].values[0]
    poly9 = nbh.loc[nbh.neighbourhood==9,'geometry'].values[0]
    poly10 = nbh.loc[nbh.neighbourhood==10,'geometry'].values[0]
    poly11 = nbh.loc[nbh.neighbourhood==11,'geometry'].values[0]
    poly12 = nbh.loc[nbh.neighbourhood==12,'geometry'].values[0]
    poly13 = nbh.loc[nbh.neighbourhood==13,'geometry'].values[0]
    poly14 = nbh.loc[nbh.neighbourhood==14,'geometry'].values[0]
    poly15 = nbh.loc[nbh.neighbourhood==15,'geometry'].values[0]
    poly16 = nbh.loc[nbh.neighbourhood==16,'geometry'].values[0]
    poly17 = nbh.loc[nbh.neighbourhood==17,'geometry'].values[0]
    poly18 = nbh.loc[nbh.neighbourhood==18,'geometry'].values[0]
    poly19 = nbh.loc[nbh.neighbourhood==19,'geometry'].values[0]
    poly20 = nbh.loc[nbh.neighbourhood==20,'geometry'].values[0]
    poly21 = nbh.loc[nbh.neighbourhood==21,'geometry'].values[0]
    poly22 = nbh.loc[nbh.neighbourhood==22,'geometry'].values[0]
    # set neighbourhood
    if pnt.within(poly1):
        neighbourhood = 1
    if pnt.within(poly2):
        neighbourhood = 2
    if pnt.within(poly3):
        neighbourhood = 3
    if pnt.within(poly4):
        neighbourhood = 4
    if pnt.within(poly5):
        neighbourhood = 5
    if pnt.within(poly6):
        neighbourhood = 6
    if pnt.within(poly7):
        neighbourhood = 7
    if pnt.within(poly8):
        neighbourhood = 8
    if pnt.within(poly9):
        neighbourhood = 9
    if pnt.within(poly10):
        neighbourhood = 10
    if pnt.within(poly11):
        neighbourhood = 11
    if pnt.within(poly12):
        neighbourhood = 12
    if pnt.within(poly13):
        neighbourhood = 13
    if pnt.within(poly14):
        neighbourhood = 14
    if pnt.within(poly15):
        neighbourhood = 15
    if pnt.within(poly16):
        neighbourhood = 16
    if pnt.within(poly17):
        neighbourhood = 17
    if pnt.within(poly18):
        neighbourhood = 18
    if pnt.within(poly19):
        neighbourhood = 19
    if pnt.within(poly20):
        neighbourhood = 20
    if pnt.within(poly21):
        neighbourhood = 21
    if pnt.within(poly22):
        neighbourhood = 22
    return neighbourhood
    # except:
    #     neighbourhood = 1
    #     return neighbourhood

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("form.html")

@app.route("/about/", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/data/", methods=["GET", "POST"])
def data():
    return render_template("see-the-data.html")

@app.route("/calculate/", methods=["GET", "POST"])
def calc():
    transactions = []
    if request.method == "POST":
        print(request.form)
        address = request.form.get("address")
        lat = float(request.form.get("lat"))
        lon = float(request.form.get("lng"))
        try:
            multiplier = get_multiplier(lat, lon)
            neighbourhood = get_neighbourhood(lat, lon)
            #amenities calculate
            try:
                dishwasher = int(request.form.get("dishwasher"))
            except:
                dishwasher = 0
            try:
                bathtub = int(request.form.get("bathtub"))
            except:
                bathtub = 0
            try:
                dryer = int(request.form.get("dryer"))
            except:
                dryer = 0

            transactions.append( #stores the data as tuple python list
                (
                int(request.form.get("accommodates")),
                neighbourhood,
                float(request.form.get("property_type")),
                bool(request.form.get("private")),
                (dishwasher + dryer + bathtub)
                )
            )
            print("multiplier: " + str(multiplier) + " neighbourhood: " + str(neighbourhood))
            result = model.predict(transactions)
            weightedresult = result * multiplier
            result_text = f'Price estimate: €{round(weightedresult[0], 2)}'
            print(result_text)
            print(transactions)
            error = "False"
        except:
            print("except error")
            error = "True"
            result_text= "Price Data Not Found"
            print(result_text)
        return render_template("form.html", answer=json.dumps(result_text) , jaddress=json.dumps(address), error=json.dumps(error))