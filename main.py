class Car:

   def turn_on(self):

     print("This car is now on")

     return self

   def driving(self):

      print("You are now driving")

      return self

   def turn_off(self):

    print("The engine is now off")

    return self

car=Car()

car.turn_on().driving().turn_off()



# code by Mr.Helper
