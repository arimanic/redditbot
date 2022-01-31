
class ImageInfo:
    def __init__(self, category = "", title = "", description = "", location = "") -> None:
        self.category = category
        self.title = title
        self.description = description
        self.location = location

im_info = {
    # filename : {type, title, comment}
    "IMG_6945.jpg" : ImageInfo('w', "title", "description", "location"),
    "IMG_3046.jpg" : ImageInfo('w', "title", "description", "location"),
    "IMG_7512-Edit.jpg" : ImageInfo('w', "title", "description", "location"),
    "IMG_3382.jpg" : ImageInfo('w', "title", "description", "location")
}