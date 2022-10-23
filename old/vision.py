import cv2


class Vision:
    @staticmethod
    def draw_rectangles(rectangles: list, screenshot, t_w, t_h):
        line_color = (0, 255, 0)
        line_type = cv2.LINE_4
        detected = False

        src2 = screenshot.copy()
        for loc in rectangles:
            # Determine the box positions
            top_left = loc
            bottom_right = (top_left[0] + t_w, top_left[0] + t_h)
            # Draw the box
            cv2.rectangle(src2, top_left, bottom_right, line_color, line_type)
            detected = True
        return src2, detected
