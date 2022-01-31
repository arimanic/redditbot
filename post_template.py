# Define a post template. It should contain an image, a subject, and a caption. The subject and caption should be auto generated from the image. It may also contain an optional automated comment to plug my gram
class post_template:

    def __init__(self, description, comment):
        self.desc = description
        self.comm = comment

    def __hash__(self) -> int:
        return hash(self.desc + self.comm)
