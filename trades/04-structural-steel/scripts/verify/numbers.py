from fractions import Fraction as F
def ft(f,i=0,n=0,d=1): return float(f+(i+F(n,d))/12)
BC=ft(14,11,1,2); CD=ft(9,0,3,8); BD=BC+CD
print('B-C',round(BC,3),'B-D',round(BD,3))
print('12KCS2 grid 3xBC',round(3*BC,2),'est 53.96 diff',round(53.96-3*BC,2),round((53.96/(3*BC)-1)*100,1),'%')
print('18KCS2 grid 4xBD',round(4*BD,2),'est 108.49 diff',round(108.49-4*BD,2),round((108.49/(4*BD)-1)*100,1),'%')
s12=[(1196.5-954.1),(1198.7-954.1),(1198.7-954.1)]; s18=[1361.3-954.0,1359.6-954.1,1361.3-954.0,1361.3-955.6]
print('12KCS2 as drawn',round(sum(s12)/18,2),[round(v/18,2) for v in s12])
print('18KCS2 as drawn',round(sum(s18)/18,2),[round(v/18,2) for v in s18])
print('est per joist 12:',round(53.96/3,2),'18:',round(108.49/4,2),'over grid per joist',round(53.96/3-BC,2),round(108.49/4-BD,2))
# markup: band top 429.5, grid B 456.83, scale 8.2675
print('markup start N of B',round((456.83-429.55)/8.2675,2))
# HSS6x6x3/8
eight=174.71-19.03
print('8 runs',round(eight,2))
b4_sched=(249.6-103.9)/9; b4_top=(240.6-103.9)/9; b4_bot=(249.6-240.6)/9
print('B-4 sched bar',round(b4_sched,2),'top',round(b4_top,2),'bottom below L1',round(b4_bot,2),"t/s 15'-2 1/4\" =",round(ft(15,2,1,4),3))
print('B-4 if base 2ft below',round(b4_top+2,2))
print('schedule-true',round(eight+b4_sched,2),'to',round(eight+b4_top+2,2))
print('stray over B-4',round(19.03-b4_sched,2),'to',round(19.03-(b4_top+2),2))
bars={'A-2.6/A-4/A.5-6':(85.8,3),'A-6/B-2':(84.6,2),'B-4':(103.9,1),'C-6/D-6/E-3':(73.8,3)}
tot=0
for k,(top,c) in bars.items():
    L=((258.6 if k!='B-4' else 249.6)-top)/9; tot+=L*c; print(k,round(L,2),'x',c)
print('schedule-bar total 9 HSS6x6x3/8',round(tot,2))
print('estimate 236.34 vs sched-true',round(236.34-(eight+b4_sched),2),round((1-(eight+b4_sched)/236.34)*100,1),'%')
print('p35 repeats 40.86 + D-5 20.21 =',round(40.86+20.21,2),'; 236.34-61.07=',round(236.34-61.07,2))
# C7
low=15.02+14.60
print('lower C7 runs',round(low,2),'share of 428.46',round(low/428.46*100,1),'%')
canopy=[(140,36),(28,157),(157,150),(236,188)]
per=[2*(w+h)/8.2675 for w,h in canopy]
print('canopy bbox perims',[round(v,1) for v in per],'sum',round(sum(per),1),'236.7/sum',round(236.7/sum(per)*100,1),'%')
# fixture 36
print('fixture36 exact',6*ft(1,7),'rounded',6*round(ft(1,7),2),'dev',round((6*ft(1,7)/9.48-1)*100,3))
