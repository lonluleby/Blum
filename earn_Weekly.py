import pyautogui
import clickPosition
import foundProgram
import myPublicMethod


earnWeekly_path = "Earn/earn_Weekly.png"
earnOpen_path = "Earn/earn_Open.png"
screen_region = (0, 0, 760, 1300)

earnClaim_path = "Earn/earn_Claim.png"
earnStart_path = "Earn/earn_Start.png"

earnClose1_path = "Earn/earn_Close1.png"


def toDo():
    while True:
        # 做Weekly任务
        result = foundProgram.locate_image_on_screen(earnWeekly_path, 0.9)
        if result:
            clickPosition.click_at_position_offset(result, 0, 200)

            prev_screenshot = myPublicMethod.take_screenshot(screen_region)

            pyautogui.scroll(-400)

            curr_screenshot = myPublicMethod.take_screenshot(screen_region)
            # 计算图像差异
            diff = myPublicMethod.image_diff(prev_screenshot, curr_screenshot)
            if diff < 100:  # 设定一个合理的差异阈值，根据实际情况调整
                print("周常任务全部做完")
                break
            result = foundProgram.locate_image_on_screen(earnOpen_path, 0.9)
            if result:
                clickPosition.click_at_position(result)
                myPublicMethod.click_Start()
                myPublicMethod.staticCheck(screen_region)
                myPublicMethod.click_Claim(screen_region)
                if myPublicMethod.is_existence_toSocial(earnClaim_path, earnStart_path):
                    print("还有任务没做完")
                else:
                    result = foundProgram.locate_image_on_screen(earnClose1_path, 0.99)
                    clickPosition.click_at_position(result)
                    print("任务已经全部做完")






