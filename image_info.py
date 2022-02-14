
class ImageInfo:
    def __init__(self, category = "", title = "", description = "", location = "", article = "") -> None:
        self.category = category
        self.title = title
        self.description = description
        self.location = location
        self.article = article

im_info = {
    # filename : {type, title, comment, article}
    "IMG_6945.jpg" : ImageInfo('w', "title", "description", "location"),
    "IMG_3046.jpg" : ImageInfo('w', "title", "description", "location"),
    "IMG_7512-Edit.jpg" : ImageInfo('w', "title", "description", "location"),
    "IMG_5678.jpg" : ImageInfo('l', "Garibaldi Lake, British Columbia", "", ""),
    "IMG_0187-Edit-person.jpg" : ImageInfo('p bc', "Hiker descending into a cloud inversion", "", "", "a"),
    "IMG_8640.jpg" : ImageInfo('p l bc', "Sunset at Mount Assiniboine", "", "", "a"),
    "IMG_4418.jpg" : ImageInfo('w', "Giant moth with an eye on its wing", "", ""),
    "IMG_7100.jpg" : ImageInfo('l bc', "Helmcken Falls", "", ""),
    "IMG_9612.jpg" : ImageInfo('l bc', "Sunshine pouring through Nairn Falls", "", ""),
    "IMG_8691.jpg" : ImageInfo('l bc', "Moonrise at Mount Assiniboine", "", ""),
    "IMG_7576-2.jpg" : ImageInfo('l bc p', "Looking up from my campsite, Golden Ears Provincial Park", "", ""),
    "IMG_2931.jpg" : ImageInfo('p', "Bubbles frozen in a lake", "", ""),
    "IMG_8981.jpg" : ImageInfo('p', "Ancient Inca terraces near Machu Picchu", "", ""),
    "IMG_8919.jpg" : ImageInfo('p', "Inca ruins near Machu Picchu", "", ""),
    "IMG_8803.jpg" : ImageInfo('p', "Stairs on the Inca Trail", "", ""),
    "IMG_8405.jpg" : ImageInfo('p', "Runkurakay", "", ""),
    "IMG_8357-Edit2.jpg" : ImageInfo('p', "The Inca Trail to Machu Picchu", "", ""),
    "IMG_7830-Edit.jpg" : ImageInfo('p', "A kayak in Lake Louise", "", ""),
    "IMG_7430-Edit.jpg" : ImageInfo('p', "A cloudy day on The Inca Trail", "", ""),
    "IMG_4973-5152_stack.jpg" : ImageInfo('l bc', "Star trails at The Black Tusk", "", ""),
    "IMG_4903.jpg" : ImageInfo('l bc', "Sunset at Panorama Ridge", "", ""),
    "IMG_3993.jpg" : ImageInfo('l p bc', "The wake of the Ferry", "", ""),
    "IMG_3550.jpg" : ImageInfo('p bc', "Tofino, BC", "", ""),
    "IMG_3167.jpg" : ImageInfo('p bc', "A tent at Upper Joffre Lake", "", ""),
    "IMG_3148.jpg" : ImageInfo('p bc', "A kayaker at Upper Joffre Lake", "", ""),
    "IMG_0692-Edit.jpg" : ImageInfo('w', "Anna's Hummingbird", "", ""),
    "IMG_0137.jpg" : ImageInfo('p', "Camp on the Cordillera Huayhuash", "", ""),
    "IMG_0171.jpg" : ImageInfo('l', "Sun breaking through the clouds in the Cordillera Huayhuash", "", ""),
    "IMG_0225.jpg" : ImageInfo('l', "Mountains of the Cordillera Huayhuash", "", ""),
    "IMG_0232.jpg" : ImageInfo('l', "Rondoy, Cordillera Huayhuash", "", ""),
    "DJI_0187.jpg" : ImageInfo('l p', "The Peruvian Desert", "", ""),
    "IMG_9544.jpg" : ImageInfo('w p', "Parrot peeking through its feathers", "", "a"),
    "IMG_9532.jpg" : ImageInfo('w p', "A Blue and Gold Macaw", "", ""),
    "IMG_8262.jpg" : ImageInfo('w', "A Hummingbird Perched on A Branch", "", ""),
    "IMG_8150.jpg" : ImageInfo('w p', "Two Hummingbirds Fighting For Territory", "", ""),
    "IMG_7512-Edit.jpg" : ImageInfo('w p', "A Two-Tailed Hummingbird", "", ""),
    "IMG_6121.jpg" : ImageInfo('w p', "The only bird with a beak longer than its body", "The sword billed hummingbird has the largest beak to body ratio of any bird. I was lucky enough to see this incredible bird at a hummingbird sanctuary in Peru", ""),
    "IMG_0185.jpg" : ImageInfo('l p', "A waterfall in a Mexican canyon", "", ""),
    "IMG_5022.jpg" : ImageInfo('w', "This Hummingbird landed reight in front of me", "", ""),
    "IMG_4196.jpg" : ImageInfo('w p', "Butterflies in the Amazon", "", ""),
    "IMG_0546-Edit.jpg" : ImageInfo('l p', "Rafting down a river in Mexico", "", ""),
    "IMG_2770.jpg" : ImageInfo('l p', "A Raven flying over Howe Sound, BC", "", ""),
    "IMG_2106.jpg" : ImageInfo('w', "A Toucan in the Amazon", "", ""),
    "IMG_1542.jpg" : ImageInfo('l p', "The sand dunes of Huacachina", "", ""),
    "IMG_1449.jpg" : ImageInfo('p', "A small fishing town on the coast of Peru", "", ""),
    "Dji-pano-3.jpg" : ImageInfo('l', "A chain of lakes in the Cordillera Huayhuash", "", ""),
    "IMG_0432.jpg" : ImageInfo('p', "A misty sunrise in the mountains", "", ""),
    "IMG_1386.jpg" : ImageInfo('l p', "Paracas, where the desert meets the ocean", "", ""),
    "IMG_1367.jpg" : ImageInfo('p', "The Paracas National Reserve, Peru", "", ""),
    "IMG_1267.jpg" : ImageInfo('l p', "Lines in the sand, Peru", "", ""),
    "IMG_1193.jpg" : ImageInfo('l p', "Laguna Paron, Peru", "", ""),
    "IMG_883.jpg" : ImageInfo('l', "A cloudy day in the Andes", "", ""),
    "IMG_0848-Edit.jpg" : ImageInfo('p', "A reflection in a puddle", "", ""),
    "IMG_0789.jpg" : ImageInfo('l p', "A river in the sky, Mexico", "", ""),
    "IMG_0623.jpg" : ImageInfo('l p', "The San Antonio Pass, Peru", "", ""),
    "IMG_0753-Pano-Edit.jpg" : ImageInfo('l p', "A 150m high arch over a Mexican river", "", ""),
    "IMG_0395-Pano.jpg" : ImageInfo('l p', "Lakes in the Peruvian Andes", "", ""),
    "IMG_0685.jpg" : ImageInfo('l p', "The mountains of Peru", "", ""),
    "IMG_0355.jpg" : ImageInfo('l p', "Laguna Carhuacocha, Peru", "", ""),
    "IMG_0344.jpg" : ImageInfo('l p', "The rolling hills of Peru", "", ""),
    "IMG_0321.jpg" : ImageInfo('l p', "Two very different neighbouring mountains in Peru", "", ""),
    "IMG_0284-Edit.jpg" : ImageInfo('p', "My camp along the Huayhuash Trek", "", ""),
    "IMG_0240.jpg" : ImageInfo('l p', "Horses roaming the mountains of Peru", "", ""),
    "IMG_0263-Edit.jpg" : ImageInfo('l p', "The 6000m twin peaks of Jirishanca and Mituraju", "", ""),
    "IMG_0067-Pano.jpg" : ImageInfo('l p', "A rainbow mountain in Peru", "", ""),
    "IMG_9698.jpg" : ImageInfo('w', "Lovebirds. Macaws mate for life and can live to be up to 90 years old!", "", ""),
    "IMG_.jpg" : ImageInfo('', "", "", ""),
    "IMG_.jpg" : ImageInfo('', "", "", ""),
    "IMG_.jpg" : ImageInfo('', "", "", ""),
    "IMG_.jpg" : ImageInfo('', "", "", ""),
    "IMG_.jpg" : ImageInfo('', "", "", ""),
    "IMG_.jpg" : ImageInfo('', "", "", "")
    # "IMG_3382.jpg" : ImageInfo('w', "title", "description", "location")
}