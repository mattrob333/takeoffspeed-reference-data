import math
SOF=[('3-6 BS',4.2,3.5,3.5,2),('6-6/4',2.7,6.5,4.0,1),('3-6/1-6',6.7,3.5,1.5,1),('4-6/3',30.5,4.5,3.0,1),('5-9/2-6',35.3,5.75,2.5,1),('2H',28.1,2.0,2.0,1)]
# Engine gypsum ceiling, reviewed-commercial profile, irregular area -> SF*12/16
print('joists engine',516.1*12/16,'vs est 387.969925 ->',(516.1*0.75/387.969925-1)*100)
print('joists engine on 516.0', 516*0.75, (516*0.75/387.969925-1)*100)
# default profile (no reviewed profile)
s=516.0
print('default: mud lb',s*0.138,(s*0.138/273.48-1)*100,'tape LF',s*0.37,'rolls',s*0.37/500,(s*0.37/500/0.387-1)*100,'screws EA',s*1.2,'adhesive none')
# engine soffit, mimic: faces, drop=board ht, toStructure=frame-board, width=0, single run per type, spacing 16
tot_board=0; tot_stud=0; tot_track=0; tot_bead=0
for n,lf,fh,bh,f in SOF:
    if n=='3-6 BS': drop=fh; up=0
    else: drop=bh; up=fh-bh
    board=lf*f*drop
    per=math.ceil(lf*12/16)+1
    studs=per*f*(drop+up)
    tot_board+=board; tot_stud+=studs; tot_track+=lf*(f+2); tot_bead+=lf*f
    print(n,board,per,studs)
print('engine soffit board',tot_board,'studs',tot_stud,'track',tot_track,'bead',tot_bead)
print('vs est studs 429.6:',tot_stud,(tot_stud/429.599624-1)*100,' without bracing est soffit part',452.125/1.33)
print('bracing share', 90.075/429.6*100)
# if reader gives width 1ft bottoms
print('bottom at 1ft width adds', sum(lf for n,lf,*_ in SOF))
# ACT engine
for tag,sf,mod in (('ACT-1',948.7,4),('ACT-2',244.8,8)):
    print(tag,'tiles',sf/mod,'mains LF',sf*12/48,'4ft tees',sf*144/(48*24),'hangers',sf*12/48/4, 'with 5% waste tiles', sf/mod*1.05)
print('attic stock 10%:', 948.7*0.1, 244.8*0.1)
# baffles field fallback
W=24; s=8; n=math.floor(W*12/s)+1; print('rows',n,'row len',370.76/37)
