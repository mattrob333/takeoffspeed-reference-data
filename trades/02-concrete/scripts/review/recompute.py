import json, math
from fractions import Fraction as Fr
def ftin(f,i=0): return Fr(f)+Fr(i,12)
R=lambda x: round(float(x),6)
est={16:1917.6,17:39.22,18:364.11,19:9.196296,20:1.0,21:1.496544,22:6.5,23:1.773333,24:2.413704,25:1.379259,26:2.166667,27:9.628148,28:0.522593,29:0.041667,30:1420.0}
leg={'slab':1917.6,'iso':39.2,'scj':364.1,'wf20':124.2,'stem8':193.8,'stem10':8.4,'pad':1}
cnt={'F30':3,'F38':3,'F50':6,'F60':1,'F70':1,'F7040':1,'F10050':1}
dims={'F30':(ftin(3),ftin(3),ftin(1)),'F38':(ftin(3,8),ftin(3,8),ftin(1)),'F50':(ftin(5),ftin(5),ftin(1,2)),
'F60':(ftin(6),ftin(6),ftin(1,4)),'F70':(ftin(7),ftin(7),ftin(1,4)),'F7040':(ftin(4),ftin(7),ftin(1,4)),'F10050':(ftin(5),ftin(10),ftin(1,2))}
lineof={'F30':20,'F38':21,'F50':22,'F60':23,'F70':24,'F7040':25,'F10050':26}
def pct(a,b): return round((a-b)/b*100,3)
out={}
out[16]=leg['slab']; out[17]=leg['iso']; out[18]=leg['scj']
out[19]=float(Fr(1242,10)*2*1/27)
for k,(L,W,D) in dims.items():
    out[lineof[k]]=float(cnt[k]*L*W*D/27)
out[27]=float(Fr(1938,10)*2*Fr(8,12)/27)
out[28]=float(Fr(84,10)*2*Fr(10,12)/27)
out[29]=float(Fr(3,2)*Fr(3,2)*Fr(1,2)/27)
# formwork exact
fw_wf=Fr(1242,10)*1*2
fw_sp=sum(cnt[k]*2*(L+W)*D for k,(L,W,D) in dims.items())
fw_st=(Fr(1938,10)+Fr(84,10))*2*2
fw_pad=4*Fr(3,2)*Fr(1,2)
fw=fw_wf+fw_sp+fw_st+fw_pad
print('formwork parts',float(fw_wf),float(fw_sp),float(fw_st),float(fw_pad),'sum',float(fw))
out[30]=math.ceil(fw/10)*10
print('EXACT from legend:')
for ln in sorted(out): print(ln, R(out[ln]), est[ln], pct(out[ln],est[ln]))
# estimator convention
print('ESTIMATOR CONVENTION:')
d2={'F30':(3.0,3.0,1.0),'F38':(3.67,3.67,1.0),'F50':(5.0,5.0,1.17),'F60':(6.0,6.0,1.33),'F70':(7.0,7.0,1.33),'F7040':(4.0,7.0,1.33),'F10050':(5.0,10.0,1.17)}
e={}
e[19]=124.15*2*1/27
for k,(L,W,D) in d2.items(): e[lineof[k]]=cnt[k]*L*W*D/27
e[27]=194.0*2*0.67/27
e[28]=8.5*2*0.83/27
e[29]=1.5*1.5*0.5/27
fw2=124.15*2+sum(cnt[k]*2*(L+W)*D for k,(L,W,D) in d2.items())+(194.0+8.5)*4+3.0
print('fw est conv',fw2, math.ceil(fw2/10)*10)
for ln in sorted(e): print(ln, R(e[ln]), est[ln], pct(e[ln],est[ln]))
# alternatives for line 27/28
print('27 with 193.8*2*0.67/27', 193.8*2*0.67/27, pct(193.8*2*0.67/27,est[27]))
print('28 with 8.4*2*0.83/27', 8.4*2*0.83/27, pct(8.4*2*0.83/27,est[28]))
print('28 with 10.75in exact', float(Fr(84,10)*2*Fr(1075,1200)/27))
print('27 needed LF for exact with 0.67:', est[27]*27/2/0.67, ' with 8/12:', est[27]*27/2/(8/12))
print('28 needed LF with 0.83:', est[28]*27/2/0.83, ' with 10/12:', est[28]*27/2/(10/12))
# fw with 10.75?
print('pad 6', 6*1.5*1.5*.5/27)
