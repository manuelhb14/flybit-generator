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
purse_list = read_images("./assets/purse/")
eyes_list = read_images("./assets/eyes/")
mouth_list = read_images("./assets/mouth/")
effects_list = read_images("./assets/effects/")

## create a new image
def create_image(background, wings, body, shoes, clothes, clock, earrings, purse, eyes, mouth, effects):
    background = Image.open("./assets/background/" + background)
    wings = Image.open("./assets/wings/" +  wings)
    body = Image.open("./assets/body/" + body)
    shoes = Image.open("./assets/shoes/" + shoes)
    clothes = Image.open("./assets/clothes/" + clothes)
    clock = Image.open("./assets/clock/" + clock)
    earrings = Image.open("./assets/earring/" + earrings)
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
    image.paste(mouth, (0, 0), mouth)
    image.paste(effects, (0, 0), effects)
    image.save("./output6.png")
    image.show()


def random_image(list):
    return random.choice(list)


def main():
    background = random_image(background_list)
    wings = random_image(wings_list)
    body = random_image(body_list)
    shoes = random_image(shoes_list)
    clothes = random_image(clothes_list)
    clock = random_image(clock_list)
    earrings = random_image(earrings_list)
    purse = random_image(purse_list)
    eyes = random_image(eyes_list)
    mouth = random_image(mouth_list)
    effects = random_image(effects_list)

    create_image(background, wings, body, shoes, clothes, clock, earrings, purse, eyes, mouth, effects)


if __name__ == "__main__":
    main()
