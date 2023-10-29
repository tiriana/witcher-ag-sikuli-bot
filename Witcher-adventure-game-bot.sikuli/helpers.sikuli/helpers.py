def wait_and_click(image_path, timeout=10, delay_after_wait=1):
    wait(image_path, timeout)
    click(image_path)

def export():
    global wait_and_click