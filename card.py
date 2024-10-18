import os.path


class EXPANSION(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    BASE = 'blank'
    BONE = 'bone'
    CARDSMITH = 'cp'
    CRYSTAL_QUEST = 'cq'
    DISTANT_LANDS = 'dl'
    GHOST_TOWN = 'gt'
    HOLIDAY_PACK = 'hp'
    ROYALTY_PACK = 'rp'
    SALT = 'salt'
    SUPER = 'sv'


class TYPE(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    ANIMAL = 'animal'
    UNIT = 'unit'
    MONSTER = 'monster'
    TREASURE = 'treasure'
    BUILDING = 'building'
    SCORE = 'score'


class COLOR(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    YELLOW = 'yellow'
    PURPLE = 'purple'
    ORANGE = 'orange'
    LIGHT = 'light'
    DARK = 'dark'
    GRAY = 'gray'


class Card:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', '')
        self.side_name = kwargs.get('side_name', None)
        self.unit = kwargs.get('unit', '')
        self.type = kwargs.get('type', 'unit')  # unit | animal | building | treasure | monster
        self.color = kwargs.get('color', 'red')  # r|b|g|y|p|o|l|d|gr
        self.color2 = kwargs.get('color2', None)  # r|b|g|y|p|o|d
        self.exp_icon = kwargs.get('exp_icon', 'blank')
        self.ability = kwargs.get('ability', '')
        self.power = min(max(kwargs.get('power', 0), 0), 9)
        self.gold = max(kwargs.get('gold', 0), 0)
        if self.type == TYPE.MONSTER and self.gold > 4:
            self.gold = 4
        self.creator = kwargs.get('creator', 'Caio Gralho')
        self.language = kwargs.get('language', 'Portuguese')
        self.gender = kwargs.get('gender', 'm')  # m|f
        self.is_alt = kwargs.get('is_alt', False) and self.has_alt()

    def get_file_name(self):
        file_name = f'{self.unit}'
        if self.type == TYPE.MONSTER or self.type == TYPE.UNIT:
            file_name = f'{self.get_coloring()}_{file_name}'
        elif self.is_alt:
            file_name = f'alt_{file_name}'
        if self.id:
            file_name += f'_{self.id}'
        return file_name

    def get_coloring(self):
        return f'{self.color}_{self.color2}' if self.is_dual_color() else self.color

    def get_card_template(self):
        if self.type in [TYPE.UNIT, TYPE.MONSTER]:
            template = self.get_coloring()
            template = f'blank_{template}' if self.type == TYPE.UNIT else f'monster_{template}'
        elif self.type in [TYPE.ANIMAL, TYPE.BUILDING]:
            template = 'blank_gray'
        else:
            template = 'treasure'
        return template

    def get_side_text(self):
        name = self.side_name or self.name
        if self.type in [TYPE.UNIT, TYPE.MONSTER]:
            name = f'{name} {self.get_color_text()}'
        return name

    def get_exp_icon(self):
        return f'icon_exp_{self.exp_icon}'

    def get_unit_icon(self):
        icon = f'unit_{self.unit}'
        if self.is_alt:
            alt_icon = f'unit_alt_{self.unit}'
            icon = alt_icon if self.has_alt else icon
        return icon

    def has_alt(self):
        return os.path.exists(f'base_images/unit_alt_{self.unit}.png')

    def get_type_text(self):
        if self.type == TYPE.UNIT:
            return f'Unidade {self.get_color_text('f')}'
        elif self.type == TYPE.MONSTER:
            return f'Monstro {self.get_color_text('m')}'
        elif self.type == TYPE.TREASURE:
            return 'Tesouro'
        elif self.type == TYPE.ANIMAL:
            return 'Animal'
        elif self.type == TYPE.BUILDING:
            return 'Construção'
        return ''

    def genderize_text(self, text, force_gender=None):
        gender = force_gender or self.gender
        article = 'o' if gender == 'm' else 'a'
        return text.replace('$', article)

    def get_color_text(self, force_gender=None):
        colors = {
            COLOR.RED: 'Vermelh$',
            COLOR.BLUE: 'Azul',
            COLOR.GREEN: 'Verde',
            COLOR.ORANGE: 'Laranja',
            COLOR.YELLOW: 'Amarel$',
            COLOR.PURPLE: 'Rox$',
            COLOR.DARK: 'Sombri$',
            COLOR.LIGHT: 'Branc$',
            COLOR.GRAY: 'Cinza',
        }
        color_text = self.genderize_text(colors[self.color], force_gender)
        if self.color2:
            color_text += f'/{self.genderize_text(colors[self.color2], force_gender)}'
        return color_text

    def is_dual_color(self):
        return self.color != COLOR.LIGHT and self.color2 is not None and self.color != self.color2

    def get_text_fill_color(self):
        return 'white' if self.type == TYPE.MONSTER else 'black'

    def get_power_icons(self):
        power5 = 1 if self.power > 6 else 0
        power1s = self.power - (power5*5)
        return sum(
            [[self.get_power_icon(1) for _ in range(power1s)]],
            [self.get_power_icon(5) for _ in range(power5)],
        )

    def get_power_icon(self, level=1):
        power_icon = 'power' if level == 1 else 'power5'
        if self.type == TYPE.MONSTER:
            power_icon += '_whiteborder'
        return 'icon_'+power_icon

    def get_gold_icon(self):
        gold_icon = 'gold'
        if self.type == TYPE.MONSTER:
            gold_icon = 'treasure_whiteborder'
        return 'icon_'+gold_icon

    def get_gold_text(self):
        return 'Tesouro' if self.type == TYPE.MONSTER else 'Ouro'

    def get_ability_lines(self):
        line_limit = 28
        ability_words = self.ability.split(' ')
        ability_lines = []
        line = ''
        for word in ability_words:
            if (len(line) + len(word) - 1) > line_limit or word == '\n':
                ability_lines.append(line[:-1])
                line = ''
            if word != '\n':
                line += f'{word} '
        ability_lines.append(line[:-1])

        return ability_lines if 'score' in self.unit else ability_lines[0:6]

    def get_side_text_color(self):
        color = (0, 0, 0, porc_to_255(.5))
        if self.type == TYPE.TREASURE:
            color = (0, 0, 0, porc_to_255(.4))
        elif self.type in [TYPE.MONSTER, TYPE.UNIT]:
            if self.color == COLOR.YELLOW:
                if self.color2 in [COLOR.RED, COLOR.ORANGE]:
                    color = (0, 0, 0, porc_to_255(.5))
                else:
                    color = (0, 0, 0, porc_to_255(.3))
            elif self.color == COLOR.PURPLE:
                if self.color2 == COLOR.YELLOW:
                    color = (0, 0, 0, porc_to_255(.3))
                elif self.color in [COLOR.RED, COLOR.ORANGE, COLOR.GREEN, COLOR.BLUE]:
                    color = (0, 0, 0, porc_to_255(.5))
                else:
                    color = (0, 0, 0, porc_to_255(.6))
            elif self.color == COLOR.DARK:
                if self.color2 == COLOR.YELLOW:
                    color = (0, 0, 0, porc_to_255(.3))
                elif self.color2 == COLOR.PURPLE:
                    color = (0, 0, 0, porc_to_255(.6))
                elif self.color in [COLOR.RED, COLOR.ORANGE, COLOR.GREEN, COLOR.BLUE]:
                    color = (0, 0, 0, porc_to_255(.5))
                else:
                    color = (255, 255, 255, porc_to_255(.4))
            elif self.color == COLOR.LIGHT:
                color = (0, 0, 0, porc_to_255(.3))

        return color

    def get_side_text_transparency(self):
        color = self.get_side_text_color()
        return color[3]


def porc_to_255(porc):
    return round(255 * porc)
