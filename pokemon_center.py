import os
import socket
import string
import requests
import json
from time import ctime
from typing import Tuple, Optional, Any
from colorama import Fore, Style, Back

#Searches for a Pokemon based on the json file (obtained through https://github.com/fanzeyi/pokemon.json/blob/master/pokedex.json)
def search_for_pokemon(pokemon_name):

    #opens the JSON
    f = open('pokedex.json', encoding="utf8")
    data = json.load(f)

    #Gathers the correct data
    for i in range(809):
        name = data[i]['name']['english']
        if name == pokemon_name:
            print(Fore.YELLOW + data[i]['name']['english'])
            print("HP:"+str(data[i]['base']['HP']))
            print("Attack:" + str(data[i]['base']['Attack']))
            print("Defense:" + str(data[i]['base']['Defense']))
            print("Sp.Attack:" + str(data[i]['base']['Sp. Attack']))
            print("SP. Defense" + str(data[i]['base']['Sp. Defense']))
            print("Speed:"+str(data[i]['base']['Sp. Attack']))
            print("Type:" + str(data[i]['type']) + Style.RESET_ALL)

            #closes file if found and returns
            f.close()
            return

    #closes the json file and prints error message
    print("I'm sorry I couldn't find that Pokemon")
    f.close()


#produces help print statements to help with new users
def help():

    #prints starting messages with explanation
    print("Please enter the command that you want to learn more about! ")
    print("Your options are: \n 1-Search for a Pokemon \n 2-Generate a Random Pokemon \n 3-Type Weaknesses/Advantages \n 4-List All Pokemon \n 5-Who's That Pokemon? Game \n 6- Help \n")

    while(1):
        #gets what command they want help with
        question = input("Which command would you like help with (enter 0 to exit): ")

        #gives a response for each command
        if question == '1':
            print("This command allows you to enter the name of a Pokemon and get the reciprocating data about them. \n" \
            "For example if you were to enter 'Charizard', his base stats and important information will be displayed on the screen.\n"
                  "If you don't know any Pokemon names try loading some up in the List All Pokemon command to get some base knowledge going!\n")

        elif question == '2':
            print("This command will generate a random Pokemon and display there stats much like the search funtion. \n"
                  "Please feel free to try it as many times as you want. The more that you do it the more that you will learn about the Pokemon world\n")

        elif question == '3':
            print("This command allows you to enter a type and get the corresponding data about the weaknesses and advantages that it has \n"
                  "Feel free to try all of them out as you will begin to gather the idea of what to use against who when your on the battlefield.\n"
                  "The options are listed when you enter the command.\n")

        elif question == '4':
            print("This command will list all the Pokemon from generation 1. They print out 10 at a time in number order until you exit the command with 0.\n"
                  "The correspoding data/stats for them will have to be loaded in the Search for a Pokemon command.\n")

        elif question == '5':
            print("This command is game that can be played to further your knowledge of Pokemon. When you enter this command an image\n"
                  "will be displayed on your screen. Once the image loads you are able to guess the name of that Pokemon.\n If you"
                  "get it right you can continue if you get it wrong you can of course try again!\n")


        #exit option
        elif question == '0':
            print("Hope you enjoy the program")
            break

        #invalid command exception
        else:
            print("Invalid command try again")

    return

#Format for the TCP connection (use later)
def tcp_client(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = '127.0.0.1'
    server_port = 12435

    try:
        sock.connect((server_address, server_port))
        print(f"Sending: {message}")
        sock.sendall(message.encode())

        response = sock.recv(1024)
        print(f"Recieved: {response.decode()}")

    except:
        print("Hmm there seems to be an error with your echo server/client. You sure you have TCP_server.py running?")

    finally:
        sock.close()






#General load in screen
print(Fore.RED + "############################################################################################################")
print("\n                                            Pokemon Center                    \n" + Style.RESET_ALL)


print("Please enter one of the following commands for the corresponding information about Pokemon:")

print(" 0-EXIT \n 1-Search for a Pokemon \n 2-Generate a Random Pokemon \n 3-Type Weaknesses/Advantages \n 4-List All Pokemon \n 5-Who's That Pokemon? Game \n 6- Help")

print(Fore.RED + "############################################################################################################" + Style.RESET_ALL)

#Constant while loop to get user input
while(1):

    #gets input
    val = input("\nEnter command: ")

    #if input is 0 it exits the program
    if val == '0':
        print("See you later")
        break

    #if input is 1 it finds information about that Pokemon
    elif val == '1':
        pokemon_name = input("Enter the name of a Pokemon to find out more information: ")
        search_for_pokemon(pokemon_name)

    #if input is 2 it generates a random pokemon(not implemented yet)
    elif val == '2':
        print("Generating a Random Pokemon")

    #prints type weaknesses(not implemented yet)
    elif val == '3':
        print("Enter one of the following types to view there strengths/weaknesses")
        print("Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dragon")
        pokemon_type = input("Type that you want: ")

    #starts the help function
    elif val == '6':
        help()

    #error handler
    else:
        print("I don't recognize your command try again!")