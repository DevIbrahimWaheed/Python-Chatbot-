# get ufc realted infromation # far better than using wikipedia for information , as i can force direct user
# https://pypi.org/project/pyufc/ the docs for the libaries
from pyufc import Fighter , PyUFCError
from fancy_tools_effects import tts_typoEffect
import wikipedia # to create a list of ufc fighters

def ufcSearch(data):
    '''This function allows the bot to use the API to get uFC fighter data'''
    try:
        get_ufc_data=Fighter()# this is the class module provide by the API
        get_ufc_data.get_fighter(data)
        name = get_ufc_data.name
        ufc_record= get_ufc_data.record
        ufc_summary = get_ufc_data.summary#the name of fighter
        tts_typoEffect("{} {} {}".format(name,ufc_record,ufc_summary))
    except PyUFCError: # call forth this error if the fighter is not found
        tts_typoEffect("The UFC fighter is not found")

