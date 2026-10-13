# estimator rounded dims (2dp) as seen in concrete lines
Fr=[('F30',3,3,1,3),('F38',3.67,3.67,1,3),('F50',5,5,1.17,6),('F60',6,6,1.33,1),('F70',7,7,1.33,1),('F7040',7,4,1.33,1),('F10050',10,5,1.17,1)]
Fe=[('F30',3,3,1,3),('F38',3+8/12,3+8/12,1,3),('F50',5,5,14/12,6),('F60',6,6,16/12,1),('F70',7,7,16/12,1),('F7040',7,4,16/12,1),('F10050',10,5,14/12,1)]
for lab,F in (('rounded',Fr),('exact',Fe)):
    conc=sum(L*W*T*c for n,L,W,T,c in F)/27
    iso=sum((L+1)*(W+1)*(T+2)*c for n,L,W,T,c in F)/27
    isoF38=sum((L+1)*(W+1)*(T+(1 if (n=='F38' and i==0) else 2)) for n,L,W,T,c in F for i in range(c))/27
    wf=124.2*(2+2)*(1+2)/27
    print(lab,'conc',round(conc,4),'iso',round(iso,4),'wf',round(wf,4),'exc',round(iso+wf,4),'exc w/ one F38 at -1',round(isoF38+wf,4))
    for n,L,W,T,c in F: print('  ',n,c,round((L+1)*(W+1)*(T+2)*c,3),'CF')
