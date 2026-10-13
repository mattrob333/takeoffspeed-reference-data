P='/home/user/takeoffspeed-reference-data/trades/01-demolition/best-practices.md'
s=open(P).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:70]
    s=s.replace(a,b)
rep("Units follow what is cheapest to measure and what the contract pays by.",
    "Units follow what is simplest to measure and what the contract measures by.")
rep('NYSDOT pays "disposal of buildings" as a lump sum per specific building', 'NYSDOT measures "disposal of buildings" as a lump sum per specific building')
rep("The reference estimate prices the two buildings at 89,780 CFT and 17,140 CFT", "The reference estimate carries the two buildings as 89,780 CFT and 17,140 CFT")
rep('NYSDOT 202-5.06: cost of asbestos removal, abatement and disposal "will be paid for separately"',
    'NYSDOT 202-5.06: asbestos removal, abatement and disposal are measured as their own item, outside the building removal')
rep("CY loose or tons, **only if priced separately** from the removal item", "CY loose or tons, **only if measured as its own item** apart from the removal item")
rep("NYSDOT includes demolition and disposal in the building lump sum (202-5.02).", "NYSDOT includes disposal in the building removal item (202-5.02).")
rep("(spec pages 26-29)", "(spec pages 26-37)")
rep('Some agency specs pay pavement-marking removal as its own item: NYSDOT 417-5 says removal of pavement markings "will be paid under separate pay items"',
    'Some agency specs measure pavement-marking removal as its own item (NYSDOT 417-5)')
rep('NYSDOT includes "any sawcutting performed in order to facilitate removal" in the slab-removal unit price (202-5.07/5.08,',
    'NYSDOT includes "any sawcutting performed in order to facilitate removal" in the slab-removal item (202-5.07/5.08,')
rep("3. Allowance or unit-price items that make disposal a separate quantity (01 22 00 Unit Prices exists in this book: check it for demolition-related unit prices).",
    "3. Allowance items or bid-form items that make disposal a separate quantity.")
open(P,'w').write(s)
