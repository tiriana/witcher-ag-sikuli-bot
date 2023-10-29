# play as jaskier to finish the game 

import org.sikuli.basics.Settings;
from org.sikuli.script import Pattern

Settings.MoveMouseDelay = 0.1
Settings.DelayValue = 0.1
Settings.DelayBeforeMouseDown = 0.1
Settings.ClickDelay = 0.1
Settings.TypeDelay = 0.05
Settings.WaitScanRate = 5
Settings.ObserveScanRate = 5

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

jaskier_task = "zwiad_na_poludniu.png"
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


def finish_a_game_as_jaskier():
    keep_restarting_the_game_until_you_get_the_right_mission();


for _ in range(2):
    finish_a_game_as_jaskier()


