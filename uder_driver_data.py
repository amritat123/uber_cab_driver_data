print("*🙏welcome your uber  cab trip... 🙏*")
print("*____________________________________________________________________________________________________*")
print()
import random
print("**current location is your cab driver**:-")

print("*_________________________________________________________________________________________________*")


def cab_driver():
    ride_kilometer1=0
    ride_kilometer2=0
    ride_kilometer3=0
    ride_kilometer4=0

    sum_km_1=0
    sum_km_2=0
    sum_km_3=0
    sum_km_3=0
    sum_km_4=0

    count_dr1=0
    count_dr2=0
    count_dr3=0
    count_dr4=0
    i=1
    while i<3:
        driver_place=["huskur","electronic city","laal baag","chnadpur","tk waterfall"]
        place_driver1=random.choice(driver_place)
        place_driver2=random.choice(driver_place)
        place_driver3=random.choice(driver_place)
        place_driver4=random.choice(driver_place)
        print(" driver1 is in:-",place_driver1,"\n","driver2 is in:-",place_driver2,"\n","driver3 is in:-",place_driver3,"\n","driver4is in:-",place_driver4,"\n")
        customer=input("enter your driver now stand position:- ")
        print()
        user=input("if you want to book the ride press the book......or.... if you want to cancel the ride press cencel:-:-:- ")
        print()

        if user=="book":
            if customer=="driver1":
                print("now your rider1 is in",place_driver1)
                list=[206,304,507,459,151,701]
                list1=random.choice(list)
                sum_km_1=sum_km_1+list1
                list2=list1*5
                ride_kilometer1=ride_kilometer1+list2
                count_dr1+=1

            elif customer=="driver2":
                print("now your driver2 is in",place_driver2)
                list=[200,308,500,457,155,708]
                list1=random.choice(list)
                sum_km_2=sum_km_2+list1
                list2=list1*5
                ride_kilometer2=ride_kilometer2+list2
                count_dr2+=1

            elif customer=="driver3":
                print("now your driver3 is in",place_driver3)
                list=[204,301,505,458,159,707]
                list1=random.choice(list)
                sum_km_3=sum_km_3+list1
                list2=list1*5
                ride_kilometer3=ride_kilometer3+list2
                count_dr3+=1

            elif customer=="driver4":
                print("now your driver4 is in:-",place_driver4)
                list=[202,303,501,454,153,701]
                list1=random.choice(list)
                sum_of_km_r4=sum_of_km_r4+list1
                list2=list1*5
                ride_kilometer4=ride_kilometer4+list2
                count_dr4+=1
        elif user=="cancel":
            continue
        i+=1
    if ride_kilometer1!=0:
        print("today driver1 earn",ride_kilometer1," and the driver1 ride",sum_km_1,"total kilometer","whole day driver1 ride",count_dr1,"time")
    if ride_kilometer2!=0:
        print("today driver2 earn",ride_kilometer2," and the driver2 ride",sum_km_2,"total kilometer","whole day driver2 ride",count_dr2,"time")
    if ride_kilometer3!=0:
        print("today driver3 earn",ride_kilometer3," and the driver3 ride",sum_km_3,"total kilometer","while day driver3 ride",count_dr3,"time")
    if ride_kilometer4!=0:    
        print("today driver4 earn",ride_kilometer4," and the driver4 ride",sum_km_4,"total kilometer","whole day driver4 ride",count_dr4,"time")

cab_driver()

               
      




























































