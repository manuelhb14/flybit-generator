from PIL import Image
import random
import os

## read image list from a directory
def read_images(path):
    images = []
    for file in os.listdir(path):
        if file.endswith(".png"):
            images.append(file)
    return images

background_list = read_images("./assets/background/")
wings_list = read_images("./assets/wings/")
body_list = read_images("./assets/body/")
shoes_list = read_images("./assets/shoes/")
clothes_list = read_images("./assets/clothes/")
clock_list = read_images("./assets/clock/")
earrings_list = read_images("./assets/earring/")
head_list = read_images("./assets/head/")
purse_list = read_images("./assets/purse/")
eyes_list = read_images("./assets/eyes/")
mouth_list = read_images("./assets/mouth/")
effects_list = read_images("./assets/effects/")

clothes_no_shoes_no_clock_list = read_images("./assets/clothes/noShoes_noClock/")
clothes_shoes_no_clock_list = read_images("./assets/clothes/shoes_noClock/")
clothes_purse_list = read_images("./assets/clothes/purse/")

head_hoodies_list = read_images("./assets/head/hoodies/")
head_special_list = read_images("./assets/head/special/")
head_bucket_hats_list = read_images("./assets/head/bucket_hats/")

eyes_special_list = read_images("./assets/eyes/special/")
eyes_fire_list = read_images("./assets/eyes/fire/")

## create a new image
def create_image(background, wings, body, shoes, clothes, clock, earrings, head, purse, eyes, mouth, effects, filename="output.png"):
    background = Image.open("./assets/background/" + background)
    wings = Image.open("./assets/wings/" +  wings)
    body = Image.open("./assets/body/" + body)
    shoes = Image.open("./assets/shoes/" + shoes)
    clothes = Image.open("./assets/clothes/" + clothes)
    clock = Image.open("./assets/clock/" + clock)
    earrings = Image.open("./assets/earring/" + earrings)
    head = Image.open("./assets/head/" + head)
    purse = Image.open("./assets/purse/" + purse)
    eyes = Image.open("./assets/eyes/" + eyes)
    mouth = Image.open("./assets/mouth/" + mouth)
    effects = Image.open("./assets/effects/" + effects)
    image = Image.new("RGBA", (background.width, background.height))
    image.paste(background, (0, 0), background)
    image.paste(wings, (0, 0), wings)
    image.paste(body, (0, 0), body)
    image.paste(shoes, (0, 0), shoes)
    image.paste(clothes, (0, 0), clothes)
    image.paste(clock, (0, 0), clock)
    image.paste(earrings, (0, 0), earrings)
    image.paste(purse, (0, 0), purse)
    image.paste(eyes, (0, 0), eyes)
    image.paste(head, (0, 0), head)
    image.paste(mouth, (0, 0), mouth)
    image.paste(effects, (0, 0), effects)
    image.save(filename)

## create a new image
def create_special_image(background, wings, body, shoes, clothes, clock, earrings, head, purse, eyes, mouth, effects, filename="output.png"):
    background = Image.open("./assets/background/" + background)
    wings = Image.open("./assets/wings/" +  wings)
    body = Image.open("./assets/body/" + body)
    shoes = Image.open("./assets/shoes/" + shoes)
    clothes = Image.open("./assets/clothes/" + clothes)
    clock = Image.open("./assets/clock/" + clock)
    earrings = Image.open("./assets/earring/" + earrings)
    head = Image.open("./assets/head/" + head)
    purse = Image.open("./assets/purse/" + purse)
    eyes = Image.open("./assets/eyes/" + eyes)
    mouth = Image.open("./assets/mouth/" + mouth)
    effects = Image.open("./assets/effects/" + effects)
    image = Image.new("RGBA", (background.width, background.height))
    image.paste(background, (0, 0), background)
    image.paste(wings, (0, 0), wings)
    image.paste(body, (0, 0), body)
    image.paste(shoes, (0, 0), shoes)
    image.paste(clothes, (0, 0), clothes)
    image.paste(clock, (0, 0), clock)
    image.paste(earrings, (0, 0), earrings)
    image.paste(purse, (0, 0), purse)
    image.paste(head, (0, 0), head)
    image.paste(eyes, (0, 0), eyes)
    image.paste(mouth, (0, 0), mouth)
    image.paste(effects, (0, 0), effects)
    image.save(filename)

def random_image(list):
    return random.choice(list)


def main(filename="output.png"):
    background = random_image(background_list)
    wings = random_image(wings_list)
    body = random_image(body_list)
    shoes = random_image(shoes_list)
    clothes = random_image(clothes_list)
    clock = random_image(clock_list)
    earrings = random_image(earrings_list)
    head = random_image(head_list)
    purse = random_image(purse_list)
    eyes = random_image(eyes_list)
    mouth = random_image(mouth_list)
    effects = random_image(effects_list)

    # print("Background: ", background)
    # print("Wings: ", wings)
    # print("Body: ", body)
    # print("Shoes: ", shoes)
    # print("Clothes: ", clothes)
    # print("Clock: ", clock)
    # print("Earrings: ", earrings)
    # print("Head: ", head)
    # print("Purse: ", purse)
    # print("Eyes: ", eyes)
    # print("Mouth: ", mouth)
    # print("Effects: ", effects, "\n\n")

    if head in head_hoodies_list:
        while eyes in eyes_special_list:
            eyes = random_image(eyes_list)
        clothes = "HOODIE {}.png".format(head.split(" ")[1][:-4]) # change from fixed length to dynamic length
    elif head in head_bucket_hats_list:
        while eyes in eyes_fire_list:
            eyes = random_image(eyes_list)

    if body == "fat.png":
        clothes = "None.png"
        purse = "None.png"
    
    if clothes in clothes_no_shoes_no_clock_list:
        clock = "None.png"
        shoes = "None.png"
    elif clothes in clothes_shoes_no_clock_list:
        clock = "None.png"

    if clothes not in clothes_purse_list:
        purse = "None.png"

    # print("Background: ", background)
    # print("Wings: ", wings)
    # print("Body: ", body)
    # print("Shoes: ", shoes)
    # print("Clothes: ", clothes)
    # print("Clock: ", clock)
    # print("Earrings: ", earrings)
    # print("Head: ", head)
    # print("Purse: ", purse)
    # print("Eyes: ", eyes)
    # print("Mouth: ", mouth)
    # print("Effects: ", effects)
    if eyes in eyes_fire_list:
        create_special_image(background, wings, body, shoes, clothes, clock, earrings, head, purse, eyes, mouth, effects, filename)
    else:
        create_image(background, wings, body, shoes, clothes, clock, earrings, head, purse, eyes, mouth, effects, filename)


if __name__ == "__main__":
    for i in range(100):
        print ("Generating image {}".format(i))
        main(filename="./test/output{}.png".format(i))

    # main(filename="./output10.png")