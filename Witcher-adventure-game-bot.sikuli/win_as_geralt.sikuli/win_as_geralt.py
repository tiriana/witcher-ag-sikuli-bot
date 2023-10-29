import org.sikuli.basics.Settings;

Settings.MoveMouseDelay = 0.1
Settings.DelayValue = 0.1
Settings.DelayBeforeMouseDown = 0.1
Settings.ClickDelay = 0.1
Settings.TypeDelay = 0.05
Settings.WaitScanRate = 5
Settings.ObserveScanRate = 5

wait_and_click = lambda image_path: (wait(image_path, 10), click(image_path))
c=wait_and_click
click_fallback = lambda main_image, fallback_image: (click(main_image), True) if exists(main_image) else (click(fallback_image), False)

# Function to double-click images as long as at least one of them exists, with a limit of 20 attempts
def double_click_images_while_one_exists(image_paths, second_image):
    attempts = 0  # Counter for the number of double-click attempts
    while True:
        if exists(second_image):
            return  # If the second image exists, return early
        clicked = False  # Flag to track if any image was clicked in the current iteration
        for image_path in image_paths:
            if exists(image_path):
                doubleClick(image_path)
                clicked = True
        if not clicked:
            break  # Exit the loop if none of the images were clicked
        attempts += 1
        if attempts >= 20:
            raise Exception("Maximum number of double-click attempts reached")

def click_priority(image_paths):
    for i, image_path in enumerate(image_paths):
        if exists(image_path, 0.2):
            click(image_path)
            return i
    return -1

setROI(Region(1768,282,1583,892))

play_offline = "play_offlie-1.png"
new_game = "new_game-1.png"
disable_icon = "disable_icon-1.png"

disable_geralt = "disable_geralt-1.png"
disable_jaskier = "disable_jaskier-1.png"
disable_triss = "disable_triss-1.png"
disable_yarpen = "disable_yarpen-1.png"


start_game = "start_game-1.png"
main_task_title = "main_task_title-1.png"
trip_icon = "trip_icon-1.png"
geralt_develop_icon = "develop_icon.png"
novigrad_destination = "novigrad_destination-1.png"
confirm_trip = "1698581903377-1.png"
red_lead = "red_lead.png"
blue_lead = "blue_lead-1.png"
purple_lead = "purple_lead.png"
sing_action = "sing_action-1.png"
sing_confirmation_ok = "sing_confirmation_ok-1.png"
menu_button = "menu_button-1.png"
exit_button = "exit_button-1.png"

turn_for_jaskier = "turn_for_jaskier-1.png"
turn_for_geralt = "turn_for_geralt.png"
one_game = "one_game.png"

small_task_handle = "small_task_handle.png"

ard_carraigh = "ard_carraigh.png"

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

def spiral_search_for_element(target_image, distance=150):
    if exists(target_image):
        return True
    directions = ["N", "E", "S", "W"]
    moves = 1
    while moves <= 10:  # Adjust the max moves based on your board size
        for direction in directions:
            for _ in range(moves):
                moveCamera(distance, direction)
                if exists(target_image):
                    return True
            # After completing one direction (e.g., North), expand the moves for East, South, West
            if direction == "N":
                moves += 1
    return False


def prepare_game():
    wait_and_click(play_offline)
    wait_and_click(new_game)
       
    wait_and_click(disable_jaskier)
    wait_and_click(disable_triss)
    wait_and_click(disable_yarpen)

    wait_and_click(one_game)

    wait_and_click(start_game)
    wait_and_click(turn_for_geralt)

def choose_quest():
    return click_fallback(small_task_handle, main_task_title)
        

def exit_the_game():
    wait_and_click(menu_button)
    wait_and_click(exit_button)

def find_on_the_map(item):
   spiral_search_for_element(item)
   
def go_to(dest):
    c(trip_icon)
    find_on_the_map(dest)
    c(dest)
    wait(1)
    c(confirm_trip)

def go_to_ard_carraigh():
    go_to(ard_carraigh) 

def go_to_shaerrawedd():
    go_to("1698613660933.png")

def go_to_vengerberg():
    go_to("1698614948541.png")
def go_to_rivia():
    go_to("1698615870002.png")
def go_to_mahakam():
    go_to("1698616326363.png")

def choose_development_card():
    click_priority(["1698615028345.png", "1698612419557.png", "1698615049844.png", "1698612428376.png", "1698613714104.png", "1698613720623.png", "1698615956434.png", "1698615965563.png", "1698616023380.png"])

def develop():
    c(geralt_develop_icon)  
    c("1698612200868.png")
    choose_development_card()

roll_the_dice = "1698612633634.png"

def throw_dice():
    c(roll_the_dice)

shield_white = "shield_dice.png"
shield_red = "shield_red.png"
sword_white = "sword_white.png"
sword_red = "sword_red.png"
parry_red = "parry_red.png"
magic_red = "magic_red.png"
end_of_fight = "end_of_fight.png"
your_results = "1698613194851.png"

def put_dice():
    double_click_images_while_one_exists([shield_white, sword_white, sword_red, shield_red], end_of_fight)

aftermath_you_received_one_bad_faith = "1698613288475.png"
aftermath_you_received_one_regular_wound = "aftermath_you_received_one_regular_wound.png"
aftermath_you_received_one_poisoned_wound = "aftermath_you_received_one_poisoned_wound.png"

aftermath_ok_btn = "1698613304745.png"

mistura_glowing_empty = "1698613325908.png"
bad_faith_confirm = "1698613354096.png"
mikstura_glowing_with_bad_faith = "mikstura_glowing_with_bad_faith.png"
investigation_glowing = "investigation_glowing.png"



def put_wound():
    click_priority([mistura_glowing_empty, mikstura_glowing_with_bad_faith, investigation_glowing])

def deal_with_aftermath():
    if exists(end_turn_btn):
        return
    if exists(aftermath_you_received_one_bad_faith):
        c(aftermath_ok_btn)
        c(mistura_glowing_empty)
        c(bad_faith_confirm)
    if exists(aftermath_you_received_one_regular_wound):
        c(aftermath_ok_btn)
        put_wound()
        c(bad_faith_confirm)
    if exists(aftermath_you_received_one_poisoned_wound):
        c(aftermath_ok_btn)
        put_wound()
        c(bad_faith_confirm)

end_turn_btn = "1698613376597.png"

def end_turn():
    c(end_turn_btn)
    if exists(turn_for_geralt):
        click(turn_for_geralt)

def choose_the_only_enemy():
    click_center()

def click_center():
    click(getROI().getCenter()) # choose random enemy

def attempt_throw_dice(max_attempts=3, wait_time=1):
    for i in range(max_attempts):
        throw_dice()
        sleep(wait_time)  # Wait for the specified time
        if exists(your_results):
            break

medallion_red = "medation_red.png"
inventory_opener = "inventory_opener.png"

def use_witcher_medallion():
    while exists(medallion_red):
        c(inventory_opener)
        c("1698617300074.png")
        sleep(1)


def fight():
    attempt_throw_dice()
    put_dice()
    use_witcher_medalion()
    c(end_of_fight)

bad_faith_ribbon = "1698615114471.png";

def play_bad_faith():
    c(bad_faith_ribbon)
    if exists(roll_the_dice):
        fight()
    

def play_obstacles():
    if exists(end_turn_btn):
        return
    
    c("1698612502344.png")

    if exists(bad_faith_ribbon):
        play_bad_faith()
    else:
        choose_the_only_enemy()
        if exists(roll_the_dice):
            fight()
        
    deal_with_aftermath()

def turn1():
    go_to_ard_carraigh()
    c(red_lead)
    develop()
    play_obstacles()
    end_turn()

def turn2():
    go_to_shaerrawedd()
    develop()
    play_obstacles()
    end_turn()

def turn3():
    go_to_vengerberg()
    develop()
    play_obstacles()
    end_turn()

def turn4():
    go_to_rivia()
    develop()
    play_obstacles()
    end_turn()

def turn5():
    go_to_mahakam()
    develop()
    play_obstacles()
    end_turn()

def do_the_quest():
    turn1()
    turn2()
    turn3()
    turn4()
    turn5()

    turn4()

    turn5()

    turn4()
    pass

def win_as_geralt():
    prepare_game()
    if choose_quest():
        do_the_quest()
    else:
        exit_the_game()
        win_as_geralt()



win_as_geralt()




