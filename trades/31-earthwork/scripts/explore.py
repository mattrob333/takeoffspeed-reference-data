import itertools
# estimator concrete lines (CY)
conc = {19:9.196296,20:1.0,21:1.496544,22:6.5,23:1.773333,24:2.413704,25:1.379259,26:2.166667,27:9.628148,28:0.522593}
ftg = sum(v for k,v in conc.items() if k<=26)
stem = conc[27]+conc[28]
print('footing CY',ftg,'stem CY',stem,'total',ftg+stem)
print('exc-backfill', 119.8-83.7)
print('haul - total conc', 36.1-(ftg+stem))
# stem wall check
print('8in stem', 193.8*0.67*2/27, 193.8*8/12*2/27, '10in', 8.4*0.83*2/27, 8.4*10/12*2/27)
# footing schedule: name, L, W, T, count
F=[('F30',3,3,1,3),('F38',3+8/12,3+8/12,1,3),('F50',5,5,14/12,6),('F60',6,6,16/12,1),('F70',7,7,16/12,1),('F7040',7,4,16/12,1),('F10050',10,5,14/12,1)]
WF=(124.2,2,1)
def exc(ws, depth_mode, wf_ws=None, wfLF=124.2):
    wf_ws = ws if wf_ws is None else wf_ws
    tot=0
    for n,L,W,T,c in F:
        D = {'T':T,'T+2':T+2,'T+1':T+1}[depth_mode]
        tot += (L+2*ws)*(W+2*ws)*D*c
    T=1
    D={'T':T,'T+2':T+2,'T+1':T+1}[depth_mode]
    tot += wfLF*(2+2*wf_ws)*D
    return tot/27
for ws in (0,0.5,1,1.5,2):
    for dm in ('T','T+1','T+2'):
        for wfLF in (124.2,202.2):
            print(ws,dm,wfLF,round(exc(ws,dm,wfLF=wfLF),2))
