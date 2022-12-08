
class Teacher:

    def __init__(self):

        # General information:
        self.name: str = None
        self.class_id: str = None

        # Lesson plans container:
        self.lp_list: dict = {'UOI': [], 'English': []}

        # Teacher-specific lesson plan folders:
        self.lp_uoi_folder_path: str = None
        self.lp_esl_folder_path: str = None
