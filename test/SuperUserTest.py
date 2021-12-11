from src.domain import SuperUser

try:
    SuperUser.initialize("pe6o", 553)
except NameError:
    print("first set threw NameError - fallback \n")
    SuperUser.initialize("pe6o",5533)

print("name-->" + SuperUser.getUserName() +"\n")
print("salted UID --> " + SuperUser.getSaltedUID() + "\n")

