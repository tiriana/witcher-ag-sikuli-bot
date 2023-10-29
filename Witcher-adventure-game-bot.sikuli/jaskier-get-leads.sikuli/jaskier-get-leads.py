import time

import org.sikuli.basics.Settings;

Settings.MoveMouseDelay = 0.1
Settings.DelayValue = 0.1
Settings.DelayBeforeMouseDown = 0.1
Settings.ClickDelay = 0.1
Settings.TypeDelay = 0.05
Settings.WaitScanRate = 5
Settings.ObserveScanRate = 5

wait_and_click = lambda image_path: (wait(image_path, 10), click(image_path))

setROI(Region(1768,282,1583,892))

play_offlie = "play_offlie.png"
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

def play_as_jaskier_to_get_a_lead(lead_color):
    wait_and_click(play_offlie)
    wait_and_click(new_game)
       
    wait_and_click(disable_geralt)
    wait_and_click(disable_triss)
    wait_and_click(disable_yarpen)

    wait_and_click(start_game)
    wait_and_click(turn_for_jaskier)
    wait_and_click(main_task_title)
    
    wait_and_click(trip_icon)
    wait_and_click(novigrad_destination)
    wait(0.33)
    wait_and_click(confirm_trip)
    wait_and_click(lead_color)
    wait_and_click(menu_button)
    wait_and_click(exit_button)

play_as_jaskier_to_get_red_lead = lambda: play_as_jaskier_to_get_a_lead("red_lead.png")
play_as_jaskier_to_get_blue_lead = lambda: play_as_jaskier_to_get_a_lead("blue_lead.png")
play_as_jaskier_to_get_purple_lead = lambda: play_as_jaskier_to_get_a_lead("purple_lead.png")

for _ in range(1000-463):
    play_as_jaskier_to_get_purple_lead()

for _ in range(1000-595):
    play_as_jaskier_to_get_blue_lead()



