from post_template import post_template
# List of subreddits is the keys of this dict

landscape_templates = {
    # "itookapicture" : post_template("ITAP of {title}", "{comment}"),
    # "nocontextpics" : post_template("PIC", "{comment}"),
    # "pics" : post_template("{title}", "{comment}"),
    # "naturepics" : post_template("{title}", "{comment}"),
    # "naturephotography" : post_template("{title}", "{comment}"),
    # "landscapephotography" : post_template("{title} [OC] [{width}x{height}]" , "{comment}"),
    # "casualphoto" : post_template("{title}", "{comment}"),
    # "Images" : post_template("{title}", "{comment}"),
    # "pic" : post_template("{title}", "{comment}"),
    # "travel" : post_template("{title} in {country}", "{comment}"),
    # "campingandhiking" : post_template("{title} in {Location}", "{comment}"),
    "earthporn" : post_template("{title} [OC] [{width}x{height}]", "") # Dont post things with man made objects
}

wildlife_templates = {
    # "itookapicture" : post_template("ITAP of {title}", "{comment}"),
    # "nocontextpics" : post_template( "PIC" , "{comment}"),
    # "pics" : post_template("{title}", "{comment}"),
    # "naturepics" : post_template("{title}", "{comment}"),
    # "naturephotography" : post_template("{title}", "{comment}"),
    # "wildlifephotography" : post_template("{title} [OC] [{width}x{height}]" , "{comment}"),
    # "pic" : post_template("{title}", "{comment}"),
    # "casualphoto" : post_template("{title}", "{comment}"),
    # "Images" : post_template("{title}", "{comment}"),
    "Natureisfuckinglit" : post_template("\N{fire} {title}", "")
}

pic_templates = {
    "itookapicture" : post_template("ITAP of {article} {title}", "{comment}")
    # "pics" : post_template("{title}", "")
}

bc_templates = {
    # "itookapicture" : post_template("ITAP of {title}", "{comment}"),
    "vancouver" : post_template("{title}", "")
}



