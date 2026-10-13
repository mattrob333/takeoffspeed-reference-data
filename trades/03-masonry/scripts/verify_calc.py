import math
z=8; mk_w=1191; sh_w=2592; pt_per_ft=18  # 1/4"=1'-0" -> 0.25in*72 = 18 pt/ft
os_px=434-205
# (a) sheet-scale
os_ft_a=os_px/z*(sh_w/mk_w)/pt_per_ft
# (b) in-image scale: 2'-0" above FFE = hatch top y=245 to FFE line y=375
ppf=(375-245)/2.0
os_ft_b=os_px/ppf
purple_h_ft=(414-245+1)/ppf
print('overshoot ft sheet-scale %.3f, image-scale %.3f'%(os_ft_a,os_ft_b))
print('purple height ft (image scale) %.3f'%purple_h_ft)
for L in (os_ft_a,os_ft_b):
    for h in (8/12+2.0, purple_h_ft):
        print(' L %.2f x h %.3f = %.2f SF'%(L,h,L*h))
area=163.6+232.1
for d in (9.2,):
    s=area-d; print('strict SF', round(s,1), 'vs400 %.2f%%'%((s-400)/400*100), 'vs395.7 %.2f%%'%(-d/area*100))
print('share of 232.1: %.2f%%'%(9.2/232.1*100))
print('rowlocks strict', round(149.3-3.5,1), round(149.8-3.5,1), 'p12', round(87.9-3.5,1), round(88.3-3.5,1))
print('red start x205, green x198 -> green overshoot ft', (434-198)/ppf)
print('raw-sum delta vs 400: %.3f%%'%((area-400)/400*100))
