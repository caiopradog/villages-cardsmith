import os.path
from card import TYPE
from PIL import Image, ImageDraw, ImageFont


def get_image_from_source(img):
    return f'base_images/{img}.png'


def load_image(img):
    path = get_image_from_source(img)
    return Image.open(path)


def load_font(pixels):
    points = pixels * 1.333
    return ImageFont.truetype('fonts/super_digitext_plus.woff', size=points)


class CardBuilder:
    def __init__(self, card):
        self.card = card
        self.img = load_image(self.card.get_card_template())
        self.file_ext = 'jpg'

    def save_img(self):
        path = f'created_images/{self.file_ext}'
        if not os.path.exists(path):
            os.makedirs(path)
        if self.file_ext == 'jpg':
            self.img = self.img.convert('RGB')
        self.img.save(f'{path}/{self.card.get_file_name()}.{self.file_ext}')

    def write_text(self, text, font_size, x, y, fill='black', anchor='ms'):
        font = load_font(font_size)
        draw = ImageDraw.Draw(self.img)
        draw.text((x, y), text, fill, font, anchor=anchor)

    def write_name(self):
        name = self.card.name
        font_size = min(78 - len(name)*2, 66)
        self.write_text(name, font_size, 418, 192, fill=self.card.get_text_fill_color())

    def write_gold(self):
        x = 228 if self.card.type == TYPE.MONSTER else 198
        color = 'white' if self.card.type == TYPE.MONSTER else 'rgba(142, 120, 43, 1)'
        self.write_text(self.card.get_gold_text(), 24, x, 965, color)

    def write_power(self):
        color = 'white' if self.card.type == TYPE.MONSTER else 'rgba(150, 53, 53, 1)'
        self.write_text('Força', 24, 198, 883, color)

    def write_ability(self):
        color = 'white' if self.card.type == TYPE.MONSTER else 'black'
        ability_lines = self.card.get_ability_lines()
        for (idx, line) in enumerate(ability_lines):
            self.write_text(line, 24, 413, 681 + (30 * idx), color)

    def write_transparent_text(self, text, font, color, xy, anchor, rotation=0):
        rotated_img = self.img.rotate(rotation, expand=True)
        text_img = Image.new('RGBA', rotated_img.size, (255, 255, 255, 0))
        text_draw = ImageDraw.Draw(text_img)
        text_draw.text(xy, text, font=font, fill=color, anchor=anchor)
        final_rotation = text_img.rotate(360 - rotation, expand=True)
        self.img = Image.alpha_composite(self.img, final_rotation)

    def write_side_names(self):
        text = self.card.get_side_text()
        color = self.card.get_side_text_color()
        font = load_font(24)
        (_, _, text_width, _) = font.getbbox(text)
        img_width, img_height = self.img.size
        self.write_transparent_text(text, font, color, (img_height - text_width - 120, 100), anchor='ls', rotation=90)
        self.write_transparent_text(text, font, color, (img_height - 120, 100), anchor='rs', rotation=270)

    def write_copyright(self):
        color = self.card.get_side_text_color()
        font = load_font(18)
        self.write_transparent_text('\u00A9 Fridgecrisis Games', font, color, (413, 1035), 'ms')

    def draw_image(self, image, x, y, center=False):
        unit_icon = load_image(image)
        ui_width, ui_height = unit_icon.size
        xpos = x
        ypos = y
        if center:
            xpos = x - round(ui_width / 2)
            ypos = y - round(ui_height / 2)
        self.img.paste(unit_icon, (xpos, ypos), unit_icon)

    def draw_unit_icon(self):
        self.draw_image(self.card.get_unit_icon(), 413, 442, center=True)

    def draw_exp_icon(self):
        self.draw_image(self.card.get_exp_icon(), 720, 121)

    def draw_powers(self):
        power_icons = self.card.get_power_icons()
        start_x = 258 if self.card.type == TYPE.MONSTER else 262
        y = 826 if self.card.type == TYPE.MONSTER else 830
        for (idx, icon) in enumerate(power_icons):
            x = start_x + idx * 86
            self.draw_image(icon, x, y)
        self.write_power()

    def draw_gold(self):
        gold = self.card.gold
        start_x = 344 if self.card.type == TYPE.MONSTER else 262
        y = 911 if self.card.type == TYPE.MONSTER else 915
        for idx in range(gold):
            x = start_x + idx * 86
            self.draw_image(self.card.get_gold_icon(), x, y)
        self.write_gold()

    def hide_gold_bar(self):
        draw = ImageDraw.Draw(self.img)
        x = 125
        y = 925
        width = 575
        height = 75
        draw.rectangle((x, y, x + width, y + height), 'white')

    def crop_to_play(self):
        final_size = (745, 1045)
        delta_w = self.img.width - final_size[0]
        delta_h = self.img.height - final_size[1]
        cropbox = (delta_w / 2, delta_h / 2, final_size[0] + delta_w / 2, final_size[1] + delta_h / 2)
        cropped_img = self.img.crop(cropbox)

        mask = Image.new(mode="L", size=cropped_img.size, color=0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, final_size[0], final_size[1]), radius=35, fill=255)

        cropped_img.putalpha(mask)
        self.img = cropped_img
        self.file_ext = 'png'

    def write_all_texts(self):
        self.write_name()
        self.write_text(self.card.get_type_text(), 24, 413, 226, fill=self.card.get_text_fill_color())
        self.write_ability()
        self.write_side_names()
        self.write_copyright()

    def draw_all_images(self):
        self.draw_unit_icon()
        self.draw_exp_icon()
        if self.card.type not in [TYPE.SCORE]:
            self.draw_gold()
        else:
            self.hide_gold_bar()
        if self.card.type in [TYPE.MONSTER, TYPE.UNIT]:
            self.draw_powers()

    def build(self):
        self.draw_all_images()
        self.write_all_texts()
