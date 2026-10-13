# Reviewer check: is 119.7556 the unique combo within +/-0.05 CY of 119.8 on a wider grid?
import itertools
F=[('F30',3,3,1,3),('F38',3+8/12,3+8/12,1,3),('F50',5,5,14/12,6),('F60',6,6,16/12,1),('F70',7,7,16/12,1),('F7040',7,4,16/12,1),('F10050',10,5,14/12,1)]
WS=[0,0.25,0.5,0.75,1,1.5,2,2.5,3]
DEP=[0,1,2,3]  # depth = T + d
LFS={'WF20 124.2':124.2,'stem 202.2':202.2,'stem8 193.8':193.8}
hits=[]
for (lfn,lf),wsw,wsp,dw,dp in itertools.product(LFS.items(),WS,WS,DEP,DEP):
    tr=lf*(2+2*wsw)*(1+dw)
    pad=sum((L+2*wsp)*(W+2*wsp)*(T+dp)*c for n,L,W,T,c in F)
    cy=(tr+pad)/27
    if abs(cy-119.8)<=0.05: hits.append((round(cy,4),lfn,wsw,wsp,dw,dp,round(tr/27,4),round(pad/27,4)))
for h in sorted(hits): print(h)
print('reviewer variant', (202.2*(2+3)*2 + sum(L*W*(T+2)*c for n,L,W,T,c in F))/27)
print('1490.4 decompositions:',124.2*3*4,124.2*4*3,124.2*6*2)
# original grid in formulas.md: ws {0,.5,1,1.5,2}, depth {T,T+1,T+2}, WF20 LF
hits0=[]
for wsw,wsp,dw,dp in itertools.product([0,.5,1,1.5,2],[0,.5,1,1.5,2],[0,1,2],[0,1,2]):
    cy=(124.2*(2+2*wsw)*(1+dw)+sum((L+2*wsp)*(W+2*wsp)*(T+dp)*c for n,L,W,T,c in F))/27
    if abs(cy-119.8)<=0.05: hits0.append((round(cy,4),wsw,wsp,dw,dp))
print('original grid hits',hits0)
