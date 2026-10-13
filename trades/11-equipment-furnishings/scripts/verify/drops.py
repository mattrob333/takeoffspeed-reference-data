runs = [  # name, LF traced (F3), ceiling ft (A-130)
 ("Employee Lounge E",6.06,10),("Transaction Bar E",6.02,11),("Relaxed Seating E",13.36,12),
 ("Relaxed Seating S",13.96,12),("Entry 101 S",13.12,12),("Weather Vestibule 100 W",7.22,12),
 ("Booth 104 W",8.06,12),("Meeting Room 105 W",5.96,10)]
LF=sum(r[1] for r in runs); est=1184.4; hidden=74.025
print("sum LF",round(LF,2))
def rep(name,sf): print(f"{name:60s} {sf:8.1f} SF  {100*(sf-est)/est:+.1f}%")
rep("ceiling at each run (traced)", sum(l*c for _,l,c in runs))
rep("flat 12'-0\" head x 74.025", hidden*12)
rep("flat 12'-0\" head x traced", LF*12)
rep("flat 10'-0\" head x 74.025", hidden*10)
rep("flat 10'-0\" head x traced", LF*10)
# reviewer variant: 10 at EL and TB, 12 elsewhere
hb={"Employee Lounge E":10,"Transaction Bar E":10}
rep("reviewer: 10' at EL+TB, 12' elsewhere (traced)", sum(l*hb.get(n,12) for n,l,_ in runs))
# section 3 (entry vestibule) 12' at Entry+Vestibule, section 1 10' elsewhere
h3={"Entry 101 S":12,"Weather Vestibule 100 W":12}
rep("12' at Entry 101+Vestibule 100, 10' elsewhere (traced)", sum(l*h3.get(n,10) for n,l,_ in runs))
# head-to-sill 2'-8"
s=2+8/12
rep("head-to-sill 10'-0\" head (7'-4\") x 74.025", hidden*(10-s))
rep("head-to-sill 12'-0\" head (9'-4\") x 74.025", hidden*(12-s))
rep("head-to-sill 10'-0\" head x traced", LF*(10-s))
rep("head-to-sill 12'-0\" head x traced", LF*(12-s))
rep("head-to-sill, 12' at Entry+Vestibule,10' elsewhere (traced)", sum(l*(h3.get(n,10)-s) for n,l,_ in runs))
print("74.0*16",74.0*16, abs(74.0*16-1184.4)/1184.4*100, "74.025*16",round(74.025*16,4))
print("SS-03 drawn width in", (1855.501708984375-1712.2847900390625)/18*12, "A+B", 66.5+95.75, (66.5+95.75)/12)
