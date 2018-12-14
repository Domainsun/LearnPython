import pickle

def say(name):
    print("name",name)

f=open("json.txt","rb")
# data=pickle.loads(f.read())
data=pickle.load(f)
data["func"]("domain")

