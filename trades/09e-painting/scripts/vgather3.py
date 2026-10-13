W_ft=9+9.75/12
for room_px in (1131,1120):
    k=W_ft/room_px
    front_l=269-157; front_r=1288-1175; back=1175-269; ret=240-195.5
    tot=front_l+front_r+back+2*ret
    print('room_px',room_px,'ft/px',round(k,5),'run px',tot,'run ft',round(tot*k,3),'return depth ft',round(ret*k,3),'no-return ft',round((front_l+front_r+back)*k,3))
