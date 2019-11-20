from bs4 import BeautifulSoup
import urllib3
import requests

url = "https://menus.sodexomyway.com/BiteMenu/Menu?menuId=14756&locationId=11870001&whereami=http://mnsu.sodexomyway.com/dining-near-me/university-dining-center"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")
allFood = soup.findAll('a', attrs={'class':'get-nutritioncalculator primary-textcolor'})
allCals = soup.findAll('a', attrs={'class':'get-nutrition primary-textcolor'})
userCalories = 0
nums = '0123456789'
#Display data in readable format

def printData(charIndex):
	for char in allFood[charIndex].contents:
		print(char)

	for char in allCals[charIndex].contents:
		print(char)
'''
#Show all foods
count = 0 
for item in allFood:
	printData(count)
	count +=1 
'''
#Gather user info (Calorie and macro goals)
def getGoals():
	userCalories = int(input("Please input calorie goal for the day (kC): "))	

#Display Info (Text/RsbPi)
fullList = {}
def compileFood():
	count = 0
	for food in allFood:
		for foodName in food.contents:
			fullList[foodName] = allCals[count].contents
			count +=1
compileFood()
calList = []
joinCount = 0
for entry in fullList:
	allCalsInt = []
	for item in fullList[entry]:
		for char in item:
			if char in nums:
				allCalsInt.append(char)
	fixedCals = ''.join(allCalsInt)
	fullList[entry] = fixedCals

calorieCount = 0 
meal = []
while calorieCount < userCalories:
	count = 0
	for food in fullList:
		if int(fullList[food]) <= calorieCount:
			meal.append(fullList[food])
			calorieCount += int(fullList[food])
			count+=1
getGoals()
print(meal)