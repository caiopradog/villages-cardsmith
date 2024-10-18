from card import Card
from card_builder import CardBuilder
from base_cards import base_cards


if __name__ == '__main__':
    cards_to_build = []
    for card in base_cards[-2:]:
        all_colors = sum([card['colors']], card['alt_colors'])
        for color in all_colors:
            color2 = None
            if type(color) is not str:
                color, color2 = color
            cards_to_build.append(Card(
                type=card['type'],
                unit=card['unit'],
                name=card['name'],
                color=color,
                color2=color2,
                power=card['power'],
                gold=card['gold'],
                exp_icon=card['exp_icon'],
                ability=card['ability'],
                is_alt=color in card['alt_colors'],
                gender=card['gender'],
            ))

    to_print = True
    for card in cards_to_build:
        try:
            cardBuilder = CardBuilder(card)
            cardBuilder.build()
            if not to_print:
                cardBuilder.crop_to_play()
            cardBuilder.save_img()
        except Exception as error:
            print('Error in card', card.name)
            print(error)
