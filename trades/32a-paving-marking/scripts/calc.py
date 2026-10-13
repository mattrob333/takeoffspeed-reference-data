import math, json
r2=lambda x: round(x+1e-12,2)
pier=lambda D,H,n: r2(math.pi/4*r2(D)**2)*H*n/27
exact=lambda D,H,n: math.pi/4*D**2*H*n/27
out={}
out['634']=241.8+505.8; out['634c']=math.ceil(out['634'])
out['635c']=math.ceil(1834.7); out['637c']=math.ceil(113.3); out['638c']=math.ceil(993.9)
out['636']=1835/25; out['636u']=1834.7/25
out['636runs_app']= (math.ceil(366.94/25)-1)*5
out['660']=pier(1.0,1.0,4); out['660app']=exact(1.0,1.0,4)
out['675']=pier(16/12,3.0,5); out['675app']=exact(16/12,3.0,5)
out['714']=pier(16/12,4.0,8); out['714app']=exact(16/12,4.0,8)
out['675_6boll']=pier(16/12,3.0,6)
out['675_c60_24in']=pier(2.0,3.0,5)
out['area16']=r2(math.pi/4*r2(16/12)**2); out['area16exact']=math.pi/4*(16/12)**2
out['area12']=r2(math.pi/4*1.0)
# impervious cross-check
imp = {'building':1900,'hd_asphalt':11367.3,'sd_asphalt':2459.2,'sidewalk':1834.7,'ramps':113.3,'conc_pav_21_18':747.6,'dumpster_slab':384.3,'transformer':16,'curb_gutter_2ft':993.9*2.0}
out['imp_sum']=sum(imp.values()); out['imp_plan']=21033; out['imp_delta_pct']=(out['imp_sum']-21033)/21033*100
# crosswalk / hatch
out['xw_cad_edges_bars']=2*22.5+8*5; out['xw_scale']=79.46/85
out['hatch_cad']=sum([7.09,7.05,7.05,7.07,7.07,7.07,5.82,3.32,4.57,2.07])
out['hatch_plus_sides']=out['hatch_cad']+2*18
out['hatch_plus_perim']=out['hatch_cad']+2*(18+5)
out['stopbar_each']=49.58/2
out['ramp_each']=113.3/2
# deltas measured vs legend
for est,leg in [(2459.18,2459.2),(11367.3,11367.3),(441.31,441.3),(79.46,79.5),(97.48,97.5),(49.58,49.6)]:
    out[f'd_{est}']=(leg-est)/est*100
# app deltas
for k,(a,e) in {'660':(out['660app'],0.117037),'675':(out['675app'],0.772222),'714':(out['714app'],1.647407)}.items():
    out['app_d_'+k]=(a-e)/e*100
out['app_hatch_36']=5*18/3; out['app_xw']=22.5
out['app_bollard_exc_merged']=out['675app']+out['714app']
out['app_sswl_merged']=441.31+45; out['app_24in_merged']=49.58+20
for k,v in out.items(): print(k, round(v,6) if isinstance(v,float) else v)
json.dump(out,open('/home/user/work/32a-paving-marking/calc.json','w'),indent=1)
