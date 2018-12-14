import pickle

def say(name):
    print(name)

info={
    "name":"domain",
    "age":18,
    "func":say
}

f=open("json.txt","wb")
# f.write(pickle.dumps(info))
pickle.dump(info,f)
f.close()
