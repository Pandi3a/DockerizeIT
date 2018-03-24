#!/usr/bin/python

import os

option = True
doc="Dockerfile"
print("")
print("")
print("################################################################")
print("  ____                _                _  _____      ___  _____ ")
print(" |  _ \   ___    ___ | | __ ___  _ __ (_)|__  / ___ |_ _||_   _|")
print(" | | | | / _ \  / __|| |/ // _ \| '__|| |  / / / _ \ | |   | |  ")
print(" | |_| || (_) || (__ |   <|  __/| |   | | / /_|  __/ | |   | |  ")
print(" |____/  \___/  \___||_|\_|\___||_|   |_|/____|\___||___|  |_|  ")
print("")
print("################################################################")
print("")
print("")
print("################################################################")
print(" Dockerize Your Script")
print("################################################################")
print("")

while option:
    print ("""
    1.Make Container Folder
    2.Create Docker File
    3.FROM
    4.ADD
    5.CMD
    6.Build
    7.Quit
    """)
    option = raw_input("Start: ")
    if option == "1":
        folder=raw_input("Type name of folder: ")
        os.system("mkdir ~/Desktop/" + folder)
        print("\n Done!")
        print("")

    elif option == "2":
      os.system("touch ~/Desktop/" + folder + "/" + doc)
      print("\n All Done!")
      print("\n NOW COPY YOUR SCRIPT IN THE NEW FOLDER!!!")
      print("")

    elif option == "3":
     fr = raw_input("Type FROM where? : ")
     os.system("echo " + "FROM " + fr + ">> " + folder + "/" + doc)
     print("\n Done You may Continue")

     print("\n FROM in Dockerfile set to " + fr)

    elif option == "4":
     ad=raw_input("Now Add your script to Dockerfile: ")
     os.system("echo " + "ADD " + ad + " /" + ">> " + folder + "/" + doc)
     print("\n Procede with step 5 ")

    elif option == "5":
     print("Write your text with quotes!!!")
     print("Example: CMD1: python | CMD2: ./script.py ")
     cm1 = raw_input("CMD1 : ")
     cm2 = raw_input("CMD2 : ")
     file = open(folder + "/" + doc , "a")
     file.write("CMD [" + cm1 + ", " +  cm2 + "]")
     file.close()



     # os.system("echo " + "CMD [" + '"' + cm1 +'"' + ", " + '"' + cm2 + '"' + "] " + ">> " + folder + "/" + doc)
     print("\n Done Ready to be Built ")
     print("\n Procede with step 6 ")


    elif option == "6":
      bd = raw_input("Type name of Docker Image: ")
      os.system("cd " + " ~/Desktop/" + folder )
      os.system("sudo docker build -t " + bd + " ~/Desktop/" + folder)
      print("\n Your Docker Image is Ready for use!! ")



    elif option == "7":
     quit()



    else:
     print("\n Not Valid Choice Try again")
