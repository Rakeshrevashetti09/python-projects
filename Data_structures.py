print(" Welcome to the DSA_for_DevOps -- List and Dictionary")
# lists
list_of_cloud = ["AWS", "azure", "gcp","oracle"]
list_of_env = ["dev", "test","prod"]

print(type(list_of_cloud))
print(type(list_of_env))

print(list_of_cloud[3])
print(list_of_env[0])

# list_iteration
for cloud in list_of_cloud:
    if cloud == "AWS":
        print("AWS is the best cloud service provider")

# Dictionary
dict_of_cloud = {
    "AWS":"Amazon Web Services",
    "azure":"microsoft azure",
    "gcp":"google gcp"
}
print(dict_of_cloud["AWS"])
print(dict_of_cloud.get("gcp","NOT FOUND"))

dict_of_cloud.update({"lenode":"example"})
print(dict_of_cloud)

