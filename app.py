from flask import Flask
import ghhops_server as hs
import rhino3dm

#register hops as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/pointat",
    description = "Get point along curve",
    inputs = [
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on curve to evaluate")
    ],
    outputs=[
        hs.HopsPoint("p", "p", "Point on curve at t")
    ],
)

def pointat(curve: rhino3dm.Curve, t):
    return curve.PointAt(t)

if __name__ == "__main__":
    app.run()