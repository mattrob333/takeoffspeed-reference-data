p='/home/user/takeoffspeed-reference-data/trades/09e-painting/reading-guide.md'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a)); s=s.replace(a,b)
rep("""The recess returns are PT-4 and need adding (perimeter × depth from A-704 detail 4).""",
    """The recess returns are PT-4 ("PAINT RECESS RETURNS ALL SIDES"). The estimator's 10.6 FT run already steps around the recess on the markup (front, both side returns, back; it is 0.8 ft longer than the 9'-9 3/4" wall on A-704 detail 4), so the side returns are in at the shallow depth drawn on A-150. Only the head and sill returns (2 × 7'-9 3/4" × 9 1/2" = 12.4 SF) are missing. Check the trace before adding returns, or you count the sides twice.""")
rep("""6. **Shop-primed frames.** 08 1113 frames ship primed. 09 9100 3.3.B.2 "Omit primer on metal surfaces that have been shop primed". Count the frames, and carry finish coats only, unless the contractor's house rule says otherwise.""",
    """6. **Shop-primed frames.** Frames ship shop-primed (08 1113 p214 "Exposed Finish: Prime"). 09 9100 3.3.B.2 ("Omit primer on metal surfaces that have been shop primed and touchup painted") lets the field primer be touch-up only, but p320 says this section's priming is in addition to shop priming and 09 9110 p328 still lists a primer system for "Hollow Metal Frames and Doors" (SW ProCryl B66-1310 / BM V131 / PPG Pitt Tech). Count the frames, carry the primer as a contractor convention (the estimator's 1P + 2C is defensible), and flag it.""")
open(p,'w').write(s)
p='/home/user/takeoffspeed-reference-data/trades/09e-painting/README.md'
s=open(p).read()
rep("""p326 3.3.B.2: **"Omit primer on metal surfaces that have been shop primed"**.""",
    """p326 3.3.B.2: **"Omit primer on metal surfaces that have been shop primed and touchup painted"**.""")
open(p,'w').write(s)
