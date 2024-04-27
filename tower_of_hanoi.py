def toh(a,from_rod,to_rod,ans_rod):
    if a==1:
        print("Move disk 1(one from rod)",from_rod,"to rod",to_rod)
        return
    toh(a-1,from_rod,ans_rod,to_rod)
    print("Move disk",a,"frm rod",from_rod,"to rod",to_rod)
    toh(a-1,ans_rod,to_rod,from_rod)

n=3
toh(n,"A","C","B")