import pyautogui
import time
import os
import clickPosition
import foundProgram
from pynput.mouse import Controller
import blumGameBoot
import moveToLeft
import closeBrowser
import moveTegram
import earnAcadmy
import earnSocial

earnEarn_path = "Earn/earn_Earn.png"
earnWeekly_path = "Earn/earn_Weekly.png"
earnNew_path = "Earn/earn_New.png"
earnAcademy_path = "Earn/earn_Academy.png"
earnSocial_path = "Earn/earn_Socials.png"
earnOpen_path = "Earn/earn_Open.png"
earnClose1_path = "Earn/earn_Close1.png"



result = foundProgram.locate_image_on_screen(earnClose1_path, 0.99)
clickPosition.click_at_position(result)






