# External libraries:
import os 


class LessonPlan:

    ID: int = 0

    def __init__(self):

        # Week:
        self.week_num: int = None

        # Filename attributes:
        self.filename_source: str = None
        self.filepath_source: str = None
        self.filename_copy: str = None
        self.filepath_copy: str = None

        # Updating ID
        self.ID += 1

    def update_week_num(self):
        prev_week_num: int = 0
        for week_num in range(1, 24):
            if str(week_num) in self.filename_source:
                prev_week_num: int = week_num
        week_num: int = prev_week_num
        self.week_num: int = week_num
