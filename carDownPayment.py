def carPmt():
  cost = int(input("Enter the cost of your car"))
  downPmt = int(input("Enter your down paymnet (if none, enter 0)"))
  trdIn = int(input("Enter your trade in value (if none, enter 0)"))
  years = int(input("Enter the number of years you plan to pay for"))
  yearIntRate = int(input("Enter you annual interest rate expressed as a percentage, 1 = 1%"))
  montInRate = (yearIntRate/100.0)/12
  months = years*12
  compndFactor = ((1+montInRate)**months)/(((1+montInRate)**months)-1)
  amntOwed = cost - downPmt - trdIn
  monthPmt = montInRate*amntOwed*compndFactor
  print ("With a downpayment of $", downPmt, "a trade-in value of $", trdIn, "an annual interest rate of",
         yearIntRate, "% and a", years, "year payment plan, your new $", cost, "car will cost $", monthPmt,
         "per month.")
carPmt()
