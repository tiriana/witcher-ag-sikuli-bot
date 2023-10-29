# play as jaskier to finish the game 

import org.sikuli.basics.Settings;
from org.sikuli.script import Pattern
from sikuli import *

Settings.MoveMouseDelay = 0.1
Settings.DelayValue = 0.1
Settings.DelayBeforeMouseDown = 0.1
Settings.DelayBeforeMouseUp = 0.1
Settings.ClickDelay = 0.1
Settings.TypeDelay = 0.05
Settings.WaitScanRate = 5
Settings.ObserveScanRate = 5
Settings.DelayBeforeDrag = 0.1
Settings.DelayBeforeDrop = 0.1
Settings.Highlight = True


window_title = "The Witcher AG"

# Use the App class to focus on the window
app = App(window_title)
app.focus()

wait_and_click = lambda image_path: (wait(image_path, 10), click(image_path))

setROI(Region(1768,282,1583,892))

play_offline = "play_offlie.png"
new_game = "new_game.png"
disable_icon = "disable_icon.png"

disable_geralt = "disable_geralt.png"
disable_jaskier = "disable_jaskier.png"
disable_triss = "disable_triss.png"
disable_yarpen = "disable_yarpen.png"


start_game = "start_game.png"
main_task_title = "main_task_title.png"
trip_icon = "trip_icon.png"
novigrad_destination = "novigrad_destination.png"
confirm_trip = "1698581903377.png"
red_lead = "red_lead.png"
blue_lead = "blue_lead.png"
purple_lead = "purple_lead.png"
sing_action = "sing_action.png"
sing_confirmation_ok = "sing_confirmation_ok.png"
menu_button = "menu_button.png"
exit_button = "exit_button.png"

turn_for_jaskier = "turn_for_jaskier.png"


one_game = "one_game.png"

jaskier_task_my_narod_oxenturtu = "jaskier_task_my_narod_oxenturtu.png"
jaskier_task_glos_rozsadku = "jaskier_task_glos_rozsadku.png"
jaskier_task_dar_jezykow = "jaskier_task_dar_jezykow.png"
jaskier_task_szalony_kaplan = "jaskier_task_szalony_kaplan.png"
jaskier_task_porozumienie_na_belletynie = "jaskier_task_porozumienie_na_belletynie.png"
jaskier_task_brat_przeciw_bratu = "jaskier_task_brat_przeciw_bratu.png"
jaskier_task_na_twe_rozkazy = "jaskier_task_na_twe_rozkazy.png"
jaskier_task_bardzo_cenny_ladunek = "jaskier_task_bardzo_cenny_ladunek.png"
jaskier_task_zwiad_na_poludniu = "jaskier_task_zwiad_na_poludniu.png"
jaskier_task_plomien_rozgryzie_malowane_dzieje = "jaskier_task_plomien_rozgryzie_malowane_dzieje.png"
jaskier_task_do_upadlego = "jaskier_task_do_upadlego.png"
jaskier_task_drugie_przyjscie_lilith = "jaskier_task_drugie_przyjscie_lilith.png"
jaskier_task_ksiazece_klejnoty = "jaskier_task_ksiazece_klejnoty.png"
jaskier_task_szpieg_w_mariborze = "jaskier_task_szpieg_w_mariborze.png"
jaskier_task_krew_w_dolinie_kwiatow = "jaskier_task_krew_w_dolinie_kwiatow.png"
jaskier_task_tajemnicze_pozary = "jaskier_task_tajemnicze_pozary.png"


jaskier_task = jaskier_task_zwiad_na_poludniu

jaskier_tasks = {
     "My Naród Oxenturtu": jaskier_task_my_narod_oxenturtu,
     "Głos Rozsądku": jaskier_task_glos_rozsadku,
     "Dar Języków": jaskier_task_dar_jezykow,
     "Szalony Kapłan": jaskier_task_szalony_kaplan,
     "Porozumienie na Belletynie": jaskier_task_porozumienie_na_belletynie,
     "Brat Przeciw Bratu": jaskier_task_brat_przeciw_bratu,
     "Na Twe Rozkazy": jaskier_task_na_twe_rozkazy,
     "Bardzo Cenny Ładunek": jaskier_task_bardzo_cenny_ladunek,
     "Zwiad na Południu": jaskier_task_zwiad_na_poludniu,
     "Płomień Rozgryzie Malowane Dzieje": jaskier_task_plomien_rozgryzie_malowane_dzieje,
     "Do Upadłego": jaskier_task_do_upadlego,
     "Drugie Przyjście Lilith": jaskier_task_drugie_przyjscie_lilith,
     "Książęce Klejnoty": jaskier_task_ksiazece_klejnoty,
     "Szpieg w Mariborze": jaskier_task_szpieg_w_mariborze,
     "Krew w Dolinie Kwiatów": jaskier_task_krew_w_dolinie_kwiatow,
     "Tajemnicze Pożary": jaskier_task_tajemnicze_pozary
}


wyzima_small = "wyzima_small.png"



def prepare_game():
    wait_and_click(play_offline)
    wait_and_click(new_game)
       
    wait_and_click(disable_geralt)
    wait_and_click(disable_triss)
    wait_and_click(disable_yarpen)

    wait_and_click(one_game)

    wait_and_click(start_game)
    wait_and_click(turn_for_jaskier)

def exit_the_game():
    wait_and_click(menu_button)
    wait_and_click(exit_button)

jaskier_task_similar = Pattern(jaskier_task).similar(0.7)

def is_jaskier_task_visible():
    return exists(jaskier_task_similar, 2)

def keep_restarting_the_game_until_you_get_the_right_mission():
    while True:
        prepare_game()
        if is_jaskier_task_visible():
            return
        else:
            wait_and_click(main_task_title)
            exit_the_game()

def perform_sing():
    wait_and_click(sing_action)
    wait_and_click(sing_confirmation_ok)

def finalize_turn():
    return

def finish_a_game_as_jaskier():
    keep_restarting_the_game_until_you_get_the_right_mission();

def zoom(direction, scroll_count=1):
    center = getROI().getCenter()
    
    for i in range(scroll_count):
        wheel(center, direction, 20)
        if i < scroll_count - 1:
            wait(0.25)

def zoom_out(scroll_count):
    zoom(WHEEL_DOWN, scroll_count)

def zoom_in(scroll_count):
    zoom(WHEEL_UP, scroll_count)

direction_map = {
    "N": (0, -1),
    "S": (0, 1),
    "W": (-1, 0),
    "E": (1, 0),
    "NE": (1, -1),
    "NW": (-1, -1),
    "SE": (1, 1),
    "SW": (-1, 1)
}

def moveCamera(distance, direction): 
    dx, dy = direction_map[direction]
    center = getROI().getCenter()
   
    dragDrop(center, Location(center.x + (dx * distance), center.y - (dy * distance)))

def moveCameraUntilImageFound(distance, direction, target_image, max_tries=10):
    for _ in range(max_tries):
        moveCamera(distance, direction)
        wait(1)
        if exists(target_image):
            print("Target image found!")
            return
    raise Exception("Target image not found after {} tries.".format(max_tries))



moveCameraUntilImageFound(500, "SW","1698606598326.png")

# exit_the_game()
# prepare_game()