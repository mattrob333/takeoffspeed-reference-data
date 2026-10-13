import json, math
REF='/home/user/takeoffspeed-reference-data'
L={l['lineNo']:l for l in json.load(open(f'{REF}/reference/estimate/lines.json'))}
G=json.load(open(f'{REF}/reference/markups/legends.json'))
def leg(page,name,prefix=False):
    for p in G:
        if p['page']==page:
            for it in p['items']:
                if it['name']==name or (prefix and it['name'].startswith(name)): return float(it['quantity'])
    raise KeyError((page,name))
def c5(x): return math.ceil(round(x/5,9))*5
def c10(x): return math.ceil(round(x/10,9))*10
fi=lambda f,i=0: f+i/12
est=lambda n: L[n]['quantity']
res={}
def chk(n,val,note=''):
    e=est(n); d=(val-e)/e*100 if e else float('nan')
    res[n]=(val,e,d); print(f'{n:4d} est={e:<12} mine={val:<14.4f} delta={d:+.3f}%  {note}')
# legend values
A6B=leg(4,'WALL A6B @ 12\'6"H'); A3B=leg(4,'WALL A3B @ 12\'6"H'); A6A=leg(4,'WALL A6A @ 12\'6"H'); A3A=leg(4,'WALL A3A @ 12\'6"H')
D3C=leg(4,'WALL D3C @ 12\'6"H 1 SIDE'); D3A=leg(4,'WALL D3A @ 12\'6"H 1 SIDE'); E8_129=leg(4,'EXT 8" STUD WALL @ 12\'9"H')
E6_123=leg(4,'EXT 6" STUD WALL @ 12\'3"H SHTNG 10\'3"H'); PAR72=leg(4,'PARAPET WALL @ 7\'2"H A310'); E8_159=leg(4,'EXT 8" STUD WALL @ 15\'9"H')
E8_4=leg(4,'EXT 8" STUD WALL @ 4\'H'); E8_159N=leg(4,'EXT 8" STUD WALL @ 15\'9"H NO GWB'); S63_188=leg(4,'6" & 3-5/8" METAL STUD @ 18\'8"H, BS 1/2" SHTNG ONLY')
S6_44=leg(4,'6" METAL STUD WALL @ 4\'4" HT, BS GWB'); A3A_39=leg(4,'WALL A3A @ 3\'9"H (NO INS)')
RT1=leg(7,'RT1 ROOFING'); RT2=leg(7,'RT2 ROOFING'); CRK=leg(7,'TAPERED POLYISOCYANURATE INSULATION ROOF CRICKET'); WALK=leg(7,'TPO WALKWAY PAD MEMBRANE')
PAR27=leg(7,'PARAPET WALL @ 2\'7"H'); PAR17=leg(7,'PARAPET WALL @ 1\'7"H'); PAR47=leg(7,'PARAPET WALL @ 4\'7"H')
COP9=leg(7,'COPING 9/A450'); COP6=leg(7,'COPING 6/A450'); COP3=leg(7,'COPING 3/A430'); EDGE=leg(7,'CANOPY EDGE 7/A430'); HEAD=leg(7,'9/A430')
HL=leg(7,"8/A450 LAP ROOF 2', INCL WALL"); CURB=leg(7,'CURB - 1/A450'); LAP21=leg(7,'PARAPET LAP @ 2\'1"H - 4,6/A450'); LAP1=leg(7,"PARAPET LAP @ 1'H - 4,6/A450"); LAP36=leg(7,'PARAPET LAP @ 3\'6"H - 4,6/A450')
HATCH=leg(7,'30"x36" ROOF ACCESS HATCH - 3/A450'); RD=leg(7,'FLASHING @ ROOF DRAIN'); VENT=leg(7,'FLASHING @ VENT PIPE')
BR200=leg(11,'EXT-1',True); BR201=leg(12,'EXT-1',True); TWF200=leg(11,'THRU WALL FLASHING'); TWF201=leg(12,'THRU WALL FLASHING')
SE200=leg(11,'SEALANT W/ BACKER ROD'); SE201=leg(12,'SEALANT W/ BACKER ROD'); AF200=leg(11,'ALUMINUM FLASHING'); AF201=leg(12,'ALUMINUM FLASHING')
SI200=leg(11,'PRE-FINISHED ALUMINUM SILL'); SI201=leg(12,'PRE-FINISHED ALUMINUM SILL'); ACM200=leg(11,'ACM1, ACM2 FINISH - 1/A440'); ACM420=leg(17,'ACM1, ACM2 FINISH - 1/A440')
EIFS1_200=leg(11,'EIFS-1'); EIFS1_201=leg(12,'EIFS-1'); EIFS2_200=leg(11,'EIFS-2'); EIFS2_201=leg(12,'EIFS-2'); LIN=leg(11,'Linear')
ACM3=leg(5,'ACM-3 ALUMINUM COMPOSITE METAL PANEL CANOPY - 10/A430'); EIFSSOF=leg(5,'EIFS SOFFIT 1/A310')
BOOTH=leg(29,'6"THK. 16GA. METAL STUD @ 12" O.C W/ 6"THK. SOUND BATT',True); SLAB=leg(33,'4"THK. CONCRETE SLAB',True); STEM8=leg(33,'8"THK. CONCRETE STEM WALL',True); STEM10=leg(33,'10"THK. CONCRETE STEM WALL',True)

interior=[A6B,A3B,A6A,A3A,D3C,D3A,A3A_39,S6_44]; ext=[E8_129,E6_123,E8_159,E8_4]
il=sum(interior); el=sum(ext); print('interior LF',il,'ext LF',el)
chk(148,4*il+el,'4xint+1xext')
# alternatives for 148
Aser=A6B+A3B+A6A+A3A; Dser=D3C+D3A; low=A3A_39+S6_44
print('  alt 4A+2D+2ext+2low=',4*Aser+2*(Dser+el+low), ' 4A+4low+2D+2ext=',4*(Aser+low)+2*(Dser+el), ' 2*(all int+ext)=',2*(il+el), ' 4*(il)+2*ext=',4*il+2*el,' 4*(il+ext)=',4*(il+el))
print('  all A120 runs incl 18-8 & parapet:', il+el+S63_188+PAR72+E8_159N)
# 149
WIN={'A':(fi(12,11.5),12,1),'B':(fi(9,11),12,1),'C':(fi(7,4),12,1),'D':(8,fi(9,4),1),'E':(6,fi(7,4),2),'F':(6,10,1),'G':(fi(13,4),fi(9,4),1),'H':(14,fi(9,4),1),'J':(fi(7,8.25),12,1),'K':(fi(7,7.625),10,1)}
for k,(w,h,n) in WIN.items(): print('   win',k,round(2*(w+h)*n,4))
GP=sum(2*(w+h)*n for w,h,n in WIN.values()); print('  glazed perim',GP)
chk(149,c10(est(88)+GP),f'910+{GP:.4f}={910+GP:.4f} ceil10')
chk(150,SE200+SE201); chk(189,SE200+SE201)
chk(151,SLAB+STEM8*2,f'implied perim {(est(151)-SLAB)/2:.2f}; with 10in stem too: {SLAB+(STEM8+STEM10)*2}')
chk(152,A3B*12.5); chk(153,A6B*12.5,f'implied LF {est(153)/12.5}')
chk(154,math.ceil(HL)*2.0); chk(155,E6_123*12.25,f'implied LF {est(155)/12.25}')
rows8=[(PAR17,fi(1,7)),(PAR27,fi(2,7)),(E8_4,4),(PAR47,fi(4,7)),(PAR72,fi(7,2)),(E8_129,fi(12,9)),(E8_159,fi(15,9)),(E8_159N,fi(15,9))]
s8=sum(a*b for a,b in rows8); chk(156,s8,f'line311={est(311)}; parapet part={PAR17*fi(1,7)+PAR27*fi(2,7)+PAR47*fi(4,7)+PAR72*fi(7,2):.2f}')
# stud-count based 311 check: studs count x heights
studs=[(35,fi(1,7)),(29,fi(2,7)),(10,4),(73,fi(4,7)),(5,fi(7,2)),(68,fi(12,9)),(38,fi(15,9))]
print('  stud-count implied LF per row (count*16/12):',[(round(c*16/12,2),h) for c,h in studs], ' sum SF via count*1.3333*h=',sum(c*16/12*h for c,h in studs))
# solve 2652.875 - sum of all but one?
chk(157,math.ceil(HL)*2.5); chk(158,round(RT2)); chk(159,round(RT1))
chk(160,c5(ACM200+ACM420)+c5(BR200+BR201),f'raw {ACM200+ACM420+BR200+BR201}')
chk(161,round(BOOTH),f'line312={est(312)} LF, line302={est(302)} SF')
laps=LAP21*fi(2,1)+LAP1*1+LAP36*fi(3,6); field=RT1+RT2
chk(162,field+laps+HL*2+EDGE*2.5,f'field {field} laps {laps:.4f} hl {HL*2} edge {EDGE*2.5}')
rem=est(162)-field-laps; print('  remainder after field+laps =',rem, ' rem-HL*2=',rem-HL*2, ' /EDGE=',(rem-HL*2)/EDGE, ' rem/EDGE=',rem/EDGE,' rem w/o laps=',est(162)-field)
# GPT alt
print('  GPT alt:',field+laps+EDGE*fi(1,4)+HL*4.5+(CURB+11)*1)
chk(163,round(RT1)+math.ceil(HL)*2); chk(164,CRK); chk(165,RT1+RT2); chk(166,c5(CURB*1.0),f'curb x1.5={CURB*1.5}')
chk(167,WALK); chk(168,c5(COP3)); chk(169,round(COP6)); chk(170,c5(COP9)); chk(171,c5(CURB)); chk(172,HATCH*2*(30+36)/12); chk(173,RD); chk(174,VENT)
chk(175,c5(HEAD)); chk(176,c5(HEAD)); chk(177,c5(CURB))
chk(178,c5(EIFS1_200+EIFS1_201),f'raw {EIFS1_200+EIFS1_201}'); chk(179,c5(EIFS2_200+EIFS2_201),f'raw {EIFS2_200+EIFS2_201}'); chk(180,c5(EIFSSOF)); chk(181,c5(ACM200+ACM420),f'raw {ACM200+ACM420}'); chk(182,c5(ACM3)); chk(183,c5(EDGE))
chk(184,est(178)+est(179)+est(180)+est(181)+est(85))
chk(185,SI200+SI201); chk(186,AF200+AF201); chk(187,TWF200+TWF201); chk(188,c5(LIN))
# fixtures
F=json.load(open(f'{REF}/trades/07-thermal-moisture/fixtures.json'))
print('\nFIXTURES', len(F))
def run(fx):
    f=fx['formula']; i={k:v['value'] for k,v in fx['inputs'].items()}
    if f=='acousticSealantLF': return i['interiorPartitionLF']*i['interiorBeadsPerLF']+i['exteriorWallLF']*i['exteriorBeadsPerLF']
    if f=='openingSealantLF': return c10(i['trimLF']+i['glazedPerimeterLF'])
    if f=='sumRuns': return sum(i['runs'])
    if f=='underSlabXpsSF': return i['slabSF']+i['perimeterLF']*i['turnDown']
    if f=='cavityInsulationSF': return i['runLF']*i['height'] if 'runLF' in i else sum(a*b for a,b in i['runs'])
    if f=='rigidBandSF': return i['runLF']*i['height']
    if f=='roofInsulationSF': return round(i['areaSF']/i['round'])*i['round']
    if f=='rigidBehindCladdingSF': return c5(i['acmSF'])+c5(i['brickSF'])
    if f=='membraneSF': return i['fieldSF']+sum(a*b for a,b in i['flashings'])
    if f=='coverBoardSF': return i['fieldSF']+i['wallLF']*i['wallHeight']
    if f=='areaSF':
        a=i['areaSF']; a=sum(a) if isinstance(a,list) else a
        return c5(a) if 'roundUpTo' in i else a
    if f=='stripSF': return c5(i['runLF']*i['width'])
    if f=='runLF': return c5(i['runLF']) if 'roundUpTo' in i else round(i['runLF'])
    if f=='curbPerimeterLF': return i['count']*2*sum(i['size'])/12
    if f=='count': return i['count']
    if f=='sumAreasSF': return sum(i['areasSF'])
    raise KeyError(f)
for fx in F:
    v=run(fx); e=fx['expected']['quantity']; d=abs(v-e)/e*100 if e else 0
    flag='' if d<=fx['tolerancePct']+1e-9 else '  <<< OUTSIDE TOLERANCE'
    rc=fx.get('recomputed'); rcflag='' if rc is None or abs(rc-v)<0.01 else f'  recomputed field {rc} != {v}'
    print(f"{fx['name'][:40]:40s} mine={v:<12.4f} exp={e:<12} d={d:.3f}% tol={fx['tolerancePct']}{flag}{rcflag}")
