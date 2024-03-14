#Pokemon Center
#Author: John Burtsche
import os
import socket
import string
import requests
import json
import random
import socket as sock
from time import ctime
from typing import Tuple, Optional, Any
from colorama import Fore, Style, Back

"""Searches for a Pokemon based on the json file (obtained through https://github.com/fanzeyi/pokemon.json/blob/master/pokedex.json)"""
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


"""produces help print statements to help with new users"""
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

"""Partners Microservice Socket: Recieves a URL and produces an Image and Path"""
def get_random_pokemon_image_path(url):
    HOST = '127.0.0.1'
    PORT = 9092

    socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    socket.connect((HOST, PORT))

    socket.send(url.encode('utf-8'))

    message = str(socket.recv(1024))

    path = message[2:-1]

    print(path)

"""Function to allows for the search of a Pokemon name based on there ID: Returns pokemon_name"""
def search_with_num(num):

    #opens the JSON
    f = open('pokedex.json', encoding="utf8")
    data = json.load(f)

    #Gathers the correct data
    pokemon_name = data[num]['name']['english']

    return pokemon_name


"""Starts the guessing game and returns nothing"""
def guessing_game(pokemon_name):

    #establishes while loop and allows the user to guess until they are done
    while(1):
        guess = input("Who's that Pokemon? (enter 0 to try another command): ")

        if guess == pokemon_name:
            print("Congratulations that's correct")
            break

        if guess == "0":
            break

        if guess != pokemon_name:
            print("Sorry that wasn't correct. Try again or enter 0 for another command")


"""function that returns strengths, weaknesses and not_effective strings as an array"""
def types_and_weaknesses(type):

    #saves response for each possible type based on input
    if type == "Normal":
        strengths = "N/A"
        weaknesses = "Rock"
        not_effective = "Ghost"

    if type == "Fire":
        strengths = "Grass, Ice, Bug"
        weaknesses = "Fire, Water, Rock, Dragon"
        not_effective = "N/A"

    if type == "Water":
        strengths = "Fire, Ground, Rock"
        weaknesses = "Water, Grass, Dragon"
        not_effective = "N/A"

    if type == "Electric":
        strengths = "Water, Flying"
        weaknesses = "Electric, Grass, Dragon"
        not_effective = "Ground"

    if type == "Grass":
        strengths = "Water, Ground, Rock"
        weaknesses = "Fire, Grass, Poison, Bug, Dragon"
        not_effective = "N/A"

    if type == "Ice":
        strengths = "Grass, Ground, Flying, Dragon"
        weaknesses = "Water, Ice"
        not_effective = "N/A"

    if type == "Fighting":
        strengths = "Normal, Ice, Rock"
        weaknesses = "Poison, Flying, Psychic, Bug"
        not_effective = "Ghost"

    if type == "Poison":
        strengths = "Grass, Bug"
        weaknesses = "Poison, Ground, Rock, Ghost"
        not_effective = "N/A"

    if type == "Ground":
        strenghths = "Fire, Electric, Posion, Ghost"
        weaknesses = "Grass, Bug"
        not_effective = "Flying"

    if type == "Flying":
        strenghths = "Grass, Fighting, Bug"
        weaknesses = "Electric, Rock"
        not_effective = "N/A"

    if type == "Psychic":
        strenghths = "Fighting, Poison"
        weaknesses = "Pyschic"
        not_effective = "N/A"

    if type == "Bug":
        strenghths = "Grass, Posion, Psychic"
        weaknesses = "Fire, Figthing, Flying, Ghost"
        not_effective = "N/A"

    if type == "Rock":
        strengths = "Fire, Ice, Psychic, Bug"
        weaknesses = "Fighting, Ground"
        not_effective = "N/A"

    if type == "Ghost":
        strengths = "Ghost"
        weaknesses = "N/A"
        not_effective = "Normal, Psychic"

    if type == "Dragon":
        strengths = "Dragon"
        weaknesses = "N/A"
        not_effective = "N/A"

    information = [strengths, weaknesses, not_effective]

    return information


"""General load in screen"""
print(Fore.RED + "############################################################################################################")
print("\n                                            Pokemon Center                    \n" + Style.RESET_ALL)


print("Please enter one of the following commands for the corresponding information about Pokemon(Gen 1):")

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

    #if input is 2. It generates a random pokemon
    elif val == '2':
        num = random.randint(1, 151)
        random_pokemoon = search_with_num(num)
        print(random_pokemoon)


    #prints type weaknesses(not implemented yet)
    elif val == '3':

        #asks for the type from the user
        print("Enter one of the following types to view there strengths/weaknesses:")
        types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon"]
        print(*types, sep=", ")
        pokemon_type = input("Type that you want: ")

        #error handling if type is not usable
        if pokemon_type not in types:
            print("That's not a type...returning to commands")

        #prints types data
        else:
            type_information = types_and_weaknesses(pokemon_type)
            print(Fore.MAGENTA + f"{pokemon_type}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Strengths: {type_information[0]}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Weaknesses: {type_information[1]}" + Style.RESET_ALL)
            print(Fore.RED + f"Not Effective Against: {type_information[2]}" + Style.RESET_ALL)


    #Prints all the Pokemon
    elif val == '4':
        i = 0
        limit = 151

        #while loop too keep listing pokemon
        while(1):

            #for loop to produce the Pokemon. If it reaches the limit it breaks
            for i in range(i, i+9):
                if i == limit:
                    print("That's all of them!")
                    break
                print(Fore.YELLOW + search_with_num(i) + Style.RESET_ALL)

            #breaks while loop if limit is reached
            if i == limit:
                break

            #asks user if they want more pokemon
            i += 10
            more_pokemon = input("Enter 1 to load more Pokemon, or 0 to exit: ")
            options = ["0", "1"]

            #error handling for input
            if more_pokemon not in options:
                print("Hmm I don't know what you mean try again")
                while(1):
                    more_pokemon = input("Enter 1 to load more Pokemon, or 0 to exit: ")
                    if more_pokemon not in options:
                        print("Hmm I don't know what you mean try again")
                    else:
                        break

            #results of user input
            if more_pokemon == "0":
                break

            if more_pokemon == "1":
                continue

    #if input is 5 it generates a random pokemon image and asks you which one it is
    elif val == '5':

        #random pokemon with int based on id numbers
        num = random.randint(1, 151)
        pokemon_num = ("{:03d}".format(num))

        #creates URL with Serebii website (image based on pokemon id number)
        Pokemon_Image = "https://www.serebii.net/pokemon/art/" +str(pokemon_num)+ ".png"

        #gets the image and saves it with the microservice
        pokemon_num = get_random_pokemon_image_path(Pokemon_Image)

        #fix off by one
        pokemon_name = search_with_num(num-1)

        #starts the guessing game
        guessing_game(pokemon_name)


    #starts the help function
    elif val == '6':
        help()

    #error handler
    else:
        print("I don't recognize your command try again!")